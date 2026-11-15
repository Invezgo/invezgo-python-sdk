"""Invezgo API client."""

from types import TracebackType
from typing import Optional, Sequence, Type, Union

import requests

from ._cache import CacheOptions
from ._transport import Transport
from .realtime import RealtimeClient
from .resources import ResourcesMixin

DEFAULT_BASE_URL = "https://api.invezgo.com"


class InvezgoClient(ResourcesMixin):
    """Client for the Invezgo API (Indonesia stock market data).

    Args:
        api_key: Primary API key (https://invezgo.com/id/setting/api).
        additional_api_keys: Fallback keys. When a key gets HTTP 429 (per-minute limit or
            monthly quota) the request is retried automatically with the next available key.
        base_url: API base URL.
        timeout: Timeout in seconds per HTTP attempt.
        cache: ``True`` (default) for an in-memory LRU cache with default settings,
            ``False`` to disable it, or a :class:`CacheOptions` instance.
        session: Optional ``requests.Session`` to reuse (proxies, adapters, retries...).
            A session you pass in is not closed by :meth:`close`.

    Example:
        >>> from invezgo import InvezgoClient
        >>> with InvezgoClient("API_KEY", additional_api_keys=["API_KEY_2"]) as client:
        ...     stocks = client.analysis.get_stock_list()
        ...     print(stocks[0]["code"])
    """

    def __init__(
        self,
        api_key: str,
        *,
        additional_api_keys: Sequence[str] = (),
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        cache: Union[bool, CacheOptions] = True,
        session: Optional[requests.Session] = None,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")
        if isinstance(additional_api_keys, str):
            raise TypeError("additional_api_keys must be a list of strings, not a string")
        options = CacheOptions() if cache is True else (cache or None)
        self._owns_session = session is None
        self._transport = Transport([api_key, *additional_api_keys], base_url, timeout, options, session)
        self._init_resources(self._transport)

    def realtime(self, *, reconnect: bool = True) -> RealtimeClient:
        """Create a WebSocket client using this client's primary API key; the URL is derived from
        ``base_url`` (``https`` -> ``wss``, ``http`` -> ``ws``, plus ``/ws``).

        Requires ``pip install "invezgo-sdk[ws]"``. Use with ``async with client.realtime() as rt:``.
        """
        base = self._transport.base_url
        url = "ws" + base[4:] if base.startswith("http") else base  # https->wss, http->ws
        return RealtimeClient(self._transport.keys[0], url=url + "/ws", reconnect=reconnect)

    def clear_cache(self) -> None:
        """Drop every cached response."""
        if self._transport.cache is not None:
            self._transport.cache.clear()

    def close(self) -> None:
        """Close the underlying HTTP session (only when the client created it)."""
        if self._owns_session:
            self._transport.session.close()

    def __enter__(self) -> "InvezgoClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self.close()
