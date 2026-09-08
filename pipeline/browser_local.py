"""Allowlisted Playwright browser inspect — localhost EMPIRE origins only.

No arbitrary public browsing. Confirmation required conceptually for mutations
(this module only fetches page title/text; no form submit by default).
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from pipeline.artifact_lineage import lineage_envelope, sha256_text
from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST_PATH = EMPIRE_ROOT / "config" / "browser_allowlist.json"
DEFAULT_CACHE = Path(
    os.environ.get(
        "EMPIRE_BROWSER_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\browser_cache",
    )
)


def load_allowlist() -> dict[str, Any]:
    try:
        raw = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
        return raw if isinstance(raw, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {
            "allow_url_prefixes": ["http://127.0.0.1:8080/", "http://localhost:8080/"],
            "block_message": "URL not allowlisted.",
        }


def is_allowed(url: str) -> tuple[bool, str]:
    cleaned = (url or "").strip()
    if not cleaned:
        return False, "url required"
    parsed = urlparse(cleaned)
    if parsed.scheme not in {"http", "https"}:
        return False, "only http(s)"
    cfg = load_allowlist()
    prefixes = cfg.get("allow_url_prefixes") or []
    for prefix in prefixes:
        if cleaned.startswith(str(prefix)):
            return True, ""
    hosts = {str(h).lower() for h in (cfg.get("allow_hosts") or [])}
    ports = {int(p) for p in (cfg.get("allow_ports") or [])}
    host = (parsed.hostname or "").lower()
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    if host in hosts and port in ports:
        return True, ""
    return False, str(cfg.get("block_message") or "URL not allowlisted.")


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp = tempfile.mkstemp(prefix="browser-", suffix=".md", dir=str(path.parent))
    tmp_path = Path(tmp)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def fetch_page(url: str, *, write_files: bool = True, note: str = "") -> dict[str, Any]:
    allowed, reason = is_allowed(url)
    if not allowed:
        return {"ok": False, "error": reason, "url": url}

    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        return {
            "ok": False,
            "error": "playwright not installed. Mechanic: pip install playwright && playwright install chromium",
            "url": url,
        }

    title = ""
    text = ""
    final_url = url
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            title = page.title() or ""
            text = page.inner_text("body")[:8000]
            final_url = page.url
            browser.close()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "url": url}

    envelope = lineage_envelope(
        schema_id="BrowserLocalPage.v1",
        tool="browser_local_fetch",
        limb="browser_local",
        model_id="playwright.chromium",
        input_hash=sha256_text(url),
        validation_ok=True,
        extra={"final_url": final_url, "architect_note": note or ""},
    )
    path_str = ""
    if write_files:
        stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
        path = DEFAULT_CACHE / f"page_{stamp}.md"
        body = "\n".join(
            [
                "---",
                *provenance_fields(
                    source="browser_local",
                    kind="allowlisted_page",
                    tool="browser_local_fetch",
                    limb="browser_local",
                    extra={"url": url, "final_url": final_url, "title": title},
                ),
                "---",
                f"# {title or final_url}",
                "",
                f"URL: {final_url}",
                "",
                text,
                "",
                f"```json\n{json.dumps(envelope, indent=2)}\n```",
                provenance_markdown_footer(
                    source="browser_local",
                    tool="browser_local_fetch",
                    limb="browser_local",
                ),
            ]
        )
        try:
            _atomic_write(path, body)
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc)}

    return {
        "ok": True,
        "url": url,
        "final_url": final_url,
        "title": title,
        "chars": len(text),
        "summary": text[:280] + ("…" if len(text) > 280 else ""),
        "lineage": envelope,
        "path": path_str,
        "note": "Allowlisted localhost fetch only. No Cognee write. No form submit.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE allowlisted browser fetch")
    parser.add_argument("url")
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)
    result = fetch_page(args.url, write_files=not args.no_write, note=args.note)
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
