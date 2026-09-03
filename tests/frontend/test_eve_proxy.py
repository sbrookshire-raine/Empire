from __future__ import annotations

import http.client
import io
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from unittest.mock import patch

from frontend import eve_proxy
from frontend.eve_proxy import eve_request, iter_ndjson, project_event
from frontend.serve import EmpireHandler


class SplitStream:
    def __init__(self, chunks: list[bytes], error: Exception | None = None) -> None:
        self.chunks = iter(chunks)
        self.error = error
        self.closed = False
        self.pending = bytearray()

    def read(self, _size: int = -1) -> bytes:
        try:
            return next(self.chunks)
        except StopIteration:
            if self.error is not None:
                error = self.error
                self.error = None
                raise error
            return b""

    def readline(self, _size: int = -1) -> bytes:
        while b"\n" not in self.pending:
            try:
                self.pending.extend(next(self.chunks))
            except StopIteration:
                if self.error is not None:
                    error = self.error
                    self.error = None
                    raise error
                line = bytes(self.pending)
                self.pending.clear()
                return line
        newline = self.pending.index(b"\n") + 1
        line = bytes(self.pending[:newline])
        del self.pending[:newline]
        return line

    def close(self) -> None:
        self.closed = True


class FakeUpstreamResponse(SplitStream):
    def __init__(
        self,
        status: int,
        body: bytes | list[bytes],
        *,
        headers: list[tuple[str, str]] | None = None,
        error: Exception | None = None,
    ) -> None:
        chunks = body if isinstance(body, list) else [body]
        super().__init__(chunks, error)
        self.status = status
        self.reason = "upstream"
        self._headers = headers or [("Content-Type", "application/json")]

    def getheaders(self) -> list[tuple[str, str]]:
        return self._headers


