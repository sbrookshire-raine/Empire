"""Run wiki calibration cases from data/eval/wiki_calibrate.jsonl.

Modes (stack-dependent):
  injection  — offline enrich_eve_message_payload (fast, no Weaviate)
  retrieval  — Weaviate search + title expectations
  live_eve   — POST /api/eve/session + stream (needs 8080, 2000, Ollama)

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  .\\venv\\Scripts\\python.exe scripts\\run-wiki-calibrate.py
  .\\venv\\Scripts\\python.exe scripts\\run-wiki-calibrate.py --tier smoke --injection
  .\\venv\\Scripts\\python.exe scripts\\run-wiki-calibrate.py --retrieval --limit 10
  .\\venv\\Scripts\\python.exe scripts\\run-wiki-calibrate.py --live-eve --tier smoke
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from unittest.mock import patch

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSONL = EMPIRE_ROOT / "data" / "eval" / "wiki_calibrate.jsonl"
ORIGIN = "http://127.0.0.1:8080"

BAD_REPLY_MARKERS = (
    "stranger things have happened",
    "wiki_scout_compare_years",
    "rank_why",
    "kind_hint",
    '"wow"',
    "'wow'",
)


@dataclass
class CaseResult:
    id: str
    passed: bool
    issues: list[str] = field(default_factory=list)
    mode: str = ""


def load_cases(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if not str(row.get("query") or "").strip():
            continue
        if row.get("tier") == "import_pending":
            continue
        cases.append(row)
    return cases


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


def stream_final_text(session_id: str, *, max_seconds: float = 180) -> str:
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
            et = str(event.get("type") or "")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if et == "message.appended":
                final = str(data.get("messageSoFar") or final)
            if et == "message.completed":
                content = data.get("text") or data.get("content") or data.get("messageSoFar")
                if content:
                    final = str(content)
            if et == "session.waiting":
                break
    return final


def _forbid_checks(case: dict[str, Any], lowered: str, *, scope: str) -> list[str]:
    """Apply must_not_contain; live_eve-only forbids skip injection checks."""
    issues: list[str] = []
    for bad in case.get("must_not_contain") or []:
        if scope == "injection" and case.get("live_eve") and str(bad).casefold() == "wow":
            continue
        if str(bad).casefold() in lowered:
            issues.append(f"{scope} contains forbidden {bad!r}")
    return issues


def run_injection(case: dict[str, Any]) -> CaseResult:
    from frontend.wiki_drift_api import WIKI_LOOKUP_MARKER, enrich_eve_message_payload, is_wiki_lookup_query

    cid = str(case.get("id") or "?")
    query = str(case.get("query") or "")
    issues: list[str] = []
    if not is_wiki_lookup_query(query):
        issues.append("is_wiki_lookup_query=False")
    with patch("frontend.wiki_drift_api.load_active_tools", return_value=["wiki_local"]):
        enriched = enrich_eve_message_payload({"message": query})
    msg = str(enriched.get("message") or "")
    lowered = msg.casefold()
    if WIKI_LOOKUP_MARKER not in msg:
        issues.append("no WIKI_LOOKUP injection")
    for needle in case.get("must_contain") or []:
        if str(needle).casefold() not in lowered:
            issues.append(f"injection missing {needle!r}")
    issues.extend(_forbid_checks(case, lowered, scope="injection"))
    if "**rank:**" in lowered:
        issues.append("debug card dump in injection")
    return CaseResult(id=cid, passed=not issues, issues=issues, mode="injection")


def run_retrieval(case: dict[str, Any]) -> CaseResult:
    from pipeline.wiki_scout import compare_years, search

    cid = str(case.get("id") or "?")
    query = str(case.get("query") or "")
    year = str(case.get("year") or "2026")
    issues: list[str] = []
    mode = str(case.get("mode") or "lookup")
    if mode == "compare":
        result = compare_years(query, write_files=False)
        titles = []
        for year_cards in (result.get("cards_by_year") or {}).values():
            if isinstance(year_cards, list):
                for card in year_cards:
                    if isinstance(card, dict):
                        titles.append(str(card.get("title") or ""))
    else:
        result = search(query, year=year, write_files=False)
        titles = [str(t) for t in result.get("titles") or []]
    if not result.get("ok"):
        issues.append(f"retrieval failed: {result.get('error')}")
        return CaseResult(id=cid, passed=False, issues=issues, mode="retrieval")
    norm_titles = " | ".join(titles).casefold()
    expect_any = case.get("expect_title_any") or []
    if expect_any and not any(str(t).casefold() in norm_titles for t in expect_any):
        issues.append(f"no expected title in {titles[:5]!r}")
    for forbid in case.get("forbid_title") or []:
        if titles and str(forbid).casefold() in str(titles[0]).casefold():
            issues.append(f"forbidden title ranked first: {forbid!r}")
    return CaseResult(id=cid, passed=not issues, issues=issues, mode="retrieval")


def run_live_eve(case: dict[str, Any]) -> CaseResult:
    cid = str(case.get("id") or "?")
    query = str(case.get("query") or "")
    issues: list[str] = []
    status, payload = _req(
        "POST",
        "/api/eve/session",
        {"message": query, "mode": "fast", "active_tools": ["wiki_local"]},
        timeout=120,
    )
    if status >= 400 or not isinstance(payload, dict) or not payload.get("sessionId"):
        issues.append(f"session failed ({status})")
        return CaseResult(id=cid, passed=False, issues=issues, mode="live_eve")
    sid = str(payload["sessionId"])
    text = stream_final_text(sid, max_seconds=240)
    lowered = text.casefold()
    if not text.strip():
        issues.append("empty Eve reply")
    for needle in case.get("must_contain") or []:
        if str(needle).casefold() not in lowered:
            issues.append(f"reply missing {needle!r}")
    issues.extend(_forbid_checks(case, lowered, scope="reply"))
    for bad in BAD_REPLY_MARKERS:
        if str(bad).casefold() in lowered:
            issues.append(f"reply contains forbidden {bad!r}")
    return CaseResult(id=cid, passed=not issues, issues=issues, mode="live_eve")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run wiki calibration JSONL")
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--tier", default="", help="Filter by tier (smoke, calibrate, …)")
    parser.add_argument("--tag", default="", help="Filter cases containing this tag")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--injection", action="store_true")
    parser.add_argument("--retrieval", action="store_true")
    parser.add_argument("--live-eve", action="store_true")
    parser.add_argument("--all", action="store_true", help="Run all applicable modes per case flags")
    args = parser.parse_args()

    if not args.jsonl.is_file():
        print(f"Missing {args.jsonl} — run: python -m pipeline.wiki_driftbench_seed --merge-into {args.jsonl}")
        return 2

    cases = load_cases(args.jsonl)
    if args.tier:
        cases = [c for c in cases if str(c.get("tier") or "") == args.tier]
    if args.tag:
        cases = [c for c in cases if args.tag in (c.get("tags") or [])]
    if args.limit > 0:
        cases = cases[: args.limit]

    run_injection_flag = args.injection or args.all
    run_retrieval_flag = args.retrieval or args.all
    run_live_flag = args.live_eve or args.all
    if not (run_injection_flag or run_retrieval_flag or run_live_flag):
        run_injection_flag = True
        run_retrieval_flag = True

    frontend_up = _req("GET", "/api/memory/status", timeout=5)[0] < 400

    results: list[CaseResult] = []
    for case in cases:
        cid = str(case.get("id") or "?")
        if run_injection_flag and case.get("injection", True):
            results.append(run_injection(case))
        if run_retrieval_flag and case.get("retrieval", True):
            results.append(run_retrieval(case))
        if run_live_flag and case.get("live_eve") and frontend_up:
            results.append(run_live_eve(case))

    passed = sum(1 for r in results if r.passed)
    failed = [r for r in results if not r.passed]
    print(f"=== Wiki calibrate: {passed}/{len(results)} passed ({len(cases)} cases) ===")
    for result in results:
        mark = "OK" if result.passed else "FAIL"
        print(f"{mark} [{result.mode}] {result.id}")
        for issue in result.issues:
            print(f"    - {issue}")
    if failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
