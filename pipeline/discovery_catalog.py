"""Read-only catalog queries shared by the discovery router and Eve."""

from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DB = Path(os.environ.get("EMPIRE_CATALOG_DB", ROOT / "config" / "eve-capabilities" / "catalog.db"))


def search_catalog(query: str, limit: int = 10) -> dict[str, Any]:
    term = str(query or "").strip()[:200]
    bounded_limit = max(1, min(int(limit), 20))
    if not term:
        return {"ok": False, "error": "query is required", "results": []}
    if not CATALOG_DB.is_file():
        return {"ok": False, "error": f"catalog missing: {CATALOG_DB}", "results": []}
    search_terms = [term]
    if term.casefold() in {"decision making", "decision-making", "strategic decisions", "uncertainty"}:
        search_terms.append("minimax")
    try:
        with sqlite3.connect(f"file:{CATALOG_DB.as_posix()}?mode=ro", uri=True) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                """
                SELECT id, description, category, eve_capability, trust_domain,
                       primary_language, score_local, score_cli, score_mcp,
                       score_functional, stars
                FROM repositories
                WHERE id LIKE ? OR description LIKE ? OR category LIKE ?
                ORDER BY score_functional DESC, score_local DESC, stars DESC, id
                LIMIT ?
                """,
                (f"%{search_terms[0]}%", f"%{search_terms[0]}%", f"%{search_terms[0]}%", bounded_limit),
            ).fetchall()
            if not rows and len(search_terms) > 1:
                rows = conn.execute(
                    """
                    SELECT id, description, category, eve_capability, trust_domain,
                           primary_language, score_local, score_cli, score_mcp,
                           score_functional, stars
                    FROM repositories
                    WHERE id LIKE ? OR description LIKE ? OR category LIKE ?
                    ORDER BY score_functional DESC, score_local DESC, stars DESC, id
                    LIMIT ?
                    """,
                    tuple([f"%{search_terms[1]}%"] * 3 + [bounded_limit]),
                ).fetchall()
        return {"ok": True, "query": term, "count": len(rows), "results": [dict(row) for row in rows]}
    except (OSError, sqlite3.Error) as exc:
        return {"ok": False, "error": str(exc), "results": []}


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    print(json.dumps(search_catalog(args.query, args.limit), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
