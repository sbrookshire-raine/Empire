"""A–Z title index for checkbox browsing (no Cognee).

Progress mode: split titles.jsonl (already ingested / reported).
Full mode: scan D:\\wiki_md\\{year}\\batch_* via ripgrep during maintenance,
then letter-partition so the UI can pick articles NOT yet ingested.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from pipeline.wiki_ops_paths import reports_dir, validate_year, wiki_md_root
from pipeline.wiki_title_matcher import is_useless_title, normalize_text

LETTER_RE = re.compile(r"^[A-Za-z]$")
_TITLE_LINE_RE = re.compile(r"^title:\s*(.*)$", re.IGNORECASE)
_MD_TITLE_MARK = ".md:title:"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def letter_dir(year: str) -> Path:
    return reports_dir(year) / "titles_by_letter"


def letter_index_path(year: str) -> Path:
    return letter_dir(year) / "index.json"


def letter_file(year: str, letter: str) -> Path:
    key = normalize_letter(letter)
    return letter_dir(year) / f"{key}.jsonl"


def ingested_paths_path(year: str) -> Path:
    return letter_dir(year) / "ingested_paths.txt"


def normalize_letter(letter: str) -> str:
    text = str(letter or "").strip()
    if not text:
        return "#"
    ch = text[0]
    if LETTER_RE.match(ch):
        return ch.upper()
    return "#"


def letter_for_title(title: str) -> str:
    norm = normalize_text(title)
    if not norm:
        return "#"
    for prefix in ("the ", "an ", "a "):
        if norm.startswith(prefix):
            norm = norm[len(prefix) :].lstrip()
            break
    if not norm:
        return "#"
    ch = norm[0]
    if "a" <= ch <= "z":
        return ch.upper()
    return "#"


def _strip_title_value(raw: str) -> str:
    text = str(raw or "").strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1].strip()
    return text


def _find_rg() -> str | None:
    rg = shutil.which("rg")
    if rg:
        return rg
    cursor_rg = Path.home() / (
        "AppData/Local/Programs/cursor/resources/app/node_modules/@vscode/ripgrep/bin/rg.exe"
    )
    return str(cursor_rg) if cursor_rg.exists() else None


def _clear_letter_files(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.jsonl"):
        old.unlink(missing_ok=True)
    for old in out_dir.glob("ingested_paths.txt"):
        old.unlink(missing_ok=True)


def _write_sorted_buckets(out_dir: Path, buckets: dict[str, list[str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for letter, lines in sorted(buckets.items()):
        lines.sort(key=lambda s: json.loads(s).get("t", "").casefold())
        (out_dir / f"{letter}.jsonl").write_text(
            "\n".join(lines) + ("\n" if lines else ""),
            encoding="utf-8",
        )
        counts[letter] = len(lines)
    return counts


def _record_line(title: str, path: str, batch: str, page_id: str = "") -> str | None:
    if not title or not path or is_useless_title(title):
        return None
    return json.dumps(
        {"t": title, "p": path, "b": batch, "id": page_id},
        ensure_ascii=False,
    )


def load_ingested_paths(year: str) -> set[str]:
    """Paths already in progress titles.jsonl (approx. already processed)."""
    y = validate_year(year)
    have: set[str] = set()
    snap = ingested_paths_path(y)
    if snap.exists():
        for line in snap.read_text(encoding="utf-8").splitlines():
            p = line.strip()
            if p:
                have.add(p.casefold())
        return have
    src = reports_dir(y) / "titles.jsonl"
    if not src.exists():
        return have
    for line in src.read_text(encoding="utf-8").splitlines():
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        p = str(obj.get("p") or "").strip()
        if p:
            have.add(p.casefold())
    return have


def _write_ingested_snapshot(year: str) -> int:
    y = validate_year(year)
    src = reports_dir(y) / "titles.jsonl"
    out = ingested_paths_path(y)
    paths: list[str] = []
    if src.exists():
        for line in src.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            p = str(obj.get("p") or "").strip()
            if p:
                paths.append(p)
    out.write_text("\n".join(paths) + ("\n" if paths else ""), encoding="utf-8")
    return len(paths)


def build_letter_index_from_progress(year: str, *, source: Path | None = None) -> dict[str, Any]:
    """Split progress titles.jsonl into per-letter JSONL (already-have set)."""
    y = validate_year(year)
    src = source or (reports_dir(y) / "titles.jsonl")
    out_dir = letter_dir(y)
    if not src.exists():
        raise FileNotFoundError(f"Missing titles catalog: {src}")
    buckets: dict[str, list[str]] = defaultdict(list)
    total = 0
    skipped = 0
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        title = str(obj.get("t") or "").strip()
        path = str(obj.get("p") or "").strip()
        rec = _record_line(
            title,
            path,
            str(obj.get("b") or ""),
            str(obj.get("page_id") or obj.get("id") or ""),
        )
        if rec is None:
            skipped += 1
            continue
        buckets[letter_for_title(title)].append(rec)
        total += 1
    _clear_letter_files(out_dir)
    counts = _write_sorted_buckets(out_dir, buckets)
    ingested_n = _write_ingested_snapshot(y)
    index = {
        "schema_version": 2,
        "year": y,
        "mode": "progress",
        "built_at": _now_iso(),
        "source": str(src),
        "total": total,
        "ingested_paths": ingested_n,
        "skipped_useless": skipped,
        "letters": counts,
        "note": (
            "Progress-only index (already reached by ingest). "
            "Run maintenance with --full letter build to browse the whole dump."
        ),
    }
    letter_index_path(y).write_text(json.dumps(index, indent=2), encoding="utf-8")
    return index


def _iter_rg_titles(year_dir: Path, *, limit_batches: int | None = None) -> Iterable[tuple[str, str, str, str]]:
    rg = _find_rg()
    if not rg:
        raise RuntimeError("ripgrep (rg) not found — required for full letter index")
    batches = sorted(year_dir.glob("batch_*"))
    if limit_batches is not None:
        batches = batches[: max(0, int(limit_batches))]
    for batch_dir in batches:
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
        for line in proc.stdout.splitlines():
            lower = line.lower()
            idx = lower.find(_MD_TITLE_MARK)
            if idx < 0:
                continue
            path_str = line[: idx + 3]
            m = _TITLE_LINE_RE.match(line[idx + 4 :])
            title = _strip_title_value(m.group(1) if m else line[idx + len(_MD_TITLE_MARK) :])
            if not title:
                continue
            page_id = Path(path_str).stem.replace("wiki_", "")
            yield title, path_str, batch_dir.name, page_id


def build_letter_index_full(
    year: str,
    *,
    wiki_md_root_path: Path | None = None,
    limit_batches: int | None = None,
) -> dict[str, Any]:
    """Scan full wiki_md year tree; write letter files for UI selection of missing articles."""
    y = validate_year(year)
    year_dir = (wiki_md_root_path or wiki_md_root()) / y
    if not year_dir.is_dir():
        raise FileNotFoundError(f"Missing wiki year dir: {year_dir}")
    out_dir = letter_dir(y)
    _clear_letter_files(out_dir)

    # Stream into unsorted temp letter files to bound memory, then sort.
    tmp_root = Path(tempfile.mkdtemp(prefix=f"wiki-letters-{y}-"))
    handles: dict[str, Any] = {}
    total = 0
    skipped = 0
    try:
        for title, path_str, batch, page_id in _iter_rg_titles(
            year_dir, limit_batches=limit_batches
        ):
            rec = _record_line(title, path_str, batch, page_id)
            if rec is None:
                skipped += 1
                continue
            letter = letter_for_title(title)
            if letter not in handles:
                handles[letter] = (tmp_root / f"{letter}.jsonl").open(
                    "a", encoding="utf-8"
                )
            handles[letter].write(rec + "\n")
            total += 1
            if total % 200_000 == 0:
                print(f"[wiki-letters] scanned {total}…", file=sys.stderr, flush=True)
    finally:
        for fh in handles.values():
            fh.close()

    counts: dict[str, int] = {}
    for tmp in sorted(tmp_root.glob("*.jsonl")):
        letter = tmp.stem
        lines = tmp.read_text(encoding="utf-8").splitlines()
        lines.sort(key=lambda s: json.loads(s).get("t", "").casefold())
        (out_dir / f"{letter}.jsonl").write_text(
            "\n".join(lines) + ("\n" if lines else ""),
            encoding="utf-8",
        )
        counts[letter] = len(lines)
        tmp.unlink(missing_ok=True)
    try:
        tmp_root.rmdir()
    except OSError:
        pass

    ingested_n = _write_ingested_snapshot(y)
    index = {
        "schema_version": 2,
        "year": y,
        "mode": "full",
        "built_at": _now_iso(),
        "source": str(year_dir),
        "total": total,
        "ingested_paths": ingested_n,
        "skipped_useless": skipped,
        "letters": counts,
        "note": (
            "Full dump letter index. UI defaults to titles not yet in progress "
            f"titles.jsonl ({ingested_n} already ingested paths marked)."
        ),
    }
    letter_index_path(y).write_text(json.dumps(index, indent=2), encoding="utf-8")
    return index


def build_letter_index(
    year: str,
    *,
    source: Path | None = None,
    full: bool = False,
    wiki_md_root_path: Path | None = None,
    limit_batches: int | None = None,
) -> dict[str, Any]:
    if full:
        return build_letter_index_full(
            year,
            wiki_md_root_path=wiki_md_root_path,
            limit_batches=limit_batches,
        )
    return build_letter_index_from_progress(year, source=source)


def list_letters(year: str) -> dict[str, Any]:
    y = validate_year(year)
    idx_path = letter_index_path(y)
    if not idx_path.exists():
        return {
            "ok": True,
            "year": y,
            "letters": {},
            "total": 0,
            "mode": None,
            "message": "Letter index missing — run maintenance full letter build",
        }
    idx = json.loads(idx_path.read_text(encoding="utf-8"))
    return {
        "ok": True,
        "year": y,
        "letters": idx.get("letters") or {},
        "total": int(idx.get("total") or 0),
        "ingested_paths": int(idx.get("ingested_paths") or 0),
        "mode": idx.get("mode"),
        "built_at": idx.get("built_at"),
        "note": idx.get("note"),
    }


def page_letter(
    year: str,
    letter: str,
    *,
    offset: int = 0,
    limit: int = 100,
    q: str = "",
    only_missing: bool = True,
) -> dict[str, Any]:
    y = validate_year(year)
    key = normalize_letter(letter)
    path = letter_file(y, key)
    if not path.exists():
        return {
            "ok": True,
            "letter": key,
            "items": [],
            "total": 0,
            "offset": offset,
            "limit": limit,
            "only_missing": only_missing,
            "message": f"No file for letter {key}",
        }
    have = load_ingested_paths(y) if only_missing else set()
    qn = q.strip().casefold()
    matched: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        p = str(obj.get("p") or "")
        already = p.casefold() in have
        if only_missing and already:
            continue
        if qn and qn not in str(obj.get("t") or "").casefold():
            continue
        obj = dict(obj)
        obj["have"] = already
        matched.append(obj)
    total = len(matched)
    slice_ = matched[offset : offset + max(1, limit)]
    return {
        "ok": True,
        "letter": key,
        "items": slice_,
        "total": total,
        "offset": offset,
        "limit": limit,
        "only_missing": only_missing,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build A-Z title letter index")
    parser.add_argument("--year", default="2017")
    parser.add_argument("--source", default="", help="Optional titles.jsonl path (progress mode)")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Scan full D:\\wiki_md year (maintenance; minutes, large)",
    )
    parser.add_argument("--wiki-md-root", default="")
    parser.add_argument("--limit-batches", type=int, default=0)
    args = parser.parse_args(argv)
    try:
        summary = build_letter_index(
            args.year,
            source=Path(args.source) if args.source else None,
            full=bool(args.full),
            wiki_md_root_path=Path(args.wiki_md_root) if args.wiki_md_root else None,
            limit_batches=args.limit_batches or None,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
