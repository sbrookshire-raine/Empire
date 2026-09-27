"""Validate, prepare, and incrementally ingest explicit local memory files."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from docling.document_converter import DocumentConverter
from filelock import FileLock, Timeout

from pipeline.cognee_client import cognify_dataset, embed_dataset, remember_many

DATASET_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
# Two ways in, measured by scripts/document-format-census.py (P13, 2026-09-27):
#   text    - read_text_any decodes it directly. `.mdx` is markdown with a different extension and `.eml` is a
#             text-encoded mail export; both were plain text that no door claimed.
#   docling - converted to Markdown first. Docling already handled all four of these, but only `.pdf` was ever
#             routed to it, so a `.docx` could be read by Eve and never remembered.
TEXT_SUFFIXES = {".md", ".txt", ".mdx", ".eml"}
DOCLING_SUFFIXES = {".pdf", ".docx", ".pptx", ".xlsx"}
ALLOWED_SUFFIXES = TEXT_SUFFIXES | DOCLING_SUFFIXES


def needs_docling(path: Path) -> bool:
    """True when a file must be converted before it can be read as text.

    A named predicate rather than an inline `== ".pdf"` comparison: the inline form is what let the routing bug
    hide, and it is now the single place tests can point at.
    """
    return path.suffix.casefold() in DOCLING_SUFFIXES
MAX_FILE_BYTES = 50 * 1024 * 1024
MAX_BATCH_FILES = 20
DIRECTIVE_FILENAME = "system.md"
DIRECTIVE_PREFIX = "lens_"
CONTENT_INDEX_LOCK_TIMEOUT_SECONDS = 600


class MemoryConversionError(RuntimeError):
    """Raised when a local document cannot be converted into usable memory text."""


@dataclass(frozen=True)
class PreparedDocument:
    source_path: Path
    content: str
    content_hash: str


def validate_dataset(name: str) -> str:
    """Return a safe explicit Cognee dataset name."""
    if not isinstance(name, str) or DATASET_RE.fullmatch(name) is None:
        raise ValueError(
            "Dataset name must contain 1-64 letters, numbers, underscores, or hyphens."
        )
    return name


def validate_memory_file(path: Path) -> Path:
    """Validate one explicit local memory file without reading its contents."""
    candidate = Path(path)
    if any(part.casefold() == "directives" for part in candidate.parts):
        raise ValueError("Files inside a directives path cannot be ingested.")

    filename = candidate.name.casefold()
    if filename == DIRECTIVE_FILENAME or filename.startswith(DIRECTIVE_PREFIX):
        raise ValueError(f"Directive file {candidate.name!r} cannot be ingested.")
    if candidate.suffix.casefold() not in ALLOWED_SUFFIXES:
        raise ValueError(
            "Memory files must be one of: " + ", ".join(sorted(ALLOWED_SUFFIXES)) + "."
        )
    if not candidate.is_file():
        raise ValueError(f"Memory file does not exist or is not a file: {candidate}")

    size = candidate.stat().st_size
    if size == 0:
        raise ValueError(f"Memory file is empty: {candidate.name}")
    if size > MAX_FILE_BYTES:
        raise ValueError(f"Memory file exceeds the 50 MiB limit: {candidate.name}")
    return candidate


def convert_with_docling(source: Path, output_dir: Path) -> Path:
    """Convert a document to UTF-8 Markdown using the installed local Docling API.

    Renamed from `convert_pdf` (P13, 2026-09-27): the body was always a generic `DocumentConverter().convert()`,
    and the old name is precisely what let the routing bug hide — it read as "the PDF path" rather than "the
    conversion path", so nobody noticed Office documents were excluded from a converter that already handled them.
    """
    destination_dir = Path(output_dir)
    destination = destination_dir / f"{source.stem}.md"
    try:
        conversion = DocumentConverter().convert(source)
        markdown = conversion.document.export_to_markdown()
    except Exception as exc:
        raise MemoryConversionError(
            f"Could not convert {source.name} to text with local Docling."
        ) from exc

    if not isinstance(markdown, str) or not markdown.strip():
        raise MemoryConversionError(
            f"Local Docling conversion produced no text for {source.name}."
        )

    destination_dir.mkdir(parents=True, exist_ok=True)
    destination.write_text(markdown, encoding="utf-8")
    return destination


# One tolerant decoder for every vault read. Strict UTF-8 turned Windows
# cp1252/latin-1 notes into UnicodeDecodeError, which the ingest reported as a
# skip - real content never reached memory. latin-1 accepts any byte sequence, so
# this path is total; whitespace and binary rejection stays with the callers.
TEXT_ENCODINGS = ("utf-8", "utf-8-sig", "cp1252", "latin-1")


def read_text_any(path: Path) -> str:
    """Decode a text file without ever raising on encoding.

    Newlines are normalised to LF, matching the universal-newline behaviour of
    the text-mode reads this replaced. That keeps content hashes stable, so the
    content index does not see every CRLF file as brand new and re-embed it.
    """
    raw = path.read_bytes()
    for encoding in TEXT_ENCODINGS:
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = raw.decode("latin-1", errors="replace")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def prepare_document(path: Path, dataset: str, job_id: str) -> PreparedDocument:
    """Read or convert one validated file and stamp traceability metadata."""
    safe_dataset = validate_dataset(dataset)
    source = validate_memory_file(path)

    if needs_docling(source):
        with tempfile.TemporaryDirectory(prefix="empire-docling-") as temporary_dir:
            converted = convert_with_docling(source, Path(temporary_dir))
            body = read_text_any(converted)
    else:
        body = read_text_any(source)

    if not body.strip():
        raise ValueError(f"Memory file contains no text: {source.name}")

    content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
    header = "\n".join(
        (
            f"source_file: {source.name}",
            f"dataset: {safe_dataset}",
            f"upload_job_id: {job_id}",
            f"content_hash: {content_hash}",
        )
    )
    return PreparedDocument(
        source_path=source,
        content=f"{header}\n\n{body}",
        content_hash=content_hash,
    )


def _content_index_path() -> Path:
    local_app_data = os.environ.get("LOCALAPPDATA")
    base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
    return base / "EMPIRE" / "memory-jobs" / "content-index.json"


def _load_content_index(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read memory content index: {path}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Memory content index must contain a JSON object: {path}")
    return data


def _save_content_index(path: Path, index: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        temporary.write_text(
            json.dumps(index, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def _merge_content_index(path: Path, entries: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = FileLock(
        str(path.with_suffix(".lock")),
        timeout=CONTENT_INDEX_LOCK_TIMEOUT_SECONDS,
        thread_local=False,
    )
    try:
        with lock:
            index = _load_content_index(path)
            index.update(entries)
            _save_content_index(path, index)
    except Timeout as exc:
        raise RuntimeError(
            "Timed out waiting for the memory content-index lock after "
            f"{CONTENT_INDEX_LOCK_TIMEOUT_SECONDS}s."
        ) from exc


async def ingest_files_async(
    paths: list[Path],
    dataset: str,
    job_id: str,
    full_graph: bool = False,
) -> dict[str, object]:
    """Ingest one explicit batch, skipping content embedded successfully before."""
    safe_dataset = validate_dataset(dataset)
    if not paths:
        raise ValueError("At least one memory file is required.")
    if len(paths) > MAX_BATCH_FILES:
        raise ValueError(f"A memory batch may contain at most {MAX_BATCH_FILES} files.")

    prepared = [prepare_document(path, safe_dataset, job_id) for path in paths]
    index_path = _content_index_path()
    index = _load_content_index(index_path)
    pending: list[PreparedDocument] = []
    skipped: list[str] = []

    for item in prepared:
        key = f"{safe_dataset}:{item.content_hash}"
        if key in index:
            skipped.append(item.source_path.name)
        else:
            pending.append(item)

    if pending:
        await remember_many(
            [item.content for item in pending],
            dataset=safe_dataset,
            mode="fast",
        )
        await embed_dataset(safe_dataset)

        entries = {
            f"{safe_dataset}:{item.content_hash}": {
                "source_file": item.source_path.name,
                "upload_job_id": job_id,
            }
            for item in pending
        }
        _merge_content_index(index_path, entries)

    if full_graph:
        await cognify_dataset(safe_dataset)

    return {
        "dataset": safe_dataset,
        "files": [item.source_path.name for item in pending],
        "documents": len(pending),
        "hashes": [item.content_hash for item in pending],
        "skipped": skipped,
    }


def ingest_files(
    paths: list[Path],
    dataset: str,
    job_id: str,
    full_graph: bool = False,
) -> dict[str, object]:
    """Synchronously ingest one explicit batch."""
    return asyncio.run(
        ingest_files_async(
            paths=paths,
            dataset=dataset,
            job_id=job_id,
            full_graph=full_graph,
        )
    )
