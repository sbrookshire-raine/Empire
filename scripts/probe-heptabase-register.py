"""Heptabase pass — card titles first, then the JSON structure, with the JSON left intact.

Implements step 1 of the ODYSSEY §13 handoff: *"Read card titles first (a cheap idea register, like the vault
search), then `All-Data.json` → `contextItems` for the link graph. **Keep the JSON; never reduce it to
markdown.**"*

Read-only on the estate; nothing is written outside stdout. One claim this probe exists to test: `ODYSSEY.md` §12
describes the 3,004 `contextItems` as *"the link graph between cards, which markdown cannot carry."* Measure that
rather than repeat it.

    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py              # counts + structure
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --register     # classify 749 names: journal / placeholder / concept / idea
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --links        # what contextItems links to
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --boards       # whiteboards = the real topical clustering
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --media        # 68 video cards + transcripts
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --find "Predictability Contract"
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --card "INFORMATION VERIFICATION" --chars 4200
    .\\venv\\Scripts\\python.exe scripts\\probe-heptabase-register.py --json         # machine-readable summary
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

DEFAULT_ROOT = Path(r"H:\Heptabase backup 4_7_26\Heptabase-Data-Backup-2026-04-08T03-50-14-422Z")

# What ODYSSEY §12 recorded, so the probe can say "ok" or "CHANGED" instead of assuming.
DOCUMENTED = {
    "cardInstances": 627,
    "whiteBoardList": 65,
    "contextItems": 3004,
    "chats": 42,
    "chatMessages": 542,
    "pdfCardInstances": 81,
    "mediaCards": 68,
    "templates": 2,
    "highlightElements": 3,
    "mindMapInstances": 0,
}


def load(root: Path) -> dict:
    return json.loads((root / "All-Data.json").read_text(encoding="utf-8"))


def measure(root: Path, data: dict) -> dict:
    """Counts, the documented-vs-measured check, and the markdown export census."""
    counts = {key: len(value) for key, value in data.items() if isinstance(value, list)}
    by_ext: Counter = Counter()
    md_bytes = 0
    for path in (root / "Card Library").rglob("*"):
        if path.is_file():
            by_ext[path.suffix.lower()] += 1
            if path.suffix.lower() == ".md":
                md_bytes += path.stat().st_size

    cards = data.get("cardList", [])
    return {
        "root_exists": root.exists(),
        "all_data_mb": round((root / "All-Data.json").stat().st_size / 1e6, 1),
        "documented": DOCUMENTED,
        "documented_ok": {k: counts.get(k) == v for k, v in DOCUMENTED.items()},
        "counts": counts,
        "card_library_ext": dict(by_ext),
        "card_library_md_kb": round(md_bytes / 1024, 1),
        "cardList_total": len(cards),
        "cardList_trashed": sum(1 for c in cards if c.get("isTrashed")),
        "cardList_with_insights": sum(1 for c in cards if c.get("insights")),
        "cardList_json_content": sum(1 for c in cards if isinstance(c.get("content"), str)),
    }


def titles(data: dict) -> list[dict]:
    """The idea register: every card title with its dates, trash state and insight count."""
    register = []
    for card in data.get("cardList", []):
        register.append(
            {
                "title": (card.get("title") or "").strip(),
                "created": (card.get("createdTime") or "")[:10],
                "edited": (card.get("lastEditedTime") or "")[:10],
                "trashed": bool(card.get("isTrashed")),
                "insights": len(card.get("insights") or []),
                "id": card.get("id"),
            }
        )
    return sorted(register, key=lambda r: (r["trashed"], r["created"]))


def links(data: dict) -> dict:
    """What `contextItems` actually relates — the §12 'link graph' claim, measured."""
    contexts = data.get("contextItems", [])
    append_to = Counter(c.get("appendToObjectType") for c in contexts)
    locate_to = Counter(c.get("locateToObjectType") for c in contexts)
    context_type = Counter(c.get("contextType") for c in contexts)

    # Degree: which cards get pulled into the most AI conversations.
    degree: Counter = Counter()
    for item in contexts:
        if item.get("appendToObjectType") != "chatMessage":
            continue
        key = item.get("contextId") or item.get("locateToObjectId")
        if key:
            degree[key] += 1

    card_titles = {c.get("id"): (c.get("title") or "") for c in data.get("cardList", [])}
    board_titles = {b.get("id"): (b.get("name") or "") for b in data.get("whiteBoardList", [])}
    hubs = [
        {"id": key, "uses": n, "title": card_titles.get(key) or board_titles.get(key) or "?"}
        for key, n in degree.most_common(30)
    ]

    # The other structural tables — the ones markdown genuinely cannot carry.
    connections = data.get("connections", [])
    return {
        "appendToObjectType": dict(append_to),
        "locateToObjectType": dict(locate_to),
        "contextType": dict(context_type),
        "chat_message_context_items": append_to.get("chatMessage", 0),
        "chat_context_share_items": append_to.get("chat2AccountRelation", 0),
        "hubs": hubs,
        "connections": len(connections),
        "connections_whiteboards": len({c.get("whiteboardId") for c in connections}),
        "sections": len(data.get("sections", [])),
        "sectionObjectRelations": len(data.get("sectionObjectRelations", [])),
        "objectPropertyRelations": len(data.get("objectPropertyRelations", [])),
        "cardTagList": len(data.get("cardTagList", [])),
        "tags": [t.get("name") for t in data.get("tagList", [])],
    }


def card_text(card: dict) -> str:
    """Recover a card's readable text from its ProseMirror `content` JSON (no markdown conversion)."""
    raw = card.get("content")
    if not isinstance(raw, str):
        return ""
    try:
        doc = json.loads(raw)
    except json.JSONDecodeError:
        return raw

    chunks: list[str] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if node.get("type") == "text":
                chunks.append(node.get("text") or "")
            elif node.get("type") in {"paragraph", "heading", "listItem", "blockquote"} and chunks:
                chunks.append("\n")
            for child in node.get("content") or []:
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(doc)
    return "".join(chunks).strip()