class FakeConnection:
    def __init__(
        self,
        response: FakeUpstreamResponse | None = None,
        *,
        request_error: Exception | None = None,
        response_error: Exception | None = None,
    ) -> None:
        self.response = response
        self.request_error = request_error
        self.response_error = response_error
        self.requests: list[tuple[str, str, bytes | None, dict[str, str]]] = []
        self.closed = False
        self.sock = None

    def request(
        self,
        method: str,
        path: str,
        body: bytes | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        if self.request_error is not None:
            raise self.request_error
        self.requests.append((method, path, body, headers or {}))

    def getresponse(self) -> FakeUpstreamResponse:
        if self.response_error is not None:
            raise self.response_error
        if self.response is None:
            raise AssertionError("Missing fake response")
        return self.response

    def close(self) -> None:
        self.closed = True


class EveProxyProjectionTests(unittest.TestCase):
    def test_ndjson_emits_complete_line_without_block_sized_read(self) -> None:
        class LineOnlyStream:
            def __init__(self) -> None:
                self.readline_calls = 0

            def read(self, size: int = -1) -> bytes:
                raise AssertionError(f"block-sized read would wait: {size}")

            def readline(self, _size: int = -1) -> bytes:
                self.readline_calls += 1
                if self.readline_calls == 1:
                    return b'{"type":"message.appended","data":{"messageDelta":"now"}}\n'
                raise TimeoutError("test must not wait for another event")

        stream = LineOnlyStream()
        events = iter_ndjson(stream)
        self.assertEqual(next(events)["data"]["messageDelta"], "now")
        self.assertEqual(stream.readline_calls, 1)

    def test_ndjson_handles_split_reads_and_unterminated_final_line(self) -> None:
        stream = SplitStream(
            [
                b'{"type":"message.',
                b'appended","data":{"messageDelta":"Hi"}}\n{"type":',
                b'"session.waiting"}',
            ]
        )
        self.assertEqual(
            [event["type"] for event in iter_ndjson(stream)],
            ["message.appended", "session.waiting"],
        )

    def test_ndjson_skips_blank_malformed_and_non_object_lines(self) -> None:
        stream = io.BytesIO(
            b'\nnot-json\n[]\n{"type":"message.appended"}\r\n  \n{"type":"session.waiting"}\n'
        )
        self.assertEqual(
            [event["type"] for event in iter_ndjson(stream)],
            ["message.appended", "session.waiting"],
        )

    def test_malformed_ndjson_is_logged_without_raw_content_or_exception(self) -> None:
        stream = io.BytesIO(
            b'private-secret:not-json\n{"type":"message.appended"}\n'
        )
        with self.assertLogs("frontend.eve_proxy", level="WARNING") as captured:
            events = list(iter_ndjson(stream))
        self.assertEqual(events, [{"type": "message.appended"}])
        logs = "\n".join(captured.output)
        self.assertIn("Dropped malformed Eve NDJSON record", logs)
        self.assertNotIn("private-secret", logs)
        self.assertNotIn("JSONDecodeError", logs)

    def test_reasoning_event_variants_are_hidden(self) -> None:
        variants = (
            "reasoning.appended",
            "reasoning.completed",
            "reasoning_delta",
            "response.reasoning.delta",
            "thinking-appended",
            "REASONING.APPENDED",
        )
        for event_type in variants:
            with self.subTest(event_type=event_type):
                self.assertIsNone(project_event({"type": event_type, "data": {"secret": "chain"}}))

    def test_message_event_keeps_literal_plain_text(self) -> None:
        event = {
            "type": "message.appended",
            "data": {"messageDelta": "<img src=x onerror=alert(1)>", "messageSoFar": "<b>Hello</b>"},
        }
        projected = project_event(event)
        self.assertIsNotNone(projected)
        assert projected is not None
        self.assertEqual(projected["data"]["messageDelta"], "<img src=x onerror=alert(1)>")
        self.assertEqual(projected["data"]["messageSoFar"], "<b>Hello</b>")
        self.assertIsInstance(projected["data"]["messageDelta"], str)

    def test_sanitize_assistant_text_strips_meta_preamble_and_keeps_reply(self) -> None:
        leaked = (
            'Since the input is a question and not a request for the user to perform an action, '
            'we will not call any tools. A simple response would be: "Yes, I\'m ready!"'
        )
        self.assertEqual(
            eve_proxy.sanitize_assistant_text(leaked),
            "Yes, I'm ready!",
        )

    def test_sanitize_assistant_text_strips_think_blocks(self) -> None:
        leaked = "<think>Planning tools.</think>Yes — ready when you are."
        self.assertEqual(
            eve_proxy.sanitize_assistant_text(leaked),
            "Yes — ready when you are.",
        )

    def test_project_event_sanitizes_assistant_messages(self) -> None:
        event = {
            "type": "message.completed",
            "data": {
                "role": "assistant",
                "message": (
                    "Since this is a question, we will not call any tools. "
                    'A simple response would be: "Hey there."'
                ),
            },
        }
        projected = project_event(event)
        self.assertIsNotNone(projected)
        assert projected is not None
        self.assertEqual(projected["data"]["message"], "Hey there.")

    def test_project_event_leaves_user_messages_untouched(self) -> None:
        event = {
            "type": "message.appended",
            "data": {"role": "user", "messageDelta": "are you ready?"},
        }
        projected = project_event(event)
        self.assertEqual(projected, event)

    def test_invalid_event_shape_is_not_exposed(self) -> None:
        for event in ({}, {"type": 3}, {"type": "message.appended", "data": "secret"}):
            with self.subTest(event=event):
                self.assertIsNone(project_event(event))


class EveRequestTests(unittest.TestCase):
    def test_allowed_method_path_matrix_and_query_forwarding(self) -> None:
        cases = (
            ("GET", "/eve/v1/info"),
            ("POST", "/eve/v1/session"),
            ("POST", "/eve/v1/session/ses_abc-123"),
            ("POST", "/eve/v1/session/ses_abc-123/cancel"),
            ("GET", "/eve/v1/session/ses_abc-123/stream"),
            ("GET", "/eve/v1/session/ses_abc-123/stream?startIndex=-1"),
        )
        for method, path in cases:
            with self.subTest(method=method, path=path):
                response = FakeUpstreamResponse(200, b"{}")
                connection = FakeConnection(response)
                with patch.object(eve_proxy, "HTTPConnection", return_value=connection) as constructor:
                    result = eve_request(method, path, {"message": "hello"} if method == "POST" else None)
                constructor.assert_called_once_with("127.0.0.1", 2000, timeout=15)
                self.assertEqual(connection.requests[0][0:2], (method, path))
                self.assertNotIn("Host", connection.requests[0][3])
                result.close()

    def test_rejects_unlisted_methods_paths_encoded_segments_and_queries(self) -> None:
        rejected = (
            ("DELETE", "/eve/v1/session"),
            ("GET", "/eve/v1/health"),
            ("GET", "/eve/v1/session"),
            ("POST", "/eve/v1/session/a/stream"),
            ("GET", "/eve/v1/session/a/cancel"),
            ("GET", "/eve/v1/session/a/stream?other=1"),
            ("GET", "/eve/v1/session/a/stream?startIndex=1&startIndex=2"),
            ("GET", "/eve/v1/session/a/stream?startIndex=1.5"),
            ("GET", "/eve/v1/session/a/stream?startIndex=9007199254740992"),
            ("GET", "/eve/v1/session/%2e%2e/stream"),
            ("GET", "/eve/v1/info?startIndex=0"),
        )
        for method, path in rejected:
            with self.subTest(method=method, path=path):
                with (
                    patch.object(eve_proxy, "HTTPConnection") as constructor,
                    self.assertRaises(eve_proxy.EveRequestError),
                ):
                    eve_request(method, path)
                constructor.assert_not_called()

    def test_json_payload_and_safe_headers_are_forwarded(self) -> None:
        connection = FakeConnection(FakeUpstreamResponse(202, b'{"ok":true}'))
        payload = {"message": "<b>hello</b>"}
        with patch.object(eve_proxy, "HTTPConnection", return_value=connection):
            result = eve_request("POST", "/eve/v1/session", payload)
        method, path, body, headers = connection.requests[0]
        self.assertEqual((method, path), ("POST", "/eve/v1/session"))
        self.assertEqual(json.loads(body), payload)
        self.assertEqual(headers, {"Accept": "application/json", "Content-Type": "application/json"})
        self.assertEqual(result.status, 202)
        result.close()

    def test_stream_uses_bounded_read_timeout(self) -> None:
        class RecordingSocket:
            def __init__(self) -> None:
                self.timeouts: list[float | None] = []

            def settimeout(self, timeout: float | None) -> None:
                self.timeouts.append(timeout)

        connection = FakeConnection(FakeUpstreamResponse(200, b""))
        socket = RecordingSocket()
        connection.sock = socket
        with patch.object(eve_proxy, "HTTPConnection", return_value=connection):
            response = eve_request("GET", "/eve/v1/session/ses_1/stream")
        self.assertEqual(socket.timeouts, [eve_proxy.EVE_STREAM_READ_TIMEOUT_SECONDS])
        self.assertIsNotNone(socket.timeouts[0])
        response.close()
        self.assertTrue(connection.closed)

    def test_connect_and_initial_read_errors_are_sanitized_and_closed(self) -> None:
        cases = (
            FakeConnection(request_error=ConnectionRefusedError("secret path")),
            FakeConnection(response_error=TimeoutError("secret timeout")),
            FakeConnection(
                FakeUpstreamResponse(
                    200,
                    [b'{"partial":'],
                    error=ConnectionResetError("secret response details"),
                )
            ),
        )
        for connection in cases:
            with self.subTest(connection=connection):
                with (
                    patch.object(eve_proxy, "HTTPConnection", return_value=connection),
                    self.assertRaisesRegex(eve_proxy.EveConnectionError, "^Eve is unavailable\\.$"),
                ):
                    eve_request("GET", "/eve/v1/info")
                self.assertTrue(connection.closed)


class EveRouteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), EmpireHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self._stop_server)

    def _stop_server(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def request(
        self,
        method: str,
        path: str,
        *,
        body: bytes | None = None,
        headers: dict[str, str] | None = None,
    ) -> tuple[int, dict[str, str], bytes]:
        connection = http.client.HTTPConnection(*self.server.server_address, timeout=2)
        try:
            connection.request(method, path, body=body, headers=headers or {})
            response = connection.getresponse()
            return response.status, dict(response.getheaders()), response.read()
        finally:
            connection.close()

    def test_same_origin_info_propagates_safe_upstream_status_and_body(self) -> None:
        upstream = FakeUpstreamResponse(
            418,
            b'{"ok":false,"error":"short and safe"}',
            headers=[
                ("Content-Type", "application/json; charset=utf-8"),
                ("Set-Cookie", "secret=never"),
                ("X-Eve-Session-Id", "ses_1"),
            ],
        )
        fake_connection = FakeConnection(upstream)
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            status, headers, body = self.request(
                "GET",
                "/api/eve/info",
                headers={"Origin": "http://127.0.0.1:8080"},
            )
        self.assertEqual(status, 418)
        self.assertEqual(body, b'{"ok":false,"error":"short and safe"}')
        self.assertEqual(headers["Content-Type"], "application/json; charset=utf-8")
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertNotIn("Set-Cookie", headers)
        self.assertEqual(headers["Access-Control-Allow-Origin"], "http://127.0.0.1:8080")

    def test_unsafe_upstream_content_type_cannot_inject_response_headers(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            b"opaque",
            headers=[("Content-Type", "application/json\r\nX-Injected: secret")],
        )
        with patch.object(eve_proxy, "HTTPConnection", return_value=FakeConnection(upstream)):
            status, headers, body = self.request("GET", "/api/eve/info")
        self.assertEqual(status, 200)
        self.assertEqual(body, b"opaque")
        self.assertEqual(headers["Content-Type"], "application/octet-stream")
        self.assertNotIn("X-Injected", headers)

    def test_disallowed_origin_is_rejected_for_get_post_and_options(self) -> None:
        for method in ("GET", "POST", "OPTIONS"):
            with self.subTest(method=method):
                with patch.object(eve_proxy, "HTTPConnection") as constructor:
                    status, headers, body = self.request(
                        method,
                        "/api/eve/info" if method != "POST" else "/api/eve/session",
                        body=b'{"message":"hello"}' if method == "POST" else None,
                        headers={
                            "Content-Type": "application/json",
                            "Origin": "http://evil.example",
                        },
                    )
                self.assertEqual(status, 403)
                self.assertNotIn("Access-Control-Allow-Origin", headers)
                self.assertIn(b"Origin is not allowed", body)
                constructor.assert_not_called()

    def test_route_matrix_rejects_arbitrary_proxy_paths_before_upstream(self) -> None:
        cases = (
            ("GET", "/api/eve/health"),
            ("POST", "/api/eve/info"),
            ("GET", "/api/eve/session"),
            ("GET", "/api/eve/session/a/cancel"),
            ("POST", "/api/eve/session/a/stream"),
            ("GET", "/api/eve/session/a/stream?bad=1"),
        )
        for method, path in cases:
            with self.subTest(method=method, path=path):
                with patch.object(eve_proxy, "HTTPConnection") as constructor:
                    status, _headers, _body = self.request(method, path)
                self.assertIn(status, (400, 404, 405))
                constructor.assert_not_called()

    def test_connect_error_returns_generic_502_without_exception_details(self) -> None:
        fake_connection = FakeConnection(request_error=ConnectionRefusedError("C:\\secret\\socket"))
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            status, _headers, body = self.request("GET", "/api/eve/info")
        self.assertEqual(status, 502)
        self.assertEqual(json.loads(body), {"ok": False, "error": "Eve is unavailable."})
        self.assertNotIn(b"secret", body)

    def test_stream_projects_lines_flushes_headers_and_emits_disconnect_sentinel(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            [
                b'{"type":"message.appended","data":{"messageDelta":"<b>Hi</b>"}}\n',
                b'{"type":"reasoning.appended","data":{"reasoningDelta":"secret"}}\n',
                b"\nnot-json\n",
            ],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
            error=ConnectionResetError("internal details"),
        )
        fake_connection = FakeConnection(upstream)
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            status, headers, body = self.request(
                "GET",
                "/api/eve/session/ses_1/stream?startIndex=0",
            )
        lines = [json.loads(line) for line in body.splitlines()]
        self.assertEqual(status, 200)
        self.assertEqual(headers["Content-Type"], "application/x-ndjson; charset=utf-8")
        self.assertEqual(headers["Cache-Control"], "no-cache")
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertNotIn("Content-Length", headers)
        self.assertEqual(lines[0]["data"]["messageDelta"], "<b>Hi</b>")
        self.assertEqual(
            lines[1],
            {
                "type": "proxy.error",
                "data": {"message": "Eve disconnected. You can retry this message."},
            },
        )
        self.assertNotIn(b"reasoning", body.lower())
        self.assertNotIn(b"secret", body)
        self.assertTrue(upstream.closed)
        self.assertTrue(fake_connection.closed)

    def test_stream_non_success_is_returned_as_finite_safe_response(self) -> None:
        upstream = FakeUpstreamResponse(
            404,
            b'{"ok":false,"error":"Session not found."}',
            headers=[("Content-Type", "application/json")],
        )
        with patch.object(eve_proxy, "HTTPConnection", return_value=FakeConnection(upstream)):
            status, headers, body = self.request("GET", "/api/eve/session/missing/stream")
        self.assertEqual(status, 404)
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertEqual(json.loads(body)["error"], "Session not found.")

    def test_client_disconnect_closes_upstream_stream(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            [b'{"type":"message.appended","data":{"messageDelta":"hello"}}\n'],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
        )
        fake_connection = FakeConnection(upstream)

        class DisconnectingWriter:
            def write(self, _data: bytes) -> int:
                raise BrokenPipeError()

            def flush(self) -> None:
                raise AssertionError("flush should not follow a failed write")

        handler = object.__new__(EmpireHandler)
        handler.wfile = DisconnectingWriter()
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            response = eve_request("GET", "/eve/v1/session/ses_1/stream")
            handler._write_eve_stream(response)
        self.assertTrue(upstream.closed)
        self.assertTrue(fake_connection.closed)

    def test_silent_upstream_timeout_emits_sentinel_and_closes_resources(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            [],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
            error=TimeoutError("private upstream timeout"),
        )
        fake_connection = FakeConnection(upstream)

        class RecordingWriter:
            def __init__(self) -> None:
                self.writes: list[bytes] = []
                self.flushes = 0

            def write(self, data: bytes) -> int:
                self.writes.append(data)
                return len(data)

            def flush(self) -> None:
                self.flushes += 1

        handler = object.__new__(EmpireHandler)
        writer = RecordingWriter()
        handler.wfile = writer
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            response = eve_request("GET", "/eve/v1/session/ses_1/stream")
            handler._write_eve_stream(response)
        self.assertEqual(
            [json.loads(line) for line in writer.writes],
            [eve_proxy.PROXY_ERROR_EVENT],
        )
        self.assertEqual(writer.flushes, 1)
        self.assertTrue(upstream.closed)
        self.assertTrue(fake_connection.closed)

    def test_each_projected_stream_line_is_flushed(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            [
                b'{"type":"message.appended","data":{"messageDelta":"one"}}\n',
                b'{"type":"session.waiting","data":{"continuationToken":"eve:next"}}\n',
            ],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
        )
        fake_connection = FakeConnection(upstream)

        class RecordingWriter:
            def __init__(self) -> None:
                self.writes: list[bytes] = []
                self.flushes = 0

            def write(self, data: bytes) -> int:
                self.writes.append(data)
                return len(data)

            def flush(self) -> None:
                self.flushes += 1

        handler = object.__new__(EmpireHandler)
        writer = RecordingWriter()
        handler.wfile = writer
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            response = eve_request("GET", "/eve/v1/session/ses_1/stream")
            handler._write_eve_stream(response)
        self.assertEqual(len(writer.writes), 2)
        self.assertEqual(writer.flushes, 2)
        self.assertTrue(all(line.endswith(b"\n") for line in writer.writes))
        self.assertTrue(fake_connection.closed)

    def test_projected_stream_preserves_upstream_next_index_across_hidden_events(self) -> None:
        upstream = FakeUpstreamResponse(
            200,
            [
                b'{"type":"message.appended","data":{"messageDelta":"one"}}\n',
                b'{"type":"reasoning.appended","data":{"reasoningDelta":"private"}}\n',
                b'{"type":"session.waiting","data":{"continuationToken":"eve:next"}}\n',
            ],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
        )
        fake_connection = FakeConnection(upstream)
        with patch.object(eve_proxy, "HTTPConnection", return_value=fake_connection):
            status, _headers, body = self.request(
                "GET",
                "/api/eve/session/ses_1/stream?startIndex=7",
            )

        events = [json.loads(line) for line in body.splitlines()]
        self.assertEqual(status, 200)
        self.assertEqual([event["type"] for event in events], ["message.appended", "session.waiting"])
        self.assertEqual(events[0]["_proxy"]["upstreamNextIndex"], 8)
        self.assertEqual(events[1]["_proxy"]["upstreamNextIndex"], 10)
        self.assertNotIn(b"private", body)

    def test_projected_stream_cursor_counts_dropped_oversized_record(self) -> None:
        oversized = (
            b'{"type":"message.appended","data":{"messageDelta":"'
            + b"private-oversized-" * 70_000
            + b'"}}\n'
        )
        self.assertGreater(len(oversized), eve_proxy.MAX_NDJSON_LINE_BYTES)
        upstream = FakeUpstreamResponse(
            200,
            [
                b'{"type":"message.appended","data":{"messageDelta":"one"}}\n',
                oversized,
                b'{"type":"session.waiting","data":{"continuationToken":"eve:next"}}\n',
            ],
            headers=[("Content-Type", "application/x-ndjson; charset=utf-8")],
        )
        with (
            self.assertLogs("frontend.eve_proxy", level="WARNING") as captured,
            patch.object(
                eve_proxy,
                "HTTPConnection",
                return_value=FakeConnection(upstream),
            ),
        ):
            status, _headers, body = self.request(
                "GET",
                "/api/eve/session/ses_1/stream?startIndex=7",
            )

        events = [json.loads(line) for line in body.splitlines()]
        self.assertEqual(status, 200)
        self.assertEqual([event["type"] for event in events], ["message.appended", "session.waiting"])
        self.assertEqual(events[0]["_proxy"]["upstreamNextIndex"], 8)
        self.assertEqual(events[1]["_proxy"]["upstreamNextIndex"], 10)
        self.assertIn("Dropped oversized Eve NDJSON record", "\n".join(captured.output))
        self.assertNotIn(b"private-oversized", body)


if __name__ == "__main__":
    unittest.main()
