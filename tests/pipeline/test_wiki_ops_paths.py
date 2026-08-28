from pipeline.wiki_ops_paths import CORPUS_TOTALS, validate_year


def test_validate_year_ok():
    assert validate_year("2017") == "2017"


def test_validate_year_rejects_traversal():
    import pytest

    with pytest.raises(ValueError):
        validate_year("../2017")


def test_corpus_total_2017():
    assert CORPUS_TOTALS["2017"] == 5347264
