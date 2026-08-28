from __future__ import annotations

import http.client
import io
import json
import tempfile
import threading
import time
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import frontend.memory_api as memory_api
import frontend.serve as serve
from frontend.memory_api import (
    DEFAULT_UPLOAD_POLICY,
    STATUS_LABELS,
    MemoryJobRunner,
    MemoryJobStore,
    UploadPolicy,
    public_job,
    sanitize_filename,
)
from frontend.serve import EmpireHandler


class UploadPart:
    def __init__(self, filename: str, content: bytes) -> None:
        self._filename = filename
        self._content = content

    def get_filename(self) -> str:
        return self._filename

    def get_payload(self, decode: bool = False) -> bytes:
        if not decode:
            raise AssertionError("Upload payload must be decoded")
        return self._content


def multipart_body(files: list[tuple[str, bytes]], **fields: str) -> tuple[str, bytes]:
    boundary = "empire-test-boundary"
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend(
            (
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode(),
                b"\r\n",
            )
        )
    for filename, content in files:
        chunks.extend(
            (
                f"--{boundary}\r\n".encode(),
                (
                    'Content-Disposition: form-data; name="files"; '
                    f'filename="{filename}"\r\n'
                ).encode(),
                b"Content-Type: application/octet-stream\r\n\r\n",
                content,
                b"\r\n",
            )
        )
    chunks.append(f"--{boundary}--\r\n".encode())
    return f"multipart/form-data; boundary={boundary}", b"".join(chunks)


