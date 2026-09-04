"""Persist Workbench toolbelt categories so Eve can filter heavy limb tools.

Core brain tools (Cognee memory + PocketBase tasks + health/models) are NEVER
gated here — they stay permanently registered. This file only tracks optional
external limbs (Gumloop, web research, Tool Forge / Active Tools).

Note: PocketBase tasks are Tasks. A Work Order is a separate concept (Eve writing
a .md request for Cursor) and must not be conflated with PocketBase.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

# Optional limbs only — default all OFF to protect context until the user opts in.
ALLOWED_CATEGORIES = ("gumloop_cloud", "web_research", "tool_forge")
DEFAULT_ACTIVE_TOOLS: tuple[str, ...] = ()


def _toolbelt_path() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder / "eve-toolbelt.json"
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    return root / "config" / "eve-toolbelt.json"


def normalize_active_tools(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return list(DEFAULT_ACTIVE_TOOLS)
    selected: list[str] = []
    for item in raw:
        if not isinstance(item, str):
            continue
        cleaned = item.strip()
        if cleaned in ALLOWED_CATEGORIES and cleaned not in selected:
            selected.append(cleaned)
    return selected


def write_active_tools(categories: list[str]) -> Path:
    path = _toolbelt_path()
    payload = {"active_tools": categories}
    try:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass
    return path


def category_enabled(category: str) -> bool:
    path = _toolbelt_path()
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return category in DEFAULT_ACTIVE_TOOLS
    if not isinstance(parsed, dict):
        return category in DEFAULT_ACTIVE_TOOLS
    return category in normalize_active_tools(parsed.get("active_tools"))


def apply_active_tools(payload: dict[str, Any]) -> dict[str, Any]:
    """Read active_tools from the chat payload, persist, strip before Eve."""

    if "active_tools" not in payload:
        return payload
    categories = normalize_active_tools(payload.get("active_tools"))
    write_active_tools(categories)
    cleaned = dict(payload)
    cleaned.pop("active_tools", None)
    return cleaned
