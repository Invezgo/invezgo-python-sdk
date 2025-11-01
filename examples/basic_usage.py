"""
Contoh penggunaan dasar Invezgo SDK.

Sebelum menggunakan, pastikan sudah memiliki API key dari:
https://invezgo.com/id/setting/api
"""

from invezgo import InvezgoClient

# Inisialisasi client
client = InvezgoClient(api_key="your-api-key-here")

# Contoh 1: Dapatkan daftar saham
try:
    stocks = client.analysis.get_stock_list()
    print(f"Total saham: {len(stocks)}")
    print(f"Contoh: {stocks[0]}")
except Exception as e:
    print(f"Error: {e}")

# Contoh 2: Dapatkan informasi perusahaan
try:
    info = client.analysis.get_information(code="BBCA")
    print(f"\nInformasi BBCA:")
    print(f"Nama: {info.get('name')}")
    print(f"Sektor: {info.get('sector')}")
except Exception as e:
    print(f"Error: {e}")

# Contoh 3: Dapatkan chart harga saham
try:
    chart = client.analysis.get_chart(
        code="BBCA",
        from_date="2024-12-01",
        to_date="2024-12-30"
    )
    print(f"\nChart data: {len(chart.get('price', []))} data points")
except Exception as e:
    print(f"Error: {e}")

# Contoh 4: Top gainer dan loser
try:
    top_change = client.analysis.get_top_change(date="2024-12-30")
    print(f"\nTop Gainer: {len(top_change.get('gain', []))} saham")
    print(f"Top Loser: {len(top_change.get('loss', []))} saham")
except Exception as e:
    print(f"Error: {e}")

