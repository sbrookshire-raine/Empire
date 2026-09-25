"""Research desk: the deferred contract has to be bounded, honest, and safe.

The desk exists because her window is ~one long article (docs/PLACEMENT.md): a job is created and
returns immediately, a worker fetches on CPU, and she reads a **bounded digest** later. These tests
use a stub fetcher, so nothing here touches the network or the real desk.
"""

from __future__ import annotations

import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import research_desk

PAGE = ("The archive holds each page as markdown with a lead section. " * 60).strip()


def stub_fetcher(title: str = "Stub page", text: str = PAGE):
    def _fetch(url: str, cache_dir: Path, note: str) -> dict:
        cache_dir.mkdir(parents=True, exist_ok=True)
        path = cache_dir / (url.rstrip("/").rsplit("/", 1)[-1] or "page")
        written = path.with_suffix(".md")
        written.write_text(f"# {title}\n\n{text}\n", encoding="utf-8")
        return {"ok": True, "title": title, "final_url": url, "path": str(written), "body": text}

    return _fetch


def failing_fetcher(url: str, cache_dir: Path, note: str) -> dict:
    return {"ok": False, "error": "connection refused"}


class DeskTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.desk = Path(self._tmp.name) / "desk"
        patcher = patch.dict(os.environ, {"EMPIRE_RESEARCH_DESK": str(self.desk)})
        patcher.start()
        self.addCleanup(patcher.stop)


class DeskContractTests(DeskTestCase):
    def test_start_returns_immediately_with_a_job_id(self) -> None:
        result = research_desk.start("what changed in yt-dlp", ["https://example.org/a"], spawn=False)
        self.assertTrue(result["ok"], result)
        self.assertTrue(research_desk.JOB_ID_RE.match(result["job_id"]), result["job_id"])
        self.assertTrue(Path(result["desk_path"]).is_dir())
        self.assertIn("research_read", result["next"])

    def test_full_cycle_is_done_and_readable(self) -> None:
        started = research_desk.start(
            "compare two pages",
            ["https://example.org/one", "https://example.org/two"],
            spawn=False,
        )
        job = started["job_id"]
        collected = research_desk.collect(
            job, fetcher=stub_fetcher("Example page", "Short body about the example page.")
        )
        self.assertEqual(collected["status"], "done", collected)
        self.assertEqual(len(collected["sources"]), 2)

        state = research_desk.status(job)
        self.assertTrue(state["has_digest"])
        self.assertEqual(state["status"], "done")

        payload = research_desk.read(job)
        self.assertTrue(payload["ok"], payload)
        self.assertIn("Example page", payload["digest"])
        self.assertIn("https://example.org/one", payload["digest"])
        self.assertFalse(payload["more_available"])

    def test_read_is_bounded_and_says_so(self) -> None:
        job = research_desk.start("long pages", ["https://example.org/big"], spawn=False)["job_id"]
        research_desk.collect(job, fetcher=stub_fetcher())
        payload = research_desk.read(job, budget=500)
        self.assertTrue(payload["ok"], payload)
        self.assertGreater(payload["chars"], 500, "the desk keeps the full text")
        self.assertTrue(payload["more_available"])
        self.assertIn("digest truncated", payload["digest"])
        self.assertLessEqual(len(payload["digest"]), 600)

    def test_a_query_without_urls_searches_then_fetches(self) -> None:
        """E-35: the desk finds its own URLs now, and records which results it chose."""

        job = research_desk.start("what is new in searxng", spawn=False)["job_id"]
        collected = research_desk.collect(
            job,
            fetcher=stub_fetcher("Found page", "Short page body."),
            searcher=lambda query, limit: {"ok": True, "urls": ["https://example.org/found"]},
        )
        self.assertEqual(collected["status"], "done", collected)
        state = research_desk.status(job)
        self.assertIn("searched and took the top 1", state["note"])
        self.assertTrue(state["has_digest"])
        self.assertIn("https://example.org/found", research_desk.read(job)["digest"])

    def test_search_unavailable_is_honest_about_it(self) -> None:
        """A down instance must never turn into an invented answer."""

        job = research_desk.start("no instance running", spawn=False)["job_id"]
        collected = research_desk.collect(
            job,
            fetcher=stub_fetcher(),
            searcher=lambda query, limit: {
                "ok": False,
                "error": "SearXNG is not reachable",
                "hint": "start it with scripts/start-searxng.ps1",
            },
        )
        self.assertEqual(collected["status"], "needs_sources")
        state = research_desk.status(job)
        self.assertIn("not reachable", state["note"])
        self.assertIn("start-searxng.ps1", state["note"])
        self.assertFalse(state["has_digest"])
        payload = research_desk.read(job)
        self.assertFalse(payload["ok"])
        self.assertIn("no digest yet", payload["error"])

    def test_one_bad_url_leaves_a_partial_desk_with_the_reason(self) -> None:
        job = research_desk.start(
            "mixed", ["https://example.org/good", "https://example.org/bad"], spawn=False
        )["job_id"]
        calls = {"n": 0}

        def flaky(url: str, cache_dir: Path, note: str) -> dict:
            calls["n"] += 1
            return stub_fetcher()(url, cache_dir, note) if calls["n"] == 1 else failing_fetcher(
                url, cache_dir, note
            )

        collected = research_desk.collect(job, fetcher=flaky)
        self.assertEqual(collected["status"], "partial")
        self.assertIn("connection refused", research_desk.status(job)["note"])

    def test_every_url_failing_is_failed_not_done(self) -> None:
        job = research_desk.start("doomed", ["https://example.org/x"], spawn=False)["job_id"]
        collected = research_desk.collect(job, fetcher=failing_fetcher)
        self.assertEqual(collected["status"], "failed")
        self.assertFalse(research_desk.status(job)["has_digest"])


