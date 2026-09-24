"""Serve EMPIRE frontend static files and a local-only service control API."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import uuid
import asyncio
import re
import urllib.error
import urllib.request
from email import policy
from email.parser import BytesParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

try:
    from frontend import (
        chat_continuity,
        chat_history,
        dashboard_api,
        companion_api,
        eve_proxy,
        eve_toolbelt,
        lego_api,
        memory_api,
        ollama_api,
        ollama_fast_ab,
        ollama_inventory,
        primitives_api,
        project_catalog,
        resource_pulse_api,
        wiki_api,
        wiki_drift_api,
        workbench_ui_api,
    )
except ModuleNotFoundError:
    import chat_continuity  # type: ignore[no-redef]
    import chat_history  # type: ignore[no-redef]
    import dashboard_api  # type: ignore[no-redef]
    import companion_api  # type: ignore[no-redef]
    import eve_proxy  # type: ignore[no-redef]
    import eve_toolbelt  # type: ignore[no-redef]
    import lego_api  # type: ignore[no-redef]
    import memory_api  # type: ignore[no-redef]
    import ollama_api  # type: ignore[no-redef]
    import ollama_fast_ab  # type: ignore[no-redef]
    import ollama_inventory  # type: ignore[no-redef]
    import project_catalog  # type: ignore[no-redef]
    import primitives_api  # type: ignore[no-redef]
    import resource_pulse_api  # type: ignore[no-redef]
    import wiki_api  # type: ignore[no-redef]
    import wiki_drift_api  # type: ignore[no-redef]
    import workbench_ui_api  # type: ignore[no-redef]

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config" / "services.json"
HOST = "127.0.0.1"
PORT = 8080
PS = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File"]
MEMORY_ALLOWED_ORIGINS = {
    "http://127.0.0.1:8080",
    "http://localhost:8080",
}


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def run_ps_script(script: Path, extra_args: list[str] | None = None, timeout: int = 120) -> dict:
    cmd = [*PS, str(script), *(extra_args or [])]
    result = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


AMBIENT_LOG_PATH = ROOT / "eve-audit" / "active_chat.log"
AMBIENT_LOG_MAX_BYTES = 5 * 1024 * 1024
AMBIENT_LOG_BACKUPS = 3
VOICE_ROUTER_MODEL = "llama3.1:latest"
# The voice router runs a SECOND model (llama3.1 8B) on every completed message. On a 16 GB
# card that competes with the 14B chat model (14B @16k ≈ 11.9 GB) and forces evictions, and in
# the measured trace it returned `fallback: true` after ~5 s — i.e. cost with no benefit.
# Off by default (2026-09-23); set EMPIRE_VOICE_ROUTER=1 to restore the rewrite pass.
VOICE_ROUTER_ENABLED = os.environ.get("EMPIRE_VOICE_ROUTER", "").strip().casefold() in {
    "1",
    "true",
    "yes",
    "on",
}
VOICE_ROUTER_PROMPT = (
    "You are Eve. Your job is to format the following technical message into a single, "
    "dry sentence. RULES: 1. You MUST preserve all numbers, dates, and proper nouns "
    "exactly as written. 2. DO NOT add any new information, recommendations, or URLs. "
    "3. If the message describes an error or blocked action, state the failure plainly "
    "with no apology. 4. DO NOT output conversational filler."
)
CATALOG_INTENT_RE = re.compile(
    r"\b(?:query|search|find)\s+(?:your\s+)?catalog\b|"
    r"\bfind\s+tools\s+related\s+to\b|\bcatalog\s+search\b",
    re.IGNORECASE,
)
# Explicit pressure to force heavy/GPU work despite constraints. Both a
# coercive verb and a heavy-resource noun must be present (order-independent)
# so ordinary prompts never trigger the resource guard.
RESOURCE_BLOCK_RE = re.compile(
    r"(?=.*\b(?:force|force[- ]?enable|override|bypass|overrule|ignore|disregard|despite|regardless)\b)"
    r"(?=.*\b(?:gpu|vram|vision|stem|demucs|rerank|heavy|headroom|constrain\w*|limit\w*)\b)",
    re.IGNORECASE | re.DOTALL,
)
CATALOG_ROUTER_PROMPT = (
    "You are an intent router. Extract the catalog search query from the user's prompt. "
    "Do NOT extract Wikipedia titles. Return ONLY JSON: "
    '{"catalog_query": "extracted term"}. If no catalog search is requested, '
    'return {"catalog_query": null}. Keep the extracted term concise. If multiple catalog '
    "concepts are requested, select the most specific tool-bearing term."
    )

def _catalog_context(message: str) -> str:
    if not CATALOG_INTENT_RE.search(message or ""):
        return ""
    catalog_text = re.split(r"\bthen\b", message or "", maxsplit=1, flags=re.IGNORECASE)[0]
    targets = re.findall(r"['\"]([^'\"]{2,120})['\"]", catalog_text)
    if not targets and re.search(r"\bminimax\b", catalog_text, re.I):
        targets.append("minimax")
    if not targets:
        return ""
    from pipeline.discovery_catalog import search_catalog

    results = [search_catalog(target, limit=5) for target in targets[:4]]
    compact = json.dumps({"queries": targets[:4], "results": results}, ensure_ascii=False, default=str)
    return f"\n\n[AUTHORITATIVE LOCAL CATALOG CONTEXT]\n{compact}\nUse these catalog facts directly."

def _resource_guard_context(message: str) -> str:
    if not RESOURCE_BLOCK_RE.search(message or ""):
        return ""
    try:
        from pipeline import resource_pulse

        pulse = resource_pulse.pulse()
    except Exception as exc:  # noqa: BLE001
        return f"\n\n[SYSTEM NOTE: Resource guard unavailable ({exc}). Refuse forced heavy work.]"
    if pulse.get("headroom_ok"):
        return ""
    reasons = "; ".join(str(item) for item in pulse.get("headroom_reasons") or [])
    return (
        "\n\n[AUTHORITATIVE RESOURCE BLOCK. The requested heavy/GPU action is "
        f"blocked. Reasons: {reasons or 'headroom unavailable'}. Refuse the action and "
        "tell the user Architect approval or safer conditions are required. Do not run "
        "unrelated tools or suggest unverified consequences.]"
    )


_USER_MESSAGE_ANCHOR = "\n\nUser message:\n"

# Cross-domain asks ("can I learn drums using the rules of juggling?") need the Architect's decoded
# ledger, not just an encyclopedia lookup. Measured 2026-09-24: with only a prompt hint, that
# question produced 6 phrase-shaped wiki searches and ZERO primitive_lookup calls, so the ledger
# route never fired. Same remedy as the catalog block: run the lookup server-side and put the
# mechanisms next to the ask.
_TRANSFER_RE = re.compile(
    r"(?:using the rules of|rules of [a-z][a-z ]{2,40} (?:for|on|in)|"
    r"apply(?:ing)? (?:the )?(?:rules|principles|idea|concept|logic|thinking) of|"
    r"borrow(?:ing)? (?:from|the)|inspired by|inspiration from|"
    r"take [a-z][a-z ]{2,30} and (?:apply|use|try|map)|"
    r"same (?:way|principle|mechanism|pattern|rules) as|"
    r"(?:work|apply|transfer)(?:s|ing)? (?:the same|to|for|with)|"
    r"could [a-z][a-z ]{2,30} (?:work|apply|help))",
    re.IGNORECASE,
)


def _transfer_context(message: str) -> str:
    """Attach the Architect's own decoded primitives when the ask transfers A onto B."""

    if not _TRANSFER_RE.search(message or ""):
        return ""
    try:
        from pipeline import primitive_lookup

        result = primitive_lookup.lookup(text=message, limit=3)
    except Exception:  # noqa: BLE001 — never let context building break a turn
        return ""
    matches = result.get("matches") or []
    if not matches:
        vocabulary = ", ".join(
            str(entry.get("primitive")) for entry in (result.get("vocabulary") or [])[:12]
        )
        return (
            "\n\n[AUTHORITATIVE PRIMITIVE LEDGER: no decoded row matches this ask. The ledger's own "
            f"vocabulary is: {vocabulary}. Name the closest of these, or say plainly that this "
            "connection is not in the ledger yet — do not invent a mechanism.]"
        )
    lines = [
        f"- {match['thing']} ({match['domain']}): mechanism = {match['mechanism'][:170]}; "
        f"primitives = {match['primitives']}; sibling = {match['sibling'][:130]}"
        for match in matches
    ]
    return (
        "\n\n[AUTHORITATIVE PRIMITIVE LEDGER CONTEXT — the Architect's own decoded mechanisms, from "
        "his thought-experiment ledger. Name the shared primitive, state the mapping in one sentence, "
        "say where the analogy breaks, and label what came from a tool vs what is your inference. "
        "Do not answer this from general knowledge alone.]\n" + "\n".join(lines)
    )


def _attach_server_context(message: str, context: str) -> str:
    """Attach authoritative server context immediately before the user request.

    Mirrors frontend/workbench_ui_api.py and frontend/memory_api.py. The companion
    preamble is long, so a block prepended above it is stranded far from the ask —
    the model then ignored catalog facts and called wiki_scout_search instead.
    """

    block = (context or "").strip()
    if not block:
        return message
    if _USER_MESSAGE_ANCHOR in message:
        head, _, user_part = message.rpartition(_USER_MESSAGE_ANCHOR)
        return f"{head}\n\n{block}\n\nUser message:\n{user_part}"
    return f"{block}\n\n[USER REQUEST]\n{message}"


