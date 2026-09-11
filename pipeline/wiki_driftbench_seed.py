"""Generate EMPIRE DriftBench calibration rows for wiki Q&A eval.

Writes JSONL cases derived from known archive patterns (redirects, vague
descriptions, parametric distractors). Public HF datasets are merged separately
via scripts/import-wiki-calibrate-samples.py when the Architect is ready.

Usage:
  .\\venv\\Scripts\\python.exe -m pipeline.wiki_driftbench_seed
  .\\venv\\Scripts\\python.exe -m pipeline.wiki_driftbench_seed --out data/eval/wiki_driftbench_seed.jsonl
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterator

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = EMPIRE_ROOT / "data" / "eval" / "wiki_driftbench_seed.jsonl"


@dataclass
class CalibrateCase:
    id: str
    source: str
    tier: str
    query: str
    year: str = "2026"
    mode: str = "lookup"  # lookup | compare | retrieval
    must_contain: list[str] = field(default_factory=list)
    must_not_contain: list[str] = field(default_factory=list)
    expect_title_any: list[str] = field(default_factory=list)
    forbid_title: list[str] = field(default_factory=list)
    injection: bool = True
    live_eve: bool = False
    retrieval: bool = True
    tags: list[str] = field(default_factory=list)
    notes: str = ""


def _handwritten_failures() -> Iterator[CalibrateCase]:
    """Cases that failed before Phase A wiki_read_lead + grounding guard."""
    yield CalibrateCase(
        id="hand_01",
        source="handwritten",
        tier="smoke",
        query="what popular 80s song got re-popularized during the later seasons of stranger things?",
        must_contain=["running up that hill"],
        expect_title_any=["Running Up That Hill"],
        live_eve=True,
        tags=["stranger_things", "revival", "vague"],
    )
    yield CalibrateCase(
        id="hand_02",
        source="handwritten",
        tier="smoke",
        query="what 80s song became a hit again in the series stranger things?",
        must_contain=["running up that hill"],
        expect_title_any=["Running Up That Hill"],
        live_eve=True,
        tags=["stranger_things", "revival"],
    )
    yield CalibrateCase(
        id="hand_03",
        source="handwritten",
        tier="smoke",
        query="what song from Kate Bush reinvigorated her career in 2025-2026?",
        must_contain=["running up that hill", "kate bush"],
        must_not_contain=["wow"],  # live_eve only — evidence may mention other singles
        expect_title_any=["Running Up That Hill"],
        live_eve=True,
        tags=["kate_bush", "revival", "parametric_distractor"],
        notes="Live reply must not hallucinate Kate Bush single 'Wow'. Injection may cite discography.",
    )
    yield CalibrateCase(
        id="hand_04",
        source="handwritten",
        tier="smoke",
        query="who is Kate Bush?",
        must_contain=["kate bush", "1958"],
        expect_title_any=["Kate Bush"],
        live_eve=True,
        tags=["bio", "entity"],
        notes="Bio lead — Catherine Bush born 1958; not 2023 Rolling Stone trivia.",
    )
    yield CalibrateCase(
        id="hand_05",
        source="handwritten",
        tier="smoke",
        query="can you access my wikipedia archive?",
        must_contain=["wikipedia", "yes"],
        must_not_contain=["wiki_scout_compare_years", "truth drift"],
        live_eve=False,
        retrieval=False,
        injection=False,
        tags=["meta", "access"],
        notes="Admission/meta — no Truth Drift hijack.",
    )
    yield CalibrateCase(
        id="hand_06",
        source="handwritten",
        tier="smoke",
        query="How did AI change between 2017 and 2026?",
        mode="compare",
        must_contain=["artificial intelligence"],
        expect_title_any=["Artificial intelligence", "Artificial Intelligence"],
        live_eve=True,
        tags=["truth_drift", "vague", "ai"],
        notes="Vague AI — must not collapse topic to bare 'truth'.",
    )
    yield CalibrateCase(
        id="hand_07",
        source="handwritten",
        tier="smoke",
        query="Compare artificial intelligence 2017 vs 2026",
        mode="compare",
        must_contain=["artificial intelligence"],
        expect_title_any=["Artificial intelligence", "Artificial Intelligence"],
        live_eve=True,
        tags=["truth_drift", "ai"],
    )


def _vague_descriptions() -> Iterator[CalibrateCase]:
    vague = [
        ("vague_01", "that Kate Bush song from Stranger Things", ["running up that hill"]),
        ("vague_02", "the 80s song in later Stranger Things", ["running up that hill"]),
        (
            "vague_03",
            "the song that came back because of the Netflix show about the upside down",
            ["running up that hill"],
        ),
        ("vague_04", "Kate Bush comeback song from the sci-fi series", ["running up that hill"]),
        ("vague_05", "what track did Max listen to in Stranger Things season 4", ["running up that hill"]),
    ]
    routing_gaps = {"vague_03", "vague_04", "dist_02"}
    for cid, query, must in vague:
        yield CalibrateCase(
            id=cid,
            source="driftbench_vague",
            tier="calibrate",
            query=query,
            must_contain=must,
            expect_title_any=["Running Up That Hill", "Stranger Things season 4"],
            injection=cid not in routing_gaps,
            tags=["vague", "conversational"] + (["routing_gap"] if cid in routing_gaps else []),
        )


def _redirect_aliases() -> Iterator[CalibrateCase]:
    aliases = [
        ("redirect_01", "running up that hill", "Running Up That Hill"),
        ("redirect_02", "Running Up That Hill (Kate Bush song)", "Running Up That Hill"),
        ("redirect_03", "RUTH Kate Bush", "Kate Bush"),  # acronym stretch — Phase B alias table
        ("redirect_04", "kate bush running up the hill", "Running Up That Hill"),
        ("redirect_05", "Kate Bush", "Kate Bush"),
    ]
    for cid, query, title in aliases:
        yield CalibrateCase(
            id=cid,
            source="driftbench_redirect",
            tier="calibrate",
            query=query,
            expect_title_any=[title],
            retrieval=True,
            injection=False,
            tags=["redirect", "alias"],
        )


def _parametric_distractors() -> Iterator[CalibrateCase]:
    yield CalibrateCase(
        id="dist_01",
        source="driftbench_distractor",
        tier="calibrate",
        query="what was Kate Bush's biggest hit after 2020?",
        must_contain=["running up that hill"],
        must_not_contain=["wow"],
        expect_title_any=["Running Up That Hill", "Kate Bush"],
        injection=False,
        tags=["parametric_distractor", "kate_bush", "routing_gap"],
    )
    yield CalibrateCase(
        id="dist_02",
        source="driftbench_distractor",
        tier="calibrate",
        query="name the Kate Bush song that charted again because of Netflix",
        must_contain=["running up that hill"],
        must_not_contain=["wow"],
        injection=False,
        tags=["parametric_distractor", "routing_gap"],
    )


def _disambiguation() -> Iterator[CalibrateCase]:
    cases = [
        ("disamb_01", "Mercury planet", ["Mercury (planet)", "Mercury"]),
        ("disamb_02", "Apple fruit company", ["Apple Inc.", "Apple"]),
        ("disamb_03", "Python programming language", ["Python (programming language)", "Python"]),
    ]
    for cid, query, titles in cases:
        yield CalibrateCase(
            id=cid,
            source="driftbench_disambiguation",
            tier="calibrate",
            query=query,
            expect_title_any=titles,
            injection=False,
            tags=["disambiguation"],
        )


def _snapshot_compare() -> Iterator[CalibrateCase]:
    yield CalibrateCase(
        id="snap_01",
        source="driftbench_snapshot",
        tier="calibrate",
        query="ChatGPT",
        mode="compare",
        year="2026",
        expect_title_any=["ChatGPT"],
        injection=False,
        retrieval=True,
        tags=["snapshot", "compare"],
        notes="Compare-years only when user asks explicitly; not for vague song Q.",
    )


def _external_placeholders() -> Iterator[CalibrateCase]:
    """Reserved slots for HF sample imports — filled by import script later."""
    for source, count, prefix in (
        ("ambigqa_sample", 50, "ambig"),
        ("redirectqa_sample", 50, "rqa"),
        ("qrecc_sample", 50, "qrecc"),
        ("faithdial_sample", 25, "fdial"),
        ("ragtruth_sample", 25, "rtruth"),
    ):
        for i in range(1, count + 1):
            yield CalibrateCase(
                id=f"{prefix}_{i:03d}",
                source=source,
                tier="import_pending",
                query="",
                injection=False,
                live_eve=False,
                retrieval=False,
                tags=["import_pending", source],
                notes=f"Populate via scripts/import-wiki-calibrate-samples.py ({source}).",
            )


def generate_cases(*, include_placeholders: bool = False) -> list[CalibrateCase]:
    cases: list[CalibrateCase] = []
    for factory in (
        _handwritten_failures,
        _vague_descriptions,
        _redirect_aliases,
        _parametric_distractors,
        _disambiguation,
        _snapshot_compare,
    ):
        cases.extend(factory())
    if include_placeholders:
        cases.extend(_external_placeholders())
    return cases


def case_to_json(case: CalibrateCase) -> dict[str, Any]:
    return {k: v for k, v in asdict(case).items() if v != "" and v != [] or k in {"query", "id"}}


def write_jsonl(cases: list[CalibrateCase], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        for case in cases:
            stream.write(json.dumps(case_to_json(case), ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate EMPIRE DriftBench seed JSONL")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--include-placeholders",
        action="store_true",
        help="Add 200 empty slots for AmbigQA/RedirectQA/etc. imports",
    )
    parser.add_argument("--merge-into", type=Path, default=None, help="Append non-duplicate ids into target JSONL")
    args = parser.parse_args(argv)

    cases = generate_cases(include_placeholders=args.include_placeholders)
    write_jsonl(cases, args.out)
    print(f"Wrote {len(cases)} cases to {args.out}")

    if args.merge_into:
        existing_ids: set[str] = set()
        merged: list[dict[str, Any]] = []
        if args.merge_into.is_file():
            for line in args.merge_into.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                existing_ids.add(str(row.get("id") or ""))
                merged.append(row)
        added = 0
        for case in cases:
            if case.id in existing_ids:
                continue
            merged.append(case_to_json(case))
            added += 1
        args.merge_into.parent.mkdir(parents=True, exist_ok=True)
        with args.merge_into.open("w", encoding="utf-8") as stream:
            for row in merged:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"Merged {added} new cases into {args.merge_into} ({len(merged)} total)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
