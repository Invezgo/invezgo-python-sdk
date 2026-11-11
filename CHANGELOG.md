# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - 2026-11-11

Regenerated from the latest OpenAPI spec (Invezgo API 1.2, 109 endpoints).

### Added
- `analysis.get_flow_of_funds(code, type, *, limit=None)`: Flow of Funds (revenue → profit flow per period, with nodes, links and bridge) for `/analysis/flow-of-funds/{code}`.
- `analysis.get_free_float(code, range)`: free float composition over time for `/analysis/free-float/{code}`.
- `type` filter on `analysis.get_disclosure` (30 disclosure categories).
- `id` field on disclosure items; `foreign_*` breakdown fields on shareholder classification and classify-table responses.

### Changed
- Screener and alert `formula` now accepts up to 2048 characters.
- Order book `time` accepts `HH:mm:ss` as well as `HH:mm`.
- Usage logs `limit` maximum raised to 520000.

### Fixed
- Package `Repository` URL now points to https://github.com/Invezgo/invezgo-python-sdk.

## [3.0.0] - 2026-10-27

Rewrite generated 1:1 from the official OpenAPI spec (Invezgo API 1.2, 107 endpoints).
See [Migrating from 2.x](#migrating-from-2x) for the upgrade guide.

### Added
- Full typing: a `TypedDict` for every request body and response object, `Literal` aliases for every enum
  parameter, `List[...]` response aliases; package passes `mypy --strict` and ships `py.typed`.
- In-memory L1 LRU cache, enabled by default (`CacheOptions(ttl=60, realtime_ttl=5, max_entries=1000,
  max_bytes=32 MiB)`); caches raw bodies of GET requests keyed by canonical path + query, purges personal
  data after successful writes; `client.clear_cache()`.
- Multiple API keys (`additional_api_keys`) with automatic rotation on HTTP 429: per-minute limits block the
  key for that endpoint only, monthly-quota errors block the whole key; honours `Retry-After` /
  `X-RateLimit-Reset`; `RateLimitError` (with `retry_after`, `quota_exceeded`, `limit`, `remaining`, `reset`)
  only when every key is blocked.
- `ValidationError` (400/422), `InvezgoConnectionError`, `InvezgoTimeoutError`; errors expose `status`,
  `request_id`, `path`, `error`, `body`.
- New endpoints: `analysis.get_uma`, `get_suspend`, `get_notation`, `get_news`, `get_disclosure`,
  `usage.get_logs`.
- Date parameters accept `datetime.date`; context-manager support; custom `requests.Session`.
- Generated API reference `docs/API.md`, full docstrings on every method, unit tests.

### Changed
- Requires Python 3.9+; options after `api_key` are keyword-only; optional query params are keyword-only
  and named exactly as in the API (`from` → `from_`).
- Renamed methods (see [Migrating from 2.x](#migrating-from-2x)), e.g. `get_chart_stock` → `get_advance_chart`,
  `screener.list_presets` → `screener.list`, `posts.get_all` → `posts.list`.
- `BadRequestError` is now an alias of `ValidationError`.

### Migrating from 2.x

| 2.x | 3.0 |
|---|---|
| Python 3.7+ | Python 3.9+, new dependency `typing_extensions` |
| `InvezgoClient(api_key, base_url, timeout)` | `InvezgoClient(api_key, *, base_url=..., timeout=..., additional_api_keys=..., cache=..., session=...)` |
| No cache | Cache enabled by default; pass `cache=False` to always hit the server |
| `from_date` / `to_date` and other custom names | Exact API names (`from_`, `to`, `filter_column`, ...); optional query params are keyword-only |
| `analysis.get_intraday` | `analysis.get_intraday_chart` |
| `analysis.get_running_trade` | `analysis.get_stock_running_trade` |
| `analysis.get_chart_stock` / `get_chart_index` / `get_chart_indicator` | `analysis.get_advance_chart` / `get_index_chart` / `get_indicator_chart` |
| `analysis.get_shareholder_detail_one` | `analysis.get_shareholder_one_detail` |
| `analysis.get_shareholder_insider` | `analysis.get_insider` |
| `batch.get_order_book_batch` / `get_intraday_data_batch` / `get_intraday_index_batch` | `batch.get_order_book` / `get_intraday_data` / `get_intraday_index` |
| `screener.list_presets` / `save_preset` / `update_preset` / `delete_preset` | `screener.list` / `save` / `update` / `delete` |
| `watchlists.list_group` | `watchlists.list_groups` |
| `posts.get_all` / `get_by_category` / `get_by_stock` / `get_by_stock_category` / `get_by_id` / `get_liked` | `posts.list` / `list_by_category` / `list_by_stock` / `list_by_stock_category` / `get` / `get_likes` |
| `client.profile`, `client.membership`, `journals.update_note`, `journals.extract_from_file` | Removed (not in the official spec) |
| `client.get/post/put/delete/patch` | Removed |
| Exception `status_code` / `response` | `status` / `body` (old names kept as aliases); new `request_id`, `path`, `error` |
| Network errors | `InvezgoConnectionError` / `InvezgoTimeoutError` (subclasses of `InvezgoError`) |
| `RateLimitError` on any 429 | Raised only when every key is blocked; new `retry_after`, `quota_exceeded` |

### Removed
- `profile`, `membership`, `journals.update_note`, `journals.extract_from_file` (not in the official spec).
- Raw `client.get/post/put/delete/patch` helpers and `setup.py` / `requirements.txt` (use `pyproject.toml`).

## [2.0.0] - 2026-06-12

### Added
- Functional `TypedDict` type definitions for all request/response models.
- New `AlertsModule` mapping to the Live Alert endpoints.
- New `UsageModule` for checking API usage quota.
- 4 missing analysis endpoints: `get_multi_time_chart`, `get_shareholder_high`, `get_shareholder_classification`, and `get_shareholder_classify_table`.

### Changed
- Parameterized `/posts` methods and transaction logs with necessary query params (`page`, `limit`, `from_date`, `to_date`).
- Updated examples to match the new SDK signatures.

### Removed
- Deprecated `/profile/...` paths.
- Obsolete `AIModule` and `HealthModule` (not present in the latest specification).

## [1.0.0] - 2024-12-30

### Added
- Initial release of Invezgo Python SDK
- Complete API coverage for all Invezgo endpoints
- Analysis module with stock data, charts, and broker analysis
- Personal modules: Watchlists, Journals, Portfolios, Trades
- AI analysis module
- Social features: Posts, Profile, Search
- Screener functionality
- Comprehensive error handling
- Type hints for better IDE support
- Full documentation and examples

