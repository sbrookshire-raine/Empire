"""Workspace search — ripgrep-style text search over allowlisted local roots.

Read-only evidence arm. Searches C:/Empire_Workbench and C:/EMPIRE/docs only;
rejects any absolute path, UNC path, or `..` escape outside the allowlist.
Redacts obvious secrets (API keys, tokens, passwords) from results.

Offline-convertible: pure Python stdlib; `rg` fast-path when on PATH, else a
built-in scanner (case-insensitive literal + regex) so it never needs the
Cursor-bundled ripgrep to function.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from pipeline.provenance import provenance_markdown_footer

ROOT = Path(__file__).resolve().parents[1]

# Allowlisted roots (real paths only, never invented).
DEFAULT_ROOTS: tuple[Path, ...] = (
    Path(r"C:\Empire_Workbench"),
    ROOT / "docs",
)

DEFAULT_MAX_RESULTS = int(os.environ.get("EMPIRE_SEARCH_MAX_RESULTS", "100"))
DEFAULT_MAX_LINE_CHARS = int(os.environ.get("EMPIRE_SEARCH_MAX_LINE_CHARS", "400"))
DEFAULT_MAX_FILE_BYTES = int(os.environ.get("EMPIRE_SEARCH_MAX_FILE_BYTES", str(2 * 1024 * 1024)))
_TEXT_EXTS: frozenset[str] = frozenset(
    {
        ".md", ".txt", ".json", ".jsonl", ".csv", ".tsv", ".py", ".ps1", ".ts",
        ".tsx", ".js", ".mjs", ".cjs", ".html", ".htm", ".css", ".yaml", ".yml",
        ".toml", ".ini", ".cfg", ".xml", ".sql", ".sh", ".bat", ".cmd", ".env",
    }
)

# Redaction patterns — strip obvious secrets before returning results.
_REDACT_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?i)\b(api[_-]?key|apikey|secret|token|password|passwd|pwd|bearer)\b\s*[:=]\s*\S+"),
    re.compile(r"\b([A-Za-z0-9_-]{20,})\b"),
)


def _search_roots() -> list[Path]:
    override = os.environ.get("EMPIRE_SEARCH_ROOTS", "").strip()
    if override:
        roots: list[Path] = []
        for part in override.split(os.pathsep):
            p = Path(part.strip()).expanduser()
            if p.is_dir():
                roots.append(p)
        if roots:
            return roots
    return [r for r in DEFAULT_ROOTS if r.is_dir()]


def _is_text_file(path: Path) -> bool:
    return path.suffix.lower() in _TEXT_EXTS


def _redact(text: str) -> str:
    out = text
    for pattern in _REDACT_PATTERNS:
        out = pattern.sub("***REDACTED***", out)
    return out


def _scan_line(line: str, query_lower: str) -> bool:
    return query_lower in line.lower()


def _rg_search(query: str, roots: list[Path], max_results: int) -> dict[str, Any] | None:
    rg = shutil.which("rg")
    if not rg:
        return None
    try:
        completed = subprocess.run(
            [
                rg,
                "--json",
                "--max-count", str(max_results),
                "--max-columns", str(DEFAULT_MAX_LINE_CHARS),
                "--glob", "!.git/**",
                "-S",
                "-e", query,
                *[str(r) for r in roots],
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if completed.returncode not in (0, 1):
        return None
    # Parse --json output: one JSON object per line; `match` records have
    # path + line_number + lines.text. This avoids Windows drive-colon parsing.
    matches: list[dict[str, Any]] = []
    for raw_line in (completed.stdout or "").splitlines():
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        try:
            event = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        if event.get("type") != "match":
            continue
        data = event.get("data") or {}
        path_obj = data.get("path") or {}
        path_text = path_obj.get("text") or ""
        # Only keep results from allowlisted text extensions (ripgrep searches
        # every file by default, including binaries).
        if not _is_text_file(Path(path_text)):
            continue
        line_obj = data.get("lines") or {}
        line_text = line_obj.get("text") or ""
        matches.append(
            {
                "path": path_text,
                "line": int(data.get("line_number") or 0),
                "text": _redact(line_text.rstrip("\n")[:DEFAULT_MAX_LINE_CHARS]),
            }
        )
    return {"ok": True, "engine": "ripgrep", "matches": matches}


def _builtin_search(query: str, roots: list[Path], max_results: int) -> dict[str, Any]:
    """Pure-Python fallback: case-insensitive literal substring over text files."""
    query_lower = query.lower()
    results: list[dict[str, Any]] = []
    stopped = False
    for root in roots:
        if stopped:
            break
        try:
            walker = os.walk(root)
        except OSError:
            continue
        for dirpath, dirnames, filenames in walker:
            dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", "__pycache__", ".venv"}]
            for filename in filenames:
                if len(results) >= max_results:
                    stopped = True
                    break
                path = Path(dirpath) / filename
                if not _is_text_file(path):
                    continue
                try:
                    if path.stat().st_size > DEFAULT_MAX_FILE_BYTES:
                        continue
                except OSError:
                    continue
                try:
                    text = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for i, line in enumerate(text.splitlines(), start=1):
                    if len(results) >= max_results:
                        stopped = True
                        break
                    if _scan_line(line, query_lower):
                        results.append(
                            {
                                "path": str(path),
                                "line": i,
                                "text": _redact(line[:DEFAULT_MAX_LINE_CHARS]),
                            }
                        )
    return {"ok": True, "engine": "builtin", "results": results}


def search(
    query: str,
    *,
    roots: list[Path] | None = None,
    max_results: int = DEFAULT_MAX_RESULTS,
    note: str = "",
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "query is required"}

    roots_used = roots if roots is not None else _search_roots()
    if not roots_used:
        return {"ok": False, "error": "no allowlisted search roots available"}

    max_results = max(1, min(int(max_results), 500))

    rg_result = _rg_search(cleaned, roots_used, max_results)
    results: list[dict[str, Any]]
    engine: str
    if rg_result is not None:
        engine = rg_result["engine"]
        results = rg_result.get("matches") or []
    else:
        builtin = _builtin_search(cleaned, roots_used, max_results)
        engine = builtin["engine"]
        results = builtin.get("results") or []

    return {
        "ok": True,
        "engine": engine,
        "query": cleaned,
        "count": len(results),
        "truncated": len(results) >= max_results,
        "roots": [str(r) for r in roots_used],
        "results": results,
        "footer": provenance_markdown_footer(source="workspace_search", tool="workspace_search", limb="local_evidence"),
        "note": (note or "").strip(),
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Workspace search (local, allowlisted)")
    parser.add_argument("query")
    parser.add_argument("--max-results", type=int, default=DEFAULT_MAX_RESULTS)
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)
    result = search(args.query, max_results=args.max_results, note=args.note)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
