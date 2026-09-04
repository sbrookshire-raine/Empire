"""FastMCP server: Eve drafts Work Orders for the Systems Mechanic (Cursor)."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORK_ORDERS_DIR = Path(r"C:\Empire_Workbench\05_Work_Orders")
DEFAULT_RESOURCE_QUEUE_DIR = Path(r"C:\Empire_Workbench\00_Resource_Queue")

mcp = FastMCP("empire-work-orders")


def _work_orders_root() -> Path:
    override = os.environ.get("EMPIRE_WORK_ORDERS_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return DEFAULT_WORK_ORDERS_DIR.resolve()


def _resource_queue_root() -> Path:
    override = os.environ.get("EMPIRE_RESOURCE_QUEUE_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return DEFAULT_RESOURCE_QUEUE_DIR.resolve()


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


def _slug(text: str, *, max_len: int = 48) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "-", text.strip()).strip("-").lower()
    if not cleaned:
        cleaned = "work-order"
    return cleaned[:max_len].rstrip("-")


def _resolve_queue_reference(source_file: str) -> tuple[str | None, str | None]:
    """Return (display path, error). Optional source under 00_Resource_Queue."""

    cleaned = source_file.strip().replace("\\", "/")
    if not cleaned:
        return None, None
    if cleaned.startswith("/") or re.match(r"^[A-Za-z]:", cleaned):
        # Absolute path allowed only if under the queue root.
        candidate = Path(cleaned).expanduser().resolve()
    else:
        if ".." in Path(cleaned).parts:
            return None, "path traversal is not allowed in source_file."
        candidate = (_resource_queue_root() / Path(*Path(cleaned).parts)).resolve()

    root = _resource_queue_root()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None, "source_file must stay under 00_Resource_Queue."

    return str(candidate), None


def _render_markdown(
    *,
    capability_needed: str,
    justification: str,
    source_file: str | None,
    created_at: str,
    order_id: str,
) -> str:
    source_line = source_file or "(none — capability request without a queue file)"
    return (
        f"# Work Order: {capability_needed.strip()}\n\n"
        f"- **Order ID:** `{order_id}`\n"
        f"- **Created (UTC):** {created_at}\n"
        f"- **Status:** open\n"
        f"- **From:** Eve (Triage Officer)\n"
        f"- **To:** Systems Mechanic (Cursor)\n\n"
        f"## Capability needed\n\n"
        f"{capability_needed.strip()}\n\n"
        f"## Source file (00_Resource_Queue)\n\n"
        f"`{source_line}`\n\n"
        f"## Justification\n\n"
        f"{justification.strip()}\n\n"
        f"## Mechanic checklist (Forge Protocol)\n\n"
        f"1. Read the source in `00_Resource_Queue` (if listed).\n"
        f"2. Build or extend the MCP wrapper under `mcp/`.\n"
        f"3. Register the server in `.cursor/mcp.json` and wire Eve if needed.\n"
        f"4. Write or update the Eve skill playbook under `agents/empire-task-agent/agent/skills/`.\n"
        f"5. On success, delete this work order from `05_Work_Orders`.\n"
        f"\n"
        f"---\n"
        f"_This is a Work Order for Cursor, not a PocketBase Task._\n"
    )


@mcp.tool()
async def draft_work_order(
    capability_needed: str,
    justification: str,
    source_file: str = "",
) -> str:
    """Create a timestamped Markdown Work Order in 05_Work_Orders for the Mechanic."""

    capability = capability_needed.strip()
    reason = justification.strip()
    if not capability:
        return _json({"ok": False, "error": "capability_needed is required."})
    if not reason:
        return _json({"ok": False, "error": "justification is required."})

    source_path, source_error = _resolve_queue_reference(source_file)
    if source_error:
        return _json(
            {
                "ok": False,
                "error": source_error,
                "source_file": source_file,
            }
        )

    if source_file.strip() and source_path is not None:
        try:
            if not Path(source_path).is_file():
                return _json(
                    {
                        "ok": False,
                        "error": f"Source file not found in Resource Queue: {source_path}",
                        "source_file": source_file,
                    }
                )
        except OSError as exc:
            return _json(
                {
                    "ok": False,
                    "error": f"Could not check source_file: {exc}",
                    "source_file": source_file,
                }
            )

    out_root = _work_orders_root()
    try:
        out_root.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return _json(
            {
                "ok": False,
                "error": f"Could not create Work Orders directory: {exc}",
                "root": str(out_root),
            }
        )

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    order_id = f"WO-{stamp}-{_slug(capability)}"
    filename = f"{order_id}.md"
    target = out_root / filename
    body = _render_markdown(
        capability_needed=capability,
        justification=reason,
        source_file=source_path,
        created_at=now.isoformat(),
        order_id=order_id,
    )

    try:
        # Exclusive create — never overwrite an existing Work Order.
        with target.open("x", encoding="utf-8") as handle:
            handle.write(body)
    except FileExistsError:
        return _json(
            {
                "ok": False,
                "error": f"Work Order already exists: {filename}",
                "path": str(target),
            }
        )
    except OSError as exc:
        return _json(
            {
                "ok": False,
                "error": f"Could not write Work Order: {exc}",
                "path": str(target),
            }
        )

    return _json(
        {
            "ok": True,
            "orderId": order_id,
            "filename": filename,
            "path": str(target),
            "root": str(out_root),
            "capability_needed": capability,
            "source_file": source_path,
            "createdAt": now.isoformat(),
        }
    )


if __name__ == "__main__":
    mcp.run()
