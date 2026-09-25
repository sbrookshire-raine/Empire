"""Research desk — the deferred tool contract: start, leave, come back, read.

Why this exists (2026-09-24)
----------------------------
Her context window is ~16k tokens (now 24,576 — E-41), which is roughly **one long article**. A
research pass never fits in that, and holding her turn open while a fetch runs is what produced the
300-second turns. So the work goes to a **desk**: a job is created and returns immediately, a worker
does the fetching on CPU with her turn closed, and she later reads a **bounded digest** from the desk.

The shape is native to the tool surface already — `stem_run`/`stem_status`,
`loom_process_shell`/`loom_status`, `thought_experiment_capture`/`thought_experiment_read`, and
`ingestion_jobs` deferring deep reasoning "to runtime". This is that same contract for reading the web.

Desk layout
-----------
    <desk>/<job_id>/meta.json     job record: query, urls, status, sources, timestamps, expiry
    <desk>/<job_id>/source.md     the fetched pages, concatenated with provenance
    <desk>/<job_id>/digest.md     the bounded digest `research_read` returns
    <desk>/<job_id>/web_cache/    where `web_scout` caches each page

Statuses: `queued` -> `running` -> `done` | `partial` | `failed`, plus `needs_sources` when there is
no URL to fetch and no search limb yet (E-35 is that missing capability; E-34 measures the hole).

    python -m pipeline.research_desk start "what changed in yt-dlp" --url https://example.org/notes
    python -m pipeline.research_desk status 20260924-153012-ab12cd
    python -m pipeline.research_desk read 20260924-153012-ab12cd --budget 1200
    python -m pipeline.research_desk open
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
WORKBENCH = Path(os.environ.get("EMPIRE_WORKBENCH_ROOT", r"C:\Empire_Workbench"))
DEFAULT_DESK = WORKBENCH / "04_Thought_Experiments" / "research"
MAX_DIGEST_CHARS = 2_400
MAX_SOURCE_CHARS = 20_000
MAX_PER_SOURCE_CHARS = 3_000
TTL_DAYS = 14
ACTIVE = ("queued", "running", "partial", "needs_sources", "failed")
JOB_ID_RE = re.compile(r"^[0-9]{8}-[0-9]{6}-[0-9a-f]{6}$")


def desk_root() -> Path:
    """Where jobs live (overridable so tests never touch the real desk)."""

    override = os.environ.get("EMPIRE_RESEARCH_DESK", "").strip()
    return Path(override) if override else DEFAULT_DESK


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _clean_id(value: str) -> str:
    """A job id is a name, never a path — the same rule the registry and playbook use."""

    cleaned = str(value or "").strip()
    return cleaned if JOB_ID_RE.match(cleaned) else ""


def _job_dir(job_id: str) -> Path | None:
    cleaned = _clean_id(job_id)
    return desk_root() / cleaned if cleaned else None


def _read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")


def _age_seconds(meta: dict[str, Any]) -> int:
    try:
        created = time.mktime(time.strptime(str(meta.get("created")), "%Y-%m-%dT%H:%M:%SZ"))
    except (ValueError, TypeError):
        return 0
    return max(0, int(time.time() - created))


def start(query: str, urls: list[str] | None = None, *, spawn: bool = True) -> dict[str, Any]:
    """Create a job and return immediately — the turn ends here, the work does not."""

    cleaned = str(query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "a query is required"}
    links = [str(url).strip() for url in (urls or []) if str(url).strip()]
    job_id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
    directory = desk_root() / job_id
    directory.mkdir(parents=True, exist_ok=True)
    meta = {
        "job_id": job_id,
        "query": cleaned,
        "urls": links,
        "status": "queued",
        "created": _now(),
        "updated": _now(),
        "sources": [],
        "digest_chars": 0,
        "note": "",
    }
    _write_json(directory / "meta.json", meta)
    if spawn:
        meta["worker_started"] = _spawn_worker(job_id)
        _write_json(directory / "meta.json", meta)
    return {
        "ok": True,
        "job_id": job_id,
        "desk_path": str(directory),
        "status": meta["status"],
        "urls": links,
        "next": "come back with research_status(job_id), then research_read(job_id)",
    }


def status(job_id: str) -> dict[str, Any]:
    """Where the job is now — cheap enough to check every turn."""

    directory = _job_dir(job_id)
    if directory is None:
        return {"ok": False, "error": "invalid job id"}
    meta = _read_json(directory / "meta.json")
    if not meta:
        return {"ok": False, "error": f"no job {job_id!r} on the desk"}
    digest = directory / "digest.md"
    return {
        "ok": True,
        "job_id": meta.get("job_id") or job_id,
        "query": meta.get("query", ""),
        "status": meta.get("status", ""),
        "sources": meta.get("sources", []),
        "age_seconds": _age_seconds(meta),
        "created": meta.get("created"),
        "updated": meta.get("updated"),
        "note": meta.get("note", ""),
        "has_digest": digest.is_file(),
        "desk_path": str(directory),
    }


def read(job_id: str, *, budget: int = MAX_DIGEST_CHARS) -> dict[str, Any]:
    """The bounded digest — her window spends tokens on this, not on the corpus."""

    directory = _job_dir(job_id)
    if directory is None:
        return {"ok": False, "error": "invalid job id"}
    meta = _read_json(directory / "meta.json")
    if not meta:
        return {"ok": False, "error": f"no job {job_id!r} on the desk"}
    digest_path = directory / "digest.md"
    if not digest_path.is_file():
        return {
            "ok": False,
            "job_id": job_id,
            "status": meta.get("status", ""),
            "error": f"no digest yet (status={meta.get('status')})",
            "note": meta.get("note", ""),
        }
    text = digest_path.read_text(encoding="utf-8")
    cap = max(400, int(budget or MAX_DIGEST_CHARS))
    truncated = len(text) > cap
    return {
        "ok": True,
        "job_id": job_id,
        "query": meta.get("query", ""),
        "status": meta.get("status", ""),
        "sources": meta.get("sources", []),
        "digest": text[:cap]
        + ("\n\n[digest truncated — ask again with a larger budget]" if truncated else ""),
        "chars": len(text),
        "more_available": truncated,
        "source_path": str(directory / "source.md"),
        "desk_path": str(directory),
    }


def open_jobs() -> list[dict[str, Any]]:
    """Everything still waiting for attention — the reason she can come back at all."""

    root = desk_root()
    if not root.is_dir():
        return []
    jobs: list[dict[str, Any]] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        meta = _read_json(child / "meta.json")
        if not meta or str(meta.get("status")) not in ACTIVE:
            continue
        jobs.append(
            {
                "job_id": meta.get("job_id") or child.name,
                "query": meta.get("query", ""),
                "status": meta.get("status", ""),
                "age_seconds": _age_seconds(meta),
                "sources": len(meta.get("sources") or []),
            }
        )
    return sorted(jobs, key=lambda job: job["age_seconds"])


def expire(*, days: int = TTL_DAYS, apply: bool = False) -> dict[str, Any]:
    """Retire old desks; dry run unless asked (mirrors `prune-workflow-data.ps1`)."""

    root = desk_root()
    if not root.is_dir():
        return {"ok": True, "expired": [], "applied": False, "root": str(root)}
    cutoff = max(1, int(days)) * 86_400
    doomed = [
        child.name
        for child in sorted(root.iterdir())
        if child.is_dir() and _age_seconds(_read_json(child / "meta.json")) > cutoff
    ]
    if apply:
        for name in doomed:
            shutil.rmtree(root / name, ignore_errors=True)
    return {"ok": True, "expired": doomed, "applied": bool(apply), "root": str(root)}


def _default_fetcher(url: str, cache_dir: Path, note: str) -> dict[str, Any]:
    """The real fetch: `web_scout` caches markdown per page (CPU + network, never the model)."""

    from pipeline import web_scout

    return web_scout.scout(url, cache_dir=cache_dir, write_files=True, note=note)


def _source_text(result: dict[str, Any], path_hint: Path) -> str:
    """`web_scout` returns the body under a few names depending on the extractor; be tolerant."""

    for key in ("body", "text", "markdown", "content"):
        value = result.get(key)
        if isinstance(value, str) and value.strip():
            return value
    written = str(result.get("path") or "")
    candidate = Path(written) if written else path_hint
    try:
        return candidate.read_text(encoding="utf-8")
    except OSError:
        return ""


def collect(
    job_id: str,
    *,
    fetcher: Callable[[str, Path, str], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """The worker: fetch each URL, write the desk, leave a bounded digest. No model involved."""

    directory = _job_dir(job_id)
    if directory is None:
        return {"ok": False, "error": "invalid job id"}
    meta = _read_json(directory / "meta.json")
    if not meta:
        return {"ok": False, "error": f"no job {job_id!r} on the desk"}

    fetch = fetcher or _default_fetcher
    meta["status"] = "running"
    meta["updated"] = _now()
    _write_json(directory / "meta.json", meta)

    links = [str(url) for url in (meta.get("urls") or [])]
    if not links:
        # Honest: with no URL and no search limb there is nothing to fetch. E-35 is that capability.
        meta["status"] = "needs_sources"
        meta["note"] = (
            "no URL given, and no web-search tool exists yet (E-34 measures the hole, E-35 builds "
            "it) — ask the Architect for a URL, or read a local document instead"
        )
        meta["updated"] = _now()
        _write_json(directory / "meta.json", meta)
        return {"ok": True, "job_id": job_id, "status": "needs_sources", "sources": []}

    cache_dir = directory / "web_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    sources: list[dict[str, Any]] = []
    failed: list[str] = []
    for url in links:
        try:
            result = fetch(url, cache_dir, str(meta.get("query") or ""))
        except Exception as exc:  # noqa: BLE001 - one bad page must not lose the whole desk
            failed.append(f"{url}: {exc}")
            continue
        if not result.get("ok"):
            failed.append(f"{url}: {result.get('error') or 'fetch failed'}")
            continue
        text = _source_text(result, cache_dir / "page.md")
        sources.append(
            {
                "url": str(result.get("final_url") or url),
                "title": str(result.get("title") or url),
                "chars": len(text),
                "path": str(result.get("path") or ""),
            }
        )

    if sources:
        blocks = [
            f"## {entry['title']}\n{entry['url']}\n\n{_written(entry).strip()}\n" for entry in sources
        ]
        (directory / "source.md").write_text(
            "\n\n---\n\n".join(blocks)[:MAX_SOURCE_CHARS], encoding="utf-8"
        )
        digest_lines = [f"# {meta.get('query')}", ""]
        for entry in sources:
            digest_lines += [
                f"## {entry['title']}",
                entry["url"],
                "",
                _written(entry)[:MAX_PER_SOURCE_CHARS].strip(),
                "",
            ]
        digest = "\n".join(digest_lines).strip() + "\n"
        (directory / "digest.md").write_text(digest, encoding="utf-8")
        meta["digest_chars"] = len(digest)

    meta["sources"] = sources
    meta["status"] = "done" if sources and not failed else ("partial" if sources else "failed")
    meta["note"] = "; ".join(failed)[:600]
    meta["updated"] = _now()
    _write_json(directory / "meta.json", meta)
    return {
        "ok": True,
        "job_id": job_id,
        "status": meta["status"],
        "sources": sources,
        "failed": failed,
    }


def _written(entry: dict[str, Any]) -> str:
    """The fetched page as cached by `web_scout`, or empty when it was not kept on disk."""

    written = str(entry.get("path") or "")
    if not written:
        return ""
    try:
        return Path(written).read_text(encoding="utf-8")
    except OSError:
        return ""


def _spawn_worker(job_id: str) -> bool:
    """Start the worker detached, so the turn can end while it works."""

    flags = 0
    if os.name == "nt":
        flags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    try:
        subprocess.Popen(
            [sys.executable, "-m", "pipeline.research_desk", "--worker", job_id],
            cwd=str(ROOT),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags,
            close_fds=True,
        )
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Research desk: deferred start -> status -> read")
    parser.add_argument(
        "action", nargs="?", default="open", choices=("start", "status", "read", "open", "expire")
    )
    parser.add_argument("value", nargs="?", default="", help="query (start) or job id (status/read)")
    parser.add_argument("--url", action="append", default=[], help="URL to fetch (repeatable)")
    parser.add_argument("--budget", type=int, default=MAX_DIGEST_CHARS)
    parser.add_argument("--days", type=int, default=TTL_DAYS)
    parser.add_argument("--apply", action="store_true", help="expire: actually delete")
    parser.add_argument("--no-spawn", action="store_true", help="start: do not launch the worker")
    parser.add_argument("--worker", default="", help="internal: run one job now")
    args = parser.parse_args(argv)

    if args.worker:
        payload = collect(args.worker)
    elif args.action == "start":
        payload = start(args.value, args.url, spawn=not args.no_spawn)
    elif args.action == "status":
        payload = status(args.value)
    elif args.action == "read":
        payload = read(args.value, budget=args.budget)
    elif args.action == "expire":
        payload = expire(days=args.days, apply=args.apply)
    else:
        payload = {"ok": True, "open": open_jobs()}
    print(json.dumps(payload, indent=2, default=str))
    return 0 if payload.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())



