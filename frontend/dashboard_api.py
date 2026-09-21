"""Read-only dashboard projections for EMPIRE catalog and operations."""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
from pathlib import Path
from typing import Any

from pipeline import resource_pulse

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DB = Path(os.environ.get("EMPIRE_CATALOG_DB", ROOT / "config" / "eve-capabilities" / "catalog.db"))
AUDIT_DIR = ROOT / "eve-audit"
TASK_NAMES = ("EMPIRE-AmbientMemoryWatchdog", "EMPIRE-ResearchScavenger")


def _read_catalog() -> sqlite3.Connection:
    if not CATALOG_DB.is_file():
        raise FileNotFoundError(f"Catalog not found: {CATALOG_DB}")
    conn = sqlite3.connect(f"file:{CATALOG_DB.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA query_only=ON")
    return conn


def catalog(payload: dict[str, str]) -> dict[str, Any]:
    query = (payload.get("query") or "").strip()[:160]
    category = (payload.get("category") or "").strip()[:120]
    capability = (payload.get("capability") or "").strip()[:120]
    trust = (payload.get("trust") or "").strip()[:120]
    try:
        with _read_catalog() as conn:
            clauses = ["1=1"]
            params: list[Any] = []
            if query:
                clauses.append("(id LIKE ? OR description LIKE ?)")
                params.extend([f"%{query}%", f"%{query}%"])
            if category:
                clauses.append("category = ?")
                params.append(category)
            if capability:
                clauses.append("eve_capability = ?")
                params.append(capability)
            if trust:
                clauses.append("trust_domain = ?")
                params.append(trust)
            where = " AND ".join(clauses)
            rows = [
                dict(row)
                for row in conn.execute(
                    f"""
                    SELECT id, url, description, category, eve_capability, trust_domain,
                           primary_language, score_local, score_cli, score_mcp, score_functional,
                           stars, has_cli, has_mcp
                    FROM repositories WHERE {where}
                    ORDER BY score_functional DESC, score_local DESC, stars DESC, id
                    LIMIT 120
                    """,
                    params,
                ).fetchall()
            ]
            stats = {
                "total_repos": conn.execute("SELECT COUNT(*) FROM repositories").fetchone()[0],
                "mcp_native": conn.execute("SELECT COUNT(*) FROM repositories WHERE has_mcp = 1").fetchone()[0],
                "cli_tools": conn.execute("SELECT COUNT(*) FROM repositories WHERE has_cli = 1").fetchone()[0],
            }
            options = {
                "categories": [r[0] for r in conn.execute("SELECT DISTINCT category FROM repositories WHERE category IS NOT NULL AND category != '' ORDER BY category")],
                "capabilities": [r[0] for r in conn.execute("SELECT DISTINCT eve_capability FROM repositories WHERE eve_capability IS NOT NULL AND eve_capability != '' ORDER BY eve_capability")],
                "trust_domains": [r[0] for r in conn.execute("SELECT DISTINCT trust_domain FROM repositories WHERE trust_domain IS NOT NULL AND trust_domain != '' ORDER BY trust_domain")],
            }
        return {"ok": True, "stats": stats, "options": options, "rows": rows, "database": str(CATALOG_DB)}
    except (OSError, sqlite3.Error) as exc:
        return {"ok": False, "error": str(exc), "stats": {}, "options": {}, "rows": []}


def resource() -> dict[str, Any]:
    try:
        return resource_pulse.pulse()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "headroom_ok": False, "headroom_reasons": ["Resource pulse unavailable"]}


def _task_state(name: str) -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["schtasks.exe", "/Query", "/TN", name, "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if result.returncode != 0:
            return {"name": name, "status": "down", "detail": "Task not registered"}
        values = next(iter(__import__("csv").reader([result.stdout.strip()])), [])
        return {"name": name, "status": "active" if len(values) > 2 and values[2].strip().casefold() == "running" else "ready", "detail": values[2] if len(values) > 2 else "registered"}
    except (OSError, subprocess.SubprocessError, StopIteration):
        return {"name": name, "status": "unknown", "detail": "Scheduler probe unavailable"}


def workers() -> dict[str, Any]:
    return {
        "ok": True,
        "workers": [
            {**_task_state(TASK_NAMES[0]), "label": "Memory Watchdog", "status_path": str(AUDIT_DIR / "ambient-memory-status.json")},
            {**_task_state(TASK_NAMES[1]), "label": "Research Scavenger", "status_path": str(AUDIT_DIR / "research-scavenger-status.json")},
        ],
    }
