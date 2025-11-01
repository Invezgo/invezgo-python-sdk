"""Trades module."""

from .base import BaseModule


class TradesModule(BaseModule):
    """Module for realized trades."""

    def list(self) -> dict:
        """
        Daftar transaksi terealisasi.

        Returns:
            List of trades
        """
        return self.client.get("/trades")

    def delete(self, data: dict) -> dict:
        """
        Hapus transaksi terealisasi.

        Args:
            data: Deletion data

        Returns:
            Deletion result
        """
        return self.client.delete("/trades", json_data=data)

    def get_summary(self) -> dict:
        """
        Ringkasan transaksi terealisasi.

        Returns:
            Trade summary
        """
        return self.client.get("/trades/summary")

    def get_summary_chart(self) -> dict:
        """
        Ringkasan transaksi terealisasi grafik.

        Returns:
            Trade summary chart data
        """
        return self.client.get("/trades/summary-chart")

    def update_note(self, id: str, data: dict) -> dict:
        """
        Update catatan transaksi terealisasi.

        Args:
            id: Trade ID
            data: Note data

        Returns:
            Updated trade data
        """
        return self.client.patch(f"/trades/{id}", json_data=data)

