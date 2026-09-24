"""Trace correlation (E-18): every record for one browser turn shares one `turn` id.

`turn.start` used to carry model/mode/message but no session, while the streamed
`tool.requested` / `tool.result` / `stream.end` records carried a session but no turn — so with
two sessions in flight (browser tracer beside the voice router, or a second tab) tool events
could not be attributed to the turn that caused them. `turn` is now the join key, minted once
per POST before the first trace record, and it is the same id the ambient capture uses.
"""

from __future__ import annotations

import http.client
import io
import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import eve_proxy, serve
from frontend.serve import EmpireHandler


async def _no_catalog_context(_message: str) -> str:
    """Keep the catalog router (a model call) out of the unit test."""

    return ""


def _identity(payload):
    return payload


def _ndjson(events: list[dict]) -> bytes:
    return b"".join(json.dumps(event).encode("utf-8") + b"\n" for event in events)


class _Closable:
    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True


class _RecordingWriter:
    def __init__(self) -> None:
        self.writes: list[bytes] = []

    def write(self, data: bytes) -> int:
        self.writes.append(data)
        return len(data)

    def flush(self) -> None:
        pass


class _TraceFileTestCase(unittest.TestCase):
    """Points the trace + ambient logs at a temp dir so no test writes into eve-audit."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        audit = Path(self._tmp.name)
        self.trace_path = audit / "eve-trace.jsonl"
        self.ambient_path = audit / "active_chat.log"
        for patcher in (
            patch.object(serve, "TRACE_ENABLED", True),
            patch.object(serve, "TRACE_LOG_PATH", self.trace_path),
            patch.object(serve, "AMBIENT_LOG_PATH", self.ambient_path),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    def records(self) -> list[dict]:
        if not self.trace_path.exists():
            return []
        return [
            json.loads(line)
            for line in self.trace_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def ambient(self) -> list[dict]:
        if not self.ambient_path.exists():
            return []
        return [
            json.loads(line)
            for line in self.ambient_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


class StreamCorrelationTests(_TraceFileTestCase):
    def test_streamed_records_share_the_turn_id_and_carry_the_session(self) -> None:
        events = [
            {"type": "actions.requested", "data": {"actions": [{"toolName": "wiki_scout_search"}]}},
            {"type": "action.result", "data": {"ok": True}},
            {"type": "turn.started", "data": {"stepIndex": 0}},
            {"type": "message.appended", "data": {"messageDelta": "hello", "stepIndex": 0}},
            {"type": "message.completed", "data": {"message": "hello", "stepIndex": 0}},
        ]
        connection = _Closable()
        response = eve_proxy.EveResponse(
            status=200,
            headers={"Content-Type": "application/x-ndjson; charset=utf-8"},
            body=b"",
            stream=io.BytesIO(_ndjson(events)),
            connection=connection,
        )
        handler = object.__new__(EmpireHandler)
        handler.wfile = _RecordingWriter()
        handler._ambient_turn_id = "turn-abc123"
        handler._ambient_user_text = "what is magnetism"

        with patch("pipeline.wiki_lookup_lock.clear_wiki_lookup_lock"):
            handler._write_eve_stream(response, session_id="ses_1")

        records = self.records()
        kinds = [record["kind"] for record in records]
        self.assertIn("tool.requested", kinds)
        self.assertIn("tool.result", kinds)
        self.assertIn("stream.end", kinds)
        for record in records:
            self.assertEqual(record.get("turn"), "turn-abc123", record)
            self.assertEqual(record.get("session"), "ses_1", record)
        requested = next(record for record in records if record["kind"] == "tool.requested")
        self.assertEqual(requested["tools"], ["wiki_scout_search"])
        self.assertTrue(connection.closed)
        # The ambient capture (chat continuity) joins on the same turn id.
        self.assertEqual({event["turn_id"] for event in self.ambient()}, {"turn-abc123"})

    def test_explicit_turn_id_wins_over_the_ambient_one(self) -> None:
        response = eve_proxy.EveResponse(
            status=200,
            headers={"Content-Type": "application/x-ndjson; charset=utf-8"},
            body=b"",
            stream=io.BytesIO(_ndjson([{"type": "turn.completed", "data": {"stepIndex": 0}}])),
            connection=_Closable(),
        )
        handler = object.__new__(EmpireHandler)
        handler.wfile = _RecordingWriter()
        handler._ambient_turn_id = "ambient-turn"

        handler._write_eve_stream(response, session_id="ses_2", turn_id="caller-turn")

        records = self.records()
        self.assertTrue(records)
        self.assertTrue(all(record.get("turn") == "caller-turn" for record in records), records)

    def test_stream_resolves_the_turn_id_through_the_session_bridge(self) -> None:
        """The POST mints the turn id; the GET /stream carries the tool events on another handler.

        Without the session→turn bridge the tool events land in a separate "(no turn id)" group —
        measured live 2026-09-24, which made per-turn tool attribution impossible with two sessions
        in flight.
        """

        serve.remember_turn("ses_bridge", "turn-from-post")
        self.assertEqual(serve.turn_for_session("ses_bridge"), "turn-from-post")
        response = eve_proxy.EveResponse(
            status=200,
            headers={"Content-Type": "application/x-ndjson; charset=utf-8"},
            body=b"",
            stream=io.BytesIO(
                _ndjson(
                    [
                        {"type": "actions.requested", "data": {"actions": [{"toolName": "wiki_scout_search"}]}},
                        {"type": "action.result", "data": {"ok": True}},
                    ]
                )
            ),
            connection=_Closable(),
        )
        handler = object.__new__(EmpireHandler)
        handler.wfile = _RecordingWriter()
        # No per-request id and no caller id: only the bridge can supply it.
        handler._write_eve_stream(response, session_id="ses_bridge")

        records = self.records()
        self.assertTrue(records)
        self.assertTrue(all(record.get("turn") == "turn-from-post" for record in records), records)

    def test_remember_turn_is_bounded_and_keeps_the_newest(self) -> None:
        for index in range(serve._MAX_TRACKED_SESSIONS + 20):
            serve.remember_turn(f"ses_{index}", f"turn_{index}")
        self.assertLessEqual(len(serve._TURN_BY_SESSION), serve._MAX_TRACKED_SESSIONS)
        newest = serve._MAX_TRACKED_SESSIONS + 19
        self.assertEqual(serve.turn_for_session(f"ses_{newest}"), f"turn_{newest}")

    def test_missing_turn_id_still_writes_session_only_records(self) -> None:
        """No turn id anywhere must not break tracing — it degrades to the old shape."""

        response = eve_proxy.EveResponse(
            status=200,
            headers={"Content-Type": "application/x-ndjson; charset=utf-8"},
            body=b"",
            stream=io.BytesIO(_ndjson([{"type": "turn.completed", "data": {"stepIndex": 0}}])),
            connection=_Closable(),
        )
        handler = object.__new__(EmpireHandler)
        handler.wfile = _RecordingWriter()

        handler._write_eve_stream(response, session_id="ses_3")

        records = self.records()
        self.assertTrue(records)
        self.assertTrue(all(record.get("turn") == "" for record in records), records)
        self.assertTrue(all(record.get("session") == "ses_3" for record in records), records)


class TurnStartCorrelationTests(_TraceFileTestCase):
    """`turn.start` carries the turn id and, when the path has one, the session id."""

    def setUp(self) -> None:
        super().setUp()
        self.server = serve.EmpireHTTPServer(("127.0.0.1", 0), EmpireHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self._stop_server)

    def _stop_server(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def _post_turn(self, path: str) -> int:
        upstream = eve_proxy.EveResponse(
            status=200,
            headers={"Content-Type": "application/json"},
            body=json.dumps({"sessionId": "ses_1"}).encode("utf-8"),
            stream=None,
            connection=_Closable(),
        )
        with (
            patch.object(serve.eve_proxy, "eve_request", return_value=upstream),
            patch.object(serve.eve_toolbelt, "apply_active_tools", _identity),
            patch.object(serve.ollama_api, "apply_chat_mode_payload", _identity),
            patch.object(
                serve.ollama_api,
                "load_active_config",
                return_value={"model": "empire-fast:14b", "mode": "fast"},
            ),
            patch.object(serve.resource_pulse_api, "enrich_eve_message_payload", _identity),
            patch.object(serve.companion_api, "enrich_eve_message_payload", _identity),
            patch.object(serve.memory_api, "enrich_eve_message_payload", _identity),
            patch.object(serve.chat_continuity, "enrich_eve_message_payload", _identity),
            patch.object(serve.workbench_ui_api, "enrich_eve_message_payload", _identity),
            patch.object(serve, "_catalog_context_async", _no_catalog_context),
        ):
            client = http.client.HTTPConnection(*self.server.server_address, timeout=5)
            try:
                client.request(
                    "POST",
                    path,
                    body=json.dumps({"message": "what is magnetism"}).encode("utf-8"),
                    headers={
                        "Content-Type": "application/json",
                        "Origin": "http://127.0.0.1:8080",
                    },
                )
                response = client.getresponse()
                response.read()
                status = response.status
            finally:
                client.close()
        return status

    def test_each_turn_gets_its_own_id_and_the_session_from_the_path(self) -> None:
        self.assertEqual(self._post_turn("/api/eve/session/ses_1"), 200)
        self.assertEqual(self._post_turn("/api/eve/session/ses_1"), 200)

        starts = [record for record in self.records() if record["kind"] == "turn.start"]
        self.assertEqual(len(starts), 2)
        turns = [record["turn"] for record in starts]
        self.assertTrue(all(len(turn) == 32 for turn in turns), turns)
        self.assertNotEqual(turns[0], turns[1])
        for record in starts:
            self.assertEqual(record["session"], "ses_1")
            self.assertEqual(record["model"], "empire-fast:14b")
            self.assertEqual(record["mode"], "fast")
            self.assertEqual(record["message"], "what is magnetism")


if __name__ == "__main__":
    unittest.main()
