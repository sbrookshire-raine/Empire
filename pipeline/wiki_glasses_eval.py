"""Fifty-query Wiki Interpreter (glasses) evaluation harness.

Runs varied encyclopedia questions against live Weaviate + interpreter.
Scores cards with gold title/snippet expectations — not Eve chat.

Usage (repo root):
  .\\venv\\Scripts\\python.exe -m pipeline.wiki_glasses_eval
  .\\venv\\Scripts\\python.exe -m pipeline.wiki_glasses_eval --no-rerank
  .\\venv\\Scripts\\python.exe -m pipeline.wiki_glasses_eval --limit 10
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from pipeline.wiki_scout import (
    DEFAULT_API_KEY,
    DEFAULT_WEAVIATE_URL,
    check_weaviate,
    compare_years,
    search,
)
from pipeline.wiki_title_matcher import normalize_text

REPORT_DIR = Path(r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache")


@dataclass
class Case:
    id: str
    query: str
    mode: str = "search"  # search | compare
    year: str = "2021"
    years: tuple[str, ...] = ("2017", "2021", "2026")
    # At least one of these normalized title substrings should appear in top-K
    expect_any_title: tuple[str, ...] = ()
    # None of these should appear in top-1 (or top-K if strict)
    forbid_title: tuple[str, ...] = ()
    # Snippet of a matching card should contain one of these (casefold)
    expect_snippet_any: tuple[str, ...] = ()
    # Soft: prefer these in rank 1
    prefer_rank1: tuple[str, ...] = ()
    notes: str = ""
    tags: tuple[str, ...] = ()


@dataclass
class CaseResult:
    id: str
    query: str
    ok: bool
    passed: bool
    score: float
    issues: list[str] = field(default_factory=list)
    titles: list[str] = field(default_factory=list)
    snippets: list[str] = field(default_factory=list)
    elapsed_s: float = 0.0
    tags: list[str] = field(default_factory=list)
    error: str = ""


def _cases() -> list[Case]:
    """Varied encyclopedia questions — gold checks stay pattern-based."""
    return [
        # --- definitions / topics ---
        Case("d01", "Artificial Intelligence", expect_any_title=("artificial intelligence",), prefer_rank1=("artificial intelligence",), tags=("topic",)),
        Case("d02", "what is photosynthesis?", expect_any_title=("photosynthesis",), prefer_rank1=("photosynthesis",), tags=("topic", "chat")),
        Case("d03", "quantum entanglement", expect_any_title=("quantum entanglement",), tags=("topic",)),
        Case("d04", "machine learning", expect_any_title=("machine learning",), tags=("topic",)),
        Case("d05", "climate change", expect_any_title=("climate change", "global warming"), tags=("topic",)),
        Case("d06", "CRISPR", expect_any_title=("crispr",), tags=("topic",)),
        Case("d07", "general relativity", expect_any_title=("general relativity", "relativity"), tags=("topic",)),
        Case("d08", "blockchain", expect_any_title=("blockchain",), tags=("topic",)),
        # --- geography / capitals ---
        Case("g01", "what is the capital of France?", expect_any_title=("france", "paris"), forbid_title=("capital punishment",), expect_snippet_any=("paris",), prefer_rank1=("france", "paris"), tags=("geo", "chat")),
        Case("g02", "capital of Japan", expect_any_title=("japan", "tokyo"), forbid_title=("capital punishment",), expect_snippet_any=("tokyo",), tags=("geo",)),
        Case("g03", "capital of Australia", expect_any_title=("australia", "canberra"), forbid_title=("capital punishment",), expect_snippet_any=("canberra",), tags=("geo",)),
        Case("g04", "where is Mount Everest?", expect_any_title=("mount everest", "everest"), tags=("geo", "chat")),
        Case("g05", "Nile River", expect_any_title=("nile", "geography of egypt"), prefer_rank1=("nile (disambiguation)", "geography of egypt", "nile"), tags=("geo", "archive_hole")),
        Case("g06", "Amazon rainforest", expect_any_title=("amazon",), tags=("geo",)),
        # --- people ---
        Case("p01", "Albert Einstein", expect_any_title=("albert einstein",), prefer_rank1=("albert einstein",), tags=("person",)),
        Case("p02", "Marie Curie", expect_any_title=("marie curie", "curie"), prefer_rank1=("marie curie (disambiguation)", "curie family", "marie curie"), forbid_title=("gargoyle", "medal"), tags=("person", "archive_hole")),
        Case("p03", "who was Ada Lovelace?", expect_any_title=("ada lovelace",), prefer_rank1=("ada lovelace",), tags=("person", "chat")),
        Case("p04", "Nelson Mandela", expect_any_title=("nelson mandela",), prefer_rank1=("nelson mandela",), tags=("person",)),
        Case("p05", "Leonardo da Vinci", expect_any_title=("leonardo da vinci",), prefer_rank1=("science and inventions of leonardo da vinci", "leonardo da vinci (disambiguation)", "leonardo da vinci"), forbid_title=("airport", "ss leonardo"), tags=("person", "archive_hole")),
        Case("p06", "Alan Turing", expect_any_title=("alan turing",), prefer_rank1=("alan turing",), tags=("person",)),
        # --- offices / who-was ---
        Case("o01", "who was the president of the united states in 2017?", year="2017", expect_any_title=("presidency of donald trump", "president of the united states", "list of presidents"), expect_snippet_any=("trump",), forbid_title=("fictional", "fifa", "world cup"), tags=("office", "chat")),
        Case("o02", "President of the United States", expect_any_title=("president of the united states",), forbid_title=("fictional president",), tags=("office",)),
        Case("o03", "List of presidents of the United States", expect_any_title=("list of presidents of the united states",), prefer_rank1=("list of presidents of the united states",), tags=("office", "list")),
        Case("o04", "Prime Minister of the United Kingdom", expect_any_title=("prime minister of the united kingdom",), tags=("office",)),
        Case("o05", "who is the Chancellor of Germany?", expect_any_title=("chancellor of germany", "germany"), tags=("office", "chat")),
        # --- history / events ---
        Case("h01", "World War II", expect_any_title=("world war ii", "second world war"), prefer_rank1=("world war ii", "world war"), tags=("history",)),
        Case("h02", "Fall of the Berlin Wall", expect_any_title=("berlin wall",), expect_snippet_any=("1989", "wall"), tags=("history",)),
        Case("h03", "Apollo 11", expect_any_title=("apollo 11",), expect_snippet_any=("moon", "armstrong", "1969"), tags=("history",)),
        Case("h04", "French Revolution", expect_any_title=("french revolution",), tags=("history",)),
        Case("h05", "September 11 attacks", expect_any_title=("september 11", "9/11"), tags=("history",)),
        Case("h06", "Industrial Revolution", expect_any_title=("industrial revolution",), prefer_rank1=("industrial revolution", "second industrial revolution"), tags=("history", "archive_hole")),
        # --- ambiguous / trap ---
        Case("a01", "Mercury", expect_any_title=("mercury",), prefer_rank1=("mercury (mythology)", "mercury (element)", "outline of mercury (planet)", "mercury (disambiguation)", "mercury"), tags=("ambiguous",)),
        Case("a02", "Python", expect_any_title=("python (programming language)", "python"), prefer_rank1=("python (programming language)", "python"), tags=("ambiguous",)),
        Case("a03", "Java", expect_any_title=("java",), tags=("ambiguous",)),
        Case("a04", "Apple", expect_any_title=("apple",), tags=("ambiguous",)),
        Case("a05", "capital punishment", expect_any_title=("capital punishment",), forbid_title=("capital of france",), tags=("trap",)),
        Case("a06", "Turkey", expect_any_title=("turkey",), prefer_rank1=("turkey",), tags=("ambiguous",)),
        # --- science / math ---
        Case("s01", "periodic table", expect_any_title=("periodic table",), prefer_rank1=("periodic table",), tags=("science",)),
        Case("s02", "DNA", expect_any_title=("dna", "deoxyribonucleic"), prefer_rank1=("dna",), tags=("science",)),
        Case("s03", "black hole", expect_any_title=("black hole",), prefer_rank1=("black hole",), tags=("science",)),
        Case("s04", "evolution", expect_any_title=("evolution",), prefer_rank1=("evolution",), tags=("science",)),
        Case("s05", "vaccine", expect_any_title=("vaccine",), prefer_rank1=("vaccine",), tags=("science",)),
        # --- culture ---
        Case("c01", "Shakespeare", expect_any_title=("shakespeare", "william shakespeare"), prefer_rank1=("william shakespeare", "shakespeare"), tags=("culture",)),
        Case("c02", "The Odyssey", expect_any_title=("odyssey",), prefer_rank1=("odyssey",), tags=("culture",)),
        Case("c03", "Beethoven", expect_any_title=("beethoven",), prefer_rank1=("beethoven (disambiguation)", "ludwig van beethoven", "list of compositions by ludwig van beethoven"), forbid_title=("lil'", "peninsula"), tags=("culture", "archive_hole")),
        Case("c04", "Olympic Games", expect_any_title=("olympic",), prefer_rank1=("olympic games",), tags=("culture",)),
        # --- compare / truth drift ---
        Case("y01", "Artificial Intelligence", mode="compare", years=("2017", "2021", "2026"), expect_any_title=("artificial intelligence",), tags=("compare", "topic")),
        Case("y02", "who was the president of the united states?", mode="compare", years=("2017", "2021", "2026"), expect_any_title=("president", "presidency", "trump", "biden"), forbid_title=("fifa", "world cup", "fictional"), tags=("compare", "office")),
        Case("y03", "climate change", mode="compare", years=("2017", "2021"), expect_any_title=("climate change", "global warming"), tags=("compare", "topic")),
        # --- conversational noise ---
        Case("n01", "can you tell me about black holes please?", expect_any_title=("black hole",), tags=("chat", "science")),
        Case("n02", "find out what CRISPR gene editing is", expect_any_title=("crispr",), tags=("chat", "science")),
        Case("n03", "Sure, let's look up the capital of Canada", expect_any_title=("canada", "ottawa"), forbid_title=("capital punishment",), expect_snippet_any=("ottawa",), tags=("chat", "geo")),
    ]


def _titles_from_result(payload: dict[str, Any], mode: str) -> list[str]:
    titles: list[str] = []
    if mode == "compare":
        for _year, cards in (payload.get("cards_by_year") or {}).items():
            for card in cards or []:
                t = str(card.get("title") or "").strip()
                if t:
                    titles.append(t)
        if not titles:
            for _year, hits in (payload.get("hits_by_year") or {}).items():
                for hit in hits or []:
                    t = str(hit.get("title") or "").strip()
                    if t:
                        titles.append(t)
    else:
        for card in payload.get("cards") or []:
            t = str(card.get("title") or "").strip()
            if t:
                titles.append(t)
        if not titles:
            titles = [str(t) for t in (payload.get("titles") or []) if str(t).strip()]
    return titles


def _snippets_from_result(payload: dict[str, Any], mode: str) -> list[str]:
    snippets: list[str] = []
    if mode == "compare":
        for _year, cards in (payload.get("cards_by_year") or {}).items():
            for card in cards or []:
                snippets.append(str(card.get("snippet") or ""))
    else:
        for card in payload.get("cards") or []:
            snippets.append(str(card.get("snippet") or ""))
    return snippets


def _norm_has(hay: str, needle: str) -> bool:
    return normalize_text(needle) in normalize_text(hay)


def _rank1_matches(title: str, prefers: tuple[str, ...]) -> bool:
    """Prefer exact / paren primary titles over substring traps (White Nile ≠ Nile)."""
    from pipeline.wiki_title_matcher import strip_leading_article, strip_parens

    tn = normalize_text(strip_parens(strip_leading_article(title)))
    for prefer in prefers:
        pn = normalize_text(prefer)
        if not pn:
            continue
        if tn == pn:
            return True
        if tn.startswith(pn + " (") or tn.startswith(pn + ","):
            return True
    return False


def evaluate_case(case: Case, payload: dict[str, Any]) -> CaseResult:
    titles = _titles_from_result(payload, case.mode)
    snippets = _snippets_from_result(payload, case.mode)
    issues: list[str] = []
    score = 1.0

    if not payload.get("ok"):
        return CaseResult(
            id=case.id,
            query=case.query,
            ok=False,
            passed=False,
            score=0.0,
            issues=[f"tool_error: {payload.get('error')}"],
            titles=titles,
            snippets=snippets[:3],
            tags=list(case.tags),
            error=str(payload.get("error") or ""),
        )

    if not titles:
        issues.append("no_titles")
        score -= 1.0

    if case.expect_any_title and titles:
        if not any(
            any(_norm_has(t, exp) for exp in case.expect_any_title) for t in titles[:6]
        ):
            issues.append(f"missing_expected_title:{case.expect_any_title}")
            score -= 0.55

    if case.forbid_title and titles:
        # Forbid in rank-1 for person/culture; top-3 otherwise
        window = titles[:1] if any(t in case.tags for t in ("person", "culture")) else titles[:5]
        bad = [
            t
            for t in window
            if any(_norm_has(t, f) for f in case.forbid_title)
        ]
        # Also fail if forbidden appears as rank1 even outside those tags
        if titles and any(_norm_has(titles[0], f) for f in case.forbid_title):
            bad = list({*bad, titles[0]})
        if bad:
            issues.append(f"forbidden_title:{bad[:2]}")
            score -= 0.45

    if case.prefer_rank1 and titles:
        top = titles[0]
        if not _rank1_matches(top, case.prefer_rank1):
            issues.append(f"rank1_not_preferred:{top}")
            score -= 0.25
            # Person/culture: wrong rank-1 is a hard fail
            if any(t in case.tags for t in ("person", "culture", "history", "geo")):
                score -= 0.2
                issues.append("rank1_hard")

    if case.expect_snippet_any and snippets:
        blob = " ".join(snippets[:6])
        if not any(normalize_text(s) in normalize_text(blob) for s in case.expect_snippet_any):
            issues.append(f"snippet_missing:{case.expect_snippet_any}")
            score -= 0.35

    # Generic scratches — only flag disambiguation when it stole rank 1
    if titles:
        tn = normalize_text(titles[0])
        if "(disambiguation)" in tn and "disambiguation" not in normalize_text(case.query):
            issues.append(f"disambiguation_high:{titles[0]}")
            score -= 0.2
    if "capital of" in normalize_text(case.query):
        for t in titles[:3]:
            if "capital punishment" in normalize_text(t):
                issues.append("capital_punishment_trap")
                score -= 0.5
                break

    score = max(0.0, min(1.0, score))
    passed = score >= 0.7 and not any(
        i.startswith("missing_expected") or i.startswith("forbidden") or i.startswith("tool")
        for i in issues
    )
    return CaseResult(
        id=case.id,
        query=case.query,
        ok=True,
        passed=passed,
        score=round(score, 3),
        issues=issues,
        titles=titles[:6],
        snippets=[re.sub(r"\s+", " ", s)[:220] for s in snippets[:4]],
        tags=list(case.tags),
    )


def run_case(case: Case, *, write_files: bool = False) -> CaseResult:
    t0 = time.perf_counter()
    try:
        if case.mode == "compare":
            payload = compare_years(
                query=case.query,
                years=list(case.years),
                limit_per_year=3,
                interpret=True,
                write_files=write_files,
            )
        else:
            payload = search(
                query=case.query,
                year=case.year,
                limit=4,
                interpret=True,
                write_files=write_files,
            )
    except Exception as exc:  # noqa: BLE001
        return CaseResult(
            id=case.id,
            query=case.query,
            ok=False,
            passed=False,
            score=0.0,
            issues=[f"exception:{exc}"],
            error=str(exc),
            tags=list(case.tags),
            elapsed_s=time.perf_counter() - t0,
        )
    result = evaluate_case(case, payload)
    result.elapsed_s = round(time.perf_counter() - t0, 2)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Wiki glasses 50-query eval")
    parser.add_argument("--limit", type=int, default=0, help="Run only first N cases")
    parser.add_argument("--ids", default="", help="Comma-separated case ids")
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--write-files", action="store_true")
    args = parser.parse_args(argv)

    if args.no_rerank:
        import os

        os.environ["EMPIRE_WIKI_RERANK"] = "0"

    # Force UTF-8 console on Windows so titles/snippets do not crash the harness
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

    ready, detail = check_weaviate(DEFAULT_WEAVIATE_URL, DEFAULT_API_KEY)
    if not ready:
        print(f"Weaviate not ready: {detail}", file=sys.stderr)
        return 2

    cases = _cases()
    if args.ids.strip():
        want = {x.strip() for x in args.ids.split(",") if x.strip()}
        cases = [c for c in cases if c.id in want]
    if args.limit and args.limit > 0:
        cases = cases[: args.limit]

    print(f"Running {len(cases)} glasses cases (rerank={'off' if args.no_rerank else 'on'})…")
    results: list[CaseResult] = []
    for i, case in enumerate(cases, start=1):
        print(f"[{i}/{len(cases)}] {case.id} {case.query[:60]}…", flush=True)
        results.append(run_case(case, write_files=args.write_files))
        r = results[-1]
        flag = "PASS" if r.passed else "FAIL"
        print(f"  -> {flag} score={r.score} {r.titles[:2]} issues={r.issues}", flush=True)

    passed = sum(1 for r in results if r.passed)
    failed = [r for r in results if not r.passed]
    weak = [r for r in results if r.passed and r.issues]

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_json = REPORT_DIR / f"glasses_eval_{stamp}.json"
    out_md = REPORT_DIR / f"glasses_eval_{stamp}.md"
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    payload = {
        "generated_at": stamp,
        "count": len(results),
        "passed": passed,
        "failed": len(failed),
        "pass_rate": round(passed / max(len(results), 1), 3),
        "mean_score": round(sum(r.score for r in results) / max(len(results), 1), 3),
        "results": [asdict(r) for r in results],
    }
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = [
        f"# Wiki Glasses Eval — {stamp}",
        "",
        f"- Cases: **{len(results)}**",
        f"- Passed: **{passed}** ({payload['pass_rate']*100:.0f}%)",
        f"- Mean score: **{payload['mean_score']}**",
        f"- Rerank: {'off' if args.no_rerank else 'on'}",
        "",
        "## Failures",
        "",
    ]
    if not failed:
        lines.append("_None_")
    for r in failed:
        lines.append(f"### {r.id} — FAIL (score {r.score})")
        lines.append(f"- Query: `{r.query}`")
        lines.append(f"- Issues: {', '.join(r.issues) or '—'}")
        lines.append(f"- Titles: {r.titles}")
        if r.snippets:
            lines.append(f"- Snippet0: {r.snippets[0][:240]}")
        lines.append("")
    lines.append("## Soft issues (passed with scratches)")
    lines.append("")
    if not weak:
        lines.append("_None_")
    for r in weak:
        lines.append(f"- **{r.id}** ({r.score}): {r.issues} → {r.titles[:2]}")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print()
    print(f"PASS {passed}/{len(results)}  mean={payload['mean_score']}")
    print(f"Report: {out_md}")
    print(f"JSON:   {out_json}")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
