"""Stream MediaWiki pages-articles XML (.bz2) into Cerebras-style Markdown.

Converts main-namespace (ns=0) articles only, skips redirects, and writes YAML
frontmatter compatible with ``pipeline.wiki_normalizer.normalize_wiki_file`` /
``derive_snapshot_year`` (snapshot_id ``20170301`` -> year ``2017``).

Usage:
    python -m pipeline.wiki_xml_convert \\
      --input I:\\EMPIRE_DATA\\wiki_xml_20170301\\enwiki-20170301-pages-articles.xml.bz2 \\
      --out-dir D:\\wiki_md\\2017 \\
      --limit 100 \\
      --snapshot-id 20170301
"""

from __future__ import annotations

import argparse
import bz2
import hashlib
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

EXTRACTOR_VERSION = "2.2.0-empire-xml"
MW_NS = "{http://www.mediawiki.org/xml/export-0.10/}"
# Some dumps use 0.11; match any mediawiki export namespace via localname helpers.
_RE_REDIRECT = re.compile(r"^\s*#\s*redirect\b", re.IGNORECASE)
_RE_HEADING = re.compile(r"^(={2,6})\s*(.+?)\s*\1\s*$", re.MULTILINE)
_RE_LINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")
_RE_CATEGORY = re.compile(r"\[\[Category:([^\]|]+)(?:\|[^\]]*)?\]\]", re.IGNORECASE)
_RE_SISTER = re.compile(
    r"\{\{\s*(?:sister|wiktionary|commons|wikiquote|wikibooks|wikisource|wikinews|"
    r"wikiversity|wikivoyage|wikispecies|meta|species)\s*\|",
    re.IGNORECASE,
)
_RE_BOLD_ITALIC = re.compile(r"'{5}(.+?)'{5}")
_RE_BOLD = re.compile(r"'{3}(.+?)'{3}")
_RE_ITALIC = re.compile(r"'{2}(.+?)'{2}")
_RE_EXTERNAL = re.compile(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]")
_RE_EXTERNAL_BARE = re.compile(r"\[(https?://[^\s\]]+)\]")
_RE_REF = re.compile(r"<ref\b[^>]*/?>.*?</ref>|<ref\b[^>]*/>", re.IGNORECASE | re.DOTALL)
_RE_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_RE_TEMPLATE = re.compile(r"\{\{[^{}]*\}\}")
_RE_FILE = re.compile(r"\[\[(?:File|Image):[^\]]+\]\]", re.IGNORECASE)
_RE_TABLE = re.compile(r"\{\|.*?\|\}", re.DOTALL)
_RE_NOWIKI = re.compile(r"<nowiki>.*?</nowiki>", re.IGNORECASE | re.DOTALL)
_RE_HTML = re.compile(r"</?(?:div|span|small|big|br|hr|center|font|gallery|poem)[^>]*>", re.IGNORECASE)


