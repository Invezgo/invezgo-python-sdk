# Invezgo Python SDK — API Reference

> Dibuat otomatis dari spesifikasi OpenAPI resmi oleh `codegen/gen_python.py`. Jangan edit manual.

Semua method tersedia di `InvezgoClient` (mis. `client.analysis.get_stock_list()`). Total 109 endpoint.

Cache tier: `default` = TTL `cache.ttl` (60 dtk), `realtime` = TTL `cache.realtime_ttl` (5 dtk), `none` = tidak di-cache.

## Daftar Isi

- [`client.analysis`](#clientanalysis)
- [`client.batch`](#clientbatch)
- [`client.search`](#clientsearch)
- [`client.screener`](#clientscreener)
- [`client.usage`](#clientusage)
- [`client.watchlists`](#clientwatchlists)
- [`client.journals`](#clientjournals)
- [`client.portfolios`](#clientportfolios)
- [`client.alerts`](#clientalerts)
- [`client.posts`](#clientposts)
- [`client.trades`](#clienttrades)

## client.analysis

Indonesia stock market data: lists, prices, charts, broker flow, shareholders, fundamentals.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`get_stock_list`](#analysisget_stock_list) | `GET /analysis/list/stock` | Stock List | `default` |
| [`get_broker_list`](#analysisget_broker_list) | `GET /analysis/list/broker` | Broker List | `default` |
| [`get_index_list`](#analysisget_index_list) | `GET /analysis/list/index` | Index List | `default` |
| [`get_uma`](#analysisget_uma) | `GET /analysis/uma` | Stock UMA List | `default` |
| [`get_suspend`](#analysisget_suspend) | `GET /analysis/suspend` | Stock Suspend List | `default` |
| [`get_notation`](#analysisget_notation) | `GET /analysis/notation` | Stock Notation List | `default` |
| [`get_information`](#analysisget_information) | `GET /analysis/information/{code}` | Company Information | `default` |
| [`get_top_change`](#analysisget_top_change) | `GET /analysis/top/change` | Top Gainer & Loser | `default` |
| [`get_top_foreign`](#analysisget_top_foreign) | `GET /analysis/top/foreign` | Top Foreign Flow | `default` |
| [`get_top_accumulation`](#analysisget_top_accumulation) | `GET /analysis/top/accumulation` | Top BDM Flow | `default` |
| [`get_top_ritel`](#analysisget_top_ritel) | `GET /analysis/top/ritel` | Top Ritel Flow | `default` |
| [`get_stock_running_trade`](#analysisget_stock_running_trade) | `GET /analysis/running-trade/{code}` | Stock Running Trade | `realtime` |
| [`get_intraday_chart`](#analysisget_intraday_chart) | `GET /analysis/intraday/{code}` | Stock/Index Intraday Chart | `realtime` |
| [`get_order_book`](#analysisget_order_book) | `GET /analysis/order-book/{code}` | Stock Order Book | `realtime` |
| [`get_order_queue`](#analysisget_order_queue) | `GET /analysis/queue/{code}` | Stock Order Queue (Tracking) | `realtime` |
| [`get_intraday_data`](#analysisget_intraday_data) | `GET /analysis/intraday-data/{code}` | Stock Intraday Data | `realtime` |
| [`get_intraday_index`](#analysisget_intraday_index) | `GET /analysis/intraday-index/{code}` | Index Intraday Data | `realtime` |
| [`get_advance_chart`](#analysisget_advance_chart) | `GET /analysis/chart/stock/{code}` | Stock Chart | `realtime` |
| [`get_index_chart`](#analysisget_index_chart) | `GET /analysis/chart/index/{code}` | Index Chart | `realtime` |
| [`get_multi_time_chart`](#analysisget_multi_time_chart) | `GET /analysis/chart/multi-time/{code}` | Stock/Index Multi Timeframe Chart | `realtime` |
| [`get_indicator_chart`](#analysisget_indicator_chart) | `GET /analysis/chart/stock/{indicator}/{code}` | Stock Chart Indicator | `default` |
| [`get_shareholder_detail`](#analysisget_shareholder_detail) | `GET /analysis/shareholder-detail` | Stock Shareholder 5% | `default` |
| [`get_shareholder_one_detail`](#analysisget_shareholder_one_detail) | `GET /analysis/shareholder-detail-one` | Stock Shareholder 1% | `default` |
| [`get_shareholder_high`](#analysisget_shareholder_high) | `GET /analysis/shareholder/high` | Stock High Concentration | `default` |
| [`get_shareholder_number`](#analysisget_shareholder_number) | `GET /analysis/shareholder/number/{code}` | Stock Shareholder Number | `default` |
| [`get_shareholder_relation`](#analysisget_shareholder_relation) | `GET /analysis/shareholder/relation` | Stock Shareholder Relation | `default` |
| [`get_shareholder`](#analysisget_shareholder) | `GET /analysis/shareholder/{code}` | Stock Shareholder Composition | `default` |
| [`get_shareholder_ksei`](#analysisget_shareholder_ksei) | `GET /analysis/shareholder/ksei/{code}` | Stock Shareholder KSEI | `default` |
| [`get_shareholder_classification`](#analysisget_shareholder_classification) | `GET /analysis/shareholder/classification/{code}` | Stock Shareholder Full Classification | `default` |
| [`get_shareholder_classify_table`](#analysisget_shareholder_classify_table) | `GET /analysis/shareholder/classify-table/{code}` | Stock Shareholder Classification Table | `default` |
| [`get_free_float`](#analysisget_free_float) | `GET /analysis/free-float/{code}` | Stock Free Float | `default` |
| [`get_summary_stock`](#analysisget_summary_stock) | `GET /analysis/summary/stock/{code}` | Stock Broker Summary | `default` |
| [`get_summary_broker`](#analysisget_summary_broker) | `GET /analysis/summary/broker/{code}` | Broker Broker Summary | `default` |
| [`get_sector_stalker`](#analysisget_sector_stalker) | `GET /analysis/stalker/sector` | Sector Stalker | `realtime` |
| [`get_sector_rotation`](#analysisget_sector_rotation) | `GET /analysis/sector/rotation` | Sector Rotation Chart | `realtime` |
| [`get_broker_stalker`](#analysisget_broker_stalker) | `GET /analysis/stalker/broker/{broker}/{stock}` | Stock Broker Stalker | `default` |
| [`get_broker_stalker_list`](#analysisget_broker_stalker_list) | `GET /analysis/stalker/list/{code}` | Broker Stalker List | `default` |
| [`get_summary_stock_chart`](#analysisget_summary_stock_chart) | `GET /analysis/summary-chart/stock/{code}` | Stock Broker Summary Chart | `default` |
| [`get_summary_broker_chart`](#analysisget_summary_broker_chart) | `GET /analysis/summary-chart/broker/{code}` | Broker Broker Summary Chart | `default` |
| [`get_inventory_stock_chart`](#analysisget_inventory_stock_chart) | `GET /analysis/inventory-chart/stock/{code}` | Stock Inventory Chart | `default` |
| [`get_inventory_broker_chart`](#analysisget_inventory_broker_chart) | `GET /analysis/inventory-chart/broker/{code}` | Broker Inventory Chart | `default` |
| [`get_momentum_chart`](#analysisget_momentum_chart) | `GET /analysis/momentum-chart/{code}` | Stock Momentum Chart | `realtime` |
| [`get_intraday_inventory_chart`](#analysisget_intraday_inventory_chart) | `GET /analysis/intraday-inventory-chart/{code}` | Stock Intraday Inventory Chart | `default` |
| [`get_sankey_chart`](#analysisget_sankey_chart) | `GET /analysis/sankey-chart/{code}` | Stock Distribution Chart | `default` |
| [`get_price_table`](#analysisget_price_table) | `GET /analysis/price-table/{code}` | Stock Price Table | `realtime` |
| [`get_time_table`](#analysisget_time_table) | `GET /analysis/time-table/{code}` | Stock Time Table | `realtime` |
| [`get_price_diary`](#analysisget_price_diary) | `GET /analysis/price-diary/{code}` | Stock Price Diary | `default` |
| [`get_price_seasonality`](#analysisget_price_seasonality) | `GET /analysis/price-seasonality/{code}` | Stock Price Seasonality | `default` |
| [`get_shareholder_above`](#analysisget_shareholder_above) | `GET /analysis/shareholder-above` | Stock Insider KSEI | `default` |
| [`get_shareholder_above_chart`](#analysisget_shareholder_above_chart) | `GET /analysis/shareholder-above-chart/{code}` | Stock Insider KSEI Chart | `default` |
| [`get_shareholder_one`](#analysisget_shareholder_one) | `GET /analysis/shareholder-one` | Stock Insider 1% | `default` |
| [`get_shareholder_one_chart`](#analysisget_shareholder_one_chart) | `GET /analysis/shareholder-one-chart/{code}` | Stock Insider 1% Chart | `default` |
| [`get_insider`](#analysisget_insider) | `GET /analysis/shareholder-insider` | Stock Insider IDX | `default` |
| [`get_insider_chart`](#analysisget_insider_chart) | `GET /analysis/insider-chart/{code}` | Stock Insider IDX Chart | `default` |
| [`get_financial_statement`](#analysisget_financial_statement) | `GET /analysis/financial-statement/{code}` | Stock Financial Statement | `default` |
| [`get_financial_statement_chart`](#analysisget_financial_statement_chart) | `GET /analysis/financial-statement-chart/{code}` | Stock Financial Statement Chart | `default` |
| [`get_keystat`](#analysisget_keystat) | `GET /analysis/keystat/{code}` | Stock Key Statistics | `default` |
| [`get_keystat_chart`](#analysisget_keystat_chart) | `GET /analysis/keystat-chart/{code}` | Stock Key Statistics Chart | `default` |
| [`get_flow_of_funds`](#analysisget_flow_of_funds) | `GET /analysis/flow-of-funds/{code}` | Stock Flow of Funds | `default` |
| [`get_calendar`](#analysisget_calendar) | `GET /analysis/calendar` | Stock Corporate Action Calendar | `default` |
| [`get_news`](#analysisget_news) | `GET /analysis/news` | Stock News | `default` |
| [`get_disclosure`](#analysisget_disclosure) | `GET /analysis/disclosure` | Stock Disclosure Information | `default` |

### analysis.get_stock_list

```python
client.analysis.get_stock_list() -> StockListResponse
```

**Stock List** — `GET /analysis/list/stock` — cache `default`

Get a complete list of all companies listed on the Indonesia Stock Exchange (IDX).

Return: `StockListResponse`


### analysis.get_broker_list

```python
client.analysis.get_broker_list() -> BrokerListResponse
```

**Broker List** — `GET /analysis/list/broker` — cache `default`

Get a complete list of all brokers/securities registered as exchange members at IDX.

Return: `BrokerListResponse`


### analysis.get_index_list

```python
client.analysis.get_index_list() -> IndexListResponse
```

**Index List** — `GET /analysis/list/index` — cache `default`

Get a complete list of all indexes available at IDX.

Return: `IndexListResponse`


### analysis.get_uma

```python
client.analysis.get_uma(page=None, limit=None, code=None) -> UmaResponse
```

**Stock UMA List** — `GET /analysis/uma` — cache `default`

Get the list of UMA (Unusual Market Activity) stock announcements from the Indonesia Stock Exchange (IDX).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah data per halaman, 1-100. |
| `code` | `str` | tidak |  | Filter kode saham, mis. `BBCA` (opsional). |

Return: `UmaResponse`


### analysis.get_suspend

```python
client.analysis.get_suspend(page=None, limit=None, code=None, active=None) -> SuspendResponse
```

**Stock Suspend List** — `GET /analysis/suspend` — cache `default`

Get the list of stock trading suspensions from the Indonesia Stock Exchange (IDX).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah data per halaman, 1-100. |
| `code` | `str` | tidak |  | Filter kode saham, mis. `BBCA` (opsional). |
| `active` | `bool` | tidak |  | `true`: hanya suspensi yang masih berlaku (end_date null); `false`: hanya yang sudah dicabut; kosongkan untuk semua (opsional). |

Return: `SuspendResponse`


### analysis.get_notation

```python
client.analysis.get_notation() -> NotationResponse
```

**Stock Notation List** — `GET /analysis/notation` — cache `default`

Get a complete list of special notations for all stocks listed on the Indonesia Stock Exchange (IDX), grouped by stock code and effective date.

Return: `NotationResponse`


### analysis.get_information

```python
client.analysis.get_information(code) -> InformationResponse
```

**Company Information** — `GET /analysis/information/{code}` — cache `default`

Get complete and detailed information about a company based on stock code.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |

Return: `InformationResponse`


### analysis.get_top_change

```python
client.analysis.get_top_change(date, filter_column=None, filter_operator=None, filter_value=None) -> TopChangeResponse
```

**Top Gainer & Loser** — `GET /analysis/top/change` — cache `default`

Get a list of stocks with the largest price increases and decreases on a specific day, complete with 5-day historical graph data.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `filter_column` | `TopChangeFilterColumn ("change", "value", "volume", "ratio")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `ratio` = rasio. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `TopChangeFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `TopChangeResponse`


### analysis.get_top_foreign

```python
client.analysis.get_top_foreign(date, filter_column=None, filter_operator=None, filter_value=None) -> TopForeignResponse
```

**Top Foreign Flow** — `GET /analysis/top/foreign` — cache `default`

Get a list of stocks with the largest foreign accumulation and distribution on a specific day, complete with 5-day historical graph data.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `filter_column` | `TopForeignFilterColumn ("change", "value", "volume", "ratio")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `ratio` = rasio. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `TopForeignFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `TopForeignResponse`


### analysis.get_top_accumulation

```python
client.analysis.get_top_accumulation(date, filter_column=None, filter_operator=None, filter_value=None) -> TopAccumulationResponse
```

**Top BDM Flow** — `GET /analysis/top/accumulation` — cache `default`

Get a list of stocks with the largest bandarmology accumulation and distribution on a specific day.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `filter_column` | `TopAccumulationFilterColumn ("change", "value", "volume", "ratio")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `ratio` = rasio. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `TopAccumulationFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `TopAccumulationResponse`


### analysis.get_top_ritel

```python
client.analysis.get_top_ritel(date, filter_column=None, filter_operator=None, filter_value=None) -> TopRitelResponse
```

**Top Ritel Flow** — `GET /analysis/top/ritel` — cache `default`

Get a list of stocks with the largest retail accumulation and distribution on a specific day.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `filter_column` | `TopRitelFilterColumn ("change", "value", "volume", "ratio")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `ratio` = rasio. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `TopRitelFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `TopRitelResponse`


### analysis.get_stock_running_trade

```python
client.analysis.get_stock_running_trade(code, date, page=None, limit=None, type=None, orderby=None, minimum=None, maximum=None, market=None, pricefrom=None, priceto=None, timefrom=None, timeto=None, sort=None) -> StockRunningTradeResponse
```

**Stock Running Trade** — `GET /analysis/running-trade/{code}` — cache `realtime`

Get realtime/historical running trade transaction data for a specific stock code.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `50` | Jumlah transaksi per halaman. |
| `type` | `StockRunningTradeType ("ALL", "BUY", "SELL")` | tidak | `ALL` | Sisi transaksi: `BUY` = match di harga offer (inisiatif beli), `SELL` = match di harga bid (inisiatif jual), `ALL` = seluruh transaksi. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `orderby` | `StockRunningTradeOrderby ("TIME", "PRICE", "VOLUME")` | tidak | `TIME` | Kolom pengurutan: `TIME` = waktu transaksi, `PRICE` = harga, `VOLUME` = volume. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `minimum` | `float` | tidak |  | Volume minimal transaksi yang ditampilkan, dalam lembar (1 lot = 100 lembar). Berguna untuk menyaring transaksi besar. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `maximum` | `float` | tidak |  | Volume maksimal transaksi yang ditampilkan, dalam lembar (1 lot = 100 lembar). Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `market` | `StockRunningTradeMarket ("ALL", "RG", "NG", "TN")` | tidak | `ALL` | Jenis pasar: `ALL` = seluruh pasar, `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `pricefrom` | `float` | tidak |  | Harga terendah transaksi yang ditampilkan (Rupiah). Menampilkan transaksi dengan harga >= `pricefrom`. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `priceto` | `float` | tidak |  | Harga tertinggi transaksi yang ditampilkan (Rupiah). Menampilkan transaksi dengan harga <= `priceto`. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `timefrom` | `str` | tidak |  | Jam awal transaksi dalam WIB, format `HH:mm` atau `HH:mm:ss`. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `timeto` | `str` | tidak |  | Jam akhir transaksi dalam WIB, format `HH:mm` atau `HH:mm:ss`. Tanpa detik, dihitung hingga detik ke-59. Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |
| `sort` | `StockRunningTradeSort ("ASC", "DESC")` | tidak | `ASC` | Arah pengurutan: `ASC` = menaik (terlama lebih dulu), `DESC` = menurun (terbaru lebih dulu). Diabaikan saat jam bursa (tanggal hari ini, 08:45–16:15 WIB pada hari bursa); hanya berlaku pada pengambilan data sehari penuh. |

Return: `StockRunningTradeResponse`


### analysis.get_intraday_chart

```python
client.analysis.get_intraday_chart(code, market) -> IntradayChartResponse
```

**Stock/Index Intraday Chart** — `GET /analysis/intraday/{code}` — cache `realtime`

Get intraday chart data for a stock with the latest date.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `market` | `IntradayChartMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `IntradayChartResponse`


### analysis.get_order_book

```python
client.analysis.get_order_book(code, market, date=None, time=None) -> OrderBookResponse
```

**Stock Order Book** — `GET /analysis/order-book/{code}` — cache `realtime`

Get order book data for a stock with the latest date or historical data at specific date/time.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `market` | `OrderBookMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |
| `date` | `Union[str, datetime.date]` | tidak |  | Tanggal order book historis (`YYYY-MM-DD`), tersedia mulai `2026-03-25`. Wajib dikirim bersama `time`; kosongkan keduanya untuk data realtime. |
| `time` | `str` | tidak |  | Jam snapshot order book dalam WIB, format `HH:mm` atau `HH:mm:ss` pada jam perdagangan (09:00–15:59); mengembalikan snapshot terdekat pada tanggal tersebut. Wajib dikirim bersama `date`. |

Return: `OrderBookResponse`


### analysis.get_order_queue

```python
client.analysis.get_order_queue(code, price, side, page=None, limit=None) -> OrderQueueResponse
```

**Stock Order Queue (Tracking)** — `GET /analysis/queue/{code}` — cache `realtime`

Get order queue (order tracking) for a stock at a specific price, side, page, and limit.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `price` | `int` | ya |  | Level harga order book (Rupiah) yang ingin dilihat detail antreannya. Harus sesuai fraksi harga saham. |
| `side` | `OrderQueueSide ("BUY", "SELL", "B", "S", "buy", "sell")` | ya |  | Sisi antrean: `BUY` = antrean beli (bid), `SELL` = antrean jual (offer). |
| `page` | `int` | tidak | `0` | Nomor halaman, dimulai dari 0. |
| `limit` | `int` | tidak | `50` | Jumlah order per halaman. |

Return: `OrderQueueResponse`


### analysis.get_intraday_data

```python
client.analysis.get_intraday_data(code, market, date=None) -> IntradayDataResponse
```

**Stock Intraday Data** — `GET /analysis/intraday-data/{code}` — cache `realtime`

Get intraday stock data with the latest date or historical data on a specific date.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `market` | `IntradayDataMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |
| `date` | `Union[str, datetime.date]` | tidak |  | Tanggal data historis (`YYYY-MM-DD`). Kosongkan untuk data realtime hari ini. |

Return: `IntradayDataResponse`


### analysis.get_intraday_index

```python
client.analysis.get_intraday_index(code) -> IntradayIndexResponse
```

**Index Intraday Data** — `GET /analysis/intraday-index/{code}` — cache `realtime`

Get intraday data for an index with the latest date.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode indeks BEI, mis. `COMPOSITE` (IHSG), `LQ45`, atau `IDX30`. Daftar kode tersedia di `/analysis/list/index`. |

Return: `IntradayIndexResponse`


### analysis.get_advance_chart

```python
client.analysis.get_advance_chart(code, from_=None, to=None) -> AdvanceChartResponse
```

**Stock Chart** — `GET /analysis/chart/stock/{code}` — cache `realtime`

Get complete stock price chart data with OHLCV data for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | tidak |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. Opsional; default 1 tahun sebelum hari ini (WIB). |
| `to` | `Union[str, datetime.date]` | tidak |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. Opsional; default hari ini (WIB). |

Return: `AdvanceChartResponse`


### analysis.get_index_chart

```python
client.analysis.get_index_chart(code, from_, to) -> IndexChartResponse
```

**Index Chart** — `GET /analysis/chart/index/{code}` — cache `realtime`

Get complete index price chart data with OHLCV data for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode indeks BEI, mis. `COMPOSITE` (IHSG), `LQ45`, atau `IDX30`. Daftar kode tersedia di `/analysis/list/index`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `IndexChartResponse`


### analysis.get_multi_time_chart

```python
client.analysis.get_multi_time_chart(code, from_, to, timeframe=None) -> MultiTimeChartResponse
```

**Stock/Index Multi Timeframe Chart** — `GET /analysis/chart/multi-time/{code}` — cache `realtime`

Get multi-timeframe chart data for stocks or indexes.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham (mis. `BBCA`) atau kode indeks (mis. `COMPOSITE`). Daftar kode tersedia di `/analysis/list/stock` dan `/analysis/list/index`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`. Batas data historis mengikuti `timeframe`. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `timeframe` | `MultiTimeChartTimeframe ("1", "5", "15", "30", "60", "D", "W", "M")` | tidak | `D` | Timeframe candle: `1`, `5`, `15`, `30`, `60` = menit; `D` = harian, `W` = mingguan, `M` = bulanan. Batas data historis: `1` = 3 bulan, `5` = 6 bulan, `15` = 12 bulan, lainnya 24 bulan. Opsional, default `D`; harus huruf kapital. |

Return: `MultiTimeChartResponse`


### analysis.get_indicator_chart

```python
client.analysis.get_indicator_chart(indicator, code, from_, to) -> IndicatorChartResponse
```

**Stock Chart Indicator** — `GET /analysis/chart/stock/{indicator}/{code}` — cache `default`

Get chart data with technical indicators for stock price analysis in a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `indicator` | `IndicatorChartIndicator ("bdm", "foreign", "ratio", "ritel", "freq", "lpm", "corr_f", "par_f", "intensity", "vol_ratio")` | ya |  | Indikator yang ditampilkan pada chart: `bdm` = aliran dana bandar, `foreign` = net beli/jual asing, `ritel` = aliran dana ritel, `freq` = frekuensi transaksi, `ratio` = rasio, `lpm` = Liquidity Pressure Model, `corr_f` = Correlation Foreign, `par_f` = Participation Foreign, `intensity` = Intensity, `vol_ratio` = Volume Rotation. Wajib huruf kecil. |
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `IndicatorChartResponse`


### analysis.get_shareholder_detail

```python
client.analysis.get_shareholder_detail(code=None, name=None) -> ShareholderDetailResponse
```

**Stock Shareholder 5%** — `GET /analysis/shareholder-detail` — cache `default`

Get company stock ownership data for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Kode saham yang ingin dilihat daftar pemegang sahamnya, mis. `BBCA`. Wajib diisi jika `name` kosong. |
| `name` | `str` | tidak |  | Nama pemegang saham untuk melihat seluruh saham yang dimilikinya. Wajib diisi jika `code` kosong. |

Return: `ShareholderDetailResponse`


### analysis.get_shareholder_one_detail

```python
client.analysis.get_shareholder_one_detail(code=None, name=None) -> ShareholderOneDetailResponse
```

**Stock Shareholder 1%** — `GET /analysis/shareholder-detail-one` — cache `default`

Get company stock ownership data based on stock code or shareholder name.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Kode saham yang ingin dilihat daftar pemegang sahamnya, mis. `BBCA`. Wajib diisi jika `name` kosong. |
| `name` | `str` | tidak |  | Nama pemegang saham untuk melihat seluruh saham yang dimilikinya. Wajib diisi jika `code` kosong. |

Return: `ShareholderOneDetailResponse`


### analysis.get_shareholder_high

```python
client.analysis.get_shareholder_high() -> ShareholderHighResponse
```

**Stock High Concentration** — `GET /analysis/shareholder/high` — cache `default`

Get high concentration stock ownership data for all issuers.

Return: `ShareholderHighResponse`


### analysis.get_shareholder_number

```python
client.analysis.get_shareholder_number(code) -> ShareholderNumberResponse
```

**Stock Shareholder Number** — `GET /analysis/shareholder/number/{code}` — cache `default`

Get the number of investors/shareholders of a company for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |

Return: `ShareholderNumberResponse`


### analysis.get_shareholder_relation

```python
client.analysis.get_shareholder_relation(code=None, name=None, depth=None, max_nodes=None, neighbors=None, min_percentage=None) -> ShareholderRelationResponse
```

**Stock Shareholder Relation** — `GET /analysis/shareholder/relation` — cache `default`

Get bidirectional shareholder relation graph data based on the latest stock ownership data.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Kode saham sebagai titik awal graf relasi kepemilikan. Wajib diisi jika `name` kosong. |
| `name` | `str` | tidak |  | Nama pemegang saham sebagai titik awal graf relasi kepemilikan. Wajib diisi jika `code` kosong. |
| `depth` | `int` | tidak | `3` | Kedalaman penelusuran relasi (jumlah lompatan). `1` = relasi langsung, `2` = termasuk relasi tingkat kedua, dan seterusnya. |
| `max_nodes` | `int` | tidak | `120` | Jumlah node maksimal (saham dan pemegang saham) dalam graf. Nilai lebih besar menghasilkan graf yang lebih lengkap dengan waktu proses lebih lama. |
| `neighbors` | `int` | tidak | `25` | Jumlah relasi maksimal yang diambil dari setiap node. |
| `min_percentage` | `float` | tidak | `1` | Persentase kepemilikan minimal yang ditampilkan. Mendukung desimal, mis. `5` untuk pemegang saham minimal 5%. |

Return: `ShareholderRelationResponse`


### analysis.get_shareholder

```python
client.analysis.get_shareholder(code) -> ShareholderResponse
```

**Stock Shareholder Composition** — `GET /analysis/shareholder/{code}` — cache `default`

Get company stock ownership composition data based on the largest shareholders on the latest date.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |

Return: `ShareholderResponse`


### analysis.get_shareholder_ksei

```python
client.analysis.get_shareholder_ksei(code, range) -> ShareholderKSEIResponse
```

**Stock Shareholder KSEI** — `GET /analysis/shareholder/ksei/{code}` — cache `default`

Get shareholder data based on KSEI classification (foreign and domestic investors in various groups) for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `range` | `int` | ya |  | Jumlah bulan terakhir yang ditampilkan, mis. `6` untuk 6 bulan terakhir. Akun TRIAL dibatasi maksimal 12 bulan. |

Return: `ShareholderKSEIResponse`


### analysis.get_shareholder_classification

```python
client.analysis.get_shareholder_classification(code, range) -> ShareholderClassificationResponse
```

**Stock Shareholder Full Classification** — `GET /analysis/shareholder/classification/{code}` — cache `default`

Get complete shareholder data with all investor classifications for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `range` | `int` | ya |  | Jumlah bulan terakhir yang ditampilkan, mis. `6` untuk 6 bulan terakhir. Akun TRIAL dibatasi maksimal 12 bulan. |

Return: `ShareholderClassificationResponse`


### analysis.get_shareholder_classify_table

```python
client.analysis.get_shareholder_classify_table(code) -> Optional[ShareholderClassifyTableResponse]
```

**Stock Shareholder Classification Table** — `GET /analysis/shareholder/classify-table/{code}` — cache `default`

Get latest shareholder data with investor classifications in table format.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |

Return: `Optional[ShareholderClassifyTableResponse]`


### analysis.get_free_float

```python
client.analysis.get_free_float(code, range) -> FreeFloatResponse
```

**Stock Free Float** — `GET /analysis/free-float/{code}` — cache `default`

Get the issuer's monthly free float share data for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `range` | `int` | ya |  | Jumlah bulan terakhir yang ditampilkan, mis. `6` untuk 6 bulan terakhir. Akun TRIAL dibatasi maksimal 12 bulan. |

Return: `FreeFloatResponse`


### analysis.get_summary_stock

```python
client.analysis.get_summary_stock(code, from_, to, investor, market) -> SummaryStockResponse
```

**Stock Broker Summary** — `GET /analysis/summary/stock/{code}` — cache `default`

Get detailed trading broker activity analysis for a specific stock within a specific time period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `investor` | `SummaryStockInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `market` | `SummaryStockMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `SummaryStockResponse`


### analysis.get_summary_broker

```python
client.analysis.get_summary_broker(code, from_, to, investor, market) -> SummaryBrokerResponse
```

**Broker Broker Summary** — `GET /analysis/summary/broker/{code}` — cache `default`

Get detailed trading activity analysis for a specific broker for all stocks within a specific time period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode broker anggota bursa (2 huruf), mis. `AK`. Dapat berisi beberapa kode yang dipisahkan koma, mis. `AK,BK,YP`. Daftar broker tersedia di `/analysis/list/broker`. Kode yang tidak terdiri dari 2 karakter akan diabaikan. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `investor` | `SummaryBrokerInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `market` | `SummaryBrokerMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `SummaryBrokerResponse`


### analysis.get_sector_stalker

```python
client.analysis.get_sector_stalker(from_, to, base=None, limit=None, filter=None, filter_column=None, filter_operator=None, filter_value=None) -> SectorStalkerResponse
```

**Sector Stalker** — `GET /analysis/stalker/sector` — cache `realtime`

Get sectoral index or stock price movement data within a specific time range.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `base` | `SectorStalkerBase ("COMPOSITE", "SYARIAH", "IDXENERGY", "IDXBASIC", "IDXINDUST", "IDXNONCYC", "IDXCYCLIC", "IDXHEALTH", "IDXFINANCE", "IDXPROPERT", "IDXTECHNO", "IDXINFRA", "IDXTRANS")` | tidak | `COMPOSITE` | Indeks acuan. `COMPOSITE` (IHSG) menampilkan rotasi antar sektor, sedangkan `SYARIAH` (saham syariah, dibandingkan dengan indeks ISSI) atau indeks sektoral IDX-IC (`IDXENERGY`, `IDXFINANCE`, dst.) menampilkan rotasi saham anggota kategori tersebut. `ISSI` diterima sebagai alias `SYARIAH`. Wajib huruf kapital. |
| `limit` | `int` | tidak |  | Jumlah saham maksimal yang ditampilkan. Hanya berlaku jika `base` bukan `COMPOSITE`. |
| `filter` | `str` | tidak |  | Pencarian saham berdasarkan sebagian kode atau nama, mis. `BB` atau `BANK`. Hanya berlaku jika `base` bukan `COMPOSITE`. |
| `filter_column` | `SectorStalkerFilterColumn ("change", "value", "volume", "foreign", "freq", "bdm", "ritel", "ratio", "open", "high", "low", "close")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `foreign` = net asing, `freq` = frekuensi, `bdm` = aliran dana bandar, `ritel` = aliran dana ritel, `ratio` = rasio, `open`/`high`/`low`/`close` = harga OHLC. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `SectorStalkerFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `SectorStalkerResponse`


### analysis.get_sector_rotation

```python
client.analysis.get_sector_rotation(from_, to, base=None, length=None, interval=None, tail=None, limit=None, filter=None, filter_column=None, filter_operator=None, filter_value=None) -> SectorRotationResponse
```

**Sector Rotation Chart** — `GET /analysis/sector/rotation` — cache `realtime`

Get sector rotation data for visualizing relative movement of sectoral indices or stocks.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `base` | `SectorRotationBase ("COMPOSITE", "SYARIAH", "IDXENERGY", "IDXBASIC", "IDXINDUST", "IDXNONCYC", "IDXCYCLIC", "IDXHEALTH", "IDXFINANCE", "IDXPROPERT", "IDXTECHNO", "IDXINFRA", "IDXTRANS")` | tidak | `COMPOSITE` | Indeks acuan. `COMPOSITE` (IHSG) menampilkan rotasi antar sektor, sedangkan `SYARIAH` (saham syariah, dibandingkan dengan indeks ISSI) atau indeks sektoral IDX-IC (`IDXENERGY`, `IDXFINANCE`, dst.) menampilkan rotasi saham anggota kategori tersebut. `ISSI` diterima sebagai alias `SYARIAH`. Wajib huruf kapital. |
| `length` | `int` | tidak | `10` | Periode smoothing untuk menghitung RS-Ratio dan RS-Momentum. Nilai kecil lebih responsif, nilai besar lebih halus. |
| `interval` | `SectorRotationInterval ("daily", "weekly")` | tidak | `weekly` | Interval data pada Relative Rotation Graph (RRG): `daily` = harian, `weekly` = mingguan. |
| `tail` | `int` | tidak | `5` | Jumlah titik jejak (tail) per sektor atau saham untuk menunjukkan arah pergerakan. |
| `limit` | `int` | tidak |  | Jumlah saham maksimal yang ditampilkan. Hanya berlaku jika `base` bukan `COMPOSITE`. |
| `filter` | `str` | tidak |  | Pencarian saham berdasarkan sebagian kode atau nama, mis. `BB` atau `BANK`. Hanya berlaku jika `base` bukan `COMPOSITE`. |
| `filter_column` | `SectorRotationFilterColumn ("change", "value", "volume", "foreign", "freq", "bdm", "ritel", "ratio", "open", "high", "low", "close")` | tidak |  | Kolom yang difilter: `change` = perubahan harga (%), `value` = nilai transaksi, `volume` = volume, `foreign` = net asing, `freq` = frekuensi, `bdm` = aliran dana bandar, `ritel` = aliran dana ritel, `ratio` = rasio, `open`/`high`/`low`/`close` = harga OHLC. Filter aktif hanya jika `filter_column`, `filter_operator`, dan `filter_value` dikirim bersamaan. |
| `filter_operator` | `SectorRotationFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk filter. Contoh: `filter_column=change&filter_operator=>&filter_value=5` menampilkan saham yang naik lebih dari 5%. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk filter. Mendukung bilangan desimal dan negatif, mis. `5` atau `-2.5`. |

Return: `SectorRotationResponse`


### analysis.get_broker_stalker

```python
client.analysis.get_broker_stalker(broker, stock, from_, to, investor, market) -> BrokerStalkerResponse
```

**Stock Broker Stalker** — `GET /analysis/stalker/broker/{broker}/{stock}` — cache `default`

Track a specific broker's trading activity on a specific stock in daily calendar format.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `broker` | `str` | ya |  | Kode broker anggota bursa (2 huruf), mis. `AK`. Dapat berisi beberapa kode yang dipisahkan koma, mis. `AK,BK,YP`. Daftar broker tersedia di `/analysis/list/broker`. Kode yang tidak terdiri dari 2 karakter akan diabaikan. |
| `stock` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `investor` | `BrokerStalkerInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `market` | `BrokerStalkerMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `BrokerStalkerResponse`


### analysis.get_broker_stalker_list

```python
client.analysis.get_broker_stalker_list(code, from_, to, investor, market) -> BrokerStalkerListResponse
```

**Broker Stalker List** — `GET /analysis/stalker/list/{code}` — cache `default`

Get list of all stocks traded by a specific broker within a specific time period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode broker anggota bursa (2 huruf), mis. `AK`. Dapat berisi beberapa kode yang dipisahkan koma, mis. `AK,BK,YP`. Daftar broker tersedia di `/analysis/list/broker`. Kode yang tidak terdiri dari 2 karakter akan diabaikan. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `investor` | `BrokerStalkerListInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `market` | `BrokerStalkerListMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `BrokerStalkerListResponse`


### analysis.get_summary_stock_chart

```python
client.analysis.get_summary_stock_chart(code, from_, to, scope, market) -> SummaryStockChartResponse
```

**Stock Broker Summary Chart** — `GET /analysis/summary-chart/stock/{code}` — cache `default`

Get broker summary infographic data for a specific stock with attractive visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `scope` | `SummaryStockChartScope ("volume", "value", "freq")` | ya |  | Metrik yang dihitung: `volume` = jumlah lembar saham, `value` = nilai transaksi (Rupiah), `freq` = frekuensi transaksi. |
| `market` | `SummaryStockChartMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `SummaryStockChartResponse`


### analysis.get_summary_broker_chart

```python
client.analysis.get_summary_broker_chart(code, from_, to, scope, market) -> SummaryBrokerChartResponse
```

**Broker Broker Summary Chart** — `GET /analysis/summary-chart/broker/{code}` — cache `default`

Get broker summary infographic data for a specific broker with attractive visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode broker anggota bursa (2 huruf), mis. `AK`. Dapat berisi beberapa kode yang dipisahkan koma, mis. `AK,BK,YP`. Daftar broker tersedia di `/analysis/list/broker`. Kode yang tidak terdiri dari 2 karakter akan diabaikan. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `scope` | `SummaryBrokerChartScope ("volume", "value", "freq")` | ya |  | Metrik yang dihitung: `volume` = jumlah lembar saham, `value` = nilai transaksi (Rupiah), `freq` = frekuensi transaksi. |
| `market` | `SummaryBrokerChartMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `SummaryBrokerChartResponse`


### analysis.get_inventory_stock_chart

```python
client.analysis.get_inventory_stock_chart(code, from_, to, scope, investor, limit=None, market, filter=None, filter_operator=None, filter_value=None) -> InventoryStockChartResponse
```

**Stock Inventory Chart** — `GET /analysis/inventory-chart/stock/{code}` — cache `default`

Get inventory chart data for a specific stock with broker activity visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `scope` | `InventoryStockChartScope ("vol", "val", "freq")` | ya |  | Metrik inventori: `vol` = volume (lembar saham), `val` = nilai transaksi (Rupiah), `freq` = frekuensi transaksi. |
| `investor` | `InventoryStockChartInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `limit` | `int` | tidak | `20` | Jumlah broker teratas yang ditampilkan. |
| `market` | `InventoryStockChartMarket ("ALL", "RG", "NG", "TN")` | ya |  | Jenis pasar: `ALL` = seluruh pasar, `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. |
| `filter` | `str` | tidak |  | Kode broker yang ingin ditampilkan, dipisahkan koma, mis. `AK,BK`. Kosongkan untuk menampilkan broker teratas. |
| `filter_operator` | `InventoryStockChartFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Saat ini tidak digunakan pada endpoint ini. |
| `filter_value` | `float` | tidak |  | Saat ini tidak digunakan pada endpoint ini. |

Return: `InventoryStockChartResponse`


### analysis.get_inventory_broker_chart

```python
client.analysis.get_inventory_broker_chart(code, from_, to, scope, investor, limit=None, market, filter=None, filter_operator=None, filter_value=None) -> InventoryBrokerChartResponse
```

**Broker Inventory Chart** — `GET /analysis/inventory-chart/broker/{code}` — cache `default`

Get inventory chart data for a specific broker with stock activity visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode broker anggota bursa (2 huruf), mis. `AK`. Dapat berisi beberapa kode yang dipisahkan koma, mis. `AK,BK,YP`. Daftar broker tersedia di `/analysis/list/broker`. Setiap kode wajib 2 karakter. |
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). Harus lebih kecil atau sama dengan `to`, dengan rentang maksimal 730 hari. |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `scope` | `InventoryBrokerChartScope ("vol", "val", "freq")` | ya |  | Metrik inventori: `vol` = volume (lembar saham), `val` = nilai transaksi (Rupiah), `freq` = frekuensi transaksi. |
| `investor` | `InventoryBrokerChartInvestor ("all", "f", "d")` | ya |  | Jenis investor yang dihitung: `all` = seluruh investor, `f` = investor asing, `d` = investor domestik. |
| `limit` | `int` | tidak | `20` | Jumlah saham teratas yang ditampilkan. |
| `market` | `InventoryBrokerChartMarket ("ALL", "RG", "NG", "TN")` | ya |  | Jenis pasar: `ALL` = seluruh pasar, `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. |
| `filter` | `str` | tidak |  | Kode saham yang ingin ditampilkan, dipisahkan koma, mis. `BBCA,BBRI`. Kosongkan untuk menampilkan saham teratas. |
| `filter_operator` | `InventoryBrokerChartFilterOperator ("<", ">", "=", ">=", "<=", "!=")` | tidak |  | Operator pembanding untuk memfilter nilai `scope`. Digunakan bersama `filter_value`. |
| `filter_value` | `float` | tidak |  | Nilai pembanding untuk `filter_operator`. Contoh: `>` dengan nilai `0` menampilkan saham yang terakumulasi (net beli). |

Return: `InventoryBrokerChartResponse`


### analysis.get_momentum_chart

```python
client.analysis.get_momentum_chart(code, date, range, scope) -> MomentumChartResponse
```

**Stock Momentum Chart** — `GET /analysis/momentum-chart/{code}` — cache `realtime`

Get momentum chart data for real-time transaction analysis with HAKA HAKI details for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `range` | `int` | ya |  | Interval waktu dalam menit, mis. `5` untuk per 5 menit atau `60` untuk per jam. |
| `scope` | `MomentumChartScope ("value", "volume")` | ya |  | Basis perhitungan: `value` = nilai transaksi (Rupiah), `volume` = jumlah lembar saham. |

Return: `MomentumChartResponse`


### analysis.get_intraday_inventory_chart

```python
client.analysis.get_intraday_inventory_chart(code, date, range, type, total, buyer, seller, filter=None, market) -> IntradayInventoryChartResponse
```

**Stock Intraday Inventory Chart** — `GET /analysis/intraday-inventory-chart/{code}` — cache `default`

Get intraday inventory chart data for transaction analysis with broker activity details for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `range` | `int` | ya |  | Interval waktu dalam menit, mis. `5` untuk per 5 menit atau `60` untuk per jam. |
| `type` | `IntradayInventoryChartType ("value", "volume")` | ya |  | Basis perhitungan: `value` = nilai transaksi (Rupiah), `volume` = jumlah lembar saham. |
| `total` | `int` | ya |  | Jumlah broker teratas yang ditampilkan. |
| `buyer` | `IntradayInventoryChartBuyer ("ALL", "F", "D")` | ya |  | Jenis investor di sisi pembeli: `ALL` = seluruh investor, `F` = asing, `D` = domestik. |
| `seller` | `IntradayInventoryChartSeller ("ALL", "F", "D")` | ya |  | Jenis investor di sisi penjual: `ALL` = seluruh investor, `F` = asing, `D` = domestik. |
| `filter` | `str` | tidak |  | Kode broker yang ingin ditampilkan, dipisahkan koma, mis. `AK,BK`. Kosongkan untuk menampilkan broker teratas. |
| `market` | `IntradayInventoryChartMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `IntradayInventoryChartResponse`


### analysis.get_sankey_chart

```python
client.analysis.get_sankey_chart(code, date, type, buyer, seller, market) -> SankeyChartResponse
```

**Stock Distribution Chart** — `GET /analysis/sankey-chart/{code}` — cache `default`

Get sankey chart data for crossing transaction visualization with broker flow details for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `type` | `SankeyChartType ("value", "volume")` | ya |  | Basis perhitungan: `value` = nilai transaksi (Rupiah), `volume` = jumlah lembar saham. |
| `buyer` | `SankeyChartBuyer ("ALL", "F", "D")` | ya |  | Jenis investor di sisi pembeli: `ALL` = seluruh investor, `F` = asing, `D` = domestik. |
| `seller` | `SankeyChartSeller ("ALL", "F", "D")` | ya |  | Jenis investor di sisi penjual: `ALL` = seluruh investor, `F` = asing, `D` = domestik. |
| `market` | `SankeyChartMarket ("RG", "NG", "TN")` | ya |  | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. |

Return: `SankeyChartResponse`


### analysis.get_price_table

```python
client.analysis.get_price_table(code, date) -> PriceTableResponse
```

**Stock Price Table** — `GET /analysis/price-table/{code}` — cache `realtime`

Get daily stock trading price transaction table with volume and frequency details for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |

Return: `PriceTableResponse`


### analysis.get_time_table

```python
client.analysis.get_time_table(code, date, range) -> TimeTableResponse
```

**Stock Time Table** — `GET /analysis/time-table/{code}` — cache `realtime`

Get daily stock trading time transaction table with HAKA/HAKI volume (lots) and percentage details per time interval for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data (`YYYY-MM-DD`). Gunakan hari bursa; tanggal libur bursa dapat menghasilkan data kosong. |
| `range` | `int` | ya |  | Interval waktu dalam menit, mis. `5` untuk per 5 menit atau `60` untuk per jam. |

Return: `TimeTableResponse`


### analysis.get_price_diary

```python
client.analysis.get_price_diary(code) -> PriceDiaryResponse
```

**Stock Price Diary** — `GET /analysis/price-diary/{code}` — cache `default`

Get daily stock price change table for the last 30 trading days (no period parameter).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |

Return: `PriceDiaryResponse`


### analysis.get_price_seasonality

```python
client.analysis.get_price_seasonality(code, range) -> PriceSeasonalityResponse
```

**Stock Price Seasonality** — `GET /analysis/price-seasonality/{code}` — cache `default`

Get monthly stock price change table with seasonality analysis for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `range` | `int` | ya |  | Jumlah tahun data historis untuk menghitung pola musiman harga bulanan, mis. `3` untuk 3 tahun terakhir. Nilai efektif maksimal 20. |

Return: `PriceSeasonalityResponse`


### analysis.get_shareholder_above

```python
client.analysis.get_shareholder_above(code=None, broker=None, name=None, from_=None, to=None, page=None, limit=None) -> ShareholderAboveResponse
```

**Stock Insider KSEI** — `GET /analysis/shareholder-above` — cache `default`

Get a list of ownership changes above 5% based on exchange reports for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Filter berdasarkan kode saham. Dapat berisi beberapa kode yang dipisahkan koma, mis. `BBCA,BBRI,BMRI`. |
| `broker` | `str` | tidak |  | Filter berdasarkan broker/kustodian tempat saham disimpan (kode 2 huruf). Dapat berisi beberapa kode yang dipisahkan koma. |
| `name` | `str` | tidak |  | Nama atau sebagian nama pemegang saham yang dicari. Kosongkan untuk menampilkan seluruh pemegang saham. |
| `from_` | `Union[str, datetime.date]` | tidak |  | Tanggal awal periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `to` | `Union[str, datetime.date]` | tidak |  | Tanggal akhir periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah transaksi per halaman. |

Return: `ShareholderAboveResponse`


### analysis.get_shareholder_above_chart

```python
client.analysis.get_shareholder_above_chart(code, broker=None, name=None, date) -> ShareholderAboveChartResponse
```

**Stock Insider KSEI Chart** — `GET /analysis/shareholder-above-chart/{code}` — cache `default`

Get chart data for ownership visualization above 5% for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `broker` | `str` | tidak |  | Filter berdasarkan broker/kustodian (kode 2 huruf). Gunakan `INSTITUSI` untuk menampilkan kepemilikan institusi. |
| `name` | `str` | tidak |  | Nama pemegang saham dengan kepemilikan di atas 5% yang ingin ditampilkan. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data kepemilikan (`YYYY-MM-DD`). Wajib diisi. |

Return: `ShareholderAboveChartResponse`


### analysis.get_shareholder_one

```python
client.analysis.get_shareholder_one(code=None, name=None, from_=None, to=None, page=None, limit=None) -> ShareholderOneResponse
```

**Stock Insider 1%** — `GET /analysis/shareholder-one` — cache `default`

Get a list of ownership changes above 1% based on exchange reports for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Filter berdasarkan kode saham. Dapat berisi beberapa kode yang dipisahkan koma, mis. `BBCA,BBRI,BMRI`. |
| `name` | `str` | tidak |  | Nama atau sebagian nama pemegang saham yang dicari. Kosongkan untuk menampilkan seluruh pemegang saham. |
| `from_` | `Union[str, datetime.date]` | tidak |  | Tanggal awal periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `to` | `Union[str, datetime.date]` | tidak |  | Tanggal akhir periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah transaksi per halaman. |

Return: `ShareholderOneResponse`


### analysis.get_shareholder_one_chart

```python
client.analysis.get_shareholder_one_chart(code, name=None, date) -> ShareholderOneChartResponse
```

**Stock Insider 1% Chart** — `GET /analysis/shareholder-one-chart/{code}` — cache `default`

Get chart data for ownership visualization above 1% for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `name` | `str` | tidak |  | Nama pemegang saham dengan kepemilikan 1%–5% yang ingin ditampilkan. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal data kepemilikan (`YYYY-MM-DD`). Wajib diisi. |

Return: `ShareholderOneChartResponse`


### analysis.get_insider

```python
client.analysis.get_insider(code=None, name=None, from_=None, to=None, page=None, limit=None) -> InsiderResponse
```

**Stock Insider IDX** — `GET /analysis/shareholder-insider` — cache `default`

Get a list of insider ownership changes (directors, commissioners, majority shareholders) for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Filter berdasarkan kode saham. Dapat berisi beberapa kode yang dipisahkan koma, mis. `BBCA,BBRI,BMRI`. |
| `name` | `str` | tidak |  | Nama atau sebagian nama pemegang saham yang dicari. Kosongkan untuk menampilkan seluruh pemegang saham. |
| `from_` | `Union[str, datetime.date]` | tidak |  | Tanggal awal periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `to` | `Union[str, datetime.date]` | tidak |  | Tanggal akhir periode laporan (`YYYY-MM-DD`). Opsional; filter tanggal hanya berlaku bila `from` dan `to` sama-sama diisi. |
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah transaksi per halaman. |

Return: `InsiderResponse`


### analysis.get_insider_chart

```python
client.analysis.get_insider_chart(code, name=None, date) -> InsiderChartResponse
```

**Stock Insider IDX Chart** — `GET /analysis/insider-chart/{code}` — cache `default`

Get chart data for insider trading visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `name` | `str` | tidak |  | Nama insider (direksi, komisaris, atau pemegang saham pengendali) yang ingin ditampilkan. |
| `date` | `Union[str, datetime.date]` | ya |  | Tanggal laporan transaksi insider di BEI (`YYYY-MM-DD`). Wajib diisi. |

Return: `InsiderChartResponse`


### analysis.get_financial_statement

```python
client.analysis.get_financial_statement(code, statement, type, limit=None) -> FinancialStatementResponse
```

**Stock Financial Statement** — `GET /analysis/financial-statement/{code}` — cache `default`

Get company financial statement data based on report type and specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `statement` | `FinancialStatementStatement ("BS", "IS", "CF")` | ya |  | Jenis laporan keuangan: `BS` = neraca (balance sheet), `IS` = laba rugi (income statement), `CF` = arus kas (cash flow). |
| `type` | `FinancialStatementType ("FY", "Q", "Q1", "Q2", "Q3", "Q4")` | ya |  | Periode laporan: `FY` = tahunan, `Q` = seluruh kuartal, `Q1`–`Q4` = kuartal tertentu. |
| `limit` | `int` | tidak | `8` | Jumlah periode laporan terakhir yang ditampilkan. |

Return: `FinancialStatementResponse`


### analysis.get_financial_statement_chart

```python
client.analysis.get_financial_statement_chart(code, statement, type, limit=None, account) -> FinancialStatementChartResponse
```

**Stock Financial Statement Chart** — `GET /analysis/financial-statement-chart/{code}` — cache `default`

Get chart data for financial statement visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `statement` | `FinancialStatementChartStatement ("BS", "IS", "CF")` | ya |  | Jenis laporan keuangan: `BS` = neraca (balance sheet), `IS` = laba rugi (income statement), `CF` = arus kas (cash flow). |
| `type` | `FinancialStatementChartType ("FY", "Q", "Q1", "Q2", "Q3", "Q4")` | ya |  | Periode laporan: `FY` = tahunan, `Q` = seluruh kuartal, `Q1`–`Q4` = kuartal tertentu. |
| `limit` | `int` | tidak | `8` | Jumlah periode laporan terakhir yang ditampilkan. |
| `account` | `str` | ya |  | ID akun laporan keuangan (string 32 karakter) yang akan ditampilkan sebagai grafik. Gunakan nilai `rows[].id` dari response `/analysis/financial-statement/{code}` dengan `statement` yang sama; ID yang tidak ditemukan menghasilkan `account_id`/`name` null dengan `amount` 0. |

Return: `FinancialStatementChartResponse`


### analysis.get_keystat

```python
client.analysis.get_keystat(code, type, limit=None) -> KeystatResponse
```

**Stock Key Statistics** — `GET /analysis/keystat/{code}` — cache `default`

Get key statistics and important financial metrics of a company for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `type` | `KeystatType ("FY", "Q", "Q1", "Q2", "Q3", "Q4")` | ya |  | Periode laporan: `FY` = tahunan, `Q` = seluruh kuartal, `Q1`–`Q4` = kuartal tertentu. |
| `limit` | `int` | tidak | `8` | Jumlah periode terakhir yang ditampilkan. |

Return: `KeystatResponse`


### analysis.get_keystat_chart

```python
client.analysis.get_keystat_chart(code, type, limit=None, name) -> KeystatChartResponse
```

**Stock Key Statistics Chart** — `GET /analysis/keystat-chart/{code}` — cache `default`

Get chart data for key statistics visualization for a specific period.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `type` | `KeystatChartType ("FY", "Q", "Q1", "Q2", "Q3", "Q4")` | ya |  | Periode laporan: `FY` = tahunan, `Q` = seluruh kuartal, `Q1`–`Q4` = kuartal tertentu. |
| `limit` | `int` | tidak | `8` | Jumlah periode terakhir yang ditampilkan (default 8). Maksimal 8 untuk periode kuartalan (`Q`, `Q1`-`Q4`) dan 3 untuk `type=FY`; karena default 8 melebihi batas FY, `limit` (1-3) wajib diisi saat `type=FY`. |
| `name` | `str` | ya |  | Nama rasio atau statistik kunci yang akan ditampilkan sebagai grafik, mis. `ROE`, `PER`, atau `PBV`. Gunakan nama yang sama persis dengan response `/analysis/keystat/{code}`. |

Return: `KeystatChartResponse`


### analysis.get_flow_of_funds

```python
client.analysis.get_flow_of_funds(code, type, limit=None) -> FlowOfFundsResponse
```

**Stock Flow of Funds** — `GET /analysis/flow-of-funds/{code}` — cache `default`

Get a company's income statement flow of funds (Sankey) per period: revenue by product/service, cost of revenue and its breakdown, operating expenses, operating profit, profit before tax, tax, net profit and profit attributable to the parent.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham emiten yang tercatat di BEI, mis. `BBCA`. Tidak case-sensitive. Daftar kode tersedia di `/analysis/list/stock`. |
| `type` | `FlowOfFundsType ("FY", "Q", "Q1", "Q2", "Q3", "Q4")` | ya |  | Periode laporan: `FY` = tahunan, `Q` = seluruh kuartal, `Q1`–`Q4` = kuartal tertentu. |
| `limit` | `int` | tidak | `8` | Jumlah periode terakhir yang ditampilkan. |

Return: `FlowOfFundsResponse`


### analysis.get_calendar

```python
client.analysis.get_calendar(code=None, type=None, page=None, limit=None) -> CalendarResponse
```

**Stock Corporate Action Calendar** — `GET /analysis/calendar` — cache `default`

Get the corporate action schedule of IDX issuers, newest first, with optional filters.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | tidak |  | Filter hasil untuk satu kode saham tertentu. |
| `type` | `CalendarType ("IPO", "PUBLIC_EXPOSE", "REVERSE", "RIGHT", "RUPS_RESULT", "RUPS_SCHEDULE", "SPLIT", "WARRANT", "BONUS", "CONVERTION", "DIVIDEND")` | tidak |  | Jenis aksi korporasi: `IPO`, `PUBLIC_EXPOSE` = paparan publik, `RUPS_SCHEDULE` / `RUPS_RESULT` = jadwal / hasil RUPS, `DIVIDEND`, `RIGHT` = rights issue, `WARRANT`, `BONUS`, `SPLIT` = stock split, `REVERSE` = reverse split, `CONVERTION` = konversi. |
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah data per halaman. |

Return: `CalendarResponse`


### analysis.get_news

```python
client.analysis.get_news(page=None, limit=None, code=None) -> NewsResponse
```

**Stock News** — `GET /analysis/news` — cache `default`

Get the stock news listing (NEWS-category posts).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah data per halaman, 1-100. |
| `code` | `str` | tidak |  | Filter kode saham, mis. `BBCA` (opsional). |

Return: `NewsResponse`


### analysis.get_disclosure

```python
client.analysis.get_disclosure(page=None, limit=None, code=None, type=None) -> DisclosureResponse
```

**Stock Disclosure Information** — `GET /analysis/disclosure` — cache `default`

Get the IDX disclosure listing.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | tidak | `1` | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | tidak | `20` | Jumlah data per halaman, 1-100. |
| `code` | `str` | tidak |  | Filter kode saham, mis. `BBCA` (opsional). |
| `type` | `DisclosureType ("shareholder", "financial", "rups", "volatility_explanation", "press_release", "public_expose", "right_issue", "dividen", "ad_publication", "use_of_proceeds", "exchange_clarification", "trading_suspension", "operational_report", "annual_report", "financial_info", "rating", "structured_warrant", "bond", "management", "buyback", "ownership", "capital_action", "public_offering", "material_transaction", "agreement", "corporate_group", "articles_identity", "legal", "material_info", "other")` | tidak |  | Filter tipe laporan (opsional, huruf besar/kecil bebas). |

Return: `DisclosureResponse`


## client.batch

Batch endpoints: fetch many stocks in one request (counted as 1 request).

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`get_order_book`](#batchget_order_book) | `GET /batch/order-book/{code}` | Batch Stock Order Book | `realtime` |
| [`get_intraday_data`](#batchget_intraday_data) | `GET /batch/intraday-data/{code}` | Batch Stock Intraday Data | `realtime` |
| [`get_intraday_index`](#batchget_intraday_index) | `GET /batch/intraday-index/{code}` | Batch Index Intraday Data | `realtime` |

### batch.get_order_book

```python
client.batch.get_order_book(code, market=None, date=None, time=None) -> BatchOrderBookResponse
```

**Batch Stock Order Book** — `GET /batch/order-book/{code}` — cache `realtime`

Get order book data for multiple stocks at once in a single request (up to 10 codes on the MAX plan, 25 on the ELITE plan).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Daftar kode saham yang dipisahkan `\|` atau koma, mis. `BBCA\|GOTO\|TLKM`. Maksimal 10 kode (paket MAX) atau 25 kode (paket ELITE) per request. |
| `market` | `BatchOrderBookMarket ("RG", "NG", "TN")` | tidak | `RG` | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. Default `RG` bila tidak diisi. |
| `date` | `Union[str, datetime.date]` | tidak |  | Tanggal order book historis (`YYYY-MM-DD`), data tersedia mulai `2026-03-25`. Kirim bersama `time`; kosongkan keduanya untuk data realtime. |
| `time` | `str` | tidak |  | Jam order book dalam WIB, format `HH:mm` dengan presisi menit. Kirim bersama `date`. |

Return: `BatchOrderBookResponse`


### batch.get_intraday_data

```python
client.batch.get_intraday_data(code, market=None, date=None) -> BatchIntradayDataResponse
```

**Batch Stock Intraday Data** — `GET /batch/intraday-data/{code}` — cache `realtime`

Get compact intraday price data for multiple stocks at once in a single request (up to 10 codes on the MAX plan, 25 on the ELITE plan).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Daftar kode saham yang dipisahkan `\|` atau koma, mis. `BBCA\|GOTO\|TLKM`. Maksimal 10 kode (paket MAX) atau 25 kode (paket ELITE) per request. |
| `market` | `BatchIntradayDataMarket ("RG", "NG", "TN")` | tidak | `RG` | Jenis pasar: `RG` = Pasar Reguler, `NG` = Pasar Negosiasi, `TN` = Pasar Tunai. Gunakan `RG` untuk analisis pergerakan harga pada umumnya. Default `RG` bila tidak diisi. |
| `date` | `Union[str, datetime.date]` | tidak |  | Tanggal data historis (`YYYY-MM-DD`). Kosongkan untuk data realtime hari ini. |

Return: `BatchIntradayDataResponse`


### batch.get_intraday_index

```python
client.batch.get_intraday_index(code) -> BatchIntradayIndexResponse
```

**Batch Index Intraday Data** — `GET /batch/intraday-index/{code}` — cache `realtime`

Get compact intraday data for multiple indexes at once in a single request (up to 10 codes on the MAX plan, 25 on the ELITE plan).

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Daftar kode indeks yang dipisahkan `\|` atau koma, mis. `COMPOSITE\|LQ45\|IDX30`. Maksimal 10 kode (paket MAX) atau 25 kode (paket ELITE) per request. Daftar indeks tersedia di `/analysis/list/index`. |

Return: `BatchIntradayIndexResponse`


## client.search

Search stocks and users.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`search`](#searchsearch) | `GET /search` | Search Stock or User | `default` |
| [`search_stock`](#searchsearch_stock) | `GET /search/stock` | Search Stock only | `default` |
| [`search_user`](#searchsearch_user) | `GET /search/user` | Search User only | `default` |

### search.search

```python
client.search.search(query) -> SearchResponse
```

**Search Stock or User** — `GET /search` — cache `default`

Search for stocks or users simultaneously based on query keywords.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `query` | `str` | ya |  | Kata kunci pencarian berupa kode saham, nama perusahaan, atau username. |

Return: `SearchResponse`


### search.search_stock

```python
client.search.search_stock(query, cursor=None) -> SearchStockResponse
```

**Search Stock only** — `GET /search/stock` — cache `default`

Search for stock data listed on the Indonesia Stock Exchange (IDX) based on query keywords with pagination support.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `query` | `str` | ya |  | Kata kunci pencarian berupa kode saham atau nama perusahaan. |
| `cursor` | `int` | tidak | `1` | Nomor halaman hasil pencarian, dimulai dari 1. Setiap halaman berisi 20 hasil. |

Return: `SearchStockResponse`


### search.search_user

```python
client.search.search_user(query, cursor=None) -> SearchUserResponse
```

**Search User only** — `GET /search/user` — cache `default`

Search for Invezgo app users based on query keywords with pagination support.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `query` | `str` | ya |  | Kata kunci pencarian berupa username atau nama pengguna. |
| `cursor` | `int` | tidak | `1` | Nomor halaman hasil pencarian, dimulai dari 1. Setiap halaman berisi 20 hasil. |

Return: `SearchUserResponse`


## client.screener

Run stock screeners and manage saved screener presets.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`screen`](#screenerscreen) | `POST /screener/screen` | Screener | `none` |
| [`list`](#screenerlist) | `GET /screener` | Screener Preset List | `default` |
| [`save`](#screenersave) | `POST /screener` | Save Screener Preset | `none` |
| [`update`](#screenerupdate) | `PUT /screener/{id}` | Update Screener Preset | `none` |
| [`delete`](#screenerdelete) | `DELETE /screener/{id}` | Delete Screener Preset | `none` |

### screener.screen

```python
client.screener.screen(body) -> ScreenerScreenResponse
```

**Screener** — `POST /screener/screen` — cache `none`

Get a list of stock data matching the specified formula.

Body: `ScreenRequest` (TypedDict di `invezgo.types`).

Return: `ScreenerScreenResponse`


### screener.list

```python
client.screener.list() -> ScreenerListResponse
```

**Screener Preset List** — `GET /screener` — cache `default`

Get the list of screener presets, grouped into your own presets, public presets, and presets shared with your plan.

Return: `ScreenerListResponse`


### screener.save

```python
client.screener.save(body) -> ScreenerSaveResponse
```

**Save Screener Preset** — `POST /screener` — cache `none`

Save a new screener preset. The formula is tested first; if it is invalid, the preset is not saved and the 400 response contains the formula error details.

Body: `SaveScreenerRequest` (TypedDict di `invezgo.types`).

Return: `ScreenerSaveResponse`


### screener.update

```python
client.screener.update(id, body) -> ScreenerUpdateResponse
```

**Update Screener Preset** — `PUT /screener/{id}` — cache `none`

Update one of your screener presets by ID. All fields (name, description, scope, formula, category) are overwritten with the new values, and the formula is tested first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID preset screener, diambil dari field `id` pada response `GET /screener`. |

Body: `UpdateScreenerRequest` (TypedDict di `invezgo.types`).

Return: `ScreenerUpdateResponse`


### screener.delete

```python
client.screener.delete(id) -> ScreenerDeleteResponse
```

**Delete Screener Preset** — `DELETE /screener/{id}` — cache `none`

Delete one of your screener presets by ID.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID preset screener, diambil dari field `id` pada response `GET /screener`. |

Return: `ScreenerDeleteResponse`


## client.usage

API usage and quota monitoring (does not consume quota).

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`get_api_usage`](#usageget_api_usage) | `GET /usage/api` | API Usage | `none` |
| [`get_logs`](#usageget_logs) | `GET /usage/logs` | API Usage Logs | `none` |

### usage.get_api_usage

```python
client.usage.get_api_usage() -> ApiUsageResponse
```

**API Usage** — `GET /usage/api` — cache `none`

Information on API usage.

Return: `ApiUsageResponse`


### usage.get_logs

```python
client.usage.get_logs(from_=None, to=None, status=None, limit=None) -> UsageLogsResponse
```

**API Usage Logs** — `GET /usage/logs` — cache `none`

Get the API usage log history (requests made with an API key) of the authenticated user, newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `str` | tidak |  | Waktu awal dalam WIB, format `YYYY-MM-DD HH:mm:ss` atau `YYYY-MM-DD`. Maksimal 30 hari ke belakang. Default 24 jam terakhir. |
| `to` | `str` | tidak |  | Waktu akhir dalam WIB, format `YYYY-MM-DD HH:mm:ss` atau `YYYY-MM-DD`. Harus lebih besar atau sama dengan `from`. Default waktu saat ini. |
| `status` | `int` | tidak |  | Filter log berdasarkan HTTP status code, mis. `200`, `422`, atau `429`. |
| `limit` | `int` | tidak |  | Jumlah log maksimal yang dikembalikan. Kosongkan untuk mengambil seluruh log. |

Return: `UsageLogsResponse`


## client.watchlists

Personal watchlists and watchlist groups.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`list`](#watchlistslist) | `GET /watchlists` | Watchlist | `default` |
| [`add`](#watchlistsadd) | `POST /watchlists` | Add Stock to Watchlist | `none` |
| [`delete`](#watchlistsdelete) | `DELETE /watchlists` | Delete Watchlist Items | `none` |
| [`list_groups`](#watchlistslist_groups) | `GET /watchlists/group` | Watchlist Group List | `default` |
| [`add_group`](#watchlistsadd_group) | `POST /watchlists/group` | Create Watchlist Group | `none` |
| [`update_group`](#watchlistsupdate_group) | `PUT /watchlists/group/{id}` | Update Watchlist Group | `none` |
| [`delete_group`](#watchlistsdelete_group) | `DELETE /watchlists/group/{id}` | Delete Watchlist Group | `none` |
| [`update`](#watchlistsupdate) | `PUT /watchlists/{id}` | Update Watchlist Item | `none` |
| [`update_note`](#watchlistsupdate_note) | `PATCH /watchlists/{id}` | Update Watchlist Note | `none` |

### watchlists.list

```python
client.watchlists.list(group=None) -> WatchlistsListResponse
```

**Watchlist** — `GET /watchlists` — cache `default`

Get the stocks in the user's watchlist with their last price and percentage change against the saved reference price.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `group` | `str` | tidak |  | ID grup watchlist yang ingin ditampilkan, diambil dari field `id` pada response `GET /watchlists/group`. Kosongkan atau isi `null` untuk menampilkan seluruh watchlist dari semua grup. |

Return: `WatchlistsListResponse`


### watchlists.add

```python
client.watchlists.add(body) -> WatchlistsAddResponse
```

**Add Stock to Watchlist** — `POST /watchlists` — cache `none`

Add a new stock to the user's watchlist.

Body: `AddWatchlistRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsAddResponse`


### watchlists.delete

```python
client.watchlists.delete(body) -> WatchlistsDeleteResponse
```

**Delete Watchlist Items** — `DELETE /watchlists` — cache `none`

Delete one or more stocks from the user's watchlist by item ID.

Body: `DeleteIdsRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsDeleteResponse`


### watchlists.list_groups

```python
client.watchlists.list_groups() -> WatchlistsListGroupsResponse
```

**Watchlist Group List** — `GET /watchlists/group` — cache `default`

Get the user's watchlist groups.

Return: `WatchlistsListGroupsResponse`


### watchlists.add_group

```python
client.watchlists.add_group(body) -> WatchlistsAddGroupResponse
```

**Create Watchlist Group** — `POST /watchlists/group` — cache `none`

Create a new watchlist group for the user.

Body: `WatchlistGroupRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsAddGroupResponse`


### watchlists.update_group

```python
client.watchlists.update_group(id, body) -> WatchlistsUpdateGroupResponse
```

**Update Watchlist Group** — `PUT /watchlists/group/{id}` — cache `none`

Rename one of the user's watchlist groups.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID grup watchlist, diambil dari field `id` pada response `GET /watchlists/group`. |

Body: `WatchlistGroupRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsUpdateGroupResponse`


### watchlists.delete_group

```python
client.watchlists.delete_group(id) -> WatchlistsDeleteGroupResponse
```

**Delete Watchlist Group** — `DELETE /watchlists/group/{id}` — cache `none`

Delete one of the user's watchlist groups.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID grup watchlist, diambil dari field `id` pada response `GET /watchlists/group`. |

Return: `WatchlistsDeleteGroupResponse`


### watchlists.update

```python
client.watchlists.update(id, body) -> WatchlistsUpdateResponse
```

**Update Watchlist Item** — `PUT /watchlists/{id}` — cache `none`

Move a watchlist item to another group and/or change its reference price.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID item watchlist, diambil dari field `id` pada response `GET /watchlists`. |

Body: `UpdateWatchlistRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsUpdateResponse`


### watchlists.update_note

```python
client.watchlists.update_note(id, body) -> WatchlistsUpdateNoteResponse
```

**Update Watchlist Note** — `PATCH /watchlists/{id}` — cache `none`

Update the note on a watchlist item.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID item watchlist, diambil dari field `id` pada response `GET /watchlists`. |

Body: `NoteRequest` (TypedDict di `invezgo.types`).

Return: `WatchlistsUpdateNoteResponse`


## client.journals

Personal trading journal transactions.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`add`](#journalsadd) | `POST /journals` | Add Journal Transaction | `none` |
| [`list`](#journalslist) | `GET /journals` | Journal Transaction List | `default` |
| [`delete`](#journalsdelete) | `DELETE /journals` | Delete Journal Transactions | `none` |
| [`get_summary`](#journalsget_summary) | `GET /journals/summary` | Journal Summary | `default` |

### journals.add

```python
client.journals.add(body) -> JournalsAddResponse
```

**Add Journal Transaction** — `POST /journals` — cache `none`

Add one BUY or SELL transaction to the user's journal and update the portfolio. A BUY adds lots and recalculates the average price (incl. buy fee) for the stock code + broker pair; a SELL reduces lots and records a realized trade (profit/loss) shown in `GET /trades`.

Body: `AddJournalRequest` (TypedDict di `invezgo.types`).

Return: `JournalsAddResponse`


### journals.list

```python
client.journals.list(from_, to) -> JournalsListResponse
```

**Journal Transaction List** — `GET /journals` — cache `default`

Get the user's journal transactions (BUY/SELL) dated between `from` and `to` (inclusive), newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `JournalsListResponse`


### journals.delete

```python
client.journals.delete(body) -> JournalsDeleteResponse
```

**Delete Journal Transactions** — `DELETE /journals` — cache `none`

Delete one or more journal transactions by ID (body `{"id": ["<id>", ...]}`) and reverse their effect on the portfolio: deleting a BUY reduces the position's lots, deleting a SELL returns the lots to the position and removes the related realized trade.

Body: `DeleteIdsRequest` (TypedDict di `invezgo.types`).

Return: `JournalsDeleteResponse`


### journals.get_summary

```python
client.journals.get_summary(from_, to) -> JournalsSummaryResponse
```

**Journal Summary** — `GET /journals/summary` — cache `default`

Get a summary of the user's journal transactions dated between `from` and `to` (inclusive): counts and percentages per transaction type, total and average value, and a per-stock recap.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `JournalsSummaryResponse`


## client.portfolios

Personal portfolio built from journal transactions.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`list`](#portfolioslist) | `GET /portfolios` | Portfolio | `default` |
| [`get_summary`](#portfoliosget_summary) | `GET /portfolios/summary` | Portfolio Summary | `default` |

### portfolios.list

```python
client.portfolios.list() -> PortfoliosListResponse
```

**Portfolio** — `GET /portfolios` — cache `default`

Get the stock positions the user currently holds (built from journal entries), combined per stock code across all brokers, most recently updated first.

Return: `PortfoliosListResponse`


### portfolios.get_summary

```python
client.portfolios.get_summary() -> PortfoliosSummaryResponse
```

**Portfolio Summary** — `GET /portfolios/summary` — cache `default`

Get the user's portfolio summary: total cost basis, market value, unrealized profit/loss, and allocation per stock, sector and subsector.

Return: `PortfoliosSummaryResponse`


## client.alerts

Live formula alerts.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`create`](#alertscreate) | `POST /alerts` | Create Alert | `none` |
| [`list`](#alertslist) | `GET /alerts` | Alert List | `default` |
| [`test`](#alertstest) | `POST /alerts/test` | Test Alert Formula | `none` |
| [`update`](#alertsupdate) | `PUT /alerts/{id}` | Update Alert | `none` |
| [`delete`](#alertsdelete) | `DELETE /alerts/{id}` | Delete Alert | `none` |

### alerts.create

```python
client.alerts.create(body) -> AlertsCreateResponse
```

**Create Alert** — `POST /alerts` — cache `none`

Create an alert to get notified when stocks meet a given formula.

Body: `AlertRequest` (TypedDict di `invezgo.types`).

Return: `AlertsCreateResponse`


### alerts.list

```python
client.alerts.list() -> AlertsListResponse
```

**Alert List** — `GET /alerts` — cache `default`

List of created alerts.

Return: `AlertsListResponse`


### alerts.test

```python
client.alerts.test(body) -> AlertsTestResponse
```

**Test Alert Formula** — `POST /alerts/test` — cache `none`

Test an alert formula before creating the alert.

Body: `TestAlertRequest` (TypedDict di `invezgo.types`).

Return: `AlertsTestResponse`


### alerts.update

```python
client.alerts.update(id, body) -> AlertsUpdateResponse
```

**Update Alert** — `PUT /alerts/{id}` — cache `none`

Update a created alert.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID alert, diambil dari field `id` pada response `GET /alerts`. |

Body: `UpdateAlertRequest` (TypedDict di `invezgo.types`).

Return: `AlertsUpdateResponse`


### alerts.delete

```python
client.alerts.delete(id) -> AlertsDeleteResponse
```

**Delete Alert** — `DELETE /alerts/{id}` — cache `none`

Delete a created alert.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID alert, diambil dari field `id` pada response `GET /alerts`. |

Return: `AlertsDeleteResponse`


## client.posts

Community posts, comments, likes and votes.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`list`](#postslist) | `GET /posts` | Post List | `default` |
| [`list_by_category`](#postslist_by_category) | `GET /posts/category/{category}` | Posts by Category | `default` |
| [`list_by_stock`](#postslist_by_stock) | `GET /posts/space/{code}` | Stock Posts | `default` |
| [`list_by_stock_category`](#postslist_by_stock_category) | `GET /posts/space/category/{code}/{category}` | Stock Posts by Category | `default` |
| [`get`](#postsget) | `GET /posts/detail/{id}` | Post Detail | `default` |
| [`get_comments`](#postsget_comments) | `GET /posts/comment/{id}` | Post Comments | `default` |
| [`get_likes`](#postsget_likes) | `GET /posts/like` | Liked Posts | `default` |
| [`get_favorites`](#postsget_favorites) | `GET /posts/favorite` | Favorite Posts | `default` |
| [`get_voters`](#postsget_voters) | `GET /posts/vote/{id}` | Post Votes | `default` |

### posts.list

```python
client.posts.list(page, limit) -> PostsListResponse
```

**Post List** — `GET /posts` — cache `default`

Get the list of all Invezgo community posts with pagination, sorted newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsListResponse`


### posts.list_by_category

```python
client.posts.list_by_category(category, page, limit) -> PostsListByCategoryResponse
```

**Posts by Category** — `GET /posts/category/{category}` — cache `default`

Get the community posts of one category with pagination, sorted newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `category` | `PostsListByCategoryCategory ("POST", "ARTICLE", "VIDEO", "STOCKPICK", "POLLING")` | ya |  | Kategori postingan: `POST` = postingan umum, `ARTICLE` = artikel, `VIDEO` = video, `STOCKPICK` = rekomendasi saham, `POLLING` = polling. |
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsListByCategoryResponse`


### posts.list_by_stock

```python
client.posts.list_by_stock(code, page, limit) -> PostsListByStockResponse
```

**Stock Posts** — `GET /posts/space/{code}` — cache `default`

Get the posts in a stock's discussion space (posts that mention the stock code) with pagination, sorted newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham untuk menampilkan postingan pada ruang diskusi saham tersebut. |
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsListByStockResponse`


### posts.list_by_stock_category

```python
client.posts.list_by_stock_category(code, category, page, limit) -> PostsListByStockCategoryResponse
```

**Stock Posts by Category** — `GET /posts/space/category/{code}/{category}` — cache `default`

Get the posts in a stock's discussion space for one category with pagination, sorted newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `code` | `str` | ya |  | Kode saham untuk menampilkan postingan pada ruang diskusi saham tersebut. |
| `category` | `PostsListByStockCategoryCategory ("POST", "ARTICLE", "VIDEO", "STOCKPICK", "POLLING")` | ya |  | Kategori postingan: `POST` = postingan umum, `ARTICLE` = artikel, `VIDEO` = video, `STOCKPICK` = rekomendasi saham, `POLLING` = polling. |
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsListByStockCategoryResponse`


### posts.get

```python
client.posts.get(id) -> PostDetailResponse
```

**Post Detail** — `GET /posts/detail/{id}` — cache `default`

Get the full content of one post by ID.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID postingan, diambil dari field `id` pada response daftar postingan (mis. `GET /posts`). |

Return: `PostDetailResponse`


### posts.get_comments

```python
client.posts.get_comments(id, page, limit) -> PostsCommentsResponse
```

**Post Comments** — `GET /posts/comment/{id}` — cache `default`

Get the comments on a post with pagination, sorted by oldest update first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID postingan, diambil dari field `id` pada response daftar postingan (mis. `GET /posts`). |
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsCommentsResponse`


### posts.get_likes

```python
client.posts.get_likes(page, limit) -> PostsLikesResponse
```

**Liked Posts** — `GET /posts/like` — cache `default`

Get the posts and comments you have liked with pagination, sorted by most recently liked.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsLikesResponse`


### posts.get_favorites

```python
client.posts.get_favorites(page, limit) -> PostsFavoritesResponse
```

**Favorite Posts** — `GET /posts/favorite` — cache `default`

Get the posts and comments you have favorited with pagination, sorted by most recently favorited.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `page` | `int` | ya |  | Nomor halaman, dimulai dari 1. |
| `limit` | `int` | ya |  | Jumlah postingan per halaman. |

Return: `PostsFavoritesResponse`


### posts.get_voters

```python
client.posts.get_voters(id) -> PostsVotersResponse
```

**Post Votes** — `GET /posts/vote/{id}` — cache `default`

Get the vote summary (agree/disagree) of a stock pick (stockpick) post.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID postingan, diambil dari field `id` pada response daftar postingan (mis. `GET /posts`). |

Return: `PostsVotersResponse`


## client.trades

Personal realized trades.

| Method | HTTP | Ringkasan | Cache |
|---|---|---|---|
| [`list`](#tradeslist) | `GET /trades` | Realized Trade List | `default` |
| [`delete`](#tradesdelete) | `DELETE /trades` | Delete Realized Trades | `none` |
| [`get_summary`](#tradesget_summary) | `GET /trades/summary` | Realized Trade Summary | `default` |
| [`get_summary_chart`](#tradesget_summary_chart) | `GET /trades/summary-chart` | Realized Trade Summary Chart | `default` |
| [`update_note`](#tradesupdate_note) | `PATCH /trades/{id}` | Update Realized Trade Note | `none` |

### trades.list

```python
client.trades.list(from_, to) -> TradesListResponse
```

**Realized Trade List** — `GET /trades` — cache `default`

Get the user's realized trades (from SELL journal entries) with a sell date between `from` and `to` (inclusive), newest first.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `TradesListResponse`


### trades.delete

```python
client.trades.delete(body) -> TradesDeleteResponse
```

**Delete Realized Trades** — `DELETE /trades` — cache `none`

Delete one or more realized trades by ID (body `{"id": ["<id>", ...]}`). Only the realized-trade records are removed; journal transactions and the portfolio are unchanged.

Body: `DeleteIdsRequest` (TypedDict di `invezgo.types`).

Return: `TradesDeleteResponse`


### trades.get_summary

```python
client.trades.get_summary(from_, to) -> TradesSummaryResponse
```

**Realized Trade Summary** — `GET /trades/summary` — cache `default`

Get a performance summary of the user's realized trades with a sell date between `from` and `to` (inclusive): profit/loss/BEP counts, totals, win rate, and the best and worst trades.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |

Return: `TradesSummaryResponse`


### trades.get_summary_chart

```python
client.trades.get_summary_chart(from_, to, code) -> TradesSummaryChartResponse
```

**Realized Trade Summary Chart** — `GET /trades/summary-chart` — cache `default`

Get daily chart data of the user's realized profit/loss with a sell date between `from` and `to` (inclusive), with its running total and the comparison index close on the same day. Only days with realized trades are returned, in ascending date order.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `from_` | `Union[str, datetime.date]` | ya |  | Tanggal awal periode (`YYYY-MM-DD`). |
| `to` | `Union[str, datetime.date]` | ya |  | Tanggal akhir periode (`YYYY-MM-DD`). Harus lebih besar atau sama dengan `from`. |
| `code` | `str` | ya |  | Kode indeks pembanding pada grafik, mis. `COMPOSITE`. Bila dikirim kosong (`code=`), setiap tanggal berisi satu baris per indeks. |

Return: `TradesSummaryChartResponse`


### trades.update_note

```python
client.trades.update_note(id, body) -> TradesUpdateNoteResponse
```

**Update Realized Trade Note** — `PATCH /trades/{id}` — cache `none`

Update the note of one of the user's realized trades. Body: `{"note": "..."}` (optional, max 150 characters); when `note` is omitted the note is cleared.

| Parameter | Tipe | Wajib | Default | Keterangan |
|---|---|---|---|---|
| `id` | `str` | ya |  | ID transaksi terealisasi, diambil dari field `id` pada response `GET /trades`. |

Body: `NoteTradeRequest` (TypedDict di `invezgo.types`).

Return: `TradesUpdateNoteResponse`
