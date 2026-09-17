"""Python verify — syntax + lint + tests in a disposable worktree.

Code-autonomy arm. Verifies Python changes in `eve-worktrees/{run-id}` with no
inherited secrets and no production mutation. Uses stdlib (py_compile +
unittest) always; uses `ruff` and `pytest` when present (optional fast path).
Returns a diff + report; never merges or pushes.

Trust domain: code (disposable worktree; no credentials; reviewable output only).
"""

from __future__ import annotations

import argparse
import json
import os
import py_compile
import subprocess
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKTREE_ROOT = Path(
    os.environ.get("EMPIRE_WORKTREE_DIR", r"C:\EMPIRE\eve-worktrees")
)


def _run(cmd: list[str], cwd: Path, timeout: float = 180) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": str(exc), "exit_code": -1, "stdout": "", "stderr": ""}
    return {
        "ok": completed.returncode == 0,
        "exit_code": completed.returncode,
        "stdout": (completed.stdout or "").strip(),
        "stderr": (completed.stderr or "").strip(),
    }


def _find_python_files(worktree: Path) -> list[Path]:
    out: list[Path] = []
    for p in worktree.rglob("*.py"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        out.append(p)
    return out


def _syntax_check(worktree: Path) -> dict[str, Any]:
    files = _find_python_files(worktree)
    errors: list[str] = []
    for p in files:
        try:
            py_compile.compile(str(p), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"{p.name}: {exc}")
        except OSError as exc:
            errors.append(f"{p.name}: {exc}")
    return {
        "ok": len(errors) == 0,
        "files_checked": len(files),
        "errors": errors,
    }


def verify(
    *,
    worktree: str,
    run_tests: bool = True,
) -> dict[str, Any]:
    wt = Path(worktree)
    if not wt.is_dir():
        return {"ok": False, "error": f"worktree not found: {wt}"}

    report: dict[str, Any] = {}

    # 1) Syntax check (always, stdlib).
    syntax = _syntax_check(wt)
    report["syntax"] = syntax

    # 2) Ruff lint (optional fast path).
    if shutil.which("ruff"):
        lint = _run(["ruff", "check", "--no-cache", "."], cwd=wt)
        report["ruff"] = {
            "ok": lint["ok"],
            "exit_code": lint["exit_code"],
            "output": (lint["stderr"] or lint["stdout"])[:2000],
        }
    else:
        report["ruff"] = {"available": False, "note": "ruff not installed — skipped"}

    # 3) Tests (optional).
    if run_tests:
        if shutil.which("pytest"):
            tests = _run(["pytest", "-q", "."], cwd=wt)
            report["pytest"] = {
                "ok": tests["ok"],
                "exit_code": tests["exit_code"],
                "output": (tests["stdout"] or tests["stderr"])[:2000],
            }
        else:
            # stdlib unittest fallback (best effort over discoverable tests dir).
            ut = _run(
                [
                    "python", "-m", "unittest",
                    "discover", "-s", "tests", "-t", ".",
                ],
                cwd=wt,
                timeout=300,
            )
            report["unittest"] = {
                "ok": ut["ok"],
                "exit_code": ut["exit_code"],
                "output": (ut["stdout"] or ut["stderr"])[:2000],
            }

    overall = bool(syntax["ok"]) and bool(report.get("ruff", {}).get("ok", True))
    return {
        "ok": overall,
        "worktree": str(wt),
        "report": report,
    }


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Verify Python in a disposable worktree")
    parser.add_argument("worktree")
    parser.add_argument("--no-tests", action="store_true")
    args = parser.parse_args(argv)
    result = verify(worktree=args.worktree, run_tests=not args.no_tests)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
