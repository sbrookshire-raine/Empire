"""Shared provenance footers for scout / thought-experiment scratch caches.

Scratch is never Cognee truth. Promote helpers must copy this metadata into
remember payloads when the Architect explicitly promotes.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def yaml_quote(value: Any) -> str:
    text = str(value or "").replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def provenance_fields(
    *,
    source: str,
    kind: str,
    tool: str,
    limb: str,
    extra: dict[str, Any] | None = None,
) -> list[str]:
    """YAML front-matter lines (without --- fences)."""

    lines = [
        f"source: {source}",
        f"kind: {kind}",
        f"tool: {tool}",
        f"limb: {limb}",
        f"fetched_at: {yaml_quote(utc_now_iso())}",
        "memory_status: scratch",
        "promote: explicit_only",
    ]
    if extra:
        for key, value in extra.items():
            if value is None:
                continue
            if isinstance(value, (int, float, bool)):
                lines.append(f"{key}: {value}")
            else:
                lines.append(f"{key}: {yaml_quote(value)}")
    return lines


def provenance_markdown_footer(
    *,
    source: str,
    tool: str,
    limb: str,
) -> str:
    return (
        "\n\n---\n\n"
        f"_Provenance: source=`{source}` tool=`{tool}` limb=`{limb}` "
        f"at `{utc_now_iso()}`. Scratch only — promote to Cognee explicitly._\n"
    )


def remember_preamble_from_front_matter(path_label: str, body: str) -> str:
    """Prefix Cognee remember content with path + provenance reminder."""

    return (
        f"[EMPIRE promote] path={path_label}\n"
        "Scratch cache promoted by explicit Architect/Eve action.\n\n"
        f"{body.strip()}\n"
    )
