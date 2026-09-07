"""E2E: Truth Drift via frontend Eve proxy with server-side wiki glasses."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from typing import Any

ORIGIN = "http://127.0.0.1:8080"
QUERY = (
    "Truth Drift: has the scope and terms related to truth changed between "
    "2017 and 2026? I care about AI creating vs absorbing — use local wiki archives."
)


def _req(
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    *,
    timeout: float = 180,
) -> tuple[int, Any]:
    data = None
    headers = {"Origin": ORIGIN, "Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        ORIGIN + path, data=data, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(body) if body else {}
        except json.JSONDecodeError:
            return exc.code, {"raw": body}


def stream_final_text(session_id: str, *, max_seconds: float = 240) -> dict[str, Any]:
    url = f"{ORIGIN}/api/eve/session/{session_id}/stream?startIndex=0"
    request = urllib.request.Request(
        url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"}
    )
    tools: list[str] = []
    final = ""
    types: set[str] = set()
    deadline = time.time() + max_seconds
    with urllib.request.urlopen(request, timeout=max_seconds) as resp:
        while time.time() < deadline:
            line = resp.readline()
            if not line:
                break
            raw = line.decode("utf-8", errors="replace").strip()
            if not raw:
                continue
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            et = str(event.get("type") or "")
            types.add(et)
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if et == "actions.requested":
                for action in data.get("actions") or []:
                    if isinstance(action, dict):
                        tools.append(str(action.get("toolName") or ""))
            if et == "message.appended":
                final = str(data.get("messageSoFar") or final)
            if et == "message.completed":
                content = data.get("text") or data.get("content") or data.get("messageSoFar")
                if content:
                    final = str(content)
            if et == "session.waiting":
                break
    return {"text": final, "tools": tools, "types": sorted(types)}


def main() -> int:
    from frontend.memory_api import is_memory_chat_query
    from frontend.wiki_drift_api import (
        WIKI_DRIFT_MARKER,
        enrich_eve_message_payload,
        is_truth_drift_query,
        pick_compare_topic,
    )

    assert is_truth_drift_query(QUERY)
    assert not is_memory_chat_query(QUERY)
    topic = pick_compare_topic(QUERY)
    print("TOPIC", topic)

    enriched = enrich_eve_message_payload({"message": QUERY})
    msg = str(enriched.get("message") or "")
    print("HAS_CARDS", WIKI_DRIFT_MARKER in msg)
    print("HAS_POST_TRUTH", "Post-truth" in msg or "post-truth" in msg.casefold())
    print("NO_NOW", "[[EMPIRE_NOW]]" not in msg)
    if WIKI_DRIFT_MARKER not in msg:
        print("FAIL: enrich did not inject wiki cards")
        print(msg[:500])
        return 1

    status, payload = _req(
        "POST",
        "/api/eve/session",
        {"message": QUERY, "mode": "fast", "active_tools": ["wiki_local"]},
        timeout=120,
    )
    print("SESSION", status, payload.get("sessionId") if isinstance(payload, dict) else payload)
    if status >= 400 or not isinstance(payload, dict) or not payload.get("sessionId"):
        print("FAIL session", payload)
        return 2
    sid = str(payload["sessionId"])
    stream = stream_final_text(sid, max_seconds=240)
    text = stream["text"]
    print("TOOLS", stream["tools"])
    print("TEXT_HEAD", text[:700].replace("\n", " / "))
    lowered = text.casefold()
    bad_contract = "contract" in lowered and "post-truth" not in lowered
    good = ("2017" in text or "2021" in text or "2026" in text) and (
        "post-truth" in lowered or "truth" in lowered
    )
    print("GROUNDED", good, "BAD_CONTRACT_RABBITHOLE", bad_contract)
    report = {
        "topic": topic,
        "session_id": sid,
        "tools": stream["tools"],
        "grounded": good,
        "bad_contract": bad_contract,
        "text": text[:2500],
        "enrich_has_cards": WIKI_DRIFT_MARKER in msg,
    }
    out = r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache\e2e_truth_drift_last.json"
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print("WROTE", out)
    if bad_contract or not good:
        print("FAIL: answer not grounded in wiki cards")
        return 3
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
