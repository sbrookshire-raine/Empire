"""Unit tests for the REA Bin-1 skill runner.

The runner is the trust boundary between a model-supplied request and a local
script. These tests cover the parts that can silently go wrong:

- the allowlist (only the six approved skills exist; the other sixteen do not),
- path jailing (an input outside the scratch root is refused, not rewritten),
- the interpreter (the result reports what actually ran, and never the broken
  `python3` Store alias on this host),
- the upstream scripts themselves (a real pass, and a real failure).
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from pipeline import rea_skills

VENDOR = Path(__file__).resolve().parents[2] / "vendor" / "rea-skills"

DEFERRED_BIN3 = {
    "agent-memory-architecture",
    "ai-experience-dialogue",
    "intake-triage",
    "rea-android-apk-trace",
    "rea-android-device-adb",
    "rea-browser-runtime-observation",
    "rea-firmware-extraction",
    "rea-investigation-setup",
    "rea-managed-dotnet-trace",
    "rea-mobile-package-formats",
    "rea-native-function-recovery",
    "rea-packet-and-signal-capture",
    "rea-runtime-instrumentation",
    "rea-static-js-electron-trace",
    "source-capture",
    "tool-model-extraction",
}


class AllowlistTests(unittest.TestCase):
    def test_exactly_six_skills_are_approved(self) -> None:
        self.assertEqual(len(rea_skills.BIN1_SKILLS), 6)
        self.assertEqual(
            set(rea_skills.BIN1_SKILLS),
            {
                "claim-ledger",
                "rea-evidence-verification",
                "rea-reconstruction-verification",
                "rea-target-free-readers",
                "rea-web-app-reconstruction",
                "repo-forkdiving",
            },
        )

    def test_the_deferred_bin3_skills_are_not_vendored(self) -> None:
        """The other sixteen upstream skills must not be reachable at all."""

        self.assertEqual(len(DEFERRED_BIN3), 16)
        for name in DEFERRED_BIN3:
            with self.subTest(name=name):
                self.assertNotIn(name, rea_skills.BIN1_SKILLS)
                self.assertFalse((VENDOR / name).exists())

    def test_only_repo_forkdiving_needs_the_network(self) -> None:
        self.assertEqual(rea_skills.NETWORK_SKILLS, frozenset({"repo-forkdiving"}))

    def test_run_script_refuses_a_skill_outside_the_allowlist(self) -> None:
        result = rea_skills.run_script("rea-native-function-recovery", "x.py", [])
        self.assertFalse(result["ok"])
        self.assertIn("not in the approved Bin-1 set", result["error"])

    def test_list_reports_six_skills(self) -> None:
        listing = rea_skills.list_skills()
        self.assertTrue(listing["ok"])
        self.assertEqual(listing["count"], 6)
        self.assertEqual(listing["deferred_bin3_count"], 16)


class InterpreterTests(unittest.TestCase):
    def test_the_store_alias_stub_is_recognised(self) -> None:
        self.assertTrue(
            rea_skills._is_store_stub(
                r"C:\Users\me\AppData\Local\Microsoft\WindowsApps\python3.exe"
            )
        )
        self.assertFalse(rea_skills._is_store_stub(r"C:\Python311\python.exe"))

    def test_resolve_python_prefers_the_repo_venv(self) -> None:
        resolved = rea_skills.resolve_python()
        self.assertIsNotNone(resolved)
        assert resolved is not None
        self.assertNotIn("windowsapps", resolved.lower())
        self.assertTrue(Path(resolved).is_file())


class PathJailTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.scratch = Path(self._tmp.name)
        os.environ["EMPIRE_REA_SCRATCH_DIR"] = str(self.scratch)
        self.addCleanup(os.environ.pop, "EMPIRE_REA_SCRATCH_DIR", None)

    def test_evidence_file_outside_the_scratch_root_is_refused(self) -> None:
        outside = self.scratch.parent / "definitely-outside.json"
        outside.write_text("{}", encoding="utf-8")
        self.addCleanup(outside.unlink, True)
        result = rea_skills.verify_evidence([str(outside)])
        self.assertFalse(result["ok"])
        self.assertIn("outside the declared root", result["error"])

    def test_config_dir_outside_the_scratch_root_is_refused(self) -> None:
        result = rea_skills.audit_reconstruction(str(Path("C:/Windows/System32")))
        self.assertFalse(result["ok"])
        self.assertIn("outside the declared root", result["error"])

    def test_work_dir_outside_the_scratch_root_is_refused(self) -> None:
        result = rea_skills.run_script(
            "rea-target-free-readers",
            "build_fixtures.py",
            ["--out", "x"],
            work_dir=str(Path("C:/Windows")),
        )
        self.assertFalse(result["ok"])
        self.assertIn("outside the declared root", result["error"])

    def test_a_command_path_outside_the_scratch_root_is_refused(self) -> None:
        with self.assertRaises(Exception):
            rea_skills._jail_command(
                "python C:/Windows/System32/cmd.exe", self.scratch
            )


class UpstreamScriptTests(unittest.TestCase):
    """The vendored scripts, run for real against their own fixtures."""

    @classmethod
    def setUpClass(cls) -> None:
        if not (VENDOR / "rea-web-app-reconstruction" / "examples" / "ref.py").is_file():
            raise unittest.SkipTest("vendored REA skill examples are not present")

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.scratch = Path(self._tmp.name)
        os.environ["EMPIRE_REA_SCRATCH_DIR"] = str(self.scratch)
        self.addCleanup(os.environ.pop, "EMPIRE_REA_SCRATCH_DIR", None)
        examples = VENDOR / "rea-web-app-reconstruction" / "examples"
        for item in examples.iterdir():
            if item.is_file():
                shutil.copy2(item, self.scratch / item.name)
        self.python = rea_skills.resolve_python()

    def test_parity_passes_for_a_matching_reconstruction(self) -> None:
        result = rea_skills.parity_check(
            f"{self.python} ref.py",
            f"{self.python} candidate.py",
            str(self.scratch / "scenarios.json"),
            work_dir=str(self.scratch),
        )
        self.assertTrue(result["ok"], result.get("error"))
        report = result["result"]
        self.assertEqual(report["status"], "comparisons-passed")
        self.assertEqual(report["candidate"]["failed"], 0)

    def test_parity_fails_for_a_broken_reconstruction(self) -> None:
        """The harness must be able to fail — a green light that cannot go red proves nothing."""

        result = rea_skills.parity_check(
            f"{self.python} ref.py",
            f"{self.python} candidate_broken.py",
            str(self.scratch / "scenarios.json"),
            work_dir=str(self.scratch),
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["exit_code"], 1)
        self.assertEqual(result["result"]["status"], "failed")

    def test_evidence_verification_passes_on_the_good_record(self) -> None:
        examples = VENDOR / "rea-evidence-verification" / "examples"
        target = self.scratch / "evidence"
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(examples / "evidence.json", target / "evidence.json")
        shutil.copy2(examples / "claims.json", target / "claims.json")
        result = rea_skills.verify_evidence(
            [str(target / "evidence.json")], str(target / "claims.json")
        )
        self.assertTrue(result["ok"], result.get("error"))
        self.assertTrue(result["result"]["passed"])

    def test_reconstruction_audit_passes_on_the_good_config(self) -> None:
        config = VENDOR / "rea-reconstruction-verification" / "examples" / "config"
        target = self.scratch / "reconstruction"
        target.mkdir(parents=True, exist_ok=True)
        shutil.copytree(config, target / "config", dirs_exist_ok=True)
        result = rea_skills.audit_reconstruction(str(target / "config"))
        self.assertTrue(result["ok"], result.get("error"))
        self.assertTrue(result["result"]["passed"])

    def test_build_fixtures_produces_local_readers(self) -> None:
        result = rea_skills.build_fixtures()
        self.assertTrue(result["ok"], result.get("error"))
        built = result["result"]
        self.assertIn("sqlite", built)
        self.assertIn("wasm", built)
        self.assertTrue(Path(built["sqlite"]["path"]).is_file())

    def test_the_vendored_tree_is_never_modified_by_a_run(self) -> None:
        """Create-only: upstream files stay byte-identical after a run."""

        before = {path: path.read_bytes() for path in VENDOR.rglob("*.py")}
        rea_skills.build_fixtures()
        after = {path: path.read_bytes() for path in VENDOR.rglob("*.py")}
        self.assertEqual(before, after)


class ReportShapeTests(unittest.TestCase):
    def test_a_result_reports_the_interpreter_that_ran(self) -> None:
        result = rea_skills.run_script(
            "rea-target-free-readers", "build_fixtures.py", ["--out", "unused"]
        )
        self.assertIn("interpreter", result)
        self.assertTrue(result["interpreter"])

    def test_a_missing_script_fails_closed(self) -> None:
        result = rea_skills.run_script("rea-target-free-readers", "nope.py", [])
        self.assertFalse(result["ok"])
        self.assertIn("not found", result["error"])


class VendoredTreeIntegrityTests(unittest.TestCase):
    """The vendored tree must stay byte-identical to the upstream bundle.

    The bundle ships its own SHA-256 manifest. Checking against it here means a
    tampered or half-copied file fails the build rather than quietly changing
    what EMPIRE runs.
    """

    def test_the_bundle_manifest_is_vendored(self) -> None:
        self.assertTrue((VENDOR / "manifest.json").is_file())
        self.assertTrue((VENDOR / "LICENSE").is_file())

    def test_every_vendored_file_matches_the_upstream_manifest(self) -> None:
        manifest = json.loads((VENDOR / "manifest.json").read_text(encoding="utf-8"))
        skills = manifest.get("skills") or {}
        checked = 0
        problems: list[str] = []
        for name, entry in skills.items():
            if name not in rea_skills.BIN1_SKILLS:
                continue
            for record in entry.get("files") or []:
                rel = str(record.get("path") or "")
                expected = str(record.get("sha256") or "")
                path = VENDOR / name / rel
                if not path.is_file():
                    problems.append(f"{name}/{rel}: missing")
                    continue
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                checked += 1
                if actual != expected:
                    problems.append(f"{name}/{rel}: sha256 differs")
        self.assertTrue(checked, "no vendored files were checked")
        self.assertEqual(problems, [], f"vendored tree drifted from upstream: {problems}")

    def test_the_vendored_tree_contains_no_bin3_skill(self) -> None:
        manifest = json.loads((VENDOR / "manifest.json").read_text(encoding="utf-8"))
        upstream_skills = set(manifest.get("skills") or {})
        self.assertEqual(len(upstream_skills), 22)
        vendored = {p.name for p in VENDOR.iterdir() if p.is_dir()}
        self.assertEqual(vendored, set(rea_skills.BIN1_SKILLS))
        self.assertEqual(
            upstream_skills - vendored,
            DEFERRED_BIN3,
            "the deferred set must be exactly the 16 skills we did not vendor",
        )


if __name__ == "__main__":
    unittest.main()