def find_cards(data: dict, needle: str) -> list[dict]:
    """Cards whose title or body matches `needle` — the reader for the next pass."""
    needle_lower = needle.lower()
    hits = []
    for card in data.get("cardList", []):
        title = (card.get("title") or "").strip()
        body = card_text(card)
        if needle_lower in title.lower() or needle_lower in body.lower():
            hits.append(
                {
                    "title": title.splitlines()[0][:120] if title else "(untitled)",
                    "created": (card.get("createdTime") or "")[:10],
                    "edited": (card.get("lastEditedTime") or "")[:10],
                    "trashed": bool(card.get("isTrashed")),
                    "chars": len(body),
                    "body": body,
                }
            )
    return sorted(hits, key=lambda h: -h["chars"])


def classify_titles(stems: list[str]) -> dict[str, list[str]]:
    """Split the 749 Card Library names into what they actually are.

    Heptabase exports journal entries, placeholder cards and concept cards into the same folder, so "749 card
    titles" is not "749 ideas". `!` in a stem is the export's stand-in for `/` (filename sanitising).
    """
    import re

    journal = re.compile(r"^\d{1,2}[!/.\-]\d{1,2}([!/.\-]\d{2,4})?(\s|$)")
    placeholder = re.compile(r"^(a wonderful new card|untitled|new card)", re.IGNORECASE)
    buckets: dict[str, list[str]] = {"journal": [], "placeholder": [], "concept": [], "idea": []}
    for stem in stems:
        if journal.match(stem):
            buckets["journal"].append(stem)
        elif placeholder.match(stem):
            buckets["placeholder"].append(stem)
        elif stem.startswith("[") and stem.endswith("]"):
            buckets["concept"].append(stem)
        else:
            buckets["idea"].append(stem)
    return buckets


