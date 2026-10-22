"""Wiki green path — extract + bounded prefetch block."""

from __future__ import annotations

from unittest.mock import patch

from frontend import wiki_drift_api
from frontend.wiki_green_path import build_green_path_block


def test_extract_albums_released_by_beach_boys() -> None:
    q = (
        "Go to my local Wikipedia and find what are the albums "
        "released by the Beach Boys."
    )
    assert wiki_drift_api.extract_search_query(q) == "The Beach Boys discography"


def test_green_path_block_when_lookup_succeeds() -> None:
    q = "tell me the names of the Beach Boys albums"
    fake_block = "[[EMPIRE_WIKI_EXTRACT]]\nStudio albums: Pet Sounds\n"
    with patch("frontend.wiki_green_path.load_active_tools", return_value=["wiki_local"]):
        with patch(
            "frontend.wiki_green_path._call_with_timeout",
            return_value=(fake_block, {}),
        ):
            out = build_green_path_block(q)
    assert "[[EMPIRE_WIKI_GREEN]]" in out
    assert "Pet Sounds" in out


def test_green_path_after_companion_and_pulse_enrich() -> None:
    import tempfile
    from pathlib import Path

    from frontend import companion_api, eve_toolbelt, resource_pulse_api
    from frontend.companion_api import extract_user_message

    q = (
        "Go to my local Wikipedia and find what are the albums "
        "released by the Beach Boys."
    )
    payload = {"message": q, "active_tools": ["wiki_local"]}
    # `apply_active_tools` PERSISTS what it is given, so it must not write
    # the operator's toolbelt file from a test.
    with tempfile.TemporaryDirectory() as tmp:
        with patch.object(
            eve_toolbelt, "_toolbelt_path", return_value=Path(tmp) / "eve-toolbelt.json"
        ):
            payload = eve_toolbelt.apply_active_tools(payload)
    bare = str(payload["message"]).strip()
    payload = companion_api.enrich_eve_message_payload(payload)
    with patch(
        "pipeline.resource_pulse.pulse",
        return_value={
            "ok": True,
            "summary": "Headroom OK.",
            "headroom_ok": True,
            "can_admit_now": [],
            "inventory": {"effective_tools": ["wiki_local"]},
            "gpu_lease": {"tenant": "idle"},
        },
    ):
        payload = resource_pulse_api.enrich_eve_message_payload(payload)
    assert extract_user_message(payload["message"]) == q
    assert bare == q
    # The green path only runs for a wiki ask when wiki_local is active, and
    # the toolbelt file is a temp file under test - so say so explicitly
    # instead of depending on what the operator happens to have selected.
    with patch("frontend.wiki_green_path.load_active_tools", return_value=["wiki_local"]):
        with patch(
            "frontend.wiki_green_path._call_with_timeout",
            return_value=("[[EMPIRE_WIKI_EXTRACT]]\nPet Sounds\n", {}),
        ):
            out = build_green_path_block(bare)
    assert "[[EMPIRE_WIKI_GREEN]]" in out
