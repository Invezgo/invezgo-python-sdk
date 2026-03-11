"""Screener module."""

from typing import List, Optional
from .base import BaseModule


class ScreenerModule(BaseModule):
    """Module for stock screening."""

    def list_presets(self) -> dict:
        """
        Daftar preset screener.

        Returns:
            List of screener presets
        """
        return self.client.get("/screener")

    def screen(
        self,
        formula: str,
        category: Optional[List[str]] = None,
    ) -> List[dict]:
        """
        Jalankan screener saham Indonesia.

        Args:
            formula: Formula untuk screening saham (contoh: "prev < close", "change > 5")
            category: Kategori indeks saham yang ingin disaring (opsional).
                     Pilihan: COMPOSITE, SYARIAH, IDXENERGY, IDXBASIC, IDXINDUST,
                     IDXNONCYC, IDXCYCLIC, IDXHEALTH, IDXFINANCE, IDXPROPERT,
                     IDXTECHNO, IDXINFRA, IDXTRANS

        Example:
            >>> client.screener.screen(
            ...     formula="prev < close",
            ...     category=["SYARIAH", "IDXENERGY"]
            ... )
            >>> client.screener.screen(
            ...     formula="change > 5 AND volume > 1000000"
            ... )

        Returns:
            List of screened stocks matching the conditions
        """
        data = {"formula": formula}
        if category is not None:
            data["category"] = category
        return self.client.post("/screener/screen", json_data=data)

    def save_preset(
        self,
        name: str,
        description: Optional[str] = None,
        scope: Optional[List[str]] = None,
        formula: Optional[str] = None,
    ) -> dict:
        """
        Simpan preset screener.

        Args:
            name: Nama preset
            description: Deskripsi preset (opsional)
            scope: Scope preset (opsional)
            formula: Formula preset (opsional)

        Returns:
            Created preset data
        """
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if scope is not None:
            data["scope"] = scope
        if formula is not None:
            data["formula"] = formula
        return self.client.post("/screener", json_data=data)

    def update_preset(
        self,
        id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        scope: Optional[List[str]] = None,
        formula: Optional[str] = None,
    ) -> dict:
        """
        Update preset screener.

        Args:
            id: ID preset yang akan diupdate
            name: Nama preset (opsional)
            description: Deskripsi preset (opsional)
            scope: Scope preset (opsional)
            formula: Formula preset (opsional)

        Returns:
            Updated preset data
        """
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if scope is not None:
            data["scope"] = scope
        if formula is not None:
            data["formula"] = formula
        return self.client.put(f"/screener/{id}", json_data=data)

    def delete_preset(self, id: str) -> dict:
        """
        Hapus preset screener.

        Args:
            id: ID preset yang akan dihapus

        Returns:
            Response data
        """
        return self.client.delete(f"/screener/{id}")
