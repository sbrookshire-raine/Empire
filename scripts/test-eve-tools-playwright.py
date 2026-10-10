"""Playwright: Eve chat turn must call a real tool (resource_farm_run or github_scout_search).

Writes verified_hands on PASS when stack + Eve are up.

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  .\\venv\\Scripts\\python.exe scripts\\test-eve-tools-playwright.py
  .\\venv\\Scripts\\python.exe scripts\\test-eve-tools-playwright.py --headful
  .\\venv\\Scripts\\python.exe scripts\\test-eve-tools-playwright.py --tool github
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))

FRONTEND = "http://127.0.0.1:8080"
EVE = "http://127.0.0.1:2000"
TIMEOUT_SEC = 240


def _http_ok(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return resp.status < 500
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def _stream_session(message: str) -> tuple[bool, str, str]:
    """Create session and poll NDJSON stream for tool-call evidence."""
    payload = json.dumps(
        {
            "message": message,
            "toolbelt": {"active_tools": ["voice_presence", "wiki_local"]},
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{FRONTEND}/api/eve/session",
        data=payload,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read().decode("utf-8", errors="replace"))
    sid = body.get("sessionId") or body.get("session_id")
    if not isinstance(sid, str) or not sid:
        return False, "", "no session id"

    deadline = time.time() + TIMEOUT_SEC
    blob = ""
    start = 0
    assistant = ""
    while time.time() < deadline:
        url = f"{FRONTEND}/api/eve/session/{sid}/stream?startIndex={start}"
        try:
            sreq = urllib.request.Request(url, headers={"Accept": "application/x-ndjson"})
            with urllib.request.urlopen(sreq, timeout=90) as resp:
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
                    if et == "text-delta" and isinstance(ev.get("text"), str):
                        assistant += ev["text"]
                    if et in {"session.waiting", "turn.completed", "session.completed"}:
                        return True, blob, assistant
        except Exception as exc:  # noqa: BLE001
            blob += f"\nstream_err:{exc}\n"
            time.sleep(2)
    return False, blob, assistant


def run_playwright_ui(*, headful: bool, question: str) -> list[str]:
    from playwright.sync_api import sync_playwright

    errors: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not headful)
        page = browser.new_page()
        page.add_init_script("try { localStorage.clear(); } catch (e) {}")
        page.goto(f"{FRONTEND}/eve.html", wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_selector("#chat-message", timeout=20_000)
        page.fill("#chat-message", question)
        page.click(".composer__send")
        deadline = time.time() + TIMEOUT_SEC
        final = ""
        stable = 0
        while time.time() < deadline:
            rendered = page.evaluate(
                "() => { const b = document.querySelectorAll("
                "'.bubble--assistant:not(.bubble--thinking) .bubble__text');"
                " return b.length ? b[b.length - 1].innerText : ''; }"
            )
            thinking = page.locator(".bubble--thinking").count()
            if rendered.strip():
                if rendered == final:
                    stable += 1
                else:
                    final = rendered
                    stable = 0
                if stable >= 3 and not thinking:
                    break
            time.sleep(0.5)
        browser.close()
        if not final.strip():
            errors.append("no assistant bubble text in browser")
        else:
            print("browser reply:", repr(final[:240]))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--headful", action="store_true")
    parser.add_argument(
        "--tool",
        choices=("farm", "github", "both"),
        default="both",
        help="Which live Eve tool-call to require",
    )
    parser.add_argument("--skip-browser", action="store_true", help="API stream only")
    args = parser.parse_args()

    if not _http_ok(f"{FRONTEND}/eve.html"):
        print("SKIP: frontend not on 8080")
        return 0
    if not _http_ok(f"{EVE}/eve/v1/info"):
        print("FAIL: Eve not on 2000 — start stack first")
        return 1

    checks: list[dict] = []
    failures: list[str] = []

    if args.tool in ("farm", "both"):
        msg = (
            "Call resource_farm_run with no query to show the processed materials catalog. "
            "Summarize farmed_repo_count in one short paragraph. Do not refuse."
        )
        done, blob, assistant = _stream_session(msg)
        low = (blob + assistant).casefold()
        ok = "resource_farm_run" in low and "tool-call" in low
        checks.append({"name": "eve_resource_farm_run", "tool": "resource_farm_run", "ok": ok})
        if not ok:
            failures.append("Eve did not tool-call resource_farm_run")
        if not done:
            failures.append("resource_farm stream did not complete")

    if args.tool in ("github", "both"):
        msg = (
            "Call github_scout_search with query 'duckdb mcp server'. "
            "List one repo name. Do not refuse."
        )
        done, blob, assistant = _stream_session(msg)
        low = (blob + assistant).casefold()
        ok = "github_scout_search" in low and "tool-call" in low
        checks.append({"name": "eve_github_scout_search", "tool": "github_scout_search", "ok": ok})
        if not ok:
            failures.append("Eve did not tool-call github_scout_search")
        refused = "don't have access to github" in low or "do not have access to the internet" in low
        if refused and not ok:
            failures.append("Eve refused GitHub")

    if not args.skip_browser and args.tool == "farm":
        q = "Show processed materials catalog — use resource_farm_run."
        ui_errs = run_playwright_ui(headful=args.headful, question=q)
        failures.extend(ui_errs)

    from pipeline import verified_hands

    if not failures:
        verified_hands.write_verification(
            checks=checks,
            source="test-eve-tools-playwright",
            notes="Live Eve tool-call regression (stream + optional browser).",
        )
        print("PASS test-eve-tools-playwright")
        for c in checks:
            print(f"  OK {c.get('name')}")
        return 0

    print("FAIL test-eve-tools-playwright")
    for f in failures:
        print(" -", f)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