def _local(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def _child(elem: ET.Element, name: str) -> ET.Element | None:
    for child in elem:
        if _local(child.tag) == name:
            return child
    return None


def _text(elem: ET.Element | None) -> str:
    if elem is None or elem.text is None:
        return ""
    return elem.text


def is_redirect(text: str) -> bool:
    return bool(_RE_REDIRECT.match(text or ""))


def extract_outgoing_links(wikitext: str) -> list[str]:
    links: list[str] = []
    seen: set[str] = set()
    skip_prefixes = ("category:", "file:", "image:", "media:", "wikipedia:")
    for match in _RE_LINK.finditer(wikitext):
        target = match.group(1).strip()
        if not target:
            continue
        if target.startswith(":"):
            target = target.lstrip(":")
        # Drop section anchors for the link target list
        target = target.split("#", 1)[0].strip()
        lower = target.lower()
        if any(lower.startswith(p) for p in skip_prefixes):
            continue
        target = target.replace("_", " ").strip()
        if not target or target in seen:
            continue
        seen.add(target)
        links.append(target)
    return links


def extract_categories(wikitext: str) -> list[str]:
    cats: list[str] = []
    seen: set[str] = set()
    for match in _RE_CATEGORY.finditer(wikitext):
        name = match.group(1).replace("_", " ").strip()
        if name and name not in seen:
            seen.add(name)
            cats.append(name)
    return cats


def extract_section_headings(wikitext: str) -> list[str]:
    headings: list[str] = []
    for match in _RE_HEADING.finditer(wikitext):
        title = match.group(2).strip()
        # Strip residual wiki markup from heading text
        title = _RE_LINK.sub(lambda m: (m.group(1).split("|")[-1] if "|" in m.group(0) else m.group(1)), title)
        title = re.sub(r"'{2,5}", "", title).strip()
        if title:
            headings.append(title)
    return headings


def extract_sister_links(wikitext: str) -> list[str]:
    # Cerebras leaves sister_links as template-derived; keep empty unless obvious.
    _ = wikitext
    return []


def wikitext_to_markdown(title: str, wikitext: str) -> str:
    """Pragmatic wikitext → Markdown (not a full MediaWiki parser)."""
    text = wikitext or ""
    text = _RE_COMMENT.sub("", text)
    text = _RE_NOWIKI.sub("", text)
    text = _RE_REF.sub("", text)
    text = _RE_FILE.sub("", text)
    text = _RE_TABLE.sub("", text)
    # Collapse nested templates iteratively (shallow)
    for _ in range(8):
        new = _RE_TEMPLATE.sub("", text)
        if new == text:
            break
        text = new
    text = _RE_HTML.sub("", text)
    text = _RE_EXTERNAL.sub(r"[\2](\1)", text)
    text = _RE_EXTERNAL_BARE.sub(r"<\1>", text)

    def _link_sub(m: re.Match[str]) -> str:
        target = (m.group(1) or "").strip()
        label = (m.group(2) if m.lastindex and m.group(2) is not None else "").strip()
        if target.lower().startswith("category:"):
            return ""
        if not label:
            label = target.split("#", 1)[0].strip() or target
        if target.startswith("#"):
            return label
        return label

    text = _RE_LINK.sub(_link_sub, text)
    text = _RE_BOLD_ITALIC.sub(r"***\1***", text)
    text = _RE_BOLD.sub(r"**\1**", text)
    text = _RE_ITALIC.sub(r"*\1*", text)

    # Headings: == X == -> ## X
    def _heading_sub(m: re.Match[str]) -> str:
        level = len(m.group(1))
        md_level = max(2, min(level, 6))
        return f"{'#' * md_level} {m.group(2).strip()}"

    text = _RE_HEADING.sub(_heading_sub, text)

    # Wiki bullets are "* item" / "** item" (asterisks + whitespace). Do NOT touch "**bold**".
    lines: list[str] = []
    bullet_re = re.compile(r"^(\*{1,5})\s+(.*)$")
    for line in text.splitlines():
        stripped = line.rstrip()
        m = bullet_re.match(stripped)
        if m:
            depth = len(m.group(1))
            indent = "  " * (depth - 1)
            stripped = f"{indent}- {m.group(2)}"
        lines.append(stripped)

    body = "\n".join(lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return f"# {title}\n\n{body}\n"


def _yaml_scalar(value: str | int) -> str:
    if isinstance(value, int):
        return str(value)
    # Match Cerebras: JSON-style quoting for strings
    return json.dumps(str(value), ensure_ascii=False)


def _yaml_list(items: list[str]) -> str:
    if not items:
        return " []"
    lines = [""]
    for item in items:
        lines.append(f"  - {_yaml_scalar(item)}")
    return "\n".join(lines)


def build_markdown(
    *,
    page_id: str,
    title: str,
    revision_id: str,
    revision_timestamp: str,
    wikitext: str,
    snapshot_id: str,
    snapshot_year: str,
    batch_name: str,
) -> tuple[str, str]:
    links = extract_outgoing_links(wikitext)
    categories = extract_categories(wikitext)
    headings = extract_section_headings(wikitext)
    sisters = extract_sister_links(wikitext)
    body_md = wikitext_to_markdown(title, wikitext)
    # Hash the markdown body (without frontmatter), Cerebras-style
    body_only = body_md
    body_sha = hashlib.sha256(body_only.encode("utf-8")).hexdigest()
    # Counts exclude the leading "# Title\n\n" roughly — use full body text
    plain = re.sub(r"^# .+\n+", "", body_only).strip()
    char_count = len(plain)
    word_count = len(plain.split()) if plain else 0
    filename = f"wiki_{page_id}.md"
    corpus_rel = f"{batch_name}/{filename}"
    doc_id = f"wikipedia:{snapshot_id}:{page_id}"

    fm = [
        "---",
        f'extractor_version: "{EXTRACTOR_VERSION}"',
        f"doc_id: {_yaml_scalar(doc_id)}",
        "source: wikipedia",
        f"snapshot_id: {_yaml_scalar(snapshot_id)}",
        f"snapshot_year: {_yaml_scalar(snapshot_year)}",
        "wiki_namespace: 0",
        f"page_id: {_yaml_scalar(page_id)}",
        f"title: {_yaml_scalar(title)}",
        f"corpus_rel_path: {_yaml_scalar(corpus_rel)}",
        f"body_sha256: {body_sha}",
        f"revision_id: {_yaml_scalar(revision_id)}",
        f"revision_timestamp: {_yaml_scalar(revision_timestamp)}",
        f"char_count: {char_count}",
        f"word_count: {word_count}",
        f"outgoing_links:{_yaml_list(links)}",
        f"categories:{_yaml_list(categories)}",
        f"sister_links:{_yaml_list(sisters)}",
        f"section_headings:{_yaml_list(headings)}",
        "---",
        "",
    ]
    return "\n".join(fm) + body_md, filename


def iter_pages(bz2_path: Path):
    """Yield page dicts from a streaming bz2 MediaWiki XML dump."""
    opener = bz2.open if str(bz2_path).endswith(".bz2") else open
    with opener(bz2_path, "rb") as fh:
        # Clear namespaces so tags are local-friendly where possible; still use _local.
        context = ET.iterparse(fh, events=("end",))
        for _event, elem in context:
            if _local(elem.tag) != "page":
                continue
            ns_el = _child(elem, "ns")
            title_el = _child(elem, "title")
            id_el = _child(elem, "id")
            rev = _child(elem, "revision")
            ns = (_text(ns_el) or "").strip()
            title = (_text(title_el) or "").strip()
            page_id = (_text(id_el) or "").strip()
            revision_id = ""
            revision_timestamp = ""
            wikitext = ""
            if rev is not None:
                revision_id = (_text(_child(rev, "id")) or "").strip()
                revision_timestamp = (_text(_child(rev, "timestamp")) or "").strip()
                text_el = _child(rev, "text")
                wikitext = _text(text_el) or ""
                if text_el is not None and not wikitext and text_el.text is None:
                    # ElementTree may leave text only in .text
                    wikitext = "".join(text_el.itertext())
            yield {
                "ns": ns,
                "title": title,
                "page_id": page_id,
                "revision_id": revision_id,
                "revision_timestamp": revision_timestamp,
                "wikitext": wikitext,
            }
            elem.clear()


def convert(
    *,
    input_path: Path,
    out_dir: Path,
    limit: int,
    snapshot_id: str,
    snapshot_year: str,
    batch_size: int = 10000,
    skip_redirects: bool = True,
    sleep_ms: int = 0,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped_redirect = 0
    skipped_ns = 0
    scanned = 0
    batch_idx = 0
    batch_count = 0
    t0 = time.time()

    for page in iter_pages(input_path):
        scanned += 1
        if page["ns"] != "0":
            skipped_ns += 1
            continue
        if skip_redirects and is_redirect(page["wikitext"]):
            skipped_redirect += 1
            continue
        if not page["page_id"] or not page["title"]:
            continue

        batch_name = f"batch_{batch_idx:05d}"
        batch_dir = out_dir / batch_name
        batch_dir.mkdir(parents=True, exist_ok=True)

        content, filename = build_markdown(
            page_id=page["page_id"],
            title=page["title"],
            revision_id=page["revision_id"],
            revision_timestamp=page["revision_timestamp"],
            wikitext=page["wikitext"],
            snapshot_id=snapshot_id,
            snapshot_year=snapshot_year,
            batch_name=batch_name,
        )
        (batch_dir / filename).write_text(content, encoding="utf-8")
        written += 1
        batch_count += 1

        if written % 25 == 0 or written == limit:
            elapsed = time.time() - t0
            print(
                f"progress: written={written} scanned={scanned} "
                f"redir_skip={skipped_redirect} ns_skip={skipped_ns} "
                f"elapsed_s={elapsed:.1f}",
                file=sys.stderr,
                flush=True,
            )

        if sleep_ms > 0:
            time.sleep(sleep_ms / 1000.0)

        if batch_count >= batch_size:
            batch_idx += 1
            batch_count = 0

        if 0 < limit <= written:
            break

    return {
        "written": written,
        "scanned": scanned,
        "skipped_redirect": skipped_redirect,
        "skipped_ns": skipped_ns,
        "out_dir": str(out_dir),
        "snapshot_id": snapshot_id,
        "snapshot_year": snapshot_year,
        "elapsed_s": round(time.time() - t0, 2),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="MediaWiki XML.bz2 → Cerebras-style Markdown")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to enwiki-*-pages-articles.xml.bz2",
    )
    parser.add_argument(
        "--out-dir",
        required=True,
        help="Output root (e.g. D:\\wiki_md\\2017); batch_NNNNN subdirs created",
    )
    parser.add_argument("--limit", type=int, default=0, help="Max articles to write (0 = all)")
    parser.add_argument("--snapshot-id", default="20170301")
    parser.add_argument(
        "--snapshot-year",
        default="",
        help="Defaults to first 4 chars of snapshot-id",
    )
    parser.add_argument("--batch-size", type=int, default=10000, help="Files per batch_NNNNN dir")
    parser.add_argument(
        "--keep-redirects",
        action="store_true",
        help="Write redirect pages (default: skip, matching Cerebras practice)",
    )
    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=0,
        help="Optional sleep after each write (throttle for shared disks)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        print(f"ERROR: input not found: {input_path}", file=sys.stderr)
        return 1

    snapshot_year = args.snapshot_year.strip() or args.snapshot_id[:4]
    result = convert(
        input_path=input_path,
        out_dir=Path(args.out_dir),
        limit=args.limit,
        snapshot_id=args.snapshot_id,
        snapshot_year=snapshot_year,
        batch_size=args.batch_size,
        skip_redirects=not args.keep_redirects,
        sleep_ms=args.sleep_ms,
    )
    print(json.dumps(result, indent=2))
    print("__WIKI_XML_CONVERT__" + json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
