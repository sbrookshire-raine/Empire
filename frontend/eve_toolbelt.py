"""Persist Workbench toolbelt categories so Eve can filter heavy limb tools.

Core brain tools (Cognee memory + PocketBase tasks + health/models) are NEVER
gated here — they stay permanently registered. This file only tracks optional
limbs, grouped into clarity buckets (Always / Session / Products).

See docs/EMPIRE_CLARITY.md.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Literal

Bucket = Literal["always", "session", "products"]

# Optional limbs only — default Voice + Wiki Local (session glasses).
ALLOWED_CATEGORIES = (
    "gumloop_cloud",
    "web_research",
    "tool_forge",
    "wiki_local",
    "time_reclaim",
    "stem_factory",
    "web_scout",
    "thought_experiments",
    "voice_presence",
    "vision_local",
    "container_scout",
    "github_scout",
    "structured_extract",
    "retrieval_rerank",
    "browser_local",
    "loom_intake",
)

CATEGORY_BUCKETS: dict[str, Bucket] = {
    "voice_presence": "always",
    "wiki_local": "session",
    "web_scout": "session",
    "github_scout": "session",
    "thought_experiments": "session",
    "container_scout": "session",
    "structured_extract": "session",
    "retrieval_rerank": "session",
    "browser_local": "session",
    "loom_intake": "session",
    "tool_forge": "session",
    "web_research": "session",
    "gumloop_cloud": "session",
    "vision_local": "session",
    "time_reclaim": "products",
    "stem_factory": "products",
}

BUCKET_ORDER: tuple[Bucket, ...] = ("always", "session", "products")
BUCKET_LABELS: dict[Bucket, str] = {
    "always": "Always (core UX)",
    "session": "Session",
    "products": "Products (LEGO)",
}

DEFAULT_ACTIVE_TOOLS: tuple[str, ...] = ("voice_presence", "wiki_local")
DEFAULTS_VERSION = 2


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


def category_bucket(category: str) -> Bucket:
    return CATEGORY_BUCKETS.get(category, "session")


def categories_by_bucket() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {b: [] for b in BUCKET_ORDER}
    for cat in ALLOWED_CATEGORIES:
        out[category_bucket(cat)].append(cat)
    return out


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
    payload = {
        "active_tools": categories,
        "defaults_version": DEFAULTS_VERSION,
        "buckets": categories_by_bucket(),
    }
    try:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError:
        pass
    return path


def load_active_tools() -> list[str]:
    path = _toolbelt_path()
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return list(DEFAULT_ACTIVE_TOOLS)
    if not isinstance(parsed, dict):
        return list(DEFAULT_ACTIVE_TOOLS)
    selected = normalize_active_tools(parsed.get("active_tools"))
    version = parsed.get("defaults_version")
    if version is None or int(version or 0) < DEFAULTS_VERSION:
        for default_tool in DEFAULT_ACTIVE_TOOLS:
            if default_tool not in selected:
                selected = normalize_active_tools([*selected, default_tool])
        parsed["active_tools"] = selected
        parsed["defaults_version"] = DEFAULTS_VERSION
        parsed["buckets"] = categories_by_bucket()
        try:
            path.write_text(json.dumps(parsed, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass
    return selected


def category_enabled(category: str) -> bool:
    return category in load_active_tools()


def capability_enabled(category: str) -> bool:
    """Manual Toolbelt OR valid Research Autopilot session grant."""
    try:
        from pipeline import admission_controller

        return admission_controller.capability_active(category)
    except Exception:
        return category_enabled(category)


def load_effective_tools() -> list[str]:
    try:
        from pipeline import admission_controller

        return admission_controller.load_effective_tools()
    except Exception:
        return load_active_tools()


def apply_active_tools(payload: dict[str, Any]) -> dict[str, Any]:
    """Read active_tools from the chat payload, persist, strip before Eve."""

    if "active_tools" not in payload:
        return payload
    categories = normalize_active_tools(payload.get("active_tools"))
    write_active_tools(categories)
    cleaned = dict(payload)
    cleaned.pop("active_tools", None)
    return cleaned


def toolbelt_meta() -> dict[str, Any]:
    """API-shaped metadata for Workbench grouping."""
    return {
        "buckets": [
            {
                "id": bucket,
                "label": BUCKET_LABELS[bucket],
                "categories": categories_by_bucket()[bucket],
            }
            for bucket in BUCKET_ORDER
        ],
        "defaults": list(DEFAULT_ACTIVE_TOOLS),
        "defaults_version": DEFAULTS_VERSION,
    }
