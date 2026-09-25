"""Research bench — the eval that decides whether Eve can work outside her own archive.

Why this exists (2026-09-24)
----------------------------
`docs/RESEARCH_CLOSURE.md` closed discovery: "future architecture changes require a **measured
DriftBench regression**, not a new README." The Architect then named the one capability he actually
wants and does not have — *"let her search the internet if I need her to"* — which is a **proven
hole**, so it gets a bench before it gets a tool. This module is that bench's logic:

- `capability_baseline()` measures, **from the repo**, which of her named needs a callable tool can
  satisfy today. The answer is derived from `pipeline.tool_registry`, so a disabled tool
  (`web_search`) is absent by construction — the absence *is* the finding, not an opinion.
- `grade()` scores a real turn against the case's rules (expected tool ran, source cited, forbidden
  claims absent, artefact produced), so "she got better" is a number and not a feeling.

What she can do today, per the case needs
-----------------------------------------
`archive` (wiki_*), `github` (github_scout_*), `fetch` (web_scout, **given** a URL),
`artefact` (create_spreadsheet / author_code after admission), `memory` (cognee_*).
`search` — a query with no URL and no archive hit — has **no tool**: `web_search` / `web_fetch` are
`disableTool()`, and `research_orchestrate` orchestrates archive + GitHub + the Product Hunt feed +
one URL you name, not a public web search. That is what this bench proves.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BENCH = ROOT / "data" / "eval" / "research_bench.jsonl"

# Which callable tools satisfy each named need. Checked against the live registry, so this table
# states intent and the repo supplies truth — including the truth that `search` has nothing.
NEED_TOOLS: dict[str, tuple[str, ...]] = {
    "search": ("web_search", "web_fetch", "searxng_search", "web_search_local"),
    "fetch": ("web_scout", "browser_local_fetch"),
    "github": ("github_scout_search", "github_scout_readme"),
    "archive": (
        "wiki_scout_search",
        "wiki_resolve",
        "wiki_read_section",
        "wiki_extract",
        "wiki_scout_compare_years",
    ),
    "artefact": ("create_spreadsheet", "author_code", "draft_work_order"),
    "memory": ("cognee_recall", "cognee_remember", "propose_remember", "confirm_remember"),
    "none": (),
}

# Safety net beyond each case's own `must_not_mention`.
BAD_REPLY_MARKERS = (
    "as an ai language model",
    "i don't have access to the internet",
    "i do not have access to the internet",
)
URL_RE = re.compile(r"https?://[^\s)\]\"']+")
SHEETS = {"create_spreadsheet", "author_code", "draft_work_order"}


def bench_path() -> Path:
    """The case file (overridable for tests)."""

    override = os.environ.get("EMPIRE_RESEARCH_BENCH", "").strip()
    return Path(override) if override else DEFAULT_BENCH


def load_cases(path: Path | None = None) -> list[dict[str, Any]]:
    """Read the JSONL cases, skipping blank lines and `import_pending` placeholders."""

    source = path or bench_path()
    cases: list[dict[str, Any]] = []
    for line in source.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if not str(row.get("query") or "").strip():
            continue
        if row.get("tier") == "import_pending":
            continue
        cases.append(row)
    return cases


def _registry_names() -> set[str]:
    from pipeline import tool_registry

    return set(tool_registry.tool_names())


def _resident_names() -> set[str]:
    from pipeline import tool_registry

    return {entry["name"] for entry in tool_registry.index() if entry.get("toolbelt") == "always"}


def _baseline_reason(need: str, required: list[str], present: list[str], resident: set[str]) -> str:
    """One plain sentence explaining the verdict (kept out of the loop so it stays readable)."""

    if need == "none":
        return "answered in prose by design — no tool should run"
    if not present:
        return f"no callable tool for a {need!r} ask (tried: {', '.join(required)})"
    residents = [name for name in present if name in resident]
    if residents:
        return f"resident: {', '.join(residents)}"
    return f"callable after admission via {', '.join(present)}"


def capability_baseline(cases: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """Per case: does a callable tool exist for what it needs? (No model required.)"""

    rows: list[dict[str, Any]] = []
    available = _registry_names()
    resident = _resident_names()
    for case in cases if cases is not None else load_cases():
        need = str(case.get("needs") or "none")
        required = list(NEED_TOOLS.get(need, ()))
        present = [name for name in required if name in available]
        blocked = need != "none" and not present
        rows.append(
            {
                "id": case.get("id"),
                "needs": need,
                "required": required,
                "available": present,
                "resident": [name for name in present if name in resident],
                "verdict": "blocked" if blocked else "ready",
                "reason": _baseline_reason(need, required, present, resident),
            }
        )
    blocked_needs = sorted({row["needs"] for row in rows if row["verdict"] == "blocked"})
    return {
        "ok": not blocked_needs,
        "cases": len(rows),
        "ready": sum(1 for row in rows if row["verdict"] == "ready"),
        "blocked": sum(1 for row in rows if row["verdict"] == "blocked"),
        "blocked_needs": blocked_needs,
        "rows": rows,
    }


def grade(
    case: dict[str, Any],
    *,
    answer: str,
    tools: list[str] | None = None,
) -> dict[str, Any]:
    """Score one real turn against its case rules. Returns `{id, passed, issues, evidence}`."""

    text = str(answer or "")
    lowered = text.casefold()
    ran = [str(name) for name in (tools or [])]
    issues: list[str] = []

    expected = [str(name) for name in (case.get("expect_tool_any") or [])]
    if expected and not set(expected) & set(ran):
        issues.append(f"no expected tool ran (saw: {', '.join(ran) or 'none'})")

    if case.get("must_cite_source") and not URL_RE.search(text):
        issues.append("no source URL in the answer")

    for needle in case.get("must_contain") or []:
        if str(needle).casefold() not in lowered:
            issues.append(f"answer missing {needle!r}")

    mention_any = [str(value) for value in (case.get("must_mention_any") or [])]
    if mention_any and not any(value.casefold() in lowered for value in mention_any):
        issues.append(f"answer mentions none of {mention_any}")

    titles = [str(value) for value in (case.get("expect_title_any") or [])]
    if titles and not any(value.casefold() in lowered for value in titles):
        issues.append(f"answer never names the page {titles}")

    if case.get("expect_artefact") and not (set(ran) & SHEETS):
        # An inline markdown table is chat text, not a document he can open — the Architect asked to
        # "package her research into documents for me to look at", so the limb must actually run.
        issues.append("no artefact: no create_spreadsheet/author_code call ran")

    for bad in list(case.get("must_not_mention") or []) + list(BAD_REPLY_MARKERS):
        if str(bad).casefold() in lowered:
            issues.append(f"answer contains forbidden {bad!r}")

    if not text.strip():
        issues.append("empty reply")

    return {
        "id": case.get("id"),
        "needs": case.get("needs"),
        "passed": not issues,
        "issues": issues,
        "evidence": {"tools": ran, "cited_url": bool(URL_RE.search(text)), "chars": len(text)},
    }


def summarise(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Roll a list of `grade()` results into pass/fail counts per need."""

    per_need: dict[str, dict[str, int]] = {}
    for result in results:
        need = str(result.get("needs") or "none")
        bucket = per_need.setdefault(need, {"pass": 0, "fail": 0})
        bucket["pass" if result.get("passed") else "fail"] += 1
    return {
        "cases": len(results),
        "passed": sum(1 for result in results if result.get("passed")),
        "failed": sum(1 for result in results if not result.get("passed")),
        "per_need": per_need,
        "failures": [
            {"id": result.get("id"), "issues": result.get("issues")}
            for result in results
            if not result.get("passed")
        ],
    }

