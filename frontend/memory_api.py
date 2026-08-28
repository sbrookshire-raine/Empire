"""Safe local uploads and serialized background memory-ingestion jobs."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import threading
import urllib.request
import uuid
from concurrent.futures import Future, ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Literal, TypedDict

import psycopg

from pipeline.ingest_files import validate_dataset, validate_memory_file

ROOT = Path(__file__).resolve().parents[1]
COGNEE_ENV_PATH = ROOT / "config" / "cognee.env"
UPLOAD_ROOT = ROOT / "data" / "eve_memory" / "uploads"
JOB_ROOT = ROOT / "data" / "eve_memory" / "jobs"
POCKETBASE_JOBS_URL = "http://127.0.0.1:8090/api/collections/ingestion_jobs/records"
INGEST_TIMEOUT_SECONDS = 600
ALLOWED_SUFFIXES = {".md", ".txt", ".pdf"}
SAFE_FILENAME_RE = re.compile(r"[^A-Za-z0-9._-]+")
JOB_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")
WINDOWS_RESERVED_NAMES = {
    "aux",
    "clock$",
    "com1",
    "com2",
    "com3",
    "com4",
    "com5",
    "com6",
    "com7",
    "com8",
    "com9",
    "con",
    "lpt1",
    "lpt2",
    "lpt3",
    "lpt4",
    "lpt5",
    "lpt6",
    "lpt7",
    "lpt8",
    "lpt9",
    "nul",
    "prn",
}

JobStatus = Literal["queued", "converting", "embedding", "ready", "failed"]
STATUS_LABELS: dict[JobStatus, str] = {
    "queued": "Uploading",
    "converting": "Reading PDF",
    "embedding": "Learning",
    "ready": "Ready",
    "failed": "Failed",
}
INTERRUPTED_STATUSES = {"queued", "converting", "embedding", "learning", "running"}


class MemoryJob(TypedDict, total=False):
    id: str
    status: JobStatus
    label: str
    dataset: str
    full_graph: bool
    files: list[dict[str, object]]
    paths: list[str]
    result: dict[str, object]
    error: str
    created_at: str
    updated_at: str


IngestCallable = Callable[..., dict[str, object]]
MirrorCallable = Callable[[dict], None]


class MemoryUploadStorageError(RuntimeError):
    """Raised when validated uploads cannot be persisted locally."""


class MemoryJobQueueError(RuntimeError):
    """Raised when a persisted job cannot be submitted to the local worker."""


def ingest_in_subprocess(
    *,
    paths: list[Path],
    dataset: str,
    job_id: str,
    full_graph: bool,
) -> dict[str, object]:
    """Run one Cognee ingestion in a fresh process and event loop."""

    command = [
        sys.executable,
        "-m",
        "pipeline.cognee_worker",
        "ingest-files",
        "--dataset",
        dataset,
        "--job-id",
        job_id,
    ]
    if full_graph:
        command.append("--full-graph")
    for path in paths:
        command.extend(("--path", str(path)))
    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=INGEST_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            f"Memory ingestion timed out after {INGEST_TIMEOUT_SECONDS}s."
        ) from exc
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Memory ingestion worker failed.")
    for line in reversed(result.stdout.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            return payload
    raise RuntimeError("Memory ingestion worker returned no JSON result.")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sanitize_filename(name: str) -> str:
    """Return a basename containing only portable, non-path filename characters."""
    if not isinstance(name, str):
        raise ValueError("Each upload must have a filename.")
    basename = Path(name.replace("\\", "/")).name.strip()
    basename = re.sub(r"\s+", "_", basename)
    basename = SAFE_FILENAME_RE.sub("_", basename)
    basename = re.sub(r"_+", "_", basename).strip(" .")
    if not basename or basename in {".", ".."}:
        raise ValueError("Upload filename is empty after sanitization.")
    if Path(basename).stem.casefold() in WINDOWS_RESERVED_NAMES:
        basename = f"upload_{basename}"
    if len(basename) > 255:
        suffix = Path(basename).suffix
        basename = f"{Path(basename).stem[: 255 - len(suffix)]}{suffix}"
    return basename


def _cognee_settings() -> dict[str, str]:
    settings: dict[str, str] = {}
    if COGNEE_ENV_PATH.exists():
        for line in COGNEE_ENV_PATH.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            settings[key.strip()] = value.strip()
    for key in (
        "DB_PROVIDER",
        "VECTOR_DB_PROVIDER",
        "GRAPH_DATABASE_PROVIDER",
        "SYSTEM_ROOT_DIRECTORY",
        "DB_HOST",
        "DB_PORT",
        "DB_USERNAME",
        "DB_PASSWORD",
        "DB_NAME",
    ):
        if key in os.environ:
            settings[key] = os.environ[key]
    if os.environ.get("EMPIRE_COGNEE_ROOT"):
        settings["SYSTEM_ROOT_DIRECTORY"] = os.environ["EMPIRE_COGNEE_ROOT"]
    return settings


def memory_stack_config() -> dict[str, str]:
    settings = _cognee_settings()
    return {
        "embeddingProvider": settings.get("EMBEDDING_PROVIDER", "ollama"),
        "embeddingModel": settings.get("EMBEDDING_MODEL", "nomic-embed-text:latest"),
        "llmModel": settings.get("LLM_MODEL", "llama3.1:latest"),
        "defaultDataset": "eve_memory",
    }


def memory_readiness() -> dict[str, object]:
    """Return bounded, read-only Cognee storage and Postgres readiness."""

    settings = _cognee_settings()
    providers_ready = (
        settings.get("DB_PROVIDER", "").casefold() == "postgres"
        and settings.get("VECTOR_DB_PROVIDER", "").casefold() == "pgvector"
        and settings.get("GRAPH_DATABASE_PROVIDER", "").casefold() == "postgres"
    )
    storage_value = settings.get("SYSTEM_ROOT_DIRECTORY", "")
    storage = Path(storage_value)
    storage_ready = bool(storage_value) and storage.is_dir()

    postgres_ready = False
    postgres_detail = "Database unavailable."
    try:
        with psycopg.connect(
            host=settings.get("DB_HOST", "localhost"),
            port=int(settings.get("DB_PORT", "5432")),
            user=settings.get("DB_USERNAME", ""),
            password=settings.get("DB_PASSWORD", ""),
            dbname=settings.get("DB_NAME", ""),
            connect_timeout=1,
            options="-c statement_timeout=1000 -c default_transaction_read_only=on",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'vector')"
                )
                row = cursor.fetchone()
                postgres_ready = bool(row and row[0])
                postgres_detail = (
                    "Postgres and pgvector are ready."
                    if postgres_ready
                    else "Postgres is available but pgvector is unavailable."
                )
    except (OSError, ValueError, psycopg.Error):
        postgres_ready = False

    cognee_ready = providers_ready and storage_ready and postgres_ready
    if not providers_ready:
        cognee_detail = "Cognee’s Postgres providers are not configured."
    elif not storage_ready:
        cognee_detail = "Cognee storage is unavailable."
    elif not postgres_ready:
        cognee_detail = "Cognee’s Postgres dependency is unavailable."
    else:
        cognee_detail = "Cognee storage and database are ready."

    return {
        "ready": cognee_ready,
        "cognee": {"ready": cognee_ready, "detail": cognee_detail},
        "postgres": {"ready": postgres_ready, "detail": postgres_detail},
    }


@dataclass(frozen=True)
class UploadPolicy:
    max_file_bytes: int = 52_428_800
    max_files: int = 20

    @property
    def max_request_bytes(self) -> int:
        return self.max_file_bytes * self.max_files + 1_048_576

    def validate(self, name: str, size: int) -> str:
        safe_name = sanitize_filename(name)
        if Path(safe_name).suffix.casefold() not in ALLOWED_SUFFIXES:
            raise ValueError("Memory files must be Markdown, text, or PDF files.")
        if size <= 0:
            raise ValueError(f"Memory file is empty: {safe_name}")
        if size > self.max_file_bytes:
            raise ValueError(f"Memory file exceeds the 50 MiB limit: {safe_name}")
        return safe_name

    def validate_batch(self, files: list[tuple[str, int]]) -> None:
        if not files:
            raise ValueError("At least one memory file is required.")
        if len(files) > self.max_files:
            raise ValueError(f"A memory batch may contain at most {self.max_files} files.")
        for name, size in files:
            self.validate(name, size)

    def validate_request_size(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Upload request is empty.")
        if size > self.max_request_bytes:
            raise ValueError("Upload request is too large.")


DEFAULT_UPLOAD_POLICY = UploadPolicy()


class MemoryJobStore:
    """Store each authoritative job record as one atomically replaced JSON file."""

    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self._lock = threading.RLock()

    def _path(self, job_id: str) -> Path:
        if not isinstance(job_id, str) or JOB_ID_RE.fullmatch(job_id) is None:
            raise ValueError("Invalid memory job ID.")
        return self.root / f"{job_id}.json"

    def write(self, job: dict) -> MemoryJob:
        job_id = str(job.get("id", ""))
        target = self._path(job_id)
        stored = dict(job)
        stored["updated_at"] = _utc_now()
        with self._lock:
            self.root.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(".tmp")
            try:
                with temporary.open("w", encoding="utf-8") as stream:
                    json.dump(stored, stream, indent=2, sort_keys=True)
                    stream.write("\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary.replace(target)
            finally:
                temporary.unlink(missing_ok=True)
        return stored  # type: ignore[return-value]

    def read(self, job_id: str) -> MemoryJob:
        path = self._path(job_id)
        with self._lock:
            if not path.is_file():
                raise KeyError(job_id)
            return json.loads(path.read_text(encoding="utf-8"))

    def list(self) -> list[MemoryJob]:
        with self._lock:
            if not self.root.exists():
                return []
            jobs: list[MemoryJob] = []
            for path in sorted(self.root.glob("*.json")):
                try:
                    jobs.append(json.loads(path.read_text(encoding="utf-8")))
                except (OSError, UnicodeError, json.JSONDecodeError):
                    continue
            return jobs

    def recover_interrupted(self) -> None:
        for job in self.list():
            if job.get("status") in INTERRUPTED_STATUSES:
                job["status"] = "failed"
                job["error"] = "Job was interrupted before completion."
                self.write(job)


def public_job(job: dict) -> dict:
    """Return only job fields safe and useful to the local HTTP client."""
    status = job.get("status")
    if status not in STATUS_LABELS:
        status = "failed"
    visible = {
        key: value
        for key, value in job.items()
        if key not in {"paths", "pocketbase_id"}
    }
    visible["status"] = status
    visible["label"] = STATUS_LABELS[status]
    return visible


def _concise_error(exc: Exception) -> str:
    first_line = str(exc).strip().splitlines()[0] if str(exc).strip() else type(exc).__name__
    return first_line[:300]


_pocketbase_ids: dict[str, str] = {}
_pocketbase_lock = threading.Lock()


def _mirror_to_pocketbase(job: dict) -> None:
    """Best-effort mirror using only the existing local PocketBase collection."""
    status = str(job.get("status"))
    mirrored_status = {
        "queued": "pending",
        "converting": "running",
        "embedding": "running",
        "ready": "success",
        "failed": "failed",
    }.get(status, "failed")
    payload: dict[str, object] = {
        "source_type": "mock",
        "source_file": ", ".join(
            str(item.get("name", "")) for item in job.get("files", [])
        )[:500],
        "status": mirrored_status,
        "records_ingested": int(job.get("result", {}).get("documents", 0)),
        "error": str(job.get("error", ""))[:5000],
    }
    job_id = str(job["id"])
    with _pocketbase_lock:
        pocketbase_id = _pocketbase_ids.get(job_id)
    url = f"{POCKETBASE_JOBS_URL}/{pocketbase_id}" if pocketbase_id else POCKETBASE_JOBS_URL
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="PATCH" if pocketbase_id else "POST",
    )
    with urllib.request.urlopen(request, timeout=2) as response:
        if not pocketbase_id:
            response_payload = json.loads(response.read().decode("utf-8"))
            with _pocketbase_lock:
                _pocketbase_ids[job_id] = str(response_payload["id"])


class MemoryJobRunner:
    """Run ingestion jobs in a single background worker."""

    def __init__(
        self,
        store: MemoryJobStore,
        *,
        ingest: IngestCallable | None = None,
        mirror: MirrorCallable | None = _mirror_to_pocketbase,
    ) -> None:
        self.store = store
        self._ingest = ingest or ingest_in_subprocess
        self._mirror = mirror
        self._executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="memory-ingest")
        self._state_lock = threading.RLock()
        self._closed = False

    @property
    def closed(self) -> bool:
        with self._state_lock:
            return self._closed

    def _best_effort_mirror(self, job: dict) -> None:
        if self._mirror is not None:
            try:
                self._mirror(job)
            except Exception:
                pass

    def _write_transition(self, job: dict) -> MemoryJob:
        stored = self.store.write(job)
        self._best_effort_mirror(stored)
        return stored

    def submit(self, job_id: str) -> Future[MemoryJob]:
        with self._state_lock:
            return self._submit_locked(job_id)

    def _submit_locked(self, job_id: str) -> Future[MemoryJob]:
        if self._closed:
            raise MemoryJobQueueError("Memory job runner is shut down.")
        self._best_effort_mirror(self.store.read(job_id))
        try:
            return self._executor.submit(self._run, job_id)
        except RuntimeError as exc:
            raise MemoryJobQueueError("Memory job runner is shut down.") from exc

    def retry(self, job_id: str) -> Future[MemoryJob]:
        with self._state_lock:
            if self._closed:
                raise MemoryJobQueueError("Memory job runner is shut down.")
            job = self.store.read(job_id)
            if job.get("status") != "failed":
                raise ValueError("Only failed memory jobs can be retried.")
            job["status"] = "queued"
            job.pop("error", None)
            job.pop("result", None)
            self.store.write(job)
            try:
                return self._submit_locked(job_id)
            except MemoryJobQueueError:
                job["status"] = "failed"
                job["error"] = "Memory job queue was unavailable."
                self.store.write(job)
                raise

    def _run(self, job_id: str) -> MemoryJob:
        job = self.store.read(job_id)
        try:
            paths = [Path(path) for path in job.get("paths", [])]
            if any(path.suffix.casefold() == ".pdf" for path in paths):
                job["status"] = "converting"
                job = self._write_transition(job)
            job["status"] = "embedding"
            job = self._write_transition(job)
            result = self._ingest(
                paths=paths,
                dataset=str(job["dataset"]),
                job_id=str(job["id"]),
                full_graph=bool(job.get("full_graph", False)),
            )
            job["status"] = "ready"
            job["result"] = result
            job.pop("error", None)
        except Exception as exc:
            job["status"] = "failed"
            job["error"] = _concise_error(exc)
        return self._write_transition(job)

    def shutdown(self) -> None:
        """Stop accepting submissions and wait for accepted jobs to finish."""
        with self._state_lock:
            self._closed = True
        self._executor.shutdown(wait=True)


JOB_STORE = MemoryJobStore(JOB_ROOT)
JOB_STORE.recover_interrupted()
JOB_RUNNER = MemoryJobRunner(JOB_STORE)


def save_uploads(parts: list, dataset: str, full_graph: bool) -> MemoryJob:
    """Validate and persist one upload batch, then queue local ingestion."""
    safe_dataset = validate_dataset(dataset)
    prepared: list[tuple[str, bytes]] = []
    for part in parts:
        supplied_name = part.get_filename()
        content = part.get_payload(decode=True)
        if not isinstance(content, bytes):
            raise ValueError("Could not decode an uploaded file.")
        safe_name = DEFAULT_UPLOAD_POLICY.validate(supplied_name, len(content))
        prepared.append((safe_name, content))
    DEFAULT_UPLOAD_POLICY.validate_batch(
        [(name, len(content)) for name, content in prepared]
    )
    names = [name.casefold() for name, _content in prepared]
    if len(names) != len(set(names)):
        raise ValueError("Uploaded filenames must be unique.")

    job_id = uuid.uuid4().hex
    upload_dir = UPLOAD_ROOT / job_id
    paths: list[Path] = []
    try:
        upload_dir.mkdir(parents=True, exist_ok=False)
        for name, content in prepared:
            destination = upload_dir / name
            with destination.open("xb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            paths.append(validate_memory_file(destination))
    except ValueError:
        shutil.rmtree(upload_dir, ignore_errors=True)
        raise
    except Exception as exc:
        shutil.rmtree(upload_dir, ignore_errors=True)
        raise MemoryUploadStorageError("Could not save memory upload.") from exc

    created_at = _utc_now()
    job: MemoryJob = {
        "id": job_id,
        "status": "queued",
        "dataset": safe_dataset,
        "full_graph": bool(full_graph),
        "files": [
            {"name": name, "bytes": len(content)} for name, content in prepared
        ],
        "paths": [str(path) for path in paths],
        "created_at": created_at,
        "updated_at": created_at,
    }
    try:
        stored = JOB_STORE.write(job)
    except Exception as exc:
        shutil.rmtree(upload_dir, ignore_errors=True)
        raise MemoryUploadStorageError("Could not save memory upload.") from exc
    try:
        JOB_RUNNER.submit(job_id)
    except Exception as exc:
        job["status"] = "failed"
        job["error"] = "Memory job queue was unavailable."
        try:
            JOB_STORE.write(job)
        except Exception:
            pass
        raise MemoryJobQueueError("Memory job queue is unavailable.") from exc
    return stored
