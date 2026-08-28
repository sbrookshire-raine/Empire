"""Wiki report export: checkpoint progress, titles rebuild, new-titles delta."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline.wiki_checkpoint import load_checkpoint
from pipeline.wiki_normalizer import _parse_frontmatter
from pipeline.wiki_ops_paths import (
    BATCHES_TOTAL,
    CORPUS_TOTALS,
    checkpoint_path,
    overnight_pid_alive,
    reports_dir,
    status_path,
    validate_year,
    wiki_md_root,
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sum_docs_processed(checkpoint: dict[str, Any], year: str) -> int:
    y = validate_year(year)
    prefix = f"{y}/"
    total = 0
    for key, batch in (checkpoint.get("batches") or {}).items():
        if not str(key).startswith(prefix):
            continue
        if not isinstance(batch, dict):
            continue
        processed = int(batch.get("processed") or 0)
        if batch.get("status") == "complete" and batch.get("total") is not None:
            total += max(processed, int(batch["total"]))
        else:
            total += processed
    return total


def build_progress_block(checkpoint: dict[str, Any], year: str) -> dict[str, Any]:
    y = validate_year(year)
    docs = sum_docs_processed(checkpoint, y)
    corpus = CORPUS_TOTALS.get(y, 0)
    percent = round(100.0 * docs / corpus, 3) if corpus else 0.0
    prefix = f"{y}/"
    batches_complete = 0
    active_key = ""
    active_next = 0
    for key, batch in sorted((checkpoint.get("batches") or {}).items()):
        if not str(key).startswith(prefix) or not isinstance(batch, dict):
            continue
        if batch.get("status") == "complete":
            batches_complete += 1
        elif not active_key:
            active_key = str(key)
            active_next = int(batch.get("next_index") or 0)
    return {
        "docs_processed": docs,
        "corpus_total": corpus,
        "percent_complete": percent,
        "batches_complete": batches_complete,
        "batches_total": BATCHES_TOTAL.get(y, 0),
        "active_batch_key": active_key,
        "active_next_index": active_next,
        "checkpoint_path": str(checkpoint_path()),
        "source": "checkpoint_sum",
    }


def _atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    tmp.replace(path)


def write_wiki_status(
    year: str,
    *,
    phase: str,
    ingest: dict[str, Any] | None = None,
    maintenance: dict[str, Any] | None = None,
    priorities: dict[str, Any] | None = None,
    titles: dict[str, Any] | None = None,
    skip_titles: bool = True,
    progress: dict[str, Any] | None = None,
) -> Path:
    y = validate_year(year)
    path = status_path(y)
    existing: dict[str, Any] = {}
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            existing = {}
    checkpoint = load_checkpoint()
    progress_block = progress or build_progress_block(checkpoint, y)
    doc = {
        "schema_version": 1,
        "year": y,
        "dataset": f"wikipedia_{y}",
        "phase": phase,
        "updated_at": _now_iso(),
        "ingest": ingest if ingest is not None else existing.get("ingest", {}),
        "progress": progress_block,
        "titles": titles if titles is not None else existing.get("titles", {}),
        "maintenance": maintenance
        if maintenance is not None
        else existing.get("maintenance", {}),
        "priorities": priorities
        if priorities is not None
        else existing.get("priorities", {}),
    }
    if skip_titles and not titles:
        doc["titles"] = existing.get("titles", doc["titles"])
    _atomic_write_json(path, doc)
    return path


def new_titles_diff(prev_titles: set[str], current_titles: set[str]) -> set[str]:
    return current_titles - prev_titles


def _read_title_from_md(path: Path) -> tuple[str, str]:
    try:
        # Frontmatter only — stop after second ---
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                text = text[: end + 3]
        meta, _ = _parse_frontmatter(text if text.startswith("---") else f"---\n---\n{text[:200]}")
        title = str(meta.get("title") or path.stem).strip()
        page_id = str(meta.get("page_id") or meta.get("doc_id") or "").strip()
        return title, page_id
    except Exception:  # noqa: BLE001
        return path.stem, ""


def rebuild_titles_catalog(
    year: str,
    *,
    wiki_md_root_path: Path,
    out_dir: Path,
    checkpoint: dict[str, Any] | None = None,
) -> dict[str, Any]:
    y = validate_year(year)
    year_dir = wiki_md_root_path / y
    cp = checkpoint if checkpoint is not None else load_checkpoint()
    titles_path = out_dir / "titles.jsonl"
    prev_path = out_dir / "titles.prev.jsonl"
    tmp_path = out_dir / "titles.jsonl.tmp"
    out_dir.mkdir(parents=True, exist_ok=True)

    prev_set: set[str] = set()
    if titles_path.exists():
        for line in titles_path.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
                t = str(obj.get("t") or "").strip()
                if t:
                    prev_set.add(t)
            except json.JSONDecodeError:
                continue
        if prev_path.exists():
            prev_path.unlink()
        titles_path.replace(prev_path)
    elif prev_path.exists():
        for line in prev_path.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
                t = str(obj.get("t") or "").strip()
                if t:
                    prev_set.add(t)
            except json.JSONDecodeError:
                continue

    current_set: set[str] = set()
    line_count = 0
    new_lines: list[str] = []
    at = _now_iso()
    batch_dirs = sorted(year_dir.glob("batch_*")) if year_dir.is_dir() else []
    with tmp_path.open("w", encoding="utf-8") as out:
        for batch_dir in batch_dirs:
            key = f"{y}/{batch_dir.name}"
            entry = (cp.get("batches") or {}).get(key, {})
            files = sorted(batch_dir.glob("*.md"))
            if entry.get("status") == "complete":
                limit = len(files)
            else:
                limit = int(entry.get("next_index") or 0)
            for i, md in enumerate(files):
                if i >= limit:
                    break
                title, _page_id = _read_title_from_md(md)
                row = {
                    "t": title,
                    "y": y,
                    "b": batch_dir.name,
                    "i": i,
                    "p": str(md),
                    "at": at,
                }
                line = json.dumps(row, ensure_ascii=False)
                out.write(line + "\n")
                line_count += 1
                current_set.add(title)
                if title not in prev_set:
                    new_lines.append(line)

    tmp_path.replace(titles_path)
    new_path = out_dir / "new-titles.jsonl"
    new_path.write_text("\n".join(new_lines) + ("\n" if new_lines else ""), encoding="utf-8")
    new_meta = {
        "schema_version": 1,
        "year": y,
        "compared_at": at,
        "prev_lines": len(prev_set),
        "current_lines": line_count,
        "new_count": len(new_lines),
        "new_titles_path": str(new_path),
    }
    _atomic_write_json(out_dir / "new-titles.json", new_meta)
    meta = {
        "schema_version": 1,
        "year": y,
        "corpus_total": CORPUS_TOTALS.get(y, 0),
        "batches_total": BATCHES_TOTAL.get(y, 0),
        "titles_bytes": titles_path.stat().st_size if titles_path.exists() else 0,
        "last_export_at": at,
        "wiki_md_root": str(wiki_md_root_path),
    }
    _atomic_write_json(out_dir / "report-meta.json", meta)
    titles_block = {
        "catalog_path": str(titles_path),
        "catalog_lines": line_count,
        "new_titles_path": str(new_path),
        "new_titles_count": len(new_lines),
        "built_at": at,
        "build_source": "md_frontmatter",
    }
    return {
        "titles": titles_block,
        "new_count": len(new_lines),
        "catalog_lines": line_count,
    }


def export_report(
    year: str,
    *,
    wiki_md_root_path: Path | None = None,
    out_root: Path | None = None,
    do_rebuild_titles: bool = False,
    skip_titles: bool = True,
    phase: str | None = None,
) -> dict[str, Any]:
    """Export wiki status. Use do_rebuild_titles (never name a param rebuild_titles):
    a bool named rebuild_titles previously shadowed the catalog function and raised
    ``'bool' object is not callable``.
    """
    y = validate_year(year)
    out_dir = (out_root / y) if out_root else reports_dir(y)
    out_dir.mkdir(parents=True, exist_ok=True)
    checkpoint = load_checkpoint()
    progress = build_progress_block(checkpoint, y)
    titles_block: dict[str, Any] | None = None
    if do_rebuild_titles and not skip_titles:
        if overnight_pid_alive(y):
            raise RuntimeError(
                f"Refuse --rebuild-titles: overnight PID alive for year={y}"
            )
        root = wiki_md_root_path or wiki_md_root()
        rebuilt = rebuild_titles_catalog(
            y, wiki_md_root_path=root, out_dir=out_dir, checkpoint=checkpoint
        )
        titles_block = rebuilt["titles"]
    status = write_wiki_status(
        y,
        phase=phase or ("maintenance" if do_rebuild_titles else "idle"),
        progress=progress,
        titles=titles_block,
        skip_titles=skip_titles or not do_rebuild_titles,
    )
    return {
        "ok": True,
        "year": y,
        "status_path": str(status),
        "progress": progress,
        "titles": titles_block,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export wiki status / titles report")
    parser.add_argument("--year", default="2017")
    parser.add_argument("--wiki-md-root", default="")
    parser.add_argument("--out-root", default="")
    parser.add_argument("--rebuild-titles", action="store_true")
    parser.add_argument("--skip-titles", action="store_true", default=False)
    parser.add_argument("--corpus-total", type=int, default=0)
    parser.add_argument("--phase", default="")
    args = parser.parse_args(argv)
    year = validate_year(args.year)
    if args.corpus_total > 0:
        CORPUS_TOTALS[year] = args.corpus_total
    skip = args.skip_titles or not args.rebuild_titles
    if args.rebuild_titles:
        skip = False
    try:
        result = export_report(
            year,
            wiki_md_root_path=Path(args.wiki_md_root) if args.wiki_md_root else None,
            out_root=Path(args.out_root) if args.out_root else None,
            do_rebuild_titles=args.rebuild_titles,
            skip_titles=skip,
            phase=args.phase or None,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
