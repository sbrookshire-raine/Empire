"""Installed Ollama inventory, ideal local suite, gap pulls, and cleanup."""

from __future__ import annotations

import re
from typing import Literal

from frontend.ollama_api import is_chat_model, load_active_model

FitLevel = Literal["excellent", "good", "tight", "heavy", "embed"]
Tier = Literal["daily", "quality", "specialist", "embed", "legacy"]
SlotStatus = Literal["covered", "weak", "gap"]

SUITE_SLOTS: list[dict] = [
    {
        "skillId": "dailyChat",
        "label": "Fast Mode (14b)",
        "description": "Default Eve voice — fast replies, tool calling, daily work.",
        "idealId": "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
        "equivalents": ["richardyoung/qwen2.5-14b-instruct-abliterated"],
        "sizeGb": 9.0,
        "fit16gb": "excellent",
        "why": "Fits 16 GB VRAM with a 16k context window and reliable tool JSON at temperature 0.35.",
        "whenToUse": "Default chat, brainstorming, quick scripts, and routine agent turns.",
    },
    {
        "skillId": "deepQuality",
        "label": "Deep Mode (32b)",
        "description": "Architect tier — complex planning and deep reasoning.",
        "idealId": "qwen2.5:32b",
        "equivalents": [],
        "sizeGb": 19.0,
        "fit16gb": "heavy",
        "why": "Highest local IQ when you accept RAM offload and an 8k context cap.",
        "whenToUse": "System planning, complex MCP work, and deep ARC sessions.",
    },
    {
        "skillId": "ragSynthesis",
        "label": "Librarian (Command-R 35b)",
        "description": "Mass synthesis across many retrieved documents.",
        "idealId": "command-r:35b",
        "equivalents": [],
        "sizeGb": 18.0,
        "fit16gb": "heavy",
        "why": "Strong RAG-style cross-reference with an 8k context window on 16 GB VRAM.",
        "whenToUse": "Reading many flattened files at once and comparing themes.",
    },
    {
        "skillId": "embedding",
        "label": "Memory embed",
        "description": "Cognee indexing — separate from Eve chat; wired in config/cognee.env.",
        "idealId": "nomic-embed-text:latest",
        "equivalents": ["nomic-embed-text", "mxbai-embed-large"],
        "sizeGb": 0.3,
        "fit16gb": "embed",
        "why": "EMPIRE default embed model; pairs with local Ollama and Cognee.",
        "whenToUse": "Workbench uploads, remember/recall, and graph memory only.",
    },
]

NAME_HINTS: list[tuple[re.Pattern[str], list[str], list[str], Tier, list[str]]] = [
    (
        re.compile(r"embed|minilm|nomic", re.I),
        ["Vector memory", "Cognee retrieval"],
        ["Not for Eve chat"],
        "embed",
        ["embedding"],
    ),
    (
        re.compile(r"coder|code", re.I),
        ["Code & repo work", "Structured output"],
        ["Weaker general chat"],
        "specialist",
        ["coding", "dailyChat"],
    ),
    (
        re.compile(r"deepseek-r1|r1", re.I),
        ["Reasoning & planning", "Multi-step tasks"],
        ["Slower than 8B"],
        "quality",
        ["reasoning", "deepQuality"],
    ),
    (
        re.compile(r"mistral-small|mistral.nemo", re.I),
        ["General intelligence", "Instruction following"],
        ["Heavier than 8–14B"],
        "quality",
        ["reasoning", "deepQuality", "dailyChat"],
    ),
    (
        re.compile(r"qwen3\.8|qwen3\.6|qwen3\.5|qwen3:8|27b", re.I),
        ["Strong reasoning", "Long context"],
        ["VRAM-heavy on 16 GB"],
        "quality",
        ["reasoning", "deepQuality"],
    ),
    (
        re.compile(r"qwen2\.5", re.I),
        ["Balanced reasoning", "General tasks"],
        ["27B variants are heavy"],
        "quality",
        ["reasoning", "dailyChat", "coding"],
    ),
    (
        re.compile(r"llama3\.1:8|llama3\.1:latest", re.I),
        ["Fast daily chat", "Tool calling", "Low VRAM"],
        ["Not the smartest tier"],
        "daily",
        ["dailyChat"],
    ),
    (
        re.compile(r"llama3\.2:1|llama3\.2:3", re.I),
        ["Very fast", "Minimal VRAM"],
        ["Limited capability"],
        "legacy",
        ["dailyChat"],
    ),
    (
        re.compile(r"llama", re.I),
        ["General chat"],
        ["Depends on size"],
        "daily",
        ["dailyChat"],
    ),
]


