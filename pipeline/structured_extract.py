"""Bounded DocumentMetadata extraction via llama.cpp (preferred) or Ollama JSON fallback.

Scratch artifacts only — never Cognee. Requires Toolbelt when used from Eve.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pipeline.artifact_lineage import lineage_envelope, lineage_markdown_block, sha256_text
from pipeline import gpu_lease
from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE = Path(
    os.environ.get(
        "EMPIRE_EXTRACT_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\extract_cache",
    )
)
FIXTURE_DIR = EMPIRE_ROOT / "data" / "eval" / "structured_extract" / "fixtures"
EXPECTED_DIR = EMPIRE_ROOT / "data" / "eval" / "structured_extract" / "expected"
ACCEPTANCE_DIR = EMPIRE_ROOT / "data" / "eval" / "acceptance"
MANIFEST_PATH = EMPIRE_ROOT / "config" / "empire-release-manifest.json"
SCHEMA_ID = "DocumentMetadata.v1"
DOCUMENT_METADATA_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "date": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
    },
    "required": ["title", "author", "date", "tags", "summary"],
}
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")


def _safe_name(value: str, fallback: str = "extract") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="extract-", suffix=".md", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def load_manifest() -> dict[str, Any]:
    try:
        raw = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def worker_config() -> dict[str, Any]:
    workers = load_manifest().get("workers") or {}
    cfg = workers.get("structured_extract") if isinstance(workers, dict) else {}
    return cfg if isinstance(cfg, dict) else {}


def llama_base_url() -> str:
    env = os.environ.get("EMPIRE_LLAMA_EXTRACT_URL", "").strip()
    if env:
        return env.rstrip("/")
    listen = str(worker_config().get("listen") or "http://127.0.0.1:8092")
    return listen.rstrip("/")


def ollama_base_url() -> str:
    return os.environ.get("EMPIRE_OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")


def _http_json(url: str, payload: dict[str, Any], *, timeout: float = 120.0) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "EMPIRE-StructuredExtract/1.0"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:  # noqa: S310 — localhost workers
            raw = resp.read(4_000_000)
    except HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:
            pass
        return {"ok": False, "error": f"HTTP {exc.code}", "detail": detail}
    except URLError as exc:
        return {"ok": False, "error": str(exc.reason or exc)}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}
    try:
        data = json.loads(raw.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        return {"ok": False, "error": f"invalid JSON: {exc}"}
    return {"ok": True, "data": data}


def _extract_message_text(data: dict[str, Any]) -> str:
    choices = data.get("choices")
    if isinstance(choices, list) and choices:
        msg = choices[0].get("message") if isinstance(choices[0], dict) else None
        if isinstance(msg, dict):
            content = msg.get("content")
            if isinstance(content, str):
                return content
    # Ollama native
    message = data.get("message")
    if isinstance(message, dict) and isinstance(message.get("content"), str):
        return str(message.get("content"))
    if isinstance(data.get("response"), str):
        return str(data.get("response"))
    return ""


def _parse_metadata_json(text: str) -> dict[str, Any] | None:
    cleaned = (text or "").strip()
    if not cleaned:
        return None
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        obj = json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", cleaned)
        if not match:
            return None
        try:
            obj = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    if not isinstance(obj, dict):
        return None
    title = str(obj.get("title") or "").strip()
    author = str(obj.get("author") or "").strip()
    date = str(obj.get("date") or "").strip()
    summary = str(obj.get("summary") or "").strip()
    tags_raw = obj.get("tags")
    tags: list[str] = []
    if isinstance(tags_raw, list):
        tags = [str(t).strip() for t in tags_raw if str(t).strip()]
    elif isinstance(tags_raw, str) and tags_raw.strip():
        tags = [p.strip() for p in tags_raw.split(",") if p.strip()]
    return {
        "title": title,
        "author": author,
        "date": date,
        "tags": tags,
        "summary": summary,
    }


def validate_metadata(obj: dict[str, Any] | None) -> bool:
    if not obj:
        return False
    if not str(obj.get("title") or "").strip():
        return False
    if not isinstance(obj.get("tags"), list):
        return False
    if not str(obj.get("summary") or "").strip():
        return False
    return True


def _system_prompt() -> str:
    return (
        "Extract DocumentMetadata as JSON only. "
        "Keys: title, author, date, tags (array of strings), summary. "
        "Use empty string for unknown author/date. No markdown fences."
    )


def call_llama_cpp(text: str) -> dict[str, Any]:
    url = f"{llama_base_url()}/v1/chat/completions"
    model = str(worker_config().get("model_id") or "Qwen3-14B-Q4_K_M")
    payload = {
        "model": model,
        "temperature": 0.0,
        "messages": [
            {"role": "system", "content": _system_prompt()},
            {"role": "user", "content": text[:12000]},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {"name": "DocumentMetadata", "schema": DOCUMENT_METADATA_SCHEMA},
        },
    }
    resp = _http_json(url, payload)
    if not resp.get("ok"):
        # Older llama.cpp: retry without json_schema
        payload.pop("response_format", None)
        resp = _http_json(url, payload)
        if not resp.get("ok"):
            return {**resp, "backend": "llama.cpp"}
    data = resp.get("data") if isinstance(resp.get("data"), dict) else {}
    raw_text = _extract_message_text(data)
    parsed = _parse_metadata_json(raw_text)
    return {
        "ok": validate_metadata(parsed),
        "backend": "llama.cpp",
        "model_id": model,
        "raw": raw_text,
        "metadata": parsed,
        "error": None if validate_metadata(parsed) else "parse/validation failed",
    }


def call_ollama_json(text: str) -> dict[str, Any]:
    interactive = load_manifest().get("interactive") or {}
    modes = interactive.get("modes") if isinstance(interactive, dict) else {}
    fast = modes.get("fast") if isinstance(modes, dict) else {}
    model = str((fast or {}).get("model") or "qwen2.5:14b")
    url = f"{ollama_base_url()}/api/chat"
    payload = {
        "model": model,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.0},
        "messages": [
            {"role": "system", "content": _system_prompt()},
            {"role": "user", "content": text[:12000]},
        ],
    }
    resp = _http_json(url, payload, timeout=180.0)
    if not resp.get("ok"):
        return {**resp, "backend": "ollama"}
    data = resp.get("data") if isinstance(resp.get("data"), dict) else {}
    raw_text = _extract_message_text(data)
    parsed = _parse_metadata_json(raw_text)
    return {
        "ok": validate_metadata(parsed),
        "backend": "ollama",
        "model_id": model,
        "raw": raw_text,
        "metadata": parsed,
        "error": None if validate_metadata(parsed) else "parse/validation failed",
    }


def heuristic_metadata(text: str) -> dict[str, Any]:
    """Offline plumbing fallback when no LLM is reachable (Mechanic dry-run only)."""
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    title = ""
    author = ""
    date = ""
    tags: list[str] = []
    for ln in lines[:20]:
        low = ln.lower()
        if low.startswith("title:"):
            title = ln.split(":", 1)[1].strip()
        elif low.startswith("author:"):
            author = ln.split(":", 1)[1].strip()
        elif low.startswith("date:") or low.startswith("published:"):
            date = ln.split(":", 1)[1].strip()
        elif low.startswith("tags:"):
            tags = [p.strip() for p in ln.split(":", 1)[1].split(",") if p.strip()]
        elif ln.startswith("# ") and not title:
            title = ln[2:].strip()
    if not title and lines:
        title = lines[0][:120]
    summary = " ".join(lines[1:4])[:280] if len(lines) > 1 else title
    return {
        "title": title,
        "author": author,
        "date": date,
        "tags": tags,
        "summary": summary,
    }


def extract_text(
    text: str,
    *,
    prefer: str = "llama",
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
    acquire_gpu: bool = True,
) -> dict[str, Any]:
    cleaned = (text or "").strip()
    if not cleaned:
        return {"ok": False, "error": "text required"}

    lease_holder = "structured_extract"
    if acquire_gpu:
        leased = gpu_lease.acquire("extract", holder=lease_holder, note="structured_extract")
        if not leased.get("ok"):
            # Still allow CPU/Ollama attempt without exclusive GPU if denied — record and continue
            gpu_note = leased.get("error")
        else:
            gpu_note = None
    else:
        gpu_note = None

    result: dict[str, Any]
    try:
        if prefer == "ollama":
            result = call_ollama_json(cleaned)
            if not result.get("ok"):
                result = call_llama_cpp(cleaned)
        else:
            result = call_llama_cpp(cleaned)
            if not result.get("ok"):
                result = call_ollama_json(cleaned)
        if not result.get("ok"):
            meta = heuristic_metadata(cleaned)
            result = {
                "ok": validate_metadata(meta),
                "backend": "heuristic",
                "model_id": "heuristic.v1",
                "metadata": meta,
                "raw": json.dumps(meta),
                "error": "LLM backends unreachable; used heuristic fallback",
                "warning": result.get("error"),
            }
    finally:
        if acquire_gpu:
            gpu_lease.release(expected="extract")

    metadata = result.get("metadata") if isinstance(result.get("metadata"), dict) else None
    ok = validate_metadata(metadata)
    input_hash = sha256_text(cleaned)
    envelope = lineage_envelope(
        schema_id=SCHEMA_ID,
        tool="structured_extract",
        limb="structured_extract",
        model_id=str(result.get("model_id") or ""),
        input_hash=input_hash,
        validation_ok=ok,
        extra={
            "backend": result.get("backend"),
            "architect_note": note or "",
            "gpu_note": gpu_note or "",
        },
    )

    path_str = ""
    if write_files and metadata is not None:
        out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE
        stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
        stem = _safe_name(f"{metadata.get('title') or 'extract'}_{stamp}")
        path = out_dir / f"{stem}.md"
        fm = [
            "---",
            *provenance_fields(
                source="structured_extract",
                kind="document_metadata",
                tool="structured_extract",
                limb="structured_extract",
                extra={"schema_id": SCHEMA_ID, "backend": result.get("backend")},
            ),
            "---",
            f"# Extract: {metadata.get('title')}",
            "",
            "```json",
            json.dumps(metadata, indent=2),
            "```",
            lineage_markdown_block(envelope),
            provenance_markdown_footer(
                source="structured_extract",
                tool="structured_extract",
                limb="structured_extract",
            ),
        ]
        try:
            _atomic_write(path, "\n".join(fm))
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc)}

    return {
        "ok": ok,
        "schema_id": SCHEMA_ID,
        "backend": result.get("backend"),
        "model_id": result.get("model_id"),
        "metadata": metadata,
        "lineage": envelope,
        "path": path_str,
        "error": None if ok else (result.get("error") or "validation failed"),
        "note": (
            f"Scratch cache {path_str}. Promote to Cognee only via explicit cognee_remember."
            if path_str
            else "Extract completed without cache write."
        ),
    }


def extract_file(path: str | Path, **kwargs: Any) -> dict[str, Any]:
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc), "path": str(p)}
    out = extract_text(text, **kwargs)
    out["source_path"] = str(p)
    return out


def _field_overlap(expected: dict[str, Any], got: dict[str, Any] | None) -> float:
    if not got:
        return 0.0
    score = 0.0
    total = 4.0
    if str(expected.get("title") or "").lower() in str(got.get("title") or "").lower() or str(
        got.get("title") or ""
    ).lower() in str(expected.get("title") or "").lower():
        score += 1.0
    if str(expected.get("author") or "").lower() == str(got.get("author") or "").lower() or not expected.get(
        "author"
    ):
        score += 1.0
    exp_tags = {str(t).lower() for t in (expected.get("tags") or [])}
    got_tags = {str(t).lower() for t in (got.get("tags") or [])}
    if not exp_tags or exp_tags & got_tags:
        score += 1.0
    if str(got.get("summary") or "").strip():
        score += 1.0
    return score / total


def run_eval(*, prefer: str = "auto") -> dict[str, Any]:
    fixtures = sorted(FIXTURE_DIR.glob("*.txt")) if FIXTURE_DIR.is_dir() else []
    rows: list[dict[str, Any]] = []
    for fx in fixtures:
        expected_path = EXPECTED_DIR / f"{fx.stem}.json"
        try:
            expected = json.loads(expected_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            expected = {}
        text = fx.read_text(encoding="utf-8")
        if prefer == "ollama":
            backends = ["ollama"]
        elif prefer == "llama":
            backends = ["llama"]
        else:
            backends = ["llama", "ollama"]

        for backend in backends:
            if backend == "llama":
                one = extract_text(text, prefer="llama", write_files=False, acquire_gpu=True)
            else:
                one = extract_text(text, prefer="ollama", write_files=False, acquire_gpu=False)
            overlap = _field_overlap(expected if isinstance(expected, dict) else {}, one.get("metadata"))
            rows.append(
                {
                    "fixture": fx.name,
                    "backend": one.get("backend"),
                    "ok": one.get("ok"),
                    "overlap": round(overlap, 3),
                    "error": one.get("error"),
                }
            )

    ACCEPTANCE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    out_path = ACCEPTANCE_DIR / f"structured_extract_{stamp}.yaml"
    parse_ok = sum(1 for r in rows if r.get("ok"))
    lines = [
        "candidate: structured_extract",
        f"status: pending_architect",
        f"evaluated_at: \"{utc_now_iso()}\"",
        f"fixture_count: {len(fixtures)}",
        f"row_count: {len(rows)}",
        f"parse_ok_count: {parse_ok}",
        "memory_promoted: false",
        "provenance_recorded: true",
        "acceptance_reason: null",
        "rejection_reason: null",
        "notes: \"Mechanic headless eval. Architect must run Smoke B.\"",
        "results:",
    ]
    for r in rows:
        lines.append(f"  - fixture: {r['fixture']}")
        lines.append(f"    backend: {r.get('backend')}")
        lines.append(f"    ok: {str(bool(r.get('ok'))).lower()}")
        lines.append(f"    overlap: {r.get('overlap')}")
        if r.get("error"):
            lines.append(f"    error: \"{str(r.get('error')).replace(chr(34), '')[:200]}\"")
    try:
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc), "rows": rows}

    return {
        "ok": True,
        "fixtures": len(fixtures),
        "parse_ok_count": parse_ok,
        "rows": rows,
        "acceptance_path": str(out_path),
        "note": "Acceptance written pending_architect. No Cognee writes.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE structured DocumentMetadata extract")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_text = sub.add_parser("text", help="Extract from raw text")
    p_text.add_argument("text")
    p_text.add_argument("--prefer", choices=["llama", "ollama"], default="llama")
    p_text.add_argument("--no-write", action="store_true")
    p_text.add_argument("--note", default="")

    p_file = sub.add_parser("file", help="Extract from a UTF-8 text file")
    p_file.add_argument("path")
    p_file.add_argument("--prefer", choices=["llama", "ollama"], default="llama")
    p_file.add_argument("--no-write", action="store_true")
    p_file.add_argument("--note", default="")

    p_eval = sub.add_parser("eval", help="Golden fixture headless eval")
    p_eval.add_argument("--prefer", choices=["auto", "llama", "ollama"], default="auto")

    args = parser.parse_args(argv)
    if args.cmd == "text":
        result = extract_text(
            args.text,
            prefer=args.prefer,
            write_files=not args.no_write,
            note=args.note,
        )
    elif args.cmd == "file":
        result = extract_file(
            args.path,
            prefer=args.prefer,
            write_files=not args.no_write,
            note=args.note,
        )
    elif args.cmd == "eval":
        result = run_eval(prefer=args.prefer)
    else:
        raise SystemExit(f"unknown command: {args.cmd}")

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
