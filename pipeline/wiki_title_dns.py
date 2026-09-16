"""Title DNS: exact/alias existence check, then open D:\\wiki_md.

Weaviate similarity is not an existence gate. This SQLite registry answers
"is there a page?" in milliseconds. Chat lookup should resolve here first.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import shutil
import sqlite3
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Literal

from pipeline.wiki_link_rank import rank_related_titles, select_hop_titles
from pipeline.wiki_ops_paths import reports_dir, validate_year, wiki_md_root
from pipeline.wiki_title_matcher import (
    normalize_text,
    strip_leading_article,
    strip_parens,
)

logger = logging.getLogger(__name__)

ResolveStatus = Literal["hit", "miss", "ambiguous"]

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS pages (
    title_norm TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    path TEXT NOT NULL,
    rel_path TEXT NOT NULL,
    page_id TEXT,
    year TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS aliases (
    alias_norm TEXT PRIMARY KEY,
    title_norm TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_aliases_title ON aliases(title_norm);
CREATE INDEX IF NOT EXISTS idx_pages_rel ON pages(rel_path);
CREATE TABLE IF NOT EXISTS links (
    from_norm TEXT NOT NULL,
    to_norm TEXT NOT NULL,
    to_title TEXT NOT NULL,
    PRIMARY KEY (from_norm, to_norm)
);
CREATE INDEX IF NOT EXISTS idx_links_to ON links(to_norm);
CREATE TABLE IF NOT EXISTS link_progress (
    rel_path TEXT PRIMARY KEY
);
"""

LINK_SKIP_PREFIXES = (
    "wikipedia:",
    "template:",
    "file:",
    "image:",
    "media:",
    "help:",
    "user:",
    "draft:",
    "module:",
    "mediawiki:",
    "special:",
    "talk:",
    "timedtext:",
    "category talk:",
    "wikipedia talk:",
)
MAX_LINKS_PER_PAGE = 80
LINK_READ_BYTES = 24_576
INBOUND_FETCH_CAP = 2_000

TV_FALSE_FRIENDS = frozenset(
    {
        "following",
        "cult following",
        "trend following",
        "score following",
    }
)

_YEAR_IN_QUESTION_RE = re.compile(r"\b((?:19|20)\d{2})\b")
_EIGHTIES_RE = re.compile(r"\b(?:80s|80's|eighties|1980s)\b", re.I)
_TV_TITLE_MARKERS = (
    "(tv",
    "miniseries",
    "television series",
    "tv series",
    "tv program",
)
_YEAR_TV_KINDS = (
    "miniseries",
    "TV series",
    "American TV series",
    "film",
)

PROGRAMMATIC_SUFFIXES = (
    " (TV series)",
    " (American TV series)",
    " (British TV series)",
    " (film)",
    " (song)",
    " (album)",
)

_TITLE_LINE_RE = re.compile(r"^title:\s*(.*)$", re.IGNORECASE)
_MD_TITLE_MARK = ".md:title:"


@dataclass(frozen=True)
class DnsHit:
    title: str
    path: str
    rel_path: str
    page_id: str
    year: str


@dataclass(frozen=True)
class DnsResult:
    status: ResolveStatus
    query: str
    year: str
    hit: DnsHit | None = None
    candidates: tuple[DnsHit, ...] = ()
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        return payload


def default_index_path(year: str) -> Path:
    override = os.environ.get("EMPIRE_WIKI_TITLE_INDEX", "").strip()
    if override:
        return Path(override)
    return reports_dir(year) / "title-index.sqlite"


def default_redirects_path(year: str) -> Path:
    override = os.environ.get("EMPIRE_WIKI_REDIRECTS", "").strip()
    if override:
        return Path(override)
    return reports_dir(year) / "redirects.tsv"


def _connect(index_path: Path) -> sqlite3.Connection:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(index_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.executescript(SCHEMA_SQL)
    cols = {str(row[1]) for row in conn.execute("PRAGMA table_info(pages)").fetchall()}
    if "is_disambiguation" not in cols:
        conn.execute(
            "ALTER TABLE pages ADD COLUMN is_disambiguation INTEGER NOT NULL DEFAULT 0"
        )
    return conn


def _strip_title_value(raw: str) -> str:
    text = str(raw or "").strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1].strip()
    return text


def _rel_path(path: Path, year_root: Path) -> str:
    try:
        return path.resolve().relative_to(year_root.resolve()).as_posix()
    except ValueError:
        return path.name


def _rg_executable() -> str | None:
    rg = shutil.which("rg")
    if rg:
        return rg
    cursor_rg = Path.home() / (
        "AppData/Local/Programs/cursor/resources/app/node_modules/@vscode/ripgrep/bin/rg.exe"
    )
    return str(cursor_rg) if cursor_rg.exists() else None


def _row_to_hit(row: sqlite3.Row, year: str) -> DnsHit:
    return DnsHit(
        title=str(row["title"] or ""),
        path=str(row["path"] or ""),
        rel_path=str(row["rel_path"] or ""),
        page_id=str(row["page_id"] or ""),
        year=str(row["year"] or year),
    )


def _page_is_disambiguation(conn: sqlite3.Connection, title_norm: str) -> bool:
    try:
        row = conn.execute(
            "SELECT is_disambiguation FROM pages WHERE title_norm = ?",
            (title_norm,),
        ).fetchone()
    except sqlite3.OperationalError:
        return False
    if not row:
        return False
    try:
        return int(row[0] or 0) == 1
    except (TypeError, ValueError):
        return False


def _lookup_exact(conn: sqlite3.Connection, title_norm: str, year: str) -> DnsHit | None:
    row = conn.execute(
        "SELECT title, path, rel_path, page_id, year FROM pages WHERE title_norm = ?",
        (title_norm,),
    ).fetchone()
    if row:
        return _row_to_hit(row, year)
    alias = conn.execute(
        "SELECT title_norm FROM aliases WHERE alias_norm = ?",
        (title_norm,),
    ).fetchone()
    if not alias:
        return None
    row = conn.execute(
        "SELECT title, path, rel_path, page_id, year FROM pages WHERE title_norm = ?",
        (str(alias["title_norm"]),),
    ).fetchone()
    return _row_to_hit(row, year) if row else None


def _disambiguation_branch(
    conn: sqlite3.Connection, title_norm: str, year: str, *, limit: int = 8
) -> list[DnsHit]:
    rows = conn.execute(
        "SELECT title, path, rel_path, page_id, year FROM pages "
        "WHERE title_norm LIKE ? ESCAPE '\\' ORDER BY length(title), title LIMIT ?",
        (title_norm.replace("%", "\\%") + " (%", limit),
    ).fetchall()
    return [_row_to_hit(row, year) for row in rows]


def _tv_context(user_question: str) -> bool:
    ql = (user_question or "").casefold()
    return any(
        token in ql
        for token in ("tv", "television", "series", "show", "actor", "cast", "starred")
    )


def _years_from_question(user_question: str) -> tuple[str, ...]:
    """Exact years only — '1980s' must not become year 1980."""
    raw = user_question or ""
    # Strip decade forms so 1980s / 1980's do not yield a false 1980.
    cleaned = re.sub(r"\b((?:19|20)\d{2})\s*'?s\b", " ", raw, flags=re.I)
    return tuple(_YEAR_IN_QUESTION_RE.findall(cleaned))


def _is_generic_letter_title(title: str) -> bool:
    return len(normalize_text(title)) <= 2


def _letter_needs_disambiguation(user_question: str) -> bool:
    ql = (user_question or "").casefold()
    return any(
        token in ql
        for token in (
            "production",
            "film",
            "movie",
            "horror",
            "tv",
            "television",
            "series",
            "miniseries",
            "album",
            "song",
            "band",
        )
    )


def _is_tv_page_title(title: str) -> bool:
    low = (title or "").casefold()
    return any(marker in low for marker in _TV_TITLE_MARKERS)


def _filter_tv_branch(hits: list[DnsHit], user_question: str) -> list[DnsHit]:
    tv_hits = [hit for hit in hits if _is_tv_page_title(hit.title)]
    if not tv_hits:
        return hits
    ql = (user_question or "").casefold()
    years = _years_from_question(user_question)
    if years:
        year_hits = [hit for hit in tv_hits if any(year in hit.title for year in years)]
        if year_hits:
            tv_hits = year_hits
    elif _EIGHTIES_RE.search(user_question or ""):
        decade = [hit for hit in tv_hits if re.search(r"\b198\d\b", hit.title)]
        if decade:
            tv_hits = decade
    if "miniseries" in ql or "original" in ql:
        mini = [hit for hit in tv_hits if "miniseries" in hit.title.casefold()]
        if mini:
            return mini
    if "tv series" in ql or "television series" in ql:
        weekly = [
            hit
            for hit in tv_hits
            if "tv series" in hit.title.casefold() and "miniseries" not in hit.title.casefold()
        ]
        if weekly:
            return weekly
    return tv_hits


def _reject_false_friend(hit: DnsHit | None, *, tv_ask: bool) -> DnsHit | None:
    if hit is None:
        return None
    if tv_ask and normalize_text(hit.title) in TV_FALSE_FRIENDS:
        return None
    return hit


def subject_variants(subject: str) -> list[str]:
    """Exact forms to try before declaring a miss."""
    raw = (subject or "").strip()
    if not raw:
        return []
    forms: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        text = value.strip()
        if not text:
            return
        key = normalize_text(text)
        if not key or key in seen:
            return
        seen.add(key)
        forms.append(text)

    add(raw)
    add(strip_leading_article(raw))
    add(strip_parens(raw))
    add(strip_parens(strip_leading_article(raw)))
    for suffix in PROGRAMMATIC_SUFFIXES:
        add(f"{raw}{suffix}")
        stripped = strip_leading_article(raw)
        if stripped != raw:
            add(f"{stripped}{suffix}")
    return forms


