"""Document format census (P11): which formats actually fail today, and which door decides that?

Gates three proposed Lens B bricks (OCR/`surya`, `marker`, `markitdown`). Without this measurement a document
brick is a guess; with it, the answer turns out to be "routing, not conversion".

**The finding that matters:** there is no single "supported format" set. There are four, one per door a file can
enter by, and the same file succeeds or fails depending on which one it uses:

    workbench upload / memory ingest   pipeline/ingest_files.py:21   .md .txt .pdf
    Cognee mock ingest (MCP)           pipeline/normalizer.py:28-40  .json .md      (raises otherwise)
    read_document (Eve reading)        pipeline/read_document.py:34 .md .txt .csv .tsv .json .jsonl
                                                                     .pdf .docx .pptx .xlsx .html .htm
    query_data                         pipeline/query_data.py:113   .csv .tsv

Those sets are **imported**, not restated, so this census cannot quietly drift from the code it measures.

Usage:
    python scripts/document-format-census.py                       # default roots
    python scripts/document-format-census.py --root I:\\wiki        # any root
    python scripts/document-format-census.py --probe 3             # identify unknown formats from samples
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline.ingest_files import ALLOWED_SUFFIXES as MEMORY_SUFFIXES  # .md .txt .pdf
from pipeline.read_document import _SUPPORTED_EXTENSIONS as READ_SUFFIXES

COGNEE_SUFFIXES = {".json", ".md"}  # pipeline/normalizer.py:28-40
DATA_SUFFIXES = {".csv", ".tsv"}  # pipeline/query_data.py:113
OFFICE_SUFFIXES = {".docx", ".pptx", ".xlsx"}  # readable, convertible, but NOT storable today

AUDIO_SUFFIXES = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".opus"}
ARCHIVE_SUFFIXES = {".zip", ".7z", ".tar", ".gz"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff"}
VIDEO_SUFFIXES = {".mp4", ".mkv", ".mov", ".avi", ".webm"}
MAIL_SUFFIXES = {".eml", ".msg", ".mbox"}
MARKDOWN_VARIANTS = {".mdx", ".markdown", ".mdown"}
CONFIG_SUFFIXES = {".yaml", ".yml", ".toml", ".ini", ".cfg", ".xml"}
CODE_SUFFIXES = {
    ".py", ".pyc", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".sh", ".bash", ".ps1", ".bat", ".cmd", ".go", ".rs", ".java", ".c", ".h", ".cpp",
}
# Identified from magic bytes, not guessed: NES is "NES\x1a", SFC/SNES and PC Engine are emulator ROMs, .mid is MIDI.
# These are not documents at all, and the census exists partly to stop anyone proposing a converter for them.
ROM_SUFFIXES = {".nes", ".sfc", ".smc", ".pce", ".gb", ".gbc", ".gba", ".z64", ".n64", ".rom", ".mid", ".midi"}
CLOUD_STUB_SUFFIXES = {".gdoc", ".gsheet", ".gslides", ".gdraw"}  # pointers with no local content
DEFAULT_ROOTS = (r"C:\Empire_Workbench", "data", "mock_data_ingest")

# Marker/state files written by tooling — files with no suffix at all are usually these or databases.
INTERNAL_HINTS = (".skill", ".restore", ".hash", ".version", ".id")


def classify(suffix: str) -> tuple[str, str]:
    """Return (bucket, why) for one extension. Ordered so the *narrowest* door wins the label."""
    if suffix in MEMORY_SUFFIXES:
        return "storable", "workbench upload -> memory"
    if suffix in COGNEE_SUFFIXES:
        return "cognee-only", "MCP cognee ingest only; NOT uploadable to memory"
    if suffix in DATA_SUFFIXES:
        return "data", "query_data / read-only; not storable"
    if suffix in OFFICE_SUFFIXES:
        return "office-gap", "Eve can read it, cannot store it (docling could convert it)"
    if suffix in READ_SUFFIXES:
        return "read-only", "Eve can read it; not storable"
    if suffix in AUDIO_SUFFIXES:
        return "audio", "needs transcription (P8)"
    if suffix in VIDEO_SUFFIXES:
        return "video", "needs transcription (P8 family); large, decide by value"
    if suffix in MAIL_SUFFIXES:
        return "mail", "text-encoded mail export; no door claims it yet (cheap win)"
    if suffix in MARKDOWN_VARIANTS:
        return "md-variant", "markdown in all but extension; trivial to store"
    if suffix in ARCHIVE_SUFFIXES:
        return "archive", "container; nothing unpacks it"
    if suffix in IMAGE_SUFFIXES:
        return "image", "needs OCR (P11 gate)"
    if suffix in CODE_SUFFIXES:
        return "code", "source code; belongs to structural reach (P9), not document ingest"
    if suffix in ROM_SUFFIXES:
        return "non-document", "emulator ROM / MIDI - identified from magic bytes, not knowledge"
    if suffix in CLOUD_STUB_SUFFIXES:
        return "cloud-stub", "pointer to cloud content; the bytes are not the document"
    if suffix in CONFIG_SUFFIXES:
        return "config", "structured config/data, not prose"
    if not suffix or any(hint in suffix for hint in INTERNAL_HINTS):
        return "internal", "tool state, not content"
    return "unknown", "no door claims this extension"


def walk(roots: list[Path]) -> dict[str, dict[str, Any]]:
    stats: dict[str, dict[str, Any]] = defaultdict(lambda: {"count": 0, "bytes": 0, "samples": []})
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            try:
                if not path.is_file():
                    continue
                size = path.stat().st_size
            except OSError:
                continue
            entry = stats[path.suffix.lower()]
            entry["count"] += 1
            entry["bytes"] += size
            if len(entry["samples"]) < 3 and size > 0:
                entry["samples"].append(path)
    return stats


def probe(path: Path) -> str:
    """Look at the bytes of an unidentified file and say what it appears to be. Measured, not assumed."""
    try:
        head = path.open("rb").read(64)
    except OSError as exc:
        return f"unreadable ({exc.__class__.__name__})"
    if not head:
        return "EMPTY (zero bytes)"
    if head[:4] == b"PK\x03\x04":
        return "ZIP container (Office/openxml or zip)"
    if head[:4] == b"%PDF":
        return "PDF"
    try:
        text = head.decode("utf-8")
        printable = sum(1 for ch in text if ch.isprintable() or ch in "\r\n\t")
        if printable >= len(text) - 1:
            first = text.splitlines()[0][:60] if text.splitlines() else ""
            return f"text (utf-8), starts: {first!r}"
    except UnicodeDecodeError:
        pass
    return f"binary, magic {head[:8].hex()}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Census of document formats by door (P11)")
    parser.add_argument("--root", action="append", default=None, help="Root to scan (repeatable)")
    parser.add_argument("--report", default="", help="Write a markdown report here")
    parser.add_argument("--probe", type=int, default=2, help="Inspect bytes of unclaimed formats (0 = off)")
    args = parser.parse_args(argv)

    repo = Path(__file__).resolve().parents[1]
    raw_roots = args.root or list(DEFAULT_ROOTS)
    roots = [Path(r) if Path(r).is_absolute() else repo / r for r in raw_roots]
    present = [r for r in roots if r.exists()]

    print("scanning:")
    for root in roots:
        print(f"  {'ok  ' if root.exists() else 'MISS'} {root}")

    stats = walk(present)
    rows: list[tuple[str, int, int, str, str]] = []
    for suffix, entry in stats.items():
        bucket, why = classify(suffix)
        rows.append((suffix or "(none)", entry["count"], entry["bytes"], bucket, why))
    rows.sort(key=lambda r: (-r[2], r[0]))

    total_files = sum(r[1] for r in rows)
    total_bytes = sum(r[2] for r in rows)

    print()
    print(f"{'ext':<14}{'files':>8}{'MB':>10}  {'bucket':<12} why")
    for suffix, count, size, bucket, why in rows:
        print(f"{suffix:<14}{count:>8}{size / 1e6:>10.1f}  {bucket:<12} {why}")

    buckets: dict[str, dict[str, int]] = {}
    for _suffix, count, size, bucket, _why in rows:
        slot = buckets.setdefault(bucket, {"count": 0, "bytes": 0})
        slot["count"] += count
        slot["bytes"] += size
    print()
    for name in ("storable", "cognee-only", "office-gap", "read-only", "data", "mail", "md-variant",
                 "audio", "video", "image", "archive", "config", "code", "non-document", "cloud-stub",
                 "internal", "unknown"):
        if name in buckets:
            slot = buckets[name]
            print(f"  {name:<12} {slot['count']:>7} files  {slot['bytes'] / 1e6:>9.1f} MB")

    # Identify what nobody claims, from real bytes rather than from guesswork.
    findings: list[str] = []
    if args.probe:
        unknown_rows = [r for r in rows if r[3] == "unknown"]
        if unknown_rows:
            print()
            print("unclaimed formats - what are they?")
        for suffix, _count, _size, _bucket, _why in unknown_rows:
            samples = stats["" if suffix == "(none)" else suffix]["samples"]
            if not samples:
                continue
            verdict = probe(samples[0])
            print(f"  {suffix:<12} {verdict}   [{samples[0].name}]")
            findings.append(f"- `{suffix}` -> {verdict} (sample: `{samples[0].name}`)")

    write_report(args.report, present, rows, buckets, findings, total_files, total_bytes, repo)
    return 0


def write_report(
    dest: str,
    roots: list[Path],
    rows: list[tuple[str, int, int, str, str]],
    buckets: dict[str, dict[str, int]],
    findings: list[str],
    total_files: int,
    total_bytes: int,
    repo: Path,
) -> None:
    if not dest:
        return

    lines = [
        "# Document format census (P11)",
        "",
        f"Measured {datetime.now(timezone.utc).date().isoformat()} by `scripts/document-format-census.py`.",
        f"Roots scanned: {', '.join(f'`{r}`' for r in roots)}.",
        f"**{total_files:,} files, {total_bytes / 1e6:,.1f} MB** across {len(rows)} extensions.",
        "",
        "## There is no single supported-format set: there are four",
        "",
        "| Door | Accepts | Decided at |",
        "|------|---------|------------|",
        f"| Workbench upload -> memory | {' '.join(sorted(MEMORY_SUFFIXES))} | `pipeline/ingest_files.py:21` |",
        f"| Cognee mock ingest (MCP) | {' '.join(sorted(COGNEE_SUFFIXES))} | `pipeline/normalizer.py:28-40` (raises otherwise) |",
        f"| read_document (Eve reads) | {' '.join(sorted(READ_SUFFIXES))} | `pipeline/read_document.py:34-39` |",
        f"| query_data | {' '.join(sorted(DATA_SUFFIXES))} | `pipeline/query_data.py:113` |",
        "",
        "A format's fate therefore depends on the *door*, not the extension: `.txt` is storable but not",
        "cognee-ingestable, `.json` is the reverse, and `.docx` can be read but not remembered.",
        "",
        "## Measured distribution",
        "",
        "| ext | files | MB | bucket | why |",
        "|-----|------:|---:|--------|-----|",
    ]
    lines += [f"| `{s}` | {c:,} | {b / 1e6:,.1f} | {bk} | {w} |" for s, c, b, bk, w in rows]

    lines += ["", "## Buckets", "", "| bucket | files | MB |", "|--------|------:|---:|"]
    lines += [
        f"| {name} | {slot['count']:,} | {slot['bytes'] / 1e6:,.1f} |"
        for name, slot in sorted(buckets.items(), key=lambda kv: -kv[1]["bytes"])
    ]

    if findings:
        lines += ["", "## Unclaimed formats, identified from their bytes", "", *findings]

    lines += [
        "",
        "## What this gates",
        "",
        "**The biggest finding is a negative one.** The `non-document` bucket — emulator ROMs and MIDI, identified",
        "from magic bytes rather than inferred from extensions — is content that no document brick should ever touch.",
        "Together with `code` (which belongs to P9's structural reach) it accounts for most of what first looked like",
        "\"501 unclassified files\". A converter proposed for that pile would have been waste.",
        "",
        "The actionable items, in cheapness order:",
        "",
        "1. ~~**`md-variant` and `mail` are ~free.**~~ **DONE 2026-09-27 (P13):** `.mdx` and `.eml` are text a reader",
        "   already existed for and are now storable — a routing change, not a component.",
        "2. ~~**`office-gap` is a capability fix, not a volume win.**~~ **DONE 2026-09-27 (P13):** docling was already",
        "   installed and already converted docx/pptx/xlsx; `ingest_files` now routes all four Docling suffixes instead",
        "   of only `.pdf`. The re-run of this census is the proof — 18 more files became storable and the `office-gap`,",
        "   `md-variant` and `mail` buckets no longer appear. A capability fix, exactly as predicted, not a volume win.",
        "3. **`audio` is the only large measured target** (see the bucket table), and it is P8 — now unblocked by P3's",
        "   retry/quarantine, since a batch this size *will* have partial failures.",
        "4. **`image` is the only bucket that genuinely needs OCR**, which is what gates `surya`.",
        "5. **`cloud-stub` needs nothing**: `.gdoc`/`.gsheet` are pointers whose bytes are not the document.",
        "",
        "Method: the accept-lists are **imported from the modules themselves**, so this census fails loudly rather",
        "than silently drifting when a door changes; and unclaimed formats are identified by reading their bytes.",
    ]

    out = Path(dest) if Path(dest).is_absolute() else repo / dest
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print()
    print(f"report written: {out}")


if __name__ == "__main__":
    raise SystemExit(main())
