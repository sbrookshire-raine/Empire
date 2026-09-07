"""Web scout → Truth Drift-style markdown under Thought Experiments/web_cache.

Local HTTP fetch first. Never auto-promotes to Cognee. No paid search APIs.
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
USER_AGENT = "EMPIRE-WebScout/1.0 (+local; Architect workbench)"


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip = 0
        self.title = ""

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


def fetch_url(url: str, *, timeout: float = 30.0) -> dict[str, Any]:
    cleaned = (url or "").strip()
    if not cleaned:
        return {"ok": False, "error": "url required"}
    parsed = urlparse(cleaned)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return {"ok": False, "error": "Only http(s) URLs allowed"}

    req = Request(cleaned, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=timeout) as resp:  # noqa: S310 — intentional local scout
            raw = resp.read(2_000_000)
            content_type = str(resp.headers.get("Content-Type") or "")
            final_url = str(resp.geturl() or cleaned)
            status = int(getattr(resp, "status", 200) or 200)
    except HTTPError as exc:
        return {"ok": False, "error": f"HTTP {exc.code}", "url": cleaned}
    except URLError as exc:
        return {"ok": False, "error": str(exc.reason or exc), "url": cleaned}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "url": cleaned}

    try:
        text = raw.decode("utf-8", errors="replace")
    except Exception:
        text = raw.decode("latin-1", errors="replace")

    title = final_url
    body = text
    if "html" in content_type.lower() or text.lstrip().lower().startswith("<!doctype") or "<html" in text[:500].lower():
        parser = _TextExtractor()
        try:
            parser.feed(text)
            body = parser.text()
            # crude title
            m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
            if m:
                title = re.sub(r"\s+", " ", m.group(1)).strip() or title
        except Exception:
            body = re.sub(r"<[^>]+>", " ", text)
            body = re.sub(r"\s+", " ", body).strip()

    if len(body) > DEFAULT_MAX_CHARS:
        body = body[: DEFAULT_MAX_CHARS - 1] + "…"

    return {
        "ok": True,
        "url": cleaned,
        "final_url": final_url,
        "status": status,
        "title": title,
        "content_type": content_type,
        "text": body,
        "chars": len(body),
    }


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
                    "title": title,
                    "status": fetched.get("status"),
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
                f"Source: {fetched.get('final_url')}",
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

    return {
        "ok": True,
        "url": fetched.get("url"),
        "final_url": fetched.get("final_url"),
        "title": title,
        "path": path_str,
        "chars": fetched.get("chars"),
        "summary": (str(fetched.get("text") or "")[:280] + ("…" if int(fetched.get("chars") or 0) > 280 else "")),
        "note": (
            f"Cached under {path_str}. Promote to Cognee only via cognee_remember after triage."
            if path_str
            else "Fetched without writing."
        ),
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
