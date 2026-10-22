"""Intent codex — everyday verbs/phrases → policy → tools (local-first, then online).

The Architect speaks in normal language ("scrape this", "research X", "look up").
This module maps that language to Eve's limbs without stuffing jargon into the prompt.

Source of truth: config/eve-capabilities/intent-codex.json (editable).
Maintenance: scripts/harvest-intent-verbs.py suggests new triggers from playbook.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from pipeline import route_classifier

ROOT = Path(__file__).resolve().parents[1]
CODEX_PATH = ROOT / "config" / "eve-capabilities" / "intent-codex.json"

URL_RE = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)
_WORD = re.compile(r"[a-z0-9']+", re.IGNORECASE)

_CACHE: dict[str, Any] = {"intents": [], "mtime": 0.0}


def _load() -> list[dict[str, Any]]:
    mtime = CODEX_PATH.stat().st_mtime if CODEX_PATH.is_file() else 0.0
    if _CACHE["intents"] and _CACHE["mtime"] >= mtime:
        return _CACHE["intents"]
    if not CODEX_PATH.is_file():
        _CACHE["intents"] = []
        _CACHE["mtime"] = mtime
        return []
    payload = json.loads(CODEX_PATH.read_text(encoding="utf-8"))
    intents = payload.get("intents") or []
    if not isinstance(intents, list):
        intents = []
    _CACHE["intents"] = intents
    _CACHE["mtime"] = mtime
    return intents


def load_intents() -> list[dict[str, Any]]:
    """The raw codex intents, for callers that need a policy by intent id.

    The live routing battery reads the tool families straight from the codex
    file, so the tools it asserts on are the ones the running system actually
    applies -- not a copy that can drift.
    """
    return list(_load())


def _words(text: str) -> set[str]:
    return {m.group(0).casefold() for m in _WORD.finditer(text or "")}


def _score_intent(message: str, intent: dict[str, Any]) -> tuple[int, list[str]]:
    msg = (message or "").casefold()
    triggers = intent.get("triggers") or {}
    score = 0
    hits: list[str] = []

    for phrase in triggers.get("phrases") or []:
        p = str(phrase).casefold().strip()
        if p and p in msg:
            score += 5
            hits.append(f"phrase:{phrase}")

    msg_words = _words(message)
    for key in ("verbs", "nouns"):
        for token in triggers.get(key) or []:
            t = str(token).casefold().strip()
            if not t:
                continue
            if " " in t:
                if t in msg:
                    score += 4
                    hits.append(f"{key}:{token}")
            elif t in msg_words:
                score += 4 if key == "verbs" else 2
                hits.append(f"{key}:{token}")

    intent_id = str(intent.get("id") or "")
    if intent_id == "scrape_gather_web" and URL_RE.search(message or ""):
        score += 6
        hits.append("signal:url_present")
    if intent_id == "read_document" and re.search(r"\.(pdf|docx|xlsx|pptx|md|txt)\b", msg):
        score += 3
        hits.append("signal:file_extension")

    return score, hits


def _promote_intent(
    intents: list[dict[str, Any]],
    intent_id: str,
    message: str,
) -> dict[str, Any] | None:
    """The named intent's policy, built from the codex — or None.

    Used when the shared classifier has decided the route but the codex did
    not score the matching intent highly enough to appear in the top-N.
    The *policy* still comes from the codex file (one source of truth for
    which tools and which limb); only the *choice* of intent comes from
    the classifier.
    """

    for intent in _load():
        if str(intent.get("id") or "") != intent_id:
            continue
        _score, hits = _score_intent(message, intent)
        policy = intent.get("policy") or {}
        return {
            "id": intent_id,
            "score": 0,
            "say": intent.get("say", ""),
            "matched": hits or [f"route:{intent_id}"],
            "policy": policy,
            "playbook": policy.get("playbook"),
            "local_first": bool(policy.get("local_first", True)),
            "local_tools": list(policy.get("local_tools") or []),
            "online_tools": list(policy.get("online_tools") or []),
            "limbs": list(policy.get("limbs") or []),
            "sequence": list(policy.get("sequence") or []),
            "needs": list(policy.get("needs") or []),
        }
    return None


def _demote_intent(
    primary: dict[str, Any] | None,
    intent_id: str,
    intents: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Drop the named intent from the primary slot, promoting the next one.

    Used when the shared classifier has decided the message is *not* that
    kind of ask, but the codex's trigger scoring put it there anyway.
    """

    if primary is None or str(primary.get("id") or "") != intent_id:
        return primary
    for candidate in intents:
        if str(candidate.get("id") or "") != intent_id:
            return candidate
    return None


