# Architect smoke evidence (plain English)

Generated: 2026-09-08 03:41 UTC

Green = Mechanic soft-smoke already passed. You only need to accept.

| Phase | What | Result | Detail |
|------:|------|--------|--------|
| 1 | Foundation (GPU lease) | **PASS** | Lease acquire/deny already verified in scorecard |
| 2 | Structured Extract (Soft Smoke B) | **PASS** | The extracted metadata from the text is as follows:  - **Title:** Architect smoke - **Tags:** smoke, extract - **Summary:** verifying structured extract limb  This information is s |
| 3 | Retrieval rerank | **PASS** | 3/3 hits |
| 4 | Browser Local allowlist | **PASS** | allow local, block public, fetch localhost OK |
| 5 | Voice VAD | **PASS** | Energy VAD: silent=no speech, tone=speech (CLI) |
| 6 | Vision UI observe | **PASS** | Observed Eve UI regions; actuators=false |
| 7 | PaddleOCR | **PARKED** | PARKED on purpose |
| 8 | SBOM scripts | **PASS** | 1 report file(s) under data/eval/sbom |

## Extra checks
- Extract scratch file present: yes
- Eve screenshot for vision: yes (`data/eval/vision_ui_smoke/eve_workbench.png`)

## Your next step

If every non-parked row says PASS, paste this into the Cursor chat:

```
Accept mechanic soft-smoke Phases 1-6 and 8
```

Or open `docs/ARCHITECT_SMOKE_REPLY_CARD.md`.
