"""Journals module."""

from typing import Optional
from .base import BaseModule


class JournalsModule(BaseModule):
    """Module for managing trading journals."""

    def list(self) -> dict:
        """
        Daftar transaksi jurnal.

        Returns:
            List of journal transactions
        """
        return self.client.get("/journals")

    def add(self, data: dict) -> dict:
        """
        Tambah transaksi jurnal baru.

        Args:
            data: Transaction data

        Returns:
            Created transaction data
        """
        return self.client.post("/journals", json_data=data)

    def delete(self, data: dict) -> dict:
        """
        Hapus jurnal.

        Args:
            data: Deletion data

        Returns:
            Deletion result
        """
        return self.client.delete("/journals", json_data=data)

    def get_summary(self) -> dict:
        """
        Ringkasan transaksi jurnal.

        Returns:
            Transaction summary
        """
        return self.client.get("/journals/summary")

    def update_note(self, id: str, data: dict) -> dict:
        """
        Update catatan transaksi jurnal.

        Args:
            id: Transaction ID
            data: Note data

        Returns:
            Updated transaction data
        """
        return self.client.patch(f"/journals/{id}", json_data=data)

    def extract_from_file(self, file_data: dict) -> dict:
        """
        Ekstrak jurnal dari file.

        Args:
            file_data: File data

        Returns:
            Extracted journal data
        """
        return self.client.post("/journals/file", json_data=file_data)

