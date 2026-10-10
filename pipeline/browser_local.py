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
from urllib.parse import unquote, urlparse

from pipeline.artifact_lineage import lineage_envelope, sha256_text
from pipeline.rea_inbox import WORKBENCH, inbox_root
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


def _allowed_file_path(path: Path) -> tuple[bool, str]:
    resolved = path.resolve()
    for root in (inbox_root().resolve(), WORKBENCH.resolve(), DEFAULT_CACHE.resolve()):
        try:
            resolved.relative_to(root)
            if resolved.is_file():
                return True, ""
            return False, "file path does not exist"
        except ValueError:
            continue
    return False, "local file must be under REA inbox, Empire_Workbench, or browser_cache"


def resolve_navigate_target(*, url: str = "", html_path: str = "") -> tuple[str | None, str | None]:
    cleaned_url = (url or "").strip()
    cleaned_path = (html_path or "").strip()
    if cleaned_url:
        parsed = urlparse(cleaned_url)
        if parsed.scheme == "file":
            local = Path(unquote(parsed.path)).resolve()
            if os.name == "nt" and str(local).startswith("\\") and len(str(local)) > 2:
                local = Path(str(local)[1:])
            ok, reason = _allowed_file_path(local)
            if not ok:
                return None, reason
            return local.as_uri(), None
        allowed, reason = is_allowed(cleaned_url)
        if not allowed:
            return None, reason
        return cleaned_url, None
    if cleaned_path:
        candidate = Path(cleaned_path)
        if not candidate.is_absolute():
            return None, "html_path must be absolute"
        ok, reason = _allowed_file_path(candidate.resolve())
        if not ok:
            return None, reason
        return candidate.resolve().as_uri(), None
    return None, "url or html_path required"


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


def capture_screenshot(
    *,
    url: str = "",
    html_path: str = "",
    full_page: bool = False,
    note: str = "",
) -> dict[str, Any]:
    target, reason = resolve_navigate_target(url=url, html_path=html_path)
    if not target:
        return {"ok": False, "error": reason or "target required"}

    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        return {
            "ok": False,
            "error": "playwright not installed. Mechanic: pip install playwright && playwright install chromium",
            "url": target,
        }

    screenshot_path = Path()
    title = ""
    final_url = target
    try:
        DEFAULT_CACHE.mkdir(parents=True, exist_ok=True)
        stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
        screenshot_path = DEFAULT_CACHE / f"screenshot_{stamp}.png"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            page.goto(target, wait_until="domcontentloaded", timeout=45000)
            title = page.title() or ""
            final_url = page.url
            page.screenshot(path=str(screenshot_path), full_page=full_page)
            browser.close()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "url": target}

    envelope = lineage_envelope(
        schema_id="BrowserLocalScreenshot.v1",
        tool="browser_capture_screenshot",
        limb="browser_local",
        model_id="playwright.chromium",
        input_hash=sha256_text(target),
        validation_ok=True,
        extra={"final_url": final_url, "architect_note": note or ""},
    )
    return {
        "ok": True,
        "url": target,
        "final_url": final_url,
        "title": title,
        "screenshot_path": str(screenshot_path.resolve()),
        "lineage": envelope,
        "note": "Screenshot only — no clicks or form submit. Allowlisted http(s) or local HTML under Workbench/REA inbox.",
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    args = list(argv if argv is not None else sys.argv[1:])
    if args and args[0] not in {"fetch", "screenshot"} and not args[0].startswith("-"):
        result = fetch_page(args[0], write_files=True, note="")
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1

    parser = argparse.ArgumentParser(description="EMPIRE allowlisted browser fetch")
    sub = parser.add_subparsers(dest="cmd", required=True)
    fetch = sub.add_parser("fetch", help="Fetch allowlisted page text")
    fetch.add_argument("url")
    fetch.add_argument("--no-write", action="store_true")
    fetch.add_argument("--note", default="")
    shot = sub.add_parser("screenshot", help="Capture allowlisted or local HTML screenshot")
    shot.add_argument("--url", default="")
    shot.add_argument("--html-path", default="")
    shot.add_argument("--full-page", action="store_true")
    shot.add_argument("--note", default="")
    parsed = parser.parse_args(args)
    if parsed.cmd == "screenshot":
        result = capture_screenshot(
            url=parsed.url,
            html_path=parsed.html_path,
            full_page=parsed.full_page,
            note=parsed.note,
        )
    else:
        result = fetch_page(
            parsed.url,
            write_files=not parsed.no_write,
            note=parsed.note,
        )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
