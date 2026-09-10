"""Compare Fast vs Librarian Eve replies on wiki calibration questions."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request

ORIGIN = "http://127.0.0.1:8080"

QUESTIONS = [
    (
        "popular_80s",
        "what popular 80s song got re-popularized during the later seasons of stranger things?",
        ("running up that hill",),
    ),
    (
        "80s_hit",
        "what 80s song became a hit again in the series stranger things?",
        ("running up that hill",),
    ),
    (
        "kb_revival",
        "what song from Kate Bush reinvigorated her career in 2025-2026?",
        ("running up that hill", "kate bush"),
    ),
    ("kb_who", "who is Kate Bush?", ("kate bush",)),
]

BAD_MARKERS = (
    "stranger things have happened",
    "wiki_scout_compare_years",
    "rank_why",
    '"wow"',
    "'wow'",
    "no direct entry",
    "kyle dixon",
)


def _req(
    method: str,
    path: str,
    payload: dict | None = None,
    *,
    timeout: float = 180,
) -> dict:
    data = None
    headers = {"Origin": ORIGIN, "Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        ORIGIN + path, data=data, headers=headers, method=method
    )
    with urllib.request.urlopen(request, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        return json.loads(body) if body else {}


def stream_text(session_id: str, *, max_seconds: float = 300) -> tuple[str, list[str]]:
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
            event = json.loads(line.decode("utf-8", errors="replace"))
            event_type = str(event.get("type") or "")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if event_type == "actions.requested":
                for action in data.get("actions") or []:
                    if isinstance(action, dict):
                        tools.append(str(action.get("toolName") or ""))
            if event_type == "message.appended":
                final = str(data.get("messageSoFar") or final)
            if event_type == "message.completed":
                content = (
                    data.get("text")
                    or data.get("content")
                    or data.get("messageSoFar")
                )
                if content:
                    final = str(content)
            if event_type == "session.waiting":
                break
    return final, tools


def run_mode(mode: str) -> list[str]:
    errors: list[str] = []
    print(f"=== {mode.upper()} ===")
    for name, question, must in QUESTIONS:
        started = time.time()
        try:
            payload = _req(
                "POST",
                "/api/eve/session",
                {
                    "message": question,
                    "mode": mode,
                    "active_tools": ["wiki_local"],
                },
            )
            session_id = str(payload.get("sessionId") or "")
            if not session_id:
                errors.append(f"{mode}/{name}: no sessionId")
                print(f"FAIL {name}: no sessionId")
                continue
            text, tools = stream_text(session_id)
            elapsed = time.time() - started
            lowered = text.casefold()
            ok = (
                bool(text.strip())
                and all(needle in lowered for needle in must)
                and not any(bad in lowered for bad in BAD_MARKERS)
            )
            status = "OK" if ok else "FAIL"
            print(f"{status} {name} ({elapsed:.1f}s) tools={tools}")
            print(" ", text[:240].replace("\n", " "))
            if not ok:
                errors.append(f"{mode}/{name}")
                for needle in must:
                    if needle not in lowered:
                        print(f"   missing {needle!r}")
                for bad in BAD_MARKERS:
                    if bad in lowered:
                        print(f"   bad marker {bad!r}")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            errors.append(f"{mode}/{name}: {exc}")
            print(f"ERR {name}: {exc}")
    print()
    return errors


def main() -> int:
    all_errors: list[str] = []
    for mode in ("fast", "librarian"):
        all_errors.extend(run_mode(mode))
    if all_errors:
        print("FAILED", len(all_errors), "case(s):", ", ".join(all_errors))
        return 1
    print("PASS all modes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
