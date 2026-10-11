"""Run Architect query battery: wiki green path (fast) + optional live Eve + REA routing.

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  $env:EMPIRE_WIKI_REPORTS_ROOT='D:\\EMPIRE_DATA\\wiki-reports'
  .\\venv\\Scripts\\python.exe scripts\\run-query-battery.py --tier fast
  .\\venv\\Scripts\\python.exe scripts\\run-query-battery.py --tier live
  .\\venv\\Scripts\\python.exe scripts\\run-query-battery.py --tier all
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
from typing import Any
from unittest.mock import patch

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

BATTERY_PATH = _ROOT / "config" / "eve-query-battery.json"
ORIGIN = "http://127.0.0.1:8080"


def _load_battery() -> dict[str, Any]:
    return json.loads(BATTERY_PATH.read_text(encoding="utf-8"))


def _needle_ok(needle: str, hay: str) -> bool:
    for alt in str(needle).split("|"):
        alt = alt.strip().casefold()
        if not alt:
            continue
        if re.search(rf"(?<![a-z0-9]){re.escape(alt)}(?![a-z0-9])", hay):
            return True
    return False


def _frontend_up() -> bool:
    try:
        with urllib.request.urlopen(f"{ORIGIN}/api/memory/status", timeout=5) as resp:
            return resp.status < 400
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def run_wiki_green(battery: dict[str, Any]) -> list[str]:
    from frontend.wiki_green_path import WIKI_GREEN_MARKER, build_green_path_block

    errors: list[str] = []
    for row in battery.get("wiki_green_path") or []:
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        budget = float(row.get("max_seconds") or 20)
        must = [str(x) for x in (row.get("must_contain") or [])]
        t0 = time.perf_counter()
        with patch("frontend.wiki_green_path.load_active_tools", return_value=["wiki_local"]):
            block = build_green_path_block(query)
        elapsed = time.perf_counter() - t0
        lowered = block.casefold()
        if elapsed > budget:
            errors.append(f"{qid}: green path slow ({elapsed:.1f}s > {budget}s)")
        if WIKI_GREEN_MARKER not in block:
            errors.append(f"{qid}: no green path block")
            continue
        for needle in must:
            if not _needle_ok(needle, lowered):
                errors.append(f"{qid}: green missing {needle!r}")
        print(f"  OK green  {qid}  {elapsed:.2f}s  len={len(block)}")
    return errors


def run_wiki_classify(battery: dict[str, Any]) -> list[str]:
    from frontend import wiki_drift_api
    from pipeline import intent_codex

    errors: list[str] = []
    for row in battery.get("wiki_classify") or []:
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        if row.get("expect_lookup") and not wiki_drift_api.is_wiki_lookup_query(query):
            errors.append(f"{qid}: is_wiki_lookup_query=False")
        title = str(row.get("expect_extract_title") or "")
        if title:
            got = wiki_drift_api.extract_search_query(query)
            if got != title:
                errors.append(f"{qid}: extract {got!r} != {title!r}")
        block = intent_codex.context_block(query)
        if "wiki_fact" not in block and wiki_drift_api.is_wiki_lookup_query(query):
            errors.append(f"{qid}: intent block missing wiki_fact")
        print(f"  OK classify  {qid}")
    return errors


def run_rea_routing(battery: dict[str, Any]) -> list[str]:
    from pipeline import intent_codex

    errors: list[str] = []
    for row in battery.get("rea_routing") or []:
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        expect = str(row.get("expect_intent") or "")
        result = intent_codex.resolve(query, min_score=4)
        primary = result.get("primary") or {}
        got = str(primary.get("id") or "")
        if expect and got != expect:
            errors.append(f"{qid}: intent {got!r} != {expect!r}")
        tools_any = row.get("expect_tools_any") or []
        if tools_any:
            local = [str(t) for t in (primary.get("local_tools") or [])]
            if not any(t in local for t in tools_any):
                errors.append(f"{qid}: tools {local!r} missing any of {tools_any}")
        print(f"  OK rea-route  {qid}  intent={got}")
    return errors


def _req_post_session(payload: dict[str, Any], *, timeout: float) -> tuple[int, dict[str, Any]]:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{ORIGIN}/api/eve/session",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Origin": ORIGIN,
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8", errors="replace"))
            return resp.status, body if isinstance(body, dict) else {}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(raw)
        except json.JSONDecodeError:
            return exc.code, {"raw": raw}


def _consume_stream_event(event: dict[str, Any], *, tools: list[str], final: str) -> str:
    et = str(event.get("type") or "")
    data = event.get("data") if isinstance(event.get("data"), dict) else {}
    if et == "actions.requested":
        for action in data.get("actions") or []:
            if isinstance(action, dict):
                tools.append(str(action.get("toolName") or ""))
    if et in {"message.appended", "message.completed"}:
        chunk = data.get("messageSoFar") or data.get("message") or data.get("text")
        if chunk:
            final = str(chunk)
    return final


def _stream_turn(session_id: str, *, max_seconds: float) -> dict[str, Any]:
    tools: list[str] = []
    final = ""
    timed_out = False
    waiting = False
    start_index = 0
    t0 = time.perf_counter()
    read_timeout = 90.0

    while time.perf_counter() - t0 < max_seconds and not waiting:
        url = f"{ORIGIN}/api/eve/session/{session_id}/stream?startIndex={start_index}"
        request = urllib.request.Request(
            url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"}
        )
        remaining = max(5.0, max_seconds - (time.perf_counter() - t0) + read_timeout)
        try:
            resp = urllib.request.urlopen(request, timeout=remaining)
        except (urllib.error.URLError, TimeoutError, OSError):
            timed_out = not final.strip()
            break
        with resp:
            sock = getattr(getattr(resp, "fp", None), "raw", None)
            if sock is not None and hasattr(sock, "_sock"):
                sock = sock._sock
            while time.perf_counter() - t0 < max_seconds:
                if sock is not None:
                    sock.settimeout(
                        min(read_timeout, max(1.0, max_seconds - (time.perf_counter() - t0)))
                    )
                try:
                    line = resp.readline()
                except (TimeoutError, OSError):
                    break
                if not line:
                    break
                try:
                    event = json.loads(line.decode("utf-8", errors="replace"))
                except json.JSONDecodeError:
                    continue
                proxy = event.get("_proxy") if isinstance(event.get("_proxy"), dict) else {}
                next_idx = proxy.get("upstreamNextIndex")
                if isinstance(next_idx, int):
                    start_index = max(start_index, next_idx)
                et = str(event.get("type") or "")
                data = event.get("data") if isinstance(event.get("data"), dict) else {}
                final = _consume_stream_event(event, tools=tools, final=final)
                if et == "session.waiting":
                    waiting = True
                    break
                if et in {"session.failed", "turn.failed", "proxy.error"}:
                    final = str(data.get("message") or final)
                    waiting = True
                    break

    if not waiting and not final.strip() and time.perf_counter() - t0 >= max_seconds - 1:
        timed_out = True
    return {
        "text": final,
        "tools": tools,
        "seconds": round(time.perf_counter() - t0, 1),
        "timed_out": timed_out,
    }


def run_wiki_session_inject(battery: dict[str, Any]) -> list[str]:
    """Confirm Workbench POST injects green wiki evidence (no LLM completion)."""

    errors: list[str] = []
    if not _frontend_up():
        print("  SKIP wiki session inject — frontend :8080 down")
        return errors
    for row in battery.get("wiki_session_inject") or []:
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        budget = float(row.get("max_seconds") or 25)
        must = [str(x) for x in (row.get("must_contain") or [])]
        t0 = time.perf_counter()
        status, payload = _req_post_session(
            {"message": query, "mode": "fast", "active_tools": ["wiki_local"]},
            timeout=min(60, budget + 30),
        )
        if status >= 400 or not payload.get("sessionId"):
            errors.append(f"{qid}: session POST failed {status}")
            continue
        sid = str(payload["sessionId"])
        received = ""
        url = f"{ORIGIN}/api/eve/session/{sid}/stream?startIndex=0"
        request = urllib.request.Request(
            url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"}
        )
        try:
            with urllib.request.urlopen(request, timeout=budget + 15) as resp:
                while time.perf_counter() - t0 < budget:
                    line = resp.readline()
                    if not line:
                        break
                    try:
                        event = json.loads(line.decode("utf-8", errors="replace"))
                    except json.JSONDecodeError:
                        continue
                    if str(event.get("type") or "") == "message.received":
                        data = event.get("data") if isinstance(event.get("data"), dict) else {}
                        received = str(data.get("message") or "")
                        break
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{qid}: stream read failed ({exc})")
            continue
        elapsed = time.perf_counter() - t0
        lowered = received.casefold()
        if not received.strip():
            errors.append(f"{qid}: no message.received event")
            continue
        for needle in must:
            if not _needle_ok(needle, lowered):
                errors.append(f"{qid}: inject missing {needle!r}")
        print(f"  OK session  {qid}  {elapsed:.2f}s  len={len(received)}")
    return errors


def run_wiki_live(battery: dict[str, Any], *, strict: bool = False) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    if not _frontend_up():
        print("  SKIP wiki live — frontend :8080 down")
        return errors
    for row in battery.get("wiki_live") or []:
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        budget = float(row.get("max_seconds") or 120)
        must = [str(x) for x in (row.get("must_contain") or [])]
        must_not = [str(x) for x in (row.get("must_not") or [])]
        status, payload = _req_post_session(
            {
                "message": query,
                "mode": "fast",
                "active_tools": ["wiki_local", "voice_presence"],
            },
            timeout=min(180, budget + 60),
        )
        if status >= 400 or not payload.get("sessionId"):
            errors.append(f"{qid}: session POST failed {status} {payload}")
            continue
        sid = str(payload["sessionId"])
        turn = _stream_turn(sid, max_seconds=budget)
        text = turn["text"]
        lowered = text.casefold()
        row_errors: list[str] = []
        optional = bool(row.get("optional"))
        if turn["seconds"] > budget:
            row_errors.append(f"{qid}: slow ({turn['seconds']}s > {budget}s)")
        if turn.get("timed_out") and not text.strip():
            row_errors.append(f"{qid}: stream idle timeout tools={turn['tools']}")
        elif not text.strip():
            row_errors.append(f"{qid}: empty reply tools={turn['tools']}")
        else:
            for needle in must:
                if not _needle_ok(needle, lowered):
                    row_errors.append(f"{qid}: missing {needle!r} in {text[:180]!r}")
            for bad in must_not:
                if bad.casefold() in lowered:
                    row_errors.append(f"{qid}: forbidden {bad!r}")
        if row_errors and optional and not strict:
            warnings.extend(row_errors)
            print(
                f"  WARN live  {qid}  {turn['seconds']}s  "
                f"(optional; Ollama may be busy) tools={turn['tools'][:4]}"
            )
        else:
            errors.extend(row_errors)
            print(
                f"  {'OK' if not row_errors else 'FAIL'} live  {qid}  "
                f"{turn['seconds']}s  tools={turn['tools'][:4]}"
            )
    for warn in warnings:
        print(f"  ~ {warn}")
    return errors


def run_rea_live(battery: dict[str, Any], *, strict: bool = False) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    if not _frontend_up():
        return errors
    for row in battery.get("rea_live") or []:
        if row.get("skip_if_no_eve"):
            pass
        qid = str(row.get("id") or "?")
        query = str(row.get("query") or "")
        budget = float(row.get("max_seconds") or 90)
        must = [str(x) for x in (row.get("must_contain") or [])]
        tools_on = list(row.get("active_tools") or ["rea", "wiki_local"])
        status, payload = _req_post_session(
            {"message": query, "mode": "fast", "active_tools": tools_on},
            timeout=budget + 60,
        )
        if status >= 400:
            errors.append(f"{qid}: session failed {status}")
            continue
        sid = str(payload.get("sessionId") or "")
        if not sid:
            errors.append(f"{qid}: no sessionId")
            continue
        turn = _stream_turn(sid, max_seconds=budget)
        lowered = turn["text"].casefold()
        row_errors: list[str] = []
        optional = bool(row.get("optional"))
        for needle in must:
            if not _needle_ok(needle, lowered):
                row_errors.append(f"{qid}: missing {needle!r}")
        if row_errors and optional and not strict:
            warnings.extend(row_errors)
            print(f"  WARN rea-live  {qid}  {turn['seconds']}s")
        else:
            errors.extend(row_errors)
            print(f"  {'OK' if not row_errors else 'FAIL'} rea-live  {qid}  {turn['seconds']}s")
    for warn in warnings:
        print(f"  ~ {warn}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Architect query battery")
    parser.add_argument(
        "--tier",
        choices=("fast", "live", "all"),
        default="fast",
        help="fast=green+classify+rea routing; live=+Eve stream; all=both",
    )
    parser.add_argument(
        "--strict-live",
        action="store_true",
        help="Fail live tier when optional cases stall (default: warn only).",
    )
    args = parser.parse_args()
    battery = _load_battery()
    print(f"Battery: {BATTERY_PATH.name}")
    all_errors: list[str] = []

    if args.tier in {"fast", "all"}:
        print("\n=== Wiki green path (server prefetch, ~seconds) ===")
        all_errors.extend(run_wiki_green(battery))
        print("\n=== Wiki classify + intent ===")
        all_errors.extend(run_wiki_classify(battery))
        print("\n=== REA intent routing ===")
        all_errors.extend(run_rea_routing(battery))
        print("\n=== Wiki session inject (POST + message.received) ===")
        all_errors.extend(run_wiki_session_inject(battery))

    if args.tier in {"live", "all"}:
        print("\n=== Wiki live Eve (Workbench stream) ===")
        all_errors.extend(run_wiki_live(battery, strict=args.strict_live))
        print("\n=== REA live (light) ===")
        all_errors.extend(run_rea_live(battery, strict=args.strict_live))

    if all_errors:
        print("\nFAIL", len(all_errors))
        for err in all_errors:
            print(" ", err)
        return 1
    print("\nPASS query battery", args.tier)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
