"""The `/api/route/classify` endpoint — the browser's window onto the classifier.

The browser used to carry its own copy of the routing rules. It could not
see the server's rules, so it disagreed with them on purpose. It now asks
the server, and this file holds the endpoint to that promise:

- the endpoint answers with the *same* route the classifier gives;
- it fails open (the browser falls back to Eve) when the classifier is
  unavailable;
- it rejects malformed input without leaking anything.
"""

from __future__ import annotations

import http.client
import json
import threading
import unittest
from http.server import ThreadingHTTPServer

import frontend.serve as serve
from frontend.serve import EmpireHandler
from pipeline import route_classifier


class RouteClassifyApiTests(unittest.TestCase):
    def setUp(self) -> None:
        class QuietHandler(EmpireHandler):
            def log_message(self, _format: str, *_args: object) -> None:
                return None

        server_type = getattr(serve, "EmpireHTTPServer", ThreadingHTTPServer)
        if server_type is ThreadingHTTPServer:
            self.server = server_type(("127.0.0.1", 0), QuietHandler)
        else:
            self.server = server_type(("127.0.0.1", 0), QuietHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self._close_server)
        self.port = self.server.server_address[1]

    def _close_server(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()

    def post(self, body: bytes, headers: dict[str, str] | None = None) -> tuple[int, dict]:
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        connection.request(
            "POST",
            "/api/route/classify",
            body=body,
            headers=headers or {"Content-Type": "application/json"},
        )
        response = connection.getresponse()
        payload = json.loads(response.read().decode())
        connection.close()
        return response.status, payload

    def classify(self, text: str) -> tuple[int, dict]:
        return self.post(json.dumps({"text": text}).encode("utf-8"))

    def test_endpoint_returns_the_shared_route(self) -> None:
        for text in (
            "Who is Kate Bush?",
            "what do you know about me",
            "list my tasks",
            "what is my disk space",
        ):
            with self.subTest(text=text):
                status, payload = self.classify(text)
                self.assertEqual(status, 200)
                self.assertTrue(payload.get("ok"))
                self.assertEqual(payload.get("route"), route_classifier.classify(text))
                self.assertIn("reason", payload)

    def test_endpoint_reports_the_memory_flag(self) -> None:
        status, payload = self.classify("what do you know about me")
        self.assertEqual(status, 200)
        self.assertTrue(payload.get("is_memory"))
        self.assertFalse(payload.get("is_wiki"))

    def test_endpoint_reports_the_wiki_flag(self) -> None:
        status, payload = self.classify("Who is Kate Bush?")
        self.assertEqual(status, 200)
        self.assertTrue(payload.get("is_wiki"))
        self.assertFalse(payload.get("is_memory"))

    def test_endpoint_rejects_a_malformed_body(self) -> None:
        status, payload = self.post(b"not-json")
        self.assertEqual(status, 400)
        self.assertFalse(payload.get("ok"))

    def test_endpoint_rejects_a_non_object_body(self) -> None:
        status, payload = self.post(b"[1, 2, 3]")
        self.assertEqual(status, 400)
        self.assertFalse(payload.get("ok"))

    def test_endpoint_rejects_an_empty_body(self) -> None:
        status, payload = self.post(b"")
        self.assertEqual(status, 400)
        self.assertFalse(payload.get("ok"))

    def test_endpoint_fails_closed_when_the_classifier_breaks(self) -> None:
        """A broken classifier must be visible, not silently mis-routed."""

        from unittest.mock import patch

        with patch.object(
            route_classifier,
            "explain",
            side_effect=RuntimeError("classifier exploded"),
        ):
            status, payload = self.classify("Who is Kate Bush?")
        self.assertEqual(status, 503)
        self.assertFalse(payload.get("ok"))
        self.assertNotIn("is_memory", payload)


if __name__ == "__main__":
    unittest.main()
