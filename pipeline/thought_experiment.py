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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capture EMPIRE thought experiment notes")
    parser.add_argument("topic")
    parser.add_argument("--url", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--out-dir", default=str(DEFAULT_DIR))
    args = parser.parse_args(argv)
    result = capture(
        args.topic,
        source_url=args.url,
        notes=args.notes,
        out_dir=Path(args.out_dir),
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
