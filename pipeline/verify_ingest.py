"""Phase 3 verification: mock ingest -> Cognee recall."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.cognee_client import recall
from pipeline.ingest_local import ingest_file


async def main() -> int:
    mock_file = ROOT / "mock_data_ingest" / "github_issue.json"
    print(f"Ingesting {mock_file}...")
    result = await ingest_file(mock_file)
    print("Ingest result:", json.dumps(result, indent=2))

    print("Recalling graph context...")
    hits = await recall("What is Issue 42 in empire/local-stack?", dataset="mock")
    print("Recall results:", json.dumps(hits, indent=2, default=str)[:2000])

    text = json.dumps(hits, default=str).lower()
    checks = {
        "mentions_issue_or_42": "42" in text or "issue" in text,
        "mentions_repo": "empire" in text or "repo" in text,
    }
    print("Checks:", checks)

    if not any(checks.values()):
        print("WARNING: recall returned weak matches; inspect results manually")
        return 1

    print("Phase 3 verification PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
