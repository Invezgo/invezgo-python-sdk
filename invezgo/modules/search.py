"""Search module."""

from .base import BaseModule


class SearchModule(BaseModule):
    """Module for search functionality."""

    def search(self, query: str) -> dict:
        """
        Cari saham atau pengguna.

        Args:
            query: Search query

        Returns:
            Search results
        """
        return self.client.get("/search", params={"query": query})

    def search_stock(self, query: str, cursor: str) -> dict:
        """
        Cari saham.

        Args:
            query: Search query
            cursor: Cursor for pagination

        Returns:
            Stock search results
        """
        return self.client.get(
            "/search/stock", params={"query": query, "cursor": cursor}
        )

    def search_user(self, query: str, cursor: str) -> dict:
        """
        Cari pengguna.

        Args:
            query: Search query
            cursor: Cursor for pagination

        Returns:
            User search results
        """
        return self.client.get(
            "/search/user", params={"query": query, "cursor": cursor}
        )

