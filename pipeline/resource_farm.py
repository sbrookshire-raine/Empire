"""GitHub resource farm — scout repos, write scout Disassembly Cards, optional Heptabase.

Scratch catalog only (disassembly_cards + github_cache). Never writes Cognee.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Any

from pipeline import disassembly_card, disassembly_publish, github_scout, heptabase_cli
from pipeline.heptabase_config import catalog_whiteboard_id

REPO_SLUG_RE = re.compile(r"github\.com/([^/\s#\"'>]+/[^/\s#\"'>]+)", re.I)
SCOUT_EVOLUTION = (
    "Scout ticket from resource_farm — README/topics only, not REA-verified. "
    "Clone to C:/Empire_Workbench/00_Resource_Queue when ready for rea_doctor + analyze."
)


def _normalize_repo(slug: str) -> str:
    cleaned = (slug or "").strip().strip("/").lower()
    if cleaned.count("/") != 1:
        return ""
    owner, name = cleaned.split("/", 1)
    if not owner or not name:
        return ""
    return f"{owner}/{name}"


def indexed_source_repos(*, limit: int = 500) -> dict[str, dict[str, Any]]:
    """Repos already represented in disassembly cards (by source_repo or evidence URL)."""
    out: dict[str, dict[str, Any]] = {}
    for card in disassembly_card.list_cards(limit=limit):
        card_id = str(card.get("id") or "")
        sr = _normalize_repo(str(card.get("source_repo") or ""))
        if sr:
            out[sr] = {"card_id": card_id, "learning_stage": card.get("learning_stage"), "via": "source_repo"}
            continue
        for ref in card.get("evidence_refs") or []:
            if not isinstance(ref, str):
                continue
            match = REPO_SLUG_RE.search(ref)
            if match:
                slug = _normalize_repo(match.group(1))
                if slug and slug not in out:
                    out[slug] = {
                        "card_id": card_id,
                        "learning_stage": card.get("learning_stage"),
                        "via": "evidence_ref",
                    }
        title = str(card.get("title") or "")
        if "`" in title:
            inner = title.split("`", 2)[1] if title.count("`") >= 2 else ""
            slug = _normalize_repo(inner)
            if slug and slug not in out:
                out[slug] = {"card_id": card_id, "learning_stage": card.get("learning_stage"), "via": "title"}
    return out


def catalog_status(*, limit: int = 50) -> dict[str, Any]:
    index = indexed_source_repos()
    recent = disassembly_card.list_cards(limit=limit)
    scout_cards = [c for c in recent if c.get("farm_kind") == "scout"]
    return {
        "ok": True,
        "mode": "catalog",
        "farmed_repo_count": len(index),
        "farmed_repos": sorted(index.keys()),
        "repo_index": index,
        "recent_scout_cards": scout_cards[:20],
        "recent_cards": recent[:10],
        "note": "Scratch catalog — not Cognee. Re-run resource_farm with a query to add new scout cards.",
    }


def _guess_container(
    language: str,
    topics: list[str],
    description: str,
    readme_excerpt: str,
) -> str:
    blob = " ".join(
        [
            language or "",
            description or "",
            readme_excerpt[:2500] or "",
            " ".join(str(t) for t in topics[:12]),
        ]
    ).lower()
    if "electron" in blob or "tauri" in blob:
        return "electron"
    if any(x in blob for x in ("unity", "godot", "unreal", "game")):
        return "game_logic"
    if any(x in blob for x in ("whisper", "demucs", "audio", "tts", "stt")):
        return "audio_pipeline"
    if language in ("C", "C++", "Rust", "Go", "Assembly") and "javascript" not in blob:
        return "native_pe"
    if language in ("JavaScript", "TypeScript", "HTML", "CSS", "Vue", "Svelte"):
        return "web"
    return "unknown"


def _scout_connections(
    slug: str,
    language: str,
    topics: list[str],
    description: str,
    readme_summary: str,
    html_url: str,
    readme_path: str,
    search_path: str,
) -> list[dict[str, str]]:
    evidence = readme_path or html_url
    rows: list[dict[str, str]] = [
        {
            "from": slug,
            "to": "Resource Queue (clone pending)",
            "kind": "intake",
            "evidence_ref": evidence,
        },
        {
            "from": "GitHub README cache",
            "to": "disassembly_cards scout ticket",
            "kind": "provenance",
            "evidence_ref": readme_path or search_path or html_url,
        },
        {
            "from": slug,
            "to": "EMPIRE Eve (Ollama + MCP + Cognee)",
            "kind": "compare",
            "evidence_ref": "C:/EMPIRE/docs/DISASSEMBLY_CATALOG.md",
        },
    ]
    if language:
        rows.append(
            {
                "from": "primary stack",
                "to": language,
                "kind": "language",
                "evidence_ref": html_url,
            }
        )
    if topics:
        rows.append(
            {
                "from": "GitHub topics",
                "to": ", ".join(str(t) for t in topics[:6]),
                "kind": "taxonomy",
                "evidence_ref": html_url,
            }
        )
    lower_blob = " ".join(
        [
            " ".join(str(t).lower() for t in topics),
            (description or "").lower(),
            (readme_summary or "").lower(),
        ]
    )
    if "mcp" in lower_blob:
        rows.append(
            {
                "from": "MCP / tools surface",
                "to": "EMPIRE mcp/ FastMCP",
                "kind": "analogy",
                "evidence_ref": evidence,
            }
        )
    while len(rows) < 3:
        rows.append(
            {
                "from": "scout evidence",
                "to": html_url,
                "kind": "link",
                "evidence_ref": evidence,
            }
        )
    return rows[:7]


def _heptabase_publish_plan(
    *,
    architect_confirm: bool,
    publish_heptabase: bool | None,
) -> tuple[bool, str]:
    """Decide whether this run should publish new cards to the catalog board."""
    if publish_heptabase is False:
        return False, "publish_heptabase=false (local cards only)"
    if not architect_confirm:
        return False, "need_architect_confirm for Heptabase (cards stay local under disassembly_cards/)"
    if not catalog_whiteboard_id():
        return False, "HEPTABASE_DISASSEMBLY_WHITEBOARD_ID not set — run ensure-heptabase-disassembly-board.ps1"
    health = heptabase_cli.health_check()
    if not health.get("ok"):
        return False, f"Heptabase not ready: {health.get('error') or health.get('hint') or 'start desktop app'}"
    return True, "board ready — publishing new scout cards as orange placements"


def run_farm(
    query: str,
    *,
    search_limit: int = 10,
    max_new_cards: int = 5,
    architect_confirm: bool = False,
    publish_heptabase: bool | None = None,
    note: str = "",
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return catalog_status()

    search_limit = max(1, min(int(search_limit or 10), 30))
    max_new_cards = max(0, min(int(max_new_cards or 5), 15))

    search = github_scout.search_repos(cleaned, limit=search_limit, note=note)
    if not search.get("ok"):
        return {"ok": False, "error": search.get("error"), "step": "github_search", "detail": search}

    index = indexed_source_repos()
    should_publish, publish_reason = _heptabase_publish_plan(
        architect_confirm=architect_confirm,
        publish_heptabase=publish_heptabase,
    )

    skipped: list[dict[str, str]] = []
    created: list[dict[str, Any]] = []
    publish_results: list[dict[str, Any]] = []
    errors: list[str] = []

    for row in search.get("results") or []:
        if len(created) >= max_new_cards:
            break
        if not isinstance(row, dict):
            continue
        slug = _normalize_repo(str(row.get("full_name") or ""))
        if not slug:
            continue
        if slug in index:
            skipped.append({"repo": slug, "existing_card_id": index[slug].get("card_id", ""), "reason": "already_farmed"})
            continue

        readme = github_scout.repo_readme(slug, note=note or f"resource_farm: {cleaned}")
        if not readme.get("ok"):
            errors.append(f"{slug}: {readme.get('error') or 'readme failed'}")
            continue

        language = str(row.get("language") or "")
        topics = row.get("topics") if isinstance(row.get("topics"), list) else []
        description = str(row.get("description") or "")
        html_url = str(row.get("html_url") or f"https://github.com/{slug}")
        readme_path = str(readme.get("path") or "")
        search_path = str(search.get("path") or "")
        summary_bits = [
            description,
            str(readme.get("summary") or "")[:300],
        ]
        target_summary = " ".join(x for x in summary_bits if x).strip()[:500]
        if not target_summary:
            target_summary = f"GitHub repo {slug} (scout-only)."

        container = _guess_container(
            language,
            [str(t) for t in topics],
            description,
            str(readme.get("summary") or ""),
        )
        payload = {
            "title": f"{slug} — scout ticket",
            "container": container,
            "target_summary": target_summary,
            "connections": _scout_connections(
                slug,
                language,
                [str(t) for t in topics],
                description,
                str(readme.get("summary") or ""),
                html_url,
                readme_path,
                search_path,
            ),
            "evidence_refs": [x for x in [readme_path, search_path, html_url] if x],
            "lego_hooks": ["resource_farm", "scout_ticket"],
            "evolution_note": SCOUT_EVOLUTION,
            "learning_stage": "draft",
            "source_repo": slug,
            "farm_kind": "scout",
        }
        try:
            written = disassembly_card.write_card(payload)
        except (ValueError, OSError) as exc:
            errors.append(f"{slug}: {exc}")
            continue
        if not written.get("ok"):
            errors.append(f"{slug}: write failed")
            continue
        card = written.get("card") or {}
        card_id = str(card.get("id") or "")
        entry: dict[str, Any] = {
            "repo": slug,
            "card_id": card_id,
            "container": container,
            "readme_cache": readme_path,
            "html_url": html_url,
        }
        created.append(entry)
        index[slug] = {"card_id": card_id, "learning_stage": "draft", "via": "this_run"}

        if should_publish and card_id:
            pub = disassembly_publish.publish_to_heptabase(
                card_id,
                architect_confirm=True,
            )
            publish_results.append({"card_id": card_id, "repo": slug, "result": pub})
            if pub.get("ok") is not True:
                errors.append(f"publish {card_id}: {pub.get('error') or 'failed'}")

    return {
        "ok": True,
        "query": cleaned,
        "search_path": search.get("path"),
        "search_count": search.get("count"),
        "created": created,
        "skipped": skipped,
        "errors": errors,
        "heptabase": {
            "attempted": should_publish,
            "reason": publish_reason,
            "publish_results": publish_results,
        },
        "catalog": {
            "farmed_repo_count": len(index),
            "new_this_run": len(created),
        },
        "next_steps": _next_steps(created, should_publish, architect_confirm),
    }


def _next_steps(
    created: list[dict[str, Any]],
    published: bool,
    architect_confirm: bool,
) -> list[str]:
    steps: list[str] = []
    if not created:
        steps.append("No new repos — try a different query or raise max_new_cards.")
    else:
        steps.append("Pick a card id and clone its repo to 00_Resource_Queue for REA when ready.")
    if created and not published and not architect_confirm:
        steps.append("To show new orange cards on Heptabase, re-run with architect_confirm=true (same turn you say yes).")
    if created and not published and architect_confirm:
        steps.append("Heptabase was not used — check heptabase.health or board id in config/heptabase.env.")
    return steps


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE GitHub resource farm")
    parser.add_argument("query", nargs="?", default="", help="GitHub search query (omit for catalog status)")
    parser.add_argument("--search-limit", type=int, default=10)
    parser.add_argument("--max-new-cards", type=int, default=5)
    parser.add_argument("--architect-confirm", action="store_true")
    parser.add_argument(
        "--publish-heptabase",
        action="store_true",
        help="Publish new cards when board ready (still requires --architect-confirm)",
    )
    parser.add_argument(
        "--no-publish-heptabase",
        action="store_true",
        help="Force local cards only",
    )
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)

    publish_flag: bool | None = None
    if args.no_publish_heptabase:
        publish_flag = False
    elif args.publish_heptabase:
        publish_flag = True

    if args.query.strip():
        result = run_farm(
            args.query,
            search_limit=args.search_limit,
            max_new_cards=args.max_new_cards,
            architect_confirm=args.architect_confirm,
            publish_heptabase=publish_flag,
            note=args.note,
        )
    else:
        result = catalog_status()

    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") is not False else 1


if __name__ == "__main__":
    raise SystemExit(main())