def boards(data: dict) -> list[dict]:
    """The real card↔card structure: which whiteboard each card sits on, plus its connector lines.

    `contextItems` turns out to record *chat* context, so the topical clustering lives here instead —
    `cardInstances.whiteboardId` (membership), `connections` (drawn links) and `sectionObjectRelations`
    (named groups inside a board).
    """
    cards_per_board: Counter = Counter()
    for inst in data.get("cardInstances", []):
        if inst.get("whiteboardId"):
            cards_per_board[inst["whiteboardId"]] += 1
    pdf_per_board: Counter = Counter()
    for inst in data.get("pdfCardInstances", []):
        if inst.get("whiteboardId"):
            pdf_per_board[inst["whiteboardId"]] += 1
    text_per_board: Counter = Counter()
    for el in data.get("textElements", []):
        if el.get("whiteboardId"):
            text_per_board[el["whiteboardId"]] += 1
    conn_per_board: Counter = Counter()
    for conn in data.get("connections", []):
        if conn.get("whiteboardId"):
            conn_per_board[conn["whiteboardId"]] += 1
    sect_per_board: Counter = Counter()
    for sect in data.get("sections", []):
        if sect.get("whiteboardId"):
            sect_per_board[sect["whiteboardId"]] += 1

    rows = []
    for board in data.get("whiteBoardList", []):
        bid = board.get("id")
        rows.append(
            {
                "name": (board.get("name") or "(unnamed)").strip(),
                "cards": cards_per_board.get(bid, 0),
                "pdfs": pdf_per_board.get(bid, 0),
                "texts": text_per_board.get(bid, 0),
                "links": conn_per_board.get(bid, 0),
                "sections": sect_per_board.get(bid, 0),
                "created": (board.get("createdTime") or "")[:10],
                "edited": (board.get("lastEditedTime") or "")[:10],
                "trashed": bool(board.get("isTrashed")),
            }
        )
    return sorted(rows, key=lambda r: -(r["cards"] + r["pdfs"] + r["texts"]))


def media(data: dict) -> list[dict]:
    """Video/media cards — the recorded-watching layer, transcript length as a proxy for depth."""
    out = []
    for card in data.get("mediaCards", []):
        transcript = card.get("transcript") or {}
        entries = transcript.get("transcriptEntries") or []
        chars = sum(len(e.get("content") or "") for e in entries if isinstance(e, dict))
        out.append(
            {
                "title": (card.get("title") or "").strip(),
                "type": card.get("type"),
                "link": card.get("link"),
                "transcript_status": transcript.get("status"),
                "transcript_entries": len(entries),
                "transcript_chars": chars,
                "created": (card.get("createdTime") or "")[:10],
            }
        )
    return sorted(out, key=lambda m: -m["transcript_chars"])


