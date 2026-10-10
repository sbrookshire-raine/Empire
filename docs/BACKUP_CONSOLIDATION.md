# Backup consolidation (current phase)

**Consolidation upload completed 2026-10-08.** This is still **not** incremental nightly backup — the next phase is occasional **delta** sync (repo tar, vault, notes) from `E:` → `pool:EMPIRE_HUB`.

## Four tiers (how the pieces fit)

| Tier | Role | What lives here |
|------|------|-----------------|
| **C: / D:** | **Primary EMPIRE workspace** — live repo (`C:\EMPIRE`), vault (`C:\Empire_Workbench`), runtime wiki corpus (`D:\wiki_md`), optional live Weaviate tree on D: | Working copies; not a backup by themselves |
| **E:** | **Staging + local SSD backup** — one organized tree `E:\EMPIRE_HUB` (tars + layout per `99_INDEX/INDEX.md`); compiled from scattered drives | **~797 GiB** on disk; **`CHAIN DONE`** staging; secrets only in `00_CORE/local_only/` (never cloud) |
| **Z:** (`pool:`) | **20 TiB cloud** — rclone union of four Google accounts; mount with `rclone mount pool: Z:` or Tab 1 in `E:\cloud_archiver_hub.py` | **`pool:EMPIRE_HUB` ~764 GiB** (matches E: payload after intentional excludes); other pool folders (early tar loads, Toontrack, etc.) are separate |
| **Offline disc** | Second local copy of `E:\EMPIRE_HUB` including `local_only` | **Not done yet** — required before aggressive C:/D: deletes per `SPACE_RECOVERY.md` |

**Irreplaceable hub content (Weaviate tars, Wikipedia dumps/runs/packed md, notes, project parts, core repo/vault tars):** staged on **E:** and copied to **`pool:EMPIRE_HUB`** on **Z:** as of 2026-10-08.

**Not in EMPIRE_HUB (separate decisions):**

- **~719 GiB ZIM library** — `F:\AI_ARCHIVE\AI_Archive_Legion\knowledge_bases` (49 ZIMs). Upload: [`docs/ZIM_CLOUD_UPLOAD.md`](ZIM_CLOUD_UPLOAD.md), [`scripts/zim-rclone-sync.ps1`](../scripts/zim-rclone-sync.ps1), [`config/zim-upload.json`](../config/zim-upload.json).
- **Live Cognee graph** — hub holds 2026-09-27 VHDX snapshot only (`V:` was not mounted at staging).
- **Ollama / large model stores** — re-downloadable; intentionally not in hub.

## Verification (2026-10-08)

- Staging: `E:\EMPIRE_HUB\99_INDEX\stage_chain.log` → **`CHAIN DONE`**; key tars present (4× Weaviate, 3× `wiki_md_*.tar`).
- Upload: `pipeline.log` / `pipeline_weaviate.log` — all Weaviate and A1/A2 phases **exit 0**; final copy **exit 0**.
- Cloud match: `rclone check` E: → `pool:EMPIRE_HUB` with [`config/hub-upload.json`](../config/hub-upload.json) excludes → **0 differences** on archive payload (run `.\scripts\hub-rclone-sync.ps1 -Action check` to re-verify).
- Size gap **~797 GiB local vs ~764 GiB cloud** = excluded `local_only`, `_superseded*`, incomplete `*.part` dumps, and operational logs under `99_INDEX` (logs stay on E: only).

## Order of operations (original consolidation)

1. **Consolidate on `E:\EMPIRE_HUB`** — tars and layout per `E:\EMPIRE_HUB\99_INDEX\INDEX.md`.
2. **Verify** — read-through tars (`verify_new.py`, logs in `99_INDEX/`).
3. **Cloud** — `pool:EMPIRE_HUB` on the 20 TiB rclone union (`Z:`). Use [`scripts/hub-rclone-sync.ps1`](../scripts/hub-rclone-sync.ps1) + [`config/hub-upload.json`](../config/hub-upload.json).
4. **Local SSD backup** — second copy (offline disc) from `E:\EMPIRE_HUB` after you are satisfied with cloud check.
5. **GitHub** — application code on branch `revision-refactor`; merge to `main` when consolidation is stable so clones match the hub `repo_mirror` tar.
6. **Space recovery on C:/D:** — only after (3) and (4); list and proof in `E:\EMPIRE_HUB\99_INDEX\SPACE_RECOVERY.md`.

## Upload bandwidth (gigabit, upstairs)

Configured in `config/hub-upload.json`:

| Window (local) | Default limit | Purpose |
|----------------|---------------|---------|
| **12:00 AM – 2:00 PM** | `off` (no rclone cap) | Max upload during sleep / low personal use |
| **2:00 PM – 12:00 AM** | `3M` | Leave headroom for work, Eve, streaming |

Tune `night_bwlimit` down (e.g. `80M`) if the link is shared or Wi‑Fi is weak upstairs.

Google Drive: **~750 GiB uploaded / account / rolling 24 h** (throughput cap, not storage cap). Your **`pool:` union** spreads **stored** data across four remotes (`gdrive_*`); each **new file** is written to **one** upstream (rclone union **create** policy — default picks among remotes with space, typically most-free-first). So:

- **Many files / many tars** in one `rclone copy` can land on **different** accounts → effective upload budget is closer to **up to ~4 × 750 GiB/day** if load is balanced, not a single 750 GiB wall for the whole pool.
- **One enormous single file** still uploads to **one** account for that transfer → that account’s 750 GiB/day still applies to that file.

The script keeps **`--drive-stop-on-upload-limit`** so one hot account stops cleanly instead of error-spamming; it is a per-remote guardrail, not proof you will hit it on every run.

## Commands

```powershell
cd C:\EMPIRE
.\scripts\hub-rclone-sync.ps1 -Action status
.\scripts\hub-rclone-sync.ps1 -Action copy
.\scripts\hub-rclone-sync.ps1 -Action check
```

Full pipeline (wait for staging, verify, copy, check): `E:\EMPIRE_HUB\99_INDEX\finish_and_upload.ps1`

Operator UI (mount Z:, ad‑hoc tars): `E:\cloud_archiver_hub.py`

**Remount Z: after reboot/crash:** Tab 1 **Start Z: Mount** in the archiver, or the same `rclone mount pool: Z:` flags documented in that script.

## Future: incremental EMPIRE updates (not wired yet)

When you change code or vault on C:/D:

1. Refresh affected tars on E: (or run targeted `build_*.py` / manual tar).
2. `.\scripts\hub-rclone-sync.ps1 -Action copy` (rclone copy is resume-friendly).
3. `.\scripts\hub-rclone-sync.ps1 -Action check`.

Do not delete duplicate data on C:/D until offline disc + any separate tiers (ZIMs) are handled.

## Related docs

- [`ESTATE_INVENTORY.md`](ESTATE_INVENTORY.md) §12 — pool + hub
- [`ODYSSEY.md`](ODYSSEY.md) §14 — narrative
- [`BACKUP_RUNBOOK.md`](BACKUP_RUNBOOK.md) — tier copy procedures
- `E:\EMPIRE_HUB\99_INDEX\INDEX.md`, `SPACE_RECOVERY.md`, `RESTORE.md`
