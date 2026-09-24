"""Cross-language config parity: the Python and TypeScript sides must not drift.

Measured 2026-09-24: `frontend/ollama_chat_profiles.SHARED_NUM_CTX` said 8192 while
`agents/empire-task-agent/agent/lib/ollama-config.ts` said 16384 and the baked models
(`config/ollama/Modelfile.*`) said 16384 — and AGENTS.md explicitly requires them to match.
Nobody notices that by reading; this test notices by parsing.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from frontend.ollama_chat_profiles import CHAT_MODES, SHARED_NUM_CTX

ROOT = Path(__file__).resolve().parents[2]
TS_CONFIG = ROOT / "agents" / "empire-task-agent" / "agent" / "lib" / "ollama-config.ts"
MODELFILE_DIR = ROOT / "config" / "ollama"

TS_NUM_CTX = re.compile(r"export const SHARED_NUM_CTX = ([\d_]+)")
TS_MODE_BLOCK = re.compile(r'\bid:\s*"([a-z_]+)",')
TS_MODEL = re.compile(r'\bmodel:\s*"([^"]+)"')
MODELFILE_CTX = re.compile(r"^PARAMETER num_ctx (\d+)\s*$", re.MULTILINE)
MODELFILE_FROM = re.compile(r"^FROM (\S+)\s*$", re.MULTILINE)


def _number(raw: str) -> int:
    return int(raw.replace("_", ""))


def _ts_mode_models(text: str) -> dict[str, str]:
    """Map mode id -> model from ollama-config.ts, slicing between `id: "..."` markers.

    A fixed-width window is wrong here: comments sit between `id` and `model` and grow freely.
    """

    starts = [(match.group(1), match.start()) for match in TS_MODE_BLOCK.finditer(text)]
    models: dict[str, str] = {}
    for index, (mode_id, start) in enumerate(starts):
        end = starts[index + 1][1] if index + 1 < len(starts) else len(text)
        block = text[start:end]
        found = TS_MODEL.search(block)
        if found and mode_id not in models:
            models[mode_id] = found.group(1)
    return models


class ConfigParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.assertTrue(TS_CONFIG.is_file(), f"missing {TS_CONFIG}")
        self.ts = TS_CONFIG.read_text(encoding="utf-8")

    def test_shared_num_ctx_matches_typescript(self) -> None:
        match = TS_NUM_CTX.search(self.ts)
        self.assertIsNotNone(match, "SHARED_NUM_CTX not found in ollama-config.ts")
        self.assertEqual(_number(match.group(1)), SHARED_NUM_CTX)

    def test_every_mode_model_matches_typescript(self) -> None:
        """Every Python chat mode must name the same model the agent will load."""

        ts_models = _ts_mode_models(self.ts)
        self.assertEqual(
            set(ts_models),
            set(CHAT_MODES),
            f"mode ids differ: python={sorted(CHAT_MODES)} ts={sorted(ts_models)}",
        )
        for mode_id, mode in CHAT_MODES.items():
            self.assertEqual(
                ts_models[mode_id],
                mode["model"],
                f"{mode_id}: python {mode['model']!r} vs typescript {ts_models[mode_id]!r}",
            )

    def test_fast_model_matches_typescript(self) -> None:
        match = TS_MODEL.search(self.ts)
        self.assertIsNotNone(match, "no model found in ollama-config.ts")
        self.assertIn(CHAT_MODES["fast"]["model"], self.ts)

    def test_every_modelfile_bakes_the_shared_context(self) -> None:
        modelfiles = sorted(MODELFILE_DIR.glob("Modelfile.*"))
        self.assertTrue(modelfiles, f"no Modelfiles under {MODELFILE_DIR}")
        for path in modelfiles:
            text = path.read_text(encoding="utf-8")
            from_match = MODELFILE_FROM.search(text)
            self.assertIsNotNone(from_match, f"{path.name} has no FROM line")
            self.assertRegex(
                from_match.group(1),
                r"^[A-Za-z0-9._/-]+:[A-Za-z0-9._-]+$",
                f"{path.name} FROM must be a tagged id (no ':latest' surprises)",
            )
            ctx = MODELFILE_CTX.search(text)
            self.assertIsNotNone(ctx, f"{path.name} has no num_ctx parameter")
            self.assertEqual(
                int(ctx.group(1)),
                SHARED_NUM_CTX,
                f"{path.name} bakes num_ctx {ctx.group(1)} but SHARED_NUM_CTX is {SHARED_NUM_CTX}",
            )

    def test_alternate_fast_model_is_a_distinct_tag(self) -> None:
        """The A/B alternate must not be the same id as the baseline, or the A/B is a no-op."""

        b_models = {
            match.group(1)
            for path in MODELFILE_DIR.glob("Modelfile.*")
            if (match := MODELFILE_FROM.search(path.read_text(encoding="utf-8")))
        }
        self.assertNotIn(
            CHAT_MODES["fast"]["model"],
            b_models - {CHAT_MODES["fast"]["model"]},
            "duplicate Fast FROM tags",
        )
        self.assertGreaterEqual(len(b_models), 2, "expected a baseline and an A/B alternate")


if __name__ == "__main__":
    unittest.main()