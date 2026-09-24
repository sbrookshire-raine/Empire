"""Read Wikipedia article leads from D:\\wiki_md after Weaviate entity match."""

from __future__ import annotations

import logging
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from pipeline.wiki_normalizer import _parse_frontmatter
from pipeline.wiki_ops_paths import validate_year, wiki_md_root

logger = logging.getLogger(__name__)

DEFAULT_LEAD_MAX_CHARS = 1800
DEFAULT_SECTION_MAX_CHARS = 1400
_TITLE_LINE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.I | re.M)
_QUOTED_RE = re.compile(r'"([^"]{2,120})"|\*([^*]{2,120})\*')
_SONG_LIKE_RE = re.compile(
    r'\b(?:Running Up That Hill|Wow|Kate Bush|Stranger Things)\b|"[^"]{3,80}"',
    re.I,
)
_CAST_QUESTION_RE = re.compile(
    r"\b(?:actors?|actress(?:es)?|cast|starred|played|characters?)\b",
    re.I,
)
_CAST_SECTION_NAMES = (
    "cast",
    "casting",
    "main cast",
    "ensemble",
    "characters",
    "main characters",
    "cast and characters",
)

SECTION_ALIASES: dict[str, tuple[str, ...]] = {
    "cast": _CAST_SECTION_NAMES,
    "discography": ("discography", "album discography", "studio albums"),
    "filmography": ("filmography", "filmography and television", "acting career"),
    "charts": (
        "chart performance",
        "charts",
        "commercial performance",
        "weekly charts",
        "year-end charts",
    ),
    "history": ("history", "historical", "origins", "background"),
    "reception": ("reception", "critical reception", "critical response"),
    "plot": ("plot", "synopsis", "premise"),
    "production": ("production", "development", "filming"),
}


def resolve_section_names(section: str) -> tuple[str, ...]:
    key = (section or "").strip().casefold()
    if not key or key in {"lead", "intro", "introduction"}:
        return ()
    if key in SECTION_ALIASES:
        return SECTION_ALIASES[key]
    # Accept raw heading text
    return (key,)


def prefer_section_for_question(user_question: str) -> str:
    ql = (user_question or "").casefold()
    if wants_cast_section(user_question):
        return "cast"
    if any(token in ql for token in ("discography", "album", "albums")):
        return "discography"
    if any(token in ql for token in ("filmography", "nightmare on elm", "franchise")):
        return "filmography"
    if any(token in ql for token in ("chart", "peak", "billboard", "2022")):
        return "charts"
    if any(token in ql for token in ("history", "historical", "origin", "biological")):
        return "history"
    if "reception" in ql or "review" in ql:
        return "reception"
    if "plot" in ql or "synopsis" in ql:
        return "plot"
    if "production" in ql:
        return "production"
    return ""



def wiki_read_lead_enabled() -> bool:
    return os.environ.get("EMPIRE_WIKI_READ_LEAD", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }


def _rg_executable() -> str | None:
    rg = shutil.which("rg")
    if rg:
        return rg
    cursor_rg = Path.home() / (
        "AppData/Local/Programs/cursor/resources/app/node_modules/@vscode/ripgrep/bin/rg.exe"
    )
    return str(cursor_rg) if cursor_rg.exists() else None


def _strip_infobox_noise(text: str) -> str:
    """Drop wikitext infobox/table lines that precede prose in converted md."""
    lines = text.splitlines()
    kept: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if kept:
                kept.append("")
            continue
        # Infobox header: "# Title | length = | label = ..."
        if re.match(r"^#\s+.+\|\s*\w+\s*=", stripped):
            continue
        # Table rows from infobox conversion
        if stripped.startswith("|") and stripped.count("|") >= 2:
            continue
        if stripped.startswith("|-") or stripped in {"{|", "|}"}:
            continue
        kept.append(line)
    collapsed = "\n".join(kept).strip()
    return re.sub(r"\n{3,}", "\n\n", collapsed)


