"""Local durable Eve chat history under %LOCALAPPDATA%\\EMPIRE\\chat-history\\."""

from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CHAT_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
MAX_MESSAGE_CHARS = 100_000
MAX_MESSAGES = 500
MAX_TITLE_CHARS = 120
ALLOWED_ROLES = frozenset({"user", "assistant", "thinking", "activity"})

ROOT = Path(__file__).resolve().parents[1]


class ChatHistoryError(ValueError):
    """Invalid chat history request."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.status = status


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def history_dir() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE" / "chat-history"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder
        except OSError:
            pass
    folder = ROOT / "config" / "chat-history"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def active_pointer_path() -> Path:
    return history_dir() / "_active.json"


def validate_chat_id(chat_id: str) -> str:
    cleaned = chat_id.strip()
    if not CHAT_ID_PATTERN.fullmatch(cleaned):
        raise ChatHistoryError("Invalid chat id.")
    if cleaned.startswith("_") or cleaned == "active":
        raise ChatHistoryError("Invalid chat id.")
    return cleaned


def _chat_path(chat_id: str) -> Path:
    return history_dir() / f"{validate_chat_id(chat_id)}.json"


def _atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    handle, tmp_name = tempfile.mkstemp(
        prefix="chat-",
        suffix=".json",
        dir=str(path.parent),
    )
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


def _title_from_messages(messages: list[dict[str, Any]]) -> str:
    for message in messages:
        if plain_role(message.get("role")) != "user":
            continue
        text = str(message.get("text") or "").strip()
        if not text:
            continue
        first_line = text.splitlines()[0].strip()
        if len(first_line) > MAX_TITLE_CHARS:
            return first_line[: MAX_TITLE_CHARS - 1] + "…"
        return first_line
    return "Untitled chat"


def plain_role(value: Any) -> str:
    return str(value or "").strip().lower()


def normalize_message(raw: Any) -> dict[str, str] | None:
    if not isinstance(raw, dict):
        return None
    role = plain_role(raw.get("role"))
    if role not in ALLOWED_ROLES:
        return None
    text = str(raw.get("text") or "")
    if len(text) > MAX_MESSAGE_CHARS:
        text = text[: MAX_MESSAGE_CHARS - 1] + "…"
    message_id = str(raw.get("id") or "").strip() or f"msg-{abs(hash(text)) % 10_000_000}"
    created = str(raw.get("createdAt") or "").strip() or _utc_now()
    return {
        "id": message_id[:128],
        "role": role,
        "text": text,
        "createdAt": created,
    }


def normalize_chat(payload: dict[str, Any], *, chat_id: str) -> dict[str, Any]:
    messages_raw = payload.get("messages")
    if not isinstance(messages_raw, list):
        messages_raw = []
    messages: list[dict[str, str]] = []
    for item in messages_raw[:MAX_MESSAGES]:
        normalized = normalize_message(item)
        if normalized is not None:
            messages.append(normalized)

    created = str(payload.get("createdAt") or "").strip() or _utc_now()
    updated = str(payload.get("updatedAt") or "").strip() or _utc_now()
    title = str(payload.get("title") or "").strip() or _title_from_messages(messages)
    if len(title) > MAX_TITLE_CHARS:
        title = title[: MAX_TITLE_CHARS - 1] + "…"

    return {
        "id": chat_id,
        "title": title,
        "mode": str(payload.get("mode") or "").strip() or "fast",
        "model": str(payload.get("model") or "").strip(),
        "createdAt": created,
        "updatedAt": updated,
        "messages": messages,
        "messageCount": len(messages),
    }


def index_entry(chat: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": chat["id"],
        "title": chat.get("title") or "Untitled chat",
        "mode": chat.get("mode") or "fast",
        "model": chat.get("model") or "",
        "createdAt": chat.get("createdAt") or "",
        "updatedAt": chat.get("updatedAt") or "",
        "messageCount": int(chat.get("messageCount") or len(chat.get("messages") or [])),
    }


def list_chats() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    try:
        paths = sorted(history_dir().glob("*.json"))
    except OSError:
        return []
    for path in paths:
        if path.name.startswith("_"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        chat_id = str(payload.get("id") or path.stem)
        try:
            chat = normalize_chat(payload, chat_id=validate_chat_id(chat_id))
        except ChatHistoryError:
            continue
        entries.append(index_entry(chat))
    entries.sort(key=lambda item: str(item.get("updatedAt") or ""), reverse=True)
    return entries


def get_chat(chat_id: str) -> dict[str, Any]:
    path = _chat_path(chat_id)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ChatHistoryError("Chat not found.", status=404) from exc
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ChatHistoryError("Could not read chat.", status=500) from exc
    if not isinstance(payload, dict):
        raise ChatHistoryError("Chat file is invalid.", status=500)
    return normalize_chat(payload, chat_id=validate_chat_id(chat_id))


def upsert_chat(chat_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ChatHistoryError("Chat payload must be a JSON object.")
    cleaned_id = validate_chat_id(chat_id)
    existing: dict[str, Any] | None = None
    path = _chat_path(cleaned_id)
    if path.exists():
        try:
            existing = get_chat(cleaned_id)
        except ChatHistoryError:
            existing = None

    merged = dict(payload)
    if existing:
        merged.setdefault("createdAt", existing.get("createdAt"))
        if not str(merged.get("title") or "").strip():
            merged["title"] = existing.get("title")
    merged["updatedAt"] = _utc_now()
    if not str(merged.get("createdAt") or "").strip():
        merged["createdAt"] = merged["updatedAt"]

    chat = normalize_chat(merged, chat_id=cleaned_id)
    if not chat["messages"] and not existing:
        # Allow empty upsert only when updating an existing chat; skip creating empties.
        raise ChatHistoryError("Cannot save an empty chat.")
    try:
        _atomic_write(path, chat)
    except OSError as exc:
        raise ChatHistoryError("Could not save chat.", status=500) from exc
    set_active_chat_id(cleaned_id)
    return chat


def delete_chat(chat_id: str) -> None:
    path = _chat_path(chat_id)
    try:
        path.unlink(missing_ok=True)
    except OSError as exc:
        raise ChatHistoryError("Could not delete chat.", status=500) from exc
    active = get_active_chat_id()
    if active == validate_chat_id(chat_id):
        clear_active_chat_id()


def get_active_chat_id() -> str | None:
    path = active_pointer_path()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict):
        return None
    chat_id = payload.get("id")
    if not isinstance(chat_id, str):
        return None
    try:
        return validate_chat_id(chat_id)
    except ChatHistoryError:
        return None


def set_active_chat_id(chat_id: str) -> None:
    cleaned = validate_chat_id(chat_id)
    try:
        _atomic_write(active_pointer_path(), {"id": cleaned, "updatedAt": _utc_now()})
    except OSError:
        pass


def clear_active_chat_id() -> None:
    try:
        active_pointer_path().unlink(missing_ok=True)
    except OSError:
        pass


def public_list() -> dict[str, Any]:
    return {
        "ok": True,
        "chats": list_chats(),
        "activeId": get_active_chat_id(),
    }
