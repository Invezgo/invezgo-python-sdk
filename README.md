# Invezgo Python SDK

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/invezgo-sdk.svg)](https://pypi.org/project/invezgo-sdk/)

Python SDK untuk mengakses [Invezgo API](https://invezgo.com) - Data Saham Indonesia yang lengkap dan terpercaya.

## Fitur

- ✅ Akses lengkap ke semua endpoint Invezgo API
- ✅ Type hints untuk better IDE support
- ✅ Error handling yang comprehensive
- ✅ Async-ready (future support)
- ✅ Easy to use dan developer-friendly

## Instalasi

```bash
pip install invezgo-sdk
```

## Quick Start

```python
from invezgo import InvezgoClient

# Inisialisasi client dengan API key
client = InvezgoClient(api_key="your-api-key-here")

# Atau dengan base URL custom
client = InvezgoClient(
    api_key="your-api-key-here",
    base_url="https://api.invezgo.com"
)

# Contoh: Dapatkan daftar saham
stocks = client.analysis.get_stock_list()
print(stocks)

# Contoh: Dapatkan informasi perusahaan
info = client.analysis.get_information(code="BBCA")
print(info)

# Contoh: Dapatkan chart harga saham
chart = client.analysis.get_chart(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30"
)
print(chart)
```

## Dokumentasi Lengkap

### Authentication

Semua request memerlukan API key yang valid. Dapatkan API key di [Invezgo API Settings](https://invezgo.com/id/setting/api).

```python
client = InvezgoClient(api_key="your-api-key")
```

### Data Saham Indonesia

#### Daftar Saham dan Broker

```python
# Daftar semua saham
stocks = client.analysis.get_stock_list()

# Daftar semua broker
brokers = client.analysis.get_broker_list()
```

#### Informasi Perusahaan

```python
# Informasi lengkap perusahaan
info = client.analysis.get_information(code="BBCA")
```

#### Chart dan Harga

```python
# Chart harga saham lengkap
chart = client.analysis.get_chart(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30"
)

# Intraday chart
intraday = client.analysis.get_intraday(code="BBCA", market="RG")

# Chart dengan indikator
indicator_chart = client.analysis.get_indicator_chart(
    code="BBCA",
    indicator="rsi",
    from_date="2024-12-01",
    to_date="2024-12-30"
)
```

#### Top Gainer & Loser

```python
# Top gainer dan loser harian
top_change = client.analysis.get_top_change(date="2024-12-30")

# Top akumulasi dan distribusi asing
top_foreign = client.analysis.get_top_foreign(date="2024-12-30")
```

#### Broker Analysis

```python
# Broker summary per saham
summary = client.analysis.get_summary_stock(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    market="RG"
)

# Broker summary per broker
broker_summary = client.analysis.get_summary_broker(
    code="AG",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    market="RG"
)
```

#### Kepemilikan Saham

```python
# Komposisi kepemilikan saham
shareholders = client.analysis.get_shareholder(code="BBCA")

# Jumlah pemegang saham
shareholder_count = client.analysis.get_shareholder_number(code="BBCA")

# Kepemilikan KSEI
ksei = client.analysis.get_shareholder_ksei(code="BBCA", range_months=6)
```

### Personal Features

#### Watchlists

```python
# Daftar watchlist
watchlists = client.watchlists.list(group="default")

# Tambah watchlist baru
client.watchlists.add(data={...})

# Update watchlist
client.watchlists.update(id="watchlist-id", data={...})

# Hapus watchlist
client.watchlists.delete(data={...})
```

#### Journals

```python
# Daftar transaksi jurnal
transactions = client.journals.list()

# Tambah transaksi jurnal
client.journals.add(data={...})

# Ringkasan transaksi
summary = client.journals.get_summary()
```

#### Portfolios

```python
# Daftar portofolio
portfolios = client.portfolios.list()

# Ringkasan portofolio
summary = client.portfolios.get_summary()
```

### AI Features

```python
# Analisa AI KSEI pemegang saham
ai_ksei = client.ai.analyze_shareholder_ksei(code="BBCA")

# Analisa AI berita saham
ai_news = client.ai.analyze_news(code="BBCA")

# Analisa AI broker summary
ai_summary = client.ai.analyze_broker_summary(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    market="RG"
)
```

## Error Handling

SDK ini meng-handle berbagai jenis error:

```python
from invezgo.exceptions import (
    InvezgoError,
    AuthenticationError,
    PaymentRequiredError,
    RateLimitError
)

try:
    result = client.analysis.get_stock_list()
except AuthenticationError:
    print("API key tidak valid")
except PaymentRequiredError:
    print("Paket berlangganan tidak mencukupi")
except RateLimitError:
    print("Melebihi batas permintaan API")
except InvezgoError as e:
    print(f"Error: {e}")
```

## Lisensi

MIT License - lihat [LICENSE](LICENSE) untuk detail.

## Support

- Email: admin@invezgo.com
- Website: https://invezgo.com
- Dokumentasi API: https://invezgo.com

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