def _size_gb(entry: dict) -> float:
    raw = entry.get("size")
    if isinstance(raw, (int, float)) and raw > 0:
        return round(raw / (1024**3), 1)
    return 0.0


def _fit_for_vram(size_gb: float, role: str, vram_gb: int = 16) -> FitLevel:
    if role == "embed":
        return "embed"
    if size_gb <= 0:
        return "good"
    if size_gb <= vram_gb * 0.45:
        return "excellent"
    if size_gb <= vram_gb * 0.62:
        return "good"
    if size_gb <= vram_gb * 0.95:
        return "tight"
    return "heavy"


def _profile_for_name(name: str) -> tuple[list[str], list[str], Tier, list[str]]:
    for pattern, strengths, tradeoffs, tier, skills in NAME_HINTS:
        if pattern.search(name):
            return strengths, tradeoffs, tier, skills
    return ["General chat"], ["Unknown family"], "daily", ["dailyChat"]


def _role(entry: dict) -> Literal["chat", "embed"]:
    return "embed" if not is_chat_model(entry) else "chat"


def _tools(entry: dict) -> bool:
    capabilities = entry.get("capabilities")
    if isinstance(capabilities, list):
        caps = {str(item).casefold() for item in capabilities}
        return "tools" in caps
    return _role(entry) == "chat" and "embed" not in str(entry.get("name") or "").casefold()


def _normalize_id(model_id: str) -> str:
    return model_id.strip().casefold()


def _matches_slot(model_id: str, slot: dict) -> bool:
    needle = _normalize_id(model_id)
    candidates = [_normalize_id(slot["idealId"])] + [_normalize_id(item) for item in slot.get("equivalents", [])]
    if needle in candidates:
        return True
    base = needle.split(":")[0]
    for candidate in candidates:
        if candidate.split(":")[0] == base:
            return True
    return False


def _pull_command(model_id: str) -> str:
    return f"ollama pull {model_id}"


def list_installed_models(tags: dict, *, vram_gb: int = 16) -> list[dict]:
    raw = tags.get("models") if isinstance(tags, dict) else None
    if not isinstance(raw, list):
        return []
    models: list[dict] = []
    for entry in raw:
        if not isinstance(entry, dict):
            continue
        model_id = str(entry.get("name") or entry.get("model") or "").strip()
        if not model_id:
            continue
        role = _role(entry)
        details = entry.get("details") if isinstance(entry.get("details"), dict) else {}
        size_gb = _size_gb(entry)
        strengths, tradeoffs, tier, skills = _profile_for_name(model_id)
        if role == "embed":
            strengths, tradeoffs, tier, skills = (
                ["Cognee / vector memory"],
                ["Not for Eve chat"],
                "embed",
                ["embedding"],
            )
        fit = _fit_for_vram(size_gb, role, vram_gb=vram_gb)
        models.append(
            {
                "id": model_id,
                "role": role,
                "sizeGb": size_gb,
                "parameterSize": str(details.get("parameter_size") or "").strip(),
                "quantization": str(details.get("quantization_level") or "").strip(),
                "family": str(details.get("family") or "").strip(),
                "tools": _tools(entry),
                "strengths": strengths,
                "tradeoffs": tradeoffs,
                "tier": tier,
                "fit16gb": fit,
                "skills": skills,
            }
        )
    models.sort(key=lambda item: (item["role"] != "chat", item["sizeGb"], item["id"]))
    return models


def _model_detail(models: list[dict], model_id: str | None) -> dict | None:
    if not model_id:
        return None
    for model in models:
        if model["id"] == model_id:
            return dict(model)
    return None


def _best_installed_for_slot(models: list[dict], slot: dict) -> dict | None:
    matches = [model for model in models if _matches_slot(model["id"], slot)]
    if not matches:
        return None
    ideal = _normalize_id(slot["idealId"])
    for model in matches:
        if _normalize_id(model["id"]) == ideal:
            return dict(model)
    matches.sort(
        key=lambda item: (
            item["fit16gb"] not in ("excellent", "embed"),
            item["fit16gb"] not in ("good",),
            item["sizeGb"],
            item["id"],
        )
    )
    return dict(matches[0])


def _slot_status(slot: dict, installed: dict | None) -> SlotStatus:
    if not installed:
        return "gap"
    if _normalize_id(installed["id"]) == _normalize_id(slot["idealId"]):
        return "covered"
    if _matches_slot(installed["id"], slot):
        return "weak"
    return "gap"


