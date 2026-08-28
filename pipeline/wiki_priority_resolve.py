"""Maintenance: resolve pending priority subjects → title matches / resolved JSONL."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline.wiki_normalizer import _parse_frontmatter
from pipeline.wiki_ops_paths import reports_dir, validate_year, wiki_md_root
from pipeline.wiki_priority_resolved import append_resolved, resolution_summary_path
from pipeline.wiki_priority_subjects import load_subjects, save_subjects
from pipeline.wiki_title_matcher import decide_match, score_subject_against_titles

_TITLE_LINE_RE = re.compile(r"^title:\s*(.*)$", re.IGNORECASE)
_MD_TITLE_MARK = ".md:title:"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_done_titles(year: str) -> set[str]:
    path = reports_dir(year) / "titles.jsonl"
    done: set[str] = set()
    if not path.exists():
        return done
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = str(obj.get("t") or "").strip().casefold()
        p = str(obj.get("p") or "").strip().casefold()
        if t:
            done.add(t)
        if p:
            done.add(p)
    return done


def _strip_title_value(raw: str) -> str:
    text = str(raw or "").strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1].strip()
    return text


def _catalog_from_rg(year_dir: Path, *, limit_batches: int | None = None) -> list[dict[str, Any]] | None:
    """Build catalog via ripgrep (orders of magnitude faster than per-file Python reads)."""
    rg = shutil.which("rg")
    if not rg:
        cursor_rg = Path.home() / (
            "AppData/Local/Programs/cursor/resources/app/node_modules/@vscode/ripgrep/bin/rg.exe"
        )
        rg = str(cursor_rg) if cursor_rg.exists() else None
    if not rg:
        return None

    batches = sorted(year_dir.glob("batch_*"))
    if limit_batches is not None:
        batches = batches[: max(0, int(limit_batches))]
    if not batches:
        return []

    catalog: list[dict[str, Any]] = []
    for batch_dir in batches:
        try:
            proc = subprocess.run(
                [
                    rg,
                    "-g",
                    "*.md",
                    "-m",
                    "1",
                    "-N",
                    "--with-filename",
                    "--no-heading",
                    "^title:\\s*",
                    str(batch_dir),
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
        except OSError:
            return None
        for line in proc.stdout.splitlines():
            lower = line.lower()
            mark = _MD_TITLE_MARK
            idx = lower.find(mark)
            if idx < 0:
                continue
            path_str = line[: idx + 3]
            title_raw = line[idx + len(mark) :]
            # rg matched "^title:\s*" so remainder may still include "title: value"
            # when --with-filename prints the full line; prefer explicit parse.
            m = _TITLE_LINE_RE.match(line[idx + 4 :])  # after ".md:"
            if m:
                title = _strip_title_value(m.group(1))
            else:
                title = _strip_title_value(title_raw)
            if not title:
                continue
            catalog.append(
                {
                    "title": title,
                    "path": path_str,
                    "page_id": Path(path_str).stem.replace("wiki_", ""),
                    "aliases": [],
                    "batch": batch_dir.name,
                }
            )
    return catalog


def _load_catalog_from_titles_jsonl(year: str) -> list[dict[str, Any]] | None:
    """Prefer the maintenance titles catalog over rescanning D:\\wiki_md (millions of files)."""
    path = reports_dir(year) / "titles.jsonl"
    if not path.exists():
        return None
    catalog: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        title = str(obj.get("t") or "").strip()
        if not title:
            continue
        catalog.append(
            {
                "title": title,
                "path": str(obj.get("p") or "").strip(),
                "page_id": str(obj.get("page_id") or obj.get("id") or "").strip(),
                "aliases": [],
                "batch": str(obj.get("b") or "").strip(),
            }
        )
    return catalog


def build_title_index(
    year: str,
    wiki_md_root_path: Path,
    *,
    limit_batches: int | None = None,
) -> list[dict[str, Any]]:
    y = validate_year(year)
    year_dir = wiki_md_root_path / y
    if not year_dir.is_dir():
        return []

    rg_catalog = _catalog_from_rg(year_dir, limit_batches=limit_batches)
    if rg_catalog is not None:
        return rg_catalog

    # Fallback: slow per-file frontmatter parse
    catalog: list[dict[str, Any]] = []
    batches = sorted(year_dir.glob("batch_*"))
    if limit_batches is not None:
        batches = batches[: max(0, int(limit_batches))]
    for batch_dir in batches:
        for md in sorted(batch_dir.glob("*.md")):
            try:
                text = md.read_text(encoding="utf-8", errors="replace")
                if text.startswith("---"):
                    end = text.find("---", 3)
                    if end != -1:
                        text = text[: end + 3]
                meta, _ = _parse_frontmatter(text)
            except Exception:  # noqa: BLE001
                meta = {}
            title = str(meta.get("title") or md.stem).strip()
            page_id = str(meta.get("page_id") or meta.get("doc_id") or "").strip()
            aliases = []
            for key in ("aliases", "redirects"):
                raw = meta.get(key) or []
                if isinstance(raw, list):
                    aliases.extend(str(a) for a in raw)
                elif raw:
                    aliases.append(str(raw))
            catalog.append(
                {
                    "title": title,
                    "path": str(md),
                    "page_id": page_id,
                    "aliases": aliases,
                    "batch": batch_dir.name,
                }
            )
    return catalog


def resolve_pending_subjects(
    year: str,
    *,
    catalog: list[dict[str, Any]] | None = None,
    candidate_limit: int = 10,
    wiki_md_root_path: Path | None = None,
    limit_batches: int | None = None,
    refresh: bool = False,
    full_catalog: bool = False,
) -> dict[str, Any]:
    y = validate_year(year)
    if catalog is None:
        # Default: progress titles.jsonl (fast). Opt into full wiki with --full-catalog.
        if full_catalog:
            catalog = build_title_index(
                y,
                wiki_md_root_path or wiki_md_root(),
                limit_batches=limit_batches,
            )
        if not catalog:
            catalog = _load_catalog_from_titles_jsonl(y) or []
            if not catalog:
                catalog = build_title_index(
                    y,
                    wiki_md_root_path or wiki_md_root(),
                    limit_batches=limit_batches,
                )
    done = _load_done_titles(y)
    doc = load_subjects()
    counts = {
        "auto": 0,
        "needs_confirm": 0,
        "unmatched": 0,
        "already_done": 0,
        "resolved_appended": 0,
        "refreshed": 0,
    }
    refreshable = {"pending", "needs_confirm", "unmatched"}
    for row in sorted(doc.get("subjects") or [], key=lambda s: int(s.get("rank") or 0)):
        status = str(row.get("status") or "")
        if status == "pending":
            pass
        elif refresh and status in refreshable:
            counts["refreshed"] += 1
        else:
            continue
        cands = score_subject_against_titles(
            str(row.get("subject") or ""),
            catalog,
            candidate_limit=candidate_limit,
        )
        decision = decide_match(cands)
        if decision["decision"] == "auto" and decision["primary"] is not None:
            primary = decision["primary"]
            identity_title = primary.title.casefold()
            identity_path = (primary.path or "").casefold()
            if identity_title in done or identity_path in done:
                row["status"] = "resolved_done"
                row["selected_articles"] = [primary.to_dict()]
                row["resolved"] = primary.to_dict()
                row["candidates"] = [c.to_dict() for c in decision["candidates"]]
                counts["already_done"] += 1
                continue
            append_resolved(
                y,
                {
                    "subject_id": row["id"],
                    "subject": row["subject"],
                    "subject_rank": row["rank"],
                    "title": primary.title,
                    "page_id": primary.page_id,
                    "path": primary.path,
                    "batch": next(
                        (
                            e.get("batch")
                            for e in catalog
                            if e.get("path") == primary.path
                        ),
                        "",
                    ),
                    "match_score": primary.score,
                    "match_reason": (
                        "exact_normalized_title"
                        if primary.match_tier == "exact"
                        else primary.match_tier
                    ),
                    "ingest_status": "awaiting",
                },
            )
            row["status"] = "queued"
            row["selected_articles"] = [primary.to_dict()]
            row["resolved"] = primary.to_dict()
            row["candidates"] = [c.to_dict() for c in decision["candidates"]]
            counts["auto"] += 1
            counts["resolved_appended"] += 1
        elif decision["decision"] == "needs_confirm":
            row["status"] = "needs_confirm"
            row["candidates"] = [c.to_dict() for c in decision["candidates"]]
            row["resolved"] = None
            counts["needs_confirm"] += 1
        else:
            row["status"] = "unmatched"
            row["suggestions"] = [
                c.to_dict() if hasattr(c, "to_dict") else c
                for c in decision.get("suggestions") or []
            ]
            row["candidates"] = []
            counts["unmatched"] += 1
    save_subjects(doc)
    summary = {
        "schema_version": 1,
        "year": y,
        "resolved_at": _now_iso(),
        "counts": counts,
        "catalog_size": len(catalog),
    }
    out = resolution_summary_path(y)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve priority subjects to articles")
    parser.add_argument("--year", default="2017")
    parser.add_argument("--wiki-md-root", default="")
    parser.add_argument("--candidate-limit", type=int, default=10)
    parser.add_argument("--limit-batches", type=int, default=0)
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-score needs_confirm / unmatched with the current matcher",
    )
    parser.add_argument(
        "--full-catalog",
        action="store_true",
        help="Scan full D:\\wiki_md titles via ripgrep (slow; better matches)",
    )
    parser.add_argument(
        "--progress-catalog",
        action="store_true",
        help="Force progress titles.jsonl only (default behavior)",
    )
    args = parser.parse_args(argv)
    try:
        summary = resolve_pending_subjects(
            args.year,
            wiki_md_root_path=Path(args.wiki_md_root) if args.wiki_md_root else None,
            candidate_limit=args.candidate_limit,
            limit_batches=args.limit_batches or None,
            refresh=bool(args.refresh),
            full_catalog=bool(args.full_catalog),
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
