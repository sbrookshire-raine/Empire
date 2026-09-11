"""Smoke: wiki lookup injection + optional live Eve reply for Stranger Things song Q&A."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

# Allow: python scripts\test-wiki-chat-smoke.py (no PYTHONPATH required)
_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))
import urllib.error
import urllib.request
from typing import Any

ORIGIN = "http://127.0.0.1:8080"

QUESTIONS = [
    (
        "popular_80s_stranger_things",
        "what popular 80s song got re-popularized during the later seasons of stranger things?",
        ("running up that hill",),
    ),
    (
        "80s_hit_again",
        "what 80s song became a hit again in the series stranger things?",
        ("running up that hill",),
    ),
    (
        "kate_bush_revival",
        "what song from Kate Bush reinvigorated her career in 2025-2026?",
        ("running up that hill", "kate bush"),
    ),
    (
        "kate_bush_who",
        "who is Kate Bush?",
        ("kate bush", "1958"),  # bio lead — not 2023 Rolling Stone trivia
    ),
]

COMPARE_QUESTIONS = [
    (
        "ai_compare_2017_2026",
        "Compare artificial intelligence 2017 vs 2026",
        ("artificial intelligence",),
    ),
]

BAD_REPLY_MARKERS = (
    "stranger things have happened",
    "wiki_scout_compare_years",
    "rank_why",
    "kind_hint",
    "no direct entry",
    "does not have a direct entry",
    "kyle dixon",
    "only the original synth score",
    '"wow"',
    "'wow'",
)


def _req(
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    *,
    timeout: float = 120,
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


def stream_final_text(session_id: str, *, max_seconds: float = 180) -> dict[str, Any]:
    url = f"{ORIGIN}/api/eve/session/{session_id}/stream?startIndex=0"
    request = urllib.request.Request(
        url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"}
    )
    tools: list[str] = []
    final = ""
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
    return {"text": final, "tools": tools}


def test_injection(name: str, question: str, must_contain: tuple[str, ...]) -> list[str]:
    from frontend.wiki_drift_api import (
        WIKI_LOOKUP_MARKER,
        enrich_eve_message_payload,
        is_wiki_lookup_query,
    )
    from unittest.mock import patch

    errors: list[str] = []
    if not is_wiki_lookup_query(question):
        errors.append(f"{name}: is_wiki_lookup_query=False")
    with patch("frontend.wiki_drift_api.load_active_tools", return_value=["wiki_local"]):
        enriched = enrich_eve_message_payload({"message": question})
    msg = str(enriched.get("message") or "")
    if WIKI_LOOKUP_MARKER not in msg:
        errors.append(f"{name}: no WIKI_LOOKUP injection")
        return errors
    lowered = msg.casefold()
    for needle in must_contain:
        if needle.casefold() not in lowered:
            errors.append(f"{name}: injection missing {needle!r}")
    if "**rank:**" in lowered or "rank_why:" in lowered:
        errors.append(f"{name}: injection contains debug card dump")
    return errors


def test_live_eve(name: str, question: str, must_contain: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    status, payload = _req(
        "POST",
        "/api/eve/session",
        {"message": question, "mode": "fast", "active_tools": ["wiki_local"]},
        timeout=120,
    )
    if status >= 400 or not isinstance(payload, dict) or not payload.get("sessionId"):
        errors.append(f"{name}: session failed ({status}) {payload}")
        return errors
    sid = str(payload["sessionId"])
    stream = stream_final_text(sid, max_seconds=180)
    text = stream["text"]
    lowered = text.casefold()
    if not text.strip():
        errors.append(f"{name}: empty Eve reply")
        return errors
    for needle in must_contain:
        if needle.casefold() not in lowered:
            errors.append(f"{name}: reply missing {needle!r}")
    for bad in BAD_REPLY_MARKERS:
        if bad in lowered:
            errors.append(f"{name}: reply contains bad marker {bad!r}")
    return errors


def test_compare_injection(name: str, question: str, must_contain: tuple[str, ...]) -> list[str]:
    from frontend.wiki_drift_api import (
        WIKI_DRIFT_MARKER,
        enrich_eve_message_payload,
        is_truth_drift_query,
    )
    from unittest.mock import patch

    errors: list[str] = []
    if not is_truth_drift_query(question):
        errors.append(f"{name}: is_truth_drift_query=False")
    with patch("frontend.wiki_drift_api.load_active_tools", return_value=["wiki_local"]):
        enriched = enrich_eve_message_payload({"message": question})
    msg = str(enriched.get("message") or "")
    if WIKI_DRIFT_MARKER not in msg:
        errors.append(f"{name}: no WIKI_DRIFT injection")
        return errors
    lowered = msg.casefold()
    for needle in must_contain:
        if needle.casefold() not in lowered:
            errors.append(f"{name}: injection missing {needle!r}")
    # Topic must not collapse to bare "truth"
    if "topic: truth" in lowered and "artificial intelligence" not in lowered:
        errors.append(f"{name}: compare topic collapsed to 'truth'")
    return errors


def main() -> int:
    print(f"EMPIRE root: {_EMPIRE_ROOT}")
    print("=== Wiki injection smoke ===")
    all_errors: list[str] = []
    for name, question, must in QUESTIONS:
        errs = test_injection(name, question, must)
        if errs:
            all_errors.extend(errs)
            print("FAIL injection", name, errs)
        else:
            print("OK injection", name)

    print("\n=== Truth Drift injection smoke ===")
    for name, question, must in COMPARE_QUESTIONS:
        errs = test_compare_injection(name, question, must)
        if errs:
            all_errors.extend(errs)
            print("FAIL injection", name, errs)
        else:
            print("OK injection", name)

    print("\n=== Live Eve smoke (8080 + 2000 + Ollama) ===")
    status, _ = _req("GET", "/api/memory/status", timeout=8)
    if status >= 400:
        print("WARN: frontend not reachable on 8080 — skip live Eve")
        if all_errors:
            for err in all_errors:
                print("ERROR:", err)
            return 1
        return 0

    for name, question, must in QUESTIONS:
        live_errors = test_live_eve(name, question, must)
        if live_errors:
            all_errors.extend(live_errors)
            print("FAIL live", name, live_errors)
        else:
            print("OK live", name)

    for name, question, must in COMPARE_QUESTIONS:
        live_errors = test_live_eve(name, question, must)
        if live_errors:
            all_errors.extend(live_errors)
            print("FAIL live", name, live_errors)
        else:
            print("OK live", name)

    if all_errors:
        print("\nFAILED", len(all_errors), "check(s)")
        for err in all_errors:
            print(" -", err)
        return 1
    print("\nPASS wiki chat smoke")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
