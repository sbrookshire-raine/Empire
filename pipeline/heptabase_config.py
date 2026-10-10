"""Load Heptabase board id and learning-map config (local files only)."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
LEARNING_MAP_PATH = EMPIRE_ROOT / "config" / "heptabase-learning-map.json"
ENV_CANDIDATES = (
    EMPIRE_ROOT / "config" / "heptabase.env",
    Path(os.environ.get("LOCALAPPDATA", "")) / "EMPIRE" / "heptabase.json",
)


def _parse_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return out
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def _parse_json_config(path: Path) -> dict[str, str]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(raw, dict):
        return {}
    return {str(k): str(v) for k, v in raw.items() if v is not None}


def load_settings() -> dict[str, str]:
    merged: dict[str, str] = {}
    for path in ENV_CANDIDATES:
        if path.suffix == ".json":
            merged.update(_parse_json_config(path))
        else:
            merged.update(_parse_env_file(path))
    for key, value in os.environ.items():
        if key.startswith("HEPTABASE_") and value:
            merged[key] = value
    return merged


def catalog_whiteboard_id() -> str:
    wid = (load_settings().get("HEPTABASE_DISASSEMBLY_WHITEBOARD_ID") or "").strip()
    if wid and re.match(r"^[0-9a-fA-F-]{36}$", wid):
        return wid
    return ""


def load_learning_map() -> dict[str, Any]:
    try:
        raw = json.loads(LEARNING_MAP_PATH.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}
