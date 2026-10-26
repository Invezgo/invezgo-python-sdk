"""HTTP transport: request building, L1 cache, API key rotation and error mapping."""

import json
import math
import re
import threading
import time
from datetime import date
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Set, Tuple
from urllib.parse import quote, urlencode

import requests

from ._cache import CacheOptions, LRUCache
from ._version import __version__
from .exceptions import (
    AuthenticationError,
    InvezgoConnectionError,
    InvezgoError,
    InvezgoTimeoutError,
    NotFoundError,
    PaymentRequiredError,
    RateLimitError,
    ServerError,
    ValidationError,
)

# Mirrors codegen/ir.py PERSONAL_SEGMENTS: a successful mutation purges these cached paths.
PERSONAL_SEGMENTS = frozenset({"watchlists", "journals", "portfolios", "trades", "alerts", "screener"})
QUOTA_RE = re.compile(r"quota|kuota|monthly|bulanan", re.I)
DEFAULT_BLOCK_SECONDS = 60.0
USER_AGENT = f"invezgo-python-sdk/{__version__}"


def _query_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, date):
        return value.isoformat()[:10]
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def build_key(route: str, path: Optional[Mapping[str, Any]], query: Optional[Mapping[str, Any]]) -> str:
    """Return the canonical ``path?query`` used both as request target and cache key."""
    url = route
    for name, value in (path or {}).items():
        url = url.replace("{" + name + "}", quote(_query_value(value), safe="!~*'()"))
    items = sorted((k, _query_value(v)) for k, v in (query or {}).items() if v is not None)
    return url + ("?" + urlencode(items, quote_via=quote) if items else "")


def _int_header(headers: Mapping[str, str], name: str) -> Optional[int]:
    try:
        return int(headers[name])
    except (KeyError, ValueError, TypeError):
        return None


def _decode(content: bytes) -> Any:
    if not content.strip():
        return None
    return json.loads(content)


