"""Primitive lookup over the Architect's decoded ledger (Loom).

The ledger is the association memory: every row decodes one *thing* into the transferable
*mechanism* underneath it, the Universal *primitives* it is built from, and a *sibling* — another
domain where the same mechanism shows up. "Does X apply to Y?" is answered by finding the primitive
both share, so this limb exists to make the ledger queryable in chat.

Measured 2026-09-24: 501 rows / 247 distinct (thing, primitives, sibling) sat in
`loom/workspace_data/primitive_ledger.csv`, readable only by the intake script — so an
idea-transfer question ("can I learn drums using the rules of juggling?") never saw `Timing & Sync`,
`Sensory Feedback`, or their siblings, and answered from training memory instead.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
from collections import Counter
from pathlib import Path
from typing import Any

DEFAULT_LEDGER = Path(
    os.environ.get(
        "EMPIRE_PRIMITIVE_LEDGER",
        r"C:\Empire_Workbench\04_Thought_Experiments\loom\workspace_data\primitive_ledger.csv",
    )
)
# Field weights: the primitive name is the join key between domains, so it counts most.
_WEIGHTS = {"primitives": 3, "thing": 2, "mechanism": 1, "sibling": 1}
_STOPWORDS = frozenset(
    {
        "the", "and", "for", "with", "that", "this", "from", "into", "onto", "over", "under",
        "using", "use", "uses", "can", "could", "would", "should", "how", "does", "did", "what",
        "when", "where", "which", "who", "why", "are", "was", "were", "has", "have", "had",
        "not", "but", "you", "your", "its", "like", "than", "then", "them", "they", "there",
        "here", "about", "same", "way", "ways", "rule", "rules", "learn", "learning", "apply",
        "applies", "work", "works", "working", "make", "makes", "get", "got",
        # Quantifiers and connectives that are 3+ chars but carry no domain signal.
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "also", "more", "most", "some", "any", "all", "each", "both", "other", "only", "just",
        "very", "too", "now", "out", "off", "own", "still", "even", "ever", "never", "always",
        "its", "their", "been", "being", "them", "these", "those", "her", "his", "she", "him",
        # Meta words *about the request itself* rather than about the thing: measured 2026-09-24,
        # "Use my primitive ledger: which primitives does juggling share with drumming, and what
        # would falsify the analogy?" matched claude-api/pgroll rows through "share"/"ledger" and
        # handed her irrelevant mechanisms. This tool searches the ledger, so these are noise.
        "primitive", "primitives", "ledger", "share", "shared", "shares", "sharing",
        "falsify", "falsified", "falsification", "analogy", "analogies", "mapping", "mappings",
        "overlap", "overlaps", "parallel", "parallels", "compare", "comparison", "same",
    }
)
_WORD = re.compile(r"[a-z0-9]+")
_MECHANISM_MAX = 400


def _terms(text: str) -> list[str]:
    """Query terms: lowercased words of 3+ chars, stopwords dropped."""

    words = _WORD.findall((text or "").casefold())
    seen: list[str] = []
    for word in words:
        if len(word) < 3 or word in _STOPWORDS or word in seen:
            continue
        seen.append(word)
    return seen


def _read_rows(ledger: Path) -> list[dict[str, str]]:
    if not ledger.is_file():
        return []
    with ledger.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _row_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (
        str(row.get("thing") or "").strip().casefold(),
        str(row.get("primitives") or "").strip().casefold(),
        str(row.get("sibling") or "").strip().casefold(),
    )


def vocabulary(rows: list[dict[str, str]], *, limit: int = 12) -> list[dict[str, Any]]:
    """The primitive names the ledger actually uses, most used first.

    Handing these back on a miss is deliberate: the vocabulary is fixed (the Seeker decodes into a
    known set), so a model that does not know the names cannot join domains.
    """

    counter: Counter[str] = Counter()
    for row in rows:
        for name in str(row.get("primitives") or "").split(";"):
            cleaned = name.strip()
            if cleaned:
                counter[cleaned] += 1
    return [{"primitive": name, "count": count} for name, count in counter.most_common(limit)]



def _document_frequency(rows: list[dict[str, str]], terms: list[str]) -> dict[str, int]:
    """How many rows each term appears in. A term in most rows cannot discriminate between them."""

    haystacks = [
        [str(row.get(field) or "").casefold() for field in _WEIGHTS] for row in rows
    ]
    counts: dict[str, int] = {}
    for term in terms:
        pattern = re.compile(rf"\b{re.escape(term)}\b")
        counts[term] = sum(
            1 for fields in haystacks if any(pattern.search(field) for field in fields)
        )
    return counts


def _score(row: dict[str, str], terms: list[str], primitive: str, domain: str) -> int:
    haystacks = {field: str(row.get(field) or "").casefold() for field in _WEIGHTS}
    score = 0
    for term in terms:
        # Word boundaries, not substrings: measured 2026-09-24, plain `in` let "play" match
        # "replayed" and pulled gh-ost into a juggling/drumming question.
        pattern = re.compile(rf"\b{re.escape(term)}\b")
        for field, weight in _WEIGHTS.items():
            if pattern.search(haystacks[field]):
                score += weight
    if primitive:
        if primitive.casefold() not in haystacks["primitives"]:
            return 0
        score += 5
    if domain:
        if domain.casefold() not in str(row.get("domain") or "").casefold():
            return 0
        score += 1
    return score


def lookup(
    *,
    text: str = "",
    primitive: str = "",
    domain: str = "",
    limit: int = 8,
    ledger: Path | None = None,
    dedupe: bool = True,
) -> dict[str, Any]:
    """Rank ledger rows against a query. Returns matches plus the ledger's own vocabulary."""

    path = Path(ledger) if ledger else DEFAULT_LEDGER
    rows = _read_rows(path)
    if not rows:
        return {
            "ok": False,
            "error": f"primitive ledger not readable at {path}",
            "ledger": str(path),
        }

    distinct = {_row_key(row) for row in rows}
    terms = _terms(text)
    # Rarity filter: measured 2026-09-24, "one" (not a stopword) matched "one help button",
    # "one uniform protocol" and "one batched pass", so a juggling/drumming question was handed
    # three irrelevant mechanisms. A term present in most rows cannot discriminate between them.
    if terms:
        frequency = _document_frequency(rows, terms)
        ceiling = max(3, int(len(rows) * 0.25))
        distinctive = [term for term in terms if frequency.get(term, 0) <= ceiling]
        terms = distinctive
    primitive_value = (primitive or "").strip()
    domain_value = (domain or "").strip()
    if not terms and not primitive_value and not domain_value:
        return {
            "ok": False,
            "error": "pass text, primitive, or domain",
            "vocabulary": vocabulary(rows),
        }

    scored: list[tuple[int, int, dict[str, str]]] = []
    for row in rows:
        score = _score(row, terms, primitive_value, domain_value)
        if score <= 0:
            continue
        scored.append((score, int(str(row.get("id") or 0) or 0), row))
    scored.sort(key=lambda item: (-item[0], item[1]))

    matches: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str, str]] = set()
    for score, row_id, row in scored:
        key = _row_key(row)
        if dedupe and key in seen_keys:
            continue
        seen_keys.add(key)
        matches.append(
            {
                "id": row_id,
                "thing": str(row.get("thing") or "").strip(),
                "domain": str(row.get("domain") or "").strip(),
                "mechanism": str(row.get("mechanism") or "").strip()[:_MECHANISM_MAX],
                "primitives": str(row.get("primitives") or "").strip(),
                "sibling": str(row.get("sibling") or "").strip(),
                "decoded_by": str(row.get("decoded_by") or "").strip(),
                "date": str(row.get("date") or "").strip(),
                "score": score,
            }
        )
        if len(matches) >= max(1, limit):
            break

    result: dict[str, Any] = {
        "ok": True,
        "ledger": str(path),
        "rows_total": len(rows),
        "rows_distinct": len(distinct),
        "terms": terms,
        "matches": matches,
        "vocabulary": vocabulary(rows),
    }
    if not matches:
        result["note"] = (
            "No ledger row matched. The vocabulary list holds the ledger's own primitive names — "
            "retry with one of those, or say plainly that this connection is not in the ledger yet."
        )
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Look up decoded primitives in the Architect's ledger"
    )
    parser.add_argument("text", nargs="?", default="")
    parser.add_argument("--primitive", default="")
    parser.add_argument("--domain", default="")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    args = parser.parse_args(argv)
    result = lookup(
        text=args.text,
        primitive=args.primitive,
        domain=args.domain,
        limit=max(1, min(args.limit, 25)),
        ledger=Path(args.ledger),
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
