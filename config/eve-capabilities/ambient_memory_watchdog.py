"""Bounded JSONL-to-Cognee ambient memory worker."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from collections import deque
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ambient_events import event_text, memory_triggered, parse_event

ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = Path(os.environ.get("EMPIRE_AUDIT_LOG", ROOT / "eve-audit" / "active_chat.log"))
STATUS_PATH = LOG_PATH.with_name("ambient-memory-status.json")
OLLAMA_URL = os.environ.get("EMPIRE_OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/") + "/api/generate"
OLLAMA_MODEL = os.environ.get("EMPIRE_AMBIENT_MODEL", "qwen2.5:14b")
DATASET = "eve_ambient"
MAX_FACTS_PER_TURN = 1
MAX_FACTS_PER_HOUR = 10
MAX_TEXT_CHARS = 4000
COMMIT_TIMES: deque[float] = deque()


def write_status(payload: dict[str, Any]) -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def extract_fact(text: str, event_id: str, opener=urllib.request.urlopen) -> dict[str, str] | None:
    prompt = (
        "Extract at most one durable project fact from this successful user turn. "
        "Return JSON only with keys fact and reason. Return {\"fact\":\"\",\"reason\":\"\"} if none.\n\n"
        f"TURN:\n{text[:MAX_TEXT_CHARS]}"
    )
    payload = json.dumps({"model": OLLAMA_MODEL, "prompt": prompt, "stream": False, "format": "json"}).encode("utf-8")
    request = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with opener(request, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    raw = result.get("response", "") if isinstance(result, dict) else ""
    parsed = json.loads(raw) if isinstance(raw, str) else raw
    fact = parsed.get("fact", "") if isinstance(parsed, dict) else ""
    reason = parsed.get("reason", "") if isinstance(parsed, dict) else ""
    if not isinstance(fact, str) or not fact.strip() or len(fact) > 2000:
        return None
    return {"fact": fact.strip(), "reason": str(reason)[:500], "event_id": event_id}


def remember_fact(fact: dict[str, str]) -> None:
    content = json.dumps({"ambient_fact": fact["fact"], "provenance": fact}, ensure_ascii=False)
    command = [sys.executable, "-m", "pipeline.cognee_worker", "remember", "--content", content, "--dataset", DATASET]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=180, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Cognee worker failed")


def process_lines(lines, *, seen: set[str] | None = None, now=time.time) -> int:
    seen = seen if seen is not None else set()
    current_time = now()
    while COMMIT_TIMES and COMMIT_TIMES[0] <= current_time - 3600:
        COMMIT_TIMES.popleft()
    facts_this_turn = 0
    for line in lines:
        event = parse_event(line)
        if not event or not memory_triggered(event):
            continue
        event_id = str(event.get("event_id") or event.get("id") or "")
        if not event_id or event_id in seen or facts_this_turn >= MAX_FACTS_PER_TURN or len(COMMIT_TIMES) >= MAX_FACTS_PER_HOUR:
            continue
        seen.add(event_id)
        fact = extract_fact(event_text(event), event_id)
        if fact:
            remember_fact(fact)
            facts_this_turn += 1
            COMMIT_TIMES.append(current_time)
    return len(COMMIT_TIMES)


def follow(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    with path.open("r", encoding="utf-8") as stream:
        stream.seek(0, os.SEEK_END)
        while True:
            line = stream.readline()
            if line:
                yield line
            else:
                time.sleep(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--once", action="store_true", help="Process current lines and exit")
    args = parser.parse_args()
    if args.once:
        if not LOG_PATH.exists():
            return 0
        with LOG_PATH.open("r", encoding="utf-8") as stream:
            process_lines(stream)
        return 0
    write_status({"ok": True, "worker": "ambient-memory", "dataset": DATASET, "started_at": time.time()})
    for line in follow(LOG_PATH):
        try:
            process_lines([line])
        except Exception as exc:  # noqa: BLE001
            write_status({"ok": False, "worker": "ambient-memory", "error": str(exc), "updated_at": time.time()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())