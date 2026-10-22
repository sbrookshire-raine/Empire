"""Prompt-budget measurement (refactor plan R-01/R-03).

One source of truth for "what does the model pay for before the user speaks": the always-on
instruction files and the tool-schema prose of the default-enabled Toolbelt set. Used by
`scripts/measure-prompt-budget.py` (human output) and `tests/test_prompt_budget.py` (ceilings).

Estimates are chars / 3.8 — the same heuristic as AGENTS.md — so absolute values are approximate but
comparisons are consistent. Authoritative totals come from Ollama's `prompt_tokens` on a real turn.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from frontend.ollama_chat_profiles import SHARED_NUM_CTX
from pipeline import tool_registry

ROOT = Path(__file__).resolve().parents[1]
CHARS_PER_TOKEN = 3.8

# The chars/3.8 estimate is a *proxy*: it cannot see the chat template, the JSON
# Schema envelope or the tool-call scaffolding that Ollama also charges for, so
# it undercounts. Measured 2026-10-21 against empire-fast:14b: 6,688 real
# prompt tokens for a prompt this estimate puts at 6,410 — a 4.3% undercount
# (and the calibrated estimate, 6,692, lands 4 tokens from the truth).
#
# The ceilings in `tests/test_prompt_budget.py` are therefore written in REAL
# tokens, and the static estimate is scaled onto that scale before it is
# compared. Re-measure with `scripts/measure-live-prompt.py` before changing
# this number.
LIVE_OVER_ESTIMATE = 1.044
INSTRUCTIONS = (
    ROOT / "eve_instructions.md",
    ROOT / "agents" / "empire-task-agent" / "agent" / "empire-routing.md",
    ROOT / "agents" / "empire-task-agent" / "agent" / "eve-operating-context.md",
)
TOOLS = ROOT / "agents" / "empire-task-agent" / "agent" / "tools"

DESC_RE = re.compile(r'description:\s*\n?\s*((?:"[^"]*"(?:\s*\+\s*)?)+)', re.DOTALL)
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
DESCRIBE_RE = re.compile(r'\.describe\(\s*((?:"[^"]*"(?:\s*\+\s*)?)+)\s*\)', re.DOTALL)


def tokens(chars: int) -> int:
    """chars -> approximate tokens (kept in one place so every report uses one basis)."""

    return int(chars / CHARS_PER_TOKEN)


def real_tokens(estimate_tokens: int) -> int:
    """Scale a static chars/3.8 estimate onto the real-token scale.

    The estimate undercounts by the template/schema overhead Ollama charges for
    (see `LIVE_OVER_ESTIMATE`). Every ceiling is written in real tokens, so
    this is the bridge between the cheap offline measure and the truth.
    """

    return int(round(estimate_tokens * LIVE_OVER_ESTIMATE))


def schema_chars(text: str) -> tuple[int, int]:
    """(description chars, parameter-description chars) in one tool source."""

    desc = DESC_RE.search(text)
    main = len("".join(STR_RE.findall(desc.group(1)))) if desc else 0
    params = sum(len("".join(STR_RE.findall(m.group(1)))) for m in DESCRIBE_RE.finditer(text))
    return main, params


def _tool_files() -> list[Path]:
    """The tool sources that cost prompt budget — disabled tools are not registered at all.

    `agent`, `bash`, `ask_question`, the sandbox filesystem tools (`glob` / `grep` / `read_file` /
    `write_file`) and provider search (`web_search` / `web_fetch`) are `export default
    disableTool()`: they never reach the schema, so counting them made the always-tool count read
    31 instead of 30 (found 2026-09-24). `pipeline.tool_registry` owns that definition.
    """

    return tool_registry.tool_sources()


def _classify(text: str) -> str:
    """Bucket one tool source: always-registered, default-gated, or gated.

    `pipeline.tool_registry` owns this definition (see `always_on_tools` /
    `default_gated_tools`) — two places deciding "what is always on" is how
    the capabilities report and the budget measurement drifted apart.
    """

    gated = "isCapabilityActive" in text or "isCategoryEnabled" in text
    if not gated:
        return "always"
    return "wiki_local" if '"wiki_local"' in text else "gated"


def measure() -> dict[str, Any]:
    """Component breakdown for the working tree."""

    instructions = {path.name: len(path.read_text(encoding="utf-8")) for path in INSTRUCTIONS}
    return _summarise(instructions, {path: path.read_text(encoding="utf-8") for path in _tool_files()})


def _git_show(rev: str, path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{rev}:{relative}"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout if result.returncode == 0 else ""


def live_tool_schemas(frontend: str = "http://127.0.0.1:8080", eve: str = "http://127.0.0.1:2000") -> list[dict[str, Any]]:
    """The tool schemas the *running* server exposes, in OpenAI function form.

    The static measurement below reads the tool sources off disk. That is the
    right basis for a ceiling test (it works with no stack), but it is an
    estimate of what the model is offered. This reads what the live agent
    actually registered, so a live measurement can compare the two.
    """
    import json as _json
    import urllib.request

    request = urllib.request.Request(f"{eve}/eve/v1/info", headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=30) as response:
        info = _json.loads(response.read().decode("utf-8", errors="replace"))
    tools: list[dict[str, Any]] = []
    for entry in (info.get("tools") or {}).get("available") or []:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name") or "").strip()
        if not name:
            continue
        schema = entry.get("inputSchema")
        parameters = schema if isinstance(schema, dict) and schema.get("properties") else {"type": "object", "properties": {}}
        tools.append(
            {
                "type": "function",
                "function": {
                    "name": name,
                    "description": str(entry.get("description") or ""),
                    "parameters": parameters,
                },
            }
        )
    return tools


def measure_live(model: str = "", ollama: str = "http://127.0.0.1:11434") -> dict[str, Any]:
    """Measure the prompt the live model actually pays, in real tokens.

    The static measurement estimates tokens as chars/3.8. That is a
    *consistent proxy*, not the truth: Ollama's own `prompt_tokens` counts
    the template, the JSON Schema envelope and the tool-call scaffolding the
    estimate cannot see. This sends the live system prompt and the live tool
    schemas to the model and reports what it was actually charged.

    Returns a dict with `ok: False` and a reason when the stack is not up —
    a measurement that cannot be taken must never look like a passing one.
    """
    import json as _json
    import urllib.error
    import urllib.request

    if not model:
        try:
            from frontend import ollama_api

            model = str((ollama_api.load_active_config() or {}).get("model") or "")
        except Exception:  # noqa: BLE001
            model = ""
    if not model:
        return {"ok": False, "reason": "no active model configured"}

    try:
        tools = live_tool_schemas()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "reason": f"cannot read the live tool surface: {exc}"}
    if not tools:
        return {"ok": False, "reason": "the live agent exposed no tools"}

    system = "\n\n---\n\n".join(
        path.read_text(encoding="utf-8").strip() for path in INSTRUCTIONS if path.is_file()
    )
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": "hi"},
        ],
        "tools": tools,
        "stream": False,
    }
    request = urllib.request.Request(
        f"{ollama}/v1/chat/completions",
        data=_json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            payload = _json.loads(response.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        return {"ok": False, "reason": f"Ollama is unreachable: {exc}"}
    except ValueError as exc:
        return {"ok": False, "reason": f"Ollama returned an unreadable body: {exc}"}

    usage = payload.get("usage") or {}
    measured = usage.get("prompt_tokens")
    if not isinstance(measured, int) or measured <= 0:
        return {"ok": False, "reason": "Ollama reported no prompt_tokens"}
    return {
        "ok": True,
        "model": model,
        "prompt_tokens": measured,
        "completion_tokens": usage.get("completion_tokens"),
        "tool_count": len(tools),
        "system_chars": len(system),
        "num_ctx": SHARED_NUM_CTX,
        "headroom_tokens": SHARED_NUM_CTX - measured,
    }


def measure_rev(rev: str) -> dict[str, Any]:
    """Same measurement against a git revision, so before/after is reproducible."""

    instructions = {path.name: len(_git_show(rev, path)) for path in INSTRUCTIONS}
    sources = {path: _git_show(rev, path) for path in _tool_files()}
    return _summarise(instructions, {p: t for p, t in sources.items() if t})


def _summarise(instructions: dict[str, int], sources: dict[Path, str]) -> dict[str, Any]:
    instruction_chars = sum(instructions.values())
    buckets = {"always": 0, "wiki_local": 0}
    counts = {"always": 0, "wiki_local": 0, "gated": 0}
    for path, text in sources.items():
        kind = _classify(text)
        counts[kind] += 1
        if kind in buckets:
            main, params = schema_chars(text)
            buckets[kind] += main + params

    default_schema = buckets["always"] + buckets["wiki_local"]
    floor = instruction_chars + default_schema
    instruction_tokens = tokens(instruction_chars)
    default_schema_tokens = tokens(default_schema)
    floor_tokens = tokens(floor)
    return {
        "instructions": instructions,
        "instruction_chars": instruction_chars,
        "instruction_tokens": instruction_tokens,
        "instruction_real_tokens": real_tokens(instruction_tokens),
        "always_tools": counts["always"],
        "always_schema_tokens": tokens(buckets["always"]),
        "default_gated_tools": counts["wiki_local"],
        "default_gated_schema_tokens": tokens(buckets["wiki_local"]),
        "default_schema_tokens": default_schema_tokens,
        "default_schema_real_tokens": real_tokens(default_schema_tokens),
        "floor_tokens": floor_tokens,
        "floor_real_tokens": real_tokens(floor_tokens),
        "live_over_estimate": LIVE_OVER_ESTIMATE,
        "num_ctx": SHARED_NUM_CTX,
        "headroom_tokens": SHARED_NUM_CTX - real_tokens(floor_tokens),
    }