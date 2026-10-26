# Invezgo Python SDK

[![PyPI](https://img.shields.io/pypi/v/invezgo-sdk.svg)](https://pypi.org/project/invezgo-sdk/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

SDK resmi untuk [Invezgo API](https://invezgo.com), penyedia data pasar modal Indonesia (BEI/IDX). SDK ini menyediakan akses bertipe ke seluruh endpoint Invezgo API, dilengkapi cache in-memory dan rotasi API key otomatis.

[Dokumentasi API](https://api.invezgo.com/documentation) · [Referensi SDK](docs/API.md) · [Changelog](CHANGELOG.md)

## Daftar Isi

- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Konfigurasi](#konfigurasi)
- [Memanggil Endpoint](#memanggil-endpoint)
- [Tipe Data](#tipe-data)
- [Caching](#caching)
- [Rotasi API Key](#rotasi-api-key)
- [Penanganan Error](#penanganan-error)
- [Pagination](#pagination)
- [Praktik yang Disarankan](#praktik-yang-disarankan)
- [Pengembangan](#pengembangan)
- [Dukungan](#dukungan)
- [Lisensi](#lisensi)

## Persyaratan

- Python 3.9 atau lebih baru
- API key Invezgo, dapat dibuat di [halaman pengaturan API](https://invezgo.com/id/setting/api)

Dependency runtime hanya `requests` dan `typing_extensions`. Client bersifat thread-safe.

## Instalasi

```bash
pip install invezgo-sdk
```

## Penggunaan

```python
import os

from invezgo import InvezgoClient

with InvezgoClient(os.environ["INVEZGO_API_KEY"]) as client:
    stocks = client.analysis.get_stock_list()
    info = client.analysis.get_information("BBCA")
    top = client.analysis.get_top_change("2024-12-30")

    print(top["gain"][0]["code"], top["gain"][0]["change"])
```

Client dapat digunakan sebagai context manager, atau ditutup secara manual dengan `client.close()`.

## Konfigurasi

```python
import os

from invezgo import CacheOptions, InvezgoClient

client = InvezgoClient(
    os.environ["INVEZGO_API_KEY"],
    additional_api_keys=[os.environ["INVEZGO_API_KEY_2"]],
    timeout=30.0,
    cache=CacheOptions(ttl=60, realtime_ttl=5),
)
```

| Opsi | Tipe | Default | Keterangan |
|---|---|---|---|
| `api_key` | `str` | wajib | API key utama. |
| `additional_api_keys` | `Sequence[str]` | `()` | API key cadangan, digunakan saat terjadi `429`. Lihat [Rotasi API Key](#rotasi-api-key). |
| `base_url` | `str` | `https://api.invezgo.com` | Base URL API. |
| `timeout` | `float` | `30.0` | Timeout per request, dalam detik. |
| `cache` | `bool \| CacheOptions` | `True` | Konfigurasi cache. `False` untuk menonaktifkan. |
| `session` | `requests.Session \| None` | `None` | Session alternatif, misalnya untuk proxy. Tidak ditutup oleh `client.close()`. |

| Field `CacheOptions` | Default | Keterangan |
|---|---|---|
| `ttl` | `60` | TTL endpoint reguler, dalam detik. |
| `realtime_ttl` | `5` | TTL endpoint realtime, dalam detik. |
| `max_entries` | `1000` | Jumlah maksimum entri cache. |
| `max_bytes` | `33554432` | Ukuran maksimum cache (32 MiB). |

Seluruh argumen selain `api_key` bersifat keyword-only. Buat satu instance client dan gunakan kembali di seluruh aplikasi. Cache, status rotasi API key, dan koneksi HTTP disimpan per instance.

## Memanggil Endpoint

Endpoint dikelompokkan berdasarkan resource:

| Resource | Cakupan |
|---|---|
| `analysis` | Daftar saham, broker, dan indeks; harga, chart, intraday, order book, running trade; broker summary; pemegang saham; laporan keuangan; kalender aksi korporasi; berita dan keterbukaan informasi |
| `batch` | Order book dan data intraday untuk beberapa saham dalam satu request |
| `search` | Pencarian saham dan pengguna |
| `screener` | Eksekusi screener dan pengelolaan preset |
| `usage` | Pemakaian dan sisa kuota API |
| `watchlists` | Watchlist dan grup watchlist |
| `journals` | Jurnal transaksi |
| `portfolios` | Portofolio |
| `alerts` | Alert berbasis formula |
| `posts` | Post, komentar, like, dan vote komunitas |
| `trades` | Realized trade |

Setiap method mengikuti pola berikut:

```
client.<resource>.<method>(*path_params, body?, *required_query, **optional_query)
```

| Argumen | Keterangan |
|---|---|
| Path parameter | Argumen posisional, sesuai urutan di URL. |
| `body` | Request body untuk `POST`, `PUT`, `PATCH`, dan `DELETE`, bertipe `*Request` (`TypedDict`). |
| Query parameter wajib | Argumen posisional setelah path parameter. |
| Query parameter opsional | Keyword-only, default `None` (tidak dikirim). |

Nama parameter sama dengan nama di API. Parameter `from` ditulis `from_` karena merupakan keyword Python. Parameter tanggal menerima `str` (`YYYY-MM-DD`) maupun `datetime.date`.

```python
# Path parameter dan query parameter wajib
client.analysis.get_broker_stalker("YP", "BBCA", "2024-12-01", "2024-12-31", "all", "RG")

# Query parameter opsional
client.analysis.get_advance_chart("BBCA", from_="2024-12-01", to="2024-12-31")

# Request body
client.screener.screen({"formula": "close > prev AND volume > 1000000", "category": ["SYARIAH"]})

# Beberapa saham sekaligus, dihitung sebagai satu request
client.batch.get_order_book("BBCA|BBRI|BMRI")
```

Daftar lengkap method, parameter, nilai default, dan tipe kembalian tersedia di [docs/API.md](docs/API.md).

## Tipe Data

Response dikembalikan sebagai `dict` biasa yang diberi tipe `TypedDict`. Seluruh tipe tersedia di modul `invezgo.types` dan lolos pemeriksaan `mypy --strict`.

```python
from invezgo.types import AddWatchlistRequest, TopChangeFilterColumn, TopChangeResponse

column: TopChangeFilterColumn = "change"  # "change" | "value" | "volume" | "ratio"
top: TopChangeResponse = client.analysis.get_top_change(
    "2024-12-30",
    filter_column=column,
    filter_operator=">",
    filter_value=5,
)

item: AddWatchlistRequest = {
    "group": "cm2x8k1q40000abcd1234efgh",
    "code": "BBCA",
    "price": 9900,
    "scope": [],
}
client.watchlists.add(item)
```

Ketentuan tipe:

| Kasus | Representasi |
|---|---|
| Parameter enum | `Literal`, misalnya `Literal["ALL", "BUY", "SELL"]` |
| Field nullable | `Optional[T]` |
| Field opsional | `NotRequired[T]` |
| Response array | Alias `XResponse = List[XItem]` |
| Response yang dapat bernilai `None` | `Optional[X]`, misalnya `get_shareholder_classify_table` |
| Angka yang dapat dikirim sebagai string | `Union[float, str]` |
| Kolom dinamis hasil `screener.screen` | Dibaca melalui `cast(Dict[str, Any], item)` |

Response berbentuk union dapat dibedakan melalui field `type`:

```python
graph = client.analysis.get_shareholder_relation(code="BBCA")

for node in graph["nodes"]:
    if node["type"] == "stock":
        print(node["label"], node["company_name"])
    else:
        print(node["label"])
```

## Caching

Cache in-memory aktif secara default untuk mengurangi pemakaian kuota dan latensi.

- Hanya request `GET` yang disimpan. Cache key terdiri dari path dan query string yang telah dinormalisasi.
- Cache menggunakan algoritma LRU dengan batas jumlah entri (`max_entries`) dan total ukuran (`max_bytes`). Entri yang paling lama tidak digunakan akan dihapus saat salah satu batas terlampaui.
- Endpoint realtime (order book, running trade, intraday, chart, batch, dan sejenisnya) menggunakan `realtime_ttl`. Endpoint lainnya menggunakan `ttl`.
- Endpoint `usage` dan request selain `GET` tidak disimpan di cache.
- Setiap request `POST`, `PUT`, `PATCH`, atau `DELETE` yang berhasil akan menghapus cache data personal (`watchlists`, `journals`, `portfolios`, `trades`, `alerts`, `screener`).

```python
InvezgoClient(api_key, cache=False)                       # nonaktifkan cache
InvezgoClient(api_key, cache=CacheOptions(realtime_ttl=0)) # nonaktifkan cache untuk endpoint realtime
InvezgoClient(api_key, cache=CacheOptions(ttl=300))       # TTL endpoint reguler 5 menit

client.clear_cache()                                      # hapus seluruh cache
```

## Rotasi API Key

Setiap API key memiliki batas request per menit untuk setiap endpoint dan kuota bulanan. Jika Anda memiliki lebih dari satu API key, tambahkan sebagai cadangan:

```python
client = InvezgoClient(
    os.environ["INVEZGO_API_KEY"],
    additional_api_keys=[os.environ["INVEZGO_API_KEY_2"], os.environ["INVEZGO_API_KEY_3"]],
)
```

Ketika API mengembalikan `429 Too Many Requests`:

1. Lama penundaan diambil dari header `Retry-After`. Jika tidak tersedia, digunakan `X-RateLimit-Reset`, kemudian 60 detik.
2. Untuk batas per menit, API key ditangguhkan hanya pada endpoint tersebut. Untuk kuota bulanan, API key ditangguhkan pada seluruh endpoint.
3. Request dikirim ulang menggunakan API key berikutnya yang tersedia.
4. API key utama digunakan kembali setelah masa penangguhan berakhir.
5. Jika seluruh API key sedang ditangguhkan, SDK melempar `RateLimitError` tanpa mengirim request.

Rotasi hanya dilakukan untuk status `429`. Untuk endpoint data personal seperti watchlist dan portofolio, gunakan API key dari akun yang sama.

Sisa kuota dapat diperiksa tanpa mengurangi kuota:

```python
usage = client.usage.get_api_usage()
print(usage["usage"], usage["limit"], usage["remaining"], usage["expire"])
```

## Penanganan Error

Seluruh exception merupakan turunan `InvezgoError`.

| Class | Status HTTP | Penyebab |
|---|---|---|
| `ValidationError` (alias `BadRequestError`) | 400, 422 | Parameter atau body tidak valid |
| `AuthenticationError` | 401 | API key tidak valid atau kedaluwarsa |
| `PaymentRequiredError` | 402 | Endpoint tidak termasuk dalam paket langganan |
| `NotFoundError` | 404 | Data tidak ditemukan |
| `RateLimitError` | 429 | Batas request atau kuota tercapai pada seluruh API key |
| `ServerError` | 5xx | Kesalahan pada server |
| `InvezgoTimeoutError` | — | Request melebihi `timeout` |
| `InvezgoConnectionError` | — | Kegagalan jaringan |

Atribut yang tersedia: `status`, `message`, `error`, `request_id`, `path`, dan `body`. `RateLimitError` juga menyediakan `retry_after` (detik), `limit`, `remaining`, `reset`, dan `quota_exceeded`.

```python
from invezgo import InvezgoError, RateLimitError, ValidationError

try:
    client.analysis.get_summary_stock("BBCA", "2024-12-01", "2024-12-31", "all", "RG")
except RateLimitError as e:
    print(f"Rate limit tercapai, coba lagi dalam {e.retry_after} detik")
except ValidationError as e:
    print(f"Parameter tidak valid: {e.message}")
except InvezgoError as e:
    print(e.status, e.message, e.request_id)
```

## Pagination

Endpoint dengan pagination mengembalikan `page`, `totalPage`, dan `nextPage`. Nilai `nextPage` adalah `None` pada halaman terakhir.

```python
page: Optional[int] = 1

while page is not None:
    res = client.analysis.get_news(page=page, limit=50)
    for item in res["data"]:
        print(item["title"])
    page = res["nextPage"]
```

## Praktik yang Disarankan

- Gunakan satu instance client untuk seluruh aplikasi.
- Simpan API key di environment variable atau secret manager.
- Gunakan format tanggal `YYYY-MM-DD`. Data end-of-day tersedia setelah pukul 18.00 WIB.
- Field waktu bersufiks `Z` menggunakan waktu WIB (UTC+7); jangan dikonversi ke zona waktu lain.
- Gunakan resource `batch` untuk mengambil data beberapa saham sekaligus.
- Saat menerima `RateLimitError`, tunggu sesuai `retry_after` sebelum mencoba kembali.
- Untuk polling data realtime, sesuaikan `realtime_ttl` dengan interval polling.

Contoh lengkap tersedia di direktori [examples](examples/).

## Pengembangan

File `invezgo/types.py`, `invezgo/resources.py`, dan `docs/API.md` dihasilkan dari spesifikasi OpenAPI dan tidak boleh diubah secara manual.

```bash
python ../codegen/generate.py python   # generate ulang kode dari OpenAPI
pip install -r requirements-dev.txt
mypy invezgo examples tests            # pemeriksaan tipe
python -m pytest                       # unit test
```

## Dukungan

Sertakan nilai `request_id` dari exception saat menghubungi tim dukungan Invezgo.

- Website: [invezgo.com](https://invezgo.com)
- Dokumentasi API: [api.invezgo.com/documentation](https://api.invezgo.com/documentation)

## Lisensi

Dirilis di bawah [MIT License](LICENSE).
