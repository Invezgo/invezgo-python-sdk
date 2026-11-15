import hashlib
import hmac
import json
import unittest
from typing import Dict

from invezgo import WebhookVerificationError, parse_webhook, verify_webhook

SECRET = "whsec_test"
NOW = 1762425300
BODY = json.dumps({
    "id": "6f1c2b8e", "domain": "update", "type": "summary", "created_at": NOW,
    "data": {"date": "2026-11-06", "path": ["/analysis/summary/stock/BBCA"]},
}).encode()


def sign(body: bytes, ts: str, secret: str = SECRET) -> str:
    return "sha256=" + hmac.new(secret.encode(), ts.encode() + b"." + body, hashlib.sha256).hexdigest()


def headers(body: bytes = BODY, ts: str = str(NOW)) -> Dict[str, str]:
    return {"X-Invezgo-Timestamp": ts, "X-Invezgo-Signature": sign(body, ts)}


class VerifyWebhookTest(unittest.TestCase):
    def reason(self, **kwargs: object) -> str:
        args = dict(raw_body=BODY, headers=headers(), secret=SECRET, now=NOW)
        args.update(kwargs)
        with self.assertRaises(WebhookVerificationError) as cm:
            verify_webhook(**args)  # type: ignore[arg-type]
        return cm.exception.reason

    def test_valid(self) -> None:
        event = verify_webhook(BODY, headers(), SECRET, now=NOW)
        self.assertEqual(event.name, "update.summary")
        self.assertEqual(event.event, "update.summary")
        self.assertEqual(event.created_at, NOW)
        self.assertEqual(event.data["date"], "2026-11-06")

    def test_str_body_and_explicit_signature(self) -> None:
        h = headers()
        event = verify_webhook(BODY.decode(), None, SECRET, signature=h["X-Invezgo-Signature"],
                               timestamp=h["X-Invezgo-Timestamp"], now=NOW)
        self.assertEqual(event.id, "6f1c2b8e")

    def test_headers_case_insensitive(self) -> None:
        h = {k.lower(): v for k, v in headers().items()}
        self.assertEqual(verify_webhook(BODY, h, SECRET, now=NOW).type, "summary")
        h = {k.upper(): v for k, v in headers().items()}
        self.assertEqual(verify_webhook(BODY, h, SECRET, now=NOW).type, "summary")

    def test_bad_signature(self) -> None:
        self.assertEqual(self.reason(secret="other"), "signature")
        self.assertEqual(self.reason(raw_body=BODY + b" "), "signature")
        self.assertEqual(self.reason(headers={"X-Invezgo-Timestamp": str(NOW)}), "signature")

    def test_stale_and_future_timestamp(self) -> None:
        self.assertEqual(self.reason(now=NOW + 301), "timestamp")
        self.assertEqual(self.reason(now=NOW - 301), "timestamp")
        verify_webhook(BODY, headers(), SECRET, now=NOW + 300)
        verify_webhook(BODY, headers(), SECRET, now=NOW + 1000, tolerance=1000)

    def test_non_digit_timestamp(self) -> None:
        for ts in ("", "-1", "1762425300.5", "abc", "²"):
            self.assertEqual(self.reason(headers=headers(ts=ts)), "timestamp", ts)

    def test_bad_json(self) -> None:
        body = b"{not json"
        self.assertEqual(self.reason(raw_body=body, headers=headers(body)), "payload")
        body = b"[1, 2]"
        self.assertEqual(self.reason(raw_body=body, headers=headers(body)), "payload")

    def test_error_is_not_api_error(self) -> None:
        from invezgo import InvezgoError
        self.assertFalse(issubclass(WebhookVerificationError, InvezgoError))

    def test_parse_without_verification(self) -> None:
        event = parse_webhook('{"id":"x","domain":"quota","type":"low","created_at":1,'
                              '"data":{"plan":"PRIME","limit":1,"used":1,"remaining":0,"reset_at":null}}')
        self.assertEqual(event.name, "quota.low")
        self.assertIsNone(event.data["reset_at"])
        self.assertEqual(parse_webhook('{"domain":"new","type":"thing","created_at":2,"data":{}}').name, "new.thing")


if __name__ == "__main__":
    unittest.main()
