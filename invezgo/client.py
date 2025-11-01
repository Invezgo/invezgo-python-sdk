"""Main client for Invezgo SDK."""

from typing import Optional
import requests
from .exceptions import (
    InvezgoError,
    AuthenticationError,
    PaymentRequiredError,
    RateLimitError,
    NotFoundError,
    BadRequestError,
    ServerError,
)
from .modules import (
    AnalysisModule,
    WatchlistsModule,
    JournalsModule,
    PortfoliosModule,
    AIModule,
    PostsModule,
    ProfileModule,
    MembershipModule,
    TradesModule,
    ScreenerModule,
    SearchModule,
    HealthModule,
)


class InvezgoClient:
    """
    Main client for interacting with Invezgo API.

    Args:
        api_key: Your Invezgo API key (required)
        base_url: Base URL for the API (default: https://api.invezgo.com)
        timeout: Request timeout in seconds (default: 30)

    Example:
        >>> client = InvezgoClient(api_key="your-api-key")
        >>> stocks = client.analysis.get_stock_list()
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.invezgo.com",
        timeout: int = 30,
    ):
        if not api_key:
            raise ValueError("API key is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        # Initialize modules
        self.analysis = AnalysisModule(self)
        self.watchlists = WatchlistsModule(self)
        self.journals = JournalsModule(self)
        self.portfolios = PortfoliosModule(self)
        self.ai = AIModule(self)
        self.posts = PostsModule(self)
        self.profile = ProfileModule(self)
        self.membership = MembershipModule(self)
        self.trades = TradesModule(self)
        self.screener = ScreenerModule(self)
        self.search = SearchModule(self)
        self.health = HealthModule(self)

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict] = None,
        json_data: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> dict:
        """
        Make HTTP request to the API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint path
            params: Query parameters
            json_data: JSON body for POST/PUT requests
            headers: Additional headers

        Returns:
            Response JSON as dictionary

        Raises:
            Various InvezgoError subclasses based on HTTP status code
        """
        url = f"{self.base_url}{endpoint}"

        default_headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if headers:
            default_headers.update(headers)

        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
                headers=default_headers,
                timeout=self.timeout,
            )

            # Handle empty responses (204 No Content)
            if response.status_code == 204:
                return {}

            # Try to parse JSON response
            try:
                data = response.json()
            except ValueError:
                data = {"message": response.text}

            # Handle errors based on status code
            if response.status_code == 401:
                raise AuthenticationError(
                    data.get("message", "Authentication required"), data
                )
            elif response.status_code == 402:
                raise PaymentRequiredError(
                    data.get("message", "Advance role user only"), data
                )
            elif response.status_code == 400:
                raise BadRequestError(data.get("message", "Bad request"), data)
            elif response.status_code == 404:
                raise NotFoundError(data.get("message", "Resource not found"), data)
            elif response.status_code == 429:
                raise RateLimitError(
                    data.get("message", "ThrottlerException: Too Many Requests"), data
                )
            elif response.status_code >= 500:
                raise ServerError(
                    data.get("message", "Server error"),
                    status_code=response.status_code,
                    response=data,
                )

            # Return data for successful responses
            return data

        except requests.exceptions.Timeout:
            raise InvezgoError("Request timeout")
        except requests.exceptions.ConnectionError:
            raise InvezgoError("Connection error")
        except (
            AuthenticationError,
            PaymentRequiredError,
            RateLimitError,
            NotFoundError,
            BadRequestError,
            ServerError,
        ):
            raise
        except Exception as e:
            raise InvezgoError(f"Unexpected error: {str(e)}")

    def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        """Make GET request."""
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Make POST request."""
        return self._request("POST", endpoint, json_data=json_data)

    def put(self, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Make PUT request."""
        return self._request("PUT", endpoint, json_data=json_data)

    def delete(self, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Make DELETE request."""
        return self._request("DELETE", endpoint, json_data=json_data)

    def patch(self, endpoint: str, json_data: Optional[dict] = None) -> dict:
        """Make PATCH request."""
        return self._request("PATCH", endpoint, json_data=json_data)

