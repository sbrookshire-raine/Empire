"""Time one Eve wiki turn: POST, first token, tools, session.waiting."""

from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "http://127.0.0.1:8080"
TRACE = _ROOT / "eve-audit" / "eve-trace.jsonl"


def main() -> int:
    query = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Go to my local Wikipedia and find what are the albums released by the Beach Boys."
    )
    trace_off = TRACE.stat().st_size if TRACE.exists() else 0
    t0 = time.perf_counter()

    payload = json.dumps(
        {"message": query, "mode": "fast", "active_tools": ["wiki_local"]}
    ).encode()
    req = urllib.request.Request(
        f"{ORIGIN}/api/eve/session",
        data=payload,
        headers={"Content-Type": "application/json", "Origin": ORIGIN},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.loads(resp.read())
    sid = body["sessionId"]
    post_s = time.perf_counter() - t0

    url = f"{ORIGIN}/api/eve/session/{sid}/stream?startIndex=0"
    req = urllib.request.Request(url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"})
    first_msg: float | None = None
    waiting: float | None = None
    tools: list[str] = []
    final_len = 0
    events: list[str] = []

    with urllib.request.urlopen(req, timeout=600) as resp:
        while time.perf_counter() - t0 < 480:
            line = resp.readline()
            if not line:
                break
            elapsed = time.perf_counter() - t0
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            et = str(ev.get("type") or "")
            d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
            if et == "actions.requested":
                for a in d.get("actions") or []:
                    if isinstance(a, dict):
                        tools.append(str(a.get("toolName") or ""))
                events.append(f"{elapsed:6.1f}s  {et}  {tools[-3:]}")
            elif et not in ("message.appended",):
                events.append(f"{elapsed:6.1f}s  {et}")
            if et in ("message.appended", "message.completed"):
                c = d.get("messageSoFar") or d.get("message") or ""
                if c and first_msg is None:
                    first_msg = elapsed
                if c:
                    final_len = len(str(c))
            if et == "session.waiting":
                waiting = elapsed
                break

    total = time.perf_counter() - t0
    print(f"Query: {query[:72]}...")
    print(f"  session POST     {post_s:.2f}s")
    print(f"  first assistant  {(first_msg or -1):.2f}s" if first_msg else "  first assistant  (none)")
    print(f"  session.waiting  {(waiting or total):.2f}s")
    print(f"  final text len   {final_len}")
    print(f"  tools            {tools}")
    print("\n=== Event timeline (non-delta) ===")
    for line in events[:40]:
        print(" ", line)
    if TRACE.exists():
        print("\n=== Trace tool lines (this turn) ===")
        turn_id = ""
        with TRACE.open(encoding="utf-8") as fh:
            fh.seek(trace_off)
            for raw in fh:
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if rec.get("kind") == "turn.start":
                    turn_id = str(rec.get("turn") or "")
                if turn_id and rec.get("turn") != turn_id:
                    continue
                k = rec.get("kind")
                if k in ("tool.requested", "tool.result", "stream.end", "event"):
                    print(f"  {k:16} {rec}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
