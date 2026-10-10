#!/usr/bin/env python3
"""Suggest intent-codex triggers from playbook Ask lines and tool one-liners.

Read-only harvest — prints JSON suggestions; does not modify intent-codex.json.

  .\\venv\\Scripts\\python.exe scripts\\harvest-intent-verbs.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = ROOT / "config" / "eve-capabilities" / "playbook"
TOOL_DOCS = ROOT / "config" / "eve-capabilities" / "tool-docs"

ASK_RE = re.compile(r'\*\*Ask:\*\*\s*"([^"]+)"', re.MULTILINE)
WORD_RE = re.compile(r"\b[a-z]{4,}\b")


def harvest_asks() -> list[str]:
    lines: list[str] = []
    for path in sorted(PLAYBOOK.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines.extend(ASK_RE.findall(text))
    return lines


def top_verbs(phrases: list[str], limit: int = 40) -> list[str]:
    counts: dict[str, int] = {}
    stop = {
        "what",
        "when",
        "where",
        "which",
        "that",
        "this",
        "with",
        "from",
        "have",
        "does",
        "your",
        "about",
        "into",
        "them",
        "they",
        "will",
        "would",
        "should",
        "could",
        "there",
        "then",
        "only",
        "just",
        "also",
        "some",
        "make",
        "give",
        "tell",
        "need",
        "want",
    }
    for phrase in phrases:
        for word in WORD_RE.findall(phrase.casefold()):
            if word in stop:
                continue
            counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [word for word, _ in ranked[:limit]]


def main() -> int:
    asks = harvest_asks()
    verbs = top_verbs(asks)
    payload = {
        "ask_samples": asks[:25],
        "ask_count": len(asks),
        "suggested_verbs_for_codex_review": verbs,
        "note": "Merge useful verbs/phrases into config/eve-capabilities/intent-codex.json by intent id.",
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
