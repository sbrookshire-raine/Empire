"""Research orchestrator — Wikipedia, GitHub, Product Hunt, web in one turn.

Uses admission controller for session grants. Writes optional intake briefs to
Resource Queue. Never promotes to Cognee.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline import admission_controller, github_scout, web_scout
from pipeline import wiki_scout

WORKBENCH = Path(os.environ.get("EMPIRE_WORKBENCH", r"C:\Empire_Workbench")).resolve()
RESOURCE_QUEUE = WORKBENCH / "00_Resource_Queue"
PRODUCT_HUNT_FEED = "https://www.producthunt.com/feed"
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")

SOURCE_TO_CAPABILITY: dict[str, str] = {
    "wiki": "wiki_local",
    "github": "github_scout",
    "producthunt": "web_scout",
    "web": "web_scout",
}


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(":", "")


def _safe_stem(value: str, fallback: str = "brief") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:80]


def write_intake_brief(
    title: str,
    body: str,
    *,
    source: str = "research_orchestrator",
) -> dict[str, Any]:
    RESOURCE_QUEUE.mkdir(parents=True, exist_ok=True)
    stem = _safe_stem(title)
    path = RESOURCE_QUEUE / f"INTAKE_{stem}_{_utc_stamp()}.md"
    content = "\n".join(
        [
            f"# {title}",
            "",
            f"Source: {source}",
            f"Generated: {_utc_stamp()}",
            "",
            body.strip(),
            "",
            "---",
            "Triage: USEFUL NOW / COOL IDEA / JUNK — do not auto-forge.",
            "",
        ]
    )
    try:
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "path": str(path)}


def _normalize_sources(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    for item in raw:
        if not isinstance(item, str):
            continue
        key = item.strip().lower()
        if key in SOURCE_TO_CAPABILITY and key not in out:
            out.append(key)
    return out


def orchestrate(
    query: str,
    *,
    sources: list[str] | None = None,
    github_limit: int = 8,
    web_url: str = "",
    note: str = "",
    write_brief: bool = True,
    release_after: bool = True,
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "query required"}

    if not admission_controller.research_partner_enabled():
        return {
            "ok": False,
            "error": "Research Partner mode is off — enable it in Workbench (More tab) or toggle Toolbelt manually.",
        }

    selected = _normalize_sources(sources) if sources else ["wiki", "github", "producthunt"]
    admission_log: list[dict[str, Any]] = []
    results: dict[str, Any] = {}

    for source in selected:
        cap = SOURCE_TO_CAPABILITY[source]
        admit = admission_controller.request_capability(
            cap,
            reason=f"research_orchestrate:{source}:{cleaned[:120]}",
            bypass_partner_check=True,
        )
        admission_log.append({"source": source, "capability": cap, "admission": admit})
        if not admit.get("ok"):
            results[source] = {"ok": False, "error": admit.get("error"), "skipped": True}
            continue

        if source == "wiki":
            results[source] = wiki_scout.search(cleaned, limit=5)
        elif source == "github":
            gh = github_scout.search_repos(cleaned, limit=github_limit, note=note)
            results[source] = gh
            if gh.get("ok") and write_brief and isinstance(gh.get("results"), list) and gh["results"]:
                top = gh["results"][:3]
                lines = [f"Query: {cleaned}", "", "Top GitHub hits:", ""]
                for row in top:
                    if isinstance(row, dict):
                        lines.append(
                            f"- **{row.get('full_name')}** — {row.get('description') or 'no description'} "
                            f"(stars {row.get('stars')})"
                        )
                brief = write_intake_brief(
                    f"GitHub scout: {cleaned[:60]}",
                    "\n".join(lines),
                )
                results[source]["intake_brief"] = brief
        elif source == "producthunt":
            results[source] = web_scout.scout(PRODUCT_HUNT_FEED, note=note or "Product Hunt feed")
        elif source == "web":
            url = (web_url or "").strip()
            if not url:
                results[source] = {"ok": False, "error": "web source requires web_url"}
            else:
                results[source] = web_scout.scout(url, note=note)

    release_result = None
    if release_after:
        release_result = admission_controller.release_session(reason="orchestrator_done")

    return {
        "ok": True,
        "query": cleaned,
        "sources": selected,
        "results": results,
        "admission_log": admission_log,
        "release": release_result,
        "note": "Scratch caches only — triage before Cognee or forge.",
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE research orchestrator")
    parser.add_argument("query")
    parser.add_argument("--sources", default="wiki,github,producthunt")
    parser.add_argument("--github-limit", type=int, default=8)
    parser.add_argument("--web-url", default="")
    parser.add_argument("--note", default="")
    parser.add_argument("--no-brief", action="store_true")
    parser.add_argument("--keep-session", action="store_true")
    args = parser.parse_args(argv)

    sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    result = orchestrate(
        args.query,
        sources=sources,
        github_limit=args.github_limit,
        web_url=args.web_url,
        note=args.note,
        write_brief=not args.no_brief,
        release_after=not args.keep_session,
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
