"""Screener module."""

from typing import Optional, List, Dict, Any
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

    def save_preset(self, data: dict) -> dict:
        """
        Simpan preset screener.

        Args:
            data: Screener preset data

        Returns:
            Saved preset data
        """
        return self.client.post("/screener", json_data=data)

    def screen(
        self,
        columns: List[str],
        conditions: List[Dict[str, Any]],
    ) -> List[dict]:
        """
        Jalankan screener.

        Args:
            columns: List of columns to return
            conditions: List of screening conditions

        Example:
            >>> client.screener.screen(
            ...     columns=["volume"],
            ...     conditions=[
            ...         {
            ...             "ratio": "BASIC",
            ...             "column": "close",
            ...             "value": "5000",
            ...             "operator": ">="
            ...         }
            ...     ]
            ... )

        Returns:
            List of screened stocks
        """
        data = {"columns": columns, "conditions": conditions}
        return self.client.post("/screener/screen", json_data=data)

