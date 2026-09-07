"""Fast-mode A/B model switch (one alternate Fast tag; Deep/Librarian pinned).

Config: %LOCALAPPDATA%\\EMPIRE\\ollama-fast-ab.json
  { "variant": "a"|"b", "b_model": "qwen2.5:14b" }
Variant a = CHAT_MODES["fast"].model; b = b_model.
Always keeps num_ctx = SHARED_NUM_CTX.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from frontend.ollama_chat_profiles import CHAT_MODES, SHARED_NUM_CTX

MODEL_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$")
DEFAULT_B_MODEL = "qwen2.5:14b"


def _config_path() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder / "ollama-fast-ab.json"
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    folder = root / "config"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "ollama-fast-ab.json"


def _atomic_write(path: Path, payload: dict[str, Any]) -> None:
    encoded = json.dumps(payload, indent=2) + "\n"
    handle, tmp_name = tempfile.mkstemp(prefix="fab-", suffix=".json", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def load_fast_ab() -> dict[str, Any]:
    path = _config_path()
    variant = "a"
    b_model = DEFAULT_B_MODEL
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        raw = {}
    if isinstance(raw, dict):
        v = str(raw.get("variant") or "a").strip().lower()
        if v in {"a", "b"}:
            variant = v
        bm = str(raw.get("b_model") or "").strip()
        if bm and MODEL_ID_PATTERN.fullmatch(bm):
            b_model = bm
    a_model = CHAT_MODES["fast"]["model"]
    active = a_model if variant == "a" else b_model
    return {
        "ok": True,
        "variant": variant,
        "a_model": a_model,
        "b_model": b_model,
        "active_model": active,
        "num_ctx": SHARED_NUM_CTX,
        "path": str(path),
        "note": "Fast mode only — Deep/Librarian stay pinned.",
    }


def save_fast_ab(*, variant: str | None = None, b_model: str | None = None) -> dict[str, Any]:
    current = load_fast_ab()
    next_variant = str(variant or current["variant"]).strip().lower()
    if next_variant not in {"a", "b"}:
        return {"ok": False, "error": "variant must be a or b"}
    next_b = str(b_model if b_model is not None else current["b_model"]).strip()
    if not MODEL_ID_PATTERN.fullmatch(next_b):
        return {"ok": False, "error": "Invalid b_model id"}
    payload = {"variant": next_variant, "b_model": next_b}
    try:
        _atomic_write(_config_path(), payload)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return load_fast_ab()


def resolve_fast_model(default_model: str) -> str:
    cfg = load_fast_ab()
    if cfg.get("variant") == "b":
        return str(cfg.get("active_model") or default_model)
    return default_model
