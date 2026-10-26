import unittest

from invezgo._cache import LRUCache


class Clock:
    def __init__(self) -> None:
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now


class LRUCacheTest(unittest.TestCase):
    def test_evicts_least_recently_used_by_entries(self) -> None:
        c = LRUCache(max_entries=2, max_bytes=1000)
        c.set("a", b"1", 60)
        c.set("b", b"2", 60)
        self.assertEqual(c.get("a"), b"1")  # a becomes most recent
        c.set("c", b"3", 60)
        self.assertIsNone(c.get("b"))
        self.assertEqual(c.get("a"), b"1")
        self.assertEqual(c.get("c"), b"3")
        self.assertEqual(len(c), 2)

    def test_evicts_by_bytes_and_skips_oversized(self) -> None:
        c = LRUCache(max_entries=100, max_bytes=10)
        c.set("a", b"12345", 60)
        c.set("b", b"12345", 60)
        self.assertEqual(c.size_bytes, 10)
        c.set("c", b"123", 60)
        self.assertIsNone(c.get("a"))
        self.assertEqual(c.size_bytes, 8)
        c.set("big", b"12345678901", 60)
        self.assertIsNone(c.get("big"))
        self.assertEqual(c.size_bytes, 8)

    def test_ttl_expiry_and_replace(self) -> None:
        clock = Clock()
        c = LRUCache(10, 100, clock)
        c.set("a", b"old", 5)
        c.set("a", b"new!", 5)
        self.assertEqual(c.size_bytes, 4)
        clock.now += 4.9
        self.assertEqual(c.get("a"), b"new!")
        clock.now += 0.2
        self.assertIsNone(c.get("a"))
        self.assertEqual(c.size_bytes, 0)

    def test_zero_ttl_not_stored_and_delete_where(self) -> None:
        c = LRUCache(10, 100)
        c.set("a", b"1", 0)
        self.assertIsNone(c.get("a"))
        c.set("/watchlists", b"1", 60)
        c.set("/analysis/x", b"2", 60)
        c.delete_where(lambda k: k.startswith("/watchlists"))
        self.assertIsNone(c.get("/watchlists"))
        self.assertEqual(c.get("/analysis/x"), b"2")
        c.clear()
        self.assertEqual((len(c), c.size_bytes), (0, 0))


if __name__ == "__main__":
    unittest.main()
