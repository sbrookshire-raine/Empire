"""Docs guide scraper — llms.txt / sitemap discovery + Markdown assembly.

Outputs to harvest_cache under Thought Experiments. Never auto-promotes to Cognee.
Ported from Gumloop TOOL_GATHERER docs-guide-scraper playbook for local EMPIRE use.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso
from pipeline.web_scout import fetch_url, normalize_url

DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_HARVEST_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\harvest_cache",
    )
)
DEFAULT_MAX_PAGES = int(os.environ.get("EMPIRE_DOCS_SCRAPE_MAX_PAGES", "80"))
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")
_LLM_PAGE = re.compile(r"^#\s+(.+?)\s*$", re.M)
_LEFT_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9]*(?:\s[^>]{0,60})?>")


def _safe_name(value: str, fallback: str = "docs") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="harvest-", suffix=".md", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def _origin(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


def _fetch_text(url: str) -> dict[str, Any]:
    result = fetch_url(url)
    if not result.get("ok"):
        return result
    body = str(result.get("text") or result.get("body") or result.get("markdown") or "")
    title = str(result.get("title") or url)
    return {"ok": True, "url": url, "title": title, "body": body}


def discover_pages(root_url: str, *, max_pages: int = DEFAULT_MAX_PAGES) -> dict[str, Any]:
    """Discover doc page URLs via llms.txt, llms-full.txt, then sitemap.xml."""
    root = normalize_url(root_url)
    if not root:
        return {"ok": False, "error": "empty root_url"}

    origin = _origin(root)
    parsed = urlparse(root)
    path_prefix = parsed.path.rstrip("/") or ""
    candidates: list[str] = []

    for suffix in ("/llms-full.txt", "/llms.txt", "llms-full.txt", "llms.txt"):
        for base in (root.rstrip("/"), origin + path_prefix):
            probe = urljoin(base + "/", suffix.lstrip("/"))
            got = _fetch_text(probe)
            if not got.get("ok"):
                continue
            body = got["body"]
            if len(body) < 40:
                continue
            if "llms-full" in suffix or body.count("# ") >= 3:
                pages = _parse_llms_full(body, origin)
                if pages:
                    return {
                        "ok": True,
                        "method": "llms-full" if "full" in suffix else "llms",
                        "root_url": root,
                        "pages": pages[:max_pages],
                        "count": min(len(pages), max_pages),
                    }
            for line in body.splitlines():
                line = line.strip()
                if line.startswith("http"):
                    candidates.append(line)
            if candidates:
                return {
                    "ok": True,
                    "method": "llms-index",
                    "root_url": root,
                    "pages": [{"url": u, "title": u} for u in candidates[:max_pages]],
                    "count": min(len(candidates), max_pages),
                }

    for sitemap in (urljoin(origin + "/", "sitemap.xml"), urljoin(root.rstrip("/") + "/", "sitemap.xml")):
        got = _fetch_text(sitemap)
        if not got.get("ok"):
            continue
        urls = _parse_sitemap(got["body"], origin, path_prefix)
        if urls:
            return {
                "ok": True,
                "method": "sitemap",
                "root_url": root,
                "pages": [{"url": u, "title": u} for u in urls[:max_pages]],
                "count": min(len(urls), max_pages),
            }

    single = _fetch_text(root)
    if single.get("ok"):
        return {
            "ok": True,
            "method": "single-page",
            "root_url": root,
            "pages": [{"url": root, "title": single.get("title", root)}],
            "count": 1,
        }

    return {"ok": False, "error": "no llms.txt, sitemap, or fetchable root page", "root_url": root}


def _parse_llms_full(body: str, origin: str) -> list[dict[str, str]]:
    pages: list[dict[str, str]] = []
    chunks = re.split(r"(?=^#\s+)", body, flags=re.M)
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        m = _LLM_PAGE.match(chunk)
        title = m.group(1).strip() if m else "Section"
        pages.append({"url": origin, "title": title, "inline_markdown": chunk})
    return pages


def _parse_sitemap(xml_text: str, origin: str, path_prefix: str) -> list[str]:
    urls: list[str] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return urls
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    if tag == "sitemapindex":
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                nested = _fetch_text(loc.text.strip())
                if nested.get("ok"):
                    urls.extend(_parse_sitemap(nested["body"], origin, path_prefix))
        return urls
    for loc in root.iter():
        if not loc.tag.endswith("loc") or not loc.text:
            continue
        u = loc.text.strip()
        if path_prefix and path_prefix not in urlparse(u).path:
            continue
        if u.startswith("http"):
            urls.append(u)
    return urls


def _clean_markdown(text: str) -> str:
    text = re.sub(r"\\([#\-_*])", r"\1", text)
    text = _LEFT_TAG.sub("", text)
    return text.strip()


def scrape_site(
    root_url: str,
    *,
    max_pages: int = DEFAULT_MAX_PAGES,
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
) -> dict[str, Any]:
    """Discover pages and assemble a single Markdown guide under harvest_cache."""
    discovery = discover_pages(root_url, max_pages=max_pages)
    if not discovery.get("ok"):
        return discovery

    pages = discovery.get("pages") or []
    sections: list[str] = []
    fetched = 0
    errors: list[str] = []

    for entry in pages:
        inline = entry.get("inline_markdown")
        if inline:
            sections.append(_clean_markdown(str(inline)))
            fetched += 1
            continue
        url = str(entry.get("url") or "")
        if not url:
            continue
        got = fetch_url(url)
        if not got.get("ok"):
            errors.append(f"{url}: {got.get('error', 'fetch failed')}")
            continue
        title = str(got.get("title") or entry.get("title") or url)
        body = str(got.get("text") or got.get("markdown") or got.get("body") or "")
        body = _clean_markdown(body)
        if not body:
            errors.append(f"{url}: empty body")
            continue
        sections.append(f"### {title}\n\n**Source:** {url}\n\n{body}\n\n---\n")
        fetched += 1

    if not sections:
        return {"ok": False, "error": "no page content fetched", "errors": errors}

    host = urlparse(normalize_url(root_url)).netloc or "docs"
    app_name = _safe_name(host.split(".")[0] if host else "docs", "docs")
    title = f"{app_name.replace('_', ' ').title()} — Complete Documentation Guide"
    header = (
        f"# {title}\n\n"
        f"> Source: {normalize_url(root_url)} | pages: {fetched} | "
        f"method: {discovery.get('method')} | {utc_now_iso()}\n\n"
    )
    if note.strip():
        header += f"> Note: {note.strip()}\n\n"
    header += "## Table of Contents\n\n"
    for i, entry in enumerate(pages[:fetched], start=1):
        label = str(entry.get("title") or entry.get("url") or f"Page {i}")
        anchor = _safe_name(label.lower(), f"page-{i}")
        header += f"- [{label}](#{anchor})\n"
    header += "\n---\n\n"

    fm = [
        "---",
        *provenance_fields(
            source=normalize_url(root_url),
            kind="docs_guide",
            tool="docs_guide_scraper",
            limb="tool_forge",
            extra={
                "method": discovery.get("method"),
                "pages_fetched": fetched,
                "architect_note": note.strip(),
            },
        ),
        "---",
        "",
    ]
    markdown = "\n".join(fm) + header + "\n\n".join(sections)
    markdown = markdown.rstrip() + provenance_markdown_footer(
        source="docs_guide",
        tool="docs_guide_scraper",
        limb="tool_forge",
    )

    out_dir = cache_dir or DEFAULT_CACHE_DIR
    filename = f"{app_name}_Complete_Guide.md"
    path = out_dir / filename
    if write_files:
        _atomic_write(path, markdown)

    return {
        "ok": True,
        "root_url": normalize_url(root_url),
        "method": discovery.get("method"),
        "pages_fetched": fetched,
        "errors": errors,
        "path": str(path) if write_files else None,
        "filename": filename,
        "chars": len(markdown),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE docs guide scraper")
    parser.add_argument("url", help="Documentation root URL")
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    parser.add_argument("--discover-only", action="store_true")
    parser.add_argument("--note", default="")
    parser.add_argument("-o", "--output-dir", type=Path, default=DEFAULT_CACHE_DIR)
    args = parser.parse_args(argv)

    if args.discover_only:
        result = discover_pages(args.url, max_pages=args.max_pages)
    else:
        result = scrape_site(
            args.url,
            max_pages=args.max_pages,
            cache_dir=args.output_dir,
            note=args.note,
        )
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
