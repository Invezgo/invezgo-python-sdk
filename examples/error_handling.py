"""
Contoh error handling dengan Invezgo SDK.
"""

from invezgo import (
    InvezgoClient,
    AuthenticationError,
    PaymentRequiredError,
    RateLimitError,
    InvezgoError,
)

client = InvezgoClient(api_key="your-api-key-here")

try:
    # Contoh request yang mungkin menghasilkan error
    result = client.analysis.get_stock_list()
    print("Success:", result)

except AuthenticationError as e:
    print(f"Error Autentikasi (401): {e}")
    print("Pastikan API key sudah benar dan aktif")

except PaymentRequiredError as e:
    print(f"Error Paket (402): {e}")
    print("Paket berlangganan tidak mencukupi atau sudah expired")
    print("Silakan upgrade paket di https://invezgo.com/subscription")

except RateLimitError as e:
    print(f"Error Rate Limit (429): {e}")
    print("Melebihi batas permintaan API")
    print("Silakan upgrade paket atau tunggu reset quota")

except InvezgoError as e:
    print(f"Error Invezgo: {e}")

except Exception as e:
    print(f"Error tidak terduga: {e}")

