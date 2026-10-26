import json
import unittest
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

import requests
from requests.structures import CaseInsensitiveDict

from invezgo import (
    AuthenticationError,
    BadRequestError,
    CacheOptions,
    InvezgoClient,
    InvezgoConnectionError,
    InvezgoError,
    InvezgoTimeoutError,
    NotFoundError,
    PaymentRequiredError,
    RateLimitError,
    ServerError,
    ValidationError,
)

BASE = "https://api.invezgo.com"


def response(status: int = 200, body: Any = None, headers: Optional[Dict[str, str]] = None,
             raw: Optional[bytes] = None) -> requests.Response:
    r = requests.Response()
    r.status_code = status
    r._content = raw if raw is not None else (b"" if body is None else json.dumps(body).encode())
    r.headers = CaseInsensitiveDict(headers or {})
    r.reason = "Reason"
    return r


class FakeSession(requests.Session):
    """Records calls; replies from a queue (or a default 200 echo)."""

    def __init__(self) -> None:
        super().__init__()
        self.calls: List[Tuple[str, str, Dict[str, str], Optional[bytes]]] = []
        self.queue: List[Any] = []

    def request(  # type: ignore[override]
        self, method: str, url: str, data: Any = None, headers: Any = None, timeout: Any = None, **kw: Any
    ) -> requests.Response:
        self.calls.append((method, url, dict(headers or {}), data))
        if self.queue:
            item = self.queue.pop(0)
            if isinstance(item, Exception):
                raise item
            return item  # type: ignore[no-any-return]
        return response(200, {"n": len(self.calls)})

    def keys_used(self) -> List[str]:
        return [h["Authorization"].split(" ", 1)[1] for _, _, h, _ in self.calls]


class Clock:
    def __init__(self) -> None:
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now


def make(cache: Any = True, keys: Tuple[str, ...] = ()) -> Tuple[InvezgoClient, FakeSession, Clock]:
    session = FakeSession()
    client = InvezgoClient("k1", additional_api_keys=list(keys), cache=cache, session=session)
    clock = Clock()
    client._transport._clock = clock
    if client._transport.cache is not None:
        client._transport.cache._clock = clock
    return client, session, clock


def rate_limited(message: str = "Too many requests: 250 requests per minute", retry_after: str = "30"
                 ) -> requests.Response:
    return response(429, {"statusCode": 429, "message": message, "error": "Too Many Requests"},
                    {"Retry-After": retry_after, "X-RateLimit-Limit": "250", "X-RateLimit-Remaining": "0",
                     "X-RateLimit-Reset": "1700000000"})


class RequestBuildingTest(unittest.TestCase):
    def test_query_is_canonical_and_typed_values_are_formatted(self) -> None:
        client, session, _ = make(cache=False)
        client.analysis.get_top_change(date(2024, 12, 30), filter_value=5.0, filter_column="change")
        self.assertEqual(session.calls[0][1],
                         BASE + "/analysis/top/change?date=2024-12-30&filter_column=change&filter_value=5")

    def test_keyword_escaped_param_and_path_encoding(self) -> None:
        client, session, _ = make(cache=False)
        client.analysis.get_indicator_chart("bdm", "A/B C", from_="2024-01-01", to=date(2024, 2, 1))
        self.assertEqual(session.calls[0][1],
                         BASE + "/analysis/chart/stock/bdm/A%2FB%20C?from=2024-01-01&to=2024-02-01")

    def test_headers_and_body(self) -> None:
        client, session, _ = make(cache=False)
        client.analysis.get_stock_list()
        client.watchlists.add({"group": "g" * 25, "code": "BBCA", "price": 9000, "scope": []})
        get_headers, post = session.calls[0][2], session.calls[1]
        self.assertEqual(get_headers["Authorization"], "Bearer k1")
        self.assertTrue(get_headers["User-Agent"].startswith("invezgo-python-sdk/"))
        self.assertNotIn("Content-Type", get_headers)
        self.assertEqual(post[0], "POST")
        self.assertEqual(post[2]["Content-Type"], "application/json")
        self.assertEqual(json.loads(post[3] or b"")["code"], "BBCA")

    def test_null_and_empty_body_return_none(self) -> None:
        client, session, _ = make(cache=False)
        session.queue = [response(200, raw=b"null"), response(200, raw=b"")]
        self.assertIsNone(client.analysis.get_shareholder_classify_table("BBCA"))
        self.assertIsNone(client.analysis.get_shareholder_classify_table("BBCA"))

    def test_requires_api_key(self) -> None:
        with self.assertRaises(ValueError):
            InvezgoClient("")


