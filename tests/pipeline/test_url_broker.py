"""Unit tests for the URL broker (SSRF / redirect guards)."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import url_broker


class UrlBrokerTests(unittest.TestCase):
    def test_allows_public_https(self) -> None:
        with patch.object(url_broker, "resolve_host", return_value=["93.184.216.34"]):
            res = url_broker.validate_url("https://example.com/page")
        self.assertTrue(res["ok"], res.get("error"))

    def test_blocks_loopback(self) -> None:
        res = url_broker.validate_url("http://127.0.0.1:8090/api/health")
        self.assertFalse(res["ok"])
        self.assertIn("blocked", res["error"])

    def test_blocks_localhost_hostname(self) -> None:
        res = url_broker.validate_url("http://localhost:8090")
        self.assertFalse(res["ok"])

    def test_blocks_private_rfc1918(self) -> None:
        res = url_broker.validate_url("http://192.168.1.10/admin")
        self.assertFalse(res["ok"])

    def test_blocks_link_local(self) -> None:
        res = url_broker.validate_url("http://169.254.169.254/latest/meta-data/")
        self.assertFalse(res["ok"])

    def test_blocks_metadata_host(self) -> None:
        res = url_broker.validate_url("http://metadata.google.internal/")
        self.assertFalse(res["ok"])

    def test_blocks_non_http_scheme(self) -> None:
        res = url_broker.validate_url("file:///etc/passwd")
        self.assertFalse(res["ok"])

    def test_blocks_dns_rebind_to_private(self) -> None:
        with patch.object(url_broker, "resolve_host", return_value=["93.184.216.34", "10.0.0.5"]):
            res = url_broker.validate_url("https://rebind.example.com")
        self.assertFalse(res["ok"])
        self.assertIn("blocked address", res["error"])

    def test_bare_domain_gets_https(self) -> None:
        with patch.object(url_broker, "resolve_host", return_value=["93.184.216.34"]):
            res = url_broker.validate_url("example.com")
        self.assertTrue(res["ok"], res.get("error"))
        self.assertTrue(res["normalized"].startswith("https://"))

    def test_ipv4_mapped_ipv6_loopback_blocked(self) -> None:
        res = url_broker.validate_url("http://[::ffff:127.0.0.1]/")
        self.assertFalse(res["ok"])


if __name__ == "__main__":
    unittest.main()
