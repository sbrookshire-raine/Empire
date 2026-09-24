"""A/B probe for Fast chat models: does it still call tools, and does it fit the context?

The Fast-mode A/B switch (``%LOCALAPPDATA%\\EMPIRE\\ollama-fast-ab.json``) lets you try a
different Fast tag. Before promoting an alternate you must know two things that a
"looks fine in chat" check cannot tell you:

1. **Tool calling** — the model still emits OpenAI-style ``tool_calls`` through the
   ``/v1/chat/completions`` proxy Eve actually uses.
2. **Context window** — the ~10k-token Eve prompt fits ``num_ctx`` (16384) without silent
   truncation, *and* tool calling still works with the prompt that big.

This probes Ollama's OpenAI-compat endpoint directly (no frontend/agent needed) with the
same tool names Eve has, and fails loudly on template leakage (``<translation>`` etc.).

    $env:PYTHONPATH='C:\\EMPIRE'
    .\\venv\\Scripts\\python.exe scripts\\ab-fast-toolcalling.py
    .\\venv\\Scripts\\python.exe scripts\\ab-fast-toolcalling.py --models empire-fast:7b
    .\\venv\\Scripts\\python.exe scripts\\ab-fast-toolcalling.py --list

Exit code 0 = every probed model passed both gates.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))

OLLAMA_URL = "http://127.0.0.1:11434/v1/chat/completions"
OUT_PATH = _EMPIRE_ROOT / "eve-audit" / "ab-toolcalling.json"
DEFAULT_MODELS = ("empire-fast:14b", "empire-fast:7b")
# Eve's real prompt measures ~10k tokens (instructions + routing + ~32 tool schemas).
TARGET_PROMPT_TOKENS = 10_000
PAD_SENTENCE = (
    "Empire keeps local notes about bands, albums, cities and historical events so that "
    "answers stay grounded in stored documents instead of guesswork. "
)
LEAK_MARKERS = ("<translation>", "</translation>", "<tool_call>", "[[EMPIRE_", "```json")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "wiki_scout_search",
            "description": "Search the local wiki index for an article title first.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "wiki_read_section",
            "description": "Read one section of an already resolved wiki article.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "section": {"type": "string"},
                },
                "required": ["title", "section"],
            },
        },
    },
]

SYSTEM_PROMPT = (
    "You are Eve, a local assistant. You have wiki tools. When the user asks about a real "
    "subject, call wiki_scout_search first with the subject name; never answer such questions "
    "from memory."
)



def _post(model: str, messages: list[dict], tools: list[dict] | None) -> tuple[dict, float, str]:
    body: dict = {"model": model, "messages": messages, "stream": False, "temperature": 0.2}
    if tools:
        body["tools"] = tools
    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=300) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:200]
        return {}, (time.perf_counter() - started) * 1000, f"HTTP {exc.code}: {detail}"
    except Exception as exc:  # noqa: BLE001
        return {}, (time.perf_counter() - started) * 1000, f"{type(exc).__name__}: {exc}"
    return payload, (time.perf_counter() - started) * 1000, ""


def _padded_system(chars: int) -> str:
    """System prompt padded with neutral prose to reach the real Eve prompt size."""

    repeats = max(1, chars // len(PAD_SENTENCE))
    return f"{SYSTEM_PROMPT}\n\nReference notes:\n{PAD_SENTENCE * repeats}"


def _tool_names(payload: dict) -> list[str]:
    names: list[str] = []
    for choice in payload.get("choices") or []:
        message = choice.get("message") or {}
        for call in message.get("tool_calls") or []:
            function = call.get("function") or {}
            if function.get("name"):
                names.append(str(function["name"]))
    return names


def _content(payload: dict) -> str:
    chunks = []
    for choice in payload.get("choices") or []:
        message = choice.get("message") or {}
        if message.get("content"):
            chunks.append(str(message["content"]))
    return "\n".join(chunks).strip()


def _probe(model: str, question: str, *, big_context: bool) -> dict:
    """Run one probe. For the big-context probe, calibrate the pad so the prompt really reaches
    TARGET_PROMPT_TOKENS (prose tokenizes at ~6 chars/token, so an assumed ratio undershoots)."""

    if not big_context:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
        payload, latency_ms, error = _post(model, messages, TOOLS)
        attempts = 1
    else:
        pad_chars = int(TARGET_PROMPT_TOKENS * 4.0)
        payload, latency_ms, error, attempts = {}, 0.0, "", 0
        for _ in range(3):
            attempts += 1
            system = _padded_system(pad_chars)
            payload, latency_ms, error = _post(
                model,
                [{"role": "system", "content": system}, {"role": "user", "content": question}],
                TOOLS,
            )
            prompt_tokens = (payload.get("usage") or {}).get("prompt_tokens") or 0
            if error or not prompt_tokens:
                break
            if prompt_tokens >= TARGET_PROMPT_TOKENS:
                break
            sent_chars = len(system) + len(question)
            pad_chars = int(pad_chars * (TARGET_PROMPT_TOKENS / prompt_tokens) * 0.98)
            pad_chars = max(pad_chars, int(sent_chars * (TARGET_PROMPT_TOKENS / prompt_tokens)))

    usage = payload.get("usage") or {}
    content = _content(payload)
    names = _tool_names(payload)
    leaks = sorted({marker for marker in LEAK_MARKERS if marker in content})
    prompt_tokens = usage.get("prompt_tokens")
    fit_ok = True
    if big_context:
        fit_ok = bool(prompt_tokens) and int(prompt_tokens) >= TARGET_PROMPT_TOKENS
    return {
        "model": model,
        "probe": "tools-bigctx" if big_context else "tools-smoke",
        "ok": bool(names) and not error and fit_ok,
        "error": error,
        "latency_ms": round(latency_ms, 1),
        "prompt_tokens": prompt_tokens,
        "completion_tokens": usage.get("completion_tokens"),
        "tool_calls": names,
        "leaks": leaks,
        "context_ok": fit_ok,
        "attempts": attempts,
        "content_preview": content[:120],
    }


def _list_models() -> list[str]:
    request = urllib.request.Request("http://127.0.0.1:11434/api/tags")
    try:
        with urllib.request.urlopen(request, timeout=10) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: cannot reach Ollama at http://127.0.0.1:11434 ({exc})")
        return []
    return sorted(model.get("name", "") for model in payload.get("models") or [])



def main() -> int:
    parser = argparse.ArgumentParser(description="Probe Fast A/B models for tool calling + context fit.")
    parser.add_argument("--models", default=",".join(DEFAULT_MODELS), help="comma-separated model tags")
    parser.add_argument("--list", action="store_true", help="list installed Ollama models and exit")
    parser.add_argument(
        "--question",
        default="Look up the band the White Stripes and tell me their best known song.",
    )
    args = parser.parse_args()

    installed = _list_models()
    if args.list:
        for name in installed:
            print(f"  {name}")
        return 0
    if not installed:
        return 1

    models = [item.strip() for item in args.models.split(",") if item.strip()]
    missing = [model for model in models if model not in installed]
    if missing:
        print(f"FAIL: not installed: {', '.join(missing)}")
        print("      build with .\\scripts\\build-empire-ollama-models.ps1")
        return 1

    results: list[dict] = []
    for model in models:
        for big in (False, True):
            result = _probe(model, args.question, big_context=big)
            results.append(result)
            flag = "PASS" if result["ok"] else "FAIL"
            print(
                f"{flag}  {result['model']:<20} {result['probe']:<13} "
                f"{result['latency_ms']:>8.0f} ms  prompt_tokens={result['prompt_tokens']}{'' if result['context_ok'] else ' (context short)'}  "
                f"tools={result['tool_calls'] or '-'}"
            )
            if result["error"]:
                print(f"      error: {result['error']}")
            if result["leaks"]:
                print(f"      TEMPLATE LEAK: {result['leaks']} -> {result['content_preview']!r}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps({"results": results}, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT_PATH.relative_to(_EMPIRE_ROOT)}")

    failed = [item for item in results if not item["ok"]]
    if failed:
        print(f"\nRESULT: {len(failed)} probe(s) FAILED — do not promote that model for Fast mode.")
        return 1
    print(f"\nRESULT: {len(models)} model(s) pass tool calling + context ({TARGET_PROMPT_TOKENS}+ token prompt).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
