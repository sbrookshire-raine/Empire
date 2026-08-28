#!/usr/bin/env python3
"""postgres-mcp-specialist helpers for EMPIRE Build1.

Thin wrappers: install check, TCP/URI smoke probe, MCP env suggestion.
Does not ship the FastMCP server itself — install gabriel-herencia/postgres-mcp
(or the published package name from that repo) separately.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import socket
import sys
from urllib.parse import urlparse

DEFAULT_URI = "postgresql://cognee:cognee@localhost:5432/cognee_db"


def check_install() -> dict:
    names = ("postgres_mcp", "postgres_mcp_server", "pg_mcp")
    found = [n for n in names if importlib.util.find_spec(n) is not None]
    return {
        "ok": bool(found),
        "found_modules": found,
        "hint": "pip install from https://github.com/gabriel-herencia/postgres-mcp if none found",
    }


def probe_host(uri: str) -> dict:
    parsed = urlparse(uri)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 5432
    try:
        with socket.create_connection((host, port), timeout=3):
            return {"ok": True, "host": host, "port": port}
    except OSError as exc:
        return {"ok": False, "host": host, "port": port, "error": str(exc)}


def suggest_mcp_env(uri: str, mode: str) -> dict:
    return {
        "DATABASE_URI": uri,
        "PG_MCP_ACCESS_MODE": mode,
        "cursor_mcp_snippet": {
            "empire-postgres": {
                "command": sys.executable,
                "args": ["-m", "postgres_mcp"],
                "env": {"DATABASE_URI": uri, "PG_MCP_ACCESS_MODE": mode},
            }
        },
        "note": "Confirm -m module name against upstream README after install.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="EMPIRE postgres-mcp helper")
    parser.add_argument(
        "--uri",
        default=os.environ.get("DATABASE_URI", DEFAULT_URI),
        help="Postgres URI (default EMPIRE cognee_db)",
    )
    parser.add_argument(
        "--mode",
        default=os.environ.get("PG_MCP_ACCESS_MODE", "readonly"),
        choices=("readonly", "readwrite", "admin"),
    )
    parser.add_argument("--check-install", action="store_true")
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--suggest-env", action="store_true")
    args = parser.parse_args()

    if not any((args.check_install, args.probe, args.suggest_env)):
        args.check_install = args.probe = args.suggest_env = True

    out: dict = {}
    if args.check_install:
        out["install"] = check_install()
    if args.probe:
        out["probe"] = probe_host(args.uri)
    if args.suggest_env:
        out["mcp"] = suggest_mcp_env(args.uri, args.mode)

    print(json.dumps(out, indent=2))
    install_ok = out.get("install", {}).get("ok", True)
    probe_ok = out.get("probe", {}).get("ok", True)
    return 0 if install_ok and probe_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
