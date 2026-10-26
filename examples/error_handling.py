"""Handling every error type raised by the SDK."""

import os

from invezgo import (
    AuthenticationError,
    InvezgoConnectionError,
    InvezgoError,
    InvezgoClient,
    NotFoundError,
    PaymentRequiredError,
    RateLimitError,
    ServerError,
    ValidationError,
)


def main() -> None:
    client = InvezgoClient(os.environ.get("INVEZGO_API_KEY", "invalid-key"))
    try:
        client.analysis.get_summary_stock("BBCA", "2024-12-01", "2024-12-31", "all", "RG")
    except AuthenticationError:
        print("API key salah atau kedaluwarsa")
    except PaymentRequiredError as e:
        print("Paket langganan tidak mencakup endpoint ini:", e.message)
    except ValidationError as e:  # 400 / 422
        print("Parameter tidak valid:", e.message)
    except NotFoundError:
        print("Data tidak ditemukan")
    except RateLimitError as e:
        print(f"Rate limit, coba lagi {e.retry_after} detik lagi")
    except ServerError as e:
        print(f"Server error {e.status}, request id {e.request_id}")
    except InvezgoConnectionError as e:  # includes InvezgoTimeoutError
        print("Gagal terhubung:", e)
    except InvezgoError as e:  # anything else from the API
        print(f"Error {e.status}: {e.message} (request id {e.request_id})")


if __name__ == "__main__":
    main()
