"""FastMCP server exposing read-only access to harvested Active Tools."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ACTIVE_TOOLS_DIR = Path(r"C:\Empire_Workbench\03_Active_Tools")
MAX_READ_BYTES = 512 * 1024

mcp = FastMCP("empire-workbench")


def _active_tools_root() -> Path:
    override = os.environ.get("EMPIRE_ACTIVE_TOOLS_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return DEFAULT_ACTIVE_TOOLS_DIR.resolve()


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


def _resolve_active_tool_path(filename: str) -> tuple[Path | None, str | None]:
    """Resolve a filename under 03_Active_Tools; return (path, error)."""

    cleaned = filename.strip().replace("\\", "/")
    if not cleaned:
        return None, "filename is required."
    if cleaned.startswith("/") or re.match(r"^[A-Za-z]:", cleaned):
        return None, "filename must be relative to 03_Active_Tools (basename or subpath only)."
    parts = Path(cleaned).parts
    if ".." in parts:
        return None, "path traversal is not allowed."

    root = _active_tools_root()
    candidate = (root / Path(*parts)).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None, "filename must stay under 03_Active_Tools."

    return candidate, None


@mcp.tool()
async def read_active_tool(filename: str) -> str:
    """Read a flattened codebase file from Empire Workbench 03_Active_Tools (read-only)."""

    target, resolve_error = _resolve_active_tool_path(filename)
    if resolve_error or target is None:
        return _json({"ok": False, "error": resolve_error, "filename": filename})

    root = _active_tools_root()
    if not root.is_dir():
        return _json(
            {
                "ok": False,
                "error": f"Active tools directory not found: {root}",
                "filename": filename,
            }
        )

    try:
        if not target.exists():
            return _json(
                {
                    "ok": False,
                    "error": f"File not found: {target.name}",
                    "filename": filename,
                    "path": str(target),
                }
            )
        if not target.is_file():
            return _json(
                {
                    "ok": False,
                    "error": "Path is not a file.",
                    "filename": filename,
                    "path": str(target),
                }
            )

        size_bytes = target.stat().st_size
        truncated = size_bytes > MAX_READ_BYTES
        read_size = min(size_bytes, MAX_READ_BYTES)
        with target.open("r", encoding="utf-8", errors="replace") as handle:
            content = handle.read(read_size)

        return _json(
            {
                "ok": True,
                "filename": filename,
                "path": str(target),
                "root": str(root),
                "sizeBytes": size_bytes,
                "truncated": truncated,
                "maxBytes": MAX_READ_BYTES,
                "content": content,
            }
        )
    except OSError as exc:
        return _json(
            {
                "ok": False,
                "error": f"Could not read file: {exc}",
                "filename": filename,
                "path": str(target),
            }
        )


if __name__ == "__main__":
    mcp.run()
