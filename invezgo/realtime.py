"""Real-time WebSocket client (running trade and order book, Elite plan).

Requires the optional extra: ``pip install "invezgo-sdk[ws]"`` (``websockets>=14``).
See https://docs.invezgo.com/api-usage/websocket (beta).
"""

import asyncio
import json
from types import TracebackType
from typing import Any, Dict, List, Literal, Optional, Sequence, Set, Type, Union

from typing_extensions import NotRequired, TypedDict

from ._transport import USER_AGENT
from .exceptions import (
    AuthenticationError,
    InvezgoConnectionError,
    InvezgoError,
    PaymentRequiredError,
    RateLimitError,
    ServerError,
)

DEFAULT_WS_URL = "wss://api.invezgo.com/ws"
MAX_TRADE_CODES = 200
MAX_ORDERBOOK_CODES = 20


class ConnectedMessage(TypedDict):
    type: Literal["connected"]


class SubscribedMessage(TypedDict):
    type: Literal["subscribed"]
    channel: str
    codes: Union[List[str], Literal["*"]]
    min_lot: NotRequired[int]
    min_value: NotRequired[int]


class PongMessage(TypedDict):
    type: Literal["pong"]


class ErrorMessage(TypedDict):
    type: Literal["error"]
    message: str


class LaggedMessage(TypedDict):
    type: Literal["lagged"]
    missed: int


class Trade(TypedDict):
    id: str
    time: str
    code: str
    price: float
    lot: int
    value: int
    change: float
    side: Literal["buy", "sell"]


class TradesMessage(TypedDict):
    type: Literal["trades"]
    ts: int
    data: List[Trade]


class OrderbookMessage(TypedDict):
    type: Literal["orderbook"]
    code: str
    side: Literal["bid", "offer"]
    levels: List[Any]
    seq: Optional[int]


class ReconnectMessage(TypedDict):
    """Emitted by the SDK (not the server) before each reconnect attempt; backfill gaps via REST."""

    type: Literal["reconnect"]
    attempt: int
    delay: float


RealtimeMessage = Union[
    ConnectedMessage, SubscribedMessage, PongMessage, ErrorMessage, LaggedMessage,
    TradesMessage, OrderbookMessage, ReconnectMessage, Dict[str, Any],
]

_END = object()


def _codes(codes: Sequence[str]) -> List[str]:
    if isinstance(codes, str):
        raise TypeError("codes must be a list of strings, not a string")
    return [c.upper() for c in codes]


def _handshake_error(status: int, body: bytes) -> InvezgoError:
    text = body.decode("utf-8", "replace").strip()
    try:
        info = json.loads(text)
        text = str(info.get("message") or text) if isinstance(info, dict) else text
    except ValueError:
        pass
    message = text or f"WebSocket handshake rejected with HTTP {status}"
    if status == 401:
        return AuthenticationError(message, status=status)
    if status == 403:
        return PaymentRequiredError(message, status=status)
    if status == 429:
        return RateLimitError(message, status=status)
    if status >= 500:
        return ServerError(message, status=status)
    return InvezgoError(message, status=status)


