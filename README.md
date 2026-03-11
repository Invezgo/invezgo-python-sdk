# Invezgo Python SDK - API Saham Indonesia

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/invezgo-sdk.svg)](https://pypi.org/project/invezgo-sdk/)

Python SDK untuk mengakses [Invezgo API](https://invezgo.com) - Platform data saham Indonesia terlengkap dengan data real-time dari Bursa Efek Indonesia (BEI).

## Tentang Invezgo API

Invezgo API menyediakan akses data saham Indonesia yang komprehensif untuk kebutuhan analisis teknikal, fundamental, dan trading. Data mencakup seluruh perusahaan tercatat di BEI dengan update real-time dan historis.

### Fitur Utama

- ✅ **Data Saham Real-time** - Harga, volume, dan order book real-time dari BEI
- ✅ **Data Historis Lengkap** - Chart OHLCV dan data perdagangan historis
- ✅ **Analisis Broker** - Broker summary, inventory chart, dan stalker
- ✅ **Kepemilikan Saham** - Data KSEI, insider trading, shareholder composition
- ✅ **Laporan Keuangan** - Financial statement dan key statistics perusahaan
- ✅ **Indikator Teknikal** - Berbagai indikator untuk analisis teknikal
- ✅ **Type Hints** - Full type hints untuk better IDE support
- ✅ **Error Handling** - Comprehensive error handling

## Instalasi

```bash
pip install invezgo-sdk
```

## Quick Start

```python
from invezgo import InvezgoClient

# Inisialisasi client dengan API key
client = InvezgoClient(api_key="your-api-key-here")

# Contoh: Dapatkan daftar saham
stocks = client.analysis.get_stock_list()
print(stocks)

# Contoh: Dapatkan informasi perusahaan
info = client.analysis.get_information(code="BBCA")
print(info)

# Contoh: Dapatkan chart harga saham
chart = client.analysis.get_chart_stock(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30"
)
print(chart)
```

## Dokumentasi Lengkap API Saham Indonesia

### Authentication

Semua request memerlukan API key yang valid. Dapatkan API key di [Invezgo API Settings](https://invezgo.com/id/setting/api).

```python
client = InvezgoClient(api_key="your-api-key")
```

### Data Master Saham Indonesia

#### Daftar Saham, Broker, dan Index

```python
# Daftar semua saham yang tercatat di BEI
stocks = client.analysis.get_stock_list()

# Daftar semua broker/sekuritas di BEI
brokers = client.analysis.get_broker_list()

# Daftar semua index (IHSG, LQ45, IDX30, sektoral, dll)
indexes = client.analysis.get_index_list()
```

#### Informasi Perusahaan

```python
# Informasi lengkap perusahaan
info = client.analysis.get_information(code="BBCA")
```

### Data Real-time Saham Indonesia

#### Intraday dan Order Book

```python
# Intraday chart saham
intraday = client.analysis.get_intraday(code="BBCA", market="RG")

# Order book saham (bid/offer)
order_book = client.analysis.get_order_book(code="BBCA", market="RG")

# Intraday data ringkas
intraday_data = client.analysis.get_intraday_data(code="BBCA", market="RG")

# Intraday data untuk index
index_intraday = client.analysis.get_intraday_index(code="COMPOSITE", market="RG")
```

### Chart dan Harga Saham Indonesia

```python
# Chart harga saham lengkap dengan OHLCV
chart = client.analysis.get_chart_stock(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30"
)

# Chart index (IHSG, LQ45, dll)
index_chart = client.analysis.get_chart_index(
    code="COMPOSITE",
    from_date="2024-12-01",
    to_date="2024-12-30"
)

# Chart dengan indikator teknikal (bdm, foreign, ritel, ratio)
indicator_chart = client.analysis.get_chart_indicator(
    code="BBCA",
    indicator="bdm",
    from_date="2024-12-01",
    to_date="2024-12-30"
)
```

### Top Gainer & Loser Harian

```python
# Top gainer dan loser harian
top_change = client.analysis.get_top_change(date="2024-12-30")

# Top akumulasi dan distribusi asing
top_foreign = client.analysis.get_top_foreign(date="2024-12-30")

# Top akumulasi dan distribusi bandarmologi
top_bdm = client.analysis.get_top_accumulation(date="2024-12-30")

# Top akumulasi dan distribusi ritel
top_ritel = client.analysis.get_top_ritel(date="2024-12-30")
```

### Analisis Broker Saham Indonesia

#### Broker Summary

```python
# Broker summary per saham
summary = client.analysis.get_summary_stock(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",  # all, f (foreign), d (domestic)
    market="RG"
)

# Broker summary per broker (bisa multiple broker)
broker_summary = client.analysis.get_summary_broker(
    code="AG,AK",  # bisa single atau multiple dipisah koma
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    market="RG"
)
```

#### Broker Stalker

```python
# Melacak aktivitas broker pada saham tertentu
stalker = client.analysis.get_broker_stalker(
    broker="AG",
    stock="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    market="RG",
    scope="value"
)

# Daftar saham yang diperdagangkan broker
stalker_list = client.analysis.get_broker_stalker_list(
    code="AG",
    from_date="2024-12-01",
    to_date="2024-12-30",
    investor="all",
    scope="value",
    market="RG"
)
```

#### Inventory Chart

```python
# Inventory chart saham
inventory = client.analysis.get_inventory_chart_stock(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    scope="val",  # vol, val, freq
    investor="all",  # all, f, d
    market="RG"
)

# Inventory chart broker
broker_inventory = client.analysis.get_inventory_chart_broker(
    code="AG",
    from_date="2024-12-01",
    to_date="2024-12-30",
    scope="val",
    investor="all",
    market="RG"
)
```

### Kepemilikan Saham (Shareholder)

#### Komposisi Kepemilikan

```python
# Komposisi kepemilikan saham (pengendali, direksi, masyarakat)
shareholders = client.analysis.get_shareholder(code="BBCA")

# Jumlah pemegang saham historis
shareholder_number = client.analysis.get_shareholder_number(code="BBCA")

# Kepemilikan KSEI (klasifikasi investor asing/domestik)
ksei = client.analysis.get_shareholder_ksei(code="BBCA", range_months=6)

# Detail kepemilikan 5%
detail = client.analysis.get_shareholder_detail(code="BBCA", name="NAMA PEMEGANG")

# Detail kepemilikan 1%
detail_one = client.analysis.get_shareholder_detail_one(code="BBCA", name="NAMA PEMEGANG")

# Graph relasi kepemilikan
relation = client.analysis.get_shareholder_relation(
    code="BBCA",
    depth=3,
    max_nodes=120
)
```

#### Insider Trading

```python
# Perubahan kepemilikan diatas 5%
above = client.analysis.get_shareholder_above(
    from_date="2024-12-01",
    to_date="2024-12-30",
    page=1,
    limit=10
)

# Chart kepemilikan diatas 5%
above_chart = client.analysis.get_shareholder_above_chart(
    code="BBCA",
    broker="AG",
    name="NAMA PEMEGANG"
)

# Perubahan kepemilikan diatas 1%
one = client.analysis.get_shareholder_one(
    from_date="2024-12-01",
    to_date="2024-12-30"
)

# Insider trading (direksi, komisaris)
insider = client.analysis.get_shareholder_insider(
    from_date="2024-12-01",
    to_date="2024-12-30"
)
```

### Analisis Sektoral Saham Indonesia

```python
# Sector stalker - pergerakan index sektoral
sector = client.analysis.get_sector_stalker(
    from_date="2024-12-01",
    to_date="2024-12-30",
    base="COMPOSITE"
)

# Sector rotation chart
rotation = client.analysis.get_sector_rotation(
    from_date="2024-12-01",
    to_date="2024-12-30",
    base="COMPOSITE",
    length=10,
    tail=5
)
```

### Laporan Keuangan dan Fundamental

```python
# Laporan keuangan (BS: Balance Sheet, IS: Income Statement, CF: Cash Flow)
financial = client.analysis.get_financial_statement(
    code="BBCA",
    statement="BS",
    type_period="Q",  # FY, Q, Q1, Q2, Q3, Q4
    limit=10
)

# Chart laporan keuangan
financial_chart = client.analysis.get_financial_statement_chart(
    code="BBCA",
    statement="BS",
    type_period="Q",
    limit=10,
    account="ACCOUNT_ID"
)

# Key statistics
keystat = client.analysis.get_keystat(
    code="BBCA",
    type_period="Q",
    limit=10
)

# Chart key statistics
keystat_chart = client.analysis.get_keystat_chart(
    code="BBCA",
    type_period="Q",
    limit=10,
    name="PER"  # PER, PBV, ROE, dll
)
```

### Data Real-time Lanjutan

```python
# Momentum chart
momentum = client.analysis.get_momentum_chart(
    code="BBCA",
    date="2024-12-30",
    range_minutes=60,
    scope="value"
)

# Intraday inventory chart
intraday_inventory = client.analysis.get_intraday_inventory_chart(
    code="BBCA",
    date="2024-12-30",
    range_minutes=60,
    type_name="value",
    total=10,
    buyer="ALL",
    seller="ALL",
    market="RG"
)

# Sankey/Crossing chart
sankey = client.analysis.get_sankey_chart(
    code="BBCA",
    date="2024-12-30",
    type_name="value",
    buyer="ALL",
    seller="ALL",
    market="RG"
)

# Price table (transaksi per harga)
price_table = client.analysis.get_price_table(code="BBCA", date="2024-12-30")

# Time table (transaksi per waktu)
time_table = client.analysis.get_time_table(
    code="BBCA",
    date="2024-12-30",
    range_minutes=60
)

# Price diary (histori harga harian)
price_diary = client.analysis.get_price_diary(code="BBCA")

# Price seasonality (histori harga bulanan)
seasonality = client.analysis.get_price_seasonality(code="BBCA", range_months=12)
```

### Kalender Corporate Action

```python
# Kalender corporate action (dividen, rights issue, dll)
calendar = client.analysis.get_calendar()
```

## Personal Features

### Watchlists

```python
# Daftar watchlist
watchlists = client.watchlists.list(group="default")

# Tambah watchlist baru
client.watchlists.add(data={"code": "BBCA", "group": "default"})

# Update watchlist
client.watchlists.update(id="watchlist-id", data={"note": "Catatan"})

# Hapus watchlist
client.watchlists.delete(data={"id": "watchlist-id"})

# Daftar grup watchlist
groups = client.watchlists.list_group()
```

### Journals (Jurnal Trading)

```python
# Daftar transaksi jurnal
transactions = client.journals.list()

# Tambah transaksi jurnal
client.journals.add(data={"code": "BBCA", "type": "buy", "price": 8000, "lot": 10})

# Ringkasan transaksi
summary = client.journals.get_summary()

# Update catatan transaksi
client.journals.update_note(id="journal-id", data={"note": "Catatan"})

# Ekstrak jurnal dari file
client.journals.extract_from_file(file_data={"file": "..."})
```

### Portfolios

```python
# Daftar portofolio
portfolios = client.portfolios.list()

# Ringkasan portofolio
summary = client.portfolios.get_summary()
```

### Realized Trades

```python
# Daftar transaksi terealisasi
trades = client.trades.list()

# Ringkasan transaksi
summary = client.trades.get_summary()

# Ringkasan grafik
chart = client.trades.get_summary_chart()

# Update catatan
client.trades.update_note(id="trade-id", data={"note": "Catatan"})
```

## AI Features

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

# Analisa AI inventory chart
ai_inventory = client.ai.analyze_inventory_chart(
    code="BBCA",
    from_date="2024-12-01",
    to_date="2024-12-30",
    scope="val",
    investor="all",
    limit="20",
    market="RG",
    filter_brokers=""
)

# Analisa AI insider trading
ai_insider = client.ai.analyze_insider(
    code="BBCA",
    name="NAMA PEMEGANG",
    from_date="2024-12-01",
    to_date="2024-12-30",
    page="1",
    limit="10"
)

# Analisa AI pemegang saham diatas 5%
ai_above = client.ai.analyze_shareholder_above(
    code="BBCA",
    broker="AG",
    name="NAMA PEMEGANG",
    from_date="2024-12-01",
    to_date="2024-12-30",
    page="1",
    limit="10"
)

# Analisa AI intraday inventory
ai_intraday = client.ai.analyze_intraday_inventory(
    code="BBCA",
    range_minutes=60,
    type_name="value",
    total=10,
    buyer="ALL",
    seller="ALL",
    broker="",
    market="RG"
)

# Analisa AI sankey chart
ai_sankey = client.ai.analyze_sankey_chart(
    code="BBCA",
    type_name="value",
    buyer="ALL",
    seller="ALL",
    market="RG"
)

# Analisa AI pemegang saham
ai_shareholder = client.ai.analyze_shareholder(code="BBCA")

# Analisa AI laporan keuangan
ai_financial = client.ai.analyze_financial_statement(
    code="BBCA",
    statement="BS",
    type_period="Q",
    limit="10"
)

# Analisa AI key statistics
ai_keystat = client.ai.analyze_keystat(
    code="BBCA",
    type_period="Q",
    limit="10"
)
```

## Social Features

### Posts

```python
# Daftar semua postingan
posts = client.posts.get_all()

# Postingan berdasarkan kategori
posts = client.posts.get_by_category(category="analisis")

# Postingan saham tertentu
posts = client.posts.get_by_stock(code="BBCA")

# Detail postingan
detail = client.posts.get_by_id(id="post-id")

# Komentar postingan
comments = client.posts.get_comments(id="post-id")

# Daftar voting
voters = client.posts.get_voters(id="post-id")
```

### Profile

```python
# Informasi profil pengguna
profile = client.profile.get_user_details(username="username")

# Postingan pengguna
posts = client.profile.get_user_posts(username="username", page="1", limit="10")

# Watchlist pengguna
watchlist = client.profile.get_user_watchlist(username="username")

# Followers
followers = client.profile.get_followers(username="username")

# Following
following = client.profile.get_following(username="username")

# Rekomendasi pengguna
recommendations = client.profile.get_recommendations()
```

## Screener Saham Indonesia

```python
# Daftar preset screener
presets = client.screener.list_presets()

# Jalankan screener
results = client.screener.screen(
    columns=["close", "volume", "change"],
    conditions=[
        {
            "ratio": "BASIC",
            "column": "change_1d_close",
            "operator": ">",
            "value": "0"
        },
        {
            "ratio": "BASIC",
            "column": "value",
            "operator": ">",
            "value": "1000000000"
        }
    ]
)
```

## Search

```python
# Cari saham atau pengguna
results = client.search.search(query="BBCA")

# Cari saham
stocks = client.search.search_stock(query="BBCA", cursor="")

# Cari pengguna
users = client.search.search_user(query="username", cursor="")
```

## Health Check

```python
# Status API
health = client.health.check()

# Status database
db_health = client.health.check_database()

# Status lengkap
full_health = client.health.check_full()
```

## Error Handling

SDK ini meng-handle berbagai jenis error:

```python
from invezgo.exceptions import (
    InvezgoError,
    AuthenticationError,
    PaymentRequiredError,
    RateLimitError,
    NotFoundError,
    BadRequestError,
    ServerError
)

try:
    result = client.analysis.get_stock_list()
except AuthenticationError:
    print("API key tidak valid")
except PaymentRequiredError:
    print("Paket berlangganan tidak mencukupi")
except RateLimitError:
    print("Melebihi batas permintaan API")
except NotFoundError:
    print("Data tidak ditemukan")
except BadRequestError:
    print("Request tidak valid")
except ServerError:
    print("Error server")
except InvezgoError as e:
    print(f"Error: {e}")
```

## Keywords

Invezgo SDK, API Saham Indonesia, Data Saham BEI, Bursa Efek Indonesia, IDX, IHSG, LQ45, IDX30, Saham Indonesia, Trading Indonesia, Broker Summary, Foreign Flow, Bandarmologi, Analisis Saham, Real-time Stock Data, Intraday Chart, Order Book, Financial Statement, Laporan Keuangan, Insider Trading, KSEI, Shareholder Analysis, Stock Screener, Technical Analysis, Fundamental Analysis.

## Lisensi

MIT License - lihat [LICENSE](LICENSE) untuk detail.

## Support

- Email: admin@invezgo.com
- Website: https://invezgo.com
- Dokumentasi API: https://invezgo.com

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