def _prefer_primary_title(
    hits: list[DnsHit],
    query: str,
    user_question: str,
) -> DnsHit | None:
    """Collapse show-vs-film forks when the question clearly names one branch."""
    if len(hits) < 2:
        return hits[0] if hits else None
    ql = (user_question or "").casefold()
    qn = normalize_text(query)
    series_cues = (
        "song",
        "songs",
        "series",
        "episode",
        "cast",
        "season",
        "netflix",
        "tv",
        "television",
        "show",
    )
    film_cues = ("film", "movie", "cinema", "theatrical")
    series_ask = any(token in ql for token in series_cues)
    film_ask = any(token in ql for token in film_cues)
    if film_ask and not series_ask:
        films = [
            h
            for h in hits
            if "(film)" in h.title.casefold() or re.search(r"\bfilm\b", h.title, re.I)
        ]
        if len(films) == 1:
            return films[0]
        return None
    # Default / series-flavored asks: prefer the bare encyclopedia title over "(film)".
    bare = [h for h in hits if normalize_text(h.title) == qn]
    if len(bare) == 1:
        return bare[0]
    if series_ask:
        non_film = [h for h in hits if "(film)" not in h.title.casefold()]
        if len(non_film) == 1:
            return non_film[0]
    return None


def resolve(
    subject: str,
    year: str = "2026",
    *,
    user_question: str = "",
    index_path: Path | None = None,
) -> DnsResult:
    y = validate_year(year)
    query = (subject or "").strip()
    if not query:
        return DnsResult(status="miss", query=query, year=y, reason="empty subject")
    path = index_path or default_index_path(y)
    if not path.is_file():
        return DnsResult(
            status="miss",
            query=query,
            year=y,
            reason=f"title index missing ({path})",
        )
    tv_ask = _tv_context(user_question)
    letter_mode = _is_generic_letter_title(query) and _letter_needs_disambiguation(
        user_question
    )
    conn = _connect(path)
    try:
        if letter_mode:
            branch = [
                h
                for h in _disambiguation_branch(
                    conn, normalize_text(query), y, limit=80
                )
                if _reject_false_friend(h, tv_ask=tv_ask)
            ]
            ql = (user_question or "").casefold()
            years = _years_from_question(user_question)
            if any(token in ql for token in ("horror", "movie", "film", "production")):
                films = [
                    h
                    for h in branch
                    if any(
                        marker in h.title.casefold()
                        for marker in ("film", "movie", "horror")
                    )
                ]
                if years:
                    year_films = [
                        h for h in films if any(year in h.title for year in years)
                    ]
                    if year_films:
                        films = year_films
                if len(films) == 1:
                    return DnsResult(
                        status="hit",
                        query=query,
                        year=y,
                        hit=films[0],
                        reason="letter_film",
                    )
                if len(films) > 1:
                    return DnsResult(
                        status="ambiguous",
                        query=query,
                        year=y,
                        candidates=tuple(films[:8]),
                        reason="letter_film_fork",
                    )
            if tv_ask:
                branch = _filter_tv_branch(branch, user_question)
            if len(branch) == 1:
                return DnsResult(
                    status="hit", query=query, year=y, hit=branch[0], reason="letter_branch"
                )
            if len(branch) > 1:
                return DnsResult(
                    status="ambiguous",
                    query=query,
                    year=y,
                    candidates=tuple(branch[:8]),
                    reason="letter_fork",
                )
        seen: set[str] = set()
        hits: list[DnsHit] = []
        forms = list(subject_variants(query))
        if tv_ask:
            year_forms: list[str] = []
            for asked_year in _years_from_question(user_question):
                for kind in _YEAR_TV_KINDS:
                    year_forms.append(f"{query} ({asked_year} {kind})")
            forms = year_forms + forms
        for form in forms:
            hit = _reject_false_friend(
                _lookup_exact(conn, normalize_text(form), y),
                tv_ask=tv_ask,
            )
            if hit is None:
                continue
            key = hit.rel_path or hit.title
            if key in seen:
                continue
            seen.add(key)
            hits.append(hit)
            exact = normalize_text(hit.title) == normalize_text(form)
            if not exact:
                continue
            if tv_ask and _is_generic_letter_title(hit.title):
                continue
            if tv_ask and (
                _years_from_question(user_question) or _EIGHTIES_RE.search(user_question or "")
            ):
                if not (
                    _is_tv_page_title(hit.title)
                    and (
                        any(year in hit.title for year in _years_from_question(user_question))
                        or (
                            _EIGHTIES_RE.search(user_question or "")
                            and re.search(r"\b198\d\b", hit.title)
                        )
                    )
                ):
                    continue
            # Bare letter pages are rarely the answer when the user names film/TV/production.
            if _is_generic_letter_title(hit.title) and _letter_needs_disambiguation(
                user_question
            ):
                continue
            # Disambiguation hub pages are not answers — expand to titled variants.
            if _page_is_disambiguation(conn, normalize_text(hit.title)) or hit.title.casefold().endswith(
                "(disambiguation)"
            ):
                branch = [
                    h
                    for h in _disambiguation_branch(
                        conn,
                        normalize_text(strip_parens(hit.title) or query),
                        y,
                        limit=60 if tv_ask else 12,
                    )
                    if _reject_false_friend(h, tv_ask=tv_ask)
                ]
                if tv_ask:
                    branch = _filter_tv_branch(branch, user_question)
                if len(branch) == 1:
                    return DnsResult(
                        status="hit",
                        query=query,
                        year=y,
                        hit=branch[0],
                        reason="disambiguation_hub",
                    )
                if len(branch) > 1:
                    return DnsResult(
                        status="ambiguous",
                        query=query,
                        year=y,
                        candidates=tuple(branch[:8]),
                        reason="disambiguation_hub",
                    )
            return DnsResult(status="hit", query=query, year=y, hit=hit, reason="exact")
        if tv_ask:
            hits = _filter_tv_branch(hits, user_question)
        if len(hits) == 1:
            only = hits[0]
            eighties_ask = bool(_EIGHTIES_RE.search(user_question or ""))
            if tv_ask and eighties_ask and not re.search(r"\b198\d\b", only.title):
                hits = []
            else:
                return DnsResult(status="hit", query=query, year=y, hit=only, reason="alias")
        if len(hits) > 1:
            preferred = _prefer_primary_title(hits, query, user_question)
            if preferred is not None:
                return DnsResult(
                    status="hit",
                    query=query,
                    year=y,
                    hit=preferred,
                    reason="preferred_primary_title",
                )
            return DnsResult(
                status="ambiguous",
                query=query,
                year=y,
                candidates=tuple(hits[:8]),
                reason="multiple exact/alias matches",
            )
        branch = [
            h
            for h in _disambiguation_branch(
                conn,
                normalize_text(query),
                y,
                limit=60 if tv_ask else 8,
            )
            if _reject_false_friend(h, tv_ask=tv_ask)
        ]
        if tv_ask:
            branch = _filter_tv_branch(branch, user_question)
        if len(branch) == 1:
            return DnsResult(status="hit", query=query, year=y, hit=branch[0], reason="disambiguation")
        if len(branch) > 1:
            preferred = _prefer_primary_title(branch, query, user_question)
            if preferred is not None:
                return DnsResult(
                    status="hit",
                    query=query,
                    year=y,
                    hit=preferred,
                    reason="preferred_primary_title",
                )
            return DnsResult(
                status="ambiguous",
                query=query,
                year=y,
                candidates=tuple(branch[:8]),
                reason="multiple titled variants",
            )
        return DnsResult(status="miss", query=query, year=y, reason="not in title registry")
    finally:
        conn.close()


