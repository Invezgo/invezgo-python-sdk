"""Analysis module for stock data."""

from typing import Optional, List, Dict, Any
from .base import BaseModule


class AnalysisModule(BaseModule):
    """Module for stock analysis and data."""

    # =========================================================================
    # List Endpoints
    # =========================================================================

    def get_stock_list(self) -> List[Dict[str, Any]]:
        """
        Get a complete list of all companies listed on the Indonesia Stock Exchange (IDX).

        Features:
        - Includes latest IPO companies
        - Excludes delisted companies
        - Complete with company logos

        Returns:
            List of stock data with code, name, and logo
        """
        return self.client.get("/analysis/list/stock")

    def get_broker_list(self) -> List[Dict[str, Any]]:
        """
        Get a complete list of all brokers/securities registered as exchange members at IDX.

        Features:
        - Follows MKBD (Member of Broker Dealer) updates
        - 2-digit broker code for identification
        - Full name of securities company

        Returns:
            List of broker data with name and code
        """
        return self.client.get("/analysis/list/broker")

    def get_index_list(self) -> List[Dict[str, Any]]:
        """
        Get a complete list of all indexes available at IDX.

        Index Categories:
        - **headline**: Main indexes (COMPOSITE/IHSG, LQ45, IDX30, IDX80)
        - **sector**: Sectoral indexes (IDXENERGY, IDXFINANCE, IDXBASIC, etc)
        - **sharia**: Sharia indexes (JII, JII70, ISSI, etc)
        - **esg**: ESG/sustainability indexes (SRI-KEHATI, IDXESGL, etc)
        - **factor**: Factor-based indexes (IDXQ30, IDXV30, IDXG30, IDXHIDIV20)
        - **thematic**: Thematic indexes (IDXBUMN20, I-GRADE, etc)
        - **board**: Board indexes (MBX, DBX, ABX)
        - **partnership**: Partnership indexes (KOMPAS100, BISNIS-27, etc)
        - **smc**: Small-Mid Cap indexes (IDXSMC-LIQ, IDXSMC-COM)

        Returns:
            List of index data with code, name, and category
        """
        return self.client.get("/analysis/list/index")

    # =========================================================================
    # Company Information
    # =========================================================================

    def get_information(self, code: str) -> Dict[str, Any]:
        """
        Get complete and detailed information about a company based on stock code.

        Information Provided:
        - Company data (name, address, website)
        - Industry classification and business sector
        - Listing date on exchange
        - Tax ID and legal information

        Args:
            code: Stock code (4-6 characters)

        Returns:
            Company information
        """
        return self.client.get(f"/analysis/information/{code}")

    # =========================================================================
    # Top Gainer/Loser Endpoints
    # =========================================================================

    def get_top_change(self, date: str) -> Dict[str, Any]:
        """
        Get a list of stocks with the largest price increases and decreases on a specific day,
        complete with 5-day historical graph data.

        Features:
        - Top Gainer: Stocks with the highest price change increase
        - Top Loser: Stocks with the largest price change decrease
        - Graph: 5-day historical price change data for each stock

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'gain' and 'loss' lists
        """
        return self.client.get("/analysis/top/change", params={"date": date})

    def get_top_foreign(self, date: str) -> Dict[str, Any]:
        """
        Get a list of stocks with the largest foreign accumulation and distribution
        on a specific day, complete with 5-day historical graph data.

        Features:
        - Top Accumulation: Stocks with the highest foreign accumulation
        - Top Distribution: Stocks with the largest foreign distribution
        - Graph: 5-day historical foreign percentage data for each stock

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'accum' and 'dist' lists
        """
        return self.client.get("/analysis/top/foreign", params={"date": date})

    def get_top_accumulation(self, date: str) -> Dict[str, Any]:
        """
        Get a list of stocks with the largest bandarmology accumulation and distribution
        on a specific day.

        Features:
        - Top Accumulation: Stocks with the largest bandarmology accumulation
        - Top Distribution: Stocks with the largest bandarmology distribution

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'accum' and 'dist' lists
        """
        return self.client.get("/analysis/top/accumulation", params={"date": date})

    def get_top_ritel(self, date: str) -> Dict[str, Any]:
        """
        Get a list of stocks with the largest retail accumulation and distribution
        on a specific day.

        Features:
        - Top Accumulation: Stocks with the highest retail accumulation
        - Top Distribution: Stocks with the largest retail distribution
        - Retail percentage data from total volume

        Args:
            date: Date in YYYY-MM-DD format

        Returns:
            Dictionary with 'accum' and 'dist' lists
        """
        return self.client.get("/analysis/top/ritel", params={"date": date})

    # =========================================================================
    # Real-time Intraday Endpoints
    # =========================================================================

    def get_intraday(self, code: str, market: str = "RG") -> List[Dict[str, Any]]:
        """
        Get intraday chart data for a stock with the latest date.

        Data Provided:
        - Intraday chart data with summary data
        - Time series data with limited length
        - Chart-ready data for intraday visualization
        - Summary data for quick display

        Args:
            code: Stock code (4-6 characters)
            market: Market type (RG, NG, TN)

        Returns:
            List of intraday data
        """
        return self.client.get(
            f"/analysis/intraday/{code}", params={"market": market}
        )

    def get_order_book(self, code: str, market: str = "RG") -> Dict[str, Any]:
        """
        Get order book data for a stock with the latest date.

        Data Provided:
        - Order book data with summary data
        - Cross section data with limited length
        - Table-ready data for order book visualization
        - Summary data for quick display

        Args:
            code: Stock code (4-6 characters)
            market: Market type (RG, NG, TN)

        Returns:
            Order book data with bid and offer
        """
        return self.client.get(
            f"/analysis/order-book/{code}", params={"market": market}
        )

    def get_intraday_data(self, code: str, market: str = "RG") -> Dict[str, Any]:
        """
        Get intraday data for a stock with the latest date.

        Data Provided:
        - Intraday data with summary data
        - Cross section data with limited length
        - Table-ready data for intraday visualization
        - Summary data for quick display

        Args:
            code: Stock code (4-6 characters)
            market: Market type (RG, NG, TN)

        Returns:
            Intraday data with OHLCV and other metrics
        """
        return self.client.get(
            f"/analysis/intraday-data/{code}", params={"market": market}
        )

    def get_intraday_index(self, code: str, market: str = "RG") -> Dict[str, Any]:
        """
        Get intraday data for an index with the latest date.

        Data Provided:
        - Intraday data with summary data
        - Cross section data with limited length
        - Table-ready data for intraday visualization
        - Summary data for quick display

        Args:
            code: Index code (e.g., COMPOSITE, LQ45)
            market: Market type (RG, NG, TN)

        Returns:
            Index intraday data with OHLCV and other metrics
        """
        return self.client.get(
            f"/analysis/intraday-index/{code}", params={"market": market}
        )

    # =========================================================================
    # Chart Endpoints
    # =========================================================================

    def get_chart_stock(
        self, code: str, from_date: str, to_date: str
    ) -> List[Dict[str, Any]]:
        """
        Get complete stock price chart data with OHLCV data for a specific period.

        Data Provided:
        - OHLCV price data (Open, High, Low, Close, Volume)
        - Time series data within specific period
        - Daily transaction information for specific period

        Args:
            code: Stock code (4-6 characters)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            List of chart data with OHLCV
        """
        return self.client.get(
            f"/analysis/chart/stock/{code}",
            params={"from": from_date, "to": to_date},
        )

    def get_chart_index(
        self, code: str, from_date: str, to_date: str
    ) -> List[Dict[str, Any]]:
        """
        Get complete index price chart data with OHLCV data for a specific period.

        Data Provided:
        - OHLCV price data (Open, High, Low, Close, Volume)
        - Time series data within specific period
        - Daily transaction information for specific period

        Args:
            code: Index code (e.g., COMPOSITE, LQ45)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            List of chart data with OHLCV
        """
        return self.client.get(
            f"/analysis/chart/index/{code}",
            params={"from": from_date, "to": to_date},
        )

    def get_chart_indicator(
        self,
        code: str,
        indicator: str,
        from_date: str,
        to_date: str,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data with technical indicators for stock price analysis in a specific period.

        Data Provided:
        - Various types of indicators (BDM, FOREIGN, RATIO, RITEL) for specific period
        - Time series data with indicators

        Args:
            code: Stock code (4-6 characters)
            indicator: Indicator type (bdm, foreign, ratio, ritel, etc.)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)

        Returns:
            List of chart data with indicator values
        """
        return self.client.get(
            f"/analysis/chart/stock/{indicator}/{code}",
            params={"from": from_date, "to": to_date},
        )

    # =========================================================================
    # Shareholder Endpoints
    # =========================================================================

    def get_shareholder_detail(self, code: str, name: str) -> List[Dict[str, Any]]:
        """
        Get company stock ownership data (5%+) for a specific period.

        Data Provided:
        - Stock ownership above 5%
        - Time series data of ownership changes
        - Growth/decline trend of ownership
        - Historical stock ownership data

        Args:
            code: Stock code (4-6 characters)
            name: Shareholder name

        Returns:
            List of shareholder detail data
        """
        return self.client.get(
            f"/analysis/shareholder-detail/{code}",
            params={"code": code, "name": name},
        )

    def get_shareholder_detail_one(self, code: str, name: str) -> List[Dict[str, Any]]:
        """
        Get company stock ownership data (1%+) based on stock code or shareholder name.

        Data Provided:
        - Stock ownership (> 1% owners)
        - Shareholder details (type, status, domicile)
        - Share count and ownership percentage

        Args:
            code: Stock code (4-6 characters)
            name: Shareholder name

        Returns:
            List of shareholder detail data
        """
        return self.client.get(
            "/analysis/shareholder-detail-one",
            params={"code": code, "name": name},
        )

    def get_shareholder_number(self, code: str) -> List[Dict[str, Any]]:
        """
        Get the number of investors/shareholders of a company for a specific period.

        Data Provided:
        - Total number of shareholders
        - Time series data of investor count changes
        - Investor growth/decline trend
        - Historical shareholder count data

        Args:
            code: Stock code (4-6 characters)

        Returns:
            List of shareholder count data over time
        """
        return self.client.get(f"/analysis/shareholder/number/{code}")

    def get_shareholder_relation(
        self,
        code: Optional[str] = None,
        name: Optional[str] = None,
        depth: Optional[int] = None,
        max_nodes: Optional[int] = None,
        neighbors: Optional[int] = None,
        min_percentage: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Get bidirectional shareholder relation graph data based on the latest stock ownership snapshots.

        Data Provided:
        - Nodes: stocks and entities/shareholders
        - Edges: ownership relations from stock -> shareholder
        - Cross-company ownership structure
        - Subsidiary data

        Args:
            code: Stock code as the starting point
            name: Shareholder name as the starting point
            depth: Depth of the graph to build (1-4)
            max_nodes: Maximum number of nodes limit
            neighbors: Maximum relations per node to expand
            min_percentage: Minimum ownership percentage filter

        Returns:
            Graph data with nodes and edges
        """
        params: Dict[str, Any] = {}
        if code:
            params["code"] = code
        if name:
            params["name"] = name
        if depth:
            params["depth"] = depth
        if max_nodes:
            params["max_nodes"] = max_nodes
        if neighbors:
            params["neighbors"] = neighbors
        if min_percentage:
            params["min_percentage"] = min_percentage

        return self.client.get("/analysis/shareholder/relation", params=params)

    def get_shareholder(self, code: str) -> List[Dict[str, Any]]:
        """
        Get company stock ownership composition data based on the largest shareholders
        on the latest date.

        Data Provided:
        - Controlling shareholder
        - Affiliated parties and directors
        - Public shareholders
        - Ownership percentage of each party
        - Badge/position (CONTROLLER, DIRECTOR, COMMISSIONER)

        Args:
            code: Stock code (4-6 characters)

        Returns:
            List of shareholder composition data
        """
        return self.client.get(f"/analysis/shareholder/{code}")

    def get_shareholder_ksei(self, code: str, range_months: int) -> List[Dict[str, Any]]:
        """
        Get shareholder data based on KSEI classification (foreign and domestic investors
        in various groups) for a specific period.

        Data Provided:
        - Foreign and domestic investor classification
        - Investor groups (IS, CP, PF, IB, ID, MF, SC, FD, OT)
        - Time series data of ownership changes
        - Ownership percentage per investor group

        Args:
            code: Stock code (4-6 characters)
            range_months: Number of months (1-120)

        Returns:
            List of KSEI shareholder data
        """
        return self.client.get(
            f"/analysis/shareholder/ksei/{code}",
            params={"range": range_months},
        )

    # =========================================================================
    # Broker Summary Endpoints
    # =========================================================================

    def get_summary_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        investor: str,
        market: str,
    ) -> List[Dict[str, Any]]:
        """
        Get detailed trading broker activity analysis for a specific stock within
        a specific time period.

        Data Provided:
        - Buy/sell activity per broker
        - Volume and transaction value
        - Trading frequency
        - Average buy/sell price
        - Investor classification (domestic/foreign)

        Args:
            code: Stock code (4-6 characters)
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
    ) -> List[Dict[str, Any]]:
        """
        Get detailed trading activity analysis for a specific broker for all stocks
        within a specific time period.

        Data Provided:
        - Buy/sell activity per stock
        - Volume and transaction value
        - Trading frequency
        - Average buy/sell price
        - Investor classification (domestic/foreign)

        Args:
            code: Broker code(s) - single or multiple separated by comma (e.g., AG or AG,AK,RX)
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

    # =========================================================================
    # Sector Analysis Endpoints
    # =========================================================================

    def get_sector_stalker(
        self,
        from_date: str,
        to_date: str,
        base: Optional[str] = None,
        limit: Optional[int] = None,
        filter_code: Optional[str] = None,
        filter_column: Optional[str] = None,
        filter_operator: Optional[str] = None,
        filter_value: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Get sectoral index or stock price movement data within a specific time range.

        Data Provided:
        - If base = COMPOSITE: Sectoral index price movement
        - Time series data for each index/stock
        - Data normalized to base 100 for comparison

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            base: Base index for filter (default: COMPOSITE)
            limit: Number of stocks to display (optional, for base != COMPOSITE)
            filter_code: Additional filter for stock code/name search (optional)
            filter_column: Column to filter (change, value, volume, foreign, freq, bdm, ritel, ratio, open, high, low, close)
            filter_operator: Comparison operator (<, >, =, >=, <=, !=)
            filter_value: Value for filter comparison

        Returns:
            Sector stalker data with index movements
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
        }
        if base:
            params["base"] = base
        if limit:
            params["limit"] = limit
        if filter_code:
            params["filter"] = filter_code
        if filter_column:
            params["filter_column"] = filter_column
        if filter_operator:
            params["filter_operator"] = filter_operator
        if filter_value:
            params["filter_value"] = filter_value

        return self.client.get("/analysis/stalker/sector", params=params)

    def get_sector_rotation(
        self,
        from_date: str,
        to_date: str,
        base: Optional[str] = None,
        length: Optional[int] = None,
        tail: Optional[int] = None,
        limit: Optional[int] = None,
        filter_code: Optional[str] = None,
        filter_column: Optional[str] = None,
        filter_operator: Optional[str] = None,
        filter_value: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Get sector rotation data for relative movement visualization of sectoral indexes or stocks.

        Data Provided:
        - If base = COMPOSITE: Relative movement of sectoral indexes vs COMPOSITE
        - If base = other index: Relative movement of stocks in that index
        - X and Y coordinates for plotting chart
        - Trail data to see historical movement
        - Quadrant classification (leading, weakening, lagging, improving)

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            base: Benchmark index (default: COMPOSITE)
            length: Calculation period (default: 10, range: 5-50)
            tail: Number of trailing points (default: 5, range: 1-20)
            limit: Number of stocks to display (optional, for base != COMPOSITE)
            filter_code: Filter for stock code/name search (optional)
            filter_column: Column to filter (change, value, volume, foreign, freq, bdm, ritel, ratio, open, high, low, close)
            filter_operator: Comparison operator (<, >, =, >=, <=, !=)
            filter_value: Value for filter comparison

        Returns:
            Sector rotation data with benchmark and trail info
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
        }
        if base:
            params["base"] = base
        if length:
            params["length"] = length
        if tail:
            params["tail"] = tail
        if limit:
            params["limit"] = limit
        if filter_code:
            params["filter"] = filter_code
        if filter_column:
            params["filter_column"] = filter_column
        if filter_operator:
            params["filter_operator"] = filter_operator
        if filter_value:
            params["filter_value"] = filter_value

        return self.client.get("/analysis/sector/rotation", params=params)

    # =========================================================================
    # Broker Stalker Endpoints
    # =========================================================================

    def get_broker_stalker(
        self,
        broker: str,
        stock: str,
        from_date: str,
        to_date: str,
        investor: str,
        market: str,
        scope: str,
    ) -> Dict[str, Any]:
        """
        Track a specific broker's trading activity on a specific stock in daily calendar format.

        Data Provided:
        - Daily net value of broker on the stock
        - Number of active trading days
        - Total accumulated net value
        - Average net value per active day
        - Day with highest net value (peak)

        Args:
            broker: Broker code(s) - single or multiple separated by comma (e.g., AG or AG,AK,RX)
            stock: Stock code (4-6 characters)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            investor: Investor type (all, f, d)
            market: Market type (RG, NG, TN)
            scope: Calculation component (volume, value)

        Returns:
            Broker stalker data with summary and calendar
        """
        return self.client.get(
            f"/analysis/stalker/broker/{broker}/{stock}",
            params={
                "from": from_date,
                "to": to_date,
                "investor": investor,
                "market": market,
                "scope": scope,
            },
        )

    def get_broker_stalker_list(
        self,
        code: str,
        from_date: str,
        to_date: str,
        investor: str,
        scope: str,
        market: str,
    ) -> Dict[str, Any]:
        """
        Get list of all stocks traded by a specific broker within a specific time period.

        Data Provided:
        - Stock list with net value (in IDR or lots)
        - Transaction count per stock
        - Buy dominance per stock (percentage)
        - Summary statistics: total stocks, total net, top stock, concentration, overall buy dominance

        Args:
            code: Broker code(s) - single or multiple separated by comma (e.g., AG or AG,AK,RX)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            investor: Investor type (all, f, d)
            scope: Calculation component (volume, value)
            market: Market type (RG, NG, TN)

        Returns:
            Broker stalker list data with summary and list
        """
        return self.client.get(
            f"/analysis/stalker/list/{code}",
            params={
                "from": from_date,
                "to": to_date,
                "investor": investor,
                "scope": scope,
                "market": market,
            },
        )

    # =========================================================================
    # Summary Chart Endpoints
    # =========================================================================

    def get_summary_chart_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        market: str,
    ) -> List[Dict[str, Any]]:
        """
        Get broker summary infographic data for a specific stock with attractive
        visualization for a specific period.

        Data Provided:
        - Broker summary infographic per stock
        - Visualization data with colors and labels
        - Buy/sell breakdown per investor type
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
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
    ) -> List[Dict[str, Any]]:
        """
        Get broker summary infographic data for a specific broker with attractive
        visualization for a specific period.

        Data Provided:
        - Broker summary infographic per broker
        - Visualization data with colors and labels
        - Buy/sell breakdown per investor type
        - Chart-ready data for visualization

        Args:
            code: Broker code(s) - single or multiple separated by comma
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

    # =========================================================================
    # Inventory Chart Endpoints
    # =========================================================================

    def get_inventory_chart_stock(
        self,
        code: str,
        from_date: str,
        to_date: str,
        scope: str,
        investor: str,
        market: str,
        limit: Optional[int] = None,
        filter_brokers: Optional[str] = None,
        filter_operator: Optional[str] = None,
        filter_value: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Get inventory chart data for a specific stock with broker activity visualization
        for a specific period.

        Data Provided:
        - Broker inventory visualization per stock
        - Time series data with broker activity
        - Accumulation and distribution analysis
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (vol, val, freq)
            investor: Investor type (all, f, d)
            market: Market type (ALL, RG, NG, TN)
            limit: Number of brokers to show (optional)
            filter_brokers: Filter for specific brokers (optional)
            filter_operator: Comparison operator for filter (<, >, =, >=, <=, !=)
            filter_value: Value for filter comparison

        Returns:
            Inventory chart data with price and broker data
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
            "scope": scope,
            "investor": investor,
            "market": market,
        }
        if limit:
            params["limit"] = limit
        if filter_brokers:
            params["filter"] = filter_brokers
        if filter_operator:
            params["filter_operator"] = filter_operator
        if filter_value:
            params["filter_value"] = filter_value

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
        market: str,
        limit: Optional[int] = None,
        filter_stocks: Optional[str] = None,
        filter_operator: Optional[str] = None,
        filter_value: Optional[float] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get inventory chart data for a specific broker with stock activity visualization
        for a specific period.

        Data Provided:
        - Broker inventory visualization per stock
        - Time series data with stock activity
        - Accumulation and distribution analysis
        - Chart-ready data for visualization

        Args:
            code: Broker code(s) - single or multiple separated by comma
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            scope: Calculation component (vol, val, freq)
            investor: Investor type (all, f, d)
            market: Market type (ALL, RG, NG, TN)
            limit: Number of stocks to show (optional)
            filter_stocks: Filter for specific stocks (optional)
            filter_operator: Comparison operator for filter (<, >, =, >=, <=, !=)
            filter_value: Value for filter comparison

        Returns:
            List of inventory chart data
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
            "scope": scope,
            "investor": investor,
            "market": market,
        }
        if limit:
            params["limit"] = limit
        if filter_stocks:
            params["filter"] = filter_stocks
        if filter_operator:
            params["filter_operator"] = filter_operator
        if filter_value:
            params["filter_value"] = filter_value

        return self.client.get(
            f"/analysis/inventory-chart/broker/{code}", params=params
        )

    # =========================================================================
    # Momentum and Intraday Chart Endpoints
    # =========================================================================

    def get_momentum_chart(
        self,
        code: str,
        date: str,
        range_minutes: int,
        scope: str,
    ) -> List[Dict[str, Any]]:
        """
        Get momentum chart data for real-time transaction analysis with HAKA HAKI details.

        Data Provided:
        - Real-time trading momentum visualization
        - HAKA HAKI data (Price, Accumulation, Increase, Indicator)
        - Momentum analysis per time interval
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            date: Date in YYYY-MM-DD format
            range_minutes: Time interval in minutes
            scope: Calculation component (value, volume)

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
        date: str,
        range_minutes: int,
        type_name: str,
        total: int,
        buyer: str,
        seller: str,
        market: str,
        filter_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get intraday inventory chart data for transaction analysis with broker activity details.

        Data Provided:
        - Intraday broker inventory visualization
        - Time series data with real-time broker activity
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            date: Date in YYYY-MM-DD format
            range_minutes: Time interval in minutes
            type_name: Analysis type (value, volume)
            total: Total data to show
            buyer: Buyer broker filter (ALL, F, D)
            seller: Seller broker filter (ALL, F, D)
            market: Market type (RG, NG, TN)
            filter_code: Additional filter (optional)

        Returns:
            Intraday inventory chart data with price and broker data
        """
        params: Dict[str, Any] = {
            "date": date,
            "range": range_minutes,
            "type": type_name,
            "total": total,
            "buyer": buyer,
            "seller": seller,
            "market": market,
        }
        if filter_code:
            params["filter"] = filter_code

        return self.client.get(
            f"/analysis/intraday-inventory-chart/{code}", params=params
        )

    # =========================================================================
    # Distribution and Price Table Endpoints
    # =========================================================================

    def get_sankey_chart(
        self,
        code: str,
        date: str,
        type_name: str,
        buyer: str,
        seller: str,
        market: str,
    ) -> Dict[str, Any]:
        """
        Get sankey chart data for crossing transaction visualization with broker flow details.

        Data Provided:
        - Crossing transaction visualization with sankey chart
        - Broker flow data with attractive visualization
        - Crossing pattern analysis
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            date: Date in YYYY-MM-DD format
            type_name: Analysis type (value, volume)
            buyer: Buyer broker filter (ALL, F, D)
            seller: Seller broker filter (ALL, F, D)
            market: Market type (RG, NG, TN)

        Returns:
            Sankey chart data with nodes and links
        """
        return self.client.get(
            f"/analysis/sankey-chart/{code}",
            params={
                "date": date,
                "type": type_name,
                "buyer": buyer,
                "seller": seller,
                "market": market,
            },
        )

    def get_price_table(self, code: str, date: str) -> List[Dict[str, Any]]:
        """
        Get daily stock trading price transaction table with volume and frequency details.

        Data Provided:
        - Price table with buy/sell volume
        - Transaction frequency per price
        - Real-time trading data
        - Daily transaction details

        Args:
            code: Stock code (4-6 characters)
            date: Date in YYYY-MM-DD format

        Returns:
            List of price table data
        """
        return self.client.get(
            f"/analysis/price-table/{code}", params={"date": date}
        )

    def get_time_table(
        self, code: str, date: str, range_minutes: int
    ) -> List[Dict[str, Any]]:
        """
        Get daily stock trading time transaction table with OHLCV details per time interval.

        Data Provided:
        - Time table with OHLCV data
        - Volume and transaction value per interval
        - Buy/sell data per time interval
        - Real-time trading data

        Args:
            code: Stock code (4-6 characters)
            date: Date in YYYY-MM-DD format
            range_minutes: Time interval in minutes

        Returns:
            List of time table data
        """
        return self.client.get(
            f"/analysis/time-table/{code}",
            params={"date": date, "range": range_minutes},
        )

    def get_price_diary(self, code: str) -> List[Dict[str, Any]]:
        """
        Get daily stock price change table with complete historical data.

        Data Provided:
        - Historical daily price data
        - Daily volume and transaction value
        - Price change percentage
        - Complete time series data

        Args:
            code: Stock code (4-6 characters)

        Returns:
            List of daily price data
        """
        return self.client.get(f"/analysis/price-diary/{code}")

    def get_price_seasonality(self, code: str, range_months: int) -> List[Dict[str, Any]]:
        """
        Get monthly stock price change table with seasonality analysis.

        Data Provided:
        - Historical monthly price data
        - Monthly volume and transaction value
        - Monthly price change percentage
        - Seasonality pattern analysis

        Args:
            code: Stock code (4-6 characters)
            range_months: Number of months (1-120)

        Returns:
            List of monthly price data
        """
        return self.client.get(
            f"/analysis/price-seasonality/{code}",
            params={"range": range_months},
        )

    # =========================================================================
    # Insider Trading Endpoints
    # =========================================================================

    def get_shareholder_above(
        self,
        from_date: str,
        to_date: str,
        code: Optional[str] = None,
        broker: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get a list of ownership changes above 5% based on exchange reports for a specific period.

        Data Provided:
        - Ownership changes above 5%
        - Insider transaction data
        - Majority shareholder information
        - Time series data of ownership changes
        - Pagination for large data

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            code: Stock code filter (optional)
            broker: Broker code filter (optional)
            name: Shareholder name filter (optional)
            page: Page number (optional)
            limit: Items per page (optional)

        Returns:
            Paginated shareholder data above 5%
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
        }
        if code:
            params["code"] = code
        if broker:
            params["broker"] = broker
        if name:
            params["name"] = name
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        return self.client.get("/analysis/shareholder-above", params=params)

    def get_shareholder_above_chart(
        self,
        code: str,
        broker: Optional[str] = None,
        name: Optional[str] = None,
        date: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data for ownership visualization above 5% for a specific period.

        Data Provided:
        - Ownership chart visualization above 5%
        - Time series data of ownership changes
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            broker: Broker code or "INSTITUSI" (optional)
            name: Shareholder name (optional)
            date: Date in YYYY-MM-DD format (optional)

        Returns:
            List of chart data
        """
        params: Dict[str, Any] = {}
        if broker:
            params["broker"] = broker
        if name:
            params["name"] = name
        if date:
            params["date"] = date

        return self.client.get(
            f"/analysis/shareholder-above-chart/{code}", params=params
        )

    def get_shareholder_one(
        self,
        from_date: str,
        to_date: str,
        code: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get a list of ownership changes above 1% based on exchange reports for a specific period.

        Data Provided:
        - Ownership changes above 1%
        - Insider transaction data
        - Majority shareholder information
        - Time series data of ownership changes
        - Pagination for large data

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            code: Stock code filter (optional)
            name: Shareholder name filter (optional)
            page: Page number (optional)
            limit: Items per page (optional)

        Returns:
            Paginated shareholder data above 1%
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
        }
        if code:
            params["code"] = code
        if name:
            params["name"] = name
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        return self.client.get("/analysis/shareholder-one", params=params)

    def get_shareholder_one_chart(
        self,
        code: str,
        broker: Optional[str] = None,
        name: Optional[str] = None,
        date: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data for ownership visualization above 1% for a specific period.

        Data Provided:
        - Ownership chart visualization above 1%
        - Time series data of ownership changes
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            broker: Broker code or "INSTITUSI" (optional)
            name: Shareholder name (optional)
            date: Date in YYYY-MM-DD format (optional)

        Returns:
            List of chart data
        """
        params: Dict[str, Any] = {}
        if broker:
            params["broker"] = broker
        if name:
            params["name"] = name
        if date:
            params["date"] = date

        return self.client.get(
            f"/analysis/shareholder-one-chart/{code}", params=params
        )

    def get_shareholder_insider(
        self,
        from_date: str,
        to_date: str,
        code: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get a list of insider ownership changes (directors, commissioners, majority shareholders)
        for a specific period.

        Data Provided:
        - Insider ownership changes
        - Directors and commissioners transaction data
        - Majority shareholder information
        - Time series data of ownership changes
        - Pagination for large data

        Args:
            from_date: Start date (YYYY-MM-DD)
            to_date: End date (YYYY-MM-DD)
            code: Stock code filter (optional)
            name: Shareholder name filter (optional)
            page: Page number (optional)
            limit: Items per page (optional)

        Returns:
            Paginated insider trading data
        """
        params: Dict[str, Any] = {
            "from": from_date,
            "to": to_date,
        }
        if code:
            params["code"] = code
        if name:
            params["name"] = name
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        return self.client.get("/analysis/shareholder-insider", params=params)

    def get_insider_chart(
        self,
        code: str,
        name: Optional[str] = None,
        date: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data for insider trading visualization for a specific period.

        Data Provided:
        - Insider trading chart visualization
        - Time series data of insider ownership changes
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            name: Shareholder name (optional)
            date: Date in YYYY-MM-DD format (optional)

        Returns:
            List of chart data
        """
        params: Dict[str, Any] = {}
        if name:
            params["name"] = name
        if date:
            params["date"] = date

        return self.client.get(
            f"/analysis/insider-chart/{code}", params=params
        )

    # =========================================================================
    # Financial Statement Endpoints
    # =========================================================================

    def get_financial_statement(
        self,
        code: str,
        statement: str,
        type_period: str,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get company financial statement data based on report type and specific period.

        Data Provided:
        - Balance Sheet
        - Income Statement
        - Cash Flow Statement
        - Historical financial statement data
        - Hierarchical data structure with parent-child relationship

        Args:
            code: Stock code (4-6 characters)
            statement: Statement type (BS, IS, CF)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods (optional)

        Returns:
            Financial statement data with rows and columns
        """
        params: Dict[str, Any] = {
            "statement": statement,
            "type": type_period,
        }
        if limit:
            params["limit"] = limit

        return self.client.get(
            f"/analysis/financial-statement/{code}", params=params
        )

    def get_financial_statement_chart(
        self,
        code: str,
        statement: str,
        type_period: str,
        account: str,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data for financial statement visualization for a specific period.

        Data Provided:
        - Financial statement chart visualization
        - Time series financial statement data
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            statement: Statement type (BS, IS, CF)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            account: Account ID to visualize
            limit: Number of periods (optional)

        Returns:
            List of chart data
        """
        params: Dict[str, Any] = {
            "statement": statement,
            "type": type_period,
            "account": account,
        }
        if limit:
            params["limit"] = limit

        return self.client.get(
            f"/analysis/financial-statement-chart/{code}", params=params
        )

    def get_keystat(
        self,
        code: str,
        type_period: str,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get key statistics and important financial metrics of a company for a specific period.

        Data Provided:
        - Important financial ratios
        - Company performance metrics
        - Historical key statistics data
        - Fundamental indicators
        - Hierarchical data structure

        Args:
            code: Stock code (4-6 characters)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            limit: Number of periods (optional)

        Returns:
            Key statistics data with rows and columns
        """
        params: Dict[str, Any] = {
            "type": type_period,
        }
        if limit:
            params["limit"] = limit

        return self.client.get(
            f"/analysis/keystat/{code}", params=params
        )

    def get_keystat_chart(
        self,
        code: str,
        type_period: str,
        name: str,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get chart data for key statistics visualization for a specific period.

        Data Provided:
        - Key statistics chart visualization
        - Time series key statistics data
        - Chart-ready data for visualization

        Args:
            code: Stock code (4-6 characters)
            type_period: Period type (FY, Q, Q1, Q2, Q3, Q4)
            name: Statistic name (e.g., ROE, PER)
            limit: Number of periods (optional)

        Returns:
            List of chart data
        """
        params: Dict[str, Any] = {
            "type": type_period,
            "name": name,
        }
        if limit:
            params["limit"] = limit

        return self.client.get(
            f"/analysis/keystat-chart/{code}", params=params
        )

    # =========================================================================
    # Corporate Action Calendar
    # =========================================================================

    def get_calendar(
        self,
        code: Optional[str] = None,
        type_action: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Get corporate action schedule based on specific filters.

        Available Filters (Must choose at least one):
        - Code: Specific stock code
        - Type: Corporate action type

        Args:
            code: Stock code (4-6 characters) (optional)
            type_action: Corporate action type (IPO, PUBLIC_EXPOSE, REVERSE, RIGHT,
                        RUPS_RESULT, RUPS_SCHEDULE, SPLIT, WARRANT, BONUS,
                        CONVERTION, DIVIDEND) (optional)
            page: Page number (default: 1) (optional)
            limit: Items per page (max: 50, default: 20) (optional)

        Returns:
            Corporate action calendar data
        """
        params: Dict[str, Any] = {}
        if code:
            params["code"] = code
        if type_action:
            params["type"] = type_action
        if page:
            params["page"] = page
        if limit:
            params["limit"] = limit

        return self.client.get("/analysis/calendar", params=params)
