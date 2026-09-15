"""Import MediaWiki redirect + page_props metadata into Title DNS.

Sources (any that exist):
  - redirects.tsv          alias<TAB>canonical
  - page_props_disambig.tsv title (one per line) OR title<TAB>1
  - enwiki-*-redirect.sql[.gz] + enwiki-*-page.sql[.gz] (optional full dumps)

Does not require Weaviate. Safe to re-run (upsert aliases / flags).
"""

from __future__ import annotations

import argparse
import gzip
import logging
import re
import sqlite3
from pathlib import Path
from typing import Iterable, Iterator

from pipeline.wiki_ops_paths import reports_dir, validate_year
from pipeline.wiki_title_dns import (
    apply_common_aliases,
    default_index_path,
    default_redirects_path,
    import_redirects,
    normalize_text,
    upsert_aliases,
    write_common_redirects_tsv,
    _connect,
)

logger = logging.getLogger(__name__)

_INSERT_RE = re.compile(
    r"\((\d+),(\d+),'((?:\\'|[^'])*)'",
    re.S,
)
_PAGE_ROW_RE = re.compile(
    r"\((\d+),(\d+),'((?:\\'|[^'])*)'",
    re.S,
)


def default_disambig_path(year: str) -> Path:
    return reports_dir(year) / "page_props_disambig.tsv"


def ensure_disambiguation_column(conn: sqlite3.Connection) -> None:
    cols = {str(row[1]) for row in conn.execute("PRAGMA table_info(pages)").fetchall()}
    if "is_disambiguation" not in cols:
        conn.execute(
            "ALTER TABLE pages ADD COLUMN is_disambiguation INTEGER NOT NULL DEFAULT 0"
        )


def mark_disambiguation_titles(conn: sqlite3.Connection, titles: Iterable[str]) -> int:
    ensure_disambiguation_column(conn)
    n = 0
    for title in titles:
        key = normalize_text(title)
        if not key:
            continue
        cur = conn.execute(
            "UPDATE pages SET is_disambiguation = 1 WHERE title_norm = ?",
            (key,),
        )
        n += int(cur.rowcount or 0)
        # Also accept bare title matching pages titled "X (disambiguation)"
        if not cur.rowcount:
            cur = conn.execute(
                "UPDATE pages SET is_disambiguation = 1 WHERE title_norm = ?",
                (normalize_text(f"{title} (disambiguation)")),
            )
            n += int(cur.rowcount or 0)
    return n


def import_disambiguation_tsv(index_path: Path, tsv_path: Path) -> int:
    if not tsv_path.is_file():
        logger.info("No disambiguation TSV at %s — skip", tsv_path)
        return 0
    titles: list[str] = []
    for line in tsv_path.read_text(encoding="utf-8", errors="replace").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        title = raw.split("\t", 1)[0].strip()
        if title:
            titles.append(title)
    conn = _connect(index_path)
    try:
        n = mark_disambiguation_titles(conn, titles)
        conn.commit()
        return n
    finally:
        conn.close()


def _open_maybe_gzip(path: Path):
    if str(path).lower().endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return path.open("r", encoding="utf-8", errors="replace")


def _unescape_sql_title(raw: str) -> str:
    text = raw.replace("\\'", "'").replace("\\\\", "\\")
    return text.replace("_", " ")


def iter_redirect_sql_pairs(
    redirect_sql: Path,
    page_sql: Path,
    *,
    max_rows: int = 0,
) -> Iterator[tuple[str, str]]:
    """Yield (alias_title, canonical_title) from MediaWiki SQL dumps (ns=0)."""
    # page_id -> title for namespace 0
    id_to_title: dict[int, str] = {}
    logger.info("Scanning page dump %s", page_sql)
    with _open_maybe_gzip(page_sql) as handle:
        for line in handle:
            if "INSERT INTO" not in line or "`page`" not in line and "page" not in line[:80]:
                if not line.lstrip().startswith("INSERT"):
                    continue
            for match in _PAGE_ROW_RE.finditer(line):
                page_id = int(match.group(1))
                ns = int(match.group(2))
                if ns != 0:
                    continue
                id_to_title[page_id] = _unescape_sql_title(match.group(3))
            if max_rows and len(id_to_title) >= max_rows:
                break
    logger.info("Loaded %s ns=0 page titles", len(id_to_title))

    logger.info("Scanning redirect dump %s", redirect_sql)
    count = 0
    with _open_maybe_gzip(redirect_sql) as handle:
        for line in handle:
            if "INSERT INTO" not in line:
                continue
            for match in _INSERT_RE.finditer(line):
                from_id = int(match.group(1))
                ns = int(match.group(2))
                if ns != 0:
                    continue
                alias = id_to_title.get(from_id)
                if not alias:
                    continue
                canonical = _unescape_sql_title(match.group(3))
                if not canonical or canonicalize_same(alias, canonical):
                    continue
                yield alias, canonical
                count += 1
                if max_rows and count >= max_rows:
                    return