class CacheTest(unittest.TestCase):
    def test_get_is_cached_and_hits_are_fresh_objects(self) -> None:
        client, session, _ = make()
        session.queue = [response(200, [{"code": "BBCA"}])]
        first = client.analysis.get_stock_list()
        first[0]["code"] = "MUTATED"
        second = client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 1)
        self.assertEqual(second[0]["code"], "BBCA")

    def test_realtime_tier_uses_short_ttl(self) -> None:
        client, session, clock = make()
        client.analysis.get_order_book("BBCA", "RG")  # realtime tier (5s)
        client.analysis.get_stock_list()  # default tier (60s)
        clock.now += 6
        client.analysis.get_order_book("BBCA", "RG")
        client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 3)
        clock.now += 60
        client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 4)

    def test_disabled_cache_and_none_tier(self) -> None:
        client, session, _ = make(cache=False)
        client.analysis.get_stock_list()
        client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 2)
        client, session, _ = make()
        client.usage.get_api_usage()
        client.usage.get_api_usage()
        self.assertEqual(len(session.calls), 2)

    def test_custom_ttl_zero_disables_tier(self) -> None:
        client, session, _ = make(cache=CacheOptions(realtime_ttl=0))
        client.analysis.get_order_book("BBCA", "RG")
        client.analysis.get_order_book("BBCA", "RG")
        client.analysis.get_stock_list()
        client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 3)

    def test_mutation_purges_personal_segments_only(self) -> None:
        client, session, _ = make()
        client.watchlists.list()
        client.portfolios.list()
        client.analysis.get_stock_list()
        client.journals.add({"code": "BBCA", "broker": "YP", "date": "2024-01-02", "lot": 1, "fee": 0,
                             "price": 9000, "scope": []})
        client.watchlists.list()
        client.portfolios.list()
        client.analysis.get_stock_list()
        paths = [c[1].replace(BASE, "") for c in session.calls]
        self.assertEqual(paths, ["/watchlists", "/portfolios", "/analysis/list/stock", "/journals",
                                 "/watchlists", "/portfolios"])

    def test_clear_cache(self) -> None:
        client, session, _ = make()
        client.analysis.get_stock_list()
        client.clear_cache()
        client.analysis.get_stock_list()
        self.assertEqual(len(session.calls), 2)


class RotationTest(unittest.TestCase):
    def test_minute_limit_rotates_and_blocks_only_that_route(self) -> None:
        client, session, clock = make(cache=False, keys=("k2",))
        session.queue = [rate_limited(retry_after="30")]
        client.analysis.get_stock_list()
        client.analysis.get_stock_list()  # same route: k1 still blocked
        client.analysis.get_broker_list()  # other route: k1 is fine
        clock.now += 31
        client.analysis.get_stock_list()  # block expired: primary preferred again
        self.assertEqual(session.keys_used(), ["k1", "k2", "k2", "k1", "k1"])

    def test_monthly_quota_blocks_whole_key(self) -> None:
        client, session, _ = make(cache=False, keys=("k2", "k2", ""))
        session.queue = [rate_limited("Monthly quota exceeded, resets 2026-11-01", retry_after="86400")]
        client.analysis.get_stock_list()
        client.analysis.get_broker_list()
        self.assertEqual(session.keys_used(), ["k1", "k2", "k2"])

    def test_all_keys_blocked_raises_without_extra_request(self) -> None:
        client, session, clock = make(cache=False, keys=("k2",))
        session.queue = [rate_limited(retry_after="30"), rate_limited(retry_after="10")]
        with self.assertRaises(RateLimitError) as ctx:
            client.analysis.get_stock_list()
        err = ctx.exception
        self.assertEqual((err.status, err.retry_after, err.limit, err.remaining), (429, 10, 250, 0))
        self.assertFalse(err.quota_exceeded)
        self.assertEqual(len(session.calls), 2)
        clock.now += 5
        with self.assertRaises(RateLimitError) as ctx:
            client.analysis.get_stock_list()
        self.assertEqual(ctx.exception.retry_after, 5)
        self.assertEqual(len(session.calls), 2)
        clock.now += 6
        client.analysis.get_stock_list()
        self.assertEqual(session.keys_used()[-1], "k2")

    def test_reset_header_fallback(self) -> None:
        client, session, clock = make(cache=False)
        client._transport._wall_clock = lambda: 1700000000 - 42
        session.queue = [response(429, {"message": "slow down"}, {"X-RateLimit-Reset": "1700000000"})]
        with self.assertRaises(RateLimitError) as ctx:
            client.analysis.get_stock_list()
        self.assertEqual(ctx.exception.retry_after, 42)


class ErrorMappingTest(unittest.TestCase):
    def check(self, status: int, cls: type[InvezgoError], message: Any = "boom") -> InvezgoError:
        client, session, _ = make(cache=False)
        session.queue = [response(status, {"statusCode": status, "message": message, "error": "E",
                                           "requestId": "rid", "path": "/x"})]
        with self.assertRaises(cls) as ctx:
            client.analysis.get_stock_list()
        err = ctx.exception
        self.assertEqual((err.status, err.request_id, err.path, err.error), (status, "rid", "/x", "E"))
        return err

    def test_mapping(self) -> None:
        self.check(401, AuthenticationError)
        self.check(402, PaymentRequiredError)
        self.check(404, NotFoundError)
        self.check(400, BadRequestError)
        self.check(503, ServerError)
        self.check(409, InvezgoError)
        err = self.check(422, ValidationError, ["`code` is required", "`price` too small"])
        self.assertEqual(err.message, "`code` is required; `price` too small")
        self.assertEqual(err.status_code, 422)

    def test_network_errors(self) -> None:
        client, session, _ = make(cache=False)
        session.queue = [requests.exceptions.ConnectTimeout("t"), requests.exceptions.ConnectionError("c")]
        with self.assertRaises(InvezgoTimeoutError):
            client.analysis.get_stock_list()
        with self.assertRaises(InvezgoConnectionError):
            client.analysis.get_stock_list()


if __name__ == "__main__":
    unittest.main()
