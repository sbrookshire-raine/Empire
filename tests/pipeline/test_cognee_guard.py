from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import cognee_guard


class CogneeGuardTests(unittest.TestCase):
    def test_memory_promote_chars_cap(self) -> None:
        with patch.dict("os.environ", {"EMPIRE_INTAKE_MEMORY_MAX_CHARS": "100"}):
            ok, reason = cognee_guard.memory_promote_allowed(chars=500)
        self.assertFalse(ok)
        self.assertIn("capped", reason)


if __name__ == "__main__":
    unittest.main()