class Transport:
    """Sends requests for the generated resource classes. Not part of the public API."""

    def __init__(
        self,
        api_keys: Sequence[str],
        base_url: str,
        timeout: float,
        cache: Optional[CacheOptions],
        session: Optional[requests.Session] = None,
        clock: Callable[[], float] = time.monotonic,
        wall_clock: Callable[[], float] = time.time,
    ) -> None:
        keys: List[str] = []
        for k in api_keys:
            if k and k not in keys:
                keys.append(k)
        if not keys:
            raise ValueError("api_key is required")
        self.keys = keys
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.cache_options = cache
        self.cache = LRUCache(cache.max_entries, cache.max_bytes, clock) if cache else None
        self.session = session or requests.Session()
        self._clock = clock
        self._wall_clock = wall_clock
        self._blocks: Dict[Tuple[int, Optional[str]], Tuple[float, bool]] = {}
        self._lock = threading.Lock()

    # ---- key rotation -------------------------------------------------------------------

    def _blocked_until(self, index: int, route: str, now: float) -> Tuple[float, bool]:
        """Latest block (until, is_quota) affecting this key for this route."""
        best = (0.0, False)
        for scope in (None, route):
            block = self._blocks.get((index, scope))
            if block and block[0] > now and block[0] > best[0]:
                best = block
        return best

    def _pick_key(self, route: str, tried: Set[int]) -> Optional[int]:
        with self._lock:
            now = self._clock()
            for i in range(len(self.keys)):
                if i not in tried and self._blocked_until(i, route, now)[0] <= now:
                    return i
            return None

    def _block(self, index: int, route: str, seconds: float, quota: bool) -> None:
        with self._lock:
            self._blocks[(index, None if quota else route)] = (self._clock() + seconds, quota)

    def _all_blocked_error(self, route: str, last: Optional[RateLimitError]) -> RateLimitError:
        with self._lock:
            now = self._clock()
            blocks = [self._blocked_until(i, route, now) for i in range(len(self.keys))]
        active = [b for b in blocks if b[0] > now]
        wait = min((b[0] for b in active), default=now) - now
        retry_after = max(0, math.ceil(wait))
        if last is not None:
            last.retry_after = retry_after
            return last
        return RateLimitError(
            f"All {len(self.keys)} API key(s) are rate limited; retry in {retry_after}s.",
            retry_after=retry_after,
            quota_exceeded=bool(active) and all(b[1] for b in active),
        )

    # ---- request ------------------------------------------------------------------------

    def request(
        self,
        method: str,
        route: str,
        *,
        path: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        cache: str = "none",
    ) -> Any:
        key = build_key(route, path, query)
        ttl = 0.0
        if self.cache is not None and self.cache_options is not None and method == "GET":
            ttl = {"default": self.cache_options.ttl, "realtime": self.cache_options.realtime_ttl}.get(cache, 0.0)
        if ttl > 0 and self.cache is not None:
            hit = self.cache.get(key)
            if hit is not None:
                return _decode(hit)

        tried: Set[int] = set()
        last_429: Optional[RateLimitError] = None
        while True:
            index = self._pick_key(route, tried)
            if index is None:
                raise self._all_blocked_error(route, last_429)
            tried.add(index)
            resp = self._send(method, key, body, self.keys[index])
            if resp.status_code != 429:
                break
            err = self._error(resp)
            assert isinstance(err, RateLimitError)
            last_429 = err
            self._block(index, route, self._wait_seconds(resp), err.quota_exceeded)

        if not 200 <= resp.status_code < 300:
            raise self._error(resp)
        content = resp.content or b""
        try:
            data = _decode(content)
        except ValueError as e:
            raise InvezgoError(f"Invalid JSON in response: {e}", status=resp.status_code, body=resp.text) from e
        if ttl > 0 and self.cache is not None:
            self.cache.set(key, content, ttl)
        if method != "GET" and self.cache is not None:
            self.cache.delete_where(lambda k: k.split("/")[1].split("?")[0] in PERSONAL_SEGMENTS)
        return data

    def _send(self, method: str, target: str, body: Any, api_key: str) -> requests.Response:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        }
        data = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(body).encode("utf-8")
        try:
            return self.session.request(method, self.base_url + target, data=data, headers=headers,
                                        timeout=self.timeout)
        except requests.exceptions.Timeout as e:
            raise InvezgoTimeoutError(f"Request timed out after {self.timeout}s: {method} {target}") from e
        except requests.exceptions.RequestException as e:
            raise InvezgoConnectionError(f"Could not reach the Invezgo API: {e}") from e

    def _wait_seconds(self, resp: requests.Response) -> float:
        retry_after = _int_header(resp.headers, "Retry-After")
        if retry_after and retry_after > 0:
            return float(retry_after)
        reset = _int_header(resp.headers, "X-RateLimit-Reset")
        if reset:
            wait = reset - self._wall_clock()
            if wait > 0:
                return wait
        return DEFAULT_BLOCK_SECONDS

    def _error(self, resp: requests.Response) -> InvezgoError:
        status = resp.status_code
        try:
            body: Any = _decode(resp.content or b"")
        except ValueError:
            body = resp.text
        info: Dict[str, Any] = body if isinstance(body, dict) else {}
        raw = info.get("message")
        if isinstance(raw, list):
            message = "; ".join(str(m) for m in raw)
        elif raw:
            message = str(raw)
        else:
            message = (body if isinstance(body, str) and body else None) or resp.reason or f"HTTP {status}"
        kwargs: Dict[str, Any] = dict(status=status, error=info.get("error"), request_id=info.get("requestId"),
                                      path=info.get("path"), body=body)
        if status == 429:
            return RateLimitError(
                message,
                retry_after=_int_header(resp.headers, "Retry-After"),
                limit=_int_header(resp.headers, "X-RateLimit-Limit"),
                remaining=_int_header(resp.headers, "X-RateLimit-Remaining"),
                reset=_int_header(resp.headers, "X-RateLimit-Reset"),
                quota_exceeded=bool(QUOTA_RE.search(message)),
                **kwargs,
            )
        cls: type = InvezgoError
        if status in (400, 422):
            cls = ValidationError
        elif status == 401:
            cls = AuthenticationError
        elif status == 402:
            cls = PaymentRequiredError
        elif status == 404:
            cls = NotFoundError
        elif status >= 500:
            cls = ServerError
        err: InvezgoError = cls(message, **kwargs)
        return err
