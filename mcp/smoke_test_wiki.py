"""Smoke test for Wikipedia MCP tools (bounded pilot + recall)."""
import asyncio
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("wiki_mcp", Path("mcp/wiki_mcp.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


async def main() -> None:
    # Truth-Drift pilot: ingest two snapshot years into sibling datasets so they coexist.
    # NOTE: fast mode still runs one cognify pass (Cognee only builds searchable vectors during
    # cognify). With local llama3.1 that is ~40s/doc, so keep the smoke-test limit small; raise
    # it for a real batch run. The first 20 files of batch_00000 share all 20 titles across
    # 2021/2026, which is what proves cross-year coexistence.
    limit = 20
    print(f"--- wiki_ingest_batch (2026/batch_0, fast, limit {limit} -> wikipedia_2026) ---")
    ingest_2026 = await mod.wiki_ingest_batch(year="2026", batch="0", mode="fast", limit=limit)
    print(ingest_2026[:600])

    print(f"--- wiki_ingest_batch (2021/batch_0, fast, limit {limit} -> wikipedia_2021) ---")
    ingest_2021 = await mod.wiki_ingest_batch(year="2021", batch="0", mode="fast", limit=limit)
    print(ingest_2021[:600])

    print("--- wiki_ingest_status ---")
    status = await mod.wiki_ingest_status()
    print(status[:600])

    # Cross-year recall: empty dataset searches ALL snapshots to confirm coexistence.
    print("--- wiki_recall (cross-year, dataset='', shared title 'Cambrai') ---")
    recall_all = await mod.wiki_recall("Cambrai snapshot_year", dataset="")
    print(recall_all[:1000])


asyncio.run(main())
