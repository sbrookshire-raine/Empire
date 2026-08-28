#!/usr/bin/env python3
"""readable-mcp-scrape helpers for EMPIRE Build1.

Prefer the FastMCP server (tommypj/readable-mcp) when registered.
This script provides: install check + optional Trafilatura one-shot convert
for local staging before Cognee ingest.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import trafilatura
except ImportError:  # optional until pip install
    trafilatura = None

BLOCKED_HOST_SUFFIXES = (
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
    "metadata.google.internal",
)


def check_install() -> dict:
    modules = ("readable_mcp", "trafilatura")
    found = {m: importlib.util.find_spec(m) is not None for m in modules}
    return {
        "ok": any(found.values()),
        "modules": found,
        "hint": "pip install readable-mcp trafilatura — see https://github.com/tommypj/readable-mcp",
    }


def _ssrf_guard(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"unsupported scheme: {parsed.scheme!r}")
    host = (parsed.hostname or "").lower()
    if not host:
        raise ValueError("missing host")
    if host.endswith(".local") or host in BLOCKED_HOST_SUFFIXES:
        raise ValueError(f"blocked host for agent fetch: {host}")
    # Basic private-range reject (not a full SSRF stack — MCP server is preferred)
    if host.startswith("10.") or host.startswith("192.168.") or host.startswith("169.254."):
        raise ValueError(f"private/link-local host blocked: {host}")


def convert_url(url: str) -> dict:
    _ssrf_guard(url)
    if trafilatura is None:
        return {
            "ok": False,
            "error": "trafilatura not installed; install readable-mcp / trafilatura",
        }

    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return {"ok": False, "error": "fetch failed or empty body", "url": url}
    md = trafilatura.extract(downloaded, output_format="markdown", include_comments=False)
    if not md:
        return {"ok": False, "error": "extraction produced empty markdown", "url": url}
    return {"ok": True, "url": url, "markdown": md, "chars": len(md)}


def main() -> int:
    parser = argparse.ArgumentParser(description="EMPIRE readable/Trafilatura helper")
    parser.add_argument("--check-install", action="store_true")
    parser.add_argument("--url", help="URL to convert to Markdown")
    parser.add_argument("-o", "--output", type=Path, help="Write Markdown to file")
    args = parser.parse_args()

    if args.check_install or not args.url:
        result = check_install()
        print(json.dumps(result, indent=2))
        if not args.url:
            return 0 if result["ok"] else 1

    try:
        out = convert_url(args.url)
    except ValueError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2))
        return 2

    if args.output and out.get("ok"):
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out["markdown"], encoding="utf-8")
        out = {k: v for k, v in out.items() if k != "markdown"}
        out["wrote"] = str(args.output)

    # Avoid dumping huge markdown to stdout unless no -o
    if out.get("ok") and "markdown" in out and not args.output:
        sys.stdout.write(out["markdown"])
        return 0

    print(json.dumps({k: v for k, v in out.items() if k != "markdown"}, indent=2))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
