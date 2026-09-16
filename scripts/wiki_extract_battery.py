"""EMPIRE wiki extract regression battery — CLI always; optional live Eve."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from frontend.wiki_drift_api import extract_search_query
from pipeline.wiki_extract import (
    format_extract_prose,
    is_extract_shaped_question,
    wiki_extract,
)
from pipeline.wiki_read_lead import prefer_section_for_question

CASES = [
    ("G1", "Extract the technical specifications table from the Nintendo Switch page.", "ok", ["ARMv8", "GM20B"], ["Multi-paradigm"], "specs table"),
    ("G2", "What paradigm field is listed for the Python programming language?", "ok", ["paradigm", "Multi-paradigm"], ["bytearray", "frozenset"], "infobox field"),
    ("G3", "Pull the U.S. television ratings table rows from The Following page.", "ok", ["11.87", "Season"], [], "ratings table"),
    ("G4", "Extract the See also list from the Cheese page.", "ok", ["List of cheeses", "Dairy"], [], "see also list"),
    ("G5", "Extract the See also list from the Linux page.", "ok", ["Comparison of Linux", "Linux From Scratch"], [], "see also list"),
    ("G6", "Extract the infobox fields from the Nintendo Switch page.", "ok", ["developer", "Nintendo"], ["ARMv8", "GM20B"], "infobox fields"),
    ("R1", "List items under the History section on the Cheese page.", "empty", [], ["8000 BCE", "Arab trader"], "prose history refuse"),
    ("R2", "What is the population of Zxqwy Blorf Band?", "miss", [], ["million", "inhabitants"], "hard miss"),
    ("R3", "Extract the population table from the Cheddar cheese page.", "empty", [], ["population is", "residents"], "missing structure"),
    ("R4", "Extract the technical specifications table from the PlayStation 2 page.", "empty", [], ["Emotion Engine", "300 MHz"], "no invent PS2 specs"),
    ("R5", "Pull the cast table rows from The Following page.", "empty", [], ["Kevin Bacon", "Ryan Hardy"], "no invent cast"),
]

LIVE_IDS = {"G1", "G2", "G3", "G4", "G6", "R1", "R2", "R4", "R5"}


def cli_run(case: tuple) -> dict:
    cid, q, expect, must, must_not, notes = case
    subject = extract_search_query(q) or q
    section = prefer_section_for_question(q) or ""
    out = wiki_extract(subject, "2026", need_hint=q, section=section, user_question=q)
    state = out.get("state") or ""
    if expect == "miss":
        ok = state == "empty" and (
            not out.get("canonical_title")
            or "not in title" in (out.get("refusal_reason") or "").casefold()
        )
    elif expect == "empty":
        ok = state in {"empty", "unsupported"} and bool(out.get("canonical_title"))
    else:
        ok = state == "ok"
    prose = format_extract_prose(out, max_chars=4000) if state == "ok" else (out.get("refusal_reason") or "")
    blob = prose.casefold()
    for m in must:
        if m.casefold() not in blob:
            ok = False
    for m in must_not:
        if m.casefold() in blob:
            ok = False
    # Structural expectations for polished cases
    if cid == "G2" and out.get("tables"):
        ok = False
    if cid == "G6" and out.get("tables"):
        ok = False
    if cid == "G3" and state == "ok":
        headers = (out.get("tables") or [{}])[0].get("headers") or []
        if len(headers) < 3 or headers[:2] == ["Property", "Value"]:
            ok = False
    return {
        "id": cid,
        "layer": "cli",
        "pass": ok,
        "expect": expect,
        "state": state,
        "shaped": is_extract_shaped_question(q),
        "subject": subject,
        "title": out.get("canonical_title"),
        "L": len(out.get("lists") or []),
        "T": len(out.get("tables") or []),
        "F": len(out.get("fields") or []),
        "notes": notes,
        "preview": prose[:200].replace("\n", " | "),
    }


def start_session(message: str) -> str:
    body = json.dumps(
        {"message": message, "mode": "fast", "active_tools": ["wiki_local"]},
    )
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write(body)
        path = f.name
    r = subprocess.run(
        [
            "curl.exe",
            "-s",
            "-S",
            "--max-time",
            "45",
            "-H",
            "Content-Type: application/json; charset=utf-8",
            "--data-binary",
            f"@{path}",
            "http://127.0.0.1:8080/api/eve/session",
        ],
        capture_output=True,
        text=True,
        timeout=50,
    )
    if r.returncode != 0:
        raise RuntimeError(f"session curl rc={r.returncode} stderr={r.stderr}")
    data = json.loads(r.stdout)
    sid = data.get("sessionId") or data.get("session_id")
    if not sid:
        raise RuntimeError(f"no sessionId in {data}")
    return sid


def stream_answer(sid: str, max_time: int = 70) -> str:
    out_path = ROOT / "tmp" / f"eve_batt_{sid[-8:]}.txt"
    out_path.parent.mkdir(exist_ok=True)
    subprocess.run(
        [
            "curl.exe",
            "-s",
            "-S",
            "-N",
            f"--max-time",
            str(max_time),
            f"http://127.0.0.1:8080/api/eve/session/{sid}/stream?startIndex=0",
            "-o",
            str(out_path),
        ],
        capture_output=True,
        text=True,
        timeout=max_time + 15,
    )
    text = out_path.read_text(encoding="utf-8", errors="replace") if out_path.exists() else ""
    final = ""
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except json.JSONDecodeError:
            continue
        typ = evt.get("type")
        data = evt.get("data") or {}
        if typ == "message.completed":
            final = data.get("message") or final
        elif typ == "message.appended":
            final = data.get("messageSoFar") or final
    return final


def grade_live(expect: str, answer: str, must, must_not) -> bool:
    blob = (answer or "").casefold()
    if not answer.strip():
        return False
    if any(x in blob for x in ("no specific task", "scratchpad", "available tools")):
        return False
    for m in must_not:
        if m.casefold() in blob:
            return False
    if expect == "ok":
        return all(m.casefold() in blob for m in must)
    refuse_ok = any(
        x in blob
        for x in (
            "did not return",
            "does not contain",
            "no structured",
            "not contain",
            "no usable",
            "cannot extract",
            "no cast",
            "no items",
            "population table",
            "not return a usable",
        )
    )
    return refuse_ok


def live_run(case: tuple) -> dict:
    cid, q, expect, must, must_not, notes = case
    try:
        sid = start_session(q)
        ans = stream_answer(sid)
        ok = grade_live(expect, ans, must, must_not)
        return {
            "id": cid,
            "layer": "live",
            "pass": ok,
            "expect": expect,
            "notes": notes,
            "chars": len(ans),
            "preview": (ans or "")[:240].replace("\n", " | "),
            "sid": sid,
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "id": cid,
            "layer": "live",
            "pass": False,
            "expect": expect,
            "notes": notes,
            "chars": 0,
            "error": str(exc),
            "preview": "",
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Wiki extract regression battery")
    parser.add_argument("--live", action="store_true", help="Also run live Eve sessions")
    parser.add_argument("--json-out", default="", help="Optional results JSON path")
    args = parser.parse_args(argv)

    cli_rows = [cli_run(c) for c in CASES]
    print("=== CLI ===")
    for r in cli_rows:
        mark = "PASS" if r["pass"] else "FAIL"
        print(f"{mark} {r['id']} state={r['state']} L={r['L']} T={r['T']} F={r['F']} | {r['notes']}")
        if not r["pass"]:
            print(f"     subject={r.get('subject')!r} title={r.get('title')!r}")
            print(f"     {r.get('preview')}")
    cli_pass = sum(1 for r in cli_rows if r["pass"])
    print(f"CLI {cli_pass}/{len(cli_rows)}")

    live_rows: list[dict] = []
    if args.live:
        print()
        print("=== LIVE EVE ===")
        live_rows = [live_run(c) for c in CASES if c[0] in LIVE_IDS]
        for r in live_rows:
            mark = "PASS" if r["pass"] else "FAIL"
            print(f"{mark} {r['id']} chars={r.get('chars', 0)} | {r['notes']}")
            if r.get("error"):
                print(f"     ERROR {r['error']}")
            else:
                print(f"     {r.get('preview')}")
        live_pass = sum(1 for r in live_rows if r["pass"])
        print(f"LIVE {live_pass}/{len(live_rows)}")
    else:
        live_pass = 0

    payload = {
        "cli": cli_rows,
        "live": live_rows,
        "cli_pass": cli_pass,
        "cli_total": len(cli_rows),
        "live_pass": live_pass,
        "live_total": len(live_rows),
    }
    out_path = Path(args.json_out) if args.json_out else ROOT / "tmp" / "wiki_extract_battery.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {out_path}")

    if cli_pass != len(cli_rows):
        return 1
    if args.live and live_pass != len(live_rows):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