def main() -> int:
    # Card titles carry emoji; console stdout defaults to cp1252 and dies on them (the repo's known
    # encoding trap). Force UTF-8 so a title can never kill the run.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Heptabase export register (read-only).")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="export root")
    parser.add_argument("--titles", action="store_true", help="print the card-title idea register")
    parser.add_argument("--links", action="store_true", help="print contextItems / connections structure")
    parser.add_argument("--media", action="store_true", help="print media cards and transcripts")
    parser.add_argument("--find", default="", help="list cards whose title or body matches this text")
    parser.add_argument("--card", default="", help="print the matching card's full text")
    parser.add_argument("--chars", type=int, default=2000, help="chars of card body to print (with --card)")
    parser.add_argument("--json", action="store_true", help="machine-readable summary")
    parser.add_argument("--md-titles", action="store_true", help="list the 749 Card Library markdown titles")
    parser.add_argument("--register", action="store_true", help="classify the 749 names: journal / placeholder / concept / idea")
    parser.add_argument("--boards", action="store_true", help="whiteboards as the real topical clustering (cards, links, sections)")
    parser.add_argument("--limit", type=int, default=0, help="cap rows in the tables (0 = all)")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"export root not found: {root}")
        return 1

    data = load(root)
    summary = measure(root, data)

    if args.json:
        payload = {
            "measure": summary,
            "links": links(data),
            "media": media(data),
            "titles": titles(data),
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    print(f"export root: {root}")
    print(f"All-Data.json: {summary['all_data_mb']} MB\n")

    print("documented (ODYSSEY §12) vs measured")
    for key, documented in DOCUMENTED.items():
        got = summary["counts"].get(key, 0)
        mark = "ok" if summary["documented_ok"][key] else "CHANGED"
        print(f"  {key:<22} doc {documented:>5}  measured {got:>5}  {mark}")

    print("\ncounts the doc does not list")
    for key in sorted(summary["counts"]):
        if key not in DOCUMENTED and summary["counts"][key]:
            print(f"  {key:<30} {summary['counts'][key]:>5}")

    print("\nCard Library on disk")
    for ext, n in sorted(summary["card_library_ext"].items()):
        print(f"  {ext:<6} {n:>5}")
    print(f"  markdown total {summary['card_library_md_kb']} KB")
    print(
        f"\ncardList: {summary['cardList_total']} cards"
        f"  ({summary['cardList_trashed']} trashed)"
        f"  insights on {summary['cardList_with_insights']}"
        f"  json content on {summary['cardList_json_content']}"
    )

    if args.links:
        info = links(data)
        print("\ncontextItems — what it actually relates (measured, not assumed)")
        print(f"  appendToObjectType {info['appendToObjectType']}")
        print(f"  locateToObjectType {info['locateToObjectType']}")
        print(f"  contextType        {info['contextType']}")
        print(
            f"  -> {info['chat_message_context_items']} attach to a chat message,"
            f" {info['chat_context_share_items']} to a share relation"
        )
        print("\n  top cards by chat-context reuse")
        for hub in info["hubs"][: args.limit or 30]:
            print(f"    {hub['uses']:>3}x  {hub['title'][:90]}")

    if args.md_titles:
        stems = sorted(p.stem for p in (root / "Card Library").glob("*.md"))
        print("\nCard Library titles (the cheap idea register — markdown stems, not JSON first lines)")
        for stem in (stems[: args.limit] if args.limit else stems):
            print(f"  {stem}")
        print(f"\n{len(stems)} card titles on disk")

    if args.register:
        stems = sorted(p.stem for p in (root / "Card Library").glob("*.md"))
        buckets = classify_titles(stems)
        print("\nCard Library names, classified (749 names != 749 ideas)")
        for name in ("journal", "placeholder", "concept", "idea"):
            print(f"  {name:<12} {len(buckets[name]):>4}")
        print("\n  -- concept cards (atomic ideas) --")
        for stem in buckets["concept"]:
            print(f"    {stem}")
        print("\n  -- the working register (everything else) --")
        for stem in (buckets["idea"][: args.limit] if args.limit else buckets["idea"]):
            print(f"    {stem}")

    if args.boards:
        print("\nwhiteboards (the topical clustering — what contextItems is NOT)")
        rows = boards(data)
        for row in (rows[: args.limit] if args.limit else rows):
            flag = "T" if row["trashed"] else " "
            print(
                f"  {flag} {row['cards']:>3} cards {row['pdfs']:>3} pdf {row['texts']:>3} txt"
                f" {row['links']:>3} link {row['sections']:>2} sect  {row['created']}  {row['name'][:60]}"
            )
        print(f"\n{len(rows)} whiteboards")

    if args.find:
        hits = find_cards(data, args.find)
        print(f"\ncards matching {args.find!r}: {len(hits)}")
        for hit in (hits[: args.limit] if args.limit else hits):
            flag = "T" if hit["trashed"] else " "
            print(f"  {flag} {hit['created']}  {hit['chars']:>7,} ch  {hit['title']}")

    if args.card:
        hits = find_cards(data, args.card)
        print(f"\ncard text for {args.card!r}: {len(hits)} match(es)")
        for hit in hits[: args.limit or 3]:
            print(f"\n--- {hit['title']}  ({hit['created']}, {hit['chars']:,} ch) ---")
            print(hit["body"][: args.chars])

    if args.media:
        print("\nmedia cards (recorded watching, transcript depth)")
        rows = media(data)
        for row in (rows[: args.limit] if args.limit else rows):
            print(
                f"  {row['transcript_chars']:>7,} ch  {row['transcript_status'] or '-':<8}"
                f" {row['created']}  {row['title'][:80]}"
            )

    if args.titles:
        print("\nidea register (card titles, live first)")
        rows = titles(data)
        for row in (rows[: args.limit] if args.limit else rows):
            flag = "T" if row["trashed"] else " "
            print(f"  {flag} {row['created']}  {row['title']}")
        print(f"\n{len(rows)} card titles  ·  {sum(1 for r in rows if not r['trashed'])} live")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
