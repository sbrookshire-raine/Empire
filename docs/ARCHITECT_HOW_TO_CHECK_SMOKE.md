# How to check smoke evidence (plain English)

You are **not** supposed to re-run developer commands. Mechanic already did. “Check evidence” = glance at a few result files and decide if you trust them.

## 30-second version

1. Open `data/eval/architect_soft_smoke_b.json` (already open in the editor).
2. Look for these green flags:
   - `"used_structured_extract": true` — Eve actually used the extract tool
   - `"has_fields": true` — it returned title/tags/summary
   - `"hits": 3, "cases": 3` — Phase 3 rerank OK
   - `"allow": true, "block": true, "fetch_ok": true` — Phase 4 browser allowlist OK
3. Optional: open `data/eval/architect_phase6_smoke.json` and confirm `"ok": true` and `"actuators": false` (vision looked, did not click).
4. Optional: open the picture `data/eval/vision_ui_smoke/eve_workbench.png` — that is the Eve screen vision looked at.

If those look fine, paste into this Cursor chat:

```
Accept mechanic soft-smoke Phases 1-6 and 8
```

That is your “I checked / I trust it” signature. Done.

## What each phase means (no jargon)

| Phase | What Mechanic proved | Where to look |
|------:|----------------------|---------------|
| 1 | GPU “one heavy job at a time” lock works | helper / scorecard |
| 2 | Eve extracted title/tags/summary via Structured Extract | soft_smoke_b.json `text_head` |
| 3 | Search rerank eval 3/3 | soft_smoke_b.json `phase3` |
| 4 | Local pages allowed; public sites blocked | soft_smoke_b.json `phase4` |
| 5 | Voice activity detector works on sample audio | VAD notes in guide |
| 6 | Vision describes Eve UI, does not click | phase6_smoke.json + eve_workbench.png |
| 7 | Skipped on purpose | parked |
| 8 | SBOM report file exists | `data/eval/sbom/` |

## If you prefer a live feel instead

Open http://127.0.0.1:8080/eve.html and chat normally. You do **not** have to re-run Soft Smoke B unless you want to. Trusting the JSON is enough.
