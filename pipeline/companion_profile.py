"""Distill Architect companion understanding from Obsidian SBX_Vault (+ Memory_Bank).

Produces:
  C:\\Empire_Workbench\\00_Core_Profile\\ARCHITECT_COMPANION.md
  C:\\Empire_Workbench\\00_Core_Profile\\architect_companion_card.md
  C:\\Empire_Workbench\\00_Core_Profile\\architect_companion_manifest.json

Primary source is the Obsidian vault (personal voice). Memory_Bank is secondary.
Never writes into Cognee.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
WORKBENCH_ROOT = Path(r"C:\Empire_Workbench")
CORE_OUTPUT = WORKBENCH_ROOT / "00_Core_Profile"
COMPANION_FILE = CORE_OUTPUT / "ARCHITECT_COMPANION.md"
CARD_FILE = CORE_OUTPUT / "architect_companion_card.md"
MANIFEST_FILE = CORE_OUTPUT / "architect_companion_manifest.json"

DEFAULT_SBX_VAULT = Path(
    os.environ.get(
        "EMPIRE_SBX_VAULT",
        r"C:\Users\m69nr\OneDrive\Desktop\SBX_Vault",
    )
)
DEFAULT_MEMORY_BANK = WORKBENCH_ROOT / "01_Memory_Bank"

ALLOWED_SUFFIXES = {".md", ".txt"}
MAX_FILE_BYTES = 200_000
MIN_BODY_CHARS = 80
TOP_SOURCES = 40
EXCERPT_CHARS = 900
CARD_MAX_CHARS = 2_800
OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.environ.get("EMPIRE_COMPANION_MODEL", "qwen2.5:14b")

SKIP_DIR_NAMES = {
    ".obsidian",
    ".git",
    "node_modules",
    "__pycache__",
    ".trash",
}

PERSONAL_PATH_RE = re.compile(
    r"(evolve|gadget|irene|notie|daily|journal|past.?lives|future.?me|"
    r"down.?and.?out|choices|practice|drum|becky|eve)",
    re.IGNORECASE,
)
PERSONAL_BODY_RE = re.compile(
    r"(?:"
    r"\bI\b|\bI'?m\b|\bI'?ve\b|\bmy\b|\bme\b|"
    r"stuck|frustrated|exhausted|overwhelmed|anxious|lonely|"
    r"gallows|dark humor|laugh|sanity|keep going|"
    r"EMPIRE|Eve|Obsidian|Architect|workbench|"
    r"where I started|future me|from zero|start over"
    r")",
    re.IGNORECASE,
)
FRICTION_RE = re.compile(
    r"(stuck|frustrated|exhausted|overwhelmed|isn't working|not working|"
    r"burned out|spinning|can't|cannot|blocked|dead end|lost)",
    re.IGNORECASE,
)
HUMOR_RE = re.compile(
    r"(humor|gallows|dark|joke|laugh|absurd|hitchhiker|irony|sarcasm|wit)",
    re.IGNORECASE,
)
ORIGIN_RE = re.compile(
    r"(EMPIRE|Eve|FORGE|Rain|workbench|local.?AI|from zero|start over|evolve)",
    re.IGNORECASE,
)
TECH_NOISE_RE = re.compile(
    r"(npm install|docker compose|openapi|function\s*\(|class\s+\w+|SELECT\s+.+\s+FROM|"
    r"wikipedia|nobel prize|youtube\.com|\(00:\d{2}:\d{2}\))",
    re.IGNORECASE,
)
CLIPPING_PATH_RE = re.compile(r"(clippings?|zettelkasten)", re.IGNORECASE)


@dataclass(frozen=True)
class ScoredNote:
    path: Path
    score: int
    source: str  # "sbx" | "memory_bank"
    body: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_text(path: Path) -> str | None:
    try:
        size = path.stat().st_size
        if size == 0 or size > MAX_FILE_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return None


def score_note(path: Path, *, source: str, vault_root: Path | None) -> ScoredNote | None:
    body = _read_text(path)
    if body is None:
        return None
    stripped = body.strip()
    if len(stripped) < MIN_BODY_CHARS:
        return None

    rel = str(path)
    try:
        if vault_root is not None:
            rel = str(path.relative_to(vault_root))
    except ValueError:
        pass

    name = path.name
    score = 0

    if CLIPPING_PATH_RE.search(rel):
        score -= 40
    if TECH_NOISE_RE.search(body) and not PERSONAL_BODY_RE.search(body[:2000]):
        score -= 35
    if body.count("http") > 25:
        score -= 25

    if PERSONAL_PATH_RE.search(rel) or PERSONAL_PATH_RE.search(name):
        score += 40
    if re.search(r"evolve|start from zero|future me|down and out", rel, re.IGNORECASE):
        score += 50
    if re.search(r"gadget|irene|notie", rel, re.IGNORECASE):
        score += 30
    if re.search(r"1_SBX|daily_notes", rel, re.IGNORECASE):
        score += 35
    # Bulk PAST LIVES: only keep if personal voice is strong
    if re.search(r"past.?lives", rel, re.IGNORECASE):
        score -= 15
        past_hits = len(PERSONAL_BODY_RE.findall(body[:4000]))
        if past_hits < 4:
            score -= 40
        else:
            score += min(past_hits * 2, 30)

    personal_hits = len(PERSONAL_BODY_RE.findall(body[:6000]))
    score += min(personal_hits * 2, 40)
    if FRICTION_RE.search(body):
        score += 25
    if HUMOR_RE.search(body):
        score += 20
    if ORIGIN_RE.search(body) or ORIGIN_RE.search(name):
        score += 20

    head = body[:1200]
    if re.search(r"\bI\b|\bI'?m\b|\bI'?ve\b", head):
        score += 15

    if source == "sbx":
        score += 25
    else:
        score -= 5

    if score < 18:
        return None
    return ScoredNote(path=path, score=score, source=source, body=stripped)


def _iter_files(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    found: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        found.append(path)
    return found


def collect_scored(
    *,
    sbx_vault: Path,
    memory_bank: Path,
) -> list[ScoredNote]:
    ranked: list[ScoredNote] = []
    if sbx_vault.is_dir():
        for path in _iter_files(sbx_vault):
            note = score_note(path, source="sbx", vault_root=sbx_vault)
            if note is not None:
                ranked.append(note)
    else:
        print(f"SKIP missing SBX vault: {sbx_vault}", file=sys.stderr)

    if memory_bank.is_dir():
        for path in _iter_files(memory_bank):
            note = score_note(path, source="memory_bank", vault_root=None)
            if note is not None:
                ranked.append(note)
    else:
        print(f"SKIP missing Memory_Bank: {memory_bank}", file=sys.stderr)

    ranked.sort(key=lambda item: (-item.score, str(item.path).casefold()))
    return ranked


def _first_paragraphs(text: str, limit: int = EXCERPT_CHARS) -> str:
    cleaned = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    cleaned = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", cleaned)
    cleaned = re.sub(r"#+\s*", "", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "…"


def _bucket_notes(notes: list[ScoredNote]) -> dict[str, list[ScoredNote]]:
    buckets: dict[str, list[ScoredNote]] = {
        "started": [],
        "now": [],
        "friction": [],
        "helps": [],
        "threads": [],
    }
    for note in notes:
        rel = str(note.path)
        name = note.path.name
        body = note.body
        # Origin / reset journals
        if re.search(
            r"evolve|start from zero|from zero|future me|rebirth|chimera|"
            r"start as architech|graduation",
            rel,
            re.I,
        ):
            buckets["started"].append(note)
        # Current EMPIRE / Gadget / Eve focus (prefer path signals over body noise)
        if re.search(
            r"gadget|irene|notie|2026.?eve|empire|lego",
            rel,
            re.I,
        ) or re.search(r"2026\s*-\s*eve", name, re.I):
            buckets["now"].append(note)
        # Friction: require friction language or clear stuck titles
        if FRICTION_RE.search(body) or re.search(
            r"down and out|exhausted|burn|garbage can|drained",
            rel,
            re.I,
        ):
            buckets["friction"].append(note)
        # Humor / practices that help
        if HUMOR_RE.search(body) or re.search(
            r"choices|practice|drum|walk notes|good day",
            rel,
            re.I,
        ):
            buckets["helps"].append(note)
        # Active project threads
        if re.search(r"gadget|irene|notie|lego|drum|daily_notes", rel, re.I):
            buckets["threads"].append(note)
    return buckets


def _section_md(title: str, notes: list[ScoredNote], *, limit: int = 5) -> str:
    lines = [f"## {title}", ""]
    if not notes:
        lines.append("_No high-signal notes found for this section._")
        lines.append("")
        return "\n".join(lines)
    seen: set[str] = set()
    count = 0
    for note in notes:
        key = str(note.path)
        if key in seen:
            continue
        seen.add(key)
        count += 1
        if count > limit:
            break
        excerpt = _first_paragraphs(note.body, 700)
        lines.append(f"### {note.path.name}")
        lines.append(f"- source: `{note.path}`")
        lines.append(f"- score: {note.score} ({note.source})")
        lines.append("")
        lines.append(excerpt)
        lines.append("")
    return "\n".join(lines)


def _fill_bucket(
    bucket: list[ScoredNote],
    pool: list[ScoredNote],
    *,
    used: set[str],
    limit: int = 5,
) -> list[ScoredNote]:
    """Prefer unique notes per section so the card is not one excerpt repeated."""

    out: list[ScoredNote] = []
    for note in bucket:
        key = str(note.path)
        if key in used:
            continue
        used.add(key)
        out.append(note)
        if len(out) >= limit:
            return out
    for note in pool:
        key = str(note.path)
        if key in used:
            continue
        used.add(key)
        out.append(note)
        if len(out) >= limit:
            break
    return out


def build_companion_markdown(notes: list[ScoredNote]) -> str:
    top = notes[:TOP_SOURCES]
    raw_buckets = _bucket_notes(notes[:80])
    used: set[str] = set()
    buckets = {
        key: _fill_bucket(raw_buckets[key], top, used=used, limit=5)
        for key in ("started", "now", "friction", "helps", "threads")
    }

    parts = [
        "# Architect Companion Profile",
        "",
        f"_Generated {_utc_now()} from SBX_Vault (primary) + Memory_Bank (secondary)._",
        "",
        "This is **companion fuel** for Eve — personal arc, friction, and what helps — "
        "not a technical project dump. Rebuild with:",
        "",
        "```powershell",
        r".\venv\Scripts\python.exe -m pipeline.companion_profile build",
        "```",
        "",
        _section_md("Started", buckets["started"]),
        _section_md("Now", buckets["now"]),
        _section_md("Friction", buckets["friction"]),
        _section_md("What helps (incl. humor)", buckets["helps"]),
        _section_md("Active threads", buckets["threads"]),
    ]
    return "\n".join(parts).rstrip() + "\n"


def _heuristic_card(notes: list[ScoredNote]) -> str:
    top = notes[:TOP_SOURCES]
    raw_buckets = _bucket_notes(notes[:80])
    used: set[str] = set()
    buckets = {
        "started": _fill_bucket(raw_buckets["started"], top, used=used, limit=2),
        "now": _fill_bucket(raw_buckets["now"], top, used=used, limit=2),
        "friction": _fill_bucket(raw_buckets["friction"], top, used=used, limit=2),
        "helps": _fill_bucket(raw_buckets["helps"], top, used=used, limit=2),
        "threads": _fill_bucket(raw_buckets["threads"], top, used=used, limit=3),
    }

    def bullets(items: list[ScoredNote], n: int = 2) -> list[str]:
        out: list[str] = []
        for note in items[:n]:
            excerpt = _first_paragraphs(note.body, 220).replace("\n", " ")
            out.append(f"- ({note.path.name}) {excerpt}")
        return out or ["- (thin signal — rebuild after adding journals)"]

    lines = [
        "Architect companion background (always-on):",
        "Started:",
        *bullets(buckets["started"], 2),
        "Now:",
        *bullets(buckets["now"], 2),
        "Friction / stuck points:",
        *bullets(buckets["friction"], 2),
        "What helps (support + dry/gallows humor OK):",
        *bullets(buckets["helps"], 2),
        "Active threads:",
        *bullets(buckets["threads"], 3),
    ]
    card = "\n".join(lines)
    if len(card) > CARD_MAX_CHARS:
        card = card[: CARD_MAX_CHARS - 1].rstrip() + "…"
    return card


def _ollama_polish_card(draft: str) -> str | None:
    """Optional local polish; fail soft if Ollama is busy/unavailable."""

    prompt = (
        "Compress the following Architect companion notes into a tight background card "
        "for a local AI companion. Keep first-person arc, friction, humor/support style, "
        "and active threads. No tools/datasets. Max 450 words. Plain text bullets.\n\n"
        f"{draft[:6000]}"
    )
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"num_predict": 500, "temperature": 0.3},
    }
    try:
        req = urllib.request.Request(
            f"{OLLAMA_URL}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        text = str(data.get("response") or "").strip()
        if len(text) < 80:
            return None
        if len(text) > CARD_MAX_CHARS:
            text = text[: CARD_MAX_CHARS - 1].rstrip() + "…"
        return text
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError, ValueError):
        return None


def build_card(notes: list[ScoredNote], *, use_ollama: bool) -> tuple[str, str]:
    draft = _heuristic_card(notes)
    if use_ollama:
        polished = _ollama_polish_card(draft)
        if polished:
            return polished, "ollama"
    return draft, "heuristic"


def write_outputs(
    *,
    notes: list[ScoredNote],
    companion_md: str,
    card: str,
    card_method: str,
    sbx_vault: Path,
    memory_bank: Path,
) -> dict[str, object]:
    CORE_OUTPUT.mkdir(parents=True, exist_ok=True)
    COMPANION_FILE.write_text(companion_md, encoding="utf-8")
    CARD_FILE.write_text(card.rstrip() + "\n", encoding="utf-8")

    sbx_count = sum(1 for n in notes if n.source == "sbx")
    mem_count = sum(1 for n in notes if n.source == "memory_bank")
    top_sources = [
        {
            "path": str(n.path),
            "score": n.score,
            "source": n.source,
        }
        for n in notes[:TOP_SOURCES]
    ]
    manifest: dict[str, object] = {
        "generated_at": _utc_now(),
        "sbx_vault": str(sbx_vault),
        "memory_bank": str(memory_bank),
        "scored_total": len(notes),
        "scored_sbx": sbx_count,
        "scored_memory_bank": mem_count,
        "card_method": card_method,
        "card_chars": len(card),
        "outputs": {
            "companion": str(COMPANION_FILE),
            "card": str(CARD_FILE),
        },
        "top_sources": top_sources,
    }
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def build(
    *,
    sbx_vault: Path | None = None,
    memory_bank: Path | None = None,
    use_ollama: bool = True,
) -> dict[str, object]:
    vault = Path(sbx_vault) if sbx_vault else DEFAULT_SBX_VAULT
    bank = Path(memory_bank) if memory_bank else DEFAULT_MEMORY_BANK
    notes = collect_scored(sbx_vault=vault, memory_bank=bank)
    if not notes:
        raise SystemExit(
            f"No companion notes scored. Check vault at {vault} and Memory_Bank at {bank}."
        )
    companion_md = build_companion_markdown(notes)
    card, method = build_card(notes, use_ollama=use_ollama)
    return write_outputs(
        notes=notes,
        companion_md=companion_md,
        card=card,
        card_method=method,
        sbx_vault=vault,
        memory_bank=bank,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build Architect companion profile from SBX_Vault")
    sub = parser.add_subparsers(dest="command", required=True)

    build_parser = sub.add_parser("build", help="Score vault notes and write companion files")
    build_parser.add_argument("--sbx-vault", type=Path, default=None)
    build_parser.add_argument("--memory-bank", type=Path, default=None)
    build_parser.add_argument(
        "--no-ollama",
        action="store_true",
        help="Skip optional Ollama polish; heuristics only",
    )

    args = parser.parse_args(argv)
    if args.command == "build":
        manifest = build(
            sbx_vault=args.sbx_vault,
            memory_bank=args.memory_bank,
            use_ollama=not args.no_ollama,
        )
        print(json.dumps(manifest, indent=2))
        print(f"Wrote {COMPANION_FILE}", file=sys.stderr)
        print(f"Wrote {CARD_FILE}", file=sys.stderr)
        print(f"Wrote {MANIFEST_FILE}", file=sys.stderr)
        return 0
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
