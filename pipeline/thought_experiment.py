"""Thought-experiment notes under 04_Thought_Experiments (Manifesto Phase 3)."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_DIR = Path(
    os.environ.get(
        "EMPIRE_THOUGHT_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments",
    )
)
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")


def _safe_name(value: str, fallback: str = "experiment") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:80]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="te-", suffix=".md", dir=str(path.parent))
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


def capture(
    topic: str,
    *,
    source_url: str = "",
    notes: str = "",
    out_dir: Path | None = None,
) -> dict[str, Any]:
    cleaned_topic = (topic or "").strip()
    if not cleaned_topic:
        return {"ok": False, "error": "topic required"}

    url = (source_url or "").strip()
    if url:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https", ""}:
            return {"ok": False, "error": "source_url must be http(s) if set"}

    dest = Path(out_dir) if out_dir else DEFAULT_DIR
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    stem = _safe_name(f"TE_{cleaned_topic}_{stamp}")
    path = dest / f"{stem}.md"

    # Optional: pull a short web scout summary into the note when URL given
    scout_block = ""
    if url:
        try:
            from pipeline.web_scout import fetch_url

            fetched = fetch_url(url)
            if fetched.get("ok"):
                snippet = str(fetched.get("text") or "")[:2000]
                scout_block = f"## Source extract\n\n{snippet}\n"
        except Exception as exc:  # noqa: BLE001
            scout_block = f"## Source extract\n\n_Fetch failed: {exc}_\n"

    fm = [
        "---",
        *provenance_fields(
            source="thought_experiment",
            kind="thought_experiment",
            tool="thought_experiment_capture",
            limb="thought_experiments",
            extra={"topic": cleaned_topic, "source_url": url},
        ),
        "---",
    ]
    body = "\n".join(
        [
            *fm,
            f"# Thought experiment: {cleaned_topic}",
            "",
            f"Captured: {utc_now_iso()}",
            f"Source: {url or '_none_'}",
            "",
            "## Architect notes",
            "",
            notes.strip() or "_None yet._",
            "",
            scout_block,
            "## Follow-ups",
            "",
            "- Discuss with Eve later",
            "- Promote useful conclusions to Cognee only after triage",
            "",
            provenance_markdown_footer(
                source="thought_experiment",
                tool="thought_experiment_capture",
                limb="thought_experiments",
            ),
        ]
    )
    try:
        _atomic_write(path, body)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    return {
        "ok": True,
        "path": str(path),
        "topic": cleaned_topic,
        "source_url": url,
        "note": "Saved under 04_Thought_Experiments. Not Cognee memory until promoted.",
    }


def list_experiments(*, limit: int = 20, out_dir: Path | None = None) -> dict[str, Any]:
    """Newest first. Capture was write-only, so a past experiment could not feed a new one."""

    dest = Path(out_dir) if out_dir else DEFAULT_DIR
    if not dest.is_dir():
        return {"ok": False, "error": f"thought-experiment dir missing: {dest}", "dir": str(dest)}
    files = [path for path in dest.glob("TE_*.md") if path.is_file()]
    files.sort(key=lambda path: path.stat().st_mtime, reverse=True)
    entries = []
    for path in files[: max(1, limit)]:
        topic = path.stem
        try:
            head = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            head = ""
        for line in head.splitlines():
            if line.startswith("# Thought experiment: "):
                topic = line.removeprefix("# Thought experiment: ").strip()
                break
        entries.append(
            {
                "name": path.stem,
                "topic": topic,
                "path": str(path),
                "modified": round(path.stat().st_mtime, 1),
                "chars": len(head),
            }
        )
    return {"ok": True, "dir": str(dest), "count": len(files), "experiments": entries}


def read_experiment(
    name_or_path: str,
    *,
    out_dir: Path | None = None,
    max_chars: int = 6000,
) -> dict[str, Any]:
    """Read one note. The path is resolved strictly inside `out_dir` — no traversal."""

    raw = (name_or_path or "").strip()
    if not raw:
        return {"ok": False, "error": "name required"}
    dest = (Path(out_dir) if out_dir else DEFAULT_DIR).resolve()
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = dest / (raw if raw.endswith(".md") else f"{raw}.md")
    try:
        resolved = candidate.resolve()
        resolved.relative_to(dest)
    except (OSError, ValueError):
        return {"ok": False, "error": "note must be inside 04_Thought_Experiments"}
    if not resolved.is_file():
        return {"ok": False, "error": f"no such note: {raw}"}
    try:
        text = resolved.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {
        "ok": True,
        "name": resolved.stem,
        "path": str(resolved),
        "truncated": len(text) > max_chars,
        "text": text[:max_chars],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capture or read EMPIRE thought experiment notes")
    parser.add_argument("topic", nargs="?", default="")
    parser.add_argument("--url", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--out-dir", default=str(DEFAULT_DIR))
    parser.add_argument("--list", action="store_true", help="list saved notes, newest first")
    parser.add_argument("--read", default="", help="read one saved note by name or path")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args(argv)

    dest = Path(args.out_dir)
    if args.list:
        result = list_experiments(limit=max(1, min(args.limit, 50)), out_dir=dest)
    elif args.read:
        result = read_experiment(args.read, out_dir=dest)
    elif args.topic:
        result = capture(
            args.topic,
            source_url=args.url,
            notes=args.notes,
            out_dir=dest,
        )
    else:
        result = {"ok": False, "error": "pass a topic, or --list, or --read NAME"}
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
