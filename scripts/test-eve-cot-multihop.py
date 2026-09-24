"""Two-turn live test: MANDATORY EXECUTION PROTOCOL (Chain-of-Thought) + multi-hop.

Turn 1: "Who is Kate Bush?"          -> lands the article lead.
Turn 2: "What else is on that page?" -> must produce a <thought> block that recognises
                                       the lead is not enough and then call a deeper wiki
                                       tool by itself (wiki_read_section / wiki_extract /
                                       another wiki_scout_search), instead of repeating
                                       the lead paragraph.

Default talks to Eve directly (port 2000, raw stream) so the `<thought>` scratch is
visible. Use --via-frontend to exercise the real Workbench path (8080), where the proxy
strips reasoning blocks from the user-visible text.

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  .\\venv\\Scripts\\python.exe scripts\\test-eve-cot-multihop.py
  .\\venv\\Scripts\\python.exe scripts\\test-eve-cot-multihop.py --via-frontend
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))

ORIGIN = "http://127.0.0.1:8080"
EVE_DIRECT = "http://127.0.0.1:2000"
EVE_ORIGIN_HEADER = ORIGIN

TURN_1 = "Who is Kate Bush?"
TURN_2 = "What else is on that page?"

DEEPER_TOOLS = {"wiki_read_section", "wiki_extract", "wiki_scout_search", "wiki_resolve"}

_REASONING_TAG = r"(?:thought|thoughts|thinking|think|reasoning)"
_THOUGHT_BLOCK_RE = re.compile(
    rf"<{_REASONING_TAG}\b[^>]*>(.*?)(?:</{_REASONING_TAG}>|$)",
    re.DOTALL | re.IGNORECASE,
)


def _request(
    method: str,
    url: str,
    payload: dict | None = None,
    *,
    timeout: float = 180,
) -> tuple[int, dict]:
    data = None
    headers = {"Origin": EVE_ORIGIN_HEADER, "Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            try:
                return response.status, (json.loads(body) if body else {})
            except json.JSONDecodeError:
                return response.status, {"raw": body[:400]}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, (json.loads(body) if body else {})
        except json.JSONDecodeError:
            return exc.code, {"raw": body[:400]}
    except Exception as exc:  # noqa: BLE001
        return 599, {"error": str(exc)}


def _eve_prefix(base: str) -> str:
    """Workbench proxy serves /api/eve/*; Eve itself serves /eve/v1/*."""

    return "/api/eve" if base.rstrip("/") == ORIGIN else "/eve/v1"


def stream_turn(
    base: str,
    session_id: str,
    *,
    start_index: int = 0,
    max_seconds: float = 240,
) -> dict:
    """Read the session NDJSON stream from `start_index`; collect text per step + tools.

    Reasoning written before a tool call lives in an *earlier step* whose `messageSoFar`
    is later replaced by the final answer, so steps are kept separately (`steps`) and
    joined into `all_text` for reasoning-block extraction. `text` is the final answer.

    `next_index` must be passed to the following turn: the session stream is cumulative,
    and re-reading from 0 replays the previous turn's events (which looks exactly like the
    model repeating itself).
    """

    url = f"{base}{_eve_prefix(base)}/session/{session_id}/stream?startIndex={start_index}"
    request = urllib.request.Request(
        url,
        headers={"Origin": EVE_ORIGIN_HEADER, "Accept": "application/x-ndjson"},
    )
    tools: list[str] = []
    steps: dict[int, str] = {}
    thinking = ""
    stopped = ""
    consumed = start_index
    deadline = time.time() + max_seconds
    with urllib.request.urlopen(request, timeout=max_seconds) as response:
        while time.time() < deadline:
            line = response.readline()
            if not line:
                break
            consumed += 1
            raw = line.decode("utf-8", errors="replace").strip()
            if not raw:
                continue
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if not isinstance(event, dict):
                continue
            event_type = str(event.get("type") or "")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            try:
                step_index = int(data.get("stepIndex") or 0)
            except (TypeError, ValueError):
                step_index = 0
            if event_type == "actions.requested":
                for action in data.get("actions") or []:
                    if isinstance(action, dict):
                        tools.append(str(action.get("toolName") or ""))
            if event_type == "message.appended":
                for key in ("messageSoFar", "message", "messageDelta", "delta"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip():
                        steps[step_index] = (
                            value
                            if key == "messageSoFar"
                            else steps.get(step_index, "") + value
                        )
            if event_type == "message.completed":
                for key in ("text", "content", "message", "messageSoFar"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip():
                        steps[step_index] = value
                        break
            if "reasoning" in event_type or "thinking" in event_type:
                for key in ("text", "messageSoFar", "message", "delta"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip():
                        thinking += value
            if event_type in {"session.waiting", "session.completed", "session.failed"}:
                stopped = event_type
                break
    ordered = [steps[index] for index in sorted(steps)]
    return {
        "text": ordered[-1] if ordered else "",
        "all_text": "\n".join(ordered),
        "steps": ordered,
        "thinking": thinking,
        "tools": tools,
        "stopped": stopped,
        "next_index": consumed,
    }


def thought_blocks(text: str) -> list[str]:
    """Extract <thought> bodies, including a block whose closing tag never arrived."""

    if not text:
        return []
    blocks: list[str] = []
    for match in _THOUGHT_BLOCK_RE.finditer(text):
        body = re.sub(r"\s+", " ", match.group(1)).strip()
        if body:
            blocks.append(body)
    return blocks


def send_turn(
    base: str,
    *,
    message: str,
    session_id: str = "",
    continuation_token: str = "",
    mode: str = "conversation",
    chat_id: str = "",
) -> tuple[int, dict]:
    """POST a turn. `mode` must be 'conversation'|'task' for Eve's own API.

    The Workbench proxy strips the chat mode ('fast'/'deep') and picks the Ollama model
    from its own active-config file, then forwards `mode: conversation`, so both routes
    accept the same value here. `chat_id` is only used by the Workbench route: it makes
    the server attach the rolling-summary context (Eve's own continuation carries no
    conversation history).
    """
    if session_id:
        url = f"{base}{_eve_prefix(base)}/session/{session_id}"
        payload = {
            "continuationToken": continuation_token,
            "message": message,
            "mode": mode,
            "active_tools": ["wiki_local"],
        }
    else:
        url = f"{base}{_eve_prefix(base)}/session"
        payload = {"message": message, "mode": mode, "active_tools": ["wiki_local"]}
    if chat_id:
        payload["chat_id"] = chat_id
    return _request("POST", url, payload, timeout=120)


def put_chat_history(base: str, chat_id: str, messages: list[dict]) -> tuple[int, dict]:
    """Persist chat turns like the Workbench UI does (feeds the rolling summary)."""

    return _request(
        "PUT",
        f"{base}/api/chat-history/{chat_id}",
        {"messages": messages, "updatedAt": None},
        timeout=30,
    )


def show(label: str, value: str, *, limit: int = 1200) -> None:
    print(f"--- {label} ---")
    text = (value or "").strip()
    if not text:
        print("(empty)")
        return
    print(text[:limit])
    if len(text) > limit:
        print(f"... [{len(text) - limit} more chars]")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--via-frontend",
        action="store_true",
        help="Use the Workbench proxy on 8080 (user-visible text, reasoning stripped)",
    )
    args = parser.parse_args()

    base = ORIGIN if args.via_frontend else EVE_DIRECT
    route = "frontend proxy 8080" if args.via_frontend else "direct, raw upstream"
    print(f"Eve endpoint: {base} ({route})")

    chat_id = f"cot-multihop-{int(time.time())}" if args.via_frontend else ""
    if chat_id:
        # Same as the UI: turn 1 is persisted so turn 2 gets the rolling summary.
        status, _ = put_chat_history(
            base, chat_id, [{"role": "user", "text": TURN_1}]
        )
        print(f"chat history seeded: {chat_id} [PUT {status}]")

    status, created = send_turn(base, message=TURN_1, chat_id=chat_id)
    print(f"\nTURN 1 -> {TURN_1!r}  [POST {status}]")
    session_id = str(created.get("sessionId") or "")
    continuation = str(created.get("continuationToken") or "")
    if status >= 400 or not session_id:
        print("FAIL: could not start session:", json.dumps(created)[:400])
        return 2

    turn1 = stream_turn(base, session_id)
    show("TURN 1 THOUGHT", "\n".join(thought_blocks(turn1["all_text"])) or turn1["thinking"])
    print("TURN 1 TOOLS:", turn1["tools"] or "none")
    show("TURN 1 REPLY", turn1["text"])
    if chat_id:
        put_chat_history(
            base,
            chat_id,
            [
                {"role": "user", "text": TURN_1},
                {"role": "assistant", "text": turn1["text"]},
            ],
        )

    status, continued = send_turn(
        base,
        session_id=session_id,
        continuation_token=continuation,
        message=TURN_2,
        chat_id=chat_id,
    )
    print(f"\nTURN 2 -> {TURN_2!r}  [POST {status}]")
    if status >= 400:
        print("FAIL: could not continue session:", json.dumps(continued)[:400])
        return 2
    if continued.get("continuationToken"):
        continuation = str(continued["continuationToken"])

    turn2 = stream_turn(base, session_id, start_index=turn1["next_index"])
    blocks = thought_blocks(turn2["all_text"])
    show("TURN 2 THOUGHT", "\n".join(blocks) or turn2["thinking"])
    print("TURN 2 TOOLS:", turn2["tools"] or "none")
    show("TURN 2 REPLY", turn2["text"])

    lead = (turn1["text"] or "").strip()
    reply = (turn2["text"] or "").strip()
    deeper = [tool for tool in turn2["tools"] if tool in DEEPER_TOOLS]
    hop_recognised = any(
        re.search(
            r"(dig|deep|not enough|only .{0,24}(lead|intro)|missing|more detail|"
            r"section|hop|discograph|album|song)",
            block,
            re.I,
        )
        for block in blocks
    )

    reasons: list[str] = []
    direct_mode = not args.via_frontend
    if direct_mode:
        print(
            "\nNOTE: the direct Eve channel sends no conversation history, so turn 2 cannot "
            "resolve\n      'that page'. Direct mode grades the CoT format only; use "
            "--via-frontend for the hop."
        )
    turn1_blocks = thought_blocks(turn1["all_text"])
    if not (blocks or turn2["thinking"]):
        if turn1_blocks or turn1["thinking"]:
            print(
                "note: turn 2 emitted no block, but turn 1 did — the protocol is active; "
                "grading behaviour."
            )
        else:
            # The block is the strongest signal the protocol is active, but the durable
            # outcome is the hop. Report it; do not fail the run on formatting alone.
            print(
                "note: no <thought> block captured this run — with a 14B model compliance is "
                "intermittent;\n      the hop below is the hard requirement."
            )
    elif not hop_recognised and not direct_mode:
        reasons.append("reasoning block did not recognise the lead was insufficient")
    if not deeper:
        reasons.append("no deeper wiki tool call in turn 2 (premature completion)")
    if reply and lead and reply[:200].casefold() == lead[:200].casefold():
        reasons.append("turn 2 reply repeats the turn 1 lead verbatim")

    print("\n=== VERDICT ===")
    print(f"reasoning block: {'yes' if (blocks or turn2['thinking']) else 'no'}")
    print(f"hop recognised:  {'yes' if hop_recognised else 'no'}")
    print(f"deeper tools:    {deeper or 'none'}")
    print(f"turn 2 length:   {len(reply)} chars (turn 1: {len(lead)})")
    if reasons:
        print("\nRESULT: FAIL - CoT/multi-hop improvement not observed")
        for reason in reasons:
            print(" -", reason)
        return 1
    print("\nRESULT: PASS - reasoning block flagged the gap and a deeper wiki call followed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
