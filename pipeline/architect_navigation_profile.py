"""Build Architect navigation profile — likes, friction, issues, response style.

Sources: Obsidian SBX_Vault (primary) + Memory_Bank (secondary), same scoring as
companion_profile. Output is Cognee fuel + a workbench card for optional reading.

  .\\venv\\Scripts\\python.exe -m pipeline.architect_navigation_profile build
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from pipeline.companion_profile import (
    DEFAULT_MEMORY_BANK,
    DEFAULT_SBX_VAULT,
    FRICTION_RE,
    collect_scored,
)

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
RAW_OUT = (
    EMPIRE_ROOT
    / "data"
    / "curated_primitives"
    / "raw_materials"
    / "architect-navigation-profile.md"
)
WORKBENCH_CARD = Path(r"C:\Empire_Workbench\00_Core_Profile\ARCHITECT_NAVIGATION.md")

SKIP_NOTE = re.compile(
    r"(clippings|zettelkasten|lexicon|listening guide|gemini genie)",
    re.I,
)
LIKE_RE = re.compile(
    r"\b(like|love|enjoy|prefer|helpful|improvement|step in the right|"
    r"good choice|works for me|proud|better than|healthier|count as a win)\b",
    re.I,
)
FRUSTRATION_RE = re.compile(
    r"\b(frustrat|stuck|apathy|exhaust|overwhelm|annoy|hate it when|"
    r"error hell|dead end|spinning|blocked|nag|ignore my request|"
    r"not everything has to be completely successful)\b",
    re.I,
)
ISSUE_TECH_RE = re.compile(
    r"\b(n8n|docker|ngrok|tokens|timeout|elevation|exfat|vhdx|"
    r"ollama|gemini|ide|troubleshoot|points of failure|mount|backup|format)\b",
    re.I,
)
STYLE_RE = re.compile(
    r"\b(plain english|basic terms|full file|language barrier|"
    r"jargon|how i talk|without effort|fool's errand|snail's pace|"
    r"jumping into development too early|small verified|close the loop)\b",
    re.I,
)
FIRST_PERSON = re.compile(r"\b(I|I'm|I've|my|me)\b", re.I)
SENTENCE_SKIP = re.compile(
    r"(^As an AI|^Below is a \"master prompt\"|^Your first message was my|"
    r"^The AI now knows|^When you ask me to `ELI5`|^Hello! I am Lexicon)",
    re.I,
)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


@dataclass(frozen=True)
class Evidence:
    category: str
    sentence: str
    note: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _note_allowed(path: Path) -> bool:
    rel = str(path)
    if SKIP_NOTE.search(rel):
        return False
    if "gemini" in path.name.casefold() and "clippings" in rel.casefold():
        return False
    return True


def _sentences(text: str) -> list[str]:
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    body = re.sub(r"^#+\s.*$", "", body, flags=re.M)
    parts = SENTENCE_SPLIT.split(body.replace("\n", " "))
    out: list[str] = []
    for part in parts:
        s = re.sub(r"\s+", " ", part).strip()
        if "as an ai" in s.casefold() or "i am lexicon" in s.casefold():
            continue
        if 24 <= len(s) <= 320 and FIRST_PERSON.search(s) and not SENTENCE_SKIP.search(s):
            out.append(s)
    return out


def classify_sentence(sentence: str) -> str | None:
    if STYLE_RE.search(sentence):
        return "response_style"
    if FRUSTRATION_RE.search(sentence) or FRICTION_RE.search(sentence):
        return "frustrations"
    if ISSUE_TECH_RE.search(sentence):
        return "issues"
    if LIKE_RE.search(sentence):
        return "likes"
    return None


def collect_evidence(vault: Path, memory_bank: Path) -> list[Evidence]:
    notes = collect_scored(sbx_vault=vault, memory_bank=memory_bank)
    seen: set[str] = set()
    evidence: list[Evidence] = []
    for note in notes:
        if note.source == "sbx" and not _note_allowed(note.path):
            continue
        for sentence in _sentences(note.body):
            cat = classify_sentence(sentence)
            if not cat:
                continue
            key = (cat, sentence.casefold())
            if key in seen:
                continue
            seen.add(key)
            evidence.append(
                Evidence(category=cat, sentence=sentence, note=note.path.name)
            )
    return evidence


def _pick(evidence: list[Evidence], category: str, limit: int) -> list[Evidence]:
    return [e for e in evidence if e.category == category][:limit]


def navigation_rules_block() -> str:
    return """## How Eve should navigate (derived rules)

Use with `architect-eve-language-bridge.md` and `resolve_intent`. Recall this doc when tone or pace feels off.

