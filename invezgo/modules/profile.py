"""Profile module."""

from typing import Optional
from .base import BaseModule


class ProfileModule(BaseModule):
    """Module for user profiles."""

    def get_user_details(self, username: str) -> dict:
        """
        Informasi profil pengguna.

        Args:
            username: Username

        Returns:
            User profile details
        """
        return self.client.get(f"/profile/detail/{username}")

    def get_user_posts(self, username: str, page: str, limit: str) -> dict:
        """
        Daftar postingan pengguna.

        Args:
            username: Username
            page: Page number
            limit: Items per page

        Returns:
            List of user posts
        """
        return self.client.get(
            f"/profile/posts/{username}",
            params={"page": page, "limit": limit},
        )

    def get_category_posts(
        self, username: str, category: str, page: str, limit: str
    ) -> dict:
        """
        Daftar postingan pengguna berdasarkan kategori.

        Args:
            username: Username
            category: Category name
            page: Page number
            limit: Items per page

        Returns:
            List of category posts
        """
        return self.client.get(
            f"/profile/posts/{username}/{category}",
            params={"page": page, "limit": limit},
        )

    def get_user_watchlist(self, username: str) -> dict:
        """
        Daftar watchlist pengguna.

        Args:
            username: Username

        Returns:
            User watchlist
        """
        return self.client.get(f"/profile/watchlist/{username}")

    def get_followers(self, username: str) -> dict:
        """
        Daftar pengikut pengguna.

        Args:
            username: Username

        Returns:
            List of followers
        """
        return self.client.get(f"/profile/follow/{username}")

    def get_following(self, username: str) -> dict:
        """
        Daftar mengikuti pengguna.

        Args:
            username: Username

        Returns:
            List of following users
        """
        return self.client.get(f"/profile/following/{username}")

    def get_memberships(self, username: str) -> dict:
        """
        Daftar membership pengguna.

        Args:
            username: Username

        Returns:
            User memberships
        """
        return self.client.get(f"/profile/membership/{username}")

    def get_recommendations(self) -> dict:
        """
        Daftar rekomendasi pengguna.

        Returns:
            User recommendations
        """
        return self.client.get("/recommendation/user")

