"""Curated Eve chat modes, Ollama sampling defaults, and per-model context limits."""

from __future__ import annotations

from typing import Any, TypedDict


class ChatMode(TypedDict):
    id: str
    label: str
    description: str
    model: str
    model_aliases: tuple[str, ...]
    num_ctx: int
    temperature: float


# Shared nucleus sampling; temperature is per-mode (strict tools vs creative).
GLOBAL_CHAT_OPTIONS: dict[str, float] = {
    "top_p": 0.90,
}

# Protect 16 GB VRAM — every mode uses the same context window.
SHARED_NUM_CTX = 8_192

CHAT_MODES: dict[str, ChatMode] = {
    "fast": {
        "id": "fast",
        "label": "Fast Mode (14b)",
        "description": (
            "Daily driver — brainstorming, quick file reads, standard scripts, and tool calls."
        ),
        "model": "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
        "model_aliases": ("richardyoung/qwen2.5-14b-instruct-abliterated",),
        "num_ctx": SHARED_NUM_CTX,
        "temperature": 0.2,
    },
    "deep": {
        "id": "deep",
        "label": "Deep Mode (32b)",
        "description": (
            "Architect — deep planning, complex MCP work, and highest-tier reasoning."
        ),
        "model": "qwen2.5:32b",
        "model_aliases": (),
        "num_ctx": SHARED_NUM_CTX,
        "temperature": 0.7,
    },
    "librarian": {
        "id": "librarian",
        "label": "Librarian (Command-R 35b)",
        "description": (
            "Mass synthesis — cross-reference many flattened files and long memory snippets."
        ),
        "model": "command-r:35b",
        "model_aliases": (),
        "num_ctx": SHARED_NUM_CTX,
        "temperature": 0.4,
    },
}

DEFAULT_CHAT_MODE = "fast"
DEFAULT_MODEL = CHAT_MODES[DEFAULT_CHAT_MODE]["model"]


def chat_mode_list() -> list[dict[str, Any]]:
    return [
        {
            "id": mode["id"],
            "label": mode["label"],
            "description": mode["description"],
            "model": mode["model"],
            "numCtx": mode["num_ctx"],
            "temperature": mode["temperature"],
            "topP": GLOBAL_CHAT_OPTIONS["top_p"],
        }
        for mode in CHAT_MODES.values()
    ]


def mode_for_model(model: str) -> str | None:
    cleaned = model.strip()
    if not cleaned:
        return None
    for mode in CHAT_MODES.values():
        if cleaned == mode["model"] or cleaned in mode["model_aliases"]:
            return mode["id"]
    return None


def resolve_mode(mode_id: str | None) -> ChatMode:
    if isinstance(mode_id, str) and mode_id.strip() in CHAT_MODES:
        return CHAT_MODES[mode_id.strip()]
    return CHAT_MODES[DEFAULT_CHAT_MODE]


def resolve_installed_model(preferred: str, installed_ids: set[str]) -> str | None:
    candidate = preferred.strip()
    if not candidate:
        return None
    if candidate in installed_ids:
        return candidate
    if ":" not in candidate:
        tagged = f"{candidate}:latest"
        if tagged in installed_ids:
            return tagged
    base = candidate.split(":", 1)[0]
    for installed in installed_ids:
        if installed == base or installed.startswith(f"{base}:"):
            return installed
    return None


def resolve_mode_for_installed(mode_id: str | None, installed_ids: set[str]) -> tuple[ChatMode, str]:
    mode = resolve_mode(mode_id)
    resolved = resolve_installed_model(mode["model"], installed_ids)
    if resolved:
        return mode, resolved
    for fallback_id in (DEFAULT_CHAT_MODE, "deep", "librarian"):
        fallback_mode = CHAT_MODES[fallback_id]
        resolved = resolve_installed_model(fallback_mode["model"], installed_ids)
        if resolved:
            return fallback_mode, resolved
    return mode, mode["model"]


def chat_options_for_mode(mode_id: str | None) -> dict[str, float | int]:
    mode = resolve_mode(mode_id)
    return {
        "temperature": mode["temperature"],
        "top_p": GLOBAL_CHAT_OPTIONS["top_p"],
        "num_ctx": mode["num_ctx"],
    }


def public_chat_mode(mode: ChatMode, *, installed_model: str) -> dict[str, Any]:
    return {
        "id": mode["id"],
        "label": mode["label"],
        "description": mode["description"],
        "model": installed_model,
        "numCtx": mode["num_ctx"],
        "temperature": mode["temperature"],
        "topP": GLOBAL_CHAT_OPTIONS["top_p"],
    }
