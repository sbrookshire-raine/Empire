"""FastMCP server for Empire Workbench Active Tools and health diagnostics."""

from __future__ import annotations

import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKBENCH_DIR = Path(r"C:\Empire_Workbench")
DEFAULT_ACTIVE_TOOLS_DIR = DEFAULT_WORKBENCH_DIR / "03_Active_Tools"
MAX_READ_BYTES = 512 * 1024
LOW_FREE_SPACE_GB = 5.0

WORKBENCH_FOLDERS = (
    "00_Resource_Queue",
    "01_Memory_Bank",
    "02_Skills_and_Prompts",
    "03_Active_Tools",
    "04_Thought_Experiments",
    "05_Work_Orders",
)

mcp = FastMCP("empire-workbench")


def _workbench_root() -> Path:
    override = os.environ.get("EMPIRE_WORKBENCH_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return DEFAULT_WORKBENCH_DIR.resolve()


def _active_tools_root() -> Path:
    override = os.environ.get("EMPIRE_ACTIVE_TOOLS_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return (_workbench_root() / "03_Active_Tools").resolve()


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


def _count_entries(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    try:
        return sum(1 for entry in directory.iterdir() if not entry.name.startswith("."))
    except OSError:
        return 0


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
async def check_workbench_health() -> str:
    """Check EMPIRE Workbench path, disk free space, and folder entry counts."""

    workbench_path = _workbench_root()
    try:
        if not workbench_path.exists():
            return _json(
                {
                    "ok": False,
                    "status": "error",
                    "message": "Workbench directory not found.",
                    "workbench_path": str(workbench_path),
                }
            )

        total, used, free = shutil.disk_usage(workbench_path)
        gb = 2**30
        free_space_gb = round(free / gb, 2)
        total_space_gb = round(total / gb, 2)
        used_space_gb = round(used / gb, 2)

        folder_counts: dict[str, int] = {}
        for folder in WORKBENCH_FOLDERS:
            folder_counts[folder] = _count_entries(workbench_path / folder)

        active_tools_count = folder_counts.get("03_Active_Tools", 0)
        low_space = free_space_gb < LOW_FREE_SPACE_GB
        status = "degraded" if low_space else "online"

        return _json(
            {
                "ok": True,
                "status": status,
                "workbench_path": str(workbench_path),
                "total_space_gb": total_space_gb,
                "used_space_gb": used_space_gb,
                "free_space_gb": free_space_gb,
                "low_free_space": low_space,
                "low_free_space_threshold_gb": LOW_FREE_SPACE_GB,
                "active_tools_count": active_tools_count,
                "folder_counts": folder_counts,
            }
        )
    except OSError as exc:
        return _json(
            {
                "ok": False,
                "status": "error",
                "message": f"Could not check workbench health: {exc}",
                "workbench_path": str(workbench_path),
            }
        )


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
