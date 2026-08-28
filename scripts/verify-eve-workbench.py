"""Bounded, local-only end-to-end verification for the Eve Workbench."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Callable, NamedTuple, TextIO


ROOT = Path(__file__).resolve().parents[1]
PYTHON = ROOT / "venv" / "Scripts" / "python.exe"
COGNEE_STORAGE = Path(r"V:\Cognee")
UPLOAD_ROOT = ROOT / "data" / "eve_memory" / "uploads"
JOB_ROOT = ROOT / "data" / "eve_memory" / "jobs"
LOCAL_APPDATA = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
CONTENT_INDEX_PATH = LOCAL_APPDATA / "EMPIRE" / "memory-jobs" / "content-index.json"
OLLAMA_URL = "http://127.0.0.1:11434/api/tags"
POCKETBASE_URL = "http://127.0.0.1:8090"
FRONTEND_URL = "http://127.0.0.1:8080"
EVE_URL = "http://127.0.0.1:2000"
DATASET_PREFIX = "eve_verify_"
POSTGRES_CONTAINER = "empire-cognee-postgres"
HTTP_TIMEOUT_SECONDS = 10
JOB_TIMEOUT_SECONDS = 300
RECALL_TIMEOUT_SECONDS = 240
STREAM_TIMEOUT_SECONDS = 180
POLL_INTERVAL_SECONDS = 1
MAX_STREAM_LINE_BYTES = 1024 * 1024
JOB_ID_PATTERN = re.compile(r"^[a-f0-9]{32}$")

STAGE_NAMES = (
    "V: Cognee storage",
    "Docker Postgres",
    "Ollama",
    "PocketBase",
    "Frontend Workbench",
    "Eve",
    "Memory upload",
    "Memory job ready",
    "Cognee recall",
    "Eve initial session",
    "Eve initial response",
    "Eve continuation",
    "Eve continuation response",
    "PocketBase tasks read-only",
)


class StageFailure(RuntimeError):
    """A concise verifier-stage failure."""


class Stage(NamedTuple):
    name: str
    check: Callable[[], str]


class StreamState:
    def __init__(self) -> None:
        self.waiting = False
        self.assistant_text = ""
        self.continuation_token = ""
        self.next_index = 0


class VerificationContext:
    def __init__(self) -> None:
        unique = uuid.uuid4().hex
        self.marker = f"EMPIRE_EVE_WORKBENCH_VERIFY_{unique}"
        self.filename = f"eve-workbench-verify-{unique}.txt"
        self.dataset = f"{DATASET_PREFIX}{unique}"
        self.job_id = ""
        self.job_status = ""
        self.session_id = ""
        self.continuation_token = ""
        self.stream_index = 0


def run_stages(stages: tuple[Stage, ...], *, output: TextIO = sys.stdout) -> str | None:
    """Run stages in order, stopping with the exact failed-stage name."""

    for stage in stages:
        started = time.monotonic()
        try:
            detail = stage.check()
        except Exception as exc:
            message = str(exc).strip() or type(exc).__name__
            print(f"FAIL {stage.name}: {message}", file=output, flush=True)
            print(f"FAILED_STAGE={stage.name}", file=output, flush=True)
            return stage.name
        elapsed = time.monotonic() - started
        suffix = f": {detail}" if detail else ""
        print(f"PASS {stage.name} ({elapsed:.1f}s){suffix}", file=output, flush=True)
    return None


def build_multipart(*, filename: str, marker: str, dataset: str) -> tuple[str, bytes]:
    """Build the verifier's one-file multipart upload with no external package."""

    boundary = f"empire-workbench-{uuid.uuid4().hex}"
    body = (
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="dataset"\r\n\r\n'
        f"{dataset}\r\n"
        f"--{boundary}\r\n"
        'Content-Disposition: form-data; name="full_graph"\r\n\r\n'
        "false\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="files"; filename="{filename}"\r\n'
        "Content-Type: text/plain; charset=utf-8\r\n\r\n"
        f"Eve Workbench local verification marker: {marker}\r\n"
        f"--{boundary}--\r\n"
    ).encode("utf-8")
    return f"multipart/form-data; boundary={boundary}", body


