#!/usr/bin/env python3
"""Live routing battery (E-03): prove Eve reaches for the RIGHT tool.

Why this exists
---------------
The live harnesses so far asserted "a tool was called" by grepping the raw
NDJSON blob for a tool name. That passes when the model merely *mentions* a
tool in prose, and it cannot tell the right tool from a plausible-but-wrong
one (E-03: "Earlier runs sometimes picked a plausible-but-wrong tool").

This probe reads the framework's **structured** events instead:

- ``actions.requested`` -> ``data.actions[].toolName``  (the request)
- ``action.result``     -> ``data.result.toolName`` + ``data.status``

and asserts the tool that ran belongs to the route the *shared* classifier
assigned to the prompt. The expected tool is derived at run time from
``pipeline.route_classifier`` + ``pipeline.intent_codex`` — the same rules the
running system uses — so this battery cannot assert something the system does
not itself claim.

Usage (stack up):
    .\\venv\\Scripts\\python.exe scripts\\verify-live-routing.py
    .\\venv\\Scripts\\python.exe scripts\\verify-live-routing.py --case wiki_album
    .\\venv\\Scripts\\python.exe scripts\\verify-live-routing.py --json-out tmp/live-routing.json

Exit code 0 = every case routed to a tool its route implies.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYTHONPATH", str(ROOT))

FRONTEND = "http://127.0.0.1:8080"
BATTERY_PATH = ROOT / "config" / "diagnostics" / "live-routing-battery.json"


def _http_json(method: str, url: str, body: dict[str, Any] | None = None, timeout: int = 60) -> tuple[int, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
            try:
                return response.status, json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                return response.status, {"raw": raw[:500]}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(raw) if raw else {"error": str(exc)}
        except json.JSONDecodeError:
            return exc.code, {"error": str(exc), "raw": raw[:500]}


def _stream_turn(prompt: str, toolbelt: list[str], timeout: int) -> tuple[list[dict], str]:
    """Create a session and collect the raw NDJSON records of one turn.

    The toolbelt is sent **flat** (`active_tools`) — the shape the toolbelt
    path actually reads. The nested `{"toolbelt": {...}}` shape was silently
    discarded, so a harness using it measured Eve against a toolbelt it never
    asked for.
    """
    status, session = _http_json(
        "POST",
        f"{FRONTEND}/api/eve/session",
        {"message": prompt, "active_tools": list(toolbelt)},
    )
    if status not in (200, 201, 202):
        return [], f"session create failed (HTTP {status})"
    sid = session.get("sessionId") or session.get("session_id")
    if not isinstance(sid, str) or not sid:
        return [], "no session id in response"

    records: list[dict] = []
    start = 0
    deadline = time.time() + timeout
    while time.time() < deadline:
        url = f"{FRONTEND}/api/eve/session/{sid}/stream?startIndex={start}"
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/x-ndjson"})
            with urllib.request.urlopen(request, timeout=min(timeout, 120)) as response:
                for line in response:
                    text = line.decode("utf-8", errors="replace").strip()
                    if not text:
                        continue
                    try:
                        record = json.loads(text)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(record, dict):
                        records.append(record)
                    if isinstance(record.get("index"), int):
                        start = max(start, int(record["index"]) + 1)
                    if str(record.get("type") or "") in {
                        "session.waiting",
                        "turn.completed",
                        "session.completed",
                    }:
                        return records, ""
        except Exception as exc:  # noqa: BLE001 - a probe reports, never crashes
            time.sleep(2)
            if time.time() > deadline:
                return records, f"stream ended without a turn-ending event: {exc}"
    return records, "timed out waiting for the turn to end"


def main() -> int:
    parser = argparse.ArgumentParser(description="Live routing battery (E-03).")
    parser.add_argument("--case", action="append", default=None, help="Only run these case ids.")
    parser.add_argument("--json-out", default="", help="Write the full report here.")
    parser.add_argument("--timeout", type=int, default=0, help="Per-case timeout in seconds.")
    args = parser.parse_args()

    from pipeline import live_probe

    if not BATTERY_PATH.is_file():
        print(f"FAIL: battery missing: {BATTERY_PATH}")
        return 1
    battery = json.loads(BATTERY_PATH.read_text(encoding="utf-8"))
    cases = battery.get("cases") or []
    if args.case:
        wanted = set(args.case)
        cases = [c for c in cases if str(c.get("id")) in wanted]
    if not cases:
        print("FAIL: no cases selected")
        return 1

    toolbelt = [str(t) for t in (battery.get("toolbelt") or [])]
    timeout = int(args.timeout or battery.get("timeout_seconds") or 240)

    # The operator's own toolbelt is restored afterwards — the file is theirs.
    from frontend import eve_toolbelt

    results: list[dict[str, Any]] = []
    with eve_toolbelt.temporary_active_tools(toolbelt):
        for case in cases:
            prompt = str(case.get("prompt") or "")
            expected_route = str(case.get("route") or "")
            started = time.time()
            records, error = _stream_turn(prompt, toolbelt, timeout)
            evidence = live_probe.read_turn(records, prompt=prompt)
            route, expected_tools = live_probe.expected_tools_for(prompt)
            require_tool = bool(case.get("require_tool", True))
            # A case that may be satisfied by prefetched evidence has no tool
            # requirement -- only a FOREIGN tool is a failure there.
            allowed = expected_tools if require_tool else []
            verdict = live_probe.assert_correct_tool(evidence, prompt, allowed=allowed)
            if expected_route and route != expected_route:
                verdict = {
                    **verdict,
                    "ok": False,
                    "reason": (
                        f"route mismatch: battery expects {expected_route!r} "
                        f"but the shared classifier says {route!r}"
                    ),
                }
            row = {
                "id": str(case.get("id") or ""),
                "prompt": prompt,
                "route": route,
                "expected_route": expected_route,
                "expected_tools": expected_tools,
                "require_tool": require_tool,
                "called": evidence.tools_called,
                "succeeded": evidence.succeeded_tools,
                "ok": bool(verdict.get("ok")) and not error,
                "reason": verdict.get("reason") or error,
                "seconds": round(time.time() - started, 1),
                "answered": bool(evidence.assistant_text.strip()),
                "note": str(case.get("note") or ""),
            }
            results.append(row)
            mark = "PASS" if row["ok"] else "FAIL"
            print(f"[{mark}] {row['id']:<20} route={row['route']:<7} called={row['called']} {row['seconds']}s")
            if not row["ok"]:
                print(f"       {row['reason']}")

    passed = [r for r in results if r["ok"]]
    summary = {
        "ok": len(passed) == len(results) and bool(results),
        "passed": len(passed),
        "failed": len(results) - len(passed),
        "cases": results,
    }
    print(f"\nlive routing: {len(passed)}/{len(results)} cases routed to the right tool")
    if args.json_out:
        out = Path(args.json_out)
        if not out.is_absolute():
            out = ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {out}")
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
