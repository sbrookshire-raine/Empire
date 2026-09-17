"""Author code — create/apply a patch in a disposable Git worktree.

Code-autonomy arm. Every change is represented as a reviewable diff in
`eve-worktrees/{run-id}`. Never pushes, merges, or mutates the production
working tree. Runs offline; git is local.

Trust domain: code (disposable worktree; no credentials; reviewable diff only).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKTREE_ROOT = Path(
    os.environ.get("EMPIRE_WORKTREE_DIR", r"C:\EMPIRE\eve-worktrees")
)


def _git(*args: str, cwd: Path) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": str(exc)}
    return {
        "ok": completed.returncode == 0,
        "exit_code": completed.returncode,
        "stdout": (completed.stdout or "").strip(),
        "stderr": (completed.stderr or "").strip(),
    }


def create_worktree(note: str = "") -> dict[str, Any]:
    """Create a fresh disposable worktree checked out at HEAD (no branch detour)."""
    if not (ROOT / ".git").exists():
        return {"ok": False, "error": f"not a git repo: {ROOT}"}
    root = DEFAULT_WORKTREE_ROOT
    try:
        root.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    run_id = uuid.uuid4().hex[:12]
    wt = root / run_id

    # Use `git worktree add --detach` so we never create/switch a named branch.
    result = _git("worktree", "add", "--detach", str(wt), "HEAD", cwd=ROOT)
    if not result["ok"]:
        return {
            "ok": False,
            "error": result.get("stderr") or result.get("stdout") or "worktree add failed",
        }
    return {
        "ok": True,
        "run_id": run_id,
        "worktree": str(wt),
        "note": (note or "").strip(),
    }


def remove_worktree(worktree: str) -> dict[str, Any]:
    wt = Path(worktree)
    result = _git("worktree", "remove", "--force", str(wt), cwd=ROOT)
    if result["ok"]:
        result = _git("worktree", "prune", cwd=ROOT)
    return {
        "ok": result["ok"],
        "worktree": str(wt),
        "error": result.get("stderr") or result.get("stdout"),
    }


def apply_patch(
    *,
    worktree: str,
    relative_path: str,
    content: str,
) -> dict[str, Any]:
    """Write a file inside a disposable worktree and return its diff."""
    wt = Path(worktree)

    # Resolve relative path safety first (defense in depth), independent of
    # whether the worktree currently exists.
    rel = (relative_path or "").strip().strip("/\\")
    if not rel or ".." in Path(rel).parts or rel.startswith("/") or re_abs(rel):
        return {"ok": False, "error": "relative_path must stay inside the worktree"}

    # Skip credential-like paths even inside the worktree.
    lowered = rel.lower()
    if any(bad in lowered for bad in (".env", "id_rsa", "credentials", ".ssh/")):
        return {"ok": False, "error": "credential-like path is not allowed"}

    if not wt.is_dir():
        return {"ok": False, "error": f"worktree not found: {wt}"}

    target = (wt / rel).resolve()
    try:
        target.relative_to(wt.resolve())
    except ValueError:
        return {"ok": False, "error": "relative_path escapes the worktree"}

    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    diff = _git("diff", "--", rel, cwd=wt)
    if not diff["ok"]:
        return {"ok": False, "error": diff.get("stderr") or diff.get("stdout") or "diff failed"}
    # For a brand-new untracked file, `git diff` is empty; show it as an add.
    diff_text = diff["stdout"]
    if not diff_text.strip():
        status = _git("status", "--porcelain", "--", rel, cwd=wt)
        if "??" in status["stdout"]:
            diff_text = _git("diff", "--no-index", "/dev/null", str(target), cwd=wt).get("stdout", "")

    return {
        "ok": True,
        "worktree": str(wt),
        "relative_path": rel,
        "diff": diff_text,
    }


def re_abs(rel: str) -> bool:
    """True if a Windows or POSIX absolute path."""
    return bool(rel.startswith(("\\", "/"))) or (len(rel) > 1 and rel[1] == ":")


def main(argv: list[str] | None = None) -> int:
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Disposable Git worktree code authoring")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("create", help="Create a disposable worktree").add_argument("--note", default="")

    rem = sub.add_parser("remove", help="Remove a disposable worktree")
    rem.add_argument("worktree")

    app = sub.add_parser("apply", help="Write a file and emit its diff")
    app.add_argument("worktree")
    app.add_argument("relative_path")
    app.add_argument("content")

    args = parser.parse_args(argv)
    if args.cmd == "create":
        out = create_worktree(note=args.note)
    elif args.cmd == "remove":
        out = remove_worktree(args.worktree)
    elif args.cmd == "apply":
        out = apply_patch(worktree=args.worktree, relative_path=args.relative_path, content=args.content)
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
