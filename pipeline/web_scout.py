"""Web scout → Truth Drift-style markdown under Thought Experiments/web_cache.

Local HTTP fetch first (optional Trafilatura extraction). Never auto-promotes to Cognee.
Not a search engine — requires a concrete http(s) URL.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_WEB_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\web_cache",
    )
)
DEFAULT_MAX_CHARS = int(os.environ.get("EMPIRE_WEB_BODY_MAX_CHARS", "12000"))
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")
USER_AGENT = os.environ.get(
    "EMPIRE_WEB_SCOUT_UA",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 EMPIRE-WebScout/1.1",
)
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/atom+xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
}


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self._skip:
            self._skip -= 1

    def handle_data(self, data: str) -> None:
        if self._skip:
            return
        text = data.strip()
        if text:
            self._chunks.append(text)

    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self._chunks)).strip()


def _safe_name(value: str, fallback: str = "page") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def normalize_url(url: str) -> str:
    cleaned = (url or "").strip().strip("<>").strip().strip("'\"")
    if not cleaned:
        return ""
    if cleaned.startswith("[") and "](" in cleaned:
        m = re.search(r"\]\((https?://[^)\s]+)\)", cleaned)
        if m:
            cleaned = m.group(1)
    if "://" not in cleaned and re.match(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/.*)?$", cleaned):
        cleaned = "https://" + cleaned
    return cleaned


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="web-", suffix=".md", dir=str(path.parent))
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


def _extract_with_trafilatura(html: str, url: str) -> tuple[str, str] | None:
    try:
        import trafilatura  # type: ignore
    except ImportError:
        return None
    try:
        title = ""
        text = ""
        bare = getattr(trafilatura, "bare_extraction", None)
        if callable(bare):
            doc = bare(
                html,
                url=url,
                include_comments=False,
                include_tables=True,
                favor_recall=True,
            )
            if doc is not None:
                if isinstance(doc, dict):
                    title = str(doc.get("title") or "")
                    text = str(doc.get("text") or doc.get("raw_text") or "")
                else:
                    title = str(getattr(doc, "title", "") or "")
                    text = str(getattr(doc, "text", "") or "")
        if not text:
            text = (
                trafilatura.extract(
                    html,
                    url=url,
                    include_comments=False,
                    include_tables=True,
                    favor_recall=True,
                    output_format="txt",
                )
                or ""
            )
        if text.lstrip().startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                text = parts[2]
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            return None
        if not title:
            m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
            if m:
                title = re.sub(r"\s+", " ", m.group(1)).strip()
        return title or url, text
    except Exception:
        return None


def _extract_basic_html(html: str, fallback_title: str) -> tuple[str, str]:
    parser = _TextExtractor()
    try:
        parser.feed(html)
        body = parser.text()
    except Exception:
        body = re.sub(r"<[^>]+>", " ", html)
        body = re.sub(r"\s+", " ", body).strip()
    title = fallback_title
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip() or title
    return title, body


def _unescape_xml(value: str) -> str:
    text = value or ""
    text = (
        text.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&amp;", "&")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
    )
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _extract_feed(xml_text: str, fallback_title: str) -> tuple[str, str] | None:
    raw = xml_text or ""
    lowered = raw[:2000].lower()
    if "<feed" not in lowered and "<rss" not in lowered and "<entry" not in lowered:
        return None

    feed_title = fallback_title
    m = re.search(r"<feed[^>]*>[\s\S]*?<title[^>]*>(.*?)</title>", raw, re.I)
    if not m:
        m = re.search(r"<channel>[\s\S]*?<title[^>]*>(.*?)</title>", raw, re.I)
    if m:
        feed_title = _unescape_xml(m.group(1)) or feed_title

    entries = re.findall(r"<entry\b[\s\S]*?</entry>", raw, re.I)
    if not entries:
        entries = re.findall(r"<item\b[\s\S]*?</item>", raw, re.I)
    if not entries:
        return None

    lines = [
        f"# {feed_title}",
        "",
        "Feed entries (order as returned by the public feed — "
        "**not** guaranteed official upvote #1 for the day):",
        "",
    ]
    for idx, entry in enumerate(entries[:40], start=1):
        title_m = re.search(r"<title[^>]*>(.*?)</title>", entry, re.I | re.S)
        link_m = re.search(
            r'<link[^>]+href="([^"]+)"[^>]*rel="alternate"|'
            r'<link[^>]+rel="alternate"[^>]+href="([^"]+)"|'
            r"<link>(.*?)</link>|"
            r'<link[^>]+href="([^"]+)"',
            entry,
            re.I | re.S,
        )
        summary_m = re.search(
            r"<summary[^>]*>(.*?)</summary>|"
            r"<content[^>]*>(.*?)</content>|"
            r"<description[^>]*>(.*?)</description>",
            entry,
            re.I | re.S,
        )
        title = _unescape_xml(title_m.group(1) if title_m else f"Entry {idx}")
        link = ""
        if link_m:
            link = next((g for g in link_m.groups() if g), "") or ""
            link = _unescape_xml(link)
        blurb = ""
        if summary_m:
            blurb = _unescape_xml(next((g for g in summary_m.groups() if g), "") or "")
            if len(blurb) > 220:
                blurb = blurb[:219].rstrip() + "…"
        lines.append(f"{idx}. **{title}**" + (f" — {link}" if link else ""))
        if blurb:
            lines.append(f"   {blurb}")
    return feed_title, "\n".join(lines).strip()


def _http_get(url: str, *, timeout: float) -> dict[str, Any]:
    req = Request(url, headers=dict(DEFAULT_HEADERS))
    try:
        with urlopen(req, timeout=timeout) as resp:  # noqa: S310 — intentional local scout
            raw = resp.read(2_500_000)
            return {
                "ok": True,
                "raw": raw,
                "content_type": str(resp.headers.get("Content-Type") or ""),
                "final_url": str(resp.geturl() or url),
                "status": int(getattr(resp, "status", 200) or 200),
                "url": url,
            }
    except HTTPError as exc:
        hint = ""
        if exc.code in {403, 429}:
            hint = " Site blocked the local fetch (bot wall / rate limit)."
        elif exc.code == 404:
            hint = " Page not found — check the URL (title may have moved)."
        return {
            "ok": False,
            "error": f"HTTP {exc.code}.{hint}".strip(),
            "url": url,
            "status": exc.code,
        }
    except URLError as exc:
        return {
            "ok": False,
            "error": f"Network error: {exc.reason or exc}",
            "url": url,
            "hint": "Check DNS/connectivity; Web Scout only fetches public http(s) URLs.",
        }
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "url": url}


def _feed_fallback_urls(url: str) -> list[str]:
    parsed = urlparse(url)
    path = (parsed.path or "/").rstrip("/") or ""
    if path not in {"", "/"}:
        return []
    base = f"{parsed.scheme}://{parsed.netloc}"
    return [
        f"{base}/feed",
        f"{base}/rss",
        f"{base}/atom.xml",
        f"{base}/feed.xml",
        f"{base}/rss.xml",
    ]


def fetch_url(url: str, *, timeout: float = 45.0) -> dict[str, Any]:
    cleaned = normalize_url(url)
    if not cleaned:
        return {
            "ok": False,
            "error": "url required — Web Scout fetches a page URL; it is not a search engine",
        }
    parsed = urlparse(cleaned)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return {
            "ok": False,
            "error": "Only http(s) URLs allowed (example: https://example.com/page)",
            "url": cleaned,
        }

    primary = _http_get(cleaned, timeout=timeout)
    used_fallback = ""
    if not primary.get("ok") and int(primary.get("status") or 0) in {403, 429}:
        for alt in _feed_fallback_urls(cleaned):
            alt_result = _http_get(alt, timeout=timeout)
            if alt_result.get("ok"):
                primary = alt_result
                used_fallback = alt
                break
    if not primary.get("ok"):
        err = dict(primary)
        if int(err.get("status") or 0) in {403, 429}:
            err["hint"] = (
                "Bot wall. Do not invent page content and do not claim you browsed manually. "
                "Ask the Architect for a paste, screenshot, or a public /feed URL if one exists."
            )
        return err

    raw = primary["raw"]
    content_type = str(primary.get("content_type") or "")
    final_url = str(primary.get("final_url") or cleaned)
    status = int(primary.get("status") or 200)

    try:
        text = raw.decode("utf-8", errors="replace")
    except Exception:
        text = raw.decode("latin-1", errors="replace")

    title = final_url
    body = text
    extractor = "raw"
    ctype = content_type.lower()
    is_feed = (
        "xml" in ctype
        or "atom" in ctype
        or "rss" in ctype
        or text.lstrip().startswith("<?xml")
        or "<feed" in text[:1200].lower()
        or "<rss" in text[:1200].lower()
    )
    is_html = (
        "html" in ctype
        or text.lstrip().lower().startswith("<!doctype")
        or "<html" in text[:800].lower()
    )
    if is_feed:
        feed = _extract_feed(text, final_url)
        if feed:
            title, body = feed
            extractor = "atom_rss"
    elif is_html:
        traf = _extract_with_trafilatura(text, final_url)
        if traf:
            title, body = traf
            extractor = "trafilatura"
        else:
            title, body = _extract_basic_html(text, final_url)
            extractor = "html_parser"

    if len(body) > DEFAULT_MAX_CHARS:
        body = body[: DEFAULT_MAX_CHARS - 1] + "…"

    if not body.strip():
        return {
            "ok": False,
            "error": "Fetched the URL but extracted no readable text (likely JS-only page).",
            "url": cleaned,
            "final_url": final_url,
            "status": status,
            "hint": "Paste a static docs URL, or capture the page another way.",
        }

    result: dict[str, Any] = {
        "ok": True,
        "url": cleaned,
        "final_url": final_url,
        "status": status,
        "title": title,
        "content_type": content_type,
        "text": body,
        "chars": len(body),
        "extractor": extractor,
    }
    if used_fallback:
        result["fallback_url"] = used_fallback
        result["note_fetch"] = (
            f"Homepage blocked; used public feed fallback {used_fallback}."
        )
    return result


def scout(
    url: str,
    *,
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
) -> dict[str, Any]:
    fetched = fetch_url(url)
    if not fetched.get("ok"):
        return fetched

    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    title = str(fetched.get("title") or "page")
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    stem = _safe_name(f"{title}_{stamp}")
    path = out_dir / f"{stem}.md"
    path_str = ""
    source_line = str(fetched.get("final_url") or "")
    if fetched.get("fallback_url"):
        source_line += f" (via {fetched.get('fallback_url')})"
    if write_files:
        fm = [
            "---",
            *provenance_fields(
                source="web",
                kind="web_page",
                tool="web_scout",
                limb="web_scout",
                extra={
                    "url": fetched.get("url"),
                    "final_url": fetched.get("final_url"),
                    "fallback_url": fetched.get("fallback_url") or "",
                    "title": title,
                    "status": fetched.get("status"),
                    "extractor": fetched.get("extractor"),
                    "architect_note": note or "",
                },
            ),
            "---",
        ]
        content = "\n".join(
            [
                *fm,
                f"# {title}",
                "",
                f"Source: {source_line}",
                "",
                str(fetched.get("text") or ""),
                provenance_markdown_footer(
                    source="web", tool="web_scout", limb="web_scout"
                ),
            ]
        )
        try:
            _atomic_write(path, content)
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc), "url": url}

    note_out = (
        f"Cached under {path_str}. Promote to Cognee only via cognee_remember after triage."
        if path_str
        else "Fetched without writing."
    )
    if fetched.get("note_fetch"):
        note_out = f"{fetched.get('note_fetch')} {note_out}"

    return {
        "ok": True,
        "url": fetched.get("url"),
        "final_url": fetched.get("final_url"),
        "fallback_url": fetched.get("fallback_url"),
        "title": title,
        "path": path_str,
        "chars": fetched.get("chars"),
        "extractor": fetched.get("extractor"),
        "summary": (
            str(fetched.get("text") or "")[:280]
            + ("…" if int(fetched.get("chars") or 0) > 280 else "")
        ),
        "note": note_out,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE web scout → web_cache markdown")
    parser.add_argument("url")
    parser.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)
    result = scout(
        args.url,
        cache_dir=Path(args.cache_dir),
        write_files=not args.no_write,
        note=args.note,
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