def _catalog_directive(message: str) -> str:
    """Directive that stops catalog asks being misrouted to the wiki limb.

    A prompt may legitimately mix both (catalog + encyclopedia), so the wiki ban
    only applies when the request has no encyclopedia target of its own.
    """

    wiki_also = False
    try:
        from frontend.companion_api import extract_user_message
        from frontend.wiki_drift_api import is_wiki_lookup_query

        # Classification only (a routing guard for mixed catalog + encyclopedia asks).
        # This is NOT retrieval middleware: it never injects wiki evidence, and it is
        # independent of EMPIRE_WIKI_MIDDLEWARE. Eve still owns the actual lookup.
        wiki_also = is_wiki_lookup_query(extract_user_message(message))
    except Exception:  # noqa: BLE001
        wiki_also = False
    if wiki_also:
        return (
            "SYSTEM DIRECTIVE: Answer the catalog portion of this request from the rows "
            'above, naming the exact tool from the "id" field. Use Wikipedia tools only '
            "for the separate encyclopedia portion. Do not replace these facts with a "
            "generic tool list."
        )
    return (
        "SYSTEM DIRECTIVE: The user is asking about local EMPIRE tools and capabilities. "
        'Answer from the rows above, naming the exact tool from the "id" field. Do NOT '
        "call wiki_scout_search, wiki_scout_compare_years, wiki_resolve, "
        "wiki_read_section, or any Wikipedia/encyclopedia tool for this request — those "
        "return encyclopedia articles and cannot contain EMPIRE tool names. Do not claim "
        "catalog search is unavailable and do not replace these facts with a generic tool list."
    )


def _router_model() -> str:
    """Model for the small routing passes (catalog intent, optional voice styling).

    2026-09-23: these used to hard-code `llama3.1:latest`. Loading a second model beside the
    14B chat model (11 GB) exceeds a 16 GB card, so the chat model gets evicted and the next
    turn pays a full reload (~30 s). Reuse whatever chat model is already loaded instead.
    """

    try:
        model = str(ollama_api.load_active_config().get("model") or "").strip()
    except Exception:  # noqa: BLE001
        model = ""
    return model or VOICE_ROUTER_MODEL


async def _extract_catalog_intent(message: str) -> str | None:
    """Use the fast local model to separate catalog intent from Wiki intent."""
    if not CATALOG_INTENT_RE.search(message or ""):
        return None
    try:
        result = await asyncio.to_thread(
            ollama_api.chat_completion,
            system_prompt=CATALOG_ROUTER_PROMPT,
            user_prompt=message[:8000],
            model=_router_model(),
            temperature=0.0,
        )
        raw = str(result.get("content") or "").strip()
        parsed = json.loads(raw)
        query = parsed.get("catalog_query") if isinstance(parsed, dict) else None
        if not isinstance(query, str) or not query.strip():
            return None
        return query.strip()[:160]
    except Exception:
        return None


async def _catalog_context_async(message: str) -> str:
    query = await _extract_catalog_intent(message)
    if not query:
        return ""
    try:
        from pipeline.discovery_catalog import search_catalog

        result = await asyncio.to_thread(search_catalog, query, 5)
        if result.get("ok") and not result.get("results"):
            for candidate in re.findall(r"\bminimax\b|\b[A-Za-z][A-Za-z-]{3,}\b", query, re.I):
                retry = await asyncio.to_thread(search_catalog, candidate, 5)
                if retry.get("results"):
                    result = retry
                    query = candidate
                    break
    except Exception as exc:  # noqa: BLE001
        return f"\n\n[SYSTEM NOTE: Catalog search unavailable: {exc}]"
    compact = json.dumps({"query": query, "result": result}, ensure_ascii=False, default=str)
    return (
        "\n\n[AUTHORITATIVE LOCAL CATALOG CONTEXT]\n"
        f"{compact}\n"
        f"{_catalog_directive(message)}"
    )


def _ambient_text(value: object, max_chars: int = 4000) -> str:
    text = str(value or "").strip()
    return text[: max_chars - 1].rstrip() + "..." if len(text) > max_chars else text


TRACE_ENABLED = os.environ.get("EMPIRE_TRACE", "").strip().casefold() in {"1", "true", "yes", "on"}
TRACE_LOG_PATH = ROOT / "eve-audit" / "eve-trace.jsonl"

# A browser turn spans two HTTP requests: the POST that starts it (which mints the turn id and is
# where `turn.start` is written) and the GET `/stream` that carries every tool/step event. They are
# *different handler instances*, so the per-request `_ambient_turn_id` cannot reach the stream — this
# small session→turn map bridges them. Without it the tool events land in a separate "(no turn id)"
# group and cannot be attributed to the question that caused them (measured 2026-09-24).
_TURN_BY_SESSION: dict[str, str] = {}
_MAX_TRACKED_SESSIONS = 64
# Same two-request problem for the *text*: the enriched user message is built on the POST, but the
# ambient record is written on the GET /stream handler, so `_ambient_user_text` was always empty
# there — the audit log held the answer but never the question. Measured 2026-09-24 while checking
# whether a server-injected context block reached the model.
_USER_TEXT_BY_SESSION: dict[str, str] = {}


def remember_turn(session_id: str, turn_id: str) -> None:
    """Record which turn is current for a session (called by the POST that starts it)."""

    session = str(session_id or "").strip()
    turn = str(turn_id or "").strip()
    if not session or not turn:
        return
    _TURN_BY_SESSION[session] = turn
    while len(_TURN_BY_SESSION) > _MAX_TRACKED_SESSIONS:
        _TURN_BY_SESSION.pop(next(iter(_TURN_BY_SESSION)), None)


def turn_for_session(session_id: str) -> str:
    """The current turn id for a session, or "" when unknown."""

    return _TURN_BY_SESSION.get(str(session_id or "").strip(), "")


def remember_user_text(session_id: str, text: str) -> None:
    """Keep the enriched user message so the stream handler can log it."""

    session = str(session_id or "").strip()
    value = str(text or "")
    if not session or not value:
        return
    _USER_TEXT_BY_SESSION[session] = value
    while len(_USER_TEXT_BY_SESSION) > _MAX_TRACKED_SESSIONS:
        _USER_TEXT_BY_SESSION.pop(next(iter(_USER_TEXT_BY_SESSION)), None)


def user_text_for_session(session_id: str) -> str:
    """The enriched user message for a session, or "" when unknown."""

    return _USER_TEXT_BY_SESSION.get(str(session_id or "").strip(), "")


def trace_event(kind: str, **fields: object) -> None:
    """Append one trace record when EMPIRE_TRACE is on.

    Covers the whole path the Architect asked for: browser turn start → each projected Eve
    event (step boundaries, tool requests, message chunks) → tool latency → voice-router
    timing. Never let tracing break chat.
    """

    if not TRACE_ENABLED:
        return
    try:
        TRACE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "ts": round(time.time(), 3),
            "kind": kind,
            **fields,
        }
        with TRACE_LOG_PATH.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, default=str) + "\n")
    except OSError:
        pass


def _append_ambient_event(
    *,
    role: str,
    text: str,
    status: str,
    session_id: str = "",
    turn_id: str = "",
) -> None:
    """Best-effort bounded event output; audit failure must not break chat."""
    if not text.strip():
        return
    try:
        AMBIENT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        if AMBIENT_LOG_PATH.exists() and AMBIENT_LOG_PATH.stat().st_size >= AMBIENT_LOG_MAX_BYTES:
            for index in range(AMBIENT_LOG_BACKUPS, 0, -1):
                source = AMBIENT_LOG_PATH.with_name(f"{AMBIENT_LOG_PATH.name}.{index}")
                target = AMBIENT_LOG_PATH.with_name(f"{AMBIENT_LOG_PATH.name}.{index + 1}")
                if index == AMBIENT_LOG_BACKUPS:
                    target.unlink(missing_ok=True)
                if source.exists():
                    source.replace(target)
            AMBIENT_LOG_PATH.replace(AMBIENT_LOG_PATH.with_name(f"{AMBIENT_LOG_PATH.name}.1"))
        event = {
            "schema_version": 1,
            "event_id": uuid.uuid4().hex,
            "session_id": _ambient_text(session_id, 128),
            "turn_id": _ambient_text(turn_id, 128),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "role": role,
            "text": _ambient_text(text),
            "status": status,
            "source": "frontend.serve",
        }
        with AMBIENT_LOG_PATH.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + "\n")
    except (OSError, TypeError, ValueError):
        pass


async def _voice_router(text: str) -> tuple[str, float, bool]:
    """Rewrite final assistant text and return (text, elapsed seconds, fallback)."""
    raw = (text or "").strip()
    if not raw:
        return raw, 0.0, True
    voice_start = time.perf_counter()
    try:
        result = await asyncio.to_thread(
            ollama_api.chat_completion,
            system_prompt=VOICE_ROUTER_PROMPT.format(payload=raw),
            user_prompt="Output only the text replacing the Translation line. Do not use quotes or a preamble.",
            model=_router_model(),
            temperature=0.25,
        )
        rewritten = str(result.get("content") or "").strip()
        candidate = rewritten or raw
        safe = _voice_output_is_safe(raw, candidate)
        return (candidate if safe else raw), time.perf_counter() - voice_start, not safe
    except Exception:
        return raw, time.perf_counter() - voice_start, True


