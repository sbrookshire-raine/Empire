"""Browser (Playwright) regression: voice turn shows scratch, or speaks gibberish.

Reproduces the 2026-09-23 report: "I used the mic, saw gibberish, then it called the tool,
showed output and started talking but only got a few words out."

The two faults it pins:

1. **Reasoning scratch reached the browser.** Deltas inside an open `<thought>` block carry no
   tag, so stateless filtering leaked the body — the UI then *spoke* "Ask: … Have: … Next: …".
   Fixed by `eve_proxy.ReasoningStreamFilter` + `cleanSpeechText` stripping blocks.
2. **Speech started mid-word and stopped early.** `voiceSpokenOffset` was a raw character
   offset into text that a later step replaces; the offset drifted into the middle of a
   sentence. Fixed by resetting the cursor when the consumed prefix no longer matches.

Usage:
  $env:PYTHONPATH='C:\\EMPIRE'
  .\\venv\\Scripts\\python.exe scripts\\test-eve-browser-playwright.py
  .\\venv\\Scripts\\python.exe scripts\\test-eve-browser-playwright.py --headful --question "..."
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

_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))

ORIGIN = "http://127.0.0.1:8080"
DEFAULT_QUESTION = "What can you tell me about the band the white stripes?"
MUST_CONTAIN = ("white stripes",)
MUST_NOT_CONTAIN = ("<thought", "Ask:", "Have:", "Next:")
REASONING_RE = re.compile(r"<(?:thought|thinking|think|reasoning)\b", re.I)
NONLATIN_RE = re.compile(
    r"^[\s\u0e00-\u0e7f\u4e00-\u9fff\u3040-\u30ff\u0400-\u04ff\u0600-\u06ff\u0590-\u05ff]{3,}"
)
TIMEOUT_MS = 240_000


def _frontend_up() -> bool:
    try:
        with urllib.request.urlopen(f"{ORIGIN}/api/memory/status", timeout=5) as resp:
            return resp.status < 400
    except (urllib.error.URLError, TimeoutError, OSError):
        return False


def _toolbelt(*, add: tuple[str, ...], origin: str) -> list[str]:
    """Ensure tools are active for the browser turn; returns the previous set for restore."""

    def _get() -> list[str]:
        try:
            with urllib.request.urlopen(f"{origin}/api/toolbelt", timeout=5) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            return list(body.get("active_tools") or [])
        except Exception:  # noqa: BLE001
            return []

    def _post(tools: list[str]) -> None:
        payload = json.dumps({"active_tools": tools}).encode("utf-8")
        request = urllib.request.Request(
            f"{origin}/api/toolbelt",
            data=payload,
            headers={"Content-Type": "application/json", "Origin": origin},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=5):
                pass
        except Exception:  # noqa: BLE001
            pass

    previous = _get()
    _post(sorted(set(previous) | set(add)))
    return previous


def _restore_toolbelt(tools: list[str], *, origin: str) -> None:
    """Restore a previously captured Toolbelt set."""

    payload = json.dumps({"active_tools": tools}).encode("utf-8")
    request = urllib.request.Request(
        f"{origin}/api/toolbelt",
        data=payload,
        headers={"Content-Type": "application/json", "Origin": origin},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=5):
            pass
    except Exception:  # noqa: BLE001
        pass


def run_browser(*, headful: bool, question: str, wait_voice: float) -> list[str]:
    from playwright.sync_api import sync_playwright

    errors: list[str] = []
    speaks: list[str] = []
    snapshots: list[str] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headful)
        page = browser.new_page()

        def on_request(request) -> None:
            if "/api/voice/speak" not in request.url:
                return
            try:
                body = json.loads(request.post_data or "{}")
            except json.JSONDecodeError:
                body = {"text": request.post_data or ""}
            speaks.append(str(body.get("text") or ""))

        page.on("request", on_request)
        # Start from a clean Workbench chat pointer so the rolling summary does not make Eve
        # think she already answered this question.
        page.add_init_script("try { localStorage.clear(); } catch (e) {}")
        page.goto(f"{ORIGIN}/eve.html", wait_until="domcontentloaded", timeout=30_000)
        page.wait_for_selector("#chat-message", timeout=15_000)
        page.fill("#chat-message", question)
        page.click(".composer__send")

        deadline = time.time() + (TIMEOUT_MS / 1000)
        final = ""
        stable = 0
        while time.time() < deadline:
            try:
                rendered = page.evaluate(
                    "() => { const b = document.querySelectorAll("
                    "'.bubble--assistant:not(.bubble--thinking) .bubble__text');"
                    " return b.length ? b[b.length - 1].innerText : ''; }"
                )
                thinking = page.locator(".bubble--thinking").count()
            except Exception:  # noqa: BLE001 — page detaching mid-poll
                rendered, thinking = "", 0
            if rendered and (not snapshots or snapshots[-1] != rendered):
                snapshots.append(rendered)
            if rendered.strip():
                if rendered == final:
                    stable += 1
                else:
                    final = rendered
                    stable = 0
                # Answer finished: no thinking indicator and the text stopped changing.
                if stable >= 3 and not thinking:
                    break
            time.sleep(0.4)

        if wait_voice > 0:
            time.sleep(wait_voice)
        browser.close()

    # --- Bubble assertions -------------------------------------------------------------
    if not final.strip():
        errors.append("no assistant text rendered")
    else:
        lowered = final.casefold()
        for needle in MUST_CONTAIN:
            if needle.casefold() not in lowered:
                errors.append(f"reply missing {needle!r}")
        for bad in MUST_NOT_CONTAIN:
            if bad.casefold() in lowered:
                errors.append(f"reply shows scratch text {bad!r}")
        if NONLATIN_RE.match(final):
            errors.append("reply starts with non-Latin junk")
    for sample in snapshots:
        if REASONING_RE.search(sample):
            errors.append(f"streamed bubble showed reasoning: {sample[:80]!r}")
            break

    # --- Speech assertions -------------------------------------------------------------
    spoken = [text for text in speaks if text.strip()]
    for text in spoken:
        if REASONING_RE.search(text):
            errors.append(f"spoke reasoning scratch: {text[:90]!r}")
            break
    for text in spoken:
        if NONLATIN_RE.match(text):
            errors.append(f"spoke non-Latin junk: {text[:90]!r}")
            break
    if spoken and final.strip():
        words = final.strip().split()
        first = spoken[0].strip()
        if words and not first.casefold().startswith(words[0].casefold()[:4]):
            errors.append(
                f"speech starts mid-sentence: spoke {first[:70]!r} but reply starts "
                f"{' '.join(words[:3])!r}"
            )
        if words and words[0].casefold() not in " ".join(spoken).casefold():
            errors.append("spoken text does not reach the reply (stopped early?)")

    print(f"bubbles sampled: {len(snapshots)}")
    print(f"speak calls:     {len(spoken)}")
    for text in spoken[:6]:
        print("  speak:", repr(text[:110]))
    print("final reply:", repr(final.strip()[:200]) or "(empty)")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Eve browser voice/reasoning regression")
    parser.add_argument("--headful", action="store_true")
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--wait-voice",
        type=float,
        default=8.0,
        help="Seconds to keep listening for TTS calls after the reply renders",
    )
    parser.add_argument("--no-voice", action="store_true", help="Skip speech assertions")
    args = parser.parse_args()

    if not _frontend_up():
        print("SKIP: frontend not reachable on 8080")
        return 0

    print("=== Eve browser voice/reasoning regression ===")
    print("Q:", args.question[:90])
    previous = _toolbelt(add=("wiki_local", "voice_presence"), origin=ORIGIN)
    try:
        errors = run_browser(
            headful=args.headful,
            question=args.question,
            wait_voice=0.0 if args.no_voice else args.wait_voice,
        )
    except ImportError:
        print("SKIP: playwright not installed")
        return 0
    finally:
        # Leave the Architect's Toolbelt exactly as it was.
        _restore_toolbelt(previous, origin=ORIGIN)

    if errors:
        print("\nFAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("\nPASS browser voice/reasoning regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())