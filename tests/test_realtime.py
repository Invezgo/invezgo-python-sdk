import asyncio
import json
import unittest
from http import HTTPStatus
from typing import Any, Awaitable, Callable, Dict, List, Optional

from invezgo import AuthenticationError, InvezgoClient, RealtimeClient

try:
    from websockets.asyncio.server import ServerConnection, serve
except ImportError:  # optional extra not installed
    serve = None  # type: ignore[assignment]

Handler = Callable[[Any, int], Awaitable[None]]


@unittest.skipIf(serve is None, "websockets is not installed")
class RealtimeTest(unittest.IsolatedAsyncioTestCase):
    async def start(self, handler: Handler, reject: Optional[HTTPStatus] = None) -> RealtimeClient:
        """Run a local server; ``handler(ws, n)`` serves the n-th connection (0-based)."""
        self.connections = 0
        self.received: List[List[Dict[str, Any]]] = []
        self.headers: List[Any] = []

        def process_request(conn: Any, request: Any) -> Any:
            self.headers.append(request.headers)
            if reject is not None:
                self.connections += 1
                return conn.respond(reject, "denied\n")
            return None

        async def serve_one(ws: ServerConnection) -> None:
            n = self.connections
            self.connections += 1
            self.received.append([])
            await handler(ws, n)

        self.server = await serve(serve_one, "127.0.0.1", 0, process_request=process_request)
        self.addAsyncCleanup(self.server.wait_closed)
        self.addCleanup(self.server.close)
        port = self.server.sockets[0].getsockname()[1]
        rt = RealtimeClient("KEY", url=f"ws://127.0.0.1:{port}/ws")
        rt._backoff = (0.01,)
        return rt

    async def recv(self, ws: Any, n: int) -> Dict[str, Any]:
        msg: Dict[str, Any] = json.loads(await ws.recv())
        self.received[n].append(msg)
        return msg

    async def collect(self, rt: RealtimeClient, until: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []

        async def run() -> None:
            async for msg in rt:
                out.append(dict(msg))
                if until(out[-1]):
                    return

        await asyncio.wait_for(run(), 5)
        return out

    async def test_queued_subscriptions_replayed_after_connected_and_decoding(self) -> None:
        trades = {"type": "trades", "ts": 1793240653184, "data": [
            {"id": "202610290000255958", "time": "092413", "code": "ISAT", "price": 1465.0, "lot": 9,
             "value": 1318500, "change": -105.0, "side": "buy"}]}
        book = {"type": "orderbook", "code": "BBCA", "side": "bid", "levels": [[9875, 120]], "seq": None}

        async def handler(ws: Any, n: int) -> None:
            await ws.send('{"type":"connected"}')
            await self.recv(ws, n)
            await self.recv(ws, n)
            await ws.send(json.dumps(trades))
            await ws.send(json.dumps(book))
            await ws.send('{"type":"brand_new","x":1}')
            await ws.wait_closed()

        rt = await self.start(handler)
        await rt.subscribe_trades(["bbca", "tlkm"], min_lot=500)
        await rt.subscribe_orderbook(["bbca"])
        async with rt:
            msgs = await self.collect(rt, lambda m: m["type"] == "brand_new")

        self.assertEqual([m["type"] for m in msgs], ["connected", "trades", "orderbook", "brand_new"])
        self.assertEqual(self.received[0], [
            {"op": "subscribe", "channel": "trades", "codes": ["BBCA", "TLKM"], "min_lot": 500},
            {"op": "subscribe", "channel": "orderbook", "codes": ["BBCA"]},
        ])
        self.assertEqual(msgs[1]["data"][0]["id"], "202610290000255958")
        self.assertIsNone(msgs[2]["seq"])
        self.assertEqual(self.headers[0]["Authorization"], "Bearer KEY")
        self.assertTrue(self.headers[0]["User-Agent"].startswith("invezgo-python-sdk/"))
        self.assertNotIn("KEY", rt.url)

    async def test_live_subscribe_after_connected(self) -> None:
        async def handler(ws: Any, n: int) -> None:
            await ws.send('{"type":"connected"}')
            msg = await self.recv(ws, n)
            await ws.send(json.dumps({"type": "subscribed", "channel": msg["channel"], "codes": "*"}))
            await ws.wait_closed()

        rt = await self.start(handler)
        async with rt:
            await self.collect(rt, lambda m: m["type"] == "connected")
            await rt.subscribe_trades()
            msgs = await self.collect(rt, lambda m: m["type"] == "subscribed")
        self.assertEqual(self.received[0], [{"op": "subscribe", "channel": "trades"}])
        self.assertEqual(msgs[-1]["codes"], "*")

    async def test_reconnect_replays_subscriptions(self) -> None:
        async def handler(ws: Any, n: int) -> None:
            await ws.send('{"type":"connected"}')
            await self.recv(ws, n)
            if n == 0:
                await ws.close(1011, "drop")  # network-style drop -> reconnect
            else:
                await ws.send('{"type":"pong"}')
                await ws.wait_closed()

        rt = await self.start(handler)
        await rt.subscribe_orderbook(["BBCA"])
        async with rt:
            msgs = await self.collect(rt, lambda m: m["type"] == "pong")
        self.assertEqual([m["type"] for m in msgs], ["connected", "reconnect", "connected", "pong"])
        self.assertEqual(self.received[0], self.received[1])
        self.assertEqual(self.received[1], [{"op": "subscribe", "channel": "orderbook", "codes": ["BBCA"]}])

    async def test_close_4400_stops_reconnect(self) -> None:
        async def handler(ws: Any, n: int) -> None:
            await ws.send('{"type":"connected"}')
            await ws.send('{"type":"error","message":"unknown op"}')
            await ws.close(4400, "invalid message")

        rt = await self.start(handler)
        async with rt:
            msgs = await asyncio.wait_for(self._all(rt), 5)
        self.assertEqual([m["type"] for m in msgs], ["connected", "error"])
        await asyncio.sleep(0.05)
        self.assertEqual(self.connections, 1)

    async def test_handshake_401_is_fatal(self) -> None:
        async def handler(ws: Any, n: int) -> None:
            pass

        rt = await self.start(handler, reject=HTTPStatus.UNAUTHORIZED)
        async with rt:
            with self.assertRaises(AuthenticationError):
                await asyncio.wait_for(self._all(rt), 5)
        self.assertEqual(self.connections, 1)

    async def _all(self, rt: RealtimeClient) -> List[Dict[str, Any]]:
        return [dict(m) async for m in rt]

    async def test_guards(self) -> None:
        rt = RealtimeClient("KEY")
        with self.assertRaises(ValueError):
            await rt.subscribe_orderbook([])
        with self.assertRaises(ValueError):
            await rt.subscribe_orderbook([f"C{i}" for i in range(21)])
        with self.assertRaises(ValueError):
            await rt.subscribe_trades([f"C{i}" for i in range(201)])
        with self.assertRaises(ValueError):
            await rt.unsubscribe("news")  # type: ignore[arg-type]
        self.assertEqual(rt._replay(), [])

    def test_url_derived_from_client(self) -> None:
        self.assertEqual(InvezgoClient("K").realtime().url, "wss://api.invezgo.com/ws")
        rt = InvezgoClient("K", base_url="http://localhost:3000/").realtime(reconnect=False)
        self.assertEqual((rt.url, rt.api_key, rt.reconnect), ("ws://localhost:3000/ws", "K", False))


if __name__ == "__main__":
    unittest.main()
