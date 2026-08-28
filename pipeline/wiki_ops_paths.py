"""Shared path helpers for Wiki Ops dashboard and maintenance tooling."""

from __future__ import annotations

import os
import re
from pathlib import Path

YEAR_RE = re.compile(r"^\d{4}$")

EMPIRE_DIR = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "EMPIRE"

DEFAULT_REPORTS_ROOT = Path(r"I:\EMPIRE_DATA\wiki-reports")
DEFAULT_LOGS_ROOT = Path(r"I:\EMPIRE_DATA\logs")
DEFAULT_WIKI_MD_ROOT = Path(os.environ.get("WIKI_ROOT", r"D:\wiki_md"))

CORPUS_TOTALS: dict[str, int] = {
    "2017": 5_347_264,
    "2021": 6_300_000,
    "2026": 7_100_000,
}

BATCHES_TOTAL: dict[str, int] = {
    "2017": 535,
    "2021": 126,
    "2026": 143,
}


def validate_year(year: str) -> str:
    text = str(year).strip()
    if not YEAR_RE.fullmatch(text):
        raise ValueError(f"Invalid year {year!r}; expected YYYY")
    return text


def subjects_path() -> Path:
    override = os.environ.get("EMPIRE_PRIORITY_SUBJECTS", "").strip()
    if override:
        return Path(override)
    return EMPIRE_DIR / "priority_subjects.json"


def reports_root() -> Path:
    override = os.environ.get("EMPIRE_WIKI_REPORTS_ROOT", "").strip()
    if override:
        return Path(override)
    return DEFAULT_REPORTS_ROOT


def reports_dir(year: str) -> Path:
    y = validate_year(year)
    return reports_root() / y


def resolved_path(year: str) -> Path:
    override = os.environ.get("EMPIRE_PRIORITY_RESOLVED", "").strip()
    if override:
        return Path(override)
    return reports_dir(year) / "priority_resolved.jsonl"


def status_path(year: str) -> Path:
    return reports_dir(year) / "wiki-status.json"


def pid_path(year: str) -> Path:
    y = validate_year(year)
    return DEFAULT_LOGS_ROOT / f"wiki-ingest-overnight-{y}.pid"


def checkpoint_path() -> Path:
    return EMPIRE_DIR / "wiki-checkpoint.json"


def abort_flag_path() -> Path:
    return EMPIRE_DIR / "wiki-abort.flag"


def wiki_md_root() -> Path:
    return Path(os.environ.get("WIKI_ROOT", str(DEFAULT_WIKI_MD_ROOT)))


def _pid_alive_windows(pid: int) -> bool:
    import ctypes

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if handle:
        ctypes.windll.kernel32.CloseHandle(handle)
        return True
    return False


def overnight_pid_alive(year: str) -> bool:
    path = pid_path(year)
    if not path.exists():
        return False
    try:
        raw = path.read_text(encoding="utf-8").strip()
        pid = int(raw.splitlines()[0].strip())
    except (OSError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name == "nt":
        try:
            return _pid_alive_windows(pid)
        except Exception:  # noqa: BLE001
            pass
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError, PermissionError):
        return False
