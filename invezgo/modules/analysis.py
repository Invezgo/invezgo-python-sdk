"""Analysis module for stock data."""

from typing import Optional, List
from .base import BaseModule


class AnalysisModule(BaseModule):
    """Module for stock analysis and data."""

    def get_stock_list(self) -> List[dict]:
        """
        Daftar lengkap perusahaan tercatat di BEI.

        Returns:
            List of stock data with code, name, and logo
        """
        return self.client.get("/analysis/list/stock")

    def get_broker_list(self) -> List[dict]:
        """
        Daftar lengkap broker/sekuritas di BEI.

        Returns:
            List of broker data with name and code
        """
        return self.client.get("/analysis/list/broker")

    def get_information(self, code: str) -> dict:
        """
        Informasi lengkap perusahaan.

        Args:
            code: Stock code (4-6 characters)

        Returns:
            Company information
        """
        return self.client.get(f"/analysis/information/{code}")

    def get_top_change(self, date: str) -> dict:
        """
        Top Gainer & Loser harian.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'gain' and 'loss' lists
        """
        return self.client.get("/analysis/top/change", params={"date": date})

    def get_top_foreign(self, date: str) -> dict:
        """
        Top Akumulasi & Distribusi Asing.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'accum' and 'dist' lists
        """
        return self.client.get("/analysis/top/foreign", params={"date": date})

    def get_top_accumulation(self, date: str) -> dict:
        """
        Top Akumulasi & Distribusi Bandarmologi.

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'accum' and 'dist' lists
        """
        return self.client.get("/analysis/top/accumulation", params={"date": date})

    def get_intraday(self, code: str, market: str = "RG") -> List[dict]:
        """
        Intraday chart saham.

        Args:
            code: Stock code
            market: Market type (RG, NG, TN)

        Returns:
            List of intraday data
        """
        return self.client.get(
            f"/analysis/intraday/{code}", params={"market": market}
        )

    def get_order_book(self, code: str, market: str = "RG") -> dict:
        """
        Order book saham.

        Args:
            code: Stock code
            market: Market type (RG, NG, TN)

        Returns:
            Order book data with bid and offer
        """
        return self.client.get(
            f"/analysis/order-book/{code}", params={"market": market}
        )

    def get_chart(
        self, code: str, from_date: str, to_date: str
    ) -> dict:
        """
        Grafik harga saham lengkap.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            Chart data with price and broker information
        """
        return self.client.get(
            f"/analysis/chart/stock/{code}",
            params={"from": from_date, "to": to_date},
        )

    def get_indicator_chart(
        self,
        code: str,
        indicator: str,
        from_date: str,
        to_date: str,
    ) -> dict:
        """
        Indikator grafik harga saham.

        Args:
            code: Stock code
            indicator: Indicator type (bdm, rsi, macd, etc.)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            Chart data with indicator
        """
        return self.client.get(
            f"/analysis/chart/stock/{indicator}/{code}",
            params={"from": from_date, "to": to_date},
        )

    def get_shareholder(self, code: str) -> List[dict]:
        """
        Komposisi kepemilikan saham.

        Args:
            code: Stock code

        Returns:
            List of shareholder data
        """
        return self.client.get(f"/analysis/shareholder/{code}")

    def get_shareholder_number(self, code: str) -> List[dict]:
        """
        Jumlah pemegang saham.

        Args:
            code: Stock code

        Returns:
            List of shareholder count data over time
        """
        return self.client.get(f"/analysis/shareholder/number/{code}")

    def get_shareholder_detail(self, code: str) -> List[dict]:
        """
        Kepemilikan saham (detail).

        Args:
            code: Stock code

        Returns:
            List of shareholder detail data
        """
        return self.client.get(f"/analysis/shareholder-detail/{code}")

    def get_shareholder_ksei(self, code: str, range_months: int) -> List[dict]:
        """
        Pemegang saham KSEI.

        Args:
            code: Stock code
            range_months: Number of months (max 12)

        Returns:
            List of KSEI shareholder data
        """
        return self.client.get(
            f"/analysis/shareholder/ksei/{code}",
            params={"range": range_months},
        )

    def get_summary_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        investor: str,
        market: str,
    ) -> List[dict]:
        """
        Analisa broker summary per saham.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            investor: Investor type (all, f, d)
            market: Market type (RG, NG, TN)

        Returns:
            List of broker summary data
        """
        return self.client.get(
            f"/analysis/summary/stock/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "investor": investor,
                "market": market,
            },
        )

    def get_summary_broker(
        self,
        code: str,
        from_date: str,
        to_date: str,
        investor: str,
        market: str,
    ) -> List[dict]:
        """
        Analisa broker summary per broker.

        Args:
            code: Broker code (2 characters)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            investor: Investor type (all, f, d)
            market: Market type (RG, NG, TN)

        Returns:
            List of broker summary data
        """
        return self.client.get(
            f"/analysis/summary/broker/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "investor": investor,
                "market": market,
            },
        )

    def get_summary_chart_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        market: str,
    ) -> List[dict]:
        """
        Infografik broker summary saham.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (volume, value, freq)
            market: Market type (RG, NG, TN)

        Returns:
            List of summary chart data
        """
        return self.client.get(
            f"/analysis/summary-chart/stock/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "scope": scope,
                "market": market,
            },
        )

    def get_summary_chart_broker(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        market: str,
    ) -> List[dict]:
        """
        Infografik broker summary broker.

        Args:
            code: Broker code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (volume, value, freq)
            market: Market type (RG, NG, TN)

        Returns:
            List of summary chart data
        """
        return self.client.get(
            f"/analysis/summary-chart/broker/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "scope": scope,
                "market": market,
            },
        )

    def get_inventory_chart_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        investor: str,
        limit: int,
        market: str,
        filter_brokers: Optional[List[str]] = None,
    ) -> dict:
        """
        Inventory chart saham.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (vol, val, freq)
            investor: Investor type (all, f, d)
            limit: Number of brokers to show (max 20)
            market: Market type (ALL, RG, NG, TN)
            filter_brokers: List of broker codes to filter

        Returns:
            Inventory chart data
        """
        params = {
            "from": from_date,
            "to": to_date,
            "scope": scope,
            "investor": investor,
            "limit": limit,
            "market": market,
        }
        if filter_brokers:
            params["filter"] = filter_brokers

        return self.client.get(
            f"/analysis/inventory-chart/stock/{code}", params=params
        )

    def get_inventory_chart_broker(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        investor: str,
        limit: int,
        market: str,
        filter_stocks: Optional[List[str]] = None,
    ) -> List[dict]:
        """
        Inventory chart broker.

        Args:
            code: Broker code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (vol, val, freq)
            investor: Investor type (all, f, d)
            limit: Number of stocks to show (max 20)
            market: Market type (ALL, RG, NG, TN)
            filter_stocks: List of stock codes to filter

        Returns:
            List of inventory chart data
        """
        params = {
            "from": from_date,
            "to": to_date,
            "scope": scope,
            "investor": investor,
            "limit": limit,
            "market": market,
        }
        if filter_stocks:
            params["filter"] = filter_stocks

        return self.client.get(
            f"/analysis/inventory-chart/broker/{code}", params=params
        )

    def get_momentum_chart(
        self,
        code: str,
        date: str,
        range_minutes: int,
        scope: str,
    ) -> List[dict]:
        """
        Momentum chart.

        Args:
            code: Stock code
            date: Date in YYYY-MM-DD format
            range_minutes: Time interval in minutes (5, 10, 15, 30, 60)
            scope: Calculation component (vol, val, freq)

        Returns:
            List of momentum chart data
        """
        return self.client.get(
            f"/analysis/momentum-chart/{code}",
            params={
                "date": date,
                "range": range_minutes,
                "scope": scope,
            },
        )

    def get_intraday_inventory_chart(
        self,
        code: str,
        range_minutes: int,
        type_name: str,
        total: int,
        buyer: str,
        seller: str,
        market: str,
        broker: Optional[str] = None,
    ) -> dict:
        """
        Intraday inventory chart.

        Args:
            code: Stock code
            range_minutes: Time interval in minutes
            type_name: Analysis type
            total: Total data to show
            buyer: Buyer broker filter (comma-separated)
            seller: Seller broker filter (comma-separated)
            market: Market type (ALL, RG, NG, TN)
            broker: Broker code filter (optional)

        Returns:
            Intraday inventory chart data
        """
        params = {
            "range": range_minutes,
            "type": type_name,
            "total": total,
            "buyer": buyer,
            "seller": seller,
            "market": market,
        }
        if broker:
            params["broker"] = broker

        return self.client.get(
            f"/analysis/intraday-inventory-chart/{code}", params=params
        )

    def get_sankey_chart(
        self,
        code: str,
        type_name: str,
        market: str,
        buyer: Optional[str] = None,
        seller: Optional[str] = None,
    ) -> dict:
        """
        Crossing / Sankey chart.

        Args:
            code: Stock code
            type_name: Analysis type
            market: Market type (ALL, RG, NG, TN)
            buyer: Buyer broker filter (optional)
            seller: Seller broker filter (optional)

        Returns:
            Sankey chart data
        """
        params = {"type": type_name, "market": market}
        if buyer:
            params["buyer"] = buyer
        if seller:
            params["seller"] = seller

        return self.client.get(f"/analysis/sankey-chart/{code}", params=params)

    def get_price_table(self, code: str, date: str) -> List[dict]:
        """
        Tabel harga transaksi perdagangan.

        Args:
            code: Stock code
            date: Date in YYYY-MM-DD format

        Returns:
            List of price table data
        """
        return self.client.get(
            f"/analysis/price-table/{code}", params={"date": date}
        )

    def get_time_table(
        self, code: str, date: str, range_minutes: int
    ) -> List[dict]:
        """
        Tabel waktu transaksi perdagangan.

        Args:
            code: Stock code
            date: Date in YYYY-MM-DD format
            range_minutes: Time interval in minutes

        Returns:
            List of time table data
        """
        return self.client.get(
            f"/analysis/time-table/{code}",
            params={"date": date, "range": range_minutes},
        )

    def get_price_diary(self, code: str) -> List[dict]:
        """
        Tabel perubahan harga harian.

        Args:
            code: Stock code

        Returns:
            List of daily price data
        """
        return self.client.get(f"/analysis/price-diary/{code}")

    def get_price_seasonality(self, code: str, range_months: int) -> List[dict]:
        """
        Tabel perubahan harga bulanan.

        Args:
            code: Stock code
            range_months: Number of months (max 60)

        Returns:
            List of monthly price data
        """
        return self.client.get(
            f"/analysis/price-seasonality/{code}",
            params={"range": range_months},
        )

    def get_shareholder_above(
        self,
        from_date: str,
        to_date: str,
        page: int,
        limit: int,
        name: Optional[str] = None,
        broker: Optional[List[str]] = None,
        code: Optional[str] = None,
    ) -> dict:
        """
        Kepemilikan saham diatas 5%.

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            page: Page number (starting from 1)
            limit: Items per page (max 100)
            name: Shareholder name filter (optional)
            broker: Broker code filter (optional)
            code: Stock code filter (optional)

        Returns:
            Paginated shareholder data
        """
        params = {
            "from": from_date,
            "to": to_date,
            "page": page,
            "limit": limit,
        }
        if name:
            params["name"] = name
        if broker:
            params["broker"] = broker
        if code:
            params["code"] = code

        return self.client.get("/analysis/shareholder-above", params=params)

    def get_shareholder_above_chart(
        self, code: str, broker: str, name: str, date: str
    ) -> dict:
        """
        Kepemilikan saham diatas 5% chart.

        Args:
            code: Stock code
            broker: Broker code
            name: Shareholder name
            date: Date in YYYY-MM-DD format

        Returns:
            Chart data
        """
        return self.client.get(
            f"/analysis/shareholder-above-chart/{code}",
            params={"broker": broker, "name": name, "date": date},
        )

    def get_insider(
        self,
        from_date: str,
        to_date: str,
        page: int,
        limit: int,
        name: Optional[str] = None,
        code: Optional[str] = None,
    ) -> dict:
        """
        Insider trading.

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            page: Page number (starting from 1)
            limit: Items per page (max 100)
            name: Shareholder name filter (optional)
            code: Stock code filter (optional)

        Returns:
            Paginated insider trading data
        """
        params = {
            "from": from_date,
            "to": to_date,
            "page": page,
            "limit": limit,
        }
        if name:
            params["name"] = name
        if code:
            params["code"] = code

        return self.client.get("/analysis/shareholder-insider", params=params)

    def get_insider_chart(self, code: str, name: str, date: str) -> dict:
        """
        Insider chart.

        Args:
            code: Stock code
            name: Shareholder name
            date: Date in YYYY-MM-DD format

        Returns:
            Chart data
        """
        return self.client.get(
            f"/analysis/insider-chart/{code}",
            params={"name": name, "date": date},
        )

    def get_financial_statement(
        self,
        code: str,
        statement: str,
        type_period: str,
        limit: int,
    ) -> dict:
        """
        Laporan keuangan perusahaan.

        Args:
            code: Stock code
            statement: Statement type (BS, IS, CF)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods (max 20)

        Returns:
            Financial statement data
        """
        return self.client.get(
            f"/analysis/financial-statement/{code}",
            params={
                "statement": statement,
                "type": type_period,
                "limit": limit,
            },
        )

    def get_financial_statement_chart(
        self,
        code: str,
        statement: str,
        type_period: str,
        limit: int,
        account: str,
    ) -> List[dict]:
        """
        Financial statement chart.

        Args:
            code: Stock code
            statement: Statement type (BS, IS, CF)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods (max 20)
            account: Account ID to visualize

        Returns:
            List of chart data
        """
        return self.client.get(
            f"/analysis/financial-statement-chart/{code}",
            params={
                "statement": statement,
                "type": type_period,
                "limit": limit,
                "account": account,
            },
        )

    def get_keystat(self, code: str, type_period: str, limit: int) -> dict:
        """
        Key statistics keuangan.

        Args:
            code: Stock code
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods (max 20)

        Returns:
            Key statistics data
        """
        return self.client.get(
            f"/analysis/keystat/{code}",
            params={"type": type_period, "limit": limit},
        )

    def get_keystat_chart(
        self, code: str, type_period: str, limit: int, name: str
    ) -> List[dict]:
        """
        Key statistics chart.

        Args:
            code: Stock code
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods
            name: Metric name to visualize (e.g., PER)

        Returns:
            List of chart data
        """
        return self.client.get(
            f"/analysis/keystat-chart/{code}",
            params={"type": type_period, "limit": limit, "name": name},
        )

