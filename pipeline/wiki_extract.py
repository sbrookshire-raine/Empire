"""Deterministic Wikipedia markdown → Evidence JSON (fields / tables / lists).

No topic-specific handlers. Does not invent facts from prose. Does not call Cognee.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
from pathlib import Path
from typing import Any

from pipeline.wiki_normalizer import _parse_frontmatter
from pipeline.wiki_ops_paths import validate_year

logger = logging.getLogger(__name__)

SCHEMA_VERSION = "EvidenceJSON/v1"
EXTRACT_MARKER = "[[EMPIRE_WIKI_EXTRACT]]"

_WIKITABLE_RE = re.compile(r"\{\|(.*?)\|\}", re.S)
_INFOBOX_RE = re.compile(r"\{\{[Ii]nfobox\b([^|]*)\|(.*?)\}\}", re.S)
_PIPE_KV_RE = re.compile(
    r"^\|\s*([A-Za-z0-9][A-Za-z0-9_\s/-]{0,80}?)\s*=\s*(.*?)\s*$",
    re.M,
)
_MD_PIPE_ROW_RE = re.compile(r"^\|(.+)\|$", re.M)
_MD_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.M)
_MD_LIST_RE = re.compile(r"^[\*\-]\s+(.+)$", re.M)
_CELL_CLEAN_RE = re.compile(
    r"(?:"
    r"\[\[[^\|\]]*\|([^\]]+)\]\]|"  # [[target|label]]
    r"\[\[([^\]]+)\]\]|"  # [[target]]
    r"'{2,3}|"  # bold/italic
    r"<[^>]+>|"  # html
    r"\{\{[^}]*\}\}"  # nested templates (drop)
    r")"
)
_ATTR_PREFIX_RE = re.compile(
    r"^(?:scope|rowspan|colspan|style|class|id|align|width|height|bgcolor)"
    r"\s*=\s*\"[^\"]*\"\s*\|?\s*",
    re.I,
)
_ATTR_PREFIX_UNQUOTED_RE = re.compile(
    r"^(?:scope|rowspan|colspan|style|class|id|align|width|height|bgcolor)"
    r"\s*=\s*[^\|]*\|?\s*",
    re.I,
)
_EXTRACT_ASK_RE = re.compile(
    r"\b(?:"
    r"population|release\s+date|released|when\s+was|how\s+many|"
    r"specifications?|specs?\b|table\b|list\s+of|list\s+items?|infobox|"
    r"founded|headquarters|capital\s+of|area\s+of|gdp|"
    r"number\s+of|episodes?|runtime|publisher|developer|"
    r"extract|fields?\b|rows?\b|ratings?\b|paradigm\b|pull\b"
    r")\b",
    re.I,
)


def is_extract_shaped_question(text: str) -> bool:
    return bool(_EXTRACT_ASK_RE.search(text or ""))


def _clean_cell(raw: str) -> str:
    text = (raw or "").strip()
    if not text:
        return ""
    # Drop footnote/template residue early so values don't bleed into prose.
    text = re.split(r"\{\{", text, maxsplit=1)[0].strip()
    for _ in range(4):
        nxt = _ATTR_PREFIX_RE.sub("", text)
        nxt = _ATTR_PREFIX_UNQUOTED_RE.sub("", nxt)
        if nxt == text:
            break
        text = nxt.strip()
    text = text.lstrip("|").strip()
    prev = None
    while prev != text:
        prev = text
        text = _CELL_CLEAN_RE.sub(
            lambda m: (m.group(1) or m.group(2) or ""),
            text,
        )
    text = re.sub(r"\s+", " ", text).strip()
    # Truncate if conversion glued following prose onto a cell.
    if ". " in text and len(text) > 120:
        text = text.split(". ", 1)[0].strip()
    return text


def _strip_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    meta, body = _parse_frontmatter(text)
    return (meta if isinstance(meta, dict) else {}), body


def _cell_parts(line: str, *, bang: bool) -> list[tuple[str, str]]:
    """Split a ! or | table line into (raw_segment, cleaned_text) cells."""
    stripped = line.strip()
    if bang:
        body = stripped.lstrip("!").strip()
        parts = re.split(r"\s*!!\s*", body)
    else:
        body = stripped[1:] if stripped.startswith("|") else stripped
        parts = body.split("||") if "||" in body else [body]
    out: list[tuple[str, str]] = []
    for part in parts:
        raw = part
        cell = part
        if "|" in cell and not cell.strip().startswith("[["):
            left, right = cell.split("|", 1)
            if re.search(r"\b(?:style|class|rowspan|colspan|align|scope|width|height|bgcolor)\b", left, re.I):
                cell = right
        out.append((raw, _clean_cell(cell)))
    return out


def _parse_wikitable_block(block: str) -> dict[str, Any] | None:
    """Parse one {| … |} body into caption/headers/rows.

    Columnar tables (scope=col / multi-column ratings) keep real headers.
    Nested tech KV tables (scope=row / rowgroup) become Property/Value.
    """
    caption = ""
    col_headers: list[str] = []
    matrix_rows: list[list[str]] = []
    kv_rows: list[list[str]] = []
    warnings: list[str] = []
    current: list[str] = []
    mode = "headers"  # headers | data
    saw_col_scope = False
    saw_row_scope = False

    def flush_row() -> None:
        nonlocal current
        cells = [c for c in current]
        current = []
        if not any(str(c).strip() for c in cells):
            return
        matrix_rows.append(cells)
        if len(cells) == 2:
            kv_rows.append([cells[0], cells[1]])
        elif len(cells) >= 3:
            # First cell often a row label in tech tables; keep matrix as-is.
            pass
        elif len(cells) == 1 and cells[0]:
            kv_rows.append([cells[0], ""])

    for raw_line in block.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("|+"):
            caption = _clean_cell(stripped[2:])
            continue
        if stripped == "|-" or stripped.startswith("|-"):
            flush_row()
            if col_headers:
                mode = "data"
            continue
        if stripped.startswith("!"):
            for raw, cleaned in _cell_parts(stripped, bang=True):
                low = raw.casefold()
                if "rowspan" in low or "colspan" in low:
                    warnings.append("rowspan_or_colspan_present")
                is_row = "scope=\"row" in low or "scope=row" in low or "scope=\"rowgroup" in low
                is_col = "scope=\"col" in low or "scope=col" in low
                if is_row:
                    saw_row_scope = True
                if is_col:
                    saw_col_scope = True
                if not cleaned:
                    continue
                # Column headers: scope=col, or bang cells before any data when not row-scoped.
                if is_col or (mode == "headers" and not is_row and not saw_row_scope):
                    col_headers.append(cleaned)
                    continue
                mode = "data"
                current.append(cleaned)
            continue
        if stripped.startswith("|"):
            mode = "data"
            for raw, cleaned in _cell_parts(stripped, bang=False):
                low = raw.casefold()
                if "rowspan" in low or "colspan" in low:
                    warnings.append("rowspan_or_colspan_present")
                current.append(cleaned)
            continue
    flush_row()

    max_width = max((len(r) for r in matrix_rows), default=0)
    # Row-scoped tech tables (Switch specs) stay Property/Value even if some rows are wide.
    if saw_row_scope and not saw_col_scope:
        columnar = False
    else:
        columnar = (
            saw_col_scope
            or len(col_headers) >= 3
            or max_width >= 4
            or (len(col_headers) >= 2 and not saw_row_scope)
        )
    if columnar and (matrix_rows or col_headers):
        headers = col_headers[:]
        if not headers and max_width:
            headers = [f"Col {i + 1}" for i in range(max_width)]
        width = len(headers) if headers else max_width
        usable_rows: list[list[str]] = []
        for row in matrix_rows:
            # Skip header-echo rows that only repeat header labels
            if headers and [c.casefold() for c in row[: len(headers)]] == [h.casefold() for h in headers]:
                continue
            padded = list(row[:width]) + [""] * max(0, width - len(row))
            if any(str(c).strip() for c in padded):
                usable_rows.append(padded)
        usable_rows = usable_rows[:40]
        if not usable_rows and not headers:
            return None
        return {
            "caption": caption,
            "headers": headers,
            "rows": usable_rows,
            "warnings": sorted(set(warnings)),
        }

    # Tech / infobox-style KV presentation — fold multi-label rows into Property/Value.
    usable_kv: list[list[str]] = []
    seen: set[tuple[str, str]] = set()
    for row in matrix_rows:
        if not any(str(c).strip() for c in row):
            continue
        if len(row) == 1:
            pair = (row[0], "")
        elif len(row) == 2:
            pair = (row[0], row[1])
        else:
            pair = (" / ".join(x for x in row[:-1] if x), row[-1])
        if pair in seen:
            continue
        seen.add(pair)
        usable_kv.append([pair[0], pair[1]])
    if usable_kv:
        return {
            "caption": caption,
            "headers": ["Property", "Value"],
            "rows": usable_kv[:40],
            "warnings": sorted(set(warnings)),
        }
    if col_headers:
        return {
            "caption": caption,
            "headers": col_headers,
            "rows": [],
            "warnings": sorted(set(warnings)),
        }
    return None


def extract_wikitables(body: str) -> list[dict[str, Any]]:
    tables: list[dict[str, Any]] = []
    for match in _WIKITABLE_RE.finditer(body):
        parsed = _parse_wikitable_block(match.group(1))
        if parsed:
            tables.append(parsed)
    return tables[:12]


def extract_infobox_fields(body: str) -> list[dict[str, str]]:
    fields: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(key: str, value: str) -> None:
        k = _clean_cell(key)
        v = _clean_cell(value)
        if not k or not v:
            return
        key_cf = k.casefold().replace(" ", "_")
        if key_cf in {
            "name",
            "image",
            "image_size",
            "image_upright",
            "alt",
            "caption",
            "logo",
            "logo_size",
            "logo_alt",
            "logo_upright",
        } or key_cf.startswith(("image", "logo", "map_", "flag")):
            return
        if len(v) > 160:
            v = v[:159].rstrip() + "…"
        # Skip broken key=value residue where value is another key=
        if re.match(r"^[A-Za-z0-9_]+\s*=\s*$", v) or v.endswith("="):
            return
        if key_cf in seen:
            return
        seen.add(key_cf)
        fields.append({"key": k, "value": v, "raw_key": key.strip(), "raw_value": value.strip()})

    for match in _INFOBOX_RE.finditer(body):
        inner = match.group(2) or ""
        for km in _PIPE_KV_RE.finditer("|" + inner.replace("\n|", "\n|")):
            add(km.group(1), km.group(2))

    # Standalone pipe KV near top of article (stripped infobox residue)
    head = body[:3500]
    for km in _PIPE_KV_RE.finditer(head):
        add(km.group(1), km.group(2))

    return fields[:80]


def extract_md_lists(body: str) -> list[dict[str, Any]]:
    lists: list[dict[str, Any]] = []
    section = "lead"
    items: list[str] = []

    def flush() -> None:
        nonlocal items
        if items:
            lists.append({"section": section, "items": items[:40]})
        items = []

    for line in body.splitlines():
        hm = _MD_HEADING_RE.match(line)
        if hm:
            flush()
            section = hm.group(2).strip()
            continue
        lm = _MD_LIST_RE.match(line)
        if lm:
            item = _clean_cell(lm.group(1))
            if item:
                items.append(item)
            continue
        if items and line.strip() == "":
            flush()
    flush()
    return lists[:20]


def extract_md_pipe_tables(body: str) -> list[dict[str, Any]]:
    """GitHub-style | a | b | tables (rare in this corpus)."""
    tables: list[dict[str, Any]] = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not (line.startswith("|") and line.endswith("|") and line.count("|") >= 3):
            i += 1
            continue
        rows_raw = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if nxt.startswith("|") and nxt.endswith("|"):
                rows_raw.append(nxt)
                i += 1
                continue
            break
        parsed_rows: list[list[str]] = []
        for raw in rows_raw:
            if re.match(r"^\|[\s\-:|]+\|$", raw):
                continue
            cells = [_clean_cell(c) for c in raw.strip("|").split("|")]
            if any(cells):
                parsed_rows.append(cells)
        if len(parsed_rows) >= 2:
            tables.append(
                {
                    "caption": "",
                    "headers": parsed_rows[0],
                    "rows": parsed_rows[1:40],
                    "warnings": ["markdown_pipe_table"],
                }
            )
    return tables[:5]


def _source_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:24]


def _filter_by_need(
    fields: list[dict[str, str]],
    tables: list[dict[str, Any]],
    lists: list[dict[str, Any]],
    need_hint: str,
) -> tuple[list[dict[str, str]], list[dict[str, Any]], list[dict[str, Any]]]:
    hint = (need_hint or "").strip().casefold()
    if not hint:
        return fields, tables, lists
    tokens = [t for t in re.split(r"[^a-z0-9]+", hint) if len(t) >= 3]
    if not tokens:
        return fields, tables, lists

    def score_text(text: str) -> int:
        cf = text.casefold()
        return sum(1 for t in tokens if t in cf)

    table_scoped = any(
        t in hint
        for t in ("table", "spec", "specs", "rating", "ratings", "rows", "wikitable")
    )
    # Word-boundary list cues — do not match "listed" inside field asks.
    list_scoped = (
        bool(
            re.search(
                r"\b(?:lists?|see also|bullets?|items under|section on)\b",
                hint,
            )
        )
        and not table_scoped
    )
    field_scoped = (
        bool(re.search(r"\b(?:fields?|paradigm|infobox)\b", hint))
        and not table_scoped
        and not list_scoped
    )
    # "infobox fields" / "paradigm field" are field-only; bare "infobox" without table still fields.
    if re.search(r"\binfobox\b", hint) and "table" not in hint and "spec" not in hint:
        field_scoped = True
        list_scoped = False
        table_scoped = False

    ranked_fields = sorted(
        fields,
        key=lambda f: score_text(f"{f.get('key', '')} {f.get('value', '')}"),
        reverse=True,
    )
    scored_fields = [
        f for f in ranked_fields if score_text(f"{f.get('key', '')} {f.get('value', '')}") > 0
    ]

    ranked_tables: list[tuple[int, dict[str, Any]]] = []
    for table in tables:
        blob = " ".join(table.get("headers") or [])
        blob += " " + " ".join(c for row in (table.get("rows") or [])[:5] for c in row)
        blob += " " + str(table.get("caption") or "")
        ranked_tables.append((score_text(blob), table))
    ranked_tables.sort(key=lambda x: x[0], reverse=True)

    ranked_lists: list[tuple[int, dict[str, Any]]] = []
    for lst in lists:
        blob = str(lst.get("section") or "") + " " + " ".join(lst.get("items") or [])
        ranked_lists.append((score_text(blob), lst))
    ranked_lists.sort(key=lambda x: x[0], reverse=True)

    if field_scoped:
        keep_fields = scored_fields[:12] if scored_fields else ranked_fields[:8]
        return keep_fields, [], []

    if list_scoped:
        keep_lists = [lst for s, lst in ranked_lists if s > 0] or [
            lst for _, lst in ranked_lists[:2]
        ]
        keep_lists = keep_lists[:6]
        return [], [], keep_lists

    if table_scoped:
        keep_tables = [t for s, t in ranked_tables if s > 0] or [t for _, t in ranked_tables[:1]]
        keep_tables = keep_tables[:1]
        # Specs tables stand alone — do not attach infobox fields/lists.
        return [], keep_tables, []

    keep_fields = scored_fields[:20] if scored_fields else ranked_fields[:12]
    keep_tables = [t for s, t in ranked_tables if s > 0] or [t for _, t in ranked_tables[:3]]
    keep_tables = keep_tables[:5]
    keep_lists = [lst for s, lst in ranked_lists if s > 0] or [lst for _, lst in ranked_lists[:3]]
    keep_lists = keep_lists[:8]
    return keep_fields, keep_tables, keep_lists


def extract_from_markdown(
    text: str,
    *,
    title: str = "",
    year: str = "2026",
    need_hint: str = "",
    section: str = "",
    path: str = "",
) -> dict[str, Any]:
    """Build Evidence JSON v1 from article markdown bytes."""
    y = validate_year(year)
    meta, body = _strip_frontmatter(text or "")
    page_title = title or str(meta.get("title") or "").strip() or "Untitled"
    src_hash = _source_hash(text or "")

    if section.strip():
        # Narrow body to named H2 when requested
        from pipeline.wiki_read_lead import resolve_section_names

        names = resolve_section_names(section)
        if names:
            narrowed = _slice_section(body, names)
            if narrowed.strip():
                body = narrowed
            else:
                return {
                    "ok": False,
                    "state": "empty",
                    "schema_version": SCHEMA_VERSION,
                    "extract_id": f"ex_{src_hash}",
                    "canonical_title": page_title,
                    "year": y,
                    "source_hash": src_hash,
                    "path": path,
                    "fields": [],
                    "tables": [],
                    "lists": [],
                    "provenance": {
                        "title": page_title,
                        "year": y,
                        "section": section,
                        "source_hash": src_hash,
                        "path": path,
                    },
                    "warnings": ["section_not_found"],
                    "refusal_reason": f"Section {section!r} not found or empty.",
                }

    fields = extract_infobox_fields(body)
    tables = extract_wikitables(body) + extract_md_pipe_tables(body)
    lists = extract_md_lists(body)
    fields, tables, lists = _filter_by_need(fields, tables, lists, need_hint)

    warnings: list[str] = []
    for table in tables:
        warnings.extend(table.get("warnings") or [])

    has_structure = bool(fields or tables or lists)
    if not has_structure:
        state = "empty"
        refusal = "No structured fields, tables, or lists could be parsed from this page."
    else:
        state = "ok"
        refusal = None

    extract_id = f"ex_{hashlib.sha256(f'{page_title}|{y}|{src_hash}'.encode()).hexdigest()[:20]}"
    return {
        "ok": state == "ok",
        "state": state,
        "schema_version": SCHEMA_VERSION,
        "extract_id": extract_id,
        "canonical_title": page_title,
        "year": y,
        "source_hash": src_hash,
        "path": path,
        "fields": fields,
        "tables": tables,
        "lists": lists,
        "provenance": {
            "title": page_title,
            "year": y,
            "section": section or "",
            "source_hash": src_hash,
            "path": path,
        },
        "warnings": sorted(set(warnings))[:20],
        "refusal_reason": refusal,
    }


def _slice_section(body: str, names: tuple[str, ...]) -> str:
    want = {n.casefold() for n in names}
    lines = body.splitlines()
    start = None
    for idx, line in enumerate(lines):
        m = _MD_HEADING_RE.match(line)
        if not m:
            continue
        heading = m.group(2).strip().casefold()
        if heading in want or any(heading.startswith(n) for n in want):
            start = idx + 1
            level = len(m.group(1))
            end = len(lines)
            for j in range(start, len(lines)):
                m2 = _MD_HEADING_RE.match(lines[j])
                if m2 and len(m2.group(1)) <= level:
                    end = j
                    break
            return "\n".join(lines[start:end])
    return ""


def format_extract_prose(evidence: dict[str, Any], *, max_chars: int = 2200) -> str:
    """Short human-readable EXTRACT block for injection (not raw markup)."""
    lines: list[str] = []
    title = evidence.get("canonical_title") or evidence.get("title") or ""
    lines.append(f"Title: {title}")
    lines.append(f"State: {evidence.get('state')}")
    fields = evidence.get("fields") or []
    if fields:
        lines.append("Fields:")
        for field in fields[:25]:
            lines.append(f"- {field.get('key')}: {field.get('value')}")
    tables = evidence.get("tables") or []
    for ti, table in enumerate(tables[:3], start=1):
        cap = table.get("caption") or f"Table {ti}"
        headers = table.get("headers") or []
        lines.append(f"Table ({cap}):")
        if headers:
            lines.append("| " + " | ".join(headers) + " |")
        for row in (table.get("rows") or [])[:12]:
            lines.append("| " + " | ".join(row) + " |")
    lists = evidence.get("lists") or []
    for lst in lists[:4]:
        sec = lst.get("section") or "list"
        items = lst.get("items") or []
        if not items:
            continue
        lines.append(f"List ({sec}):")
        for item in items[:15]:
            lines.append(f"- {item}")
    if evidence.get("refusal_reason"):
        lines.append(f"Refusal: {evidence['refusal_reason']}")
    text = "\n".join(lines)
    if len(text) > max_chars:
        return text[: max_chars - 1].rstrip() + "…"
    return text


def format_extract_injection(evidence: dict[str, Any], *, user_question: str) -> str:
    prose = format_extract_prose(evidence)
    state = str(evidence.get("state") or "error")
    question = (user_question or "").strip()
    # Lead with User message so Eve/companion parsers and the model see the ask first.
    lines = [
        f"User message:\n{question}",
        "",
        EXTRACT_MARKER,
        f"EXTRACT (mandatory — schema {evidence.get('schema_version')} — snapshot {evidence.get('year')}):",
        prose,
        f"extract_id: {evidence.get('extract_id')}",
        f"source_hash: {evidence.get('source_hash')}",
        "",
    ]
    if state == "ok":
        lines.extend(
            [
                "CRITICAL: Your entire reply must be the EXTRACT table/fields above in plain Markdown.",
                "Do not discuss tools, locks, remembering, scratchpads, or errors.",
                "Do not say you will proceed later — output the table now.",
                "CONTRACT: Answer the User message using ONLY EXTRACT fields/tables/lists above.",
                "Present the table clearly. Do not invent values missing from EXTRACT.",
                "Do NOT call any tools.",
            ]
        )
    else:
        lines.extend(
            [
                "CONTRACT: EXTRACT is not usable (empty/unsupported/error).",
                "Refuse clearly. Do NOT invent facts. Do NOT fall back to training memory.",
                "Do NOT call wiki tools for a parametric fill.",
            ]
        )
    return "\n".join(lines)


def wiki_extract(
    subject: str,
    year: str = "2026",
    *,
    need_hint: str = "",
    section: str = "",
    user_question: str = "",
    index_path: Path | None = None,
) -> dict[str, Any]:
    """Title DNS resolve → read markdown → Evidence JSON."""
    from pipeline.wiki_title_dns import resolve as dns_resolve

    y = validate_year(year)
    query = (subject or "").strip()
    if not query:
        return {
            "ok": False,
            "state": "error",
            "schema_version": SCHEMA_VERSION,
            "refusal_reason": "empty subject",
            "fields": [],
            "tables": [],
            "lists": [],
        }
    dns = dns_resolve(query, y, user_question=user_question or need_hint, index_path=index_path)
    if dns.status == "ambiguous":
        return {
            "ok": False,
            "state": "ambiguous",
            "schema_version": SCHEMA_VERSION,
            "query": query,
            "year": y,
            "candidates": [c.title for c in dns.candidates],
            "refusal_reason": "Ambiguous title — ask which page to open.",
            "fields": [],
            "tables": [],
            "lists": [],
        }
    if dns.status != "hit" or dns.hit is None:
        return {
            "ok": False,
            "state": "empty",
            "schema_version": SCHEMA_VERSION,
            "query": query,
            "year": y,
            "refusal_reason": dns.reason or "not in title registry",
            "fields": [],
            "tables": [],
            "lists": [],
        }
    path = Path(dns.hit.path)
    if not path.is_file():
        return {
            "ok": False,
            "state": "error",
            "schema_version": SCHEMA_VERSION,
            "canonical_title": dns.hit.title,
            "year": y,
            "refusal_reason": f"markdown missing at {dns.hit.path}",
            "fields": [],
            "tables": [],
            "lists": [],
        }
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        logger.warning("wiki_extract read failed for %s: %s", path, exc)
        return {
            "ok": False,
            "state": "error",
            "schema_version": SCHEMA_VERSION,
            "canonical_title": dns.hit.title,
            "year": y,
            "refusal_reason": f"read error: {exc}",
            "fields": [],
            "tables": [],
            "lists": [],
        }
    hint = need_hint or user_question
    result = extract_from_markdown(
        text,
        title=dns.hit.title,
        year=y,
        need_hint=hint,
        section=section,
        path=str(path),
    )
    result["query"] = query
    result["rel_path"] = dns.hit.rel_path
    return result


def wiki_resolve(
    subject: str,
    year: str = "2026",
    *,
    user_question: str = "",
    index_path: Path | None = None,
) -> dict[str, Any]:
    from pipeline.wiki_title_dns import resolve as dns_resolve

    y = validate_year(year)
    dns = dns_resolve(subject, y, user_question=user_question, index_path=index_path)
    state = {
        "hit": "exact",
        "ambiguous": "ambiguous",
        "miss": "missing",
    }.get(dns.status, dns.status)
    # Alias detection: hit but query != title
    if dns.status == "hit" and dns.hit is not None:
        if normalize_loose(subject) != normalize_loose(dns.hit.title):
            state = "alias"
    return {
        "ok": dns.status == "hit",
        "state": state,
        "query": subject,
        "year": y,
        "canonical_title": dns.hit.title if dns.hit else None,
        "path": dns.hit.path if dns.hit else None,
        "rel_path": dns.hit.rel_path if dns.hit else None,
        "candidates": [
            {"title": c.title, "path": c.path, "rel_path": c.rel_path} for c in dns.candidates
        ],
        "reason": dns.reason,
        "source_id": "title_dns",
    }


def normalize_loose(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().casefold())


def remember_wiki_extract(
    subject: str,
    year: str = "2026",
    *,
    dataset: str = "eve_memory",
    need_hint: str = "",
    extract_id: str = "",
) -> dict[str, Any]:
    """Remember a successful structured extract into Cognee (sparse). Never automatic."""
    from pipeline.provenance import provenance_fields, provenance_markdown_footer
    from pipeline.wiki_scout import allowed_promote_datasets, promote_wiki_cache

    y = validate_year(year)
    chosen = (dataset or "eve_memory").strip() or "eve_memory"
    if chosen not in allowed_promote_datasets():
        return {"ok": False, "state": "rejected", "reason": f"dataset not allowed: {chosen}"}

    evidence = wiki_extract(subject, y, need_hint=need_hint)
    if evidence.get("state") != "ok":
        return {
            "ok": False,
            "state": "rejected",
            "reason": evidence.get("refusal_reason") or "extract not ok",
            "extract_state": evidence.get("state"),
        }
    if extract_id and extract_id != evidence.get("extract_id"):
        return {
            "ok": False,
            "state": "rejected",
            "reason": "extract_id mismatch — re-run wiki_extract first",
        }

    prose = format_extract_prose(evidence, max_chars=1800)
    title = str(evidence.get("canonical_title") or subject)
    cache_dir = Path(
        __import__("os").environ.get(
            "EMPIRE_WIKI_CACHE_DIR",
            r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache",
        )
    )
    cache_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^a-z0-9]+", "_", title.casefold()).strip("_")[:80] or "extract"
    cache_path = cache_dir / f"extract_{y}_{safe}.md"
    body = (
        f"# Wikipedia extract — {title} ({y})\n\n"
        f"extract_id: {evidence.get('extract_id')}\n"
        f"source_hash: {evidence.get('source_hash')}\n\n"
        f"{prose}\n\n"
        + provenance_markdown_footer(source="title_dns", tool="wiki_remember", limb="wiki_local")
    )
    try:
        cache_path.write_text(body, encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "state": "rejected", "reason": f"cache write failed: {exc}"}

    promo = promote_wiki_cache(str(cache_path), dataset=chosen)
    return {
        "ok": bool(promo.get("ok")),
        "state": "stored" if promo.get("ok") else "rejected",
        "memory_id": promo.get("dataset"),
        "source_hash": evidence.get("source_hash"),
        "extract_id": evidence.get("extract_id"),
        "cache_path": str(cache_path),
        "promote": promo,
        "provenance": provenance_fields(
            source="title_dns",
            kind="wiki_extract",
            tool="wiki_remember",
            limb="wiki_local",
        ),
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Wikipedia structured extract CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ex = sub.add_parser("extract", help="Resolve + extract Evidence JSON")
    p_ex.add_argument("subject")
    p_ex.add_argument("--year", default="2026")
    p_ex.add_argument("--need", default="")
    p_ex.add_argument("--section", default="")
    p_ex.add_argument("--question", default="")

    p_rs = sub.add_parser("resolve", help="Title DNS resolve only")
    p_rs.add_argument("subject")
    p_rs.add_argument("--year", default="2026")
    p_rs.add_argument("--question", default="")

    p_rm = sub.add_parser("remember", help="Remember ok extract into Cognee")
    p_rm.add_argument("subject")
    p_rm.add_argument("--year", default="2026")
    p_rm.add_argument("--dataset", default="eve_memory")
    p_rm.add_argument("--need", default="")
    p_rm.add_argument("--extract-id", default="")

    args = parser.parse_args(argv)
    if args.cmd == "extract":
        out = wiki_extract(
            args.subject,
            args.year,
            need_hint=args.need,
            section=args.section,
            user_question=args.question,
        )
    elif args.cmd == "resolve":
        out = wiki_resolve(args.subject, args.year, user_question=args.question)
    elif args.cmd == "remember":
        out = remember_wiki_extract(
            args.subject,
            args.year,
            dataset=args.dataset,
            need_hint=args.need,
            extract_id=args.extract_id,
        )
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") or out.get("state") in {"empty", "ambiguous", "unsupported"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