def canonicalize_same(a: str, b: str) -> bool:
    return normalize_text(a) == normalize_text(b)


def import_redirect_sql(
    index_path: Path,
    redirect_sql: Path,
    page_sql: Path,
    *,
    max_rows: int = 0,
) -> int:
    if not redirect_sql.is_file() or not page_sql.is_file():
        logger.warning("Missing SQL dumps — skip redirect SQL import")
        return 0
    pairs = list(iter_redirect_sql_pairs(redirect_sql, page_sql, max_rows=max_rows))
    conn = _connect(index_path)
    try:
        # Only keep aliases whose canonical exists in pages
        existing = {
            str(row["title_norm"])
            for row in conn.execute("SELECT title_norm FROM pages").fetchall()
        }
        title_by_norm = {
            str(row["title_norm"]): str(row["title"])
            for row in conn.execute("SELECT title_norm, title FROM pages").fetchall()
        }
        kept: list[tuple[str, str]] = []
        for alias, canonical in pairs:
            canon_n = normalize_text(canonical)
            if canon_n not in existing:
                continue
            kept.append((alias, title_by_norm.get(canon_n, canonical)))
        n = upsert_aliases(conn, kept)
        conn.commit()
        return n
    finally:
        conn.close()


def seed_disambig_from_titles(conn: sqlite3.Connection) -> int:
    """Mark pages whose title ends with (disambiguation)."""
    ensure_disambiguation_column(conn)
    cur = conn.execute(
        "UPDATE pages SET is_disambiguation = 1 "
        "WHERE title LIKE '% (disambiguation)' OR title LIKE '%(disambiguation)'"
    )
    return int(cur.rowcount or 0)


def import_mediawiki_meta(
    year: str = "2026",
    *,
    index_path: Path | None = None,
    redirects_tsv: Path | None = None,
    disambig_tsv: Path | None = None,
    redirect_sql: Path | None = None,
    page_sql: Path | None = None,
    max_sql_rows: int = 0,
) -> dict[str, object]:
    y = validate_year(year)
    index = index_path or default_index_path(y)
    if not index.is_file():
        return {"ok": False, "error": f"missing index {index}"}

    write_common_redirects_tsv(redirects_tsv or default_redirects_path(y))
    common_n = apply_common_aliases(index)
    redir_n = import_redirects(index, redirects_tsv or default_redirects_path(y))
    sql_n = 0
    if redirect_sql and page_sql:
        sql_n = import_redirect_sql(
            index, Path(redirect_sql), Path(page_sql), max_rows=max_sql_rows
        )

    conn = _connect(index)
    try:
        title_n = seed_disambig_from_titles(conn)
        conn.commit()
    finally:
        conn.close()
    disambig_n = import_disambiguation_tsv(index, disambig_tsv or default_disambig_path(y))

    return {
        "ok": True,
        "year": y,
        "index_path": str(index),
        "common_aliases": common_n,
        "redirect_tsv_aliases": redir_n,
        "redirect_sql_aliases": sql_n,
        "disambiguation_title_flags": title_n,
        "disambiguation_tsv_flags": disambig_n,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Import MediaWiki meta into Title DNS")
    parser.add_argument("--year", default="2026")
    parser.add_argument("--index", default="")
    parser.add_argument("--redirects-tsv", default="")
    parser.add_argument("--disambig-tsv", default="")
    parser.add_argument("--redirect-sql", default="")
    parser.add_argument("--page-sql", default="")
    parser.add_argument("--max-sql-rows", type=int, default=0)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    result = import_mediawiki_meta(
        args.year,
        index_path=Path(args.index) if args.index else None,
        redirects_tsv=Path(args.redirects_tsv) if args.redirects_tsv else None,
        disambig_tsv=Path(args.disambig_tsv) if args.disambig_tsv else None,
        redirect_sql=Path(args.redirect_sql) if args.redirect_sql else None,
        page_sql=Path(args.page_sql) if args.page_sql else None,
        max_sql_rows=args.max_sql_rows,
    )
    print(result)
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
