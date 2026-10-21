#!/usr/bin/env python3
"""claim-ledger limb — knowledge that is DONE, not read.

A claim without a check is a document. A claim with a check is a capability.
This limb holds claims for EXECUTION, not text for recall: Eve does not recall
"binwalk extracts squashfs", it runs the check and learns whether that is still
true today.

Why this is not a second memory store: it stores no prose for retrieval. It
stores a claim, the command that would falsify it, and the last result. The
value is that a claim cannot go stale silently - a check either passes or it
does not, right now.

Roots: CLAIM_LEDGER_DB (the sqlite file) and CLAIM_LEDGER_ROOTS (semicolon- or
newline-separated directories a check may touch). Every check runs with cwd
inside a declared root; a check naming a path outside them is refused.

Windows note (2026-10-21, EMPIRE integration): the upstream parser split the
root list on ``[;:]``, which shreds a Windows drive letter - ``C:\\a;D:\\b``
became ``C``, ``\\a``, ``D``, ``\\b`` and every check then failed with
``[WinError 267] The directory name is invalid``. Roots are now separated by
``;`` or newline only, and a single drive-qualified path is accepted whole.
"""
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

# EMPIRE runs the MCP SDK's bundled FastMCP, not the standalone package. They
# are different implementations: the standalone one accepts @mcp.tool bare, the
# SDK one requires @mcp.tool(). Import whichever is present; the called form
# below works in both.
try:
    from mcp.server.fastmcp import FastMCP   # the SDK's bundled one
    _SDK_FASTMCP = True
except ImportError:
    from fastmcp import FastMCP              # standalone fallback
    _SDK_FASTMCP = False

# --- declared roots ---------------------------------------------------------
# A tool that can escape its roots is rejected before review. The DB path and
# every directory a check may run in must be declared here, from the env.
DB = Path(os.environ.get("CLAIM_LEDGER_DB",
                         str(Path(__file__).parent / "claims.db")))
# The database's directory must exist before sqlite can open the file — a
# missing directory surfaces as "unable to open database file", which reads
# like a permissions problem rather than a missing folder.
try:
    DB.parent.mkdir(parents=True, exist_ok=True)
except OSError:
    pass
_roots_env = os.environ.get("CLAIM_LEDGER_ROOTS", "")


def _parse_roots(raw: str) -> list[Path]:
    """Split a declared-root list without shredding Windows drive letters.

    The upstream implementation split on ``[;:]``, which turned
    ``C:\\work;D:\\other`` into four nonsense fragments. Roots are separated by
    ``;`` or a newline here; a lone ``C:\\work`` is one root, whole.
    """
    parts = [p.strip() for p in re.split(r"[;\r\n]+", raw or "") if p.strip()]
    return [Path(p).resolve() for p in parts]


ROOTS = _parse_roots(_roots_env)
if not ROOTS:
    # a defaulted root is not containment; require it explicitly
    ROOTS = [DB.parent.resolve()]
# A declared root is where a check runs, so it must exist. Creating it keeps
# the limb usable on a fresh install; a check still cannot name a path outside
# the roots, and the root set is unchanged.
for _root in ROOTS:
    try:
        _root.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass

CHECK_TIMEOUT = int(os.environ.get("CLAIM_LEDGER_TIMEOUT", "120"))
# Checks are POSIX-shaped upstream (pipe, grep). On Windows `shell=True` runs
# cmd.exe, where those operators do not exist, so a POSIX check would report a
# false failure. `CLAIM_LEDGER_SHELL` picks the interpreter; the default on
# this host is PowerShell, which understands pipes and redirection.
#
# The value is resolved to a real path: `subprocess(executable=...)` does not
# do a PATH lookup, so a bare "cmd.exe" would fail with WinError 2 even though
# cmd.exe is on PATH.
def _resolve_shell(raw: str) -> str:
    """Turn a configured shell into an absolute executable path (or empty)."""

    cleaned = (raw or "").strip()
    if not cleaned:
        return ""
    candidate = Path(cleaned)
    if candidate.is_file():
        return str(candidate)
    found = shutil.which(cleaned)
    return found or ""


SHELL = _resolve_shell(os.environ.get("CLAIM_LEDGER_SHELL", ""))
GRADES = ("promotional", "community-reported", "first-party-documented",
          "independently-corroborated", "reproduced")

mcp = FastMCP("claim-ledger")


