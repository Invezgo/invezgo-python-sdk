"""Health check module."""

from .base import BaseModule


class HealthModule(BaseModule):
    """Module for API health checks."""

    def check(self) -> dict:
        """
        Status API.

        Returns:
            API health status
        """
        return self.client.get("/health")

    def check_database(self) -> dict:
        """
        Status database.

        Returns:
            Database health status
        """
        return self.client.get("/health/database")

    def check_full(self) -> dict:
        """
        Status API dan database.

        Returns:
            Full health status
        """
        return self.client.get("/health/full")

