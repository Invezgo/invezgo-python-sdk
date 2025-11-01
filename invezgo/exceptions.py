"""Custom exceptions for Invezgo SDK."""


class InvezgoError(Exception):
    """Base exception for all Invezgo SDK errors."""

    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response

    def __str__(self):
        if self.status_code:
            return f"{self.status_code}: {self.message}"
        return self.message


class AuthenticationError(InvezgoError):
    """Raised when API key is invalid or missing (401)."""

    def __init__(self, message: str = "Authentication required", response: dict = None):
        super().__init__(message, status_code=401, response=response)


class PaymentRequiredError(InvezgoError):
    """Raised when subscription package is insufficient or expired (402)."""

    def __init__(
        self,
        message: str = "Advance role user only",
        response: dict = None,
    ):
        super().__init__(message, status_code=402, response=response)


class NotFoundError(InvezgoError):
    """Raised when resource is not found (404)."""

    def __init__(self, message: str = "Resource not found", response: dict = None):
        super().__init__(message, status_code=404, response=response)


class RateLimitError(InvezgoError):
    """Raised when API rate limit is exceeded (429)."""

    def __init__(
        self,
        message: str = "ThrottlerException: Too Many Requests",
        response: dict = None,
    ):
        super().__init__(message, status_code=429, response=response)


class BadRequestError(InvezgoError):
    """Raised when request is invalid (400)."""

    def __init__(self, message: str = "Bad request", response: dict = None):
        super().__init__(message, status_code=400, response=response)


class ServerError(InvezgoError):
    """Raised when server error occurs (500+)."""

    def __init__(self, message: str = "Server error", status_code: int = 500, response: dict = None):
        super().__init__(message, status_code=status_code, response=response)

