"""Normalize Wikipedia Markdown into Cognee-ready documents with ground-truth edges.

Each source file carries rich YAML frontmatter (title, outgoing_links, categories,
section_headings, revision_timestamp, doc_id). We reuse that frontmatter as ground-truth
graph edges instead of re-deriving them with an LLM. In ``full`` mode we additionally ask
Ollama for an abstractive summary, then let Cognee's cognify pass build the graph.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import httpx

try:  # PyYAML ships transitively via transformers/huggingface_hub in this venv.
    import yaml  # type: ignore

    _HAVE_YAML = True
except Exception:  # noqa: BLE001
    _HAVE_YAML = False

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")
SUMMARY_TIMEOUT_SEC = float(os.getenv("WIKI_SUMMARY_TIMEOUT", "120"))


def _split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body). Empty frontmatter if none present."""
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].strip("\n"), parts[2].lstrip("\n")


def _parse_frontmatter_manual(block: str) -> dict[str, Any]:
    """Minimal YAML-subset parser: scalars and simple ``- item`` lists."""
    meta: dict[str, Any] = {}
    current_key: str | None = None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if raw.lstrip().startswith("- ") and current_key is not None:
            item = raw.strip()[2:].strip().strip('"')
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(item)
            continue
        if ":" in raw:
            key, value = raw.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value in ("", "[]"):
                meta[key] = [] if value == "[]" else ""
                current_key = key if value == "" else None
            else:
                meta[key] = value.strip('"')
                current_key = None
    return meta


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    block, body = _split_frontmatter(text)
    if not block:
        return {}, body.strip()
    if _HAVE_YAML:
        try:
            loaded = yaml.safe_load(block)
            if isinstance(loaded, dict):
                return loaded, body.strip()
        except Exception:  # noqa: BLE001 — fall back to manual parser
            pass
    return _parse_frontmatter_manual(block), body.strip()


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    text = str(value).strip()
    return [text] if text else []


def derive_snapshot_year(meta: dict[str, Any], fallback_year: str = "") -> str:
    """Resolve the snapshot year for Truth-Drift tracking.

    Priority: frontmatter ``snapshot_id`` (e.g. "20260401" -> "2026") -> ``--year`` folder
    fallback -> ``revision_timestamp`` year. Parametric by year (2017/2021/2026/...); nothing
    is hardcoded to a specific snapshot set.
    """
    snapshot_id = str(meta.get("snapshot_id", "")).strip()
    if len(snapshot_id) >= 4 and snapshot_id[:4].isdigit():
        return snapshot_id[:4]
    if fallback_year and str(fallback_year)[:4].isdigit():
        return str(fallback_year)[:4]
    revision = str(meta.get("revision_timestamp", "")).strip()
    if len(revision) >= 4 and revision[:4].isdigit():
        return revision[:4]
    return "unknown"


def ollama_summarize(title: str, body: str) -> str:
    """Best-effort abstractive summary via local Ollama. Returns '' on any failure."""
    snippet = body[:6000]
    prompt = (
        "Summarize the following Wikipedia article in 2-3 sentences, then list the key "
        "entities as a comma-separated line prefixed with 'Entities:'.\n\n"
        f"Title: {title}\n\n{snippet}"
    )
    try:
        response = httpx.post(
            f"{OLLAMA_BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"},
            json={
                "model": OLLAMA_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "stream": False,
            },
            timeout=SUMMARY_TIMEOUT_SEC,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception:  # noqa: BLE001 — summary is optional enrichment
        return ""


def build_document(
    meta: dict[str, Any],
    body: str,
    *,
    snapshot_year: str,
    with_summary: str = "",
) -> str:
    """Build enriched Cognee text: snapshot-year + frontmatter edges as explicit triples.

    Truth-Drift design: each article node identity is snapshot-scoped ("<Title> (<YEAR>)")
    so multiple yearly snapshots of the same topic COEXIST as separate nodes, while a shared
    canonical topic node ("<Title>") links them together for cross-year comparison queries.
    Snapshot/year edges are emitted near the TOP so they are prominent for both embeddings
    and cognify, and are present in BOTH fast and full modes.
    """
    title = str(meta.get("title", "")).strip() or "Unknown"
    doc_id = str(meta.get("doc_id", "")).strip()
    revision = str(meta.get("revision_timestamp", "")).strip()
    snapshot = str(meta.get("snapshot_id", "")).strip()
    year = snapshot_year or "unknown"
    subject = f"{title} ({year})"  # snapshot-scoped node identity

    links = _as_list(meta.get("outgoing_links"))
    categories = _as_list(meta.get("categories"))
    sections = _as_list(meta.get("section_headings"))

    # Prominent snapshot-year header + triples FIRST (Truth-Drift anchor).
    lines: list[str] = [
        f"SnapshotYear: {year}",
        f"Title: {title}",
        f"SnapshotEntity: {subject}",
        "SourceType: wikipedia",
        "SnapshotEdges:",
        f"{subject} snapshot_year {year}",
        f"{subject} is_snapshot_of {title}",
        f"{subject} has_snapshot_year {year}",
    ]
    if snapshot:
        lines.append(f"{subject} snapshot_version {snapshot}")
    if revision:
        lines.append(f"{subject} revision_timestamp {revision}")

    if doc_id:
        lines.append(f"DocId: {doc_id}")
    if revision:
        lines.append(f"RevisionTimestamp: {revision}")
    if snapshot:
        lines.append(f"SnapshotId: {snapshot}")

    if links or categories:
        lines.append("Relationships:")
        for target in links:
            lines.append(f"{subject} links_to {target}")
        for category in categories:
            lines.append(f"{subject} in_category {category}")

    if sections:
        lines.append("Sections: " + "; ".join(sections))

    if with_summary:
        lines.append("")
        lines.append("Summary:")
        lines.append(with_summary)

    lines.append("")
    lines.append(body)
    return "\n".join(line for line in lines if line is not None)


def normalize_wiki_file(
    path: Path,
    *,
    dataset: str = "wikipedia",
    mode: str = "fast",
    fallback_year: str = "",
) -> dict[str, Any]:
    """Normalize one Wikipedia .md file into a Cognee-ready document + metadata."""
    meta, body = _parse_frontmatter(path.read_text(encoding="utf-8"))

    title = str(meta.get("title", "")).strip() or path.stem
    doc_id = str(meta.get("doc_id", "")).strip() or str(meta.get("page_id", "")).strip() or path.stem
    body_sha = str(meta.get("body_sha256", "")).strip()
    snapshot_year = derive_snapshot_year(meta, fallback_year)
    snapshot_id = str(meta.get("snapshot_id", "")).strip()

    summary = ""
    if mode == "full":
        summary = ollama_summarize(title, body)

    document = build_document(meta, body, snapshot_year=snapshot_year, with_summary=summary)

    return {
        "source_type": "wikipedia",
        "external_id": doc_id,
        "doc_id": doc_id,
        "title": title,
        "snapshot_entity": f"{title} ({snapshot_year or 'unknown'})",
        "source_file": str(path),
        "dataset": dataset,
        "document": document,
        "body_sha256": body_sha,
        "snapshot_year": snapshot_year,
        "snapshot_id": snapshot_id,
        "revision_timestamp": str(meta.get("revision_timestamp", "")).strip(),
        "outgoing_links": _as_list(meta.get("outgoing_links")),
        "categories": _as_list(meta.get("categories")),
        "has_summary": bool(summary),
    }
