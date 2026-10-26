"""In-memory (L1) LRU cache for raw response bodies."""

import threading
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Optional, Tuple


@dataclass(frozen=True)
class CacheOptions:
    """Cache settings. Pass ``cache=False`` to :class:`InvezgoClient` to disable caching entirely.

    Attributes:
        ttl: Seconds a normal GET response stays fresh. ``<= 0`` disables this tier.
        realtime_ttl: Seconds a ``[REALTIME]`` endpoint response stays fresh. ``<= 0`` disables this tier.
        max_entries: Maximum number of cached responses (least recently used evicted first).
        max_bytes: Maximum total size of cached response bodies, in bytes.
    """

    ttl: float = 60.0
    realtime_ttl: float = 5.0
    max_entries: int = 1000
    max_bytes: int = 32 * 1024 * 1024


class LRUCache:
    """Thread-safe LRU bounded by entry count and total bytes, with per-entry TTL.

    Raw bodies are stored instead of parsed objects: smaller in memory, and every hit
    yields a fresh object so callers cannot mutate cached data.
    """

    def __init__(self, max_entries: int, max_bytes: int, clock: Callable[[], float] = time.monotonic) -> None:
        self.max_entries = max_entries
        self.max_bytes = max_bytes
        self._clock = clock
        self._data: "OrderedDict[str, Tuple[bytes, float]]" = OrderedDict()
        self._bytes = 0
        self._lock = threading.Lock()

    def __len__(self) -> int:
        return len(self._data)

    @property
    def size_bytes(self) -> int:
        return self._bytes

    def get(self, key: str) -> Optional[bytes]:
        with self._lock:
            item = self._data.get(key)
            if item is None:
                return None
            if item[1] <= self._clock():
                self._remove(key)
                return None
            self._data.move_to_end(key)
            return item[0]

    def set(self, key: str, body: bytes, ttl: float) -> None:
        if ttl <= 0 or len(body) > self.max_bytes or self.max_entries <= 0:
            return
        with self._lock:
            if key in self._data:
                self._remove(key)
            self._data[key] = (body, self._clock() + ttl)
            self._bytes += len(body)
            while len(self._data) > self.max_entries or self._bytes > self.max_bytes:
                self._remove(next(iter(self._data)))

    def delete_where(self, predicate: Callable[[str], bool]) -> None:
        with self._lock:
            for key in [k for k in self._data if predicate(k)]:
                self._remove(key)

    def clear(self) -> None:
        with self._lock:
            self._data.clear()
            self._bytes = 0

    def _remove(self, key: str) -> None:
        body, _ = self._data.pop(key)
        self._bytes -= len(body)
