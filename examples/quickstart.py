"""Quick start: fetch market data with full typing.

Run: INVEZGO_API_KEY=... python examples/quickstart.py
"""

import os
from datetime import date, timedelta

from invezgo import InvezgoClient
from invezgo.types import StockListItem, TopChangeResponse


def main() -> None:
    with InvezgoClient(os.environ["INVEZGO_API_KEY"]) as client:
        stocks: list[StockListItem] = client.analysis.get_stock_list()
        print(f"{len(stocks)} saham tercatat, contoh: {stocks[0]['code']} - {stocks[0]['name']}")

        info = client.analysis.get_information("BBCA")
        print("Informasi BBCA:", sorted(info)[:5], "...")

        # Date params accept "YYYY-MM-DD" strings or datetime.date objects.
        last_week = date.today() - timedelta(days=7)
        top: TopChangeResponse = client.analysis.get_top_change(last_week, filter_column="value",
                                                                 filter_operator=">", filter_value=1e9)
        for row in top["gain"][:5]:
            print(f"{row['code']:6} {row['change']:+.2f}%  harga={row['price']}")

        # `from` is a Python keyword, so the argument is called `from_`.
        candles = client.analysis.get_advance_chart("BBCA", from_=last_week, to=date.today())
        for c in candles[-3:]:
            print(c["date"], c.get("close"))

        # Pagination: follow `nextPage` until it is None.
        page: int | None = 1
        while page is not None and page <= 2:
            news = client.analysis.get_news(page=page, limit=5)
            for item in news["data"]:
                print("-", item["date"], item["title"])
            page = news["nextPage"]


if __name__ == "__main__":
    main()
