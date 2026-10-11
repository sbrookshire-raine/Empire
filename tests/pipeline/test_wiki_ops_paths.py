from pathlib import Path

from pipeline import wiki_ops_paths
from pipeline.wiki_ops_paths import CORPUS_TOTALS, validate_year


def test_validate_year_ok():
    assert validate_year("2017") == "2017"


def test_validate_year_rejects_traversal():
    import pytest

    with pytest.raises(ValueError):
        validate_year("../2017")


def test_corpus_total_2017():
    assert CORPUS_TOTALS["2017"] == 5347264


def test_reports_root_env_override(monkeypatch, tmp_path):
    monkeypatch.setenv("EMPIRE_WIKI_REPORTS_ROOT", str(tmp_path / "custom"))
    assert wiki_ops_paths.reports_root() == tmp_path / "custom"


def test_reports_root_falls_back_to_d_when_i_not_wiki_storage(monkeypatch, tmp_path):
    monkeypatch.delenv("EMPIRE_WIKI_REPORTS_ROOT", raising=False)
    monkeypatch.setattr(wiki_ops_paths, "_empire_wiki_data_on_drive_i", lambda: False)
    assert wiki_ops_paths.reports_root() == Path(r"D:\EMPIRE_DATA\wiki-reports")