def upsert_pages(conn: sqlite3.Connection, rows: Iterable[tuple[str, str, str, str, str]]) -> int:
    """rows: (title, path, rel_path, page_id, year)"""
    payload: list[tuple[str, str, str, str, str, str]] = []
    for title, path, rel_path, page_id, year in rows:
        title = title.strip()
        if not title:
            continue
        payload.append((normalize_text(title), title, path, rel_path, page_id, year))
    if not payload:
        return 0
    conn.executemany(
        "INSERT OR REPLACE INTO pages(title_norm, title, path, rel_path, page_id, year) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        payload,
    )
    return len(payload)


def upsert_aliases(conn: sqlite3.Connection, pairs: Iterable[tuple[str, str]]) -> int:
    """pairs: (alias_title, canonical_title)"""
    payload: list[tuple[str, str]] = []
    for alias, canonical in pairs:
        alias_n = normalize_text(alias)
        canon_n = normalize_text(canonical)
        if not alias_n or not canon_n or alias_n == canon_n:
            continue
        payload.append((alias_n, canon_n))
    if not payload:
        return 0
    conn.executemany(
        "INSERT OR REPLACE INTO aliases(alias_norm, title_norm) VALUES (?, ?)",
        payload,
    )
    return len(payload)


def seed_parenthetical_aliases(conn: sqlite3.Connection) -> int:
    """Bare title → disambiguated page when exactly one such page exists."""
    rows = conn.execute("SELECT title_norm, title FROM pages").fetchall()
    existing = {str(r["title_norm"]) for r in rows}
    by_bare: dict[str, list[str]] = {}
    for row in rows:
        title = str(row["title"] or "")
        bare = strip_parens(title)
        if bare == title:
            continue
        bare_n = normalize_text(bare)
        if not bare_n or bare_n in existing:
            continue
        by_bare.setdefault(bare_n, []).append(title)
    pairs: list[tuple[str, str]] = []
    for _bare_n, titles in by_bare.items():
        if len(titles) != 1:
            continue
        pairs.append((strip_parens(titles[0]), titles[0]))
    return upsert_aliases(conn, pairs)


# High-value aliases for EMPIRE chat pain points (until a full MediaWiki redirect dump lands).
COMMON_REDIRECT_ALIASES: tuple[tuple[str, str], ...] = (
    ("Running Up That Hill (Kate Bush song)", "Running Up That Hill"),
    ("running up that hill", "Running Up That Hill"),
    ("kate bush running up the hill", "Running Up That Hill"),
    ("Running Up That Hill (song)", "Running Up That Hill"),
    ("A Deal with God", "Running Up That Hill"),
    ("Stranger Things (TV series)", "Stranger Things"),
    ("Stranger Things (Netflix series)", "Stranger Things"),
    ("The Following (TV series)", "The Following"),
    ("The Following (TV show)", "The Following"),
    ("V (TV miniseries)", "V (1983 miniseries)"),
    ("V the miniseries", "V (1983 miniseries)"),
    ("V (1983)", "V (1983 miniseries)"),
    ("V (1984)", "V (1984 TV series)"),
    ("Kate Bush (singer)", "Kate Bush"),
)