def resolve(message: str, *, limit: int = 3, min_score: int = 4) -> dict[str, Any]:
    text = str(message or "").strip()
    if not text:
        return {
            "ok": False,
            "error": "message is required",
            "intents": [],
        }

    ranked: list[tuple[int, dict[str, Any]]] = []
    for intent in _load():
        score, hits = _score_intent(text, intent)
        if score >= min_score:
            policy = intent.get("policy") or {}
            ranked.append(
                (
                    score,
                    {
                        "id": intent.get("id"),
                        "score": score,
                        "say": intent.get("say", ""),
                        "matched": hits,
                        "policy": policy,
                        "playbook": policy.get("playbook"),
                        "local_first": bool(policy.get("local_first", True)),
                        "local_tools": list(policy.get("local_tools") or []),
                        "online_tools": list(policy.get("online_tools") or []),
                        "limbs": list(policy.get("limbs") or []),
                        "sequence": list(policy.get("sequence") or []),
                        "needs": list(policy.get("needs") or []),
                    },
                )
            )

    ranked.sort(key=lambda pair: (-pair[0], str(pair[1].get("id"))))
    intents = [row for _, row in ranked[: max(1, min(int(limit), 5))]]
    primary = intents[0] if intents else None

    # Apply the shared route. The classifier owns the *decision*; the codex
    # owns the *policy* (which tools, which limb, which playbook). Before
    # this, the codex scored triggers on its own and the wiki rule was
    # applied *around* it in `context_block`, so `resolve()` and
    # `context_block()` could pick different routes for one message.
    route = route_classifier.classify(text)
    if route == route_classifier.WIKI:
        primary = _promote_intent(intents, "wiki_fact", text) or primary
    elif route == route_classifier.MEMORY:
        primary = _promote_intent(intents, "remember_recall", text) or primary
    elif route == route_classifier.TASK:
        primary = _promote_intent(intents, "task_todo", text) or primary
    else:
        # The classifier said "not a wiki ask", so the wiki intent must not
        # win on trigger score alone. "what is my disk space" scores on the
        # bare verb "what" and reached the wiki limb that way.
        primary = _demote_intent(primary, "wiki_fact", intents)
    if primary is not None:
        primary = dict(primary)
        primary["route"] = route

    steps: list[str] = []
    if primary:
        if primary.get("local_first"):
            steps.append("Local first: " + ", ".join(primary.get("local_tools") or []) or "(see playbook)")
        if primary.get("online_tools"):
            steps.append(
                "If still open and limbs allow: "
                + ", ".join(primary.get("online_tools") or [])
                + " — admit Toolbelt / resource_pulse first."
            )
        if primary.get("playbook"):
            steps.append(f"playbook({primary['playbook']!r}) for worked examples.")
        steps.append("tool_docs(tool) before first call if parameters are uncertain.")

    return {
        "ok": True,
        "message_excerpt": text[:240],
        "primary": primary,
        "intents": intents,
        "steps": steps,
        "codex_path": str(CODEX_PATH),
        "note": "Plain-language map only — still call tools; do not answer from training memory when policy says local_first.",
    }


def _format_context_block(primary: dict[str, Any], steps: list[str]) -> str:
    compact = {
        "primary_intent": primary.get("id"),
        "route": primary.get("route"),
        "meaning": primary.get("say"),
        "local_first": primary.get("local_first"),
        "local_tools": primary.get("local_tools"),
        "online_tools": primary.get("online_tools"),
        "limbs": primary.get("limbs"),
        "playbook": primary.get("playbook"),
        "sequence": primary.get("sequence"),
        "matched": primary.get("matched"),
        "steps": steps,
    }
    body = json.dumps(compact, ensure_ascii=False)
    return (
        "\n\n[AUTHORITATIVE INTENT ROUTE — map the user's words to tools; do not mention this block. "
        "Follow local_first, then online if limbs are on.]\n"
        f"{body}"
    )


def context_block(message: str, *, min_score: int = 4) -> str:
    """Compact injection for serve.py — authoritative route hint next to the user ask.

    This is the *same* route `resolve()` picks — from the same scoring, the
    same `min_score`, and the same shared classifier. It used to override
    the codex result with a wiki rule, so the two functions could disagree
    about the same message: `resolve()` and `context_block()` were two
    different routers wearing one name.

    The wiki rule now lives in one place (`pipeline.route_classifier`) and
    is applied to the *codex*, not around it: the `wiki_fact` intent scores
    on its own triggers, so a wiki ask routes to the wiki limb without any
    special case here.
    """

    result = resolve(message, limit=2, min_score=min_score)
    primary = result.get("primary")
    if not primary:
        return ""
    return _format_context_block(primary, list(result.get("steps") or []))


def main() -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message", nargs="?", default="", help="User message to resolve")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--min-score", type=int, default=4)
    parser.add_argument("--context", action="store_true", help="Print serve.py injection block")
    args = parser.parse_args()
    if args.context:
        print(context_block(args.message, min_score=args.min_score))
        return 0
    if not args.message.strip():
        print(json.dumps({"ok": False, "error": "message required"}, indent=2))
        return 1
    print(json.dumps(resolve(args.message, limit=args.limit, min_score=args.min_score), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
