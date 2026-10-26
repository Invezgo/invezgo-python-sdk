"""Multiple API keys (auto-rotation on HTTP 429) and tuning the in-memory LRU cache."""

import os

from invezgo import CacheOptions, InvezgoClient, RateLimitError


def main() -> None:
    client = InvezgoClient(
        os.environ["INVEZGO_API_KEY"],
        additional_api_keys=[k for k in os.environ.get("INVEZGO_EXTRA_KEYS", "").split(",") if k],
        cache=CacheOptions(
            ttl=120,  # normal endpoints: 2 minutes
            realtime_ttl=2,  # [REALTIME] endpoints: 2 seconds
            max_entries=500,
            max_bytes=16 * 1024 * 1024,  # 16 MiB
        ),
        timeout=15,
    )
    try:
        client.analysis.get_stock_list()  # HTTP request
        client.analysis.get_stock_list()  # served from cache, no quota used
        book = client.analysis.get_order_book("BBCA", "RG")  # realtime tier
        print(book["code"], book["bid"][:1])

        usage = client.usage.get_api_usage()  # never cached
        print(f"Kuota terpakai {usage['usage']}/{usage['limit']}, sisa {usage['remaining']}")
    except RateLimitError as e:
        # Raised only when *every* key is rate limited.
        kind = "kuota bulanan" if e.quota_exceeded else "limit per menit"
        print(f"Semua API key terkena {kind}; coba lagi dalam {e.retry_after} detik")
    finally:
        client.clear_cache()
        client.close()


if __name__ == "__main__":
    main()
