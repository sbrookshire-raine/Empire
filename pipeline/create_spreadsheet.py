"""Create spreadsheet — openpyxl writer producing .xlsx into eve-output only.

Artifact arm (writable to eve-output, never elsewhere). Blocks formula
injection (cells starting with =, +, -, @, tab, CR) and external links by
escaping them as inert text. Pure Python, offline-convertible.

Trust domain: artifact (network DENY; no shell; no memory).
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

from pipeline.provenance import provenance_markdown_footer

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = Path(
    os.environ.get("EMPIRE_EVE_OUTPUT_DIR", r"C:\EMPIRE\eve-output")
)
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

# Cells that could be interpreted as formulas / commands when opened in Excel.
_FORMULA_PREFIXES: tuple[str, ...] = ("=", "+", "-", "@", "\t", "\r")


def output_dir() -> Path:
    override = os.environ.get("EMPIRE_EVE_OUTPUT_DIR", "").strip()
    if override:
        return Path(override)
    return DEFAULT_OUTPUT_DIR


def _safe_stem(name: str) -> str:
    cleaned = _SAFE.sub("_", (name or "").strip()).strip("_")
    return (cleaned or "spreadsheet")[:120]


def _neutralize(value: Any) -> Any:
    """Escape values that Excel would treat as formulas (injection guard)."""
    if isinstance(value, str):
        if value[:1] in _FORMULA_PREFIXES:
            return "'" + value
        return value
    if value is None:
        return ""
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value
    return str(value)


def create_spreadsheet(
    *,
    filename: str,
    headers: list[str],
    rows: list[list[Any]],
    sheet_name: str = "Sheet1",
    note: str = "",
) -> dict[str, Any]:
    name = _safe_stem(filename)
    if not name.lower().endswith(".xlsx"):
        name += ".xlsx"
    if not headers or not isinstance(headers, list):
        return {"ok": False, "error": "headers (non-empty list) are required"}
    if not isinstance(rows, list):
        return {"ok": False, "error": "rows must be a list of lists"}

    try:
        from openpyxl import Workbook
    except ImportError:
        return {"ok": False, "error": "openpyxl not installed"}

    out_dir = output_dir()
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    # Enforce max dimensions to bound memory.
    max_cols = len(headers)
    if max_cols > 200:
        return {"ok": False, "error": f"too many columns ({max_cols} > 200)"}
    if len(rows) > 20_000:
        return {"ok": False, "error": "too many rows (> 20000)"}

    wb = Workbook()
    ws = wb.active
    ws.title = (sheet_name or "Sheet1")[:31]
    ws.append([_neutralize(h) for h in headers])
    for row in rows:
        if not isinstance(row, (list, tuple)):
            return {"ok": False, "error": "each row must be a list"}
        # Pad/truncate to header width.
        cells = [_neutralize(c) for c in row[:max_cols]]
        cells += [""] * (max_cols - len(cells))
        ws.append(cells)

    out_path = out_dir / name
    try:
        wb.save(str(out_path))
    except OSError as exc:
        return {"ok": False, "error": str(exc), "path": str(out_path)}

    size = out_path.stat().st_size
    return {
        "ok": True,
        "path": str(out_path),
        "filename": name,
        "rows_written": len(rows),
        "columns": max_cols,
        "size_bytes": size,
        "sheet": ws.title,
        "footer": provenance_markdown_footer(source="create_spreadsheet", tool="create_spreadsheet", limb="artifact"),
        "note": (note or "").strip(),
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Write an .xlsx to eve-output (openpyxl)")
    parser.add_argument("--filename", required=True)
    parser.add_argument("--sheet", default="Sheet1")
    parser.add_argument("--headers-json", required=True, help='JSON array, e.g. \'["a","b"]\'')
    parser.add_argument("--rows-json", required=True, help='JSON array of arrays')
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)

    try:
        headers = json.loads(args.headers_json)
        rows = json.loads(args.rows_json)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"bad JSON: {exc}"}))
        return 1

    result = create_spreadsheet(
        filename=args.filename,
        headers=headers,
        rows=rows,
        sheet_name=args.sheet,
        note=args.note,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
