"""
Contoh penggunaan lanjutan Invezgo SDK.
"""

from invezgo import InvezgoClient

client = InvezgoClient(api_key="your-api-key-here")

# Contoh: Broker Analysis
print("=== Broker Analysis ===")
try:
    summary = client.analysis.get_summary_stock(
        code="BBCA",
        from_date="2024-12-01",
        to_date="2024-12-30",
        investor="all",
        market="RG"
    )
    print(f"Broker summary untuk BBCA: {len(summary)} brokers")
except Exception as e:
    print(f"Error: {e}")

# Contoh: Kepemilikan Saham
print("\n=== Kepemilikan Saham ===")
try:
    shareholders = client.analysis.get_shareholder(code="BBCA")
    print(f"Total pemegang saham: {len(shareholders)}")
    for shareholder in shareholders[:5]:
        print(f"  - {shareholder.get('name')}: {shareholder.get('percentage')}%")
except Exception as e:
    print(f"Error: {e}")

# Contoh: Financial Statement
print("\n=== Laporan Keuangan ===")
try:
    financial = client.analysis.get_financial_statement(
        code="BBCA",
        statement="IS",  # Income Statement
        type_period="Q",  # Quarterly
        limit=4
    )
    print(f"Laporan keuangan: {len(financial.get('rows', []))} akun")
except Exception as e:
    print(f"Error: {e}")

# Contoh: Screener
print("\n=== Screener ===")
try:
    screened = client.screener.screen(
        columns=["code", "close", "volume"],
        conditions=[
            {
                "ratio": "BASIC",
                "column": "close",
                "value": "5000",
                "operator": ">="
            }
        ]
    )
    print(f"Hasil screener: {len(screened)} saham")
except Exception as e:
    print(f"Error: {e}")

# Contoh: AI Analysis
print("\n=== AI Analysis ===")
try:
    ai_news = client.ai.analyze_news(code="BBCA")
    print("AI Analysis berita saham berhasil")
except Exception as e:
    print(f"Error: {e}")

