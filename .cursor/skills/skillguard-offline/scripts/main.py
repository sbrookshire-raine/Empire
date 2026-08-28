#!/usr/bin/env python3
"""skillguard-offline: invoke SkillGuard (or print install guidance).

Zero LLM. Scans Cursor skill trees before enablement.
Upstream: https://github.com/yangyixxxx/skillguard
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path


def check_install() -> dict:
    module_ok = importlib.util.find_spec("skillguard") is not None
    cli = shutil.which("skillguard")
    return {
        "ok": module_ok or bool(cli),
        "module": module_ok,
        "cli": cli,
        "hint": "pip install skillguard — https://github.com/yangyixxxx/skillguard",
    }


def run_scan(target: Path) -> int:
    target = target.resolve()
    if not target.exists():
        print(json.dumps({"ok": False, "error": f"missing path: {target}"}))
        return 2

    cli = shutil.which("skillguard")
    candidates: list[list[str]] = []
    if cli:
        candidates.append([cli, str(target)])
    candidates.append([sys.executable, "-m", "skillguard", str(target)])
    candidates.append([sys.executable, "-m", "skillguard.cli", str(target)])

    last_err = ""
    for cmd in candidates:
        try:
            proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
        except OSError as exc:
            last_err = str(exc)
            continue
        sys.stdout.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        if proc.returncode == 0 or proc.stdout or proc.stderr:
            return proc.returncode
        last_err = proc.stderr or f"exit {proc.returncode}"

    print(
        json.dumps(
            {
                "ok": False,
                "error": "skillguard not runnable",
                "detail": last_err,
                "hint": "Install from https://github.com/yangyixxxx/skillguard then re-run",
                "target": str(target),
            },
            indent=2,
        )
    )
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="EMPIRE SkillGuard offline helper")
    parser.add_argument("target", nargs="?", type=Path, help="Skill dir or SKILL.md")
    parser.add_argument("--check-install", action="store_true")
    args = parser.parse_args()

    if args.check_install or args.target is None:
        info = check_install()
        print(json.dumps(info, indent=2))
        if args.target is None:
            return 0 if info["ok"] else 1

    return run_scan(args.target)


if __name__ == "__main__":
    raise SystemExit(main())