def _voice_output_is_safe(raw: str, candidate: str) -> bool:
    """Reject rewrites that drop protected literals or failure/refusal semantics."""
    import re

    leaked_meta = (
        "presentation layer",
        "voice formatter",
        "payload to translate",
        "output only the text",
        "example 1:",
        "translation:",
    )
    candidate_lower = candidate.casefold()
    raw_lower = raw.casefold()
    if any(marker in candidate_lower and marker not in raw_lower for marker in leaked_meta):
        return False
    for token in re.findall(r"https?://\S+|\b\d+(?:[.,:-]\d+)*\b", raw):
        if token.casefold() not in candidate.casefold():
            return False
    for phrase in re.findall(r"\([^)]{2,120}\)|'[^']{2,120}'|\"[^\"]{2,120}\"", raw):
        if phrase.casefold() not in candidate.casefold():
            return False
    stopwords = {
        "a", "an", "the", "and", "or", "to", "of", "in", "on", "for", "with",
        "is", "are", "was", "were", "be", "this", "that", "it", "from", "as",
        "only", "local", "system", "payload", "result",
    }
    raw_words = set(re.findall(r"[a-z0-9][a-z0-9'-]*", raw_lower)) - stopwords
    candidate_words = set(re.findall(r"[a-z0-9][a-z0-9'-]*", candidate_lower)) - stopwords
    if raw_words:
        overlap = len(raw_words & candidate_words) / len(raw_words)
        novel = len(candidate_words - raw_words)
        if novel > 15 or (len(raw_words) >= 4 and overlap < 0.3):
            return False
    if any(term in raw_lower for term in ("cannot", "can't", "unable", "no usable", "not found", "blocked", "failure", "error")):
        if not any(term in candidate_lower for term in ("cannot", "can't", "unable", "no usable", "not found", "blocked", "failure", "error")):
            return False
    return True


def run_ps_command(command: str, timeout: int = 30) -> dict:
    result = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def get_port_pid(port: int) -> int | None:
    result = run_ps_command(
        f"(Get-NetTCPConnection -LocalPort {port} -State Listen -ErrorAction SilentlyContinue "
        f"| Select-Object -First 1).OwningProcess"
    )
    if not result["ok"] or not result["stdout"]:
        return None
    try:
        pid = int(result["stdout"].strip())
        return pid if pid > 0 else None
    except ValueError:
        return None


def port_listening(port: int) -> bool:
    return get_port_pid(port) is not None


def check_health(url: str, timeout_sec: int = 8) -> dict:
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            return {"ok": 200 <= resp.status < 300, "detail": f"HTTP {resp.status}"}
    except urllib.error.HTTPError as err:
        return {"ok": False, "detail": f"HTTP {err.code}"}
    except Exception as err:  # noqa: BLE001
        return {"ok": False, "detail": str(err)}


def resolve_path(relative: str) -> Path:
    path = Path(relative.replace("/", os.sep))
    if path.is_absolute():
        return path
    return ROOT / path


def resolve_executable(exe: str) -> str:
    if exe.startswith("npm"):
        for candidate in ("npm.cmd", "npm"):
            resolved = shutil_which(candidate)
            if resolved:
                return resolved
    if exe.startswith("python"):
        resolved = shutil_which("python")
        if resolved:
            return resolved
    resolved = resolve_path(exe)
    return str(resolved)


def shutil_which(name: str) -> str | None:
    return shutil.which(name)


def expand_env(values: dict[str, str]) -> dict[str, str]:
    expanded: dict[str, str] = {}
    for key, value in values.items():
        expanded[key] = value.replace("{{EMPIRE_ROOT}}", str(ROOT))
    return expanded


def wait_for_health(service: dict, defaults: dict) -> dict:
    retries = int(defaults.get("healthRetries", 12))
    delay = int(defaults.get("healthRetrySec", 1))
    timeout = int(defaults.get("healthTimeoutSec", 8))
    health = {"ok": False, "detail": "not checked"}
    for attempt in range(1, retries + 1):
        health = check_health(service["healthUrl"], timeout)
        if health["ok"]:
            return health
        if attempt < retries:
            time.sleep(delay)
    return health


def start_managed_service(name: str, config: dict) -> dict:
    service = config["services"][name]
    defaults = config["defaults"]

    if not service.get("managed"):
        health = wait_for_health(service, defaults)
        if not health["ok"]:
            return {"ok": False, "error": f"External service '{name}' unhealthy: {health['detail']}"}
        return {"ok": True, "stdout": f"[{name}] external service healthy"}

    port = int(service["port"])
    if port_listening(port):
        health = wait_for_health(service, defaults)
        if health["ok"]:
            return {"ok": True, "stdout": f"[{name}] already listening on port {port}"}
        return {"ok": False, "error": f"[{name}] port {port} in use but unhealthy: {health['detail']}"}

    start = service["start"]
    prepare = start.get("prepare")
    if prepare:
        prepare_result = subprocess.run(
            [
                resolve_executable(str(prepare["exe"])),
                *[str(item) for item in prepare.get("args", [])],
            ],
            cwd=str(resolve_path(str(prepare.get("cwd", ".")))),
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
        if prepare_result.returncode != 0:
            detail = prepare_result.stderr.strip() or prepare_result.stdout.strip()
            return {
                "ok": False,
                "error": f"[{name}] runtime preparation failed: {detail}",
            }
    exe = resolve_executable(start["exe"])
    cwd = str(resolve_path(start["cwd"]))
    args = [str(a) for a in start.get("args", [])]
    env = os.environ.copy()
    env.update(expand_env(start.get("env", {})))

    creationflags = 0
    if os.name == "nt" and start.get("hidden"):
        creationflags = subprocess.CREATE_NO_WINDOW  # type: ignore[attr-defined]

    subprocess.Popen(  # noqa: S603
        [exe, *args],
        cwd=cwd,
        env=env,
        creationflags=creationflags,
    )

    health = wait_for_health(service, defaults)
    if not health["ok"]:
        return {"ok": False, "error": f"[{name}] failed health check: {health['detail']}"}
    return {"ok": True, "stdout": f"[{name}] started on port {port}"}


def stop_managed_service(name: str, config: dict) -> dict:
    service = config["services"][name]
    defaults = config["defaults"]

    if not service.get("managed"):
        return {"ok": True, "stdout": f"[{name}] external - left running"}

    port = int(service["port"])
    pid = get_port_pid(port)
    if not pid:
        return {"ok": True, "stdout": f"[{name}] not running"}

    grace = int(defaults.get("stopGraceSec", 5))
    run_ps_command(f"Stop-Process -Id {pid} -ErrorAction SilentlyContinue")
    deadline = time.time() + grace
    while time.time() < deadline:
        if not get_port_pid(port):
            return {"ok": True, "stdout": f"[{name}] stopped pid {pid}"}
        time.sleep(0.4)

    run_ps_command(f"Stop-Process -Id {pid} -Force -ErrorAction SilentlyContinue")
    time.sleep(int(defaults.get("stopForceSec", 3)))
    return {"ok": True, "stdout": f"[{name}] forced stop pid {pid}"}


def roll_services(action: str, only: list[str] | None, config: dict) -> dict:
    order_key = "rollInOrder" if action == "start" else "rollOutOrder"
    order = config[order_key]
    if only:
        order = [name for name in order if name in only]

    lines: list[str] = []
    ok = True
    for name in order:
        if name not in config["services"]:
            continue
        if action == "start":
            result = start_managed_service(name, config)
        else:
            result = stop_managed_service(name, config)
        line = result.get("stdout") or result.get("error") or f"[{name}] done"
        lines.append(line)
        if not result.get("ok"):
            ok = False
            break

    return {"ok": ok, "stdout": "\n".join(lines), "stderr": "" if ok else lines[-1]}


class EmpireHTTPServer(ThreadingHTTPServer):
    """Frontend server that owns and cleanly drains its memory-job executor."""

    def __init__(
        self,
        server_address,
        request_handler_class,
        *,
        memory_runner: memory_api.MemoryJobRunner | None = None,
    ) -> None:
        self.memory_runner = memory_runner or memory_api.JOB_RUNNER
        super().__init__(server_address, request_handler_class)

    def server_close(self) -> None:
        try:
            super().server_close()
        finally:
            self.memory_runner.shutdown()


class EmpireHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND), **kwargs)

    def end_headers(self) -> None:
        path = urlparse(self.path).path
        origin = self.headers.get("Origin")
        local_only_api = (
            path.startswith("/api/memory/")
            or path.startswith("/api/projects/")
            or path.startswith("/api/eve/")
            or path.startswith("/api/ollama/")
            or path == "/api/gpu-lease"
            or path == "/api/toolbelt"
            or path == "/api/admission"
            or path.startswith("/api/voice/")
            or path.startswith("/api/lego/")
            or path.startswith("/api/daze/")
        )
        if local_only_api:
            if origin in MEMORY_ALLOWED_ORIGINS:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")
        else:
            self.send_header("Access-Control-Allow-Origin", "*")
        methods = "GET, POST, OPTIONS" if path.startswith("/api/eve/") else (
            "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        )
        self.send_header("Access-Control-Allow-Methods", methods)
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        if path.endswith((".html", ".js", ".css")) or path in {"/", "/eve.html"}:
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self) -> None:
        path = urlparse(self.path).path
        if (
            path.startswith("/api/memory/")
            or path.startswith("/api/projects/")
            or path.startswith("/api/eve/")
            or path.startswith("/api/ollama/")
            or path == "/api/gpu-lease"
            or path == "/api/toolbelt"
            or path == "/api/admission"
            or path.startswith("/api/voice/")
            or path.startswith("/api/chat-history")
            or path.startswith("/api/lego/")
            or path.startswith("/api/daze/")
        ) and not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        if path.startswith("/api/eve/"):
            requested_method = self.headers.get("Access-Control-Request-Method", "GET")
            try:
                eve_proxy.validate_eve_request(
                    requested_method,
                    self._eve_upstream_path(),
                )
            except eve_proxy.EveRequestError as exc:
                return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        self.send_response(204)
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/eve/"):
            return self._eve_proxy_request("GET")
        if path == "/api/ollama/models":
            return self._ollama_models()
        if path == "/api/ollama/inventory":
            return self._ollama_inventory()
        if path == "/api/ollama/fast-ab":
            return self._send_json(200, ollama_fast_ab.load_fast_ab())
        if path == "/api/gpu-lease":
            return self._gpu_lease_get()
        if path == "/api/admission":
            return self._admission_get()
        if path == "/api/resource-pulse":
            return self._send_json(200, dashboard_api.resource())
        if path == "/api/catalog":
            params = parse_qs(urlparse(self.path).query)
            payload = {key: (values[0] if values else "") for key, values in params.items()}
            return self._send_json(200, dashboard_api.catalog(payload))
        if path == "/api/workers/status":
            return self._send_json(200, dashboard_api.workers())
        if path.startswith("/api/lego/"):
            return self._lego_get(path)
        if path.startswith("/api/daze/"):
            return self._daze_api("GET")
        if path == "/api/toolbelt":
            active = eve_toolbelt.load_active_tools()
            return self._send_json(
                200,
                {
                    "ok": True,
                    "active_tools": active,
                    "voice_presence": "voice_presence" in active,
                },
            )
        if path == "/api/voice/health":
            try:
                from pipeline import voice_presence

                health = voice_presence.health()
            except Exception as exc:  # noqa: BLE001
                health = {"ok": False, "error": str(exc)}
            active = eve_toolbelt.load_active_tools()
            health = dict(health) if isinstance(health, dict) else {"ok": False}
            health["voice_presence_limb"] = "voice_presence" in active
            health["active_tools"] = active
            return self._send_json(200 if health.get("ok") else 503, health)
        if path == "/api/chat-history" or path.startswith("/api/chat-history/"):
            return self._chat_history_get(path)
        if path == "/api/memory/status":
            return self._memory_status()
        if path == "/api/projects/catalog":
            return self._projects_catalog_get()
        if path.startswith("/api/memory/jobs/"):
            return self._memory_job_get(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_get(path)
        if path == "/api/primitives/status":
            return self._primitives_get()
        if path == "/api/services/status":
            snapshot_path = FRONTEND / "dashboard-status.json"
            if not snapshot_path.exists() or snapshot_path.stat().st_size == 0:
                run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
            if snapshot_path.exists() and snapshot_path.stat().st_size > 0:
                try:
                    payload = json.loads(snapshot_path.read_text(encoding="utf-8-sig"))
                    return self._send_json(200, payload)
                except json.JSONDecodeError:
                    run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
                    try:
                        payload = json.loads(snapshot_path.read_text(encoding="utf-8-sig"))
                        return self._send_json(200, payload)
                    except json.JSONDecodeError:
                        pass
            return self._send_json(503, {"ok": False, "error": "Status snapshot missing or invalid"})
        if path == "/api/verify/stack":
            report_path = FRONTEND / "verify-stack.json"
            if report_path.exists() and report_path.stat().st_size > 0:
                try:
                    return self._send_json(200, json.loads(report_path.read_text(encoding="utf-8")))
                except json.JSONDecodeError:
                    pass
            return self._send_json(404, {"ok": False, "error": "No verification report yet"})
        if path.endswith(".html") and self._serve_html_with_cache_busting(path):
            return None
        return super().do_GET()

    def _serve_html_with_cache_busting(self, path: str) -> bool:
        """Serve an HTML page with asset query versions taken from file mtimes.

        Without this the Architect's browser keeps the cached `eve-workbench.js` after a fix —
        which is how an already-fixed UI (bubble doubling, spoken scratch) still looked broken.
        A normal refresh is then enough; no hard-refresh ritual.
        """

        if not path.endswith(".html"):
            return False
        target = (FRONTEND / path.lstrip("/")).resolve()
        try:
            target.relative_to(FRONTEND.resolve())
        except ValueError:
            return False
        if not target.is_file():
            return False
        try:
            html = target.read_text(encoding="utf-8")
        except OSError:
            return False

        def versioned(match: "re.Match[str]") -> str:
            name = match.group(1)
            asset = (FRONTEND / name.lstrip("/")).resolve()
            try:
                stamp = int(asset.stat().st_mtime)
            except OSError:
                return match.group(0)
            return f'{match.group(0)[: -len(name) - 1]}{name}?v={stamp}"'

        html = re.sub(r'"([A-Za-z0-9_./-]+\.(?:js|css))"', versioned, html)
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass
        return True

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/eve/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            payload = self._read_eve_json()
            if payload is None:
                return None
            payload = eve_toolbelt.apply_active_tools(payload)
            payload = ollama_api.apply_chat_mode_payload(payload)
            active_config = ollama_api.load_active_config()
            # One id per browser turn, minted before the first trace record so every later
            # record for this turn (tool latency, step events, stream end, ambient capture)
            # can be attributed to it. The agent session id only exists after the session
            # is created — never on the first turn — so `turn` is the join key and
            # `session` is attached whenever the request path already carries it.
            self._ambient_turn_id = uuid.uuid4().hex
            # The turn id must survive to the GET /stream request that carries the tool events.
            remember_turn(self._eve_session_id_from_path(), self._ambient_turn_id)
            trace_event(
                "turn.start",
                turn=self._ambient_turn_id,
                session=self._eve_session_id_from_path(),
                message=str(payload.get("message") or "")[:400],
                active_tools=payload.get("active_tools"),
                # Which model the agent was told to use — makes Fast A/B runs attributable
                # (cross-check with `ollama ps` for what is actually resident).
                model=str(active_config.get("model") or ""),
                mode=str(active_config.get("mode") or ""),
            )
            try:
                # Wikipedia retrieval is an autonomous MCP tool process (2026-09-23):
                # Eve owns intent/pronouns and calls empire-wiki-scout herself, so the
                # regex lookup gate must NOT run per turn. Only the explicit legacy
                # escape hatch (EMPIRE_WIKI_MIDDLEWARE=1) evaluates it.
                if wiki_drift_api.wiki_middleware_enabled():
                    raw_message = payload.get("message")
                    force_wiki = isinstance(raw_message, str) and wiki_drift_api.is_wiki_lookup_query(raw_message)
                    payload = wiki_drift_api.enrich_eve_message_payload(payload, force=force_wiki)
            except Exception:
                pass
            try:
                payload = resource_pulse_api.enrich_eve_message_payload(payload)
            except Exception:
                pass
            try:
                payload = companion_api.enrich_eve_message_payload(payload)
            except Exception:
                pass
            try:
                payload = memory_api.enrich_eve_message_payload(payload)
            except Exception:
                pass
            try:
                payload = chat_continuity.enrich_eve_message_payload(payload)
            except Exception:
                pass
            try:
                payload = workbench_ui_api.enrich_eve_message_payload(payload)
            except Exception:
                pass
            if isinstance(payload.get("message"), str):
                payload = dict(payload)
                original_message = payload["message"]
                # Context builders must never abort session creation: an escaping
                # exception closes the socket before any response is written.
                try:
                    catalog_context = asyncio.run(_catalog_context_async(original_message))
                except Exception:
                    catalog_context = ""
                try:
                    resource_context = _resource_guard_context(original_message)
                except Exception:
                    resource_context = ""
                try:
                    transfer_context = _transfer_context(original_message)
                except Exception:
                    transfer_context = ""
                # Place next to the ask, not above the companion preamble: the
                # model ignored a distant catalog block and called the wiki limb.
                payload["message"] = _attach_server_context(
                    original_message,
                    f"{catalog_context}{resource_context}{transfer_context}",
                )
            pending = payload.pop("_wiki_evidence", None)
            self._pending_wiki_evidence = pending if isinstance(pending, dict) else None
            # `_wiki_evidence` only exists on the legacy escape-hatch path
            # (EMPIRE_WIKI_MIDDLEWARE=1). Keep the re-format inside that boundary so
            # the autonomous path never rewrites Eve's message.
            if (
                self._pending_wiki_evidence
                and wiki_drift_api.wiki_middleware_enabled()
                and isinstance(payload.get("message"), str)
            ):
                message = str(payload["message"])
                if "[[EMPIRE_WIKI_LOOKUP]]" not in message and "[[EMPIRE_WIKI_EXTRACT]]" not in message:
                    try:
                        payload["message"] = wiki_drift_api._format_evidence_block(
                            self._pending_wiki_evidence,
                            user_question=message,
                        )
                    except Exception:
                        pass
            self._ambient_user_text = str(payload.get("message") or "")
            remember_user_text(self._eve_session_id_from_path(), self._ambient_user_text)
            return self._eve_proxy_request("POST", payload)
        if path.startswith("/api/memory/") and not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        if path == "/api/memory/recall":
            return self._memory_recall()
        if path == "/api/memory/answer":
            return self._memory_answer()
        if path == "/api/memory/optimize":
            return self._memory_optimize()
        if path == "/api/projects/catalog/refresh":
            return self._projects_catalog_refresh()
        if path == "/api/memory/upload":
            return self._memory_upload()
        if path == "/api/ollama/summarize-tasks":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._ollama_summarize_tasks()
        if path == "/api/ollama/fast-ab":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._ollama_fast_ab_set()
        if path == "/api/gpu-lease":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._gpu_lease_post()
        if path == "/api/admission":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._admission_post()
        if path.startswith("/api/lego/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._lego_post(path)
        if path.startswith("/api/daze/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._daze_api("POST")
        if path == "/api/voice/transcribe":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._voice_transcribe()
        if path == "/api/voice/speak":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._voice_speak()
        if path == "/api/toolbelt":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            payload = self._read_json()
            if not isinstance(payload, dict):
                return self._send_json(400, {"ok": False, "error": "JSON object required"})
            active = eve_toolbelt.normalize_active_tools(payload.get("active_tools"))
            path_written = eve_toolbelt.write_active_tools(active)
            return self._send_json(
                200,
                {
                    "ok": True,
                    "active_tools": active,
                    "voice_presence": "voice_presence" in active,
                    "path": str(path_written),
                },
            )
        if path.startswith("/api/memory/jobs/") and path.endswith("/retry"):
            return self._memory_retry(path)
        payload = self._read_json()

        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("POST", path, payload)

        if path == "/api/primitives/ingest":
            return self._primitives_ingest(payload)

        if path == "/api/services/refresh":
            result = run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
            return self._finish_control(result)

        if path == "/api/verify/stack":
            return self._run_verify_stack(payload)

        if path == "/api/services/start":
            return self._service_action("start", payload)

        if path == "/api/services/stop":
            return self._service_action("stop", payload)

        self.send_error(404)

    def _memory_origin_allowed(self) -> bool:
        origin = self.headers.get("Origin")
        return origin is None or origin in MEMORY_ALLOWED_ORIGINS

    def _eve_upstream_path(self) -> str:
        parsed = urlparse(self.path)
        upstream = "/eve/v1/" + parsed.path[len("/api/eve/") :]
        return upstream + (f"?{parsed.query}" if parsed.query else "")

    def _eve_session_id_from_path(self) -> str:
        parsed = urlparse(self.path)
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) >= 4 and parts[1] == "eve" and parts[2] == "session":
            return parts[3]
        return ""

    def _read_eve_json(self) -> dict | None:
        raw_length = self.headers.get("Content-Length", "0")
        try:
            length = int(raw_length)
        except ValueError:
            self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
            return None
        if length < 0 or length > 1024 * 1024:
            status = 413 if length > 1024 * 1024 else 400
            self._send_json(status, {"ok": False, "error": "Invalid Eve request size."})
            return None
        if not length:
            return {}
        content_type = self.headers.get("Content-Type", "")
        if not content_type.casefold().startswith("application/json"):
            self._send_json(415, {"ok": False, "error": "Eve requests require application/json."})
            return None
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"ok": False, "error": "Invalid JSON body."})
            return None
        if not isinstance(payload, dict):
            self._send_json(400, {"ok": False, "error": "Expected a JSON object."})
            return None
        return payload

    def _eve_proxy_request(self, method: str, payload: dict | None = None) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        upstream_path = self._eve_upstream_path()
        try:
            response = eve_proxy.eve_request(method, upstream_path, payload)
        except eve_proxy.EveRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except eve_proxy.EveConnectionError:
            return self._send_json(502, {"ok": False, "error": "Eve is unavailable."})

        if response.is_stream:
            self.send_response(response.status)
            self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            return self._write_eve_stream(
                response,
                eve_proxy.stream_start_index(upstream_path),
                session_id=self._eve_session_id_from_path(),
                turn_id=getattr(self, "_ambient_turn_id", ""),
            )

        try:
            body = response.body
            # A *new* session has no id in the request path; the response carries it, so map it here
            # (the browser then streams from `/api/eve/session/<id>/stream`, a separate request).
            if body:
                try:
                    created = json.loads(body.decode("utf-8"))
                except (UnicodeDecodeError, json.JSONDecodeError, TypeError):
                    created = {}
                if isinstance(created, dict):
                    created_session = str(created.get("sessionId") or "")
                    if created_session:
                        remember_turn(created_session, getattr(self, "_ambient_turn_id", ""))
                        remember_user_text(
                            created_session, getattr(self, "_ambient_user_text", "")
                        )
            pending = getattr(self, "_pending_wiki_evidence", None)
            if pending and body:
                try:
                    created = json.loads(body.decode("utf-8"))
                    session_id = str(created.get("sessionId") or "")
                    if session_id:
                        wiki_drift_api.register_wiki_evidence(session_id, pending)
                except (UnicodeDecodeError, json.JSONDecodeError, TypeError):
                    pass
            self._pending_wiki_evidence = None
            self.send_response(response.status)
            for name, value in response.headers.items():
                self.send_header(name, value)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            return None
        finally:
            response.close()

    def _apply_wiki_grounding_event(
        self,
        projected: dict,
        *,
        session_id: str,
    ) -> dict:
        if not session_id:
            return projected
        event_type = str(projected.get("type") or "")
        if event_type == "session.waiting":
            wiki_drift_api.pop_wiki_evidence(session_id)
            return projected
        evidence = wiki_drift_api.get_wiki_evidence(session_id)
        if not evidence or event_type not in {"message.completed", "message.appended"}:
            return projected
        data = projected.get("data")
        if not isinstance(data, dict):
            return projected
        try:
            from pipeline.wiki_grounding_guard import apply_grounding_guard
        except Exception:
            return projected
        user_question = str(evidence.get("user_question") or "")
        patched = dict(data)
        for key in ("message", "messageSoFar", "text", "content"):
            value = patched.get(key)
            if isinstance(value, str) and value.strip():
                patched[key] = apply_grounding_guard(
                    value,
                    evidence,
                    user_question=user_question,
                )
        updated = dict(projected)
        updated["data"] = patched
        return updated

    def _write_eve_stream(
        self,
        response: eve_proxy.EveResponse,
        upstream_next_index: int = 0,
        *,
        session_id: str = "",
        turn_id: str = "",
    ) -> None:
        # `turn_id` is the caller's, else the turn the session is currently on (the POST that
        # started it is a *different handler instance* — see `remember_turn`), else this
        # request's own id. All three must agree so trace records and ambient capture join
        # on one id.
        turn_id = turn_id or turn_for_session(session_id) or getattr(self, "_ambient_turn_id", "")
        client_connected = True
        assistant_text = ""
        qwen_start = time.perf_counter()
        # Per-step stateful reasoning filter: a `<thought>` block's deltas carry no tag, so
        # stateless stripping per event would leak the block body to the browser (and to TTS).
        reasoning_filters: dict = {}
        tool_started: float | None = None
        stream_started = time.perf_counter()
        try:
            if response.stream is None:
                return
            for event in eve_proxy.iter_ndjson_records(response.stream):
                upstream_next_index += 1
                if event is None:
                    continue
                projected = eve_proxy.project_event(event)
                if projected is None:
                    continue
                projected = self._apply_wiki_grounding_event(
                    projected,
                    session_id=session_id,
                )
                projected = eve_proxy.filter_stream_event(projected, reasoning_filters)
                event_type = str(projected.get("type") or "")
                data = projected.get("data")
                if event_type == "actions.requested":
                    requested = [
                        str((action or {}).get("toolName") or "")
                        for action in (data.get("actions") if isinstance(data, dict) else []) or []
                        if isinstance(action, dict)
                    ]
                    trace_event(
                        "tool.requested",
                        tools=requested,
                        turn=turn_id,
                        session=session_id,
                    )
                    tool_started = time.perf_counter()
                elif event_type == "action.result" and tool_started is not None:
                    trace_event(
                        "tool.result",
                        ms=round((time.perf_counter() - tool_started) * 1000, 1),
                        turn=turn_id,
                        session=session_id,
                    )
                    tool_started = None
                elif event_type in {
                    "step.started",
                    "step.completed",
                    "turn.started",
                    "turn.completed",
                    "session.waiting",
                }:
                    trace_event(
                        "event",
                        type=event_type,
                        step=(data or {}).get("stepIndex") if isinstance(data, dict) else None,
                        turn=turn_id,
                        session=session_id,
                    )
                elif event_type in {"message.appended", "message.completed"} and isinstance(data, dict):
                    chunk = data.get("messageSoFar") or data.get("message") or data.get("messageDelta")
                    trace_event(
                        "message",
                        type=event_type,
                        step=data.get("stepIndex"),
                        chars=len(chunk) if isinstance(chunk, str) else 0,
                        turn=turn_id,
                        session=session_id,
                    )
                data = projected.get("data")
                if isinstance(data, dict):
                    cumulative = data.get("messageSoFar") or data.get("message")
                    if isinstance(cumulative, str) and cumulative.strip():
                        assistant_text = cumulative
                if event_type == "message.completed" and assistant_text:
                    qwen_time = time.perf_counter() - qwen_start
                    if VOICE_ROUTER_ENABLED:
                        assistant_text, voice_time, used_fallback = asyncio.run(
                            _voice_router(assistant_text)
                        )
                    else:
                        voice_time, used_fallback = 0.0, False
                    print(
                        f"[TRACER] Qwen Generation: {qwen_time:.2f}s | "
                        f"Llama Voice Styling: {voice_time:.2f}s | "
                        f"Total: {(qwen_time + voice_time):.2f}s | "
                        f"Fallback Used: {used_fallback}",
                        flush=True,
                    )
                    trace_event(
                        "voice_router",
                        qwen_s=round(qwen_time, 2),
                        voice_s=round(voice_time, 2),
                        total_s=round(qwen_time + voice_time, 2),
                        fallback=used_fallback,
                        turn=turn_id,
                        session=session_id,
                    )
                    if isinstance(data, dict):
                        data = dict(data)
                        for key in ("message", "messageSoFar", "text", "content"):
                            if isinstance(data.get(key), str):
                                data[key] = assistant_text
                        projected = dict(projected)
                        projected["data"] = data
                    _append_ambient_event(
                        role="user",
                        text=getattr(self, "_ambient_user_text", "") or user_text_for_session(session_id),
                        status="completed",
                        session_id=session_id,
                        turn_id=turn_id,
                    )
                    try:
                        from pipeline.wiki_lookup_lock import clear_wiki_lookup_lock

                        clear_wiki_lookup_lock()
                    except Exception:
                        pass
                    _append_ambient_event(
                        role="assistant",
                        text=assistant_text,
                        status="completed",
                        session_id=session_id,
                        turn_id=turn_id,
                    )
                projected = eve_proxy.with_upstream_next_index(
                    projected,
                    upstream_next_index,
                )
                line = json.dumps(projected, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
                self.wfile.write(line + b"\n")
                self.wfile.flush()
        except BrokenPipeError:
            client_connected = False
        except (OSError, TimeoutError):
            if client_connected:
                try:
                    line = json.dumps(
                        eve_proxy.PROXY_ERROR_EVENT,
                        separators=(",", ":"),
                    ).encode("utf-8")
                    self.wfile.write(line + b"\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, OSError):
                    pass
        finally:
            trace_event(
                "stream.end",
                seconds=round(time.perf_counter() - stream_started, 2),
                turn=turn_id,
                session=session_id,
            )
            response.close()

    def _memory_recall(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        if content_length <= 0:
            return self._send_json(400, {"ok": False, "error": "Request body is required."})
        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON body must be an object."})
        query = str(payload.get("query") or "").strip()
        if not query:
            return self._send_json(400, {"ok": False, "error": "Query is required."})
        dataset = str(payload.get("dataset") or memory_api.DEFAULT_CHAT_RECALL_DATASET)
        try:
            result = memory_api.recall_for_chat(query, dataset=dataset)
        except ValueError as exc:
            return self._send_json(400, {"ok": False, "error": str(exc)})
        if not result.get("ok"):
            return self._send_json(503, result)
        return self._send_json(
            200,
            {
                "ok": True,
                "query": result.get("query"),
                "dataset": result.get("dataset"),
                "chunkCount": result.get("chunkCount", 0),
                "contextBlock": result.get("contextBlock", ""),
            },
        )

    def _memory_answer(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        if content_length <= 0:
            return self._send_json(400, {"ok": False, "error": "Request body is required."})
        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON body must be an object."})
        query = str(payload.get("query") or "").strip()
        if not query:
            return self._send_json(400, {"ok": False, "error": "Query is required."})
        fast = bool(payload.get("fast"))
        result = memory_api.answer_memory_chat(query, fast=fast)
        if not result.get("ok"):
            return self._send_json(503, result)
        return self._send_json(
            200,
            {
                "ok": True,
                "answer": result.get("answer", ""),
                "chunkCount": result.get("chunkCount", 0),
                "model": result.get("model"),
                "sources": result.get("sources") or [],
            },
        )

    def _memory_optimize(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            content_length = 0
        payload: dict[str, object] = {}
        if content_length > 0:
            try:
                body = self.rfile.read(content_length)
                parsed = json.loads(body.decode("utf-8"))
                if isinstance(parsed, dict):
                    payload = parsed
            except (UnicodeDecodeError, json.JSONDecodeError):
                return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        max_files = payload.get("maxFiles", 60)
        fresh = bool(payload.get("fresh"))
        try:
            max_files_int = int(max_files)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            max_files_int = 60
        try:
            result = memory_api.run_optimize_eve_core(
                max_files=max_files_int,
                fresh=fresh,
            )
        except RuntimeError as exc:
            return self._send_json(503, {"ok": False, "error": str(exc)})
        return self._send_json(200, result)

    def _projects_catalog_get(self) -> None:
        rebuild = urlparse(self.path).query.find("rebuild=1") >= 0
        catalog = project_catalog.load_project_catalog(rebuild=rebuild)
        projects = [
            project_catalog.public_project(item)
            for item in catalog.get("projects", [])
            if isinstance(item, dict)
        ]
        return self._send_json(
            200,
            {
                "ok": True,
                "generatedAt": catalog.get("generated_at"),
                "projectCount": catalog.get("project_count", len(projects)),
                "inEveCoreCount": catalog.get("in_eve_core_count"),
                "flattenedCount": catalog.get("flattened_count"),
                "projects": projects,
            },
        )

    def _projects_catalog_refresh(self) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        catalog = project_catalog.save_project_catalog()
        projects = [
            project_catalog.public_project(item)
            for item in catalog.get("projects", [])
            if isinstance(item, dict)
        ]
        return self._send_json(
            200,
            {
                "ok": True,
                "generatedAt": catalog.get("generated_at"),
                "projectCount": len(projects),
                "projects": projects,
            },
        )

    def _memory_status(self) -> None:
        jobs = [memory_api.public_job(job) for job in memory_api.JOB_STORE.list()]
        return self._send_json(
            200,
            {
                "ok": True,
                "readiness": memory_api.memory_readiness(),
                "statuses": memory_api.STATUS_LABELS,
                "config": memory_api.memory_stack_config(),
                "eveCore": memory_api.eve_core_status(),
                "jobs": jobs,
            },
        )

    def _memory_job_get(self, path: str) -> None:
        job_id = path[len("/api/memory/jobs/") :].strip("/")
        if not job_id or "/" in job_id:
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            job = memory_api.JOB_STORE.read(job_id)
        except (KeyError, ValueError):
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        return self._send_json(200, {"ok": True, "job": memory_api.public_job(job)})

    def _memory_upload(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        try:
            memory_api.DEFAULT_UPLOAD_POLICY.validate_request_size(content_length)
        except ValueError as exc:
            status = 413 if content_length > memory_api.DEFAULT_UPLOAD_POLICY.max_request_bytes else 400
            return self._send_json(status, {"ok": False, "error": str(exc)})

        content_type = self.headers.get("Content-Type", "")
        if not content_type.casefold().startswith("multipart/form-data"):
            return self._send_json(
                415,
                {"ok": False, "error": "Memory uploads require multipart/form-data."},
            )
        if "\r" in content_type or "\n" in content_type:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Type."})

        try:
            body = self.rfile.read(content_length)
            synthetic = (
                f"Content-Type: {content_type}\r\n"
                "MIME-Version: 1.0\r\n"
                "\r\n"
            ).encode("ascii", errors="strict")
            message = BytesParser(policy=policy.default).parsebytes(synthetic + body)
            if not message.is_multipart():
                raise ValueError("Malformed multipart upload.")
            parts = []
            fields: dict[str, str] = {}
            for part in message.iter_parts():
                disposition = part.get_content_disposition()
                if disposition != "form-data":
                    continue
                filename = part.get_filename()
                field_name = part.get_param("name", header="content-disposition")
                if filename is not None:
                    parts.append(part)
                elif field_name:
                    content = part.get_payload(decode=True) or b""
                    fields[str(field_name)] = content.decode(
                        part.get_content_charset() or "utf-8",
                        errors="strict",
                    )
            dataset = fields.get("dataset", "eve_memory").strip() or "eve_memory"
            full_graph_value = fields.get("full_graph", "false").strip().casefold()
            if full_graph_value not in {"true", "false", "1", "0", "yes", "no"}:
                raise ValueError("full_graph must be true or false.")
            full_graph = full_graph_value in {"true", "1", "yes"}
        except (UnicodeError, ValueError) as exc:
            message_text = str(exc)
            status = 413 if "too large" in message_text.casefold() or "exceeds" in message_text.casefold() else 400
            return self._send_json(status, {"ok": False, "error": message_text})
        except Exception:
            return self._send_json(
                400,
                {"ok": False, "error": "Could not parse multipart upload."},
            )

        try:
            job = memory_api.save_uploads(parts, dataset, full_graph)
        except memory_api.MemoryJobQueueError:
            return self._send_json(
                503,
                {"ok": False, "error": "Memory job queue is unavailable."},
            )
        except memory_api.MemoryUploadStorageError:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not save memory upload."},
            )
        except ValueError as exc:
            message_text = str(exc)
            status = 413 if "too large" in message_text.casefold() or "exceeds" in message_text.casefold() else 400
            return self._send_json(status, {"ok": False, "error": message_text})
        except Exception:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not save memory upload."},
            )
        return self._send_json(
            202,
            {"ok": True, "job": memory_api.public_job(job)},
        )

    def _memory_retry(self, path: str) -> None:
        prefix = "/api/memory/jobs/"
        job_id = path[len(prefix) : -len("/retry")].strip("/")
        if not job_id or "/" in job_id:
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            memory_api.JOB_STORE.read(job_id)
        except (KeyError, ValueError):
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            memory_api.JOB_RUNNER.retry(job_id)
        except ValueError as exc:
            return self._send_json(409, {"ok": False, "error": str(exc)})
        except memory_api.MemoryJobQueueError:
            return self._send_json(
                503,
                {"ok": False, "error": "Memory job queue is unavailable."},
            )
        except Exception:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not retry memory job."},
            )
        job = memory_api.JOB_STORE.read(job_id)
        return self._send_json(
            202,
            {"ok": True, "job": memory_api.public_job(job)},
        )

    def do_PUT(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/ollama/model":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._ollama_set_model()
        if path.startswith("/api/lego/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._lego_put(path)
        if path.startswith("/api/chat-history/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._chat_history_put(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("PUT", path, self._read_json())
        self.send_error(404)

    def _ollama_models(self) -> None:
        try:
            tags = ollama_api.fetch_tags()
        except ollama_api.OllamaConnectionError:
            return self._send_json(
                503,
                ollama_api.models_status(
                    None,
                    connected=False,
                    error="Ollama is unavailable.",
                ),
            )
        payload = ollama_api.models_status(tags, connected=True)
        payload["inventory"] = ollama_inventory.build_inventory(tags)
        return self._send_json(200, payload)

    def _ollama_inventory(self) -> None:
        try:
            tags = ollama_api.fetch_tags()
        except ollama_api.OllamaConnectionError as exc:
            return self._send_json(
                503,
                {
                    "ok": False,
                    "connected": False,
                    "error": str(exc),
                    "fastAb": ollama_fast_ab.load_fast_ab(),
                },
            )
        payload = ollama_inventory.build_inventory(tags)
        if isinstance(payload, dict):
            payload = dict(payload)
            payload["fastAb"] = ollama_fast_ab.load_fast_ab()
            payload["ok"] = True
            payload["connected"] = True
            # Loopback harden note for Architect
            payload["ollamaClientHint"] = (
                "Clients must use http://127.0.0.1:11434 — never 0.0.0.0 as a client URL."
            )
        return self._send_json(200, payload)

    def _ollama_fast_ab_set(self) -> None:
        payload = self._read_json()
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON object required"})
        result = ollama_fast_ab.save_fast_ab(
            variant=str(payload.get("variant") or "") or None,
            b_model=str(payload.get("b_model") or "") or None,
        )
        status = 200 if result.get("ok") else 400
        # Sync active Fast model when mode is fast
        if result.get("ok"):
            try:
                active = ollama_api.load_active_config()
                if str(active.get("mode")) == "fast":
                    ollama_api.save_active_config(
                        mode="fast",
                        model=str(result.get("active_model")),
                    )
            except OSError:
                pass
        return self._send_json(status, result)

    def _gpu_lease_get(self) -> None:
        try:
            from pipeline import gpu_lease

            return self._send_json(200, gpu_lease.status())
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})

    def _admission_get(self) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        try:
            from pipeline import admission_controller

            return self._send_json(200, admission_controller.status())
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})

    def _admission_post(self) -> None:
        payload = self._read_json()
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON object required"})
        try:
            from pipeline import admission_controller

            result = admission_controller.handle_api_action(payload)
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})
        status = 200 if result.get("ok") else 400
        return self._send_json(status, result)

    def _daze_api(self, method: str) -> None:
        try:
            from frontend import daze_api
        except ModuleNotFoundError:
            import daze_api  # type: ignore[no-redef]
        payload: dict | None = None
        if method in {"POST", "DELETE"}:
            raw_length = self.headers.get("Content-Length", "0")
            try:
                length = int(raw_length)
            except ValueError:
                length = 0
            if length > 0:
                payload = self._read_json()
                if payload is not None and not isinstance(payload, dict):
                    return self._send_json(400, {"ok": False, "error": "JSON object required"})
        try:
            status, result = daze_api.handle_api(method, self.path, payload)
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})
        return self._send_json(status, result)

    def _lego_get(self, path: str) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        if path == "/api/lego/bricks":
            return self._send_json(200, lego_api.load_bricks())
        if path == "/api/lego/recipes":
            return self._send_json(200, lego_api.load_recipes())
        if path == "/api/lego/board":
            return self._send_json(200, lego_api.load_board())
        return self._send_json(404, {"ok": False, "error": "Unknown lego route"})

    def _lego_put(self, path: str) -> None:
        if path != "/api/lego/board":
            return self._send_json(404, {"ok": False, "error": "Unknown lego route"})
        payload = self._read_json()
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON object required"})
        result = lego_api.save_board(payload)
        status = 200 if result.get("ok") else 400
        return self._send_json(status, result)

    def _lego_post(self, path: str) -> None:
        payload = self._read_json()
        body = payload if isinstance(payload, dict) else {}
        if path == "/api/lego/apply-toolbelt":
            result = lego_api.apply_toolbelt_from_board(body)
            status = 200 if result.get("ok") else 400
            return self._send_json(status, result)
        if path == "/api/lego/validate":
            result = lego_api.validate_board(body)
            status = 200 if result.get("ok") else 400
            return self._send_json(status, result)
        if path == "/api/lego/recipe":
            recipe_id = str(body.get("id") or body.get("recipe_id") or "").strip()
            if not recipe_id:
                return self._send_json(400, {"ok": False, "error": "recipe id required"})
            result = lego_api.instantiate_recipe(recipe_id)
            status = 200 if result.get("ok") else 400
            return self._send_json(status, result)
        return self._send_json(404, {"ok": False, "error": "Unknown lego route"})

    def _gpu_lease_post(self) -> None:
        payload = self._read_json()
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON object required"})
        try:
            from pipeline import gpu_lease

            action = str(payload.get("action") or "status").strip().lower()
            if action == "release":
                return self._send_json(200, gpu_lease.release())
            if action == "acquire":
                tenant = str(payload.get("tenant") or "").strip()
                return self._send_json(
                    200,
                    gpu_lease.acquire(
                        tenant,  # type: ignore[arg-type]
                        holder=str(payload.get("holder") or ""),
                        force=bool(payload.get("force")),
                    ),
                )
            return self._send_json(200, gpu_lease.status())
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})

    def _voice_transcribe(self) -> None:
        """Accept multipart audio upload, write temp file, call speech API."""
        try:
            from pipeline import voice_presence
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})

        content_type = self.headers.get("Content-Type", "")
        if "multipart/form-data" not in content_type:
            return self._send_json(400, {"ok": False, "error": "multipart/form-data required"})
        try:
            length = int(self.headers.get("Content-Length") or "0")
        except ValueError:
            length = 0
        if length <= 0 or length > 25_000_000:
            return self._send_json(400, {"ok": False, "error": "Invalid audio size"})
        raw = self.rfile.read(length)
        # Reuse email parser like memory upload
        header_bytes = f"Content-Type: {content_type}\r\n\r\n".encode("utf-8")
        msg = BytesParser(policy=policy.default).parsebytes(header_bytes + raw)
        audio_bytes = None
        filename = "upload.webm"
        for part in msg.iter_parts():
            name = part.get_param("name", header="content-disposition")
            if name == "file":
                audio_bytes = part.get_payload(decode=True)
                filename = part.get_filename() or filename
                break
        if not audio_bytes:
            return self._send_json(400, {"ok": False, "error": "file field required"})
        tmp_dir = Path(os.environ.get("TEMP") or FRONTEND) / "empire-voice"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = tmp_dir / f"mic-{int(time.time() * 1000)}-{filename}"
        try:
            tmp_path.write_bytes(audio_bytes)
            result = voice_presence.transcribe(tmp_path)
        finally:
            try:
                tmp_path.unlink(missing_ok=True)
            except OSError:
                pass
        status = 200 if result.get("ok") else 502
        return self._send_json(status, result)

    def _voice_speak(self) -> None:
        """Synthesize short TTS audio (mp3) when Voice Presence limb is on."""
        if not eve_toolbelt.category_enabled("voice_presence"):
            return self._send_json(
                403,
                {
                    "ok": False,
                    "error": "Enable Toolbelt → Voice Presence to hear Eve speak.",
                },
            )
        payload = self._read_json()
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON object required"})
        text = str(payload.get("text") or "").strip()
        if not text:
            return self._send_json(400, {"ok": False, "error": "text required"})
        # Cap length so replies stay snappy
        if len(text) > 2500:
            text = text[:2500].rstrip() + "…"
        try:
            from pipeline import voice_presence
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})

        tmp_dir = Path(os.environ.get("TEMP") or FRONTEND) / "empire-voice"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        tmp_path = tmp_dir / f"speak-{int(time.time() * 1000)}.mp3"
        try:
            result = voice_presence.speak(text, out_path=tmp_path)
            if not result.get("ok"):
                return self._send_json(502, result)
            audio = tmp_path.read_bytes()
        except Exception as exc:  # noqa: BLE001
            return self._send_json(500, {"ok": False, "error": str(exc)})
        finally:
            try:
                tmp_path.unlink(missing_ok=True)
            except OSError:
                pass
        if not audio:
            return self._send_json(502, {"ok": False, "error": "empty TTS audio"})
        self.send_response(200)
        self.send_header("Content-Type", "audio/mpeg")
        self.send_header("Content-Length", str(len(audio)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(audio)

    def _ollama_set_model(self) -> None:
        payload = self._read_json()
        try:
            tags = ollama_api.fetch_tags()
            mode = payload.get("mode")
            if isinstance(mode, str) and mode.strip():
                result = ollama_api.set_active_model("", tags, mode=mode.strip())
            else:
                result = ollama_api.set_active_model(str(payload.get("model") or ""), tags)
        except ollama_api.OllamaConnectionError:
            return self._send_json(503, {"ok": False, "error": "Ollama is unavailable."})
        except ollama_api.OllamaRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        result["inventory"] = ollama_inventory.build_inventory(tags)
        return self._send_json(200, result)

    def _ollama_summarize_tasks(self) -> None:
        payload = self._read_json()
        tasks = payload.get("tasks") if isinstance(payload, dict) else None
        if not isinstance(tasks, list):
            tasks = []
        model = str(payload.get("model") or "").strip() if isinstance(payload, dict) else ""
        try:
            result = ollama_api.summarize_tasks(tasks, model=model or None)
        except ollama_api.OllamaConnectionError:
            return self._send_json(
                503,
                {"ok": False, "error": "Ollama could not summarize tasks."},
            )
        except ollama_api.OllamaRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        return self._send_json(200, result)

    def do_PATCH(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("PATCH", path, self._read_json())
        self.send_error(404)

    def do_DELETE(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/chat-history/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._chat_history_delete(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("DELETE", path, {})
        if path.startswith("/api/daze/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._daze_api("DELETE")
        self.send_error(404)

    def _chat_history_get(self, path: str) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        try:
            if path == "/api/chat-history":
                return self._send_json(200, chat_history.public_list())
            chat_id = path[len("/api/chat-history/") :].strip("/")
            if not chat_id or "/" in chat_id:
                return self._send_json(404, {"ok": False, "error": "Chat not found."})
            if chat_id == "active":
                active_id = chat_history.get_active_chat_id()
                return self._send_json(200, {"ok": True, "activeId": active_id})
            chat = chat_history.get_chat(chat_id)
            return self._send_json(200, {"ok": True, "chat": chat})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not load chat history."})

    def _chat_history_put(self, path: str) -> None:
        chat_id = path[len("/api/chat-history/") :].strip("/")
        if not chat_id or "/" in chat_id:
            return self._send_json(404, {"ok": False, "error": "Chat not found."})
        payload = self._read_json()
        try:
            chat = chat_history.upsert_chat(chat_id, payload)
            return self._send_json(200, {"ok": True, "chat": chat})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not save chat history."})

    def _chat_history_delete(self, path: str) -> None:
        chat_id = path[len("/api/chat-history/") :].strip("/")
        if not chat_id or "/" in chat_id:
            return self._send_json(404, {"ok": False, "error": "Chat not found."})
        try:
            if chat_id == "active":
                chat_history.clear_active_chat_id()
                return self._send_json(200, {"ok": True, "activeId": None})
            chat_history.delete_chat(chat_id)
            return self._send_json(200, {"ok": True, "id": chat_id})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not delete chat."})

    def _primitives_get(self) -> None:
        try:
            return self._send_json(200, primitives_api.primitives_status())
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _primitives_ingest(self, payload: dict) -> None:
        try:
            skip = bool(payload.get("skip_cognify"))
            return self._send_json(
                200,
                primitives_api.primitives_run_ingest(skip_cognify=skip),
            )
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _wiki_get(self, path: str) -> None:
        try:
            qs = wiki_api.parse_query(self.path)
            year_q = qs.get("year") or []
            year = year_q[0] if year_q else "2017"
            if path == "/api/wiki/status":
                return self._send_json(200, wiki_api.wiki_status(year))
            if path == "/api/wiki/glasses-health":
                glasses_year = year_q[0] if year_q else None
                return self._send_json(200, wiki_api.wiki_glasses_health(glasses_year))
            if path == "/api/wiki/titles":
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                q = (qs.get("q") or [""])[0]
                return self._send_json(
                    200,
                    wiki_api.wiki_titles(year, q=q, offset=offset, limit=limit),
                )
            if path == "/api/wiki/titles/letters":
                return self._send_json(200, wiki_api.wiki_letters(year))
            if path == "/api/wiki/titles/by-letter":
                letter = (qs.get("letter") or ["A"])[0]
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                q = (qs.get("q") or [""])[0]
                only_missing_raw = (qs.get("only_missing") or ["1"])[0].strip().lower()
                only_missing = only_missing_raw not in ("0", "false", "no")
                return self._send_json(
                    200,
                    wiki_api.wiki_titles_by_letter(
                        year,
                        letter,
                        offset=offset,
                        limit=limit,
                        q=q,
                        only_missing=only_missing,
                    ),
                )
            if path == "/api/wiki/new-titles":
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                return self._send_json(
                    200,
                    wiki_api.wiki_new_titles(year, offset=offset, limit=limit),
                )
            if path == "/api/wiki/priorities":
                return self._send_json(200, wiki_api.wiki_priorities_get())
            return self._send_json(404, {"ok": False, "error": "Unknown wiki route"})
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _wiki_mutate(self, method: str, path: str, payload: dict) -> None:
        try:
            if path == "/api/wiki/priorities" and method == "PUT":
                return self._send_json(200, wiki_api.wiki_priorities_put(payload))
            if path == "/api/wiki/priorities" and method == "POST":
                return self._send_json(200, wiki_api.wiki_priorities_post(payload))
            if path == "/api/wiki/priorities/confirm" and method == "POST":
                return self._send_json(200, wiki_api.wiki_priorities_confirm(payload))
            if path == "/api/wiki/titles/queue" and method == "POST":
                return self._send_json(200, wiki_api.wiki_queue_articles(payload))
            if path.startswith("/api/wiki/priorities/") and method in ("PATCH", "DELETE"):
                subject_id = path[len("/api/wiki/priorities/") :].strip("/")
                if not subject_id or subject_id == "confirm":
                    return self._send_json(404, {"ok": False, "error": "Missing subject id"})
                if method == "PATCH":
                    return self._send_json(
                        200,
                        wiki_api.wiki_priorities_patch(subject_id, payload),
                    )
                return self._send_json(200, wiki_api.wiki_priorities_delete(subject_id))
            return self._send_json(404, {"ok": False, "error": "Unknown wiki route"})
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length).decode("utf-8"))
        except json.JSONDecodeError:
            return {}

    def _run_verify_stack(self, payload: dict) -> None:
        python = ROOT / "venv" / "Scripts" / "python.exe"
        script = ROOT / "scripts" / "verify-stack.py"
        cmd = [str(python), str(script), "--json"]
        if payload.get("skipCognee"):
            cmd.append("--skip-cognee")
        if payload.get("fullIngest"):
            cmd.append("--full-ingest")
        result = subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=360,
        )
        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError:
            report = {
                "ok": False,
                "error": result.stderr.strip() or result.stdout.strip() or "verify-stack failed",
            }
        status = 200 if report.get("ok") else 500
        self._send_json(status, report)

    def _service_action(self, action: str, payload: dict) -> None:
        service = payload.get("service")
        services = payload.get("services") or ([] if not service else [service])

        if action == "stop" and "frontend" in services:
            return self._send_json(
                400,
                {
                    "ok": False,
                    "error": "Stopping the Tasks UI from the dashboard would shut down this page.",
                },
            )

        if action == "start" and payload.get("all"):
            services = []

        if action == "stop" and payload.get("all"):
            services = []

        config = load_config()
        if action == "start" and payload.get("all"):
            if not payload.get("skipOllamaCheck"):
                ollama = config["services"]["ollama"]
                health = wait_for_health(ollama, config["defaults"])
                if not health["ok"]:
                    return self._send_json(
                        500,
                        {"ok": False, "error": f"Ollama is not healthy: {health['detail']}"},
                    )
            result = roll_services("start", None, config)
            return self._finish_control(result)

        if action == "stop" and payload.get("all"):
            result = roll_services("stop", None, config)
            return self._finish_control(result)

        if not services:
            return self._send_json(400, {"ok": False, "error": "Missing service or services"})

        result = roll_services(action, services, config)
        return self._finish_control(result)

    def _finish_control(self, result: dict) -> None:
        refresh = run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
        status = 200 if result.get("ok") else 500
        result["refresh"] = refresh
        self._send_json(status, result)

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        request = args[0] if args else ""
        if str(request).startswith("GET /api/") or str(request).startswith("POST /api/"):
            super().log_message(format, *args)


def main() -> int:
    server = EmpireHTTPServer((HOST, PORT), EmpireHandler)
    print(f"EMPIRE frontend + control API: http://{HOST}:{PORT}/")
    print(f"Dashboard: http://{HOST}:{PORT}/dashboard.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        return 0
    finally:
        server.server_close()


if __name__ == "__main__":
    sys.exit(main())
