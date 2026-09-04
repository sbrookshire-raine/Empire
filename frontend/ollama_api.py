"""Local Ollama model listing and Workbench selection."""

from __future__ import annotations

import json
import os
import re
import tempfile
from http.client import HTTPConnection, HTTPException
from pathlib import Path

from frontend.ollama_chat_profiles import (
    CHAT_MODES,
    DEFAULT_CHAT_MODE,
    DEFAULT_MODEL,
    chat_options_for_mode,
    mode_for_model,
    public_chat_mode,
    resolve_mode,
    resolve_mode_for_installed,
)

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


def load_active_config() -> dict[str, object]:
    path = active_model_path()
    mode = DEFAULT_CHAT_MODE
    model = DEFAULT_MODEL
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        payload = {}
    if isinstance(payload, dict):
        stored_mode = payload.get("mode")
        if isinstance(stored_mode, str) and stored_mode.strip() in CHAT_MODES:
            mode = stored_mode.strip()
        stored_model = payload.get("model")
        if isinstance(stored_model, str) and MODEL_ID_PATTERN.fullmatch(stored_model.strip()):
            model = stored_model.strip()
    options = chat_options_for_mode(mode)
    resolved_mode = resolve_mode(mode)
    return {
        "mode": resolved_mode["id"],
        "model": model,
        "options": options,
        "numCtx": resolved_mode["num_ctx"],
        "label": resolved_mode["label"],
        "description": resolved_mode["description"],
    }


def load_active_model() -> str:
    return str(load_active_config()["model"])


def save_active_config(*, mode: str, model: str) -> None:
    path = active_model_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (
        json.dumps(
            {
                "mode": mode,
                "model": model,
                "options": chat_options_for_mode(mode),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
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


def save_active_model(model: str, *, mode: str | None = None) -> None:
    resolved_mode = mode or mode_for_model(model) or DEFAULT_CHAT_MODE
    save_active_config(mode=resolved_mode, model=model)


def apply_chat_mode_payload(payload: dict) -> dict:
    """Sync Workbench chat `mode` into the active Ollama config, then strip it for Eve."""

    if "mode" not in payload:
        return payload

    cleaned = dict(payload)
    mode_raw = cleaned.pop("mode", None)
    if not isinstance(mode_raw, str):
        return cleaned

    mode_id = mode_raw.strip()
    if mode_id not in CHAT_MODES:
        return cleaned

    active = load_active_config()
    mode = resolve_mode(mode_id)
    stored_model = str(active.get("model") or "").strip()
    if mode_for_model(stored_model) == mode_id and stored_model:
        model = stored_model
    else:
        model = mode["model"]
    try:
        save_active_config(mode=mode_id, model=model)
    except OSError:
        pass
    return cleaned


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
    active = load_active_config()
    installed_ids = {item["id"] for item in list_chat_models(tags or {})}
    active_mode = resolve_mode(str(active["mode"]))
    active_model = str(active["model"])
    if installed_ids:
        active_mode, active_model = resolve_mode_for_installed(active_mode["id"], installed_ids)
    return {
        "ok": connected,
        "connected": connected,
        "active": active_model,
        "activeMode": active_mode["id"],
        "activeModeLabel": active_mode["label"],
        "activeModeDescription": active_mode["description"],
        "chatModes": [
            public_chat_mode(
                resolve_mode(mode["id"]),
                installed_model=resolve_mode_for_installed(mode["id"], installed_ids)[1]
                if installed_ids
                else mode["model"],
            )
            for mode in CHAT_MODES.values()
        ],
        "chatOptions": chat_options_for_mode(active_mode["id"]),
        "models": list_chat_models(tags or {}),
        "error": error if not connected else "",
    }


def set_active_model(model: str, tags: dict, *, mode: str | None = None) -> dict:
    installed_ids = {item["id"] for item in list_chat_models(tags)}
    if mode is not None:
        cleaned_mode = mode.strip()
        if cleaned_mode not in CHAT_MODES:
            raise OllamaRequestError("Choose a valid Eve chat mode.")
        resolved_mode, candidate = resolve_mode_for_installed(cleaned_mode, installed_ids)
        if candidate not in installed_ids:
            raise OllamaRequestError(
                f"{resolved_mode['label']} is not installed. Run: ollama pull {resolved_mode['model']}"
            )
        save_active_config(mode=resolved_mode["id"], model=candidate)
        return models_status(tags, connected=True)

    candidate = model.strip() if isinstance(model, str) else ""
    if not MODEL_ID_PATTERN.fullmatch(candidate):
        raise OllamaRequestError("Choose a local Ollama chat model.")
    if candidate not in installed_ids:
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
    active = load_active_config()
    options = active["options"] if isinstance(active.get("options"), dict) else {}
    body = json.dumps(
        {
            "model": model_id,
            "messages": [
                {"role": "system", "content": "Brief task summaries only."},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "temperature": options.get("temperature", 0.2),
            "top_p": options.get("top_p", 0.9),
            "options": {"num_ctx": options.get("num_ctx", 8_192)},
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


def chat_completion(
    *,
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
    temperature: float | None = None,
) -> dict[str, object]:
    """Run one non-streaming Ollama chat completion on the active Workbench model."""

    model_id = (model or load_active_model()).strip()
    if not MODEL_ID_PATTERN.fullmatch(model_id):
        raise OllamaRequestError("Choose a local Ollama chat model.")
    active = load_active_config()
    options = active["options"] if isinstance(active.get("options"), dict) else {}
    body = json.dumps(
        {
            "model": model_id,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "temperature": temperature if temperature is not None else options.get("temperature", 0.2),
            "top_p": options.get("top_p", 0.9),
            "options": {"num_ctx": options.get("num_ctx", 8_192)},
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
        raw = response.read(512 * 1024)
        if response.status >= 400:
            raise OllamaConnectionError("Ollama could not complete this chat request.")
        payload = json.loads(raw.decode("utf-8"))
        if not isinstance(payload, dict):
            raise OllamaConnectionError("Ollama chat response was invalid.")
        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OllamaConnectionError("Ollama chat response was empty.")
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        content = ""
        if isinstance(message, dict):
            content = str(message.get("content") or "").strip()
        if not content:
            raise OllamaConnectionError("Ollama chat response was empty.")
        return {"ok": True, "content": content, "model": model_id}
    except (HTTPException, OSError, TimeoutError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise OllamaConnectionError("Ollama could not complete this chat request.") from exc
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