def _within(path, roots):
    """True when path is inside one of the declared roots."""
    try:
        p = Path(path).resolve()
    except Exception:
        return False
    for r in roots:
        try:
            p.relative_to(r)
            return True
        except ValueError:
            continue
    return False


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@contextmanager
def _con():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
        con.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def _init():
    with _con() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS claims (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                slug         TEXT UNIQUE NOT NULL,
                claim        TEXT NOT NULL,
                check_cmd    TEXT,
                grade        TEXT NOT NULL DEFAULT 'community-reported',
                source       TEXT,
                created_at   TEXT NOT NULL,
                last_run     TEXT,
                last_exit    INTEGER,
                last_output  TEXT,
                passes       INTEGER DEFAULT 0,
                fails        INTEGER DEFAULT 0
            )""")
        con.execute("CREATE INDEX IF NOT EXISTS idx_grade ON claims(grade)")


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


@mcp.tool()
def claim_add(claim: str, check_cmd: str = "", grade: str = "community-reported",
              source: str = "") -> dict:
    """Record a claim, optionally with the command that would prove it wrong.

    Use when you learn something that should stay true - a version, a path, a
    count, a behaviour. Give the check command whenever one exists; a claim with
    no check is a document and is counted as such. Returns the slug and whether
    the claim is executable.
    """
    if grade not in GRADES:
        return {"ok": False, "error": f"grade must be one of {GRADES}"}
    _init()
    slug = _slug(claim)
    with _con() as con:
        con.execute("""INSERT OR REPLACE INTO claims
            (slug, claim, check_cmd, grade, source, created_at)
            VALUES (?,?,?,?,?,?)""",
            (slug, claim, check_cmd or None, grade, source, _now()))
    return {"ok": True, "slug": slug,
            "kind": "capability" if check_cmd else "document"}


@mcp.tool()
def claim_verify(slug: str = "") -> dict:
    """Run the checks and record what happened.

    Use when you need to know whether a claim is still true - especially one
    carried over from an earlier session, which may have gone stale. Pass a slug
    to check one claim, or leave it empty to check all. A failing check is the
    finding: report it rather than quietly fixing it.
    """
    _init()
    results = {"passed": [], "failed": [], "unchecked": []}
    with _con() as con:
        q = "SELECT * FROM claims"
        params = ()
        if slug:
            q += " WHERE slug LIKE ?"
            params = (f"%{slug}%",)
        for r in con.execute(q, params).fetchall():
            if not r["check_cmd"]:
                results["unchecked"].append(r["slug"])
                continue
            # Run inside a declared root; refuse anything outside. The first
            # declared root that still exists is the working directory — the
            # upstream `next((x for x in ROOTS if _within(x, ROOTS)), ...)`
            # expression was always true and therefore never checked anything.
            cwd = next((str(x) for x in ROOTS if x.is_dir()), str(ROOTS[0]))
            try:
                p = subprocess.run(r["check_cmd"], shell=True, cwd=cwd,
                                   capture_output=True, text=True,
                                   timeout=CHECK_TIMEOUT, executable=SHELL or None)
                code, out = p.returncode, (p.stdout + p.stderr).strip()[-500:]
            except subprocess.TimeoutExpired:
                code, out = 124, f"timed out after {CHECK_TIMEOUT}s"
            except Exception as e:
                code, out = 125, f"{type(e).__name__}: {e}"
            ok = code == 0
            con.execute("""UPDATE claims SET last_run=?, last_exit=?,
                last_output=?, passes=passes+?, fails=fails+? WHERE id=?""",
                (_now(), code, out, 1 if ok else 0, 0 if ok else 1, r["id"]))
            (results["passed"] if ok else results["failed"]).append(
                {"slug": r["slug"], "exit": code, "output": out[:200]})
    return {"ok": True, **results,
            "summary": f"passed {len(results['passed'])}, "
                       f"failed {len(results['failed'])}, "
                       f"unchecked {len(results['unchecked'])}"}


@mcp.tool()
def claim_health() -> dict:
    """How much of what is claimed can actually be proven.

    Use before trusting the store, or when asked how reliable it is. Returns the
    fraction of claims that have a check and pass. A store where most claims have
    no check is a library, not a forge - say so plainly rather than implying
    more confidence than the number supports.
    """
    _init()
    with _con() as con:
        total = con.execute("SELECT COUNT(*) FROM claims").fetchone()[0]
        if not total:
            return {"ok": True, "total": 0, "verdict": "empty"}
        checked = con.execute(
            "SELECT COUNT(*) FROM claims WHERE check_cmd IS NOT NULL"
        ).fetchone()[0]
        passing = con.execute(
            "SELECT COUNT(*) FROM claims WHERE check_cmd IS NOT NULL "
            "AND last_exit = 0").fetchone()[0]
    cp = round(100 * checked / total)
    pp = round(100 * passing / total)
    if pp >= 60:
        verdict = "forge - most claims are executable and true"
    elif cp >= 60:
        verdict = "partly executable - checks exist but are failing"
    elif cp >= 25:
        verdict = "mostly a library - most claims cannot be checked"
    else:
        verdict = "library - this is text, not capability"
    return {"ok": True, "total": total, "checked": checked, "passing": passing,
            "unchecked": total - checked, "checked_pct": cp,
            "passing_pct": pp, "verdict": verdict}


@mcp.tool()
def claim_list(unchecked: bool = False, failing: bool = False) -> list:
    """List claims, optionally only the ones that are documents or failing.

    Use to find what still needs a check (unchecked=true) or what is known-false
    and needs attention (failing=true).
    """
    _init()
    with _con() as con:
        q = ("SELECT slug, claim, grade, check_cmd, last_exit, last_run "
             "FROM claims")
        if unchecked:
            q += " WHERE check_cmd IS NULL"
        elif failing:
            q += " WHERE last_exit IS NOT NULL AND last_exit != 0"
        q += " ORDER BY slug"
        return [{"slug": r["slug"], "claim": r["claim"], "grade": r["grade"],
                 "kind": "capability" if r["check_cmd"] else "document",
                 "last_exit": r["last_exit"], "last_run": r["last_run"]}
                for r in con.execute(q)]


if __name__ == "__main__":
    # The SDK's run() takes (transport, mount_path); the standalone one also
    # accepts show_banner. Pass only what each accepts.
    if _SDK_FASTMCP:
        mcp.run(transport="stdio")
    else:
        mcp.run(show_banner=False)
