"""Base module class for Invezgo SDK."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import InvezgoClient


class BaseModule:
    """Base class for all Invezgo SDK modules."""

    def __init__(self, client: "InvezgoClient"):
        """
        Initialize module with client.

        Args:
            client: InvezgoClient instance
        """
        self.client = client

