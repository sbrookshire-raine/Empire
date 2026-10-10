"""Keyword route index for Eve's own tools — not the external OSS catalog.db.

Answers: "what tool / limb / playbook area fits this intent?" with resource hints so she
does not load every schema or call heavy limbs without admission.

Sources (rebuilt on cache miss):
  - tool_registry.index() — name, one_line, toolbelt
  - playbook.index() — area, one_line, tools list
  - config/capability-manifest.json — limb load (GPU, network, auto_enable)
  - config/eve-capabilities/route-synonyms.json — manual phrase boosts
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from pipeline import playbook, tool_registry

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "capability-manifest.json"
SYNONYMS_PATH = ROOT / "config" / "eve-capabilities" / "route-synonyms.json"

STOPWORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "and",
        "or",
        "for",
        "to",
        "of",
        "in",
        "on",
        "with",
        "how",
        "do",
        "i",
        "me",
        "my",
        "you",
        "your",
        "is",
        "are",
        "can",
        "what",
        "which",
        "use",
        "using",
        "local",
        "eve",
        "empire",
        "tool",
        "tools",
    }
)

_CACHE: dict[str, Any] = {"entries": [], "mtime": 0.0}


def _dir_mtime(path: Path) -> float:
    if not path.is_dir():
        return 0.0
    latest = 0.0
    for child in path.glob("*"):
        try:
            latest = max(latest, child.stat().st_mtime)
        except OSError:
            continue
    return latest


def _cache_key() -> float:
    parts = [
        _dir_mtime(tool_registry.docs_dir()),
        _dir_mtime(playbook.playbook_dir()),
        MANIFEST_PATH.stat().st_mtime if MANIFEST_PATH.is_file() else 0.0,
        SYNONYMS_PATH.stat().st_mtime if SYNONYMS_PATH.is_file() else 0.0,
    ]
    return max(parts)


def _tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9_]{2,}", text.casefold())
    return {w for w in words if w not in STOPWORDS}


def _load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.is_file():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("categories") or {}
    except (OSError, json.JSONDecodeError):
        return {}


def _load_synonyms() -> dict[str, dict[str, list[str]]]:
    if not SYNONYMS_PATH.is_file():
        return {}
    try:
        payload = json.loads(SYNONYMS_PATH.read_text(encoding="utf-8"))
        return payload.get("phrases") or {}
    except (OSError, json.JSONDecodeError):
        return {}


def _limb_load(category: str, manifest: dict[str, Any]) -> dict[str, Any]:
    row = manifest.get(category) if category else {}
    if not isinstance(row, dict):
        row = {}
    return {
        "toolbelt": category or "always",
        "gpu_tenant": row.get("gpu_tenant", "none"),
        "network": bool(row.get("network", False)),
        "auto_enable": bool(row.get("auto_enable", False)),
        "session_ttl_min": int(row.get("session_ttl_min") or 0),
        "requires_services": list(row.get("requires_services") or []),
    }


def _next_steps(kind: str, entry_id: str, toolbelt: str, playbook_area: str) -> list[str]:
    steps: list[str] = []
    if toolbelt and toolbelt not in {"always", ""}:
        steps.append(
            f"If the limb is off: resource_pulse() then admit_for_goal({toolbelt!r}) or enable Toolbelt."
        )
    if playbook_area:
        steps.append(f"playbook({playbook_area!r}) for worked ask→tool→artefact routes.")
    if kind == "tool":
        steps.append(f"tool_docs({entry_id!r}) for parameters before calling.")
    elif kind == "limb":
        steps.append(f"playbook() — list areas — then open the area that lists {entry_id} tools.")
    elif kind == "area":
        steps.append(f"playbook({entry_id!r}) — then tool_docs for a specific tool name.")
    return steps


def build_entries() -> list[dict[str, Any]]:
    manifest = _load_manifest()
    synonyms = _load_synonyms()
    entries: list[dict[str, Any]] = []

    tool_to_area: dict[str, str] = {}
    for area_row in playbook.index():
        area_id = str(area_row.get("area") or "")
        tools_field = str(area_row.get("tools") or "")
        for name in re.findall(r"[a-z][a-z0-9_]{2,}", tools_field):
            tool_to_area.setdefault(name, area_id)

    for row in tool_registry.index():
        name = str(row.get("name") or "")
        one_line = str(row.get("one_line") or "")
        toolbelt = str(row.get("toolbelt") or "always")
        keywords = _tokenize(f"{name} {one_line} {toolbelt}")
        entries.append(
            {
                "kind": "tool",
                "id": name,
                "one_line": one_line,
                "toolbelt": toolbelt,
                "playbook_area": tool_to_area.get(name, ""),
                "keywords": sorted(keywords),
                "load": _limb_load(toolbelt if toolbelt != "always" else "", manifest),
                "next_steps": _next_steps(
                    "tool", name, toolbelt, tool_to_area.get(name, "")
                ),
            }
        )

    for row in playbook.index():
        area_id = str(row.get("area") or "")
        one_line = str(row.get("one_line") or "")
        tools_field = str(row.get("tools") or "")
        keywords = _tokenize(f"{area_id} {one_line} {tools_field}")
        entries.append(
            {
                "kind": "area",
                "id": area_id,
                "one_line": one_line,
                "toolbelt": "",
                "playbook_area": area_id,
                "keywords": sorted(keywords),
                "tools_preview": tools_field[:240],
                "load": {"note": "Playbook slice only — check each tool's limb before calling."},
                "next_steps": _next_steps("area", area_id, "", area_id),
            }
        )

    for cat_id, row in manifest.items():
        if not isinstance(row, dict):
            continue
        label = str(row.get("label") or cat_id)
        one_line = f"Toolbelt limb: {label}"
        keywords = _tokenize(f"{cat_id} {label}")
        entries.append(
            {
                "kind": "limb",
                "id": cat_id,
                "one_line": one_line,
                "toolbelt": cat_id,
                "playbook_area": "",
                "keywords": sorted(keywords),
                "load": _limb_load(cat_id, manifest),
                "next_steps": _next_steps("limb", cat_id, cat_id, ""),
            }
        )

    for phrase, mapping in synonyms.items():
        boost_tokens = _tokenize(phrase)
        for entry in entries:
            if entry["kind"] == "tool" and entry["id"] in (mapping.get("tools") or []):
                entry["keywords"] = sorted(set(entry["keywords"]) | boost_tokens)
            if entry["kind"] == "limb" and entry["id"] in (mapping.get("limbs") or []):
                entry["keywords"] = sorted(set(entry["keywords"]) | boost_tokens)
            if entry["kind"] == "area" and entry["id"] in (mapping.get("areas") or []):
                entry["keywords"] = sorted(set(entry["keywords"]) | boost_tokens)

    return entries


def _entries() -> list[dict[str, Any]]:
    key = _cache_key()
    if _CACHE["entries"] and _CACHE["mtime"] >= key:
        return _CACHE["entries"]
    built = build_entries()
    _CACHE["entries"] = built
    _CACHE["mtime"] = key
    return built


def route(query: str, limit: int = 5) -> dict[str, Any]:
    term = str(query or "").strip()[:200]
    bounded = max(1, min(int(limit), 10))
    if not term:
        return {
            "ok": False,
            "error": "query is required",
            "hint": "Describe the goal (e.g. reverse engineer electron app, wiki cast list, github mcp).",
            "results": [],
        }

    intent_summary: dict[str, Any] | None = None
    try:
        from pipeline.intent_codex import resolve as resolve_intent

        intent_payload = resolve_intent(term, limit=2, min_score=4)
        if intent_payload.get("ok") and intent_payload.get("primary"):
            intent_summary = {
                "primary_intent": intent_payload["primary"].get("id"),
                "say": intent_payload["primary"].get("say"),
                "local_tools": intent_payload["primary"].get("local_tools"),
                "online_tools": intent_payload["primary"].get("online_tools"),
                "limbs": intent_payload["primary"].get("limbs"),
                "playbook": intent_payload["primary"].get("playbook"),
            }
    except Exception:
        intent_summary = None

    q_lower = term.casefold()
    q_tokens = _tokenize(term)
    synonyms = _load_synonyms()
    phrase_boost: dict[str, int] = {}
    for phrase, mapping in synonyms.items():
        if phrase.casefold() in q_lower:
            for tool_id in mapping.get("tools") or []:
                phrase_boost[f"tool:{tool_id}"] = phrase_boost.get(f"tool:{tool_id}", 0) + 8
            for limb_id in mapping.get("limbs") or []:
                phrase_boost[f"limb:{limb_id}"] = phrase_boost.get(f"limb:{limb_id}", 0) + 8
            for area_id in mapping.get("areas") or []:
                phrase_boost[f"area:{area_id}"] = phrase_boost.get(f"area:{area_id}", 0) + 8

    scored: list[tuple[int, dict[str, Any]]] = []
    for entry in _entries():
        kind = entry["kind"]
        entry_id = entry["id"]
        hay = " ".join(entry["keywords"]) + " " + entry.get("one_line", "")
        score = 0
        for token in q_tokens:
            if token in entry["keywords"]:
                score += 3
            elif token in hay:
                score += 1
        if q_lower in entry_id.casefold() or q_lower in entry.get("one_line", "").casefold():
            score += 4
        score += phrase_boost.get(f"{kind}:{entry_id}", 0)
        if score > 0:
            hit = {k: v for k, v in entry.items() if k != "keywords"}
            hit["score"] = score
            scored.append((score, hit))

    scored.sort(key=lambda pair: (-pair[0], pair[1]["kind"], pair[1]["id"]))
    results = [row for _, row in scored[:bounded]]

    return {
        "ok": True,
        "query": term,
        "count": len(results),
        "intent_codex": intent_summary,
        "protocol": [
            "0) resolve_intent(message) — everyday verbs → local-first policy (intent-codex.json).",
            "1) capability_route(query) — pick tool, limb, or playbook area (this call).",
            "2) playbook(area) — worked examples; tool_docs(tool) — parameters.",
            "3) resource_pulse() before heavy limbs; admit_for_goal(category) if off.",
            "search_catalog is for external OSS/MCP repo rows in catalog.db — not this index.",
        ],
        "results": results,
    }


def list_index(*, max_entries: int = 40) -> dict[str, Any]:
    """Compact inventory for debugging — not for prompt stuffing."""

    bounded = max(1, min(int(max_entries), 200))
    slim = []
    for entry in _entries()[:bounded]:
        slim.append(
            {
                "kind": entry["kind"],
                "id": entry["id"],
                "toolbelt": entry.get("toolbelt"),
                "one_line": (entry.get("one_line") or "")[:120],
            }
        )
    return {
        "ok": True,
        "total": len(_entries()),
        "shown": len(slim),
        "entries": slim,
        "note": "Use capability_route(query) for keyword search; do not paste the full index into chat.",
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Route query; omit with --list")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--list", action="store_true", help="Print compact index sample")
    args = parser.parse_args()
    if args.list:
        print(json.dumps(list_index(), ensure_ascii=False, indent=2))
        return 0
    if not args.query.strip():
        print(json.dumps(route("", args.limit), ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(route(args.query, args.limit), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
