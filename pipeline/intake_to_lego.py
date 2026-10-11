"""One-shot intake: web URL or GitHub → Disassembly Card → optional Heptabase → optional memory.

Architect does not run separate CLI steps; Eve calls `intake_to_lego_run` (TypeScript → this module).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from pipeline import disassembly_card, disassembly_publish, github_scout, resource_farm, web_scout
from pipeline.cognee_guard import guard_memory_promotion
from pipeline.eve_staging import confirm_remember, propose_remember

RESOURCE_QUEUE = Path(r"C:\Empire_Workbench\00_Resource_Queue")
REPO_SLUG_RE = re.compile(r"^([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)$")
GITHUB_URL_RE = re.compile(r"github\.com/([^/\s#\"'>]+/[^/\s#\"'>]+)", re.I)

WEB_EVOLUTION = (
    "Web intake — page text cached locally, not REA-verified. "
    "Re-run with study/REA after downloading or cloning artefacts."
)
STUDY_EVOLUTION = (
    "Study seed — shallow clone under Resource Queue. "
    "Run REA (rea_analyze_javascript / rea_invoke) for verified evidence, then update this card."
)


def _normalize_repo(value: str) -> str:
    cleaned = (value or "").strip().strip("/")
    match = GITHUB_URL_RE.search(cleaned)
    if match:
        cleaned = match.group(1)
    if not REPO_SLUG_RE.match(cleaned):
        return ""
    return cleaned.lower()


def _publish_plan(architect_confirm: bool, publish_heptabase: bool | None) -> tuple[bool, str]:
    return resource_farm._heptabase_publish_plan(  # noqa: SLF001 — shared publish policy
        architect_confirm=architect_confirm,
        publish_heptabase=publish_heptabase,
    )


def _maybe_memory_promotion(
    card_id: str,
    card: dict[str, Any],
    *,
    architect_confirm: bool,
    promote_memory: bool,
    promote_confirm: bool,
) -> dict[str, Any] | None:
    if not promote_memory:
        return None
    text = (
        f"Disassembly card {card_id}: {(card.get('title') or '').strip()}\n\n"
        f"{(card.get('target_summary') or '').strip()}\n\n"
        f"Evidence: {', '.join(str(x) for x in (card.get('evidence_refs') or [])[:5])}"
    ).strip()
    blocked = guard_memory_promotion(text)
    if blocked:
        return {"blocked": blocked}
    proposed = propose_remember(
        text,
        reason=f"intake_to_lego card {card_id}",
        source="intake_to_lego",
    )
    result: dict[str, Any] = {"propose": proposed}
    if promote_confirm and architect_confirm and proposed.get("ok"):
        entry_id = str(proposed.get("entry_id") or "")
        if entry_id:
            confirmed = confirm_remember(entry_id, target_dataset="eve_memory")
            result["confirm"] = confirmed
            if confirmed.get("ok"):
                mature = disassembly_publish.mark_mature(card_id, architect_confirm=True)
                result["mark_mature"] = mature
    return result


def intake_web(
    url: str,
    *,
    architect_confirm: bool = False,
    publish_heptabase: bool | None = None,
    promote_memory: bool = False,
    promote_confirm: bool = False,
    note: str = "",
) -> dict[str, Any]:
    cleaned = (url or "").strip()
    if not cleaned.startswith(("http://", "https://")):
        return {"ok": False, "error": "url must start with http:// or https://", "kind": "web"}
    host = urlparse(cleaned).netloc or cleaned
    fetched = web_scout.scout(cleaned, write_files=True, note=note or "intake_to_lego")
    if not fetched.get("ok"):
        return {"ok": False, "error": fetched.get("error"), "kind": "web", "detail": fetched}

    title = str(fetched.get("title") or host)
    body = str(fetched.get("text") or fetched.get("content") or "")[:1200]
    cache_path = str(fetched.get("path") or "")
    final_url = str(fetched.get("final_url") or cleaned)
    summary = f"{title} — web intake. {body[:400].strip()}".strip()

    payload = {
        "title": f"{title} — web intake",
        "container": "web",
        "target_summary": summary,
        "connections": [
            {"from": host, "to": "Web cache", "kind": "fetched", "evidence_ref": cache_path or final_url},
            {"from": "Web cache", "to": "Disassembly catalog", "kind": "catalog", "evidence_ref": cache_path or final_url},
            {"from": "Disassembly catalog", "to": "Heptabase (optional)", "kind": "visual", "evidence_ref": final_url},
        ],
        "evidence_refs": [x for x in [cache_path, final_url] if x],
        "lego_hooks": ["intake_to_lego", "web_scout"],
        "evolution_note": WEB_EVOLUTION,
        "learning_stage": "draft",
        "farm_kind": "web",
    }
    written = disassembly_card.write_card(payload)
    if not written.get("ok"):
        return {"ok": False, "error": "disassembly_card write failed", "kind": "web", "detail": written}
    card = written.get("card") or {}
    card_id = str(card.get("id") or "")

    should_publish, publish_reason = _publish_plan(architect_confirm, publish_heptabase)
    publish_result: dict[str, Any] | None = None
    if should_publish and card_id:
        publish_result = disassembly_publish.publish_to_heptabase(card_id, architect_confirm=True)
    elif publish_reason:
        publish_result = {"ok": False, "skipped": True, "reason": publish_reason}

    memory = _maybe_memory_promotion(
        card_id,
        card,
        architect_confirm=architect_confirm,
        promote_memory=promote_memory,
        promote_confirm=promote_confirm,
    )

    return {
        "ok": True,
        "kind": "web",
        "url": cleaned,
        "final_url": final_url,
        "card_id": card_id,
        "cache_path": cache_path,
        "publish": publish_result,
        "memory": memory,
        "next_steps": [
            "For deeper study: save artefacts to Resource Queue and run REA (skill-reverse-engineering).",
            "To promote memory without auto-confirm: propose_remember only; Architect confirms in Memory tab.",
        ],
    }


def _ensure_git_on_path() -> None:
    if shutil.which("git"):
        return
    candidates = [
        Path(os.environ.get("ProgramFiles", "")) / "Git" / "cmd",
        Path(os.environ.get("ProgramFiles(x86)", "")) / "Git" / "cmd",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Git" / "cmd",
    ]
    for directory in candidates:
        git_exe = directory / "git.exe"
        if git_exe.is_file():
            os.environ["PATH"] = f"{directory}{os.pathsep}{os.environ.get('PATH', '')}"
            return


def _shallow_clone(slug: str) -> dict[str, Any]:
    _ensure_git_on_path()
    dest = RESOURCE_QUEUE / slug.replace("/", "_")
    if dest.is_dir() and any(dest.iterdir()):
        return {"ok": True, "path": str(dest), "cloned": False, "note": "already present"}
    RESOURCE_QUEUE.mkdir(parents=True, exist_ok=True)
    remote = f"https://github.com/{slug}.git"
    try:
        proc = subprocess.run(
            ["git", "clone", "--depth", "1", remote, str(dest)],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
    except FileNotFoundError:
        return {"ok": False, "error": "git not on PATH — install Git for Windows or clone manually."}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"git clone timed out for {slug}"}
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:400]
        return {"ok": False, "error": err or f"git clone failed for {slug}"}
    return {"ok": True, "path": str(dest), "cloned": True}


def intake_github(
    *,
    query: str = "",
    repo: str = "",
    depth: str = "scout",
    search_limit: int = 10,
    max_new_cards: int = 5,
    architect_confirm: bool = False,
    publish_heptabase: bool | None = None,
    promote_memory: bool = False,
    promote_confirm: bool = False,
    note: str = "",
) -> dict[str, Any]:
    slug = _normalize_repo(repo)
    cleaned_query = (query or "").strip()

    if depth not in {"scout", "study"}:
        return {"ok": False, "error": "depth must be scout or study", "kind": "github"}

    if slug:
        return _intake_github_repo(
            slug,
            depth=depth,
            architect_confirm=architect_confirm,
            publish_heptabase=publish_heptabase,
            promote_memory=promote_memory,
            promote_confirm=promote_confirm,
            note=note,
        )

    if not cleaned_query:
        status = resource_farm.catalog_status()
        status["hint"] = "Pass query (search) or repo (owner/name or GitHub URL)."
        status["kind"] = "github"
        return status

    farm = resource_farm.run_farm(
        cleaned_query,
        search_limit=search_limit,
        max_new_cards=max_new_cards,
        architect_confirm=architect_confirm,
        publish_heptabase=publish_heptabase,
        note=note or "intake_to_lego",
    )
    farm["kind"] = "github"
    farm["depth"] = "scout"
    if depth == "study" and farm.get("created"):
        study_notes = []
        for row in farm.get("created") or []:
            if not isinstance(row, dict):
                continue
            rs = _normalize_repo(str(row.get("repo") or ""))
            if rs:
                study_notes.append(_shallow_clone(rs))
        farm["study_clones"] = study_notes
    return farm


def _intake_github_repo(
    slug: str,
    *,
    depth: str,
    architect_confirm: bool,
    publish_heptabase: bool | None,
    promote_memory: bool,
    promote_confirm: bool,
    note: str,
) -> dict[str, Any]:
    index = resource_farm.indexed_source_repos()
    if slug in index and depth == "scout":
        return {
            "ok": True,
            "kind": "github",
            "depth": depth,
            "repo": slug,
            "skipped": True,
            "existing_card_id": index[slug].get("card_id"),
            "hint": "Use depth=study to shallow-clone, or REA on Resource Queue path.",
        }

    readme = github_scout.repo_readme(slug, note=note or f"intake_to_lego: {slug}")
    if not readme.get("ok"):
        return {"ok": False, "kind": "github", "repo": slug, "error": readme.get("error"), "step": "readme"}

    search = github_scout.search_repos(slug, limit=1, note=note)
    row: dict[str, Any] = {}
    if search.get("ok") and search.get("results"):
        first = search["results"][0]
        if isinstance(first, dict):
            row = first
    language = str(row.get("language") or "")
    topics = row.get("topics") if isinstance(row.get("topics"), list) else []
    description = str(row.get("description") or "")
    html_url = str(row.get("html_url") or f"https://github.com/{slug}")
    readme_path = str(readme.get("path") or "")
    search_path = str(search.get("path") or "")
    target_summary = " ".join(
        x for x in [description, str(readme.get("summary") or "")[:300]] if x
    ).strip() or f"GitHub repo {slug}."

    clone_info: dict[str, Any] | None = None
    local_path = ""
    if depth == "study":
        clone_info = _shallow_clone(slug)
        if clone_info.get("ok"):
            local_path = str(clone_info.get("path") or "")

    container = resource_farm._guess_container(  # noqa: SLF001
        language,
        [str(t) for t in topics],
        description,
        str(readme.get("summary") or ""),
    )
    connections = resource_farm._scout_connections(  # noqa: SLF001
        slug,
        language,
        [str(t) for t in topics],
        description,
        str(readme.get("summary") or ""),
        html_url,
        readme_path,
        search_path,
    )
    if local_path:
        connections.insert(
            1,
            {
                "from": slug,
                "to": local_path,
                "kind": "study_clone",
                "evidence_ref": local_path,
            },
        )

    payload = {
        "title": f"{slug} — {'study seed' if depth == 'study' else 'scout ticket'}",
        "container": container,
        "target_summary": target_summary,
        "connections": connections,
        "evidence_refs": [x for x in [local_path, readme_path, search_path, html_url] if x],
        "lego_hooks": ["intake_to_lego", "resource_farm", "study" if depth == "study" else "scout_ticket"],
        "evolution_note": STUDY_EVOLUTION if depth == "study" else resource_farm.SCOUT_EVOLUTION,
        "learning_stage": "draft",
        "source_repo": slug,
        "farm_kind": "study" if depth == "study" else "scout",
    }
    written = disassembly_card.write_card(payload)
    if not written.get("ok"):
        return {"ok": False, "kind": "github", "repo": slug, "error": "write_card failed", "detail": written}
    card = written.get("card") or {}
    card_id = str(card.get("id") or "")

    should_publish, publish_reason = _publish_plan(architect_confirm, publish_heptabase)
    publish_result: dict[str, Any] | None = None
    if should_publish and card_id:
        publish_result = disassembly_publish.publish_to_heptabase(card_id, architect_confirm=True)
    elif publish_reason:
        publish_result = {"ok": False, "skipped": True, "reason": publish_reason}

    memory = _maybe_memory_promotion(
        card_id,
        card,
        architect_confirm=architect_confirm,
        promote_memory=promote_memory,
        promote_confirm=promote_confirm,
    )

    return {
        "ok": True,
        "kind": "github",
        "depth": depth,
        "repo": slug,
        "card_id": card_id,
        "clone": clone_info,
        "local_path": local_path or None,
        "publish": publish_result,
        "memory": memory,
        "next_steps": [
            "Scout: hypotheses only — run REA on local_path for verified connections." if depth == "study" else "Clone with depth=study or hand off to skill-reverse-engineering.",
            "Heptabase orange board requires architect_confirm on the same turn.",
        ],
    }


def run_intake(payload: dict[str, Any]) -> dict[str, Any]:
    kind = str(payload.get("kind") or "").strip().lower()
    if kind == "web":
        return intake_web(
            str(payload.get("url") or ""),
            architect_confirm=bool(payload.get("architect_confirm")),
            publish_heptabase=payload.get("publish_heptabase"),
            promote_memory=bool(payload.get("promote_memory")),
            promote_confirm=bool(payload.get("promote_confirm")),
            note=str(payload.get("note") or ""),
        )
    if kind == "github":
        return intake_github(
            query=str(payload.get("query") or ""),
            repo=str(payload.get("repo") or ""),
            depth=str(payload.get("depth") or "scout"),
            search_limit=int(payload.get("search_limit") or 10),
            max_new_cards=int(payload.get("max_new_cards") or 5),
            architect_confirm=bool(payload.get("architect_confirm")),
            publish_heptabase=payload.get("publish_heptabase"),
            promote_memory=bool(payload.get("promote_memory")),
            promote_confirm=bool(payload.get("promote_confirm")),
            note=str(payload.get("note") or ""),
        )
    return {"ok": False, "error": "kind must be web or github"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Read JSON payload from stdin")
    parser.add_argument("--kind", choices=["web", "github"])
    parser.add_argument("--url")
    parser.add_argument("--query")
    parser.add_argument("--repo")
    parser.add_argument("--depth", choices=["scout", "study"], default="scout")
    parser.add_argument("--architect-confirm", action="store_true")
    parser.add_argument("--promote-memory", action="store_true")
    parser.add_argument("--promote-confirm", action="store_true")
    parser.add_argument("--note", default="")
    parser.add_argument("--search-limit", type=int, default=10)
    parser.add_argument("--max-new-cards", type=int, default=5)
    parser.add_argument("--publish-heptabase", action="store_true")
    parser.add_argument("--no-publish-heptabase", action="store_true")
    args = parser.parse_args()

    publish_flag: bool | None = None
    if args.publish_heptabase:
        publish_flag = True
    elif args.no_publish_heptabase:
        publish_flag = False

    if args.json:
        raw = json.load(__import__("sys").stdin)
        out = run_intake(raw if isinstance(raw, dict) else {})
    else:
        if not args.kind:
            parser.error("--kind required unless --json")
        payload: dict[str, Any] = {
            "kind": args.kind,
            "architect_confirm": args.architect_confirm,
            "promote_memory": args.promote_memory,
            "promote_confirm": args.promote_confirm,
            "note": args.note,
            "publish_heptabase": publish_flag,
        }
        if args.kind == "web":
            payload["url"] = args.url or ""
        else:
            payload["query"] = args.query or ""
            payload["repo"] = args.repo or ""
            payload["depth"] = args.depth
            payload["search_limit"] = args.search_limit
            payload["max_new_cards"] = args.max_new_cards
        out = run_intake(payload)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
