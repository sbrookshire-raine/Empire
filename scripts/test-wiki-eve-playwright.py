"""Playwright smoke: Eve chat UI with Wiki Local for calibration question.

Requires: frontend :8080, Eve :2000, Ollama, Weaviate :8091 (Start-EMPIRE.bat -Weaviate).

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  .\\venv\\Scripts\\python.exe scripts\\test-wiki-eve-playwright.py
  .\\venv\\Scripts\\python.exe scripts\\test-wiki-eve-playwright.py --headful
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORIGIN = "http://127.0.0.1:8080"
DEFAULT_QUESTION = (
    "what popular 80s song got re-popularized during the later seasons of stranger things?"
)
MUST_CONTAIN = ("running up that hill",)
MUST_NOT = ("wow", "wiki_scout_compare_years")
TIMEOUT_MS = 240_000


def _frontend_up() -> bool:
    try:
        req = urllib.request.Request(f"{ORIGIN}/api/memory/status")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status < 400
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def _enable_wiki_local() -> None:
    payload = json.dumps({"active_tools": ["wiki_local", "voice_presence"]}).encode("utf-8")
    req = urllib.request.Request(
        f"{ORIGIN}/api/toolbelt",
        data=payload,
        headers={"Content-Type": "application/json", "Origin": ORIGIN},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10):
            pass
    except urllib.error.HTTPError:
        # Toolbelt route may differ; session payload still passes active_tools.
        pass


def run_playwright(*, headful: bool, question: str) -> list[str]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return ["playwright not installed"]

    errors: list[str] = []
    _enable_wiki_local()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headful)
        page = browser.new_page()
        page.goto(f"{ORIGIN}/eve.html", wait_until="domcontentloaded", timeout=30_000)
        page.wait_for_selector("#chat-message", timeout=15_000)

        textarea = page.locator("#chat-message")
        textarea.fill(question)
        page.locator(".composer__send").click()

        # Wait for assistant bubble after thinking indicator clears
        page.wait_for_selector(".bubble--assistant:not(.bubble--thinking)", timeout=TIMEOUT_MS)
        bubbles = page.locator(".bubble--assistant:not(.bubble--thinking) .bubble__text")
        count = bubbles.count()
        if count < 1:
            errors.append("no assistant bubble rendered")
            browser.close()
            return errors
        text = bubbles.nth(count - 1).inner_text(timeout=5_000)
        lowered = text.casefold()
        if not text.strip():
            errors.append("empty assistant text")
        for needle in MUST_CONTAIN:
            if needle not in lowered:
                errors.append(f"reply missing {needle!r}")
        for bad in MUST_NOT:
            if bad in lowered:
                errors.append(f"reply contains forbidden {bad!r}")
        browser.close()
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Playwright wiki Eve smoke")
    parser.add_argument("--headful", action="store_true")
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    if not _frontend_up():
        print("SKIP: frontend not reachable on 8080")
        return 0

    print("=== Playwright wiki Eve smoke ===")
    print("Q:", args.question[:80] + ("…" if len(args.question) > 80 else ""))
    errors = run_playwright(headful=args.headful, question=args.question)
    if errors:
        print("FAIL", errors)
        return 1
    print("PASS playwright wiki eve smoke")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
