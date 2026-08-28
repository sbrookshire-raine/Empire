import inspect

from pipeline import wiki_report_export
from pipeline.wiki_report_export import new_titles_diff, sum_docs_processed


def test_sum_complete_prefers_total():
    cp = {
        "batches": {
            "2017/batch_00000": {"processed": 100, "total": 10000, "status": "complete"},
            "2017/batch_00001": {"processed": 50, "status": "partial", "next_index": 50},
        }
    }
    assert sum_docs_processed(cp, "2017") == 10050


def test_new_titles_set_difference():
    prev = {"A", "B"}
    current = {"B", "C", "D"}
    assert new_titles_diff(prev, current) == {"C", "D"}


def test_rebuild_titles_param_does_not_shadow_catalog_fn():
    """Regression: bool param named rebuild_titles made catalog call raise
    'bool' object is not callable during maintenance --rebuild-titles.
    """
    sig = inspect.signature(wiki_report_export.export_report)
    assert "do_rebuild_titles" in sig.parameters
    assert "rebuild_titles" not in sig.parameters
    assert callable(wiki_report_export.rebuild_titles_catalog)
    src = inspect.getsource(wiki_report_export.export_report)
    assert "rebuild_titles_catalog(" in src
    # Ensure we never call a name that is only the bool flag.
    assert "rebuild_titles(" not in src.replace("rebuild_titles_catalog(", "").replace(
        "do_rebuild_titles", ""
    )