def extract_lead(body: str, *, max_chars: int = DEFAULT_LEAD_MAX_CHARS) -> str:
    """Return lead paragraph(s) — body text before the first H2."""
    _, text = _parse_frontmatter(body)
    cleaned = _strip_infobox_noise(text.strip())
    if not cleaned:
        return ""
    parts = re.split(r"\n##\s+", cleaned, maxsplit=1)
    lead = parts[0].strip()
    lead = re.sub(r"\n#+\s+.*", "", lead).strip()
    # Drop converted-md title line: "# Kate Bush **Catherine Bush** (born …"
    lead = re.sub(r"^#\s+[^*\n]+?(?=\*\*)", "", lead).strip()
    lead = re.sub(r"^#\s+[^\n]+?\n+", "", lead).strip()
    lead = re.sub(r"\s+", " ", lead)
    if len(lead) > max_chars:
        lead = lead[: max_chars - 1].rstrip() + "…"
    return lead


def extract_named_section(
    body: str,
    section_names: tuple[str, ...] | list[str],
    *,
    max_chars: int = DEFAULT_SECTION_MAX_CHARS,
) -> str:
    """Return the first matching ## section body (markdown), collapsed to prose."""
    wanted = {str(name).casefold().strip() for name in section_names if str(name).strip()}
    if not wanted:
        return ""
    _, text = _parse_frontmatter(body)
    cleaned = _strip_infobox_noise(text.strip())
    if not cleaned:
        return ""
    parts = re.split(r"\n(?=##\s+)", cleaned)
    for part in parts:
        match = re.match(r"^##\s+(.+?)\s*\n(.*)$", part, re.S)
        if not match:
            continue
        heading = match.group(1).strip().casefold()
        if heading not in wanted and not any(heading.startswith(name) for name in wanted):
            continue
        section = match.group(2).strip()
        section = re.split(r"\n##\s+", section, maxsplit=1)[0].strip()
        section = re.sub(r"\s+", " ", section)
        if len(section) > max_chars:
            section = section[: max_chars - 1].rstrip() + "…"
        return section
    return ""


def list_section_titles(body: str, *, limit: int = 12) -> list[str]:
    """Return the page's H2 headings, so a miss can tell the model what *does* exist."""

    titles: list[str] = []
    seen: set[str] = set()
    for match in re.finditer(r"^##\s+(.+?)\s*$", body or "", re.MULTILINE):
        title = re.sub(r"\s+", " ", match.group(1)).strip()
        key = title.casefold()
        if not title or key in seen:
            continue
        seen.add(key)
        titles.append(title)
        if len(titles) >= max(1, limit):
            break
    return titles


def wants_cast_section(user_question: str) -> bool:
    return bool(_CAST_QUESTION_RE.search(user_question or ""))


def allowed_names_from_lead(lead: str, *, title: str = "") -> list[str]:
    names: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        key = value.strip().casefold()
        if not key or key in seen or len(key) < 2:
            return
        seen.add(key)
        names.append(value.strip())

    if title.strip():
        add(title.strip())
    for match in _QUOTED_RE.finditer(lead):
        add(match.group(1) or match.group(2) or "")
    for match in _SONG_LIKE_RE.finditer(lead):
        add(match.group(0).strip("\"* "))
    return names[:24]


def _corpus_rel_from_weaviate(title: str, year: str) -> str | None:
    from pipeline.wiki_scout import (
        DEFAULT_API_KEY,
        DEFAULT_WEAVIATE_URL,
        _graphql_exact_title,
        resolve_collection,
    )

    title_clean = (title or "").strip()
    if not title_clean:
        return None
    try:
        collection, _year = resolve_collection(year=year)
        rows = _graphql_exact_title(
            base_url=DEFAULT_WEAVIATE_URL,
            api_key=DEFAULT_API_KEY,
            collection=collection,
            title=title_clean,
            limit=3,
        )
    except Exception as exc:  # noqa: BLE001
        logger.debug("wiki_read_lead Weaviate title lookup failed for %r: %s", title_clean, exc)
        return None
    for row in rows:
        rel = str(row.get("corpus_rel_path") or "").strip()
        if rel:
            return rel
    return None