def seed_common_aliases(conn: sqlite3.Connection) -> int:
    """Seed curated alias→canonical pairs when the canonical page exists."""
    existing = {
        str(row["title_norm"])
        for row in conn.execute("SELECT title_norm FROM pages").fetchall()
    }
    title_by_norm = {
        str(row["title_norm"]): str(row["title"])
        for row in conn.execute("SELECT title_norm, title FROM pages").fetchall()
    }
    pairs: list[tuple[str, str]] = []
    for alias, canonical in COMMON_REDIRECT_ALIASES:
        canon_n = normalize_text(canonical)
        if canon_n not in existing:
            continue
        pairs.append((alias, title_by_norm.get(canon_n, canonical)))
    return upsert_aliases(conn, pairs)


def write_common_redirects_tsv(path: Path) -> int:
    """Write COMMON_REDIRECT_ALIASES to redirects.tsv (merge with comments)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Title DNS aliases - tab-separated: alias<TAB>canonical",
        "# Curated EMPIRE common redirects (seed_common_aliases).",
        "# Full MediaWiki redirect dump can replace/extend this file.",
        "",
    ]
    for alias, canonical in COMMON_REDIRECT_ALIASES:
        lines.append(f"{alias}\t{canonical}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(COMMON_REDIRECT_ALIASES)


def apply_common_aliases(index_path: Path) -> int:
    conn = _connect(index_path)
    try:
        n = seed_common_aliases(conn)
        conn.commit()
        return n
    finally:
        conn.close()



def _skip_link_target(title: str) -> bool:
    text = (title or "").strip()
    if not text or text.startswith("#"):
        return True
    key = text.casefold()
    return any(key.startswith(prefix) for prefix in LINK_SKIP_PREFIXES)


def _read_frontmatter_head(path: Path) -> str:
    try:
        raw = path.read_bytes()[:LINK_READ_BYTES].decode("utf-8", errors="replace")
    except OSError:
        return ""
    if not raw.startswith("---"):
        return ""
    end = raw.find("\n---", 3)
    if end < 0:
        return raw
    return raw[3:end]


def _outgoing_from_frontmatter(block: str) -> list[str]:
    from pipeline.wiki_normalizer import _as_list, _parse_frontmatter_manual

    meta = _parse_frontmatter_manual(block)
    return _as_list(meta.get("outgoing_links"))


def build_links(
    year: str = "2026",
    *,
    index_path: Path | None = None,
    wiki_root: Path | None = None,
    resume: bool = True,
    limit_pages: int | None = None,
) -> dict[str, Any]:
    """Second pass: title → outgoing_links web from markdown frontmatter."""
    y = validate_year(year)
    year_root = (wiki_root or wiki_md_root()) / y
    out = index_path or default_index_path(y)
    if not out.is_file():
        raise FileNotFoundError(f"title index missing: {out}")
    conn = _connect(out)
    inserted = 0
    scanned = 0
    skipped = 0
    try:
        if not resume:
            conn.execute("DELETE FROM links")
            conn.execute("DELETE FROM link_progress")
            conn.commit()
        done = {str(r[0]) for r in conn.execute("SELECT rel_path FROM link_progress")}
        rows = conn.execute(
            "SELECT title, title_norm, rel_path FROM pages ORDER BY rel_path"
        ).fetchall()
        logger.info(
            "links %s: %s pages in index, %s already done (resume=%s)",
            y,
            len(rows),
            len(done),
            resume,
        )
        pending: list[tuple[str, str, str]] = []
        for row in rows:
            rel = str(row["rel_path"] or "")
            if not rel:
                continue
            if rel in done:
                skipped += 1
                continue
            path = year_root / rel.replace("/", os.sep)
            block = _read_frontmatter_head(path)
            from_norm = str(row["title_norm"] or "")
            kept = 0
            for target in _outgoing_from_frontmatter(block):
                clean = target.split("#", 1)[0].strip()
                if _skip_link_target(clean):
                    continue
                to_norm = normalize_text(clean)
                if not to_norm or to_norm == from_norm:
                    continue
                pending.append((from_norm, to_norm, clean))
                kept += 1
                if kept >= MAX_LINKS_PER_PAGE:
                    break
            conn.execute("INSERT OR IGNORE INTO link_progress(rel_path) VALUES (?)", (rel,))
            scanned += 1
            if len(pending) >= 2000:
                conn.executemany(
                    "INSERT OR IGNORE INTO links(from_norm, to_norm, to_title) VALUES (?, ?, ?)",
                    pending,
                )
                inserted += len(pending)
                pending.clear()
                conn.commit()
                if scanned % 20000 == 0:
                    logger.info("links %s: scanned %s pages", y, scanned)
            if limit_pages is not None and scanned >= int(limit_pages):
                break
        if pending:
            conn.executemany(
                "INSERT OR IGNORE INTO links(from_norm, to_norm, to_title) VALUES (?, ?, ?)",
                pending,
            )
            inserted += len(pending)
            conn.commit()
        edges = int(conn.execute("SELECT COUNT(*) FROM links").fetchone()[0] or 0)
    finally:
        conn.close()
    return {
        "ok": True,
        "year": y,
        "index_path": str(out),
        "pages_scanned": scanned,
        "pages_skipped": skipped,
        "edges": edges,
        "edges_inserted": inserted,
    }


def neighbors(
    subject: str,
    year: str = "2026",
    *,
    limit: int = 16,
    index_path: Path | None = None,
    user_question: str = "",
) -> dict[str, Any]:
    """Outbound (and inbound) titles from the link web. Empty if links not built."""
    y = validate_year(year)
    dns = resolve(subject, y, user_question=user_question, index_path=index_path)
    if dns.status != "hit" or dns.hit is None:
        return {
            "ok": False,
            "status": dns.status,
            "query": subject,
            "outbound": [],
            "inbound": [],
            "ranked": [],
            "hops": [],
        }
    path = index_path or default_index_path(y)
    cap = max(1, min(int(limit), 40))
    conn = _connect(path)
    try:
        key = normalize_text(dns.hit.title)
        out_rows = conn.execute(
            "SELECT to_title FROM links WHERE from_norm = ?",
            (key,),
        ).fetchall()
        in_rows = conn.execute(
            "SELECT p.title FROM links l "
            "JOIN pages p ON p.title_norm = l.from_norm "
            "WHERE l.to_norm = ? LIMIT ?",
            (key, INBOUND_FETCH_CAP),
        ).fetchall()
    finally:
        conn.close()
    outbound_raw = [str(r[0]).strip() for r in out_rows if str(r[0]).strip()]
    inbound_raw = [str(r[0]).strip() for r in in_rows if str(r[0]).strip()]
    ranked = rank_related_titles(
        outbound_raw + inbound_raw,
        user_question,
        landing_title=dns.hit.title,
    )
    hops = select_hop_titles(
        ranked,
        user_question,
        landing_title=dns.hit.title,
        limit=2,
    )
    out_keys = {normalize_text(title) for title in outbound_raw}
    outbound = [title for title in ranked if normalize_text(title) in out_keys][:cap]
    inbound = [title for title in ranked if normalize_text(title) not in out_keys][:cap]
    return {
        "ok": True,
        "title": dns.hit.title,
        "year": y,
        "outbound": outbound,
        "inbound": inbound,
        "ranked": ranked[:cap],
        "hops": hops,
    }


def import_redirects(index_path: Path, redirects_path: Path) -> int:
    """Import alias\\tcanonical TSV (or alias,canonical CSV). Titles only."""
    if not redirects_path.is_file():
        logger.info("No redirect dump at %s — skip alias import", redirects_path)
        return 0
    pairs: list[tuple[str, str]] = []
    for line in redirects_path.read_text(encoding="utf-8", errors="replace").splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if "\t" in text:
            left, right = text.split("\t", 1)
        elif "," in text:
            left, right = text.split(",", 1)
        else:
            continue
        pairs.append((left.strip(), right.strip()))
    conn = _connect(index_path)
    try:
        n = upsert_aliases(conn, pairs)
        conn.commit()
        return n
    finally:
        conn.close()


def _parse_rg_title_line(line: str) -> tuple[str, str] | None:
    lower = line.lower()
    idx = lower.find(_MD_TITLE_MARK)
    if idx < 0:
        return None
    path_str = line[: idx + 3]
    rest = line[idx + 4 :]
    match = _TITLE_LINE_RE.match(rest)
    title = _strip_title_value(match.group(1) if match else line[idx + len(_MD_TITLE_MARK) :])
    if not title:
        return None
    return path_str, title


def build_index(
    year: str = "2026",
    *,
    index_path: Path | None = None,
    wiki_root: Path | None = None,
    limit_batches: int | None = None,
    redirects_path: Path | None = None,
    resume: bool = False,
) -> dict[str, Any]:
    y = validate_year(year)
    year_root = (wiki_root or wiki_md_root()) / y
    out = index_path or default_index_path(y)
    if not year_root.is_dir():
        raise FileNotFoundError(f"wiki_md year folder missing: {year_root}")
    rg = _rg_executable()
    if not rg:
        raise RuntimeError("rg (ripgrep) is required to build the title index")

    batches = sorted(year_root.glob("batch_*"))
    if limit_batches is not None:
        batches = batches[: max(0, int(limit_batches))]
    if not batches:
        raise FileNotFoundError(f"no batch_* folders under {year_root}")

    done_batches: set[str] = set()
    if resume and out.exists():
        peek = _connect(out)
        try:
            for row in peek.execute("SELECT DISTINCT rel_path FROM pages"):
                rel = str(row["rel_path"] or "")
                if "/" in rel:
                    done_batches.add(rel.split("/", 1)[0])
                elif "\\" in rel:
                    done_batches.add(rel.split("\\", 1)[0])
        finally:
            peek.close()
    elif out.exists():
        out.unlink()
    conn = _connect(out)
    inserted = int(conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0] or 0)
    try:
        for i, batch_dir in enumerate(batches, start=1):
            if batch_dir.name in done_batches:
                logger.info("title index %s: skip %s (already indexed)", y, batch_dir.name)
                continue
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
                    r"^title:\s*",
                    str(batch_dir),
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            rows: list[tuple[str, str, str, str, str]] = []
            for line in proc.stdout.splitlines():
                parsed = _parse_rg_title_line(line)
                if not parsed:
                    continue
                path_str, title = parsed
                path = Path(path_str)
                rel = _rel_path(path, year_root)
                page_id = path.stem.replace("wiki_", "")
                rows.append((title, str(path), rel, page_id, y))
            inserted += upsert_pages(conn, rows)
            conn.commit()
            if i == 1 or i % 10 == 0 or i == len(batches):
                logger.info("title index %s: batch %s/%s (%s titles)", y, i, len(batches), inserted)
        alias_n = seed_parenthetical_aliases(conn)
        common_n = seed_common_aliases(conn)
        conn.commit()
    finally:
        conn.close()

    redir = redirects_path or default_redirects_path(y)
    try:
        write_common_redirects_tsv(redir)
    except OSError:
        pass
    imported = import_redirects(out, redir)
    return {
        "ok": True,
        "year": y,
        "index_path": str(out),
        "pages": inserted,
        "parenthetical_aliases": alias_n,
        "common_aliases": common_n,
        "redirect_aliases": imported,
        "batches": len(batches),
    }


REMEMBER_MAX_LEAD = 1800
_SLUG_RE = re.compile(r"[^a-z0-9]+")


def remembered_ledger_path(year: str) -> Path:
    return reports_dir(year) / "remembered-titles.jsonl"


def _title_already_remembered(year: str, title_norm: str, dataset: str) -> bool:
    path = remembered_ledger_path(year)
    if not path.is_file():
        return False
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (
                str(row.get("title_norm") or "") == title_norm
                and str(row.get("dataset") or "") == dataset
            ):
                return True
    except OSError:
        return False
    return False


def _append_remembered(year: str, title: str, dataset: str, cache_path: str) -> None:
    path = remembered_ledger_path(year)
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "title": title,
        "title_norm": normalize_text(title),
        "dataset": dataset,
        "cache_path": cache_path,
        "year": year,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def remember_wiki_lead(
    subject: str,
    year: str = "2026",
    *,
    dataset: str = "eve_memory",
    user_question: str = "",
    index_path: Path | None = None,
    promote: bool = True,
) -> dict[str, Any]:
    """Explicit Cognee remember of a Title DNS lead only.

    Never bulk-ingests wiki_md. Lead is capped. Same title+dataset is skipped.
    """
    from pipeline.provenance import provenance_fields, provenance_markdown_footer
    from pipeline.wiki_read_lead import wiki_read_lead
    from pipeline.wiki_scout import allowed_promote_datasets, promote_wiki_cache

    y = validate_year(year)
    chosen = (dataset or "eve_memory").strip() or "eve_memory"
    if chosen not in allowed_promote_datasets():
        return {"ok": False, "error": f"dataset not allowed: {chosen}"}
    dns = resolve(subject, y, user_question=user_question, index_path=index_path)
    if dns.status != "hit" or dns.hit is None:
        return {
            "ok": False,
            "error": dns.reason or "title not in registry",
            "status": dns.status,
            "query": dns.query,
        }
    hit = dns.hit
    title_n = normalize_text(hit.title)
    if _title_already_remembered(y, title_n, chosen):
        return {
            "ok": True,
            "skipped": True,
            "reason": "already remembered",
            "title": hit.title,
            "dataset": chosen,
        }
    lead = wiki_read_lead(hit.title, y, corpus_rel_path=hit.rel_path or None, max_chars=REMEMBER_MAX_LEAD)
    if not lead.get("ok"):
        return {
            "ok": False,
            "error": str(lead.get("error") or "lead missing"),
            "title": hit.title,
        }
    slug = _SLUG_RE.sub("_", title_n).strip("_")[:60] or "wiki"
    cache_dir = Path(
        os.environ.get(
            "EMPIRE_WIKI_CACHE_DIR",
            r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache",
        )
    )
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"dns_{slug}_{y}.md"
    fm = provenance_fields(
        source="title_dns",
        kind="wiki_chunk",
        tool="remember_wiki_lead",
        limb="wiki_local",
        extra={
            "title": hit.title,
            "snapshot": y,
            "rel_path": hit.rel_path,
            "cognee_dataset": chosen,
        },
    )
    body = (
        "---\n"
        + "\n".join(fm)
        + "\n---\n\n"
        + f"# {hit.title}\n\n"
        + str(lead.get("lead") or "").strip()
        + provenance_markdown_footer(source="title_dns", tool="remember_wiki_lead", limb="wiki_local")
    )
    cache_path.write_text(body, encoding="utf-8")
    if not promote:
        _append_remembered(y, hit.title, chosen, str(cache_path))
        return {
            "ok": True,
            "title": hit.title,
            "dataset": chosen,
            "path": str(cache_path),
            "chars": len(body),
            "promoted": False,
        }
    result = promote_wiki_cache(cache_path, dataset=chosen, max_chars=REMEMBER_MAX_LEAD + 2000)
    if not result.get("ok"):
        return {
            "ok": False,
            "error": result.get("error") or "promote failed",
            "title": hit.title,
            "path": str(cache_path),
        }
    _append_remembered(y, hit.title, chosen, str(cache_path))
    return {
        "ok": True,
        "title": hit.title,
        "dataset": chosen,
        "path": str(cache_path),
        "chars": result.get("chars"),
        "note": "Lead only — not the full article. Explicit remember.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build or query the Wikipedia title DNS")
    sub = parser.add_subparsers(dest="cmd", required=True)
    build = sub.add_parser("build", help="Scan wiki_md frontmatter into SQLite")
    build.add_argument("--year", default="2026")
    build.add_argument("--limit-batches", type=int, default=0)
    build.add_argument("--index", default="")
    build.add_argument("--redirects", default="")
    build.add_argument("--resume", action="store_true")
    lookup = sub.add_parser("resolve", help="Look up a subject")
    lookup.add_argument("subject")
    lookup.add_argument("--year", default="2026")
    lookup.add_argument("--question", default="")
    lookup.add_argument("--index", default="")
    aliases = sub.add_parser("import-redirects", help="Load alias\\tcanonical TSV")
    aliases.add_argument("--year", default="2026")
    aliases.add_argument("--redirects", required=True)
    aliases.add_argument("--index", default="")
    common = sub.add_parser(
        "seed-common-aliases",
        help="Seed curated EMPIRE redirect aliases into an existing index",
    )
    common.add_argument("--year", default="2026")
    common.add_argument("--index", default="")
    common.add_argument(
        "--write-tsv",
        action="store_true",
        help="Also refresh redirects.tsv under wiki-reports",
    )
    remember = sub.add_parser("remember", help="Explicit Cognee remember of a DNS lead")
    remember.add_argument("subject")
    remember.add_argument("--year", default="2026")
    remember.add_argument("--dataset", default="eve_memory")
    remember.add_argument("--question", default="")
    remember.add_argument("--index", default="")
    remember.add_argument("--no-promote", action="store_true")
    links = sub.add_parser("links", help="Build title→title link web from frontmatter")
    links.add_argument("--year", default="2026")
    links.add_argument("--index", default="")
    links.add_argument("--no-resume", action="store_true")
    links.add_argument("--limit-pages", type=int, default=0)
    near = sub.add_parser("neighbors", help="List linked titles for a subject")
    near.add_argument("subject")
    near.add_argument("--year", default="2026")
    near.add_argument("--index", default="")
    near.add_argument("--limit", type=int, default=16)
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if args.cmd == "build":
        result = build_index(
            args.year,
            index_path=Path(args.index) if args.index else None,
            limit_batches=args.limit_batches or None,
            redirects_path=Path(args.redirects) if args.redirects else None,
            resume=bool(args.resume),
        )
        print(result)
        return 0
    if args.cmd == "import-redirects":
        y = validate_year(args.year)
        index = Path(args.index) if args.index else default_index_path(y)
        n = import_redirects(index, Path(args.redirects))
        print({"ok": True, "aliases": n, "index_path": str(index)})
        return 0
    if args.cmd == "seed-common-aliases":
        y = validate_year(args.year)
        index = Path(args.index) if args.index else default_index_path(y)
        if getattr(args, "write_tsv", False):
            write_common_redirects_tsv(default_redirects_path(y))
        n = apply_common_aliases(index)
        print({"ok": True, "aliases": n, "index_path": str(index)})
        return 0
    if args.cmd == "remember":
        remembered = remember_wiki_lead(
            args.subject,
            args.year,
            dataset=args.dataset,
            user_question=args.question,
            index_path=Path(args.index) if args.index else None,
            promote=not args.no_promote,
        )
        print(json.dumps(remembered, indent=2, default=str))
        return 0 if remembered.get("ok") else 1
    if args.cmd == "links":
        built = build_links(
            args.year,
            index_path=Path(args.index) if args.index else None,
            resume=not args.no_resume,
            limit_pages=args.limit_pages or None,
        )
        print(json.dumps(built, indent=2, default=str))
        return 0 if built.get("ok") else 1
    if args.cmd == "neighbors":
        near_result = neighbors(
            args.subject,
            args.year,
            limit=args.limit,
            index_path=Path(args.index) if args.index else None,
        )
        print(json.dumps(near_result, indent=2, default=str))
        return 0 if near_result.get("ok") else 1
    result = resolve(
        args.subject,
        args.year,
        user_question=args.question,
        index_path=Path(args.index) if args.index else None,
    )
    print(result.to_dict())
    return 0 if result.status != "miss" else 2


if __name__ == "__main__":
    raise SystemExit(main())
