"""Membership module."""

from .base import BaseModule


class MembershipModule(BaseModule):
    """Module for membership management."""

    def list(self) -> dict:
        """
        Daftar membership.

        Returns:
            List of memberships
        """
        return self.client.get("/membership")

    def add(self, data: dict) -> dict:
        """
        Tambah membership baru.

        Args:
            data: Membership data

        Returns:
            Created membership data
        """
        return self.client.post("/membership", json_data=data)

    def get_scope(self) -> dict:
        """
        Daftar scope membership.

        Returns:
            List of membership scopes
        """
        return self.client.get("/membership/scope")

    def get_transactions(self) -> dict:
        """
        Daftar transaksi membership.

        Returns:
            List of membership transactions
        """
        return self.client.get("/membership/list")

    def update(self, id: str, data: dict) -> dict:
        """
        Update membership.

        Args:
            id: Membership ID
            data: Update data

        Returns:
            Updated membership data
        """
        return self.client.put(f"/membership/{id}", json_data=data)

    def delete(self, id: str) -> dict:
        """
        Hapus membership.

        Args:
            id: Membership ID

        Returns:
            Deletion result
        """
        return self.client.delete(f"/membership/{id}")