class RealtimeClient:
    """WebSocket client for ``wss://api.invezgo.com/ws``.

    Subscriptions made before the server's ``connected`` message are queued, and the desired
    subscription state is replayed after every reconnect.

    Example:
        >>> async with client.realtime() as rt:
        ...     await rt.subscribe_trades(["BBCA", "TLKM"])
        ...     async for msg in rt:
        ...         if msg["type"] == "trades":
        ...             print(msg["data"])

    Args:
        api_key: API key (sent as ``Authorization: Bearer``, never in the URL).
        url: WebSocket URL.
        reconnect: Reconnect automatically with exponential backoff (1, 2, 4, 8, 16, 30 s).
    """

    _backoff: Sequence[float] = (1, 2, 4, 8, 16, 30)

    def __init__(self, api_key: str, *, url: str = DEFAULT_WS_URL, reconnect: bool = True) -> None:
        if not api_key:
            raise ValueError("api_key is required")
        try:
            from websockets.asyncio.client import connect
            from websockets.exceptions import ConnectionClosed, InvalidStatus, WebSocketException
        except ImportError as e:
            raise ImportError(
                'RealtimeClient requires the "websockets" package: pip install "invezgo-sdk[ws]"'
            ) from e
        self._connect = connect
        self._closed_exc: Type[Exception] = ConnectionClosed
        self._status_exc: Type[Exception] = InvalidStatus
        self._ws_exc: Type[Exception] = WebSocketException
        self.api_key = api_key
        self.url = url
        self.reconnect = reconnect
        self._trades: Union[None, Literal["*"], Set[str]] = None
        self._min_lot: Optional[int] = None
        self._min_value: Optional[int] = None
        self._orderbook: Set[str] = set()
        self._ws: Any = None
        self._ready = False
        self._closed = False
        self._task: Optional["asyncio.Task[None]"] = None
        self._queue: "Optional[asyncio.Queue[Any]]" = None

    # ---- lifecycle ----------------------------------------------------------------------

    def _start(self) -> None:
        if self._task is None:
            self._queue = asyncio.Queue()
            self._task = asyncio.get_running_loop().create_task(self._run())

    async def __aenter__(self) -> "RealtimeClient":
        self._start()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    def __aiter__(self) -> "RealtimeClient":
        return self

    async def __anext__(self) -> RealtimeMessage:
        self._start()
        assert self._queue is not None
        item = await self._queue.get()
        if item is _END:
            self._queue.put_nowait(_END)
            raise StopAsyncIteration
        if isinstance(item, BaseException):
            self._queue.put_nowait(_END)
            raise item
        result: RealtimeMessage = item
        return result

    async def close(self) -> None:
        """Close the connection and stop reconnecting; iteration then ends."""
        self._closed = True
        if self._ws is not None:
            await self._ws.close()
        if self._task is not None:
            self._task.cancel()
            await asyncio.gather(self._task, return_exceptions=True)
        if self._queue is not None:
            self._queue.put_nowait(_END)

    async def _run(self) -> None:
        assert self._queue is not None
        attempt = 0
        headers = {"Authorization": f"Bearer {self.api_key}"}
        while not self._closed:
            code: Optional[int] = None
            try:
                async with self._connect(self.url, additional_headers=headers, user_agent_header=USER_AGENT) as ws:
                    self._ws = ws
                    try:
                        async for raw in ws:
                            if await self._handle(ws, raw):
                                attempt = 0
                    except self._closed_exc:
                        pass
                    code = ws.close_code
            except self._status_exc as e:
                status = e.response.status_code  # type: ignore[attr-defined]
                err = _handshake_error(status, e.response.body or b"")  # type: ignore[attr-defined]
                if status in (401, 403) or not self.reconnect:
                    self._queue.put_nowait(err)
                    return
            except (OSError, asyncio.TimeoutError, self._ws_exc) as e:
                if not self.reconnect:
                    self._queue.put_nowait(InvezgoConnectionError(f"Could not reach the Invezgo WebSocket: {e}"))
                    return
            else:
                if code == 4400 or not self.reconnect:  # 4400: invalid client message, retrying won't help
                    break
            finally:
                self._ws = None
                self._ready = False
            if self._closed:
                break
            delay = self._backoff[min(attempt, len(self._backoff) - 1)]
            attempt += 1
            self._queue.put_nowait({"type": "reconnect", "attempt": attempt, "delay": delay})
            await asyncio.sleep(delay)
        self._queue.put_nowait(_END)

    async def _handle(self, ws: Any, raw: Union[str, bytes]) -> bool:
        """Deliver one server frame; returns True on ``connected``."""
        assert self._queue is not None
        try:
            msg = json.loads(raw)
        except ValueError:
            return False
        if not isinstance(msg, dict):
            return False
        connected = msg.get("type") == "connected"
        if connected:
            for payload in self._replay():
                await ws.send(json.dumps(payload))
            self._ready = True
        self._queue.put_nowait(msg)
        return connected

    def _replay(self) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        if self._trades:  # "*" or a non-empty set
            sub: Dict[str, Any] = {"op": "subscribe", "channel": "trades"}
            if self._trades != "*":
                sub["codes"] = sorted(self._trades)
            if self._min_lot is not None:
                sub["min_lot"] = self._min_lot
            if self._min_value is not None:
                sub["min_value"] = self._min_value
            out.append(sub)
        if self._orderbook:
            out.append({"op": "subscribe", "channel": "orderbook", "codes": sorted(self._orderbook)})
        return out

    async def _send(self, payload: Dict[str, Any]) -> None:
        # Before ``connected`` the remembered state is replayed instead.
        if self._ready and self._ws is not None:
            await self._ws.send(json.dumps(payload))

    # ---- public API ---------------------------------------------------------------------

    async def subscribe_trades(
        self,
        codes: Optional[Sequence[str]] = None,
        *,
        min_lot: Optional[int] = None,
        min_value: Optional[int] = None,
    ) -> None:
        """Subscribe to running trades for ``codes`` (all stocks when ``None``), optionally filtered by size."""
        payload: Dict[str, Any] = {"op": "subscribe", "channel": "trades"}
        if codes is None:
            trades: Union[Literal["*"], Set[str]] = "*"
        else:
            upper = _codes(codes)
            trades = self._trades if self._trades == "*" else (self._trades or set()) | set(upper)
            if trades != "*" and len(trades) > MAX_TRADE_CODES:
                raise ValueError(f"At most {MAX_TRADE_CODES} trade codes per connection")
            payload["codes"] = upper
        if min_lot is not None:
            payload["min_lot"] = self._min_lot = min_lot
        if min_value is not None:
            payload["min_value"] = self._min_value = min_value
        self._trades = trades
        await self._send(payload)

    async def subscribe_orderbook(self, codes: Sequence[str]) -> None:
        """Subscribe to the order book of ``codes`` (1 to 20 codes per connection)."""
        upper = _codes(codes)
        if not upper:
            raise ValueError("subscribe_orderbook requires at least one code")
        merged = self._orderbook | set(upper)
        if len(merged) > MAX_ORDERBOOK_CODES:
            raise ValueError(f"At most {MAX_ORDERBOOK_CODES} order book codes per connection")
        self._orderbook = merged
        await self._send({"op": "subscribe", "channel": "orderbook", "codes": upper})

    async def unsubscribe(self, channel: Literal["trades", "orderbook"], codes: Optional[Sequence[str]] = None) -> None:
        """Unsubscribe ``codes`` from ``channel``; without ``codes`` the whole channel (and trade filters)."""
        if channel not in ("trades", "orderbook"):
            raise ValueError('channel must be "trades" or "orderbook"')
        payload: Dict[str, Any] = {"op": "unsubscribe", "channel": channel}
        if codes is None:
            if channel == "trades":
                self._trades = self._min_lot = self._min_value = None
            else:
                self._orderbook = set()
        else:
            upper = _codes(codes)
            payload["codes"] = upper
            if channel == "orderbook":
                self._orderbook -= set(upper)
            elif isinstance(self._trades, set):
                self._trades -= set(upper)
        await self._send(payload)

    async def ping(self) -> None:
        """Send ``{"op":"ping"}``; the server answers with a ``pong`` message."""
        if not self._ready:
            raise InvezgoConnectionError("WebSocket is not connected")
        await self._send({"op": "ping"})


__all__ = [
    "RealtimeClient",
    "RealtimeMessage",
    "ConnectedMessage",
    "SubscribedMessage",
    "PongMessage",
    "ErrorMessage",
    "LaggedMessage",
    "Trade",
    "TradesMessage",
    "OrderbookMessage",
    "ReconnectMessage",
]