def build_suite_slots(models: list[dict]) -> list[dict]:
    roster: list[dict] = []
    for slot in SUITE_SLOTS:
        installed = _best_installed_for_slot(models, slot)
        status = _slot_status(slot, installed)
        pull_id = slot["idealId"] if status in ("gap", "weak") else None
        roster.append(
            {
                "id": slot["skillId"],
                "label": slot["label"],
                "description": slot["description"],
                "status": status,
                "ideal": {
                    "id": slot["idealId"],
                    "sizeGb": slot["sizeGb"],
                    "fit16gb": slot["fit16gb"],
                    "why": slot["why"],
                    "whenToUse": slot["whenToUse"],
                    "pullCommand": _pull_command(slot["idealId"]),
                },
                "installed": installed,
                "installedId": installed["id"] if installed else None,
                "pull": (
                    {
                        "id": pull_id,
                        "command": _pull_command(pull_id),
                        "why": slot["why"],
                    }
                    if pull_id and status != "covered"
                    else None
                ),
            }
        )
    return roster


def _keeper_ids(slots: list[dict]) -> set[str]:
    keep: set[str] = set()
    for slot in slots:
        if slot.get("installedId"):
            keep.add(str(slot["installedId"]))
        elif slot.get("status") == "gap":
            keep.add(str(slot["ideal"]["id"]))
    return keep


def _duplicate_removals(
    models: list[dict],
    duplicate_groups: list[list[str]],
    keepers: set[str],
) -> list[dict]:
    removals: list[dict] = []
    for group in duplicate_groups:
        if len(group) < 2:
            continue
        preferred = None
        for model_id in group:
            if model_id in keepers:
                preferred = model_id
                break
        if not preferred:
            preferred = sorted(group, key=lambda item: (":" in item, item))[0]
        for model_id in group:
            if model_id == preferred:
                continue
            removals.append(
                {
                    "id": model_id,
                    "reason": f"Duplicate of {preferred} (same digest).",
                    "command": f"ollama rm {model_id}",
                }
            )
    return removals


def _redundant_removals(models: list[dict], slots: list[dict], keepers: set[str]) -> list[dict]:
    removals: list[dict] = []
    installed_by_skill = {slot["id"]: slot.get("installedId") for slot in slots}

    deep_slot = next((slot for slot in slots if slot["id"] == "deepQuality"), None)
    deep_keeper = installed_by_skill.get("deepQuality")
    for model in models:
        if model["role"] != "chat":
            continue
        model_id = model["id"]
        if model_id in keepers:
            continue
        if "27" in model_id or "27b" in model["parameterSize"].casefold():
            if deep_keeper and model_id != deep_keeper:
                removals.append(
                    {
                        "id": model_id,
                        "reason": f"Extra 27B build — keep one deep-quality model ({deep_keeper}).",
                        "command": f"ollama rm {model_id}",
                    }
                )
                continue
        if model["tier"] == "legacy" and installed_by_skill.get("dailyChat"):
            removals.append(
                {
                    "id": model_id,
                    "reason": f"Legacy tiny model — daily chat covered by {installed_by_skill['dailyChat']}.",
                    "command": f"ollama rm {model_id}",
                }
            )
            continue
        if model_id == "llama3.1:latest" and installed_by_skill.get("dailyChat") == "llama3.1:8b":
            removals.append(
                {
                    "id": model_id,
                    "reason": "Same weights as llama3.1:8b under a different tag.",
                    "command": f"ollama rm {model_id}",
                }
            )

    embed_keeper = installed_by_skill.get("embedding")
    if embed_keeper:
        for model in models:
            if model["role"] != "embed" or model["id"] == embed_keeper:
                continue
            removals.append(
                {
                    "id": model["id"],
                    "reason": f"Extra embed model — Cognee uses {embed_keeper}.",
                    "command": f"ollama rm {model['id']}",
                }
            )

    if deep_slot and deep_slot.get("status") == "covered" and deep_keeper:
        for model in models:
            if model["role"] != "chat" or model["id"] in keepers:
                continue
            if model["id"] == deep_keeper:
                continue
            if "deepQuality" in model.get("skills", []) and model["fit16gb"] == "heavy":
                removals.append(
                    {
                        "id": model["id"],
                        "reason": f"Heavy overlap with deep-quality keeper {deep_keeper}.",
                        "command": f"ollama rm {model['id']}",
                    }
                )

    return removals


def _unique_removals(items: list[dict]) -> list[dict]:
    seen: set[str] = set()
    ordered: list[dict] = []
    for item in items:
        model_id = str(item.get("id") or "")
        if not model_id or model_id in seen:
            continue
        seen.add(model_id)
        ordered.append(item)
    return ordered


