# UPGRADE/ — provenance bundle for the capability arms

This folder is **not** a build area or a dependency. It is the original handoff bundle from the
governed-discovery / capability-arms work, kept for provenance and for the one file that is still a
live data source:

| File | Status |
|------|--------|
| `osint-catalog.json` | **Live input.** `config/eve-capabilities/seed_catalog.py` reads it (`DEFAULT_SOURCE`) to build `config/eve-capabilities/catalog.db` |
| `PRIMARY_TASK_UPGRADE.MD` | Historical handoff prompt (the arms work shipped) |
| `SECONDARY_TASK_UPGRADE.md` | Historical handoff prompt (the arms work shipped) |

Removed 2026-09-24 in the refactor evaluation (see [`docs/REFACTOR_EVAL.md`](../docs/REFACTOR_EVAL.md)),
because each had been superseded by a live copy elsewhere:

- five `*.zip` micro-skill archives → unpacked into `eve-skills/<skill>/` (5 skills × 18 files);
- `discovery-router.py`, `seed-catalog.py` → the grown, tested versions live in
  `config/eve-capabilities/` and are covered by `tests/pipeline/test_discovery_catalog.py` and
  `tests/pipeline/test_capability_seed.py`.

Git history holds all removed files if provenance is ever needed again.