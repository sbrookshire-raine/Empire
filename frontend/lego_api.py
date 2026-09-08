"""LEGO whiteboard API — brick catalog, board JSON, Toolbelt apply."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

try:
    from frontend import eve_toolbelt
except ModuleNotFoundError:
    import eve_toolbelt  # type: ignore[no-redef]

ROOT = Path(__file__).resolve().parents[1]
BRICKS_PATH = ROOT / "config" / "lego-bricks.json"
WORKBENCH = Path(
    os.environ.get("EMPIRE_WORKBENCH", r"C:\Empire_Workbench")
).resolve()
BOARD_DIR = WORKBENCH / "03_Active_Tools" / "lego_boards"
DEFAULT_BOARD = BOARD_DIR / "default.json"

EMPTY_BOARD: dict[str, Any] = {
    "schema_version": 1,
    "nodes": [],
    "edges": [],
    "viewport": {"x": 0, "y": 0, "zoom": 1},
}


def _empire_root() -> Path:
    return ROOT


def load_bricks() -> dict[str, Any]:
    try:
        raw = BRICKS_PATH.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read brick catalog: {exc}", "bricks": []}
    bricks = data.get("bricks") if isinstance(data, dict) else None
    if not isinstance(bricks, list):
        return {"ok": False, "error": "Brick catalog missing bricks[]", "bricks": []}
    return {
        "ok": True,
        "schema_version": data.get("schema_version", 1),
        "bricks": bricks,
        "path": str(BRICKS_PATH),
    }


def _brick_by_id(bricks: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for brick in bricks:
        if isinstance(brick, dict) and isinstance(brick.get("id"), str):
            out[brick["id"]] = brick
    return out


def load_board() -> dict[str, Any]:
    try:
        if not DEFAULT_BOARD.exists():
            return {
                "ok": True,
                "board": dict(EMPTY_BOARD),
                "path": str(DEFAULT_BOARD),
                "exists": False,
            }
        data = json.loads(DEFAULT_BOARD.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"ok": False, "error": "Board file is not an object"}
        board = {
            "schema_version": int(data.get("schema_version") or 1),
            "nodes": data.get("nodes") if isinstance(data.get("nodes"), list) else [],
            "edges": data.get("edges") if isinstance(data.get("edges"), list) else [],
            "viewport": data.get("viewport")
            if isinstance(data.get("viewport"), dict)
            else {"x": 0, "y": 0, "zoom": 1},
        }
        return {
            "ok": True,
            "board": board,
            "path": str(DEFAULT_BOARD),
            "exists": True,
        }
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read board: {exc}"}


def save_board(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {"ok": False, "error": "Expected JSON object"}
    board = {
        "schema_version": 1,
        "nodes": payload.get("nodes") if isinstance(payload.get("nodes"), list) else [],
        "edges": payload.get("edges") if isinstance(payload.get("edges"), list) else [],
        "viewport": payload.get("viewport")
        if isinstance(payload.get("viewport"), dict)
        else {"x": 0, "y": 0, "zoom": 1},
    }
    try:
        BOARD_DIR.mkdir(parents=True, exist_ok=True)
        DEFAULT_BOARD.write_text(
            json.dumps(board, indent=2) + "\n", encoding="utf-8"
        )
    except OSError as exc:
        return {"ok": False, "error": f"Cannot write board: {exc}"}
    return {"ok": True, "board": board, "path": str(DEFAULT_BOARD)}


def apply_toolbelt_from_board(payload: dict[str, Any] | None = None) -> dict[str, Any]:
    """Enable Toolbelt categories for enabled optional bricks on the board."""
    catalog = load_bricks()
    if not catalog.get("ok"):
        return catalog
    by_id = _brick_by_id(catalog["bricks"])

    if payload and isinstance(payload.get("nodes"), list):
        nodes = payload["nodes"]
    else:
        loaded = load_board()
        if not loaded.get("ok"):
            return loaded
        nodes = loaded["board"]["nodes"]

    selected: list[str] = []
    enabled_bricks: list[str] = []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        brick_id = str(node.get("brick") or "").strip()
        enabled = bool(node.get("enabled", True))
        if not enabled or not brick_id:
            continue
        meta = by_id.get(brick_id)
        if not meta:
            continue
        enabled_bricks.append(brick_id)
        toolbelt = meta.get("toolbelt")
        if isinstance(toolbelt, str) and toolbelt.strip():
            cat = toolbelt.strip()
            if cat in eve_toolbelt.ALLOWED_CATEGORIES and cat not in selected:
                selected.append(cat)

    path = eve_toolbelt.write_active_tools(selected)
    return {
        "ok": True,
        "active_tools": selected,
        "enabled_bricks": enabled_bricks,
        "toolbelt_path": str(path),
        "note": "Core bricks (memory/tasks/docling/gpu) stay available without Toolbelt.",
    }
