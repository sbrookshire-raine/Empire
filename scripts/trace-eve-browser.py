"""Browser tracer: every HTTP hop + the server-side event/tool timeline for one turn.

Answers "where do the ~90 seconds go, and does anything loop?" from the browser the Architect
actually uses. The server timeline is grouped by the per-turn `turn` id (E-18), so a second
session in flight — another tab, the voice router, a harness — cannot be read as this run's.

Start the Workbench with tracing on first:

    $env:EMPIRE_TRACE='1'; .\\venv\\Scripts\\python.exe -m frontend.serve

Then:

    $env:PYTHONPATH='C:\\EMPIRE'
    .\\venv\\Scripts\\python.exe scripts\\trace-eve-browser.py
    .\\venv\\Scripts\\python.exe scripts\\trace-eve-browser.py --headful --question "..."
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

_EMPIRE_ROOT = Path(__file__).resolve().parents[1]
if str(_EMPIRE_ROOT) not in sys.path:
    sys.path.insert(0, str(_EMPIRE_ROOT))

ORIGIN = "http://127.0.0.1:8080"
TRACE_PATH = _EMPIRE_ROOT / "eve-audit" / "eve-trace.jsonl"
OUT_PATH = _EMPIRE_ROOT / "eve-audit" / "browser-trace.jsonl"
DEFAULT_QUESTION = "What can you tell me about the band the white stripes?"
INTERESTING = re.compile(r"/api/(eve|voice|toolbelt|memory|chat-history)")
TIMEOUT_S = 300


def _clear_active_chat() -> None:
    """Drop the Workbench's active-chat pointer so no rolling summary skews the trace.

    Without this the model answers "I already provided that" from the previous turn's digest
    and never calls a wiki tool — which hides the tool latency we are hunting.
    """

    request = urllib.request.Request(
        f"{ORIGIN}/api/chat-history/active",
        headers={"Origin": ORIGIN},
        method="DELETE",
    )
    try:
        with urllib.request.urlopen(request, timeout=5):
            pass
    except Exception:  # noqa: BLE001
        pass


def _toolbelt(tools: list[str]) -> list[str]:
    with urllib.request.urlopen(f"{ORIGIN}/api/toolbelt", timeout=5) as resp:
        previous = list(json.loads(resp.read().decode("utf-8")).get("active_tools") or [])
    _restore_toolbelt(sorted(set(previous) | set(tools)), origin=ORIGIN)
    return previous


def _restore_toolbelt(tools: list[str], *, origin: str) -> None:
    """Restore a previously captured Toolbelt set."""

    payload = json.dumps({"active_tools": tools}).encode()
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


_post_toolbelt = _restore_toolbelt


def run(*, headful: bool, questions: list[str]) -> tuple[list[dict], list[dict]]:
    from playwright.sync_api import sync_playwright

    http: list[dict] = []
    turns: list[dict] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headful)
        page = browser.new_page()
        started: dict[str, float] = {}

        def on_request(request) -> None:
            if INTERESTING.search(request.url):
                started[request.url] = time.perf_counter()

        def on_response(response) -> None:
            url = response.url
            if not INTERESTING.search(url):
                return
            begun = started.pop(url, None)
            http.append(
                {
                    "url": url.replace(ORIGIN, ""),
                    "status": response.status,
                    "ms": round((time.perf_counter() - begun) * 1000, 1) if begun else None,
                }
            )

        def snapshot() -> tuple[list[str], bool]:
            try:
                texts = page.evaluate(
                    "() => Array.from(document.querySelectorAll("
                    "'.bubble--assistant:not(.bubble--thinking) .bubble__text'))"
                    ".map(function (n) { return n.innerText || ''; })"
                )
                busy = page.locator(".composer__send").get_attribute("aria-busy") == "true"
            except Exception:  # noqa: BLE001
                texts, busy = [], True
            return ([str(t) for t in texts] if isinstance(texts, list) else []), busy

        page.on("request", on_request)
        page.on("response", on_response)
        page.add_init_script("try { localStorage.clear(); } catch (e) {}")
        page.goto(f"{ORIGIN}/eve.html", wait_until="domcontentloaded", timeout=30_000)
        page.wait_for_selector("#chat-message", timeout=15_000)

        for question in questions:
            before = len(snapshot()[0])
            page.fill("#chat-message", question)
            t0 = time.perf_counter()
            page.click(".composer__send")
            idle = 0
            texts: list[str] = []
            deadline = time.time() + TIMEOUT_S
            while time.time() < deadline:
                texts, busy = snapshot()
                if not busy and len(texts) > before:
                    idle += 1
                    if idle >= 4:
                        break
                else:
                    idle = 0
                time.sleep(0.4)
            elapsed = time.perf_counter() - t0
            added = len(texts) - before
            turns.append(
                {
                    "question": question,
                    "seconds": round(elapsed, 1),
                    "bubbles": added,
                    "texts": texts[before:],
                }
            )
            print(f"  > {question[:60]!r}: {elapsed:5.1f}s  bubbles_added={added}")
            for index, text in enumerate(texts[before:], 1):
                print(f"      [{index}] {text.strip()[:80]!r}")
        browser.close()
    return http, turns


UNATTRIBUTED = "(no turn id)"


def _describe(record: dict) -> str | None:
    """One printable line for the trace records this probe cares about."""

    kind = record.get("kind")
    if kind == "tool.requested":
        return f"tool.requested  {record.get('tools')}"
    if kind == "tool.result":
        return f"tool.result     {record.get('ms')} ms"
    if kind == "stream.end":
        return f"stream.end      {record.get('seconds')}s"
    if kind == "event" and record.get("type") in {"turn.completed", "session.waiting"}:
        return f"event           {record.get('type')}"
    return None


def _read_new_records(offset: int) -> list[dict]:
    """Read the trace records written since `offset` (the size before the run)."""

    records: list[dict] = []
    if not TRACE_PATH.exists():
        return records
    with TRACE_PATH.open(encoding="utf-8") as handle:
        handle.seek(offset)
        for line in handle:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def _group_by_turn(records: list[dict]) -> list[dict]:
    """Group records by the `turn` id minted per browser turn (E-18).

    Without this, a second session in flight (another tab, the voice router, a harness)
    interleaves its tool events into this run's timeline. Records that carry no turn id —
    written before E-18, or by something else — are kept together and labelled rather than
    being silently attributed to this run.
    """

    groups: dict[str, dict] = {}
    order: list[str] = []
    for record in records:
        key = str(record.get("turn") or "") or UNATTRIBUTED
        group = groups.get(key)
        if group is None:
            group = {"key": key, "start": None, "lines": []}
            groups[key] = group
            order.append(key)
        if record.get("kind") == "turn.start":
            group["start"] = record
            continue
        line = _describe(record)
        if line:
            group["lines"].append(line)
    return [groups[key] for key in order]


def _print_turn_trace(offset: int) -> None:
    print("\n=== Server trace (per turn: tools + timings) ===")
    groups = _group_by_turn(_read_new_records(offset))
    if not groups:
        print("  (no records after the mark — start the Workbench with EMPIRE_TRACE=1)")
        return
    for group in groups:
        start = group["start"] or {}
        header = (
            f"model={start.get('model') or '?'} mode={start.get('mode') or '?'} "
            f"session={start.get('session') or '-'} "
            f"{str(start.get('message') or '')[:48]!r}"
        )
        label = group["key"] if group["key"] == UNATTRIBUTED else group["key"][:12]
        print(f"  turn {label}  {header}")
        for line in group["lines"]:
            print(f"    {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Browser + server trace for Eve turns")
    parser.add_argument("--headful", action="store_true")
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--questions",
        default="",
        help="Pipe-separated multi-turn script (overrides --question)",
    )
    args = parser.parse_args()

    questions = (
        [q.strip() for q in args.questions.split("|") if q.strip()]
        if args.questions
        else [args.question]
    )

    if not TRACE_PATH.exists():
        print(f"NOTE: {TRACE_PATH.name} not found — start the Workbench with EMPIRE_TRACE=1")
    before = TRACE_PATH.stat().st_size if TRACE_PATH.exists() else 0
    _clear_active_chat()
    previous = _toolbelt(["wiki_local", "voice_presence"])
    try:
        http, turns = run(headful=args.headful, questions=questions)
    except ImportError:
        print("SKIP: playwright not installed")
        return 0
    finally:
        _restore_toolbelt(previous, origin=ORIGIN)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("a", encoding="utf-8") as handle:
        for record in http:
            handle.write(json.dumps(record, default=str) + "\n")

    print("\n=== Bubbles per question (1 = healthy, >1 = doubling) ===")
    doubled = [turn for turn in turns if turn["bubbles"] > 1]
    for turn in turns:
        flag = "DOUBLE" if turn["bubbles"] > 1 else "ok    "
        print(f"  {flag}  {turn['seconds']:5.1f}s  bubbles={turn['bubbles']}  {turn['question'][:52]}")

    _print_turn_trace(before)

    if doubled:
        print(f"\nRESULT: {len(doubled)} question(s) rendered multiple assistant bubbles")
        return 1
    print("\nRESULT: one bubble per question")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())