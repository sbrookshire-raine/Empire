from __future__ import annotations

import ast
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scripts" / "ensure-eve-build.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("ensure_eve_build", HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load Eve build helper.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ServiceLaunchConfigurationTests(unittest.TestCase):
    def test_worker_loads_local_configuration_before_importing_cognee(self) -> None:
        source = (ROOT / "pipeline" / "cognee_worker.py").read_text(encoding="utf-8")
        self.assertLess(source.index("load_cognee_env()"), source.index("import cognee"))

    def test_worker_ingest_uses_async_path_not_nested_event_loop(self) -> None:
        source = (ROOT / "pipeline" / "cognee_worker.py").read_text(encoding="utf-8")
        self.assertIn("from pipeline.ingest_files import ingest_files_async", source)
        self.assertIn("await ingest_files_async(", source)
        self.assertNotIn("asyncio.to_thread", source)
        self.assertNotIn("ingest_files,", source)

    def test_frontend_launches_venv_module_and_checks_memory_api(self) -> None:
        config = json.loads((ROOT / "config" / "services.json").read_text(encoding="utf-8"))
        frontend = config["services"]["frontend"]
        self.assertEqual(frontend["healthUrl"], "http://127.0.0.1:8080/api/memory/status")
        self.assertEqual(frontend["start"]["exe"], "venv/Scripts/python.exe")
        self.assertEqual(frontend["start"]["args"], ["-m", "frontend.serve"])
        self.assertEqual(frontend["start"]["cwd"], ".")

        stack = (ROOT / "scripts" / "start-stack.ps1").read_text(encoding="utf-8")
        standalone = (ROOT / "scripts" / "start-frontend.ps1").read_text(encoding="utf-8")
        for source in (stack, standalone):
            self.assertIn("venv", source.lower())
            self.assertIn("frontend.serve", source)
            self.assertIn("-m", source)
            self.assertIn("http://127.0.0.1:8080/api/memory/status", source)

    def test_eve_launches_built_production_server_on_loopback(self) -> None:
        config = json.loads((ROOT / "config" / "services.json").read_text(encoding="utf-8"))
        eve = config["services"]["eve"]
        self.assertEqual(
            eve["start"]["prepare"],
            {
                "exe": "venv/Scripts/python.exe",
                "args": ["scripts/ensure-eve-build.py"],
                "cwd": ".",
            },
        )
        self.assertEqual(
            eve["start"]["args"],
            ["exec", "--", "eve", "start", "--host", "127.0.0.1", "--port", "2000"],
        )
        serve_source = (ROOT / "frontend" / "serve.py").read_text(encoding="utf-8")
        self.assertIn('start.get("prepare")', serve_source)

        for name in ("start-stack.ps1", "start-eve.ps1"):
            source = (ROOT / "scripts" / name).read_text(encoding="utf-8")
            self.assertIn("ensure-eve-build.py", source)
            self.assertIn("eve", source)
            self.assertIn("start", source)
            self.assertIn("--host", source)
            self.assertIn("127.0.0.1", source)
            self.assertIn("--port", source)
            self.assertIn("2000", source)
            self.assertNotIn('"dev"', source)
        self.assertIn("Ready: http://127.0.0.1:8080/eve.html", stack_source())


def stack_source() -> str:
    return (ROOT / "scripts" / "start-stack.ps1").read_text(encoding="utf-8")


@unittest.skipUnless(HELPER.is_file(), "Eve build helper is not implemented yet")
class EveBuildStalenessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.helper = load_helper()

    def test_missing_or_older_output_requires_build(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "agent.ts"
            output = root / "index.mjs"
            source.write_text("source", encoding="utf-8")
            self.assertTrue(self.helper.build_required(output, [source]))

            output.write_text("output", encoding="utf-8")
            os.utime(output, (source.stat().st_mtime + 5, source.stat().st_mtime + 5))
            self.assertFalse(self.helper.build_required(output, [source]))

            os.utime(source, (output.stat().st_mtime + 5, output.stat().st_mtime + 5))
            self.assertTrue(self.helper.build_required(output, [source]))

    def test_collect_inputs_includes_agent_and_package_metadata_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "agent").mkdir()
            wanted = [
                root / "agent" / "agent.ts",
                root / "agent" / "instructions.ts",
                root / "package.json",
                root / "package-lock.json",
                root / "tsconfig.json",
            ]
            for path in wanted:
                path.write_text("x", encoding="utf-8")
            ignored = root / ".eve" / "generated.mjs"
            ignored.parent.mkdir()
            ignored.write_text("x", encoding="utf-8")

            self.assertEqual(set(self.helper.collect_inputs(root)), set(wanted))


class MechanicGreenLiveGateTests(unittest.TestCase):
    """The green gate must be able to *require* the live tier.

    `mechanic-green.ps1` had no `-Live` switch at all, so the live
    verification could never be run from the gate — and "green" meant
    "nothing was proven on the wire" without saying so. The live tier is
    therefore now requested with `-Live` and *enforced*: the report must
    say the live tier ran.
    """

    SCRIPT = ROOT / "scripts" / "mechanic-green.ps1"

    def source(self) -> str:
        return self.SCRIPT.read_text(encoding="utf-8")

    def test_gate_declares_a_live_switch(self) -> None:
        self.assertIn("[switch]$Live", self.source())

    def test_gate_runs_the_live_tier_when_requested(self) -> None:
        source = self.source()
        self.assertIn("verify-capabilities.ps1\") -Live", source)

    def test_gate_enforces_that_the_live_tier_actually_ran(self) -> None:
        """Requesting -Live and getting a silent no-op must be a FAILURE."""

        source = self.source()
        self.assertIn("live_ran", source)
        self.assertIn("live verification tier did not run", source)

    def test_gate_discards_a_stale_live_report_first(self) -> None:
        """A report left over from an earlier run must not satisfy the gate.

        Without the delete, a `live_ran: true` report on disk from a previous
        (successful) run would make the check pass without the live tier
        having run in this gate.
        """

        source = self.source()
        self.assertIn("Remove-Item $liveReport -Force", source)

    def test_gate_still_runs_the_offline_tier(self) -> None:
        source = self.source()
        self.assertIn("verify-capabilities.ps1\")", source)
        self.assertIn("unit tests", source)


class LiveHarnessToolbeltTests(unittest.TestCase):
    """The live harnesses must send a toolbelt the toolbelt path reads.

    They posted `{"toolbelt": {"active_tools": [...]}}`, which the toolbelt
    path never read — the nested object was silently dropped, so every
    routing measurement was taken against a toolbelt that was never
    actually applied.
    """

    HARNESSES = (
        ROOT / "scripts" / "test-eve-tools-playwright.py",
        ROOT / "scripts" / "smoke-eve-hands.py",
    )

    def test_harnesses_send_a_flat_active_tools_list(self) -> None:
        """Check the *code*, not the prose.

        The docstrings deliberately name the old nested shape to explain the
        defect, so a text search would flag the explanation as the bug.
        """

        for path in self.HARNESSES:
            with self.subTest(harness=path.name):
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
                nested = [
                    node
                    for node in ast.walk(tree)
                    if isinstance(node, ast.Dict)
                    and any(
                        isinstance(key, ast.Constant) and key.value == "toolbelt"
                        for key in node.keys
                        if key is not None
                    )
                ]
                self.assertEqual(
                    nested,
                    [],
                    f"{path.name} still posts the nested toolbelt shape",
                )
                flat = [
                    node
                    for node in ast.walk(tree)
                    if isinstance(node, ast.Dict)
                    and any(
                        isinstance(key, ast.Constant) and key.value == "active_tools"
                        for key in node.keys
                        if key is not None
                    )
                ]
                self.assertTrue(flat, f"{path.name} must send a flat active_tools list")

    def test_harnesses_restore_the_operator_toolbelt(self) -> None:
        """The toolbelt file is the operator's, not the harness's.

        Every harness that posts a session payload with a toolbelt makes the
        toolbelt path PERSIST it - the agent only ever reads the file. So a
        harness that does not restore the selection silently rewrites the
        Architect's toolbelt: running the wiki smoke used to turn the
        voice_presence limb OFF (E-07).

        The set of offenders is DISCOVERED, not listed: the old check named
        five harnesses and the next nine (a research bench, a wiki
        calibration, the browser probes...) were missed because the list was
        a snapshot. A harness that posts a toolbelt and does not guard it is
        now a failure wherever it lives.
        """

        scripts = sorted((ROOT / "scripts").rglob("*.py"))
        self.assertTrue(scripts, "no scripts found to check")
        checked = 0
        for path in scripts:
            source = path.read_text(encoding="utf-8")
            if not _posts_a_toolbelt(source):
                continue
            checked += 1
            with self.subTest(harness=path.name):
                self.assertIn(
                    "temporary_active_tools",
                    source,
                    f"{path.name} posts a toolbelt but never restores the "
                    "operator's selection - wrap it in "
                    "eve_toolbelt.temporary_active_tools(...)",
                )
        self.assertGreaterEqual(
            checked,
            10,
            "the discovery found suspiciously few toolbelt-posting harnesses",
        )

    def test_the_guard_is_importable_and_restores_byte_for_byte(self) -> None:
        """The guard is the mechanism the harnesses rely on.

        It must be importable from the repo root (the harnesses add the root
        to sys.path themselves) and must put the file back exactly as it was
        found - including the case where there was NO file.
        """

        from frontend import eve_toolbelt

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            original = b'{"active_tools": ["voice_presence"], "extra": 1}\n'
            path.write_bytes(original)
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                    self.assertEqual(
                        eve_toolbelt.load_active_tools(),
                        ["wiki_local"],
                    )
                self.assertEqual(path.read_bytes(), original)

    def test_the_guard_removes_a_file_it_created(self) -> None:
        """A missing file and a file holding [] are different states.

        The agent falls back to its default Voice + Wiki selection only when
        the file is ABSENT, so restoring "[]" would turn the voice limb off
        on a fresh install.
        """

        from frontend import eve_toolbelt

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                    self.assertTrue(path.exists())
                self.assertFalse(
                    path.exists(),
                    "the guard left a file behind that was not there before",
                )


def _posts_a_toolbelt(source: str) -> bool:
    """True when a script posts a toolbelt the toolbelt path will persist.

    Looked up in the CODE, not the prose: several harnesses explain the
    defect in their docstrings, and a text search would flag the
    explanation as the bug.
    """

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key in node.keys:
            if isinstance(key, ast.Constant) and key.value == "active_tools":
                return True
    return False


if __name__ == "__main__":
    unittest.main()
