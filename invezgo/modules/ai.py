"""AI module for AI-powered analysis."""

from typing import Optional
from .base import BaseModule


class AIModule(BaseModule):
    """Module for AI-powered stock analysis."""

    def analyze_shareholder_ksei(self, code: str) -> dict:
        """
        Analisa AI KSEI pemegang saham.

        Args:
            code: Stock code

        Returns:
            AI analysis result
        """
        return self.client.get(f"/ai/shareholder/ksei/{code}")

    def analyze_inventory_chart(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        investor: str,
        limit: str,
        market: str,
        filter_brokers: str,
    ) -> dict:
        """
        Analisa AI Inventory Chart.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component
            investor: Investor type
            limit: Number limit
            market: Market type
            filter_brokers: Broker filter

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/inventory-chart/stock/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "scope": scope,
                "investor": investor,
                "limit": limit,
                "market": market,
                "filter": filter_brokers,
            },
        )

    def analyze_news(self, code: str) -> dict:
        """
        Analisa AI berita saham.

        Args:
            code: Stock code

        Returns:
            AI analysis result
        """
        return self.client.get(f"/ai/news/{code}")

    def analyze_broker_summary(
        self,
        code: str,
        from_date: str,
        to_date: str,
        investor: str,
        market: str,
    ) -> dict:
        """
        Analisa AI Broker Summary.

        Args:
            code: Stock code
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            investor: Investor type (all, f, d)
            market: Market type (RG, NG, TN)

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/summary/stock/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "investor": investor,
                "market": market,
            },
        )

    def analyze_insider(
        self,
        code: str,
        name: str,
        from_date: str,
        to_date: str,
        page: str,
        limit: str,
    ) -> dict:
        """
        Analisa AI Insider pemegang saham.

        Args:
            code: Stock code
            name: Shareholder name
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            page: Page number
            limit: Items per page

        Returns:
            AI analysis result
        """
        return self.client.get(
            "/ai/shareholder-insider",
            params={
                "code": code,
                "name": name,
                "from": from_date,
                "to": to_date,
                "page": page,
                "limit": limit,
            },
        )

    def analyze_shareholder_above(
        self,
        code: str,
        broker: str,
        name: str,
        from_date: str,
        to_date: str,
        page: str,
        limit: str,
    ) -> dict:
        """
        Analisa AI pemegang saham di atas 5%.

        Args:
            code: Stock code
            broker: Broker code
            name: Shareholder name
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            page: Page number
            limit: Items per page

        Returns:
            AI analysis result
        """
        return self.client.get(
            "/ai/shareholder-above",
            params={
                "code": code,
                "broker": broker,
                "name": name,
                "from": from_date,
                "to": to_date,
                "page": page,
                "limit": limit,
            },
        )

    def analyze_intraday_inventory(
        self,
        code: str,
        range_minutes: int,
        type_name: str,
        total: int,
        buyer: str,
        seller: str,
        broker: str,
        market: str,
    ) -> dict:
        """
        Analisa AI Intraday Inventory Chart.

        Args:
            code: Stock code
            range_minutes: Time interval in minutes
            type_name: Analysis type
            total: Total data
            buyer: Buyer filter
            seller: Seller filter
            broker: Broker filter
            market: Market type

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/intraday-inventory-chart/{code}",
            params={
                "range": range_minutes,
                "type": type_name,
                "total": total,
                "buyer": buyer,
                "seller": seller,
                "broker": broker,
                "market": market,
            },
        )

    def analyze_sankey_chart(
        self,
        code: str,
        type_name: str,
        buyer: str,
        seller: str,
        market: str,
    ) -> dict:
        """
        Analisa AI Sankey / Crossing Chart.

        Args:
            code: Stock code
            type_name: Analysis type
            buyer: Buyer filter
            seller: Seller filter
            market: Market type

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/sankey-chart/{code}",
            params={
                "type": type_name,
                "buyer": buyer,
                "seller": seller,
                "market": market,
            },
        )

    def analyze_shareholder(self, code: str) -> dict:
        """
        Analisa AI pemegang saham.

        Args:
            code: Stock code

        Returns:
            AI analysis result
        """
        return self.client.get(f"/ai/shareholder/{code}")

    def analyze_financial_statement(
        self,
        code: str,
        statement: str,
        type_period: str,
        limit: str,
    ) -> dict:
        """
        Analisa AI laporan keuangan.

        Args:
            code: Stock code
            statement: Statement type (BS, IS, CF)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/financial-statement/{code}",
            params={
                "statement": statement,
                "type": type_period,
                "limit": limit,
            },
        )

    def analyze_keystat(
        self,
        code: str,
        type_period: str,
        limit: str,
    ) -> dict:
        """
        Analisa AI Key Statistics.

        Args:
            code: Stock code
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods

        Returns:
            AI analysis result
        """
        return self.client.get(
            f"/ai/keystat/{code}",
            params={"type": type_period, "limit": limit},
        )