class MemoryApiTests(unittest.TestCase):
    def test_memory_readiness_checks_cognee_storage_and_pgvector(self) -> None:
        class FakeCursor:
            def __enter__(self):
                return self

            def __exit__(self, *_args) -> None:
                return None

            def execute(self, query: str) -> None:
                self.query = query

            def fetchone(self) -> tuple[bool]:
                return (True,)

        class FakeConnection:
            def __init__(self) -> None:
                self.cursor_instance = FakeCursor()

            def __enter__(self):
                return self

            def __exit__(self, *_args) -> None:
                return None

            def cursor(self) -> FakeCursor:
                return self.cursor_instance

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cognee"
            root.mkdir()
            env_path = Path(tmp) / "cognee.env"
            env_path.write_text(
                "\n".join(
                    (
                        "DB_PROVIDER=postgres",
                        "VECTOR_DB_PROVIDER=pgvector",
                        "GRAPH_DATABASE_PROVIDER=postgres",
                        f"SYSTEM_ROOT_DIRECTORY={root}",
                        "DB_HOST=localhost",
                        "DB_PORT=5432",
                        "DB_USERNAME=cognee",
                        "DB_PASSWORD=secret",
                        "DB_NAME=cognee_db",
                    )
                ),
                encoding="utf-8",
            )
            connection = FakeConnection()
            with (
                patch.object(memory_api, "COGNEE_ENV_PATH", env_path),
                patch.dict(memory_api.os.environ, {}, clear=True),
                patch.object(memory_api.psycopg, "connect", return_value=connection) as connect,
            ):
                readiness = memory_api.memory_readiness()

        self.assertTrue(readiness["ready"])
        self.assertTrue(readiness["postgres"]["ready"])
        self.assertTrue(readiness["cognee"]["ready"])
        self.assertIn("pg_extension", connection.cursor_instance.query)
        self.assertEqual(connect.call_args.kwargs["connect_timeout"], 1)

    def test_filename_drops_path_components_and_unsafe_characters(self) -> None:
        self.assertEqual(sanitize_filename(r"..\..\  my <> notes .txt"), "my_notes_.txt")

    def test_policy_enforces_extension_and_per_file_bounds(self) -> None:
        policy = UploadPolicy(max_file_bytes=4)
        self.assertEqual(policy.validate("notes.MD", 4), "notes.MD")
        for filename, size in (("payload.exe", 1), ("empty.txt", 0), ("large.pdf", 5)):
            with self.subTest(filename=filename), self.assertRaises(ValueError):
                policy.validate(filename, size)

    def test_policy_enforces_request_and_twenty_file_bounds(self) -> None:
        policy = UploadPolicy(max_file_bytes=4, max_files=20)
        policy.validate_request_size(policy.max_request_bytes)
        with self.assertRaises(ValueError):
            policy.validate_request_size(policy.max_request_bytes + 1)
        with self.assertRaises(ValueError):
            policy.validate_batch([("a.txt", 1)] * 21)

    def test_save_uploads_uses_only_job_upload_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = memory_api.MemoryJobStore(root / "jobs")
            runner = memory_api.MemoryJobRunner(
                store,
                ingest=lambda **_kwargs: {},
                mirror=None,
            )
            try:
                with (
                    patch.object(memory_api, "UPLOAD_ROOT", root / "uploads"),
                    patch.object(memory_api, "JOB_STORE", store),
                    patch.object(memory_api, "JOB_RUNNER", runner),
                ):
                    job = memory_api.save_uploads(
                        [UploadPart(r"..\outside\notes.txt", b"hello")],
                        "eve_memory",
                        False,
                    )
            finally:
                runner.shutdown()
            saved_path = Path(job["paths"][0])
            self.assertEqual(saved_path.parent, root / "uploads" / job["id"])
            self.assertEqual(saved_path.read_bytes(), b"hello")
            self.assertFalse((root / "outside" / "notes.txt").exists())

    def test_save_uploads_rejects_more_than_twenty_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = memory_api.MemoryJobStore(Path(tmp) / "jobs")
            runner = memory_api.MemoryJobRunner(store, ingest=lambda **_kwargs: {})
            self.addCleanup(runner.shutdown)
            with (
                patch.object(memory_api, "UPLOAD_ROOT", Path(tmp) / "uploads"),
                patch.object(memory_api, "JOB_STORE", store),
                patch.object(memory_api, "JOB_RUNNER", runner),
                self.assertRaisesRegex(ValueError, "20"),
            ):
                memory_api.save_uploads(
                    [UploadPart(f"{index}.txt", b"x") for index in range(21)],
                    "eve_memory",
                    False,
                )

    def test_directive_rejection_is_delegated_to_ingestion_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = memory_api.MemoryJobStore(Path(tmp) / "jobs")
            runner = memory_api.MemoryJobRunner(store, ingest=lambda **_kwargs: {})
            self.addCleanup(runner.shutdown)
            with (
                patch.object(memory_api, "UPLOAD_ROOT", Path(tmp) / "uploads"),
                patch.object(memory_api, "JOB_STORE", store),
                patch.object(memory_api, "JOB_RUNNER", runner),
                patch.object(
                    memory_api,
                    "validate_memory_file",
                    side_effect=ValueError("Directive file cannot be ingested."),
                ) as validate,
                self.assertRaisesRegex(ValueError, "Directive"),
            ):
                memory_api.save_uploads(
                    [UploadPart("SYSTEM.md", b"do not ingest")],
                    "eve_memory",
                    False,
                )
            validate.assert_called_once()

    def test_job_store_writes_atomic_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            original_replace = Path.replace
            replacements: list[tuple[Path, Path]] = []

            def tracking_replace(source: Path, target: Path) -> Path:
                replacements.append((source, target))
                return original_replace(source, target)

            with patch.object(Path, "replace", tracking_replace):
                store.write({"id": "j1", "status": "queued"})

            self.assertEqual(store.read("j1")["status"], "queued")
            self.assertEqual(len(replacements), 1)
            self.assertEqual(replacements[0][0].suffix, ".tmp")
            self.assertFalse(replacements[0][0].exists())

    def test_interrupted_queued_and_active_jobs_recover_as_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            for status in ("queued", "converting", "embedding", "learning"):
                store.write({"id": status, "status": status})
            store.write({"id": "ready", "status": "ready"})

            store.recover_interrupted()

            for status in ("queued", "converting", "embedding", "learning"):
                self.assertEqual(store.read(status)["status"], "failed")
                self.assertIn("interrupted", store.read(status)["error"].lower())
            self.assertEqual(store.read("ready")["status"], "ready")

    def test_public_jobs_have_valid_status_labels_and_hide_paths(self) -> None:
        for status, label in STATUS_LABELS.items():
            public = public_job({"id": "j1", "status": status, "paths": ["secret"]})
            self.assertEqual(public["label"], label)
            self.assertNotIn("paths", public)

    def test_runner_serializes_work_with_one_worker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            active = 0
            maximum = 0
            lock = threading.Lock()

            def ingest(**_kwargs: object) -> dict[str, int]:
                nonlocal active, maximum
                with lock:
                    active += 1
                    maximum = max(maximum, active)
                time.sleep(0.03)
                with lock:
                    active -= 1
                return {"documents": 1}

            runner = MemoryJobRunner(store, ingest=ingest, mirror=None)
            self.addCleanup(runner.shutdown)
            for job_id in ("j1", "j2"):
                store.write(
                    {
                        "id": job_id,
                        "status": "queued",
                        "dataset": "eve_memory",
                        "full_graph": False,
                        "paths": [str(Path(tmp) / f"{job_id}.txt")],
                        "files": [{"name": f"{job_id}.txt", "bytes": 1}],
                    }
                )
            first = runner.submit("j1")
            second = runner.submit("j2")
            first.result(timeout=2)
            second.result(timeout=2)

            self.assertEqual(maximum, 1)
            self.assertEqual(store.read("j1")["status"], "ready")
            self.assertEqual(store.read("j2")["status"], "ready")

    def test_two_sequential_uploads_use_isolated_ingest_processes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = MemoryJobStore(root / "jobs")
            completed = memory_api.subprocess.CompletedProcess(
                args=[],
                returncode=0,
                stdout=json.dumps({"dataset": "eve_memory", "documents": 1}),
                stderr="",
            )
            with patch.object(memory_api.subprocess, "run", return_value=completed) as run:
                runner = MemoryJobRunner(store, mirror=None)
                try:
                    with (
                        patch.object(memory_api, "UPLOAD_ROOT", root / "uploads"),
                        patch.object(memory_api, "JOB_STORE", store),
                        patch.object(memory_api, "JOB_RUNNER", runner),
                    ):
                        first = memory_api.save_uploads(
                            [UploadPart("first.txt", b"first")],
                            "eve_memory",
                            False,
                        )
                        while store.read(first["id"])["status"] not in {"ready", "failed"}:
                            time.sleep(0.005)
                        second = memory_api.save_uploads(
                            [UploadPart("second.txt", b"second")],
                            "eve_memory",
                            False,
                        )
                        while store.read(second["id"])["status"] not in {"ready", "failed"}:
                            time.sleep(0.005)
                finally:
                    runner.shutdown()

            self.assertEqual(store.read(first["id"])["status"], "ready")
            self.assertEqual(store.read(second["id"])["status"], "ready")
            self.assertEqual(run.call_count, 2)
            for call in run.call_args_list:
                command = call.args[0]
                self.assertIn("pipeline.cognee_worker", command)
                self.assertIn("ingest-files", command)
                self.assertIsNotNone(call.kwargs["timeout"])

    def test_runner_best_effort_mirrors_queued_transition(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            mirrored: list[str] = []
            runner = MemoryJobRunner(
                store,
                ingest=lambda **_kwargs: {"documents": 0},
                mirror=lambda job: mirrored.append(str(job["status"])),
            )
            self.addCleanup(runner.shutdown)
            store.write(
                {
                    "id": "j1",
                    "status": "queued",
                    "dataset": "eve_memory",
                    "full_graph": False,
                    "paths": [],
                    "files": [],
                }
            )

            runner.submit("j1").result(timeout=2)

            self.assertEqual(mirrored[0], "queued")
            self.assertEqual(mirrored[-1], "ready")

    def test_retry_accepts_only_failed_jobs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            runner = MemoryJobRunner(
                store,
                ingest=lambda **_kwargs: {"documents": 0},
                mirror=None,
            )
            self.addCleanup(runner.shutdown)
            store.write(
                {
                    "id": "failed",
                    "status": "failed",
                    "dataset": "eve_memory",
                    "full_graph": False,
                    "paths": [],
                    "files": [],
                }
            )
            store.write({"id": "ready", "status": "ready"})

            runner.retry("failed").result(timeout=2)
            self.assertEqual(store.read("failed")["status"], "ready")
            with self.assertRaises(ValueError):
                runner.retry("ready")

    def test_concurrent_retry_submits_failed_job_once(self) -> None:
        class SlowFailedReadStore(MemoryJobStore):
            def read(self, job_id: str) -> memory_api.MemoryJob:
                job = super().read(job_id)
                if job.get("status") == "failed":
                    time.sleep(0.03)
                return job

        with tempfile.TemporaryDirectory() as tmp:
            store = SlowFailedReadStore(Path(tmp))
            ingests = 0
            ingest_lock = threading.Lock()

            def ingest(**_kwargs: object) -> dict[str, int]:
                nonlocal ingests
                with ingest_lock:
                    ingests += 1
                return {"documents": 0}

            runner = MemoryJobRunner(store, ingest=ingest, mirror=None)
            self.addCleanup(runner.shutdown)
            store.write(
                {
                    "id": "failed",
                    "status": "failed",
                    "dataset": "eve_memory",
                    "full_graph": False,
                    "paths": [],
                    "files": [],
                }
            )
            barrier = threading.Barrier(8)
            outcomes: list[str] = []
            outcomes_lock = threading.Lock()

            def retry() -> None:
                barrier.wait()
                try:
                    runner.retry("failed").result(timeout=2)
                    outcome = "submitted"
                except ValueError:
                    outcome = "rejected"
                with outcomes_lock:
                    outcomes.append(outcome)

            threads = [threading.Thread(target=retry) for _index in range(8)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join(timeout=3)

            self.assertTrue(all(not thread.is_alive() for thread in threads))
            self.assertEqual(outcomes.count("submitted"), 1)
            self.assertEqual(outcomes.count("rejected"), 7)
            self.assertEqual(ingests, 1)

    def test_shutdown_waits_for_active_job_then_rejects_submissions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))
            started = threading.Event()
            release = threading.Event()

            def ingest(**_kwargs: object) -> dict[str, int]:
                started.set()
                release.wait(timeout=2)
                return {"documents": 0}

            runner = MemoryJobRunner(store, ingest=ingest, mirror=None)
            store.write(
                {
                    "id": "j1",
                    "status": "queued",
                    "dataset": "eve_memory",
                    "full_graph": False,
                    "paths": [],
                    "files": [],
                }
            )
            store.write({"id": "j2", "status": "queued"})
            runner.submit("j1")
            self.assertTrue(started.wait(timeout=1))

            shutdown_thread = threading.Thread(target=runner.shutdown)
            shutdown_thread.start()
            deadline = time.monotonic() + 1
            while not runner.closed and time.monotonic() < deadline:
                time.sleep(0.005)

            self.assertTrue(runner.closed)
            self.assertTrue(shutdown_thread.is_alive())
            with self.assertRaisesRegex(RuntimeError, "shut down"):
                runner.submit("j2")
            release.set()
            shutdown_thread.join(timeout=2)
            self.assertFalse(shutdown_thread.is_alive())

    def test_mirror_failure_does_not_break_job_and_errors_are_concise(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryJobStore(Path(tmp))

            def broken_ingest(**_kwargs: object) -> dict:
                raise RuntimeError("first line\n" + ("detail " * 200))

            def broken_mirror(_job: dict) -> None:
                raise OSError("PocketBase unavailable")

            runner = MemoryJobRunner(store, ingest=broken_ingest, mirror=broken_mirror)
            self.addCleanup(runner.shutdown)
            store.write(
                {
                    "id": "j1",
                    "status": "queued",
                    "dataset": "eve_memory",
                    "full_graph": False,
                    "paths": [],
                    "files": [],
                }
            )
            runner.submit("j1").result(timeout=2)
            job = store.read("j1")
            self.assertEqual(job["status"], "failed")
            self.assertEqual(job["error"], "first line")
            self.assertLessEqual(len(job["error"]), 300)


class MemoryHttpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.store = memory_api.MemoryJobStore(root / "jobs")
        self.runner = memory_api.MemoryJobRunner(
            self.store,
            ingest=lambda **_kwargs: {"documents": 1},
            mirror=None,
        )
        self.patches = (
            patch.object(memory_api, "UPLOAD_ROOT", root / "uploads"),
            patch.object(memory_api, "JOB_STORE", self.store),
            patch.object(memory_api, "JOB_RUNNER", self.runner),
            patch.object(
                memory_api,
                "memory_readiness",
                return_value={
                    "ready": True,
                    "cognee": {"ready": True, "detail": "Ready."},
                    "postgres": {"ready": True, "detail": "Ready."},
                },
            ),
        )
        for item in self.patches:
            item.start()
            self.addCleanup(item.stop)

        class MultipartFirstHandler(EmpireHandler):
            def _read_json(self) -> dict:
                if self.path == "/api/memory/upload":
                    raise AssertionError("JSON parser ran before multipart parser")
                return super()._read_json()

            def log_message(self, _format: str, *_args: object) -> None:
                return None

        server_type = getattr(serve, "EmpireHTTPServer", ThreadingHTTPServer)
        if server_type is ThreadingHTTPServer:
            self.server = server_type(("127.0.0.1", 0), MultipartFirstHandler)
        else:
            self.server = server_type(
                ("127.0.0.1", 0),
                MultipartFirstHandler,
                memory_runner=self.runner,
            )
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self._close_server)
        self.port = self.server.server_address[1]

    def _close_server(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()
        if not hasattr(serve, "EmpireHTTPServer"):
            self.runner.shutdown()

    def request(
        self,
        method: str,
        path: str,
        body: bytes = b"",
        headers: dict[str, str] | None = None,
    ) -> tuple[int, dict]:
        status, payload, _headers = self.request_with_headers(method, path, body, headers)
        return status, payload

    def request_with_headers(
        self,
        method: str,
        path: str,
        body: bytes = b"",
        headers: dict[str, str] | None = None,
    ) -> tuple[int, dict, dict[str, str]]:
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=2)
        connection.request(method, path, body=body, headers=headers or {})
        response = connection.getresponse()
        payload = json.loads(response.read().decode())
        response_headers = dict(response.getheaders())
        connection.close()
        return response.status, payload, response_headers

    def test_upload_parses_multipart_before_json_and_returns_accepted_job(self) -> None:
        content_type, body = multipart_body(
            [(r"..\..\notes.txt", b"hello")],
            dataset="eve_memory",
            full_graph="false",
        )
        status, payload = self.request(
            "POST",
            "/api/memory/upload",
            body,
            {"Content-Type": content_type, "Content-Length": str(len(body))},
        )
        self.assertEqual(status, 202)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["job"]["status"], "queued")
        self.assertEqual(payload["job"]["label"], "Uploading")
        self.assertEqual(payload["job"]["files"], [{"name": "notes.txt", "bytes": 5}])

    def test_oversized_request_is_rejected_before_body_read(self) -> None:
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=2)
        connection.putrequest("POST", "/api/memory/upload")
        connection.putheader("Content-Type", "multipart/form-data; boundary=x")
        connection.putheader("Content-Length", str(DEFAULT_UPLOAD_POLICY.max_request_bytes + 1))
        connection.endheaders()
        response = connection.getresponse()
        payload = json.loads(response.read().decode())
        connection.close()
        self.assertEqual(response.status, 413)
        self.assertFalse(payload["ok"])

    def test_status_unknown_job_and_retry_conflict_routes(self) -> None:
        readiness = {
            "ready": False,
            "cognee": {"ready": False, "detail": "Storage unavailable."},
            "postgres": {"ready": False, "detail": "Database unavailable."},
        }
        with patch.object(memory_api, "memory_readiness", return_value=readiness):
            status, payload = self.request("GET", "/api/memory/status")
        self.assertEqual(status, 200)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["statuses"]["ready"], "Ready")
        self.assertEqual(payload["readiness"], readiness)
        self.assertFalse(payload["readiness"]["ready"])

        status, _payload = self.request("GET", "/api/memory/jobs/missing")
        self.assertEqual(status, 404)

        self.store.write({"id": "ready", "status": "ready"})
        status, payload = self.request("POST", "/api/memory/jobs/ready/retry")
        self.assertEqual(status, 409)
        self.assertIn("failed", payload["error"].lower())

    def test_unexpected_parser_error_returns_concise_json(self) -> None:
        content_type, body = multipart_body([("notes.txt", b"hello")])
        with patch.object(
            serve.BytesParser,
            "parsebytes",
            side_effect=RuntimeError("SECRET parser traceback detail"),
        ):
            status, payload = self.request(
                "POST",
                "/api/memory/upload",
                body,
                {"Content-Type": content_type, "Content-Length": str(len(body))},
            )
        self.assertEqual(status, 400)
        self.assertEqual(payload, {"ok": False, "error": "Could not parse multipart upload."})
        self.assertNotIn("SECRET", json.dumps(payload))

    def test_unexpected_filesystem_error_returns_concise_json(self) -> None:
        content_type, body = multipart_body([("notes.txt", b"hello")])
        with patch.object(
            memory_api,
            "validate_memory_file",
            side_effect=OSError("SECRET filesystem path and trace"),
        ):
            status, payload = self.request(
                "POST",
                "/api/memory/upload",
                body,
                {"Content-Type": content_type, "Content-Length": str(len(body))},
            )
        self.assertEqual(status, 500)
        self.assertEqual(payload, {"ok": False, "error": "Could not save memory upload."})
        self.assertNotIn("SECRET", json.dumps(payload))

    def test_unexpected_job_submit_error_returns_concise_json(self) -> None:
        content_type, body = multipart_body([("notes.txt", b"hello")])
        with patch.object(
            self.runner,
            "submit",
            side_effect=RuntimeError("SECRET executor shutdown detail"),
        ):
            status, payload = self.request(
                "POST",
                "/api/memory/upload",
                body,
                {"Content-Type": content_type, "Content-Length": str(len(body))},
            )
        self.assertEqual(status, 503)
        self.assertEqual(payload, {"ok": False, "error": "Memory job queue is unavailable."})
        self.assertNotIn("SECRET", json.dumps(payload))

    def test_memory_mutation_rejects_arbitrary_browser_origin(self) -> None:
        content_type, body = multipart_body([("notes.txt", b"hello")])
        status, payload, headers = self.request_with_headers(
            "POST",
            "/api/memory/upload",
            body,
            {
                "Content-Type": content_type,
                "Content-Length": str(len(body)),
                "Origin": "https://evil.example",
            },
        )
        self.assertEqual(status, 403)
        self.assertEqual(payload, {"ok": False, "error": "Origin is not allowed."})
        self.assertNotIn("Access-Control-Allow-Origin", headers)

    def test_memory_response_allows_same_origin_without_wildcard(self) -> None:
        status, _payload, headers = self.request_with_headers(
            "GET",
            "/api/memory/status",
            headers={"Origin": "http://127.0.0.1:8080"},
        )
        self.assertEqual(status, 200)
        self.assertEqual(
            headers.get("Access-Control-Allow-Origin"),
            "http://127.0.0.1:8080",
        )
        self.assertNotEqual(headers.get("Access-Control-Allow-Origin"), "*")

    def test_server_close_shuts_down_memory_runner(self) -> None:
        if not hasattr(serve, "EmpireHTTPServer"):
            self.fail("EmpireHTTPServer lifecycle seam is missing")
        self.assertFalse(self.runner.closed)
        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()
        self.assertTrue(self.runner.closed)


if __name__ == "__main__":
    unittest.main()
