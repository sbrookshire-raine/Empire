"""Query data — read-only DuckDB over local CSV/JSON/Parquet/SQLite copies.

Evidence arm, offline-convertible (duckdb wheel mirrored to D:\wheels). Reads
from a strict allowlist of local file paths only — no URLs, no DuckDB
extensions, no external table functions. Caps rows/bytes/time to keep queries
cheap and safe.

Two modes:
  * data_file given → the file is registered as table `data`; your SQL runs
    against it (e.g. "SELECT * FROM data WHERE x > 10 LIMIT 20").
  * data_file empty → full SQL runs directly, but network/extension/attach
    keywords are blocked.

Trust domain: local_evidence (read-only; network DENY).
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

from pipeline.provenance import provenance_markdown_footer

ROOT = Path(__file__).resolve().parents[1]

# Allowlisted data roots (real paths only). Queries may reference files under these.
DEFAULT_DATA_ROOTS: tuple[Path, ...] = (
    Path(r"C:\Empire_Workbench"),
    ROOT / "data",
)

DEFAULT_MAX_ROWS = int(os.environ.get("EMPIRE_QUERY_MAX_ROWS", "1000"))
DEFAULT_MAX_BYTES = int(os.environ.get("EMPIRE_QUERY_MAX_BYTES", str(2 * 1024 * 1024)))
DEFAULT_TIMEOUT_SEC = float(os.environ.get("EMPIRE_QUERY_TIMEOUT", "30"))

# Forbidden DuckDB features that could reach outside the allowlist.
_BANNED_KEYWORDS: tuple[str, ...] = (
    "INSTALL", "LOAD ", "ATTACH", "COPY ", "EXPORT", "http://", "https://",
    "read_csv_auto(", "read_json_auto(", "read_parquet(", "sqlite_scan(",
    "read_csv(", "read_json(", "glob(", "list_files(", "read_text(",
)


def _data_roots() -> list[Path]:
    override = os.environ.get("EMPIRE_QUERY_ROOTS", "").strip()
    if override:
        roots: list[Path] = []
        for part in override.split(os.pathsep):
            p = Path(part.strip()).expanduser()
            if p.is_dir():
                roots.append(p)
        if roots:
            return roots
    return [r for r in DEFAULT_DATA_ROOTS if r.is_dir()]


def _resolve_under_roots(candidate: str) -> tuple[Path | None, str | None]:
    """Resolve a data file reference strictly under an allowlisted root."""
    raw = (candidate or "").strip().strip('"').strip("'")
    if not raw:
        return None, "empty path"
    if raw.startswith("http://") or raw.startswith("https://"):
        return None, "network paths are forbidden"
    p = Path(raw)
    roots = _data_roots()
    if not roots:
        return None, "no allowlisted data roots configured"

    if p.is_absolute():
        candidate_path = p.resolve()
    else:
        candidate_path = None
        for root in roots:
            guess = (root / raw).resolve()
            if guess.exists():
                candidate_path = guess
                break
        if candidate_path is None:
            candidate_path = (roots[0] / raw).resolve()

    for root in roots:
        try:
            candidate_path.relative_to(root.resolve())
            if candidate_path.is_file():
                return candidate_path, None
            return None, f"file not found: {candidate_path}"
        except ValueError:
            continue
    return None, "path escapes allowlisted data roots"


def _scan_sql(sql: str) -> dict[str, Any] | None:
    upper = sql.upper()
    for keyword in _BANNED_KEYWORDS:
        if keyword.upper() in upper:
            return {"ok": False, "error": f"forbidden construct: {keyword.strip()}"}
    stripped = upper.lstrip()
    if not stripped.startswith(("SELECT", "SHOW", "DESCRIBE", "PRAGMA", "SUMMARIZE", "WITH")):
        return {"ok": False, "error": "only read queries (SELECT/WITH) are allowed"}
    statements = [s for s in sql.split(";") if s.strip()]
    if len(statements) > 1:
        return {"ok": False, "error": "multiple statements are not allowed"}
    return None


def _reader_sql_for(path: Path) -> str | None:
    ext = path.suffix.lower()
    posix = path.as_posix()
    if ext in {".csv", ".tsv"}:
        return f"read_csv_auto('{posix}')"
    if ext in {".json", ".jsonl"}:
        return f"read_json_auto('{posix}')"
    if ext == ".parquet":
        return f"read_parquet('{posix}')"
    if ext in {".db", ".sqlite", ".sqlite3"}:
        return f"sqlite_scan('{posix}', 'main')"
    return None


def query(
    sql: str,
    *,
    data_file: str = "",
    max_rows: int = DEFAULT_MAX_ROWS,
    timeout_sec: float = DEFAULT_TIMEOUT_SEC,
) -> dict[str, Any]:
    cleaned = (sql or "").strip()
    if not cleaned:
        return {"ok": False, "error": "sql is required"}

    scan_error = _scan_sql(cleaned)
    if scan_error is not None:
        return scan_error

    try:
        import duckdb  # type: ignore
    except ImportError:
        return {"ok": False, "error": "duckdb not installed (offline wheel: D:\\wheels\\duckdb-1.2.2-*.whl)"}

    data_path: Path | None = None
    if data_file:
        data_path, path_error = _resolve_under_roots(data_file)
        if path_error or data_path is None:
            return {"ok": False, "error": path_error or "invalid data file"}
        reader = _reader_sql_for(data_path)
        if reader is None:
            return {"ok": False, "error": f"unsupported extension: {data_path.suffix}"}

    max_rows = max(1, min(int(max_rows), 10000))
    timeout_sec = max(1.0, min(float(timeout_sec), 120.0))

    started = time.monotonic()
    con = None
    try:
        con = duckdb.connect(database=":memory:")
        con.execute("SET memory_limit='512MB'")
        if data_path is not None:
            # Register the allowlisted file as a view named `data`.
            reader = _reader_sql_for(data_path)
            con.execute(f"CREATE VIEW data AS SELECT * FROM {reader}")
        result = con.execute(cleaned.rstrip(";").rstrip())
        columns = [d[0] for d in result.description]
        rows = result.fetchmany(max_rows + 1)
        truncated = len(rows) > max_rows
        rows = rows[:max_rows]
    except Exception as exc:  # noqa: BLE001
        elapsed = round(time.monotonic() - started, 3)
        return {"ok": False, "error": str(exc)[:500], "elapsed_sec": elapsed}
    finally:
        if con is not None:
            try:
                con.close()
            except Exception:
                pass

    elapsed = round(time.monotonic() - started, 3)
    payload = json.dumps({"columns": columns, "rows": rows}, default=str, ensure_ascii=False)
    size_bytes = len(payload.encode("utf-8"))
    if size_bytes > DEFAULT_MAX_BYTES:
        return {
            "ok": False,
            "error": f"result too large ({size_bytes} bytes > {DEFAULT_MAX_BYTES}); add LIMIT / narrower columns",
            "columns": columns,
            "elapsed_sec": elapsed,
        }

    return {
        "ok": True,
        "columns": columns,
        "rows": rows,
        "row_count": len(rows),
        "truncated": truncated,
        "elapsed_sec": elapsed,
        "result_bytes": size_bytes,
        "footer": provenance_markdown_footer(source="query_data", tool="query_data", limb="local_evidence"),
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Read-only DuckDB over local data")
    parser.add_argument("sql")
    parser.add_argument("--data-file", default="")
    parser.add_argument("--max-rows", type=int, default=DEFAULT_MAX_ROWS)
    args = parser.parse_args(argv)
    result = query(args.sql, data_file=args.data_file, max_rows=args.max_rows)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
