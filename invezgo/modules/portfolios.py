"""Portfolios module."""

from .base import BaseModule


class PortfoliosModule(BaseModule):
    """Module for managing portfolios."""

    def list(self) -> dict:
        """
        Daftar portofolio.

        Returns:
            List of portfolios
        """
        return self.client.get("/portfolios")

    def get_summary(self) -> dict:
        """
        Ringkasan portofolio.

        Returns:
            Portfolio summary
        """
        return self.client.get("/portfolios/summary")