def _request(
    url: str,
    *,
    method: str = "GET",
    data: bytes | None = None,
    headers: dict[str, str] | None = None,
    timeout: float = HTTP_TIMEOUT_SECONDS,
) -> tuple[int, dict[str, str], bytes]:
    request = urllib.request.Request(
        url,
        data=data,
        headers=headers or {},
        method=method,
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, dict(response.headers.items()), response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise StageFailure(f"HTTP {exc.code}: {detail or exc.reason}") from exc
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        raise StageFailure(str(exc)) from exc


def _json_request(
    url: str,
    *,
    method: str = "GET",
    payload: dict | None = None,
    timeout: float = HTTP_TIMEOUT_SECONDS,
) -> tuple[dict, dict[str, str]]:
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    _status, response_headers, body = _request(
        url,
        method=method,
        data=data,
        headers=headers,
        timeout=timeout,
    )
    try:
        decoded = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StageFailure("Response was not valid JSON.") from exc
    if not isinstance(decoded, dict):
        raise StageFailure("Expected a JSON object response.")
    return decoded, response_headers


def consume_stream_event(state: StreamState, event: dict) -> None:
    """Project only the event fields needed to verify a completed Eve turn."""

    event_type = event.get("type")
    data = event.get("data")
    if not isinstance(event_type, str) or not isinstance(data, dict):
        return
    if event_type in {"message.appended", "message.completed"}:
        cumulative = data.get("messageSoFar") or data.get("message")
        delta = data.get("messageDelta") or data.get("delta")
        if isinstance(cumulative, str) and cumulative:
            state.assistant_text = cumulative
        elif isinstance(delta, str) and delta:
            state.assistant_text += delta
    if event_type == "session.waiting":
        state.waiting = True
        token = data.get("continuationToken")
        if isinstance(token, str):
            state.continuation_token = token
    if event_type in {"turn.failed", "session.failed", "step.failed", "proxy.error"}:
        message = data.get("message")
        raise StageFailure(str(message) if message else f"Eve emitted {event_type}.")
    proxy = event.get("_proxy")
    if isinstance(proxy, dict) and isinstance(proxy.get("upstreamNextIndex"), int):
        state.next_index = proxy["upstreamNextIndex"]
    else:
        state.next_index += 1


def _read_eve_stream(session_id: str, start_index: int) -> StreamState:
    url = (
        f"{FRONTEND_URL}/api/eve/session/{session_id}/stream"
        f"?startIndex={start_index}"
    )
    request = urllib.request.Request(url, headers={"Accept": "application/x-ndjson"})
    deadline = time.monotonic() + STREAM_TIMEOUT_SECONDS
    state = StreamState()
    try:
        with urllib.request.urlopen(request, timeout=STREAM_TIMEOUT_SECONDS) as response:
            while time.monotonic() < deadline:
                raw_line = response.readline(MAX_STREAM_LINE_BYTES + 1)
                if not raw_line:
                    break
                if len(raw_line) > MAX_STREAM_LINE_BYTES:
                    raise StageFailure("Eve emitted an oversized stream event.")
                try:
                    event = json.loads(raw_line)
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
                if isinstance(event, dict):
                    consume_stream_event(state, event)
                if state.waiting:
                    break
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise StageFailure(f"HTTP {exc.code}: {detail or exc.reason}") from exc
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        raise StageFailure(str(exc)) from exc
    if not state.waiting:
        raise StageFailure("Eve stream ended before session.waiting.")
    if not state.assistant_text.strip():
        raise StageFailure("Eve reached session.waiting without assistant text.")
    return state


def _check_storage() -> str:
    if not COGNEE_STORAGE.is_dir():
        raise StageFailure(f"Missing Cognee storage: {COGNEE_STORAGE}")
    return str(COGNEE_STORAGE)


def _check_postgres() -> str:
    docker = shutil.which("docker")
    if docker is None:
        raise StageFailure("docker executable is unavailable.")
    try:
        result = subprocess.run(
            [
                docker,
                "inspect",
                "--format={{.State.Running}}",
                POSTGRES_CONTAINER,
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise StageFailure("Docker inspect timed out.") from exc
    if result.returncode != 0:
        raise StageFailure(result.stderr.strip() or "Docker Postgres container was not found.")
    if result.stdout.strip().casefold() != "true":
        raise StageFailure("Docker Postgres container is not running.")
    return f"{POSTGRES_CONTAINER} is running"


def _check_ollama() -> str:
    payload, _headers = _json_request(OLLAMA_URL)
    models = payload.get("models")
    if not isinstance(models, list):
        raise StageFailure("Ollama model list is missing.")
    return f"{len(models)} model(s) available"


def _check_pocketbase() -> str:
    payload, _headers = _json_request(f"{POCKETBASE_URL}/api/health")
    if payload.get("code") not in (None, 200) and not payload.get("message"):
        raise StageFailure("PocketBase health response was not healthy.")
    return "health API reachable"


def _check_frontend() -> str:
    _status, _headers, page = _request(f"{FRONTEND_URL}/eve.html")
    if b"Chat with Eve" not in page or b"eve-workbench.js" not in page:
        raise StageFailure("Frontend does not serve the Eve Workbench.")
    memory, _headers = _json_request(f"{FRONTEND_URL}/api/memory/status")
    if not memory.get("ok"):
        raise StageFailure("Running frontend has not loaded the Workbench memory API.")
    return "eve.html and memory API reachable"


def _check_eve() -> str:
    payload, _headers = _json_request(f"{EVE_URL}/eve/v1/info")
    if not payload:
        raise StageFailure("Eve info response was empty.")
    return "info API reachable"


def _upload_fixture(context: VerificationContext) -> str:
    content_type, body = build_multipart(
        filename=context.filename,
        marker=context.marker,
        dataset=context.dataset,
    )
    _status, _headers, response_body = _request(
        f"{FRONTEND_URL}/api/memory/upload",
        method="POST",
        data=body,
        headers={
            "Content-Type": content_type,
            "Content-Length": str(len(body)),
        },
        timeout=HTTP_TIMEOUT_SECONDS,
    )
    try:
        payload = json.loads(response_body.decode("utf-8"))
        job = payload["job"]
        job_id = job["id"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise StageFailure("Upload did not return a memory job.") from exc
    if not isinstance(job_id, str) or JOB_ID_PATTERN.fullmatch(job_id) is None:
        raise StageFailure("Upload returned an invalid memory job ID.")
    if job.get("dataset") != context.dataset:
        raise StageFailure("Upload did not use the unique verification dataset.")
    context.job_id = job_id
    context.job_status = str(job.get("status", ""))
    return f"job {job_id}"


def _poll_job(context: VerificationContext) -> str:
    deadline = time.monotonic() + JOB_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        payload, _headers = _json_request(
            f"{FRONTEND_URL}/api/memory/jobs/{context.job_id}"
        )
        job = payload.get("job")
        if not isinstance(job, dict):
            raise StageFailure("Memory job response is missing.")
        context.job_status = str(job.get("status", ""))
        if context.job_status == "ready":
            return "ready"
        if context.job_status == "failed":
            raise StageFailure(str(job.get("error") or "Memory ingestion failed."))
        time.sleep(POLL_INTERVAL_SECONDS)
    raise StageFailure(f"Memory job did not become ready within {JOB_TIMEOUT_SECONDS}s.")


def _recall_marker(context: VerificationContext) -> str:
    if not PYTHON.is_file():
        raise StageFailure(f"Missing Python environment: {PYTHON}")
    try:
        result = subprocess.run(
            [
                str(PYTHON),
                "-m",
                "pipeline.cognee_worker",
                "recall",
                "--query",
                context.marker,
                "--dataset",
                context.dataset,
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=RECALL_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise StageFailure(f"Cognee recall timed out after {RECALL_TIMEOUT_SECONDS}s.") from exc
    if result.returncode != 0:
        raise StageFailure(result.stderr.strip() or "Cognee recall failed.")
    payload = None
    for line in reversed(result.stdout.splitlines()):
        try:
            candidate = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(candidate, dict):
            payload = candidate
            break
    if payload is None:
        raise StageFailure("Cognee worker returned no JSON result.")
    if context.marker not in json.dumps(payload, ensure_ascii=False):
        raise StageFailure("Cognee recall did not return the unique marker.")
    return f"unique marker recalled from {context.dataset}"


def _create_session(context: VerificationContext) -> str:
    payload, headers = _json_request(
        f"{FRONTEND_URL}/api/eve/session",
        method="POST",
        payload={"message": "Reply with the word READY."},
        timeout=30,
    )
    session_id = payload.get("sessionId") or headers.get("X-Eve-Session-Id")
    if not isinstance(session_id, str) or not session_id:
        raise StageFailure("Eve did not return a session ID.")
    context.session_id = session_id
    token = payload.get("continuationToken")
    if isinstance(token, str):
        context.continuation_token = token
    return f"session {session_id}"


def _read_initial_response(context: VerificationContext) -> str:
    state = _read_eve_stream(context.session_id, context.stream_index)
    context.stream_index = state.next_index
    context.continuation_token = state.continuation_token or context.continuation_token
    return f"assistant text received ({len(state.assistant_text.strip())} chars)"


def _continue_session(context: VerificationContext) -> str:
    if not context.continuation_token:
        raise StageFailure("Eve did not provide a continuation token.")
    payload, _headers = _json_request(
        f"{FRONTEND_URL}/api/eve/session/{context.session_id}",
        method="POST",
        payload={
            "continuationToken": context.continuation_token,
            "message": "Reply with the word READY again.",
        },
        timeout=30,
    )
    token = payload.get("continuationToken")
    if isinstance(token, str) and token:
        context.continuation_token = token
    return "continuation accepted"


def _read_continuation_response(context: VerificationContext) -> str:
    state = _read_eve_stream(context.session_id, context.stream_index)
    context.stream_index = state.next_index
    context.continuation_token = state.continuation_token or context.continuation_token
    return f"second assistant text received ({len(state.assistant_text.strip())} chars)"


def _read_tasks() -> str:
    payload, _headers = _json_request(
        f"{POCKETBASE_URL}/api/collections/tasks/records?perPage=1&page=1"
    )
    total = payload.get("totalItems")
    if not isinstance(total, int):
        raise StageFailure("PocketBase tasks response is missing totalItems.")
    return f"read-only query returned totalItems={total}"


def _worker_json(arguments: list[str], *, timeout: int) -> dict:
    try:
        result = subprocess.run(
            [str(PYTHON), "-m", "pipeline.cognee_worker", *arguments],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise StageFailure(f"Cognee worker timed out after {timeout}s.") from exc
    if result.returncode != 0:
        raise StageFailure(result.stderr.strip() or "Cognee worker failed.")
    for line in reversed(result.stdout.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            return payload
    raise StageFailure("Cognee worker returned no JSON result.")


def _forget_verification_dataset(context: VerificationContext) -> str:
    payload = _worker_json(
        ["forget", "--dataset", context.dataset],
        timeout=RECALL_TIMEOUT_SECONDS,
    )
    if payload.get("dataset") != context.dataset:
        raise StageFailure("Cognee forget returned the wrong dataset.")
    if payload.get("status") not in {"forgotten", "absent"}:
        raise StageFailure("Cognee forget did not confirm dataset removal.")
    return f"dataset {context.dataset} removed"


def remove_content_index_entries(
    context: VerificationContext,
    index_path: Path = CONTENT_INDEX_PATH,
) -> int:
    if not index_path.is_file():
        return 0
    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise StageFailure("Could not read the memory content index.") from exc
    if not isinstance(index, dict):
        raise StageFailure("Memory content index is not an object.")
    prefix = f"{context.dataset}:"
    keys = [
        key
        for key, value in index.items()
        if isinstance(key, str)
        and key.startswith(prefix)
        and isinstance(value, dict)
        and value.get("upload_job_id") == context.job_id
    ]
    for key in keys:
        del index[key]
    if keys:
        temporary = index_path.with_name(
            f".{index_path.name}.{uuid.uuid4().hex}.tmp"
        )
        try:
            temporary.write_text(
                json.dumps(index, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            temporary.replace(index_path)
        finally:
            temporary.unlink(missing_ok=True)
    return len(keys)


def _cleanup_content_index(context: VerificationContext) -> str:
    removed = remove_content_index_entries(context)
    return f"{removed} exact content-index key(s) removed"


def exact_mirror_ids(payload: dict, filename: str) -> list[str]:
    items = payload.get("items")
    if not isinstance(items, list):
        return []
    return [
        str(item["id"])
        for item in items
        if isinstance(item, dict)
        and item.get("source_file") == filename
        and isinstance(item.get("id"), str)
    ]


def _delete_mirrored_job(context: VerificationContext) -> str:
    query = urllib.parse.urlencode(
        {
            "page": "1",
            "perPage": "10",
            "filter": f'source_file = "{context.filename}"',
        }
    )
    payload, _headers = _json_request(
        f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records?{query}"
    )
    record_ids = exact_mirror_ids(payload, context.filename)
    for record_id in record_ids:
        _request(
            f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records/{record_id}",
            method="DELETE",
        )
    remaining, _headers = _json_request(
        f"{POCKETBASE_URL}/api/collections/ingestion_jobs/records?{query}"
    )
    if exact_mirror_ids(remaining, context.filename):
        raise StageFailure("Exact PocketBase mirror still exists after cleanup.")
    return f"{len(record_ids)} exact PocketBase mirror(s) removed"


def _remove_local_artifacts(context: VerificationContext) -> str:
    if not context.job_id:
        return "no local job artifacts created"
    if JOB_ID_PATTERN.fullmatch(context.job_id) is None:
        raise StageFailure("Refusing cleanup for an invalid job ID.")
    if context.job_status not in {"ready", "failed"}:
        raise StageFailure("Memory job is not terminal; local artifacts retained.")
    upload_dir = UPLOAD_ROOT / context.job_id
    job_file = JOB_ROOT / f"{context.job_id}.json"
    if upload_dir.parent != UPLOAD_ROOT or job_file.parent != JOB_ROOT:
        raise StageFailure("Refusing cleanup outside verifier artifact roots.")
    shutil.rmtree(upload_dir, ignore_errors=True)
    job_file.unlink(missing_ok=True)
    if upload_dir.exists() or job_file.exists():
        raise StageFailure("Local verifier artifacts still exist.")
    return "exact upload and job artifacts removed"


def cleanup_context(
    context: VerificationContext,
    *,
    output: TextIO = sys.stdout,
) -> list[str]:
    operations = (
        ("Cognee dataset", _forget_verification_dataset),
        ("content index", _cleanup_content_index),
        ("PocketBase mirror", _delete_mirrored_job),
        ("local artifacts", _remove_local_artifacts),
    )
    failures: list[str] = []
    for label, operation in operations:
        try:
            detail = operation(context)
            print(f"CLEANUP PASS {label}: {detail}", file=output, flush=True)
        except Exception as exc:
            message = str(exc).strip() or type(exc).__name__
            failure = f"{label}: {message}"
            failures.append(failure)
            print(f"CLEANUP FAIL {failure}", file=output, flush=True)
    return failures


def build_stages(context: VerificationContext) -> tuple[Stage, ...]:
    return (
        Stage(STAGE_NAMES[0], _check_storage),
        Stage(STAGE_NAMES[1], _check_postgres),
        Stage(STAGE_NAMES[2], _check_ollama),
        Stage(STAGE_NAMES[3], _check_pocketbase),
        Stage(STAGE_NAMES[4], _check_frontend),
        Stage(STAGE_NAMES[5], _check_eve),
        Stage(STAGE_NAMES[6], lambda: _upload_fixture(context)),
        Stage(STAGE_NAMES[7], lambda: _poll_job(context)),
        Stage(STAGE_NAMES[8], lambda: _recall_marker(context)),
        Stage(STAGE_NAMES[9], lambda: _create_session(context)),
        Stage(STAGE_NAMES[10], lambda: _read_initial_response(context)),
        Stage(STAGE_NAMES[11], lambda: _continue_session(context)),
        Stage(STAGE_NAMES[12], lambda: _read_continuation_response(context)),
        Stage(STAGE_NAMES[13], _read_tasks),
    )


def main() -> int:
    context = VerificationContext()
    print(f"Eve Workbench verification marker: {context.marker}", flush=True)
    failed_stage = None
    cleanup_failures: list[str] = []
    try:
        failed_stage = run_stages(build_stages(context))
    finally:
        cleanup_failures = cleanup_context(context)
    if failed_stage is not None:
        return 1
    if cleanup_failures:
        print("FAILED_STAGE=Cleanup", flush=True)
        return 1
    print(f"PASS all {len(STAGE_NAMES)} Eve Workbench stages", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
