#!/usr/bin/env python3
"""Smoke: Eve hands stay visible — pulse, admit without Partner, GitHub scout, release.

Usage (stack up):
  .\\venv\\Scripts\\python.exe scripts\\smoke-eve-hands.py
  .\\venv\\Scripts\\python.exe scripts\\smoke-eve-hands.py --eve-chat
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
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYTHONPATH", str(ROOT))

FRONTEND = "http://127.0.0.1:8080"
EVE = "http://127.0.0.1:2000"


def _http_json(method: str, url: str, body: dict[str, Any] | None = None) -> tuple[int, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            try:
                return resp.status, json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                return resp.status, {"raw": raw[:500]}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(raw) if raw else {"error": str(exc)}
        except json.JSONDecodeError:
            return exc.code, {"error": str(exc), "raw": raw[:500]}


def check(name: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--eve-chat",
        action="store_true",
        help="Also send a live Eve turn that should use github_scout_search",
    )
    args = parser.parse_args()

    from pipeline import admission_controller, github_scout, resource_pulse
    from frontend import resource_pulse_api, wiki_drift_api

    print("=== Eve hands smoke ===")

    admission_controller.release_session("smoke-hands-start")
    admission_controller.set_research_partner(False)

    # 1) Wiki must not steal capability questions
    q = "What capabilities do you have right now, and what's free on the machine?"
    check(
        "capability Q is pulse-shaped",
        wiki_drift_api.is_resource_pulse_query(q),
    )
    check(
        "capability Q is not wiki lookup",
        not wiki_drift_api.is_wiki_lookup_query(q),
    )

    # 2) Pulse inject
    enriched = resource_pulse_api.enrich_eve_message_payload({"message": q})
    msg = str(enriched.get("message") or "")
    check(
        "pulse inject marker",
        resource_pulse_api.RESOURCE_PULSE_MARKER in msg,
        msg[msg.find("[[") : msg.find("[[") + 80] if "[[" in msg else "missing",
    )

    # 3) Live pulse
    snap = resource_pulse.pulse()
    check("pulse ok", bool(snap.get("ok")), str(snap.get("summary", ""))[:120])
    print(f"       can_admit_now={snap.get('can_admit_now')}")
    print(f"       effective={snap.get('inventory', {}).get('effective_tools')}")

    # 4) Admit without Research Partner
    admission_controller.release_session("smoke-hands-pre")
    admission_controller.set_research_partner(False)
    admit = resource_pulse.admit_for_goal("github_scout", "smoke-hands")
    check("admit_for_goal github_scout", bool(admit.get("ok")), str(admit.get("error") or ""))
    check(
        "capability_active without partner",
        admission_controller.capability_active("github_scout"),
    )
    check(
        "effective includes github_scout",
        "github_scout" in admission_controller.load_effective_tools(),
    )

    # 5) Built Eve bundle always registers github_scout_search as defineTool
    index = ROOT / "agents" / "empire-task-agent" / ".output" / "server" / "index.mjs"
    check("eve build index exists", index.is_file(), str(index))
    text = index.read_text(encoding="utf-8", errors="replace")
    # Always-on tool: defineTool near github_scout_search, not only defineDynamic turn.started
    check(
        "github_scout_search always defineTool",
        "github_scout_search_default = defineTool" in text
        or "var github_scout_search_default = defineTool" in text,
    )
    check("ensureLightCapability in build", "ensureLightCapability" in text)

    # 6) GitHub search (live network — may rate-limit)
    search = github_scout.search_repos("duckdb mcp", limit=3, note="smoke-hands")
    results = search.get("results") if isinstance(search.get("results"), list) else []
    check(
        "github_scout.search_repos runs",
        bool(search.get("ok")) and len(results) > 0
        or "rate" in str(search.get("error") or "").lower(),
        str(search.get("error") or f"results={len(results)}")[:160],
    )

    # 7) Release
    rel = admission_controller.release_session("smoke-hands-post")
    check("release session", bool(rel.get("ok")))
    check(
        "github inactive after release",
        not admission_controller.capability_active("github_scout"),
    )

    if args.eve_chat:
        print("--- live Eve chat ---")
        status, _ = _http_json("GET", f"{EVE}/eve/v1/info")
        check("Eve up", status == 200, f"HTTP {status}")
        status, sess = _http_json(
            "POST",
            f"{FRONTEND}/api/eve/session",
            {
                "message": (
                    "Call github_scout_search with query 'duckdb mcp server'. "
                    "Then briefly list repo names. Do not refuse."
                ),
                "toolbelt": {"active_tools": ["voice_presence", "wiki_local"]},
            },
        )
        check("Eve session create", status in (200, 201, 202), f"HTTP {status} {sess}")
        sid = sess.get("sessionId") or sess.get("session_id")
        check("session id", isinstance(sid, str) and bool(sid), str(sid))
        # Poll stream briefly for tool / github evidence
        deadline = time.time() + 180
        blob = ""
        start = 0
        saw_waiting = False
        while time.time() < deadline and not saw_waiting:
            url = f"{FRONTEND}/api/eve/session/{sid}/stream?startIndex={start}"
            try:
                req = urllib.request.Request(url, headers={"Accept": "application/x-ndjson"})
                with urllib.request.urlopen(req, timeout=90) as resp:
                    for line in resp:
                        line_s = line.decode("utf-8", errors="replace").strip()
                        if not line_s:
                            continue
                        blob += line_s + "\n"
                        try:
                            ev = json.loads(line_s)
                        except json.JSONDecodeError:
                            continue
                        if isinstance(ev.get("index"), int):
                            start = max(start, int(ev["index"]) + 1)
                        et = str(ev.get("type") or "")
                        if et in {"session.waiting", "turn.completed", "session.completed"}:
                            saw_waiting = True
                            break
            except Exception as exc:  # noqa: BLE001
                print(f"       stream note: {exc}")
                time.sleep(2)
        low = blob.casefold()
        print(f"       stream_chars={len(blob)} waiting={saw_waiting}")
        called = "github_scout_search" in low and "tool-call" in low
        refused = (
            "don't have direct access" in low
            or "do not have access to github" in low
            or "no access to external" in low
            or "don't have access to the internet" in low
            or "do not have access to the internet" in low
        )
        check(
            "Eve requested github_scout_search tool-call",
            called,
            "look for actions.requested / toolName github_scout_search",
        )
        check("Eve did not refuse GitHub access", not refused or called, low[:240])

    print("=== all smoke checks passed ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