class DeskSafetyTests(DeskTestCase):
    def test_a_job_id_is_never_a_path(self) -> None:
        for bad in ("../../secrets", "a/b", "..", "", "not-a-job-id"):
            with self.subTest(bad=bad):
                self.assertFalse(research_desk.status(bad)["ok"], bad)
                self.assertFalse(research_desk.read(bad)["ok"], bad)
                self.assertFalse(research_desk.collect(bad)["ok"], bad)

    def test_unknown_job_reports_cleanly(self) -> None:
        payload = research_desk.status("20260924-153012-abcdef")
        self.assertFalse(payload["ok"])
        self.assertIn("no job", payload["error"])

    def test_open_jobs_lists_only_unfinished_work(self) -> None:
        waiting = research_desk.start("still running", ["https://example.org/a"], spawn=False)["job_id"]
        finished = research_desk.start("already done", ["https://example.org/b"], spawn=False)["job_id"]
        research_desk.collect(finished, fetcher=stub_fetcher())

        open_ids = [job["job_id"] for job in research_desk.open_jobs()]
        self.assertIn(waiting, open_ids)
        self.assertNotIn(finished, open_ids)

    def test_expire_is_a_dry_run_unless_asked(self) -> None:
        job = research_desk.start("old job", spawn=False)["job_id"]
        meta_path = self.desk / job / "meta.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["created"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 3 * 86_400))
        meta_path.write_text(json.dumps(meta), encoding="utf-8")

        dry = research_desk.expire(days=1)
        self.assertEqual(dry["expired"], [job])
        self.assertFalse(dry["applied"])
        self.assertTrue(meta_path.is_file(), "a dry run must not delete")

        applied = research_desk.expire(days=1, apply=True)
        self.assertTrue(applied["applied"])
        self.assertFalse((self.desk / job).exists())

    def test_fresh_jobs_survive_expiry(self) -> None:
        job = research_desk.start("fresh", spawn=False)["job_id"]
        self.assertEqual(research_desk.expire(days=1)["expired"], [])
        self.assertTrue((self.desk / job).is_dir())


if __name__ == "__main__":
    unittest.main()

