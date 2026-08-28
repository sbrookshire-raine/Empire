"""Local Ollama model listing and Workbench selection."""

from __future__ import annotations

import json
import os
import re
import tempfile
from http.client import HTTPConnection, HTTPException
from pathlib import Path

DEFAULT_MODEL = "llama3.1:8b"
OLLAMA_HOST = "127.0.0.1"
OLLAMA_PORT = 11434
OLLAMA_TIMEOUT_SECONDS = 5
OLLAMA_CHAT_TIMEOUT_SECONDS = 90
MAX_TAGS_BYTES = 2 * 1024 * 1024
MAX_SUMMARY_TASKS = 40
MAX_SUMMARY_DESC_CHARS = 200
MODEL_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$")


class OllamaRequestError(ValueError):
    """Raised when a Workbench model selection is not a local chat model."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.status = status


class OllamaConnectionError(ConnectionError):
    """Ollama is not reachable on loopback."""


def active_model_path() -> Path:
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "EMPIRE" / "ollama-active-model.json"
    return Path(__file__).resolve().parents[1] / "config" / "ollama-active-model.json"


def load_active_model() -> str:
    path = active_model_path()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return DEFAULT_MODEL
    if not isinstance(payload, dict):
        return DEFAULT_MODEL
    model = payload.get("model")
    if isinstance(model, str) and MODEL_ID_PATTERN.fullmatch(model.strip()):
        return model.strip()
    return DEFAULT_MODEL


def save_active_model(model: str) -> None:
    path = active_model_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps({"model": model}, indent=2, sort_keys=True) + "\n"
    handle, tmp_name = tempfile.mkstemp(
        prefix="ollama-model-",
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


def is_chat_model(entry: dict) -> bool:
    name = str(entry.get("name") or entry.get("model") or "").strip()
    if not name:
        return False
    capabilities = entry.get("capabilities")
    if isinstance(capabilities, list) and capabilities:
        caps = {str(item).casefold() for item in capabilities}
        if "embedding" in caps and "completion" not in caps and "tools" not in caps:
            return False
        return "completion" in caps or "tools" in caps
    lowered = name.casefold()
    family = str((entry.get("details") or {}).get("family") or "").casefold()
    if "embed" in lowered or family in {"bert", "nomic-bert"}:
        return False
    return True


def list_chat_models(tags: dict) -> list[dict]:
    raw = tags.get("models") if isinstance(tags, dict) else None
    if not isinstance(raw, list):
        return []
    models: list[dict] = []
    seen: set[str] = set()
    for entry in raw:
        if not isinstance(entry, dict) or not is_chat_model(entry):
            continue
        model_id = str(entry.get("name") or entry.get("model") or "").strip()
        if not model_id or model_id in seen or not MODEL_ID_PATTERN.fullmatch(model_id):
            continue
        seen.add(model_id)
        capabilities = entry.get("capabilities")
        tools = isinstance(capabilities, list) and any(
            str(item).casefold() == "tools" for item in capabilities
        )
        details = entry.get("details") if isinstance(entry.get("details"), dict) else {}
        size = str(details.get("parameter_size") or "").strip()
        models.append(
            {
                "id": model_id,
                "label": f"{model_id} · {size}" if size else model_id,
                "tools": tools,
            }
        )
    return models


def models_status(tags: dict | None, *, connected: bool, error: str = "") -> dict:
    return {
        "ok": connected,
        "connected": connected,
        "active": load_active_model(),
        "models": list_chat_models(tags or {}),
        "error": error if not connected else "",
    }


def set_active_model(model: str, tags: dict) -> dict:
    candidate = model.strip() if isinstance(model, str) else ""
    if not MODEL_ID_PATTERN.fullmatch(candidate):
        raise OllamaRequestError("Choose a local Ollama chat model.")
    allowed = {item["id"] for item in list_chat_models(tags)}
    if candidate not in allowed:
        raise OllamaRequestError("That model is not a local Ollama chat model.")
    save_active_model(candidate)
    return models_status(tags, connected=True)


def format_tasks_for_summary(tasks: list[dict], *, limit: int = MAX_SUMMARY_TASKS) -> str:
    lines: list[str] = []
    for task in tasks[:limit]:
        if not isinstance(task, dict):
            continue
        title = str(task.get("title") or "").strip()
        if not title:
            continue
        status = str(task.get("status") or "todo").strip()
        priority = task.get("priority", "")
        description = str(task.get("description") or "").strip()
        if len(description) > MAX_SUMMARY_DESC_CHARS:
            description = description[: MAX_SUMMARY_DESC_CHARS - 1] + "…"
        line = f"- [{status}] {title} (priority {priority})"
        if description:
            line += f": {description}"
        lines.append(line)
    return "\n".join(lines) if lines else "No tasks."


def summarize_tasks(tasks: list[dict], *, model: str | None = None) -> dict:
    if not isinstance(tasks, list):
        raise OllamaRequestError("Task list is invalid.")
    model_id = (model or load_active_model()).strip()
    if not MODEL_ID_PATTERN.fullmatch(model_id):
        raise OllamaRequestError("Choose a local Ollama chat model.")
    if not tasks:
        return {
            "ok": True,
            "summary": "No PocketBase tasks yet. Add tasks on the Tasks tab when you want Eve to track work.",
            "model": model_id,
            "taskCount": 0,
        }
    task_block = format_tasks_for_summary(tasks)
    prompt = (
        "Summarize this local PocketBase task list for someone about to chat with Eve.\n"
        "Write 3–6 short bullet points covering: in-progress vs todo vs done, "
        "highest-priority open items, anything that looks blocked, and one suggested focus.\n"
        "Under 120 words. Plain bullets only. No preamble.\n\n"
        f"Tasks:\n{task_block}"
    )
    body = json.dumps(
        {
            "model": model_id,
            "messages": [
                {"role": "system", "content": "Brief task summaries only."},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "options": {"temperature": 0.3},
        }
    ).encode("utf-8")
    connection = HTTPConnection(OLLAMA_HOST, OLLAMA_PORT, timeout=OLLAMA_CHAT_TIMEOUT_SECONDS)
    try:
        connection.request(
            "POST",
            "/v1/chat/completions",
            body=body,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )
        response = connection.getresponse()
        raw = response.read(256 * 1024)
        if response.status >= 400:
            raise OllamaConnectionError("Ollama could not summarize tasks.")
        payload = json.loads(raw.decode("utf-8"))
        if not isinstance(payload, dict):
            raise OllamaConnectionError("Ollama summary was invalid.")
        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OllamaConnectionError("Ollama summary was empty.")
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        content = ""
        if isinstance(message, dict):
            content = str(message.get("content") or "").strip()
        if not content:
            raise OllamaConnectionError("Ollama summary was empty.")
        return {
            "ok": True,
            "summary": content,
            "model": model_id,
            "taskCount": len(tasks),
        }
    except (HTTPException, OSError, TimeoutError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OllamaConnectionError("Ollama could not summarize tasks.") from exc
    finally:
        connection.close()


def fetch_tags() -> dict:
    connection = HTTPConnection(OLLAMA_HOST, OLLAMA_PORT, timeout=OLLAMA_TIMEOUT_SECONDS)
    try:
        connection.request("GET", "/api/tags", headers={"Accept": "application/json"})
        response = connection.getresponse()
        body = response.read(MAX_TAGS_BYTES + 1)
        if len(body) > MAX_TAGS_BYTES:
            raise OllamaConnectionError("Ollama model list was too large.")
        if response.status >= 400:
            raise OllamaConnectionError("Ollama is unavailable.")
        payload = json.loads(body.decode("utf-8"))
        if not isinstance(payload, dict):
            raise OllamaConnectionError("Ollama model list was invalid.")
        return payload
    except (HTTPException, OSError, TimeoutError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OllamaConnectionError("Ollama is unavailable.") from exc
    finally:
        connection.close()