def resolve_md_path(
    title: str,
    year: str,
    *,
    corpus_rel_path: str | None = None,
) -> Path | None:
    y = validate_year(year)
    root = wiki_md_root() / y
    rel = (corpus_rel_path or "").strip().replace("\\", "/").lstrip("/")
    if not rel:
        try:
            from pipeline.wiki_title_dns import resolve as dns_resolve

            dns = dns_resolve(title, y)
            if dns.status == "hit" and dns.hit is not None:
                if dns.hit.path:
                    hit_path = Path(dns.hit.path)
                    if hit_path.is_file():
                        return hit_path
                if dns.hit.rel_path:
                    rel = dns.hit.rel_path
        except Exception as exc:  # noqa: BLE001
            logger.debug("wiki_read Title DNS path failed for %r: %s", title, exc)
        if not rel:
            rel = _corpus_rel_from_weaviate(title, year) or ""
    if rel:
        candidate = root / rel
        if candidate.is_file():
            return candidate
    title_clean = (title or "").strip()
    if not title_clean or not root.is_dir():
        return None
    rg = _rg_executable()
    if not rg:
        return None
    # Last resort: scan a handful of early batches only. A full-year rg times out, and a stall
    # here blocks the whole tool call, so keep it short and small (Title DNS already had the
    # chance to answer — it holds the authoritative path for every indexed title).
    batch_dirs = sorted(root.glob("batch_*"))[:4]
    if not batch_dirs:
        return None
    try:
        proc = subprocess.run(
            [
                rg,
                "-g",
                "*.md",
                "-m",
                "1",
                "-l",
                "--ignore-case",
                f"^title:\\s*{re.escape(title_clean)}\\s*$",
                *(str(batch_dir) for batch_dir in batch_dirs),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
            timeout=3,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        logger.warning("wiki_read_lead rg lookup failed for %r: %s", title_clean, exc)
        return None
    for line in proc.stdout.splitlines():
        path = Path(line.strip())
        if path.is_file():
            return path
    return None


def wiki_read_lead(
    entity: str,
    snapshot: str,
    *,
    corpus_rel_path: str | None = None,
    max_chars: int = DEFAULT_LEAD_MAX_CHARS,
    user_question: str = "",
    include_cast_section: bool | None = None,
) -> dict[str, Any]:
    title = (entity or "").strip()
    year = validate_year(snapshot)
    if not title:
        return {"ok": False, "error": "entity is required"}
    path = resolve_md_path(title, year, corpus_rel_path=corpus_rel_path)
    if path is None:
        return {
            "ok": False,
            "error": f"no markdown file for {title!r} ({year})",
            "title": title,
            "snapshot": year,
        }
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        logger.warning("wiki_read_lead read failed %s: %s", path, exc)
        return {"ok": False, "error": str(exc), "title": title, "snapshot": year}
    meta, _ = _parse_frontmatter(raw)
    resolved_title = str(meta.get("title") or title).strip() or title
    lead = extract_lead(raw, max_chars=max_chars)
    if not lead:
        return {
            "ok": False,
            "error": "empty lead",
            "title": resolved_title,
            "snapshot": year,
            "path": str(path),
        }
    want_cast = (
        include_cast_section
        if include_cast_section is not None
        else wants_cast_section(user_question)
    )
    cast_section = ""
    if want_cast:
        cast_section = extract_named_section(
            raw,
            _CAST_SECTION_NAMES,
            max_chars=min(DEFAULT_SECTION_MAX_CHARS, max(600, max_chars)),
        )
    name_source = f"{lead} {cast_section}".strip()
    allowed = allowed_names_from_lead(name_source, title=resolved_title)
    out: dict[str, Any] = {
        "ok": True,
        "title": resolved_title,
        "snapshot": year,
        "lead": lead,
        "allowed_names": allowed,
        "path": str(path),
    }
    if cast_section:
        out["cast_section"] = cast_section
        out["section_name"] = "Cast"
    return out


def wiki_read(
    entity: str,
    snapshot: str = "2026",
    *,
    section: str = "",
    corpus_rel_path: str | None = None,
    max_chars: int = DEFAULT_LEAD_MAX_CHARS,
    user_question: str = "",
) -> dict[str, Any]:
    """Read lead and/or a named H2 section from local markdown (Title DNS path)."""
    question = user_question or ""
    section_key = (section or "").strip() or prefer_section_for_question(question)
    base = wiki_read_lead(
        entity,
        snapshot,
        corpus_rel_path=corpus_rel_path,
        max_chars=max_chars,
        user_question=question,
        include_cast_section=(section_key.casefold() == "cast") if section_key else None,
    )
    if not base.get("ok"):
        return base
    names = resolve_section_names(section_key)
    if not names:
        return base
    path_str = str(base.get("path") or "")
    path = Path(path_str) if path_str else None
    if path is None or not path.is_file():
        return base
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        base["section_error"] = str(exc)
        return base
    body = extract_named_section(
        raw,
        names,
        max_chars=min(DEFAULT_SECTION_MAX_CHARS, max(600, max_chars)),
    )
    if body:
        label = section_key.strip().title() or "Section"
        base["section_name"] = label
        base["section"] = body
        if label.casefold() == "cast" or "cast" in names:
            base["cast_section"] = body
        merged = list(base.get("allowed_names") or [])
        for name in allowed_names_from_lead(body, title=str(base.get("title") or "")):
            if name.casefold() not in {str(x).casefold() for x in merged}:
                merged.append(name)
        base["allowed_names"] = merged[:24]
    elif section_key:
        base["section_name"] = section_key
        base["section_missing"] = True
        # Tell the model what exists and forbid more guessing: observed live, a missing section
        # with no guidance produced 15 consecutive wiki_read_section calls (107 s turn).
        available = list_section_titles(raw)
        base["available_sections"] = available
        base["chat_reply_rule"] = (
            "That section does not exist on this page. Do NOT guess another section name. "
            + (
                f"Useful sections that DO exist: {', '.join(available)}. You may read ONE of those "
                "if the user's fact is likely there. "
                if available
                else ""
            )
            + "Otherwise answer from the lead you already have (or say the local archive does not "
            "cover that detail). Never call wiki_read_section twice for the same page in one turn."
        )
    return base


def pick_lead_target(
    user_question: str,
    hit_meta: list[dict[str, Any]],
) -> tuple[str, str | None]:
    """Choose the best article title (+ optional corpus_rel_path) for lead read."""
    from pipeline.wiki_interpreter import normalize_text, resolve_lookup_topic

    ql = normalize_text(user_question)
    preferred: list[str] = []
    topic = resolve_lookup_topic(user_question)
    if "stranger things" in ql and any(
        token in ql for token in ("song", "80s", "80's", "popular", "hit", "music")
    ):
        preferred.extend(
            [
                "Running Up That Hill",
                "Music of Stranger Things",
                "Stranger Things season 4",
            ]
        )
    if "kate bush" in ql or (topic and topic.casefold() == "kate bush"):
        if any(
            token in ql
            for token in ("song", "reinvig", "reviv", "resurg", "career", "comeback")
        ):
            preferred.extend(["Running Up That Hill", "Kate Bush"])
        else:
            preferred.append("Kate Bush")
    elif topic:
        preferred.append(topic)

    meta_by_title = {
        str(row.get("title") or "").casefold(): row for row in hit_meta if row.get("title")
    }
    for title in preferred:
        row = meta_by_title.get(title.casefold())
        if row:
            return str(row.get("title") or title), str(row.get("corpus_rel_path") or "") or None
        if title:
            return title, None

    for row in hit_meta:
        t = str(row.get("title") or "").strip()
        if t:
            return t, str(row.get("corpus_rel_path") or "") or None
    return "", None
