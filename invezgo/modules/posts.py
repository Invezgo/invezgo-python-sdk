"""Posts module."""

from typing import Optional
from .base import BaseModule


class PostsModule(BaseModule):
    """Module for posts and social features."""

    def get_all(self) -> dict:
        """
        Daftar semua postingan.

        Returns:
            List of posts
        """
        return self.client.get("/posts")

    def get_by_category(self, category: str) -> dict:
        """
        Daftar postingan berdasarkan kategori.

        Args:
            category: Category name

        Returns:
            List of posts in category
        """
        return self.client.get(f"/posts/category/{category}")

    def get_by_stock(self, code: str) -> dict:
        """
        Daftar postingan saham.

        Args:
            code: Stock code

        Returns:
            List of posts for stock
        """
        return self.client.get(f"/posts/space/{code}")

    def get_by_stock_category(self, code: str, category: str) -> dict:
        """
        Daftar postingan saham berdasarkan kategori.

        Args:
            code: Stock code
            category: Category name

        Returns:
            List of posts
        """
        return self.client.get(f"/posts/space/category/{code}/{category}")

    def get_by_id(self, id: str) -> dict:
        """
        Isi postingan.

        Args:
            id: Post ID

        Returns:
            Post details
        """
        return self.client.get(f"/posts/detail/{id}")

    def get_comments(self, id: str) -> dict:
        """
        Daftar komentar postingan.

        Args:
            id: Post ID

        Returns:
            List of comments
        """
        return self.client.get(f"/posts/comment/{id}")

    def get_liked(self) -> dict:
        """
        Daftar postingan disukai.

        Returns:
            List of liked posts
        """
        return self.client.get("/posts/like")

    def get_favorites(self) -> dict:
        """
        Daftar postingan favorit.

        Returns:
            List of favorited posts
        """
        return self.client.get("/posts/favorite")

    def get_voters(self, id: str) -> dict:
        """
        Daftar voting postingan.

        Args:
            id: Post ID

        Returns:
            List of voters
        """
        return self.client.get(f"/posts/vote/{id}")