def build_pull_gaps(slots: list[dict]) -> list[dict]:
    pulls: list[dict] = []
    for slot in slots:
        if slot["status"] == "covered":
            continue
        pull = slot.get("pull")
        if not pull:
            continue
        entry = dict(pull)
        entry["skillId"] = slot["id"]
        entry["label"] = slot["label"]
        pulls.append(entry)
    return pulls


def build_eve_briefing(
    slots: list[dict],
    pulls: list[dict],
    removals: list[dict],
    *,
    vram_gb: int,
    ram_gb: int,
) -> str:
    lines = [
        f"EMPIRE local model suite ({vram_gb} GB VRAM, {ram_gb} GB RAM).",
        "Eve should route tasks to the model that matches the skill, not always the active chat default.",
        "",
        "Skill routing:",
    ]
    for slot in slots:
        target = slot["installedId"] or slot["ideal"]["id"]
        status = slot["status"]
        lines.append(
            f"- {slot['label']} ({status}): use `{target}` — {slot['ideal']['whenToUse']}"
        )
    if pulls:
        lines.extend(["", "Pull to fill gaps:"])
        for pull in pulls:
            lines.append(f"- `{pull['command']}` — {pull['why']}")
    if removals:
        lines.extend(["", "Safe to remove (duplicates / overlap):"])
        for item in removals[:8]:
            lines.append(f"- `{item['command']}` — {item['reason']}")
    return "\n".join(lines)


def build_recommendations(
    models: list[dict],
    *,
    duplicate_groups: list[list[str]] | None = None,
    vram_gb: int = 16,
    ram_gb: int = 64,
    active_chat: str | None = None,
) -> dict:
    chat_models = [model for model in models if model["role"] == "chat"]
    heavy = [model["id"] for model in chat_models if model["fit16gb"] == "heavy"]
    slots = build_suite_slots(models)
    keepers = _keeper_ids(slots)
    removals = _unique_removals(
        _duplicate_removals(models, duplicate_groups or [], keepers)
        + _redundant_removals(models, slots, keepers)
    )
    pulls = build_pull_gaps(slots)
    gaps = sum(1 for slot in slots if slot["status"] == "gap")
    weak = sum(1 for slot in slots if slot["status"] == "weak")
    covered = sum(1 for slot in slots if slot["status"] == "covered")

    summary_parts = [
        f"{vram_gb} GB VRAM · {ram_gb} GB RAM.",
        f"Suite: {covered} covered, {weak} workable, {gaps} gap{'s' if gaps != 1 else ''}.",
        "One model per skill — pull gaps, remove duplicates, route Eve by task type.",
    ]
    if heavy:
        summary_parts.append(
            "Heavy installs: " + ", ".join(heavy[:3]) + ("…" if len(heavy) > 3 else "") + "."
        )

    eve_guidance = {
        slot["id"]: slot["installedId"] or slot["ideal"]["id"] for slot in slots
    }

    return {
        "hardware": {"vramGb": vram_gb, "ramGb": ram_gb},
        "activeChat": active_chat or load_active_model(),
        "summary": " ".join(summary_parts),
        "suite": slots,
        "skills": slots,
        "pullGaps": pulls,
        "removeSuggestions": removals,
        "optionalCleanup": [item["id"] for item in removals],
        "recommendedKeep": sorted(keepers),
        "eveBriefing": build_eve_briefing(slots, pulls, removals, vram_gb=vram_gb, ram_gb=ram_gb),
        "eveGuidance": eve_guidance,
        "heavyModels": heavy,
    }


def _duplicate_groups(digest_by_id: dict[str, str]) -> list[list[str]]:
    by_digest: dict[str, list[str]] = {}
    for model_id, digest in digest_by_id.items():
        if not digest:
            continue
        by_digest.setdefault(digest, []).append(model_id)
    return [ids for ids in by_digest.values() if len(ids) > 1]


def build_inventory(tags: dict, *, vram_gb: int = 16, ram_gb: int = 64) -> dict:
    raw = tags.get("models") if isinstance(tags, dict) else None
    digest_by_id: dict[str, str] = {}
    if isinstance(raw, list):
        for entry in raw:
            if isinstance(entry, dict):
                model_id = str(entry.get("name") or entry.get("model") or "").strip()
                digest = str(entry.get("digest") or "").strip()
                if model_id and digest:
                    digest_by_id[model_id] = digest

    models = list_installed_models(tags, vram_gb=vram_gb)
    duplicate_groups = _duplicate_groups(digest_by_id)
    recommendations = build_recommendations(
        models,
        duplicate_groups=duplicate_groups,
        vram_gb=vram_gb,
        ram_gb=ram_gb,
        active_chat=load_active_model(),
    )

    return {
        "ok": True,
        "models": models,
        "recommendations": recommendations,
        "duplicateGroups": duplicate_groups,
    }
