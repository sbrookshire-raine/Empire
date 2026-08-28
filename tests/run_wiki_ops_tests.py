"""Minimal test runner (pytest blocked by app control on pip)."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

failures = 0


def check(name: str, fn) -> None:
    global failures
    try:
        fn()
        print(f"PASS {name}")
    except Exception as exc:  # noqa: BLE001
        failures += 1
        print(f"FAIL {name}: {exc}")
        traceback.print_exc()


def main() -> int:
    from pipeline.wiki_ops_paths import CORPUS_TOTALS, overnight_pid_alive, validate_year
    from pipeline.wiki_title_matcher import (
        decide_match,
        normalize_text,
        score_subject_against_titles,
    )

    check("validate_year", lambda: assert_eq(validate_year("2017"), "2017"))

    def bad_year() -> None:
        try:
            validate_year("../2017")
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

    check("validate_year_reject", bad_year)
    check("corpus", lambda: assert_eq(CORPUS_TOTALS["2017"], 5347264))
    print("INFO overnight_alive=", overnight_pid_alive("2017"))

    fixture = json.loads(
        Path("tests/pipeline/fixtures/wiki_title_catalog.json").read_text(encoding="utf-8")
    )
    check(
        "normalize",
        lambda: assert_eq(normalize_text("  Battle   of  Cambrai "), "battle of cambrai"),
    )

    def cambrai() -> None:
        decision = decide_match(score_subject_against_titles("Battle of Cambrai", fixture))
        assert decision["decision"] == "auto"
        assert decision["primary"].title == "Cambrai"

    check("cambrai_auto", cambrai)

    def guitar() -> None:
        decision = decide_match(score_subject_against_titles("guitar", fixture))
        assert decision["decision"] == "needs_confirm", decision
        assert len(decision["candidates"]) >= 2

    check("guitar_confirm", guitar)

    def unmatched() -> None:
        decision = decide_match(score_subject_against_titles("zzzxnotapage999", fixture))
        assert decision["decision"] == "unmatched"

    check("unmatched", unmatched)

    from pipeline.wiki_priority_subjects import (
        add_subjects,
        delete_subject,
        empty_queue,
        load_subjects,
        move_subject,
        patch_subject,
        save_subjects,
    )
    from pipeline.wiki_report_export import new_titles_diff, sum_docs_processed

    def subjects_flow() -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "s.json"
            doc = add_subjects(empty_queue(), ["Alpha", "Beta", "Gamma"], updated_by="t")
            save_subjects(doc, path)
            doc = load_subjects(path)
            beta = doc["subjects"][1]["id"]
            doc = move_subject(doc, beta, "up")
            assert [s["subject"] for s in doc["subjects"]] == ["Beta", "Alpha", "Gamma"]
            assert [s["rank"] for s in doc["subjects"]] == [1, 2, 3]
            sid = doc["subjects"][0]["id"]
            doc = delete_subject(doc, sid)
            assert len(doc["subjects"]) == 2

    check("subjects_move_delete", subjects_flow)

    def edit_reset() -> None:
        doc = add_subjects(
            empty_queue(), [{"subject": "guitar", "intent": "demo"}], updated_by="t"
        )
        doc["subjects"][0]["status"] = "needs_confirm"
        doc["subjects"][0]["candidates"] = [{"title": "Guitar"}]
        sid = doc["subjects"][0]["id"]
        doc = patch_subject(doc, sid, subject="Bass guitar")
        assert doc["subjects"][0]["status"] == "pending"
        assert doc["subjects"][0]["candidates"] == []
        doc = patch_subject(doc, sid, intent="new")
        assert doc["subjects"][0]["status"] == "pending"
        assert doc["subjects"][0]["intent"] == "new"

    check("edit_reset", edit_reset)

    check(
        "sum_docs",
        lambda: assert_eq(
            sum_docs_processed(
                {
                    "batches": {
                        "2017/batch_00000": {
                            "processed": 100,
                            "total": 10000,
                            "status": "complete",
                        },
                        "2017/batch_00001": {
                            "processed": 50,
                            "status": "partial",
                        },
                    }
                },
                "2017",
            ),
            10050,
        ),
    )
    check(
        "new_diff",
        lambda: assert_eq(new_titles_diff({"A", "B"}, {"B", "C", "D"}), {"C", "D"}),
    )

    from pipeline.wiki_priority_resolved import append_resolved, drain_awaiting, list_awaiting

    def drain() -> None:
        with tempfile.TemporaryDirectory() as td:
            os.environ["EMPIRE_WIKI_REPORTS_ROOT"] = td
            Path(td, "2017").mkdir()
            append_resolved(
                "2017",
                {
                    "subject_id": "s1",
                    "subject": "A",
                    "subject_rank": 1,
                    "title": "A",
                    "path": "a.md",
                    "match_score": 1,
                    "match_reason": "exact",
                },
            )
            append_resolved(
                "2017",
                {
                    "subject_id": "s2",
                    "subject": "B",
                    "subject_rank": 2,
                    "title": "B",
                    "path": "b.md",
                    "match_score": 1,
                    "match_reason": "user_confirm",
                },
            )
            calls: list[str] = []
            result = drain_awaiting(
                "2017", lambda row: (calls.append(row["title"]) or "ingested")
            )
            assert result["drained"] == 2
            assert calls == ["A", "B"]
            assert list_awaiting("2017") == []

    check("drain", drain)

    from pipeline.wiki_codex_seed import parse_codex_primitives
    from pipeline.wiki_priority_resolve import resolve_pending_subjects
    from pipeline.wiki_priority_resolved import load_resolved_lines

    sample = (
        "## I. CYBERNETICS\n\n"
        "1. **The Reinforcing Loop:** Output feeds back.\n"
        "2. **The Balancing Loop:** Counter.\n"
    )
    check("parse_codex", lambda: assert_eq(len(parse_codex_primitives(sample)), 2))

    def resolve_tests() -> None:
        with tempfile.TemporaryDirectory() as td:
            os.environ["EMPIRE_PRIORITY_SUBJECTS"] = str(Path(td) / "subj.json")
            os.environ["EMPIRE_WIKI_REPORTS_ROOT"] = str(Path(td) / "reports")
            Path(td, "reports", "2017").mkdir(parents=True)
            doc = add_subjects(empty_queue("2017"), ["Cambrai"], updated_by="t")
            save_subjects(doc, Path(td) / "subj.json")
            summary = resolve_pending_subjects("2017", catalog=fixture)
            assert summary["counts"]["auto"] == 1
            assert load_resolved_lines("2017")[0]["title"] == "Cambrai"
            doc = add_subjects(empty_queue("2017"), ["guitar"], updated_by="t")
            save_subjects(doc, Path(td) / "subj.json")
            (Path(td) / "reports" / "2017" / "priority_resolved.jsonl").write_text(
                "", encoding="utf-8"
            )
            summary2 = resolve_pending_subjects("2017", catalog=fixture)
            assert summary2["counts"]["needs_confirm"] == 1
            assert summary2["counts"]["resolved_appended"] == 0

    check("resolve", resolve_tests)

    print("\nTOTAL FAILURES", failures)
    return 1 if failures else 0


def assert_eq(a, b) -> None:
    if a != b:
        raise AssertionError(f"{a!r} != {b!r}")


if __name__ == "__main__":
    raise SystemExit(main())
