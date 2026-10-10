"""REA analysis inbox — local uploads for reverse-engineering (no Cognee).

Architect drops binaries, zips, ASAR, or web bundles via the Eve chat composer.
Files land under Empire_Workbench/rea_inbox/; Eve receives absolute paths in the
session message and via rea_list_inbox.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import uuid
import zipfile
from datetime import datetime, timezone
from email.message import Message
from pathlib import Path
from typing import Any, TypedDict

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
WORKBENCH = Path(os.environ.get("EMPIRE_WORKBENCH_ROOT", r"C:\Empire_Workbench"))
INBOX_ROOT = WORKBENCH / "rea_inbox"
FALLBACK_INBOX = EMPIRE_ROOT / "data" / "rea_inbox"

MAX_FILES = 8
MAX_FILE_BYTES = int(os.environ.get("EMPIRE_REA_MAX_FILE_BYTES", str(200 * 1024 * 1024)))
MAX_REQUEST_BYTES = int(os.environ.get("EMPIRE_REA_MAX_REQUEST_BYTES", str(220 * 1024 * 1024)))

ALLOWED_SUFFIXES = frozenset(
    {
        ".zip",
        ".7z",
        ".exe",
        ".dll",
        ".bin",
        ".apk",
        ".asar",
        ".js",
        ".mjs",
        ".cjs",
        ".json",
        ".wasm",
        ".html",
        ".htm",
        ".node",
        ".msi",
        ".dmg",
        ".so",
        ".dylib",
        ".dat",
    }
)

SAFE_FILENAME_RE = re.compile(r"[^A-Za-z0-9._-]+")
BUNDLE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{8,64}$")


class ReaFileRow(TypedDict, total=False):
    name: str
    path: str
    size: int
    kind: str


class ReaBundle(TypedDict, total=False):
    id: str
    created_at: str
    label: str
    files: list[ReaFileRow]
    analysis_roots: list[str]
    notes: list[str]


def inbox_root() -> Path:
    root = INBOX_ROOT
    try:
        root.mkdir(parents=True, exist_ok=True)
        return root
    except OSError:
        FALLBACK_INBOX.mkdir(parents=True, exist_ok=True)
        return FALLBACK_INBOX


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sanitize_filename(name: str) -> str:
    base = Path(name or "upload").name
    cleaned = SAFE_FILENAME_RE.sub("_", base).strip("._")
    if not cleaned:
        cleaned = "upload"
    if len(cleaned) > 180:
        stem = Path(cleaned).stem[:120]
        suffix = Path(cleaned).suffix[:20]
        cleaned = f"{stem}{suffix}"
    return cleaned


def _validate_suffix(name: str) -> None:
    suffix = Path(name).suffix.lower()
    if suffix not in ALLOWED_SUFFIXES:
        allowed = ", ".join(sorted(ALLOWED_SUFFIXES))
        raise ValueError(f"{name}: type not allowed for REA inbox ({allowed}).")


def _safe_extract_zip(zip_path: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    resolved_dest = dest.resolve()
    with zipfile.ZipFile(zip_path, "r") as archive:
        for member in archive.namelist():
            if member.endswith("/"):
                continue
            target = (dest / member).resolve()
            if not str(target).startswith(str(resolved_dest)):
                raise ValueError("Zip archive contains unsafe paths.")
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as src, target.open("wb") as out:
                shutil.copyfileobj(src, out)


def _discover_analysis_roots(bundle_dir: Path) -> list[str]:
    roots: list[str] = []
    extracted = bundle_dir / "extracted"
    if extracted.is_dir():
        children = [p for p in extracted.iterdir() if p.name not in {".DS_Store"}]
        if len(children) == 1 and children[0].is_dir():
            roots.append(str(children[0].resolve()))
        else:
            roots.append(str(extracted.resolve()))
    for path in sorted(bundle_dir.iterdir()):
        if path.name in {"manifest.json", "extracted"}:
            continue
        if path.is_dir():
            roots.append(str(path.resolve()))
        elif path.suffix.lower() in {".asar", ".html", ".htm", ".js", ".exe", ".dll", ".apk", ".wasm"}:
            roots.append(str(path.resolve()))
    # De-dupe while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for item in roots:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique


def _write_manifest(bundle_dir: Path, bundle: ReaBundle) -> None:
    path = bundle_dir / "manifest.json"
    path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False), encoding="utf-8")


def save_multipart_upload(parts: list[Message], *, label: str = "") -> ReaBundle:
    if not parts:
        raise ValueError("Choose at least one file to upload for analysis.")
    if len(parts) > MAX_FILES:
        raise ValueError(f"Choose {MAX_FILES} files or fewer per upload.")

    bundle_id = uuid.uuid4().hex[:12]
    bundle_dir = inbox_root() / bundle_id
    bundle_dir.mkdir(parents=True, exist_ok=False)

    rows: list[ReaFileRow] = []
    notes: list[str] = []
    total_bytes = 0

    for part in parts:
        filename = part.get_filename()
        if not filename:
            continue
        safe_name = sanitize_filename(filename)
        _validate_suffix(safe_name)
        payload = part.get_payload(decode=True) or b""
        size = len(payload)
        if size <= 0:
            raise ValueError(f"{safe_name} is empty.")
        if size > MAX_FILE_BYTES:
            raise ValueError(f"{safe_name} exceeds REA inbox size limit.")
        total_bytes += size
        if total_bytes > MAX_REQUEST_BYTES:
            raise ValueError("Combined upload exceeds REA inbox request limit.")

        target = bundle_dir / safe_name
        target.write_bytes(payload)
        kind = "archive" if target.suffix.lower() == ".zip" else "file"
        rows.append(
            {
                "name": safe_name,
                "path": str(target.resolve()),
                "size": size,
                "kind": kind,
            }
        )
        if target.suffix.lower() == ".zip":
            extract_dir = bundle_dir / "extracted"
            _safe_extract_zip(target, extract_dir)
            notes.append(f"Extracted {safe_name} to {extract_dir}.")

    if not rows:
        shutil.rmtree(bundle_dir, ignore_errors=True)
        raise ValueError("No valid files in upload.")

    analysis_roots = _discover_analysis_roots(bundle_dir)
    bundle: ReaBundle = {
        "id": bundle_id,
        "created_at": _utc_now(),
        "label": (label or "").strip() or f"REA upload ({len(rows)} file(s))",
        "files": rows,
        "analysis_roots": analysis_roots,
        "notes": notes,
    }
    _write_manifest(bundle_dir, bundle)
    return bundle


def _manifest_path(bundle_id: str) -> Path:
    if not BUNDLE_ID_RE.match(bundle_id):
        raise ValueError("Unknown upload id.")
    return inbox_root() / bundle_id / "manifest.json"


def read_bundle(bundle_id: str) -> ReaBundle:
    path = _manifest_path(bundle_id)
    if not path.is_file():
        raise KeyError(bundle_id)
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Corrupt REA upload manifest.")
    return raw  # type: ignore[return-value]


def public_bundle(bundle: ReaBundle) -> dict[str, Any]:
    return {
        "id": bundle.get("id"),
        "created_at": bundle.get("created_at"),
        "label": bundle.get("label"),
        "files": [
            {"name": f.get("name"), "size": f.get("size"), "kind": f.get("kind")}
            for f in bundle.get("files") or []
            if isinstance(f, dict)
        ],
        "analysis_roots": list(bundle.get("analysis_roots") or []),
        "notes": list(bundle.get("notes") or []),
    }


def list_bundles(*, limit: int = 20) -> list[dict[str, Any]]:
    root = inbox_root()
    if not root.is_dir():
        return []
    dirs = sorted(
        (p for p in root.iterdir() if p.is_dir()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    out: list[dict[str, Any]] = []
    for entry in dirs[: max(1, min(limit, 50))]:
        manifest = entry / "manifest.json"
        if not manifest.is_file():
            continue
        try:
            bundle = json.loads(manifest.read_text(encoding="utf-8"))
            if isinstance(bundle, dict):
                out.append(public_bundle(bundle))  # type: ignore[arg-type]
        except (OSError, json.JSONDecodeError, ValueError):
            continue
    return out


def resolve_read_path(candidate: str) -> tuple[Path | None, str | None]:
    raw = (candidate or "").strip().strip('"').strip("'")
    if not raw:
        return None, "path is required"
    if raw.startswith("http://") or raw.startswith("https://"):
        return None, "use browser tools for http(s) URLs"
    path = Path(raw)
    if not path.is_absolute():
        return None, "path must be absolute"
    resolved = path.resolve()
    allowed_roots = [inbox_root().resolve(), WORKBENCH.resolve()]
    for root in allowed_roots:
        try:
            resolved.relative_to(root)
            if not resolved.is_file():
                return None, "path is not a file"
            return resolved, None
        except ValueError:
            continue
    return None, "path must be under the REA inbox or Empire_Workbench"


REA_UPLOAD_MARKER = "[[EMPIRE_REA_UPLOADS]]"


def context_block_for_upload_ids(upload_ids: list[str]) -> str:
    bundles: list[dict[str, Any]] = []
    for upload_id in upload_ids:
        cleaned = str(upload_id or "").strip()
        if not cleaned:
            continue
        try:
            bundles.append(public_bundle(read_bundle(cleaned)))
        except (KeyError, ValueError, OSError, json.JSONDecodeError):
            bundles.append({"id": cleaned, "error": "upload not found"})
    if not bundles:
        return ""
    body = json.dumps({"uploads": bundles}, ensure_ascii=False)
    return (
        f"\n\n{REA_UPLOAD_MARKER}\n"
        "The Architect attached local file(s) for reverse engineering. "
        "Use these absolute analysis_roots — do not ask them to copy files elsewhere. "
        "Start with rea_doctor, then rea_analyze_javascript for JS/Electron folders or rea_invoke for native. "
        "For UI behavior of a local HTML/Electron surface, use app_visual_observe with html_path or an allowlisted URL.\n"
        f"{body}"
    )


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE REA inbox")
    sub = parser.add_subparsers(dest="cmd", required=True)
    list_cmd = sub.add_parser("list", help="List recent uploads")
    list_cmd.add_argument("--limit", type=int, default=20)
    show = sub.add_parser("show", help="Show one upload")
    show.add_argument("bundle_id")
    args = parser.parse_args(argv)
    if args.cmd == "list":
        print(json.dumps({"ok": True, "uploads": list_bundles(limit=args.limit)}, indent=2))
        return 0
    if args.cmd == "show":
        bundle = read_bundle(args.bundle_id)
        print(json.dumps({"ok": True, "upload": public_bundle(bundle)}, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