1. **Plain goals, not tool sermons** — answer in his words; one clear next step.
2. **Energy over calendar** — short windows beat multi-day plans; celebrate small verified wins (`close the loop`).
3. **Friction → shrink the step** — when he sounds stuck, apathetic, or in "error hell", propose the smallest verifiable move, not a new architecture.
4. **Scanner-aware** — novelty is normal; validate what was learned before pushing a brand-new stack.
5. **Technical load** — he has hit Docker/n8n/tokens/mount/backup issues repeatedly; be precise, local-first, fail loud — never invent cloud or drive state.
6. **Life load is real** — notes mention work, health, and home stress; be steady and practical, do not pry or catalogue other people.
7. **Humor** — dry/gallows humor is OK when it matches his tone; substance first.
8. **Corrections** — if he updates a fact, `architect_now_update` / ARCHITECT_NOW wins over old journals.
9. **Language** — `lookup` = local files/memory first; `research` = broader; `scrape` = web_scout when admitted.
"""


def build_markdown(vault: Path, memory_bank: Path, evidence: list[Evidence]) -> str:
    parts = [
        "---",
        "title: Architect navigation profile (likes, friction, issues)",
        "dataset: eve_core",
        "fuel: architect_voice",
        "companion: architect-eve-language-bridge.md",
        f"generated: {_utc_now()}",
        "---",
        "",
        "# Architect navigation profile",
        "",
        f"Built from `{vault}` (+ Memory_Bank). **Evidence lines are his words** from notes; "
        "Gemini/clipping/model paste is excluded. Use for **tone and pace**, not as task truth.",
        "",
        navigation_rules_block(),
        "",
        "## What he likes / what helps",
        "",
    ]
    likes = _pick(evidence, "likes", 35)
    parts.extend(f"- ({e.note}) {e.sentence}" for e in likes) if likes else parts.append("- _(thin — add journals)_")
    parts.extend(["", "## Frustrations", ""])
    fr = _pick(evidence, "frustrations", 35)
    parts.extend(f"- ({e.note}) {e.sentence}" for e in fr) if fr else parts.append("- _(thin)_")
    parts.extend(["", "## Issues he has hit (tech + process)", ""])
    iss = _pick(evidence, "issues", 35)
    parts.extend(f"- ({e.note}) {e.sentence}" for e in iss) if iss else parts.append("- _(thin)_")
    parts.extend(["", "## How he asks to be met (response style)", ""])
    sty = _pick(evidence, "response_style", 25)
    parts.extend(f"- ({e.note}) {e.sentence}" for e in sty) if sty else parts.append("- _(thin)_")
    parts.extend(
        [
            "",
            "## Eve recall",
            "",
            '`cognee_recall("Architect navigation profile likes frustrations", dataset="eve_core")`',
            "",
            "Rebuild:",
            "",
            "```powershell",
            r".\venv\Scripts\python.exe -m pipeline.architect_navigation_profile build",
            r".\scripts\setup-architect-language-memory.ps1",
            "```",
            "",
        ]
    )
    return "\n".join(parts).rstrip() + "\n"


def build_card(md: str, *, max_chars: int = 1_200) -> str:
    """Compact card for workbench optional read (not auto-injected)."""
    lines = [ln for ln in md.splitlines() if ln.startswith("- (")]
    card = "Navigation hints (from SBX_Vault):\n" + "\n".join(lines[:12])
    if len(card) > max_chars:
        card = card[: max_chars - 1].rstrip() + "…"
    return card + "\n"


def build(
    *,
    sbx_vault: Path | None = None,
    memory_bank: Path | None = None,
) -> dict[str, object]:
    vault = sbx_vault or DEFAULT_SBX_VAULT
    bank = memory_bank or DEFAULT_MEMORY_BANK
    evidence = collect_evidence(vault, bank)
    md = build_markdown(vault, bank, evidence)
    RAW_OUT.parent.mkdir(parents=True, exist_ok=True)
    RAW_OUT.write_text(md, encoding="utf-8")
    try:
        WORKBENCH_CARD.parent.mkdir(parents=True, exist_ok=True)
        WORKBENCH_CARD.write_text(build_card(md), encoding="utf-8")
    except OSError:
        pass
    counts: dict[str, int] = {}
    for e in evidence:
        counts[e.category] = counts.get(e.category, 0) + 1
    return {
        "vault": str(vault),
        "raw_out": str(RAW_OUT),
        "workbench_card": str(WORKBENCH_CARD),
        "evidence_counts": counts,
        "evidence_total": len(evidence),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Architect navigation profile")
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("--sbx-vault", type=Path, default=None)
    build_parser.add_argument("--memory-bank", type=Path, default=None)
    args = parser.parse_args(argv)
    if args.command == "build":
        manifest = build(sbx_vault=args.sbx_vault, memory_bank=args.memory_bank)
        print(json.dumps(manifest, indent=2))
        return 0
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
