"""Primitives curated dashboard API (file list + last ingest status)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "data" / "curated_primitives"
RAW = CURATED / "raw_materials"
DIRECTIVES = CURATED / "directives"
STATUS = CURATED / "status" / "last_ingest.json"


def _list_dir(path: Path) -> list[dict[str, Any]]:
    if not path.is_dir():
        return []
    items: list[dict[str, Any]] = []
    for p in sorted(path.iterdir()):
        if p.name.startswith("."):
            continue
        items.append(
            {
                "name": p.name,
                "path": str(p),
                "bytes": p.stat().st_size if p.is_file() else None,
                "kind": "dir" if p.is_dir() else "file",
            }
        )
    return items


def primitives_status() -> dict[str, Any]:
    last: dict[str, Any] = {}
    if STATUS.exists():
        try:
            last = json.loads(STATUS.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            last = {"ok": False, "error": "unreadable last_ingest.json"}
    return {
        "ok": True,
        "dataset": "primitives_test",
        "raw_materials": str(RAW),
        "directives": str(DIRECTIVES),
        "system_prompt": str(DIRECTIVES / "SYSTEM.md"),
        "fuel": _list_dir(RAW),
        "directive_files": _list_dir(DIRECTIVES),
        "last_ingest": last,
        "readme": str(CURATED / "README.md"),
    }


def primitives_run_ingest(*, skip_cognify: bool = False) -> dict[str, Any]:
    ps1 = ROOT / "scripts" / "ingest-curated-primitives.ps1"
    if not ps1.exists():
        raise FileNotFoundError(str(ps1))
    cmd = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(ps1),
    ]
    if skip_cognify:
        cmd.append("-SkipCognify")
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60 * 60 * 3,
    )
    status = primitives_status()
    status["run"] = {
        "exit_code": proc.returncode,
        "stdout_tail": (proc.stdout or "")[-4000:],
        "stderr_tail": (proc.stderr or "")[-2000:],
    }
    status["ok"] = proc.returncode == 0
    return status
