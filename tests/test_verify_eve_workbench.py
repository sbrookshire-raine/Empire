from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify-eve-workbench.py"


def load_verifier():
    spec = importlib.util.spec_from_file_location("verify_eve_workbench", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load Eve Workbench verifier.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VerifierPresenceTests(unittest.TestCase):
    def test_verifier_exists_with_every_required_stage(self) -> None:
        self.assertTrue(SCRIPT.is_file(), "Eve Workbench verifier script is missing")
        verifier = load_verifier()
        self.assertEqual(
            verifier.STAGE_NAMES,
            (
                "V: Cognee storage",
                "Docker Postgres",
                "Ollama",
                "PocketBase",
                "Frontend Workbench",
                "Eve",
                "Memory upload",
                "Memory job ready",
                "Cognee recall",
                "Eve initial session",
                "Eve initial response",
                "Eve continuation",
                "Eve continuation response",
                "PocketBase tasks read-only",
            ),
        )

    def test_eve_uses_chat_completions_for_ollama_continuations(self) -> None:
        agent_source = (
            SCRIPT.parents[1]
            / "agents"
            / "empire-task-agent"
            / "agent"
            / "agent.ts"
        ).read_text(encoding="utf-8")
        self.assertIn("ollama.chat(modelId)", agent_source)
        self.assertIn("ollama.chat(selectedOllamaModel())", agent_source)
        self.assertIn("defineDynamic", agent_source)
        self.assertIn('"step.started"', agent_source)
        self.assertIn("selectedOllamaModel", agent_source)


@unittest.skipUnless(SCRIPT.is_file(), "verifier is not implemented yet")
class VerifierLogicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.verifier = load_verifier()

    def test_run_stages_stops_and_reports_exact_failed_stage(self) -> None:
        calls: list[str] = []
        output = io.StringIO()

        def pass_first() -> str:
            calls.append("first")
            return "ok"

        def fail_second() -> str:
            calls.append("second")
            raise RuntimeError("expected failure")

        def must_not_run() -> str:
            calls.append("third")
            return "bad"

        stages = (
            self.verifier.Stage("first", pass_first),
            self.verifier.Stage("missing stage behavior", fail_second),
            self.verifier.Stage("third", must_not_run),
        )
        result = self.verifier.run_stages(stages, output=output)

        self.assertEqual(result, "missing stage behavior")
        self.assertEqual(calls, ["first", "second"])
        self.assertIn("PASS first", output.getvalue())
        self.assertIn("FAIL missing stage behavior: expected failure", output.getvalue())
        self.assertIn("FAILED_STAGE=missing stage behavior", output.getvalue())

    def test_multipart_upload_is_unique_text_in_eve_memory(self) -> None:
        context = self.verifier.VerificationContext()
        content_type, body = self.verifier.build_multipart(
            filename=context.filename,
            marker=context.marker,
            dataset=context.dataset,
        )

        self.assertTrue(content_type.startswith("multipart/form-data; boundary="))
        self.assertIn(b'name="dataset"', body)
        self.assertIn(context.dataset.encode(), body)
        self.assertRegex(context.dataset, r"^eve_verify_[a-f0-9]{32}$")
        self.assertIn(b'name="full_graph"', body)
        self.assertIn(b"false", body)
        self.assertIn(context.filename.encode(), body)
        self.assertIn(context.marker.encode(), body)

    def test_stream_state_requires_waiting_and_assistant_text(self) -> None:
        state = self.verifier.StreamState()
        self.verifier.consume_stream_event(
            state,
            {"type": "message.appended", "data": {"messageDelta": "READY"}},
        )
        self.verifier.consume_stream_event(
            state,
            {
                "type": "session.waiting",
                "data": {"continuationToken": "next-token"},
                "_proxy": {"upstreamNextIndex": 7},
            },
        )

        self.assertTrue(state.waiting)
        self.assertEqual(state.assistant_text, "READY")
        self.assertEqual(state.continuation_token, "next-token")
        self.assertEqual(state.next_index, 7)

    def test_content_index_cleanup_removes_only_exact_verifier_entries(self) -> None:
        context = self.verifier.VerificationContext()
        context.job_id = "a" * 32
        with tempfile.TemporaryDirectory() as temporary:
            index_path = Path(temporary) / "content-index.json"
            target_key = f"{context.dataset}:target"
            same_dataset_other_job = f"{context.dataset}:other"
            unrelated = "primitives_test:keep"
            index_path.write_text(
                json.dumps(
                    {
                        target_key: {"upload_job_id": context.job_id},
                        same_dataset_other_job: {"upload_job_id": "other"},
                        unrelated: {"upload_job_id": context.job_id},
                    }
                ),
                encoding="utf-8",
            )

            removed = self.verifier.remove_content_index_entries(context, index_path)

            self.assertEqual(removed, 1)
            self.assertEqual(
                json.loads(index_path.read_text(encoding="utf-8")),
                {
                    same_dataset_other_job: {"upload_job_id": "other"},
                    unrelated: {"upload_job_id": context.job_id},
                },
            )

    def test_cleanup_runs_every_step_and_reports_failures(self) -> None:
        context = self.verifier.VerificationContext()
        output = io.StringIO()
        calls: list[str] = []

        def record(name: str, *, failure: bool = False):
            def operation(_context) -> str:
                calls.append(name)
                if failure:
                    raise RuntimeError(f"{name} failed")
                return name

            return operation

        with (
            patch.object(self.verifier, "_forget_verification_dataset", record("forget")),
            patch.object(
                self.verifier,
                "_cleanup_content_index",
                record("index", failure=True),
            ),
            patch.object(self.verifier, "_delete_mirrored_job", record("mirror")),
            patch.object(self.verifier, "_remove_local_artifacts", record("local")),
        ):
            failures = self.verifier.cleanup_context(context, output=output)

        self.assertEqual(calls, ["forget", "index", "mirror", "local"])
        self.assertEqual(failures, ["content index: index failed"])
        self.assertIn("CLEANUP FAIL content index: index failed", output.getvalue())

    def test_mirror_filter_keeps_only_exact_unique_filename(self) -> None:
        context = self.verifier.VerificationContext()
        payload = {
            "items": [
                {"id": "exact", "source_file": context.filename},
                {"id": "other", "source_file": f"prefix-{context.filename}"},
                {"id": "task", "title": context.filename},
            ]
        }
        self.assertEqual(
            self.verifier.exact_mirror_ids(payload, context.filename),
            ["exact"],
        )

    def test_mirror_cleanup_deletes_exact_record_and_confirms_absence(self) -> None:
        context = self.verifier.VerificationContext()
        responses = [
            ({"items": [{"id": "mirror-id", "source_file": context.filename}]}, {}),
            ({"items": []}, {}),
        ]
        with (
            patch.object(self.verifier, "_json_request", side_effect=responses) as query,
            patch.object(
                self.verifier,
                "_request",
                return_value=(204, {}, b""),
            ) as delete,
        ):
            detail = self.verifier._delete_mirrored_job(context)

        self.assertEqual(query.call_count, 2)
        self.assertIn("1 exact", detail)
        self.assertIn("/mirror-id", delete.call_args.args[0])
        self.assertEqual(delete.call_args.kwargs["method"], "DELETE")


if __name__ == "__main__":
    unittest.main()
