"""Webhook signature verification and parsing (stdlib only, no API key needed).

See https://docs.invezgo.com/api-usage/webhook (beta).
"""

import hashlib
import hmac
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional, Union

from typing_extensions import NotRequired, TypedDict


class WebhookVerificationError(Exception):
    """A webhook delivery failed verification or could not be decoded.

    Attributes:
        reason: ``"timestamp"``, ``"signature"`` or ``"payload"``.
    """

    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason
        self.message = message


@dataclass(frozen=True)
class WebhookEvent:
    """A webhook event. ``domain`` and ``type`` stay plain strings so new events never break decoding."""

    id: str
    domain: str
    type: str
    created_at: int
    data: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self) -> str:
        """``"{domain}.{type}"``, e.g. ``"update.summary"`` (same as the ``X-Invezgo-Event`` header)."""
        return f"{self.domain}.{self.type}"

    event = name


class WebhookUpdateData(TypedDict):
    """``data`` of every ``update.*`` event."""

    date: str
    path: List[str]
    code: NotRequired[str]
    title: NotRequired[str]


class WebhookAlertStock(TypedDict):
    code: str
    price: float


class WebhookAlertTriggeredData(TypedDict):
    """``data`` of ``alert.triggered``."""

    alert_id: str
    alert_name: str
    stocks_in: List[WebhookAlertStock]
    stocks_out: List[WebhookAlertStock]


class WebhookAlertDisabledData(TypedDict):
    """``data`` of ``alert.disabled``."""

    alert_id: str
    alert_name: str
    reason: str


class WebhookTestPingData(TypedDict):
    """``data`` of ``test.ping``."""

    message: str


class WebhookQuotaData(TypedDict):
    """``data`` of ``quota.low`` and ``quota.exhausted``."""

    plan: str
    limit: int
    used: int
    remaining: int
    reset_at: Optional[int]


def _to_bytes(value: Union[bytes, str]) -> bytes:
    return value.encode("utf-8") if isinstance(value, str) else bytes(value)


def parse_webhook(raw_body: Union[bytes, str]) -> WebhookEvent:
    """Decode a webhook body **without** verifying its signature (tests / already-verified bodies)."""
    try:
        obj = json.loads(_to_bytes(raw_body))
    except ValueError as e:
        raise WebhookVerificationError("payload", f"Invalid webhook JSON: {e}") from e
    if not isinstance(obj, dict):
        raise WebhookVerificationError("payload", "Webhook payload must be a JSON object")
    data = obj.get("data")
    try:
        created_at = int(obj.get("created_at") or 0)
    except (TypeError, ValueError) as e:
        raise WebhookVerificationError("payload", "Invalid webhook created_at") from e
    return WebhookEvent(
        id=str(obj.get("id", "")),
        domain=str(obj.get("domain", "")),
        type=str(obj.get("type", "")),
        created_at=created_at,
        data=data if isinstance(data, dict) else {},
    )


def verify_webhook(
    raw_body: Union[bytes, str],
    headers: Optional[Mapping[str, str]],
    secret: Union[str, bytes],
    *,
    signature: Optional[str] = None,
    timestamp: Optional[str] = None,
    tolerance: float = 300,
    now: Optional[float] = None,
) -> WebhookEvent:
    """Verify an Invezgo webhook delivery and return the decoded event.

    Args:
        raw_body: The exact request body received (bytes or str); never re-serialised JSON.
        headers: Request headers (looked up case-insensitively), or ``None`` when ``signature``
            and ``timestamp`` are passed directly.
        secret: Webhook secret from https://invezgo.com/id/setting/api.
        signature: ``X-Invezgo-Signature`` value; overrides ``headers``.
        timestamp: ``X-Invezgo-Timestamp`` value; overrides ``headers``.
        tolerance: Maximum age (or clock skew) of the timestamp, in seconds.
        now: Current Unix time in seconds (defaults to ``time.time()``).

    Raises:
        WebhookVerificationError: ``reason`` is ``"timestamp"``, ``"signature"`` or ``"payload"``.
    """
    lower = {k.lower(): v for k, v in (headers or {}).items()}
    ts = timestamp if timestamp is not None else lower.get("x-invezgo-timestamp", "")
    sig = signature if signature is not None else lower.get("x-invezgo-signature", "")
    current = time.time() if now is None else now
    # isascii(): str.isdigit() also accepts non-ASCII digits such as "²".
    if not (ts.isascii() and ts.isdigit()) or abs(current - int(ts)) > tolerance:
        raise WebhookVerificationError("timestamp", "Webhook timestamp is missing, invalid or outside the tolerance")
    body = _to_bytes(raw_body)
    expected = "sha256=" + hmac.new(_to_bytes(secret), ts.encode() + b"." + body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected.encode(), _to_bytes(sig)):
        raise WebhookVerificationError("signature", "Webhook signature does not match")
    return parse_webhook(body)


__all__ = [
    "WebhookVerificationError",
    "WebhookEvent",
    "WebhookUpdateData",
    "WebhookAlertStock",
    "WebhookAlertTriggeredData",
    "WebhookAlertDisabledData",
    "WebhookTestPingData",
    "WebhookQuotaData",
    "verify_webhook",
    "parse_webhook",
]
