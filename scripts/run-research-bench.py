"""Research bench runner — prove the hole before building for it, then prove the fix.

Two modes, deliberately separate:

    # No model needed: does a callable tool exist for each named need? (reads the tool registry)
    .\\venv\\Scripts\\python.exe scripts\\run-research-bench.py --baseline

    # Real turns against the running Workbench, graded by the same rules the tests use
    $env:EMPIRE_TRACE='1'
    .\\venv\\Scripts\\python.exe scripts\\run-research-bench.py --live --out eve-audit\\research-bench-live.json

`--baseline` is the ticket `docs/RESEARCH_CLOSURE.md` asks for: it names, from the repo, exactly
which of the Architect's asks no tool can serve. `--require-ready` turns it into a gate — use it
once the capability has been built (it fails while a need is still blocked).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline import research_bench as bench  # noqa: E402

ORIGIN = "http://127.0.0.1:8080"
TRACE_PATH = ROOT / "eve-audit" / "eve-trace.jsonl"


def _req(method: str, path: str, payload: dict[str, Any] | None = None, *, timeout: float = 120) -> tuple[int, Any]:
    data = None
    headers = {"Origin": ORIGIN, "Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(ORIGIN + path, data=data, headers=headers, method=method)
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
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": str(exc)}


def stream_final_text(session_id: str, *, max_seconds: float = 240) -> str:
    """Read the answer out of the projected NDJSON stream (same contract as the wiki calibrate)."""

    url = f"{ORIGIN}/api/eve/session/{session_id}/stream?startIndex=0"
    request = urllib.request.Request(url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"})
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
            kind = str(event.get("type") or "")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if kind == "message.appended":
                final = str(data.get("messageSoFar") or final)
            if kind == "message.completed":
                content = data.get("text") or data.get("content") or data.get("messageSoFar")
                if content:
                    final = str(content)
            if kind == "session.waiting":
                break
    return final


def _trace_offset() -> int:
    return TRACE_PATH.stat().st_size if TRACE_PATH.exists() else 0


def _tools_since(offset: int) -> list[str]:
    """Tool names requested since `offset` — the trace is the only honest source of this."""

    names: list[str] = []
    if not TRACE_PATH.exists():
        return names
    with TRACE_PATH.open(encoding="utf-8") as handle:
        handle.seek(offset)
        for line in handle:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if record.get("kind") == "tool.requested":
                names.extend(str(name) for name in (record.get("tools") or []))
    return names


def _print_baseline(payload: dict[str, Any]) -> None:
    for row in payload["rows"]:
        print(f"  {row['id']:6s} {row['needs']:9s} {row['verdict']:8s} {row['reason']}")
    print(
        f"\n  cases={payload['cases']}  ready={payload['ready']}  blocked={payload['blocked']}"
        f"  blocked_needs={payload['blocked_needs'] or 'none'}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="EMPIRE research bench")
    parser.add_argument("--baseline", action="store_true", help="Capability baseline from the repo")
    parser.add_argument("--live", action="store_true", help="Run the cases against the Workbench")
    parser.add_argument("--case", default="", help="Limit to one case id")
    parser.add_argument(
        "--require-ready",
        action="store_true",
        help="Exit 1 while any case's need has no callable tool (use after the fix)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a table")
    parser.add_argument("--out", type=Path, default=None, help="Write the JSON summary here")
    args = parser.parse_args()

    cases = bench.load_cases()
    if args.case:
        cases = [case for case in cases if case.get("id") == args.case]
        if not cases:
            print(f"no case {args.case!r} in {bench.bench_path()}")
            return 2

    if not args.live:
        payload = bench.capability_baseline(cases)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print("=== Research bench — capability baseline (no model needed) ===")
            _print_baseline(payload)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        if args.require_ready and not payload["ok"]:
            print(f"\nBLOCKED: no callable tool for {payload['blocked_needs']}")
            return 1
        return 0

    print("=== Research bench — live turns ===")
    if not TRACE_PATH.exists():
        print("  WARNING: no trace file — tool evidence is invisible, so grades read pessimistic.")
        print("  Start the Workbench with EMPIRE_TRACE=1 for an honest run.")
    results: list[dict[str, Any]] = []
    for case in cases:
        query = str(case.get("query") or "")
        offset = _trace_offset()
        status, payload = _req(
            "POST",
            "/api/eve/session",
            {"message": query, "mode": "fast", "active_tools": ["wiki_local"]},
        )
        if status >= 400 or not isinstance(payload, dict) or not payload.get("sessionId"):
            reason = payload.get("error") if isinstance(payload, dict) else payload
            results.append(
                {
                    "id": case.get("id"),
                    "needs": case.get("needs"),
                    "passed": False,
                    "issues": [f"session failed ({status}: {reason})"],
                    "evidence": {"tools": [], "cited_url": False, "chars": 0},
                }
            )
            print(f"  {case.get('id'):6s} FAIL  session failed ({status})")
            continue
        answer = stream_final_text(str(payload["sessionId"]))
        tools = _tools_since(offset)
        result = bench.grade(case, answer=answer, tools=tools)
        results.append(result)
        flag = "pass" if result["passed"] else "FAIL"
        print(f"  {result['id']:6s} {flag}  tools={tools or 'none'}  {result['issues'] or ''}")

    summary = bench.summarise(results)
    print(f"\n  passed={summary['passed']}/{summary['cases']}  per_need={summary['per_need']}")
    if args.json:
        print(json.dumps({"results": results, "summary": summary}, indent=2, default=str))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            json.dumps({"results": results, "summary": summary}, indent=2, default=str),
            encoding="utf-8",
        )
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
