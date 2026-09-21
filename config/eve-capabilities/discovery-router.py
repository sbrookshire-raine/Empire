"""Read-only FastMCP discovery over the EMPIRE capability catalog."""

from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP

ROOT = Path(os.environ.get("EMPIRE_ROOT", Path(__file__).resolve().parents[2])).resolve()
CATALOG_DB = Path(os.environ.get("EMPIRE_CATALOG_DB", ROOT / "config" / "eve-capabilities" / "catalog.db")).resolve()
SKILLS_ROOT = Path(os.environ.get("EMPIRE_SKILLS_DIR", ROOT / "eve-skills")).resolve()
MAX_QUERY_CHARS = 200
MAX_MANIFEST_CHARS = 120_000
MAX_LIMIT = 50

mcp = FastMCP("empire-discovery")


def _bounded_text(value: str, field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    value = value.strip()
    if len(value) > MAX_QUERY_CHARS:
        raise ValueError(f"{field} exceeds {MAX_QUERY_CHARS} characters")
    return value


def _limit(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("limit must be an integer")
    if value < 1:
        raise ValueError("limit must be at least 1")
    return min(value, MAX_LIMIT)


def _read_connection() -> sqlite3.Connection:
    if not CATALOG_DB.is_file():
        raise FileNotFoundError(f"Catalog not found: {CATALOG_DB}")
    connection = sqlite3.connect(f"file:{CATALOG_DB.as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only = ON")
    return connection


def _json(payload: object) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, default=str)


def _safe_skill_path(skill_name: str) -> Path:
    name = _bounded_text(skill_name, "skill_name")
    if not name or name in {".", ".."} or "/" in name or "\\" in name:
        raise ValueError("skill_name must be a direct skill directory name")
    candidate = (SKILLS_ROOT / name / "SKILL.md").resolve()
    try:
        candidate.relative_to(SKILLS_ROOT)
    except ValueError as exc:
        raise ValueError("skill path escapes the skills root") from exc
    return candidate


@mcp.tool()
def search_catalog(query: str = "", eve_capability: str = "", limit: int = 15) -> str:
    """Search approved catalog metadata without changing the catalog."""
    query = _bounded_text(query, "query")
    eve_capability = _bounded_text(eve_capability, "eve_capability")
    limit = _limit(limit)
    sql = """
        SELECT id, description, eve_capability, trust_domain, score_local, score_mcp, score_cli
        FROM repositories WHERE 1=1
    """
    params: list[object] = []
    if query:
        sql += " AND (id LIKE ? OR description LIKE ?)"
        params.extend([f"%{query}%", f"%{query}%"])
    if eve_capability:
        sql += " AND eve_capability = ?"
        params.append(eve_capability)
    sql += " ORDER BY score_functional DESC, score_local DESC, id LIMIT ?"
    params.append(limit)
    with _read_connection() as connection:
        rows = [dict(row) for row in connection.execute(sql, params).fetchall()]
    return _json(rows or {"message": "No catalog tools matched the request."})


@mcp.tool()
def inspect_tool_metadata(repo_id: str) -> str:
    """Return full metadata for one exact repository or local skill."""
    repo_id = _bounded_text(repo_id, "repo_id")
    if not repo_id or len(repo_id) > MAX_QUERY_CHARS:
        raise ValueError("repo_id is required")
    with _read_connection() as connection:
        row = connection.execute("SELECT * FROM repositories WHERE id = ?", (repo_id,)).fetchone()
        if row is None:
            return _json({"message": f"Tool with ID '{repo_id}' was not found."})
        result = dict(row)
        result["capabilities"] = [
            item[0] for item in connection.execute(
                "SELECT capability_name FROM capabilities WHERE repo_id = ? ORDER BY capability_name",
                (repo_id,),
            ).fetchall()
        ]
        skill = connection.execute("SELECT * FROM local_skills WHERE repo_id = ?", (repo_id,)).fetchone()
        if skill is not None:
            result["local_skill"] = dict(skill)
    return _json(result)


@mcp.tool()
def load_skill_manifest(skill_name: str) -> str:
    """Read one installed SKILL.md from the direct skills root only."""
    path = _safe_skill_path(skill_name)
    if not path.is_file():
        return _json({"message": f"SKILL.md not found for '{skill_name}'."})
    if path.stat().st_size > MAX_MANIFEST_CHARS:
        raise ValueError("SKILL.md exceeds the manifest size limit")
    return path.read_text(encoding="utf-8")


@mcp.tool()
def search_research_library(keyword: str, limit: int = 5) -> str:
    """Search locally harvested research metadata and abstracts."""
    keyword = _bounded_text(keyword, "keyword")
    if not keyword:
        raise ValueError("keyword is required")
    limit = _limit(limit)
    pattern = f"%{keyword}%"
    with _read_connection() as connection:
        rows = [
            dict(row)
            for row in connection.execute(
                """
                SELECT id, title, authors, published_date, abstract_summary,
                       source_url, local_file_path, retrieved_at
                FROM research_abstracts
                WHERE title LIKE ? OR keywords LIKE ? OR abstract_summary LIKE ?
                ORDER BY retrieved_at DESC, id
                LIMIT ?
                """,
                (pattern, pattern, pattern, limit),
            ).fetchall()
        ]
    return _json(rows or {"message": f"No harvested research matched '{keyword}'."})


@mcp.tool()
def catalog_status() -> str:
    """Return read-only catalog health and row counts."""
    with _read_connection() as connection:
        version = connection.execute("SELECT MAX(version) FROM schema_version").fetchone()[0]
        counts = {}
        for table in ("repositories", "capabilities", "local_skills", "research_abstracts"):
            counts[table] = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    return _json({"ok": True, "database": str(CATALOG_DB), "schema_version": version, "counts": counts})


if __name__ == "__main__":
    mcp.run()