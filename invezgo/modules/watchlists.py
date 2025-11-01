"""Watchlists module."""

from typing import Optional
from .base import BaseModule


class WatchlistsModule(BaseModule):
    """Module for managing watchlists."""

    def list(self, group: str = "null") -> dict:
        """
        Daftar watchlist.

        Args:
            group: Group name from /watchlists/group

        Returns:
            List of watchlists
        """
        return self.client.get("/watchlists", params={"group": group})

    def add(self, data: dict) -> dict:
        """
        Tambah saham baru ke watchlist.

        Args:
            data: Watchlist data

        Returns:
            Created watchlist data
        """
        return self.client.post("/watchlists", json_data=data)

    def delete(self, data: dict) -> dict:
        """
        Hapus watchlist.

        Args:
            data: Watchlist deletion data

        Returns:
            Deletion result
        """
        return self.client.delete("/watchlists", json_data=data)

    def update(self, id: str, data: dict) -> dict:
        """
        Update watchlist.

        Args:
            id: Watchlist ID
            data: Update data

        Returns:
            Updated watchlist data
        """
        return self.client.put(f"/watchlists/{id}", json_data=data)

    def update_note(self, id: str, data: dict) -> dict:
        """
        Update catatan watchlist.

        Args:
            id: Watchlist ID
            data: Note data

        Returns:
            Updated watchlist data
        """
        return self.client.patch(f"/watchlists/{id}", json_data=data)

    def list_group(self) -> dict:
        """
        Daftar grup watchlist.

        Returns:
            List of watchlist groups
        """
        return self.client.get("/watchlists/group")

    def add_group(self, data: dict) -> dict:
        """
        Tambahkan grup baru ke watchlist.

        Args:
            data: Group data

        Returns:
            Created group data
        """
        return self.client.post("/watchlists/group", json_data=data)

