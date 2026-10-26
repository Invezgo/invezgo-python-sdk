"""Exceptions raised by the Invezgo SDK."""

from typing import Any, Optional


class InvezgoError(Exception):
    """Base class for every SDK error.

    Attributes:
        message: Human-readable message (array messages from the API are joined with ``"; "``).
        status: HTTP status code, ``0`` for network errors.
        error: HTTP status text from the error body, e.g. ``"Unauthorized"``.
        request_id: Request ID from the API; quote it when contacting support.
        path: Request path reported by the API.
        body: Decoded JSON error body (or raw text when it is not JSON).
    """

    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        error: Optional[str] = None,
        request_id: Optional[str] = None,
        path: Optional[str] = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.error = error
        self.request_id = request_id
        self.path = path
        self.body = body

    @property
    def status_code(self) -> int:
        """Alias of :attr:`status` (2.x name)."""
        return self.status

    @property
    def response(self) -> Any:
        """Alias of :attr:`body` (2.x name)."""
        return self.body

    def __str__(self) -> str:
        return f"{self.status}: {self.message}" if self.status else self.message


class ValidationError(InvezgoError):
    """Invalid request parameters or body (400, 422)."""


BadRequestError = ValidationError


class AuthenticationError(InvezgoError):
    """API key missing, invalid or expired (401)."""


class PaymentRequiredError(InvezgoError):
    """Your subscription plan does not include this endpoint (402)."""


class NotFoundError(InvezgoError):
    """Resource not found (404)."""


class ServerError(InvezgoError):
    """Server-side error (5xx). Safe to retry later."""


class RateLimitError(InvezgoError):
    """Per-minute rate limit or monthly quota exceeded (429) on every configured API key.

    Attributes:
        retry_after: Seconds until at least one API key may be used again.
        limit: ``X-RateLimit-Limit`` header (requests per minute), when present.
        remaining: ``X-RateLimit-Remaining`` header, when present.
        reset: ``X-RateLimit-Reset`` header (Unix seconds), when present.
        quota_exceeded: ``True`` when the monthly quota (not the per-minute limit) is used up.
    """

    def __init__(
        self,
        message: str,
        *,
        retry_after: Optional[int] = None,
        limit: Optional[int] = None,
        remaining: Optional[int] = None,
        reset: Optional[int] = None,
        quota_exceeded: bool = False,
        **kwargs: Any,
    ) -> None:
        kwargs.setdefault("status", 429)
        super().__init__(message, **kwargs)
        self.retry_after = retry_after
        self.limit = limit
        self.remaining = remaining
        self.reset = reset
        self.quota_exceeded = quota_exceeded


class InvezgoConnectionError(InvezgoError):
    """The API could not be reached (DNS, TLS, connection reset...)."""


class InvezgoTimeoutError(InvezgoConnectionError):
    """The request exceeded the configured timeout."""


__all__ = [
    "InvezgoError",
    "ValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PaymentRequiredError",
    "NotFoundError",
    "ServerError",
    "RateLimitError",
    "InvezgoConnectionError",
    "InvezgoTimeoutError",
]
