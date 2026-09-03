from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path


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
            self.assertIn("venv\\Scripts\\python.exe", source)
            self.assertIn('"-m", "frontend.serve"', source)
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
            self.assertIn('"start", "--host", "127.0.0.1", "--port", "2000"', source)
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


if __name__ == "__main__":
    unittest.main()
