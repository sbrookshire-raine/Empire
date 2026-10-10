# ZIM library — cloud upload runbook

**Source of truth (local):** `F:\AI_ARCHIVE\AI_Archive_Legion\knowledge_bases` (~**719 GiB**, 6,328 files, 49 `.zim` files plus indexes and sidecar folders).

**Cloud target:** `pool:ZIM_RESOURCES` on the 20 TiB rclone union (`Z:` when mounted).

**Related:** [`BACKUP_CONSOLIDATION.md`](BACKUP_CONSOLIDATION.md) (EMPIRE_HUB tier), [`ESTATE_INVENTORY.md`](ESTATE_INVENTORY.md) §12 (ZIM census), [`BACKUP_RUNBOOK.md`](BACKUP_RUNBOOK.md) (T0 sources).

## Strategy: folder copy, not tar bundles

| Approach | Verdict |
|----------|---------|
| **Tar per year / per folder** | **No** — `.zim` files are already compressed archives. Wrapping them in `.tar` adds CPU time, needs extra scratch disk (~719 GiB on E: or F:), and one bad tar blocks verification of many ZIMs. |
| **`rclone copy` tree mirror** | **Yes** — one cloud object per file; **resume-friendly** after crash or daily upload cap; **union pool** can place each large `.zim` on a different Google account (~750 GiB upload/day per account). |

Layout on cloud matches source paths under `pool:ZIM_RESOURCES/` (eleven small devdocs ZIMs were uploaded flat at pool root in an earlier pass; `copy` skips unchanged files and fills in `wikipedia/`, `books/`, `stackoverflow/`, etc.).

## Bandwidth (same as hub)

From [`config/zim-upload.json`](../config/zim-upload.json):

| Window (local) | Limit |
|----------------|--------|
| **12:00 AM – 2:00 PM** | `off` (full gigabit) |
| **2:00 PM – 12:00 AM** | `3M` |

Expect **multiple nights** for ~719 GiB even at full speed; a single 200 GiB `.zim` is limited by **one account’s** daily upload quota until the next window.

## Commands

```powershell
cd C:\EMPIRE
.\scripts\zim-rclone-sync.ps1 -Action status
.\scripts\zim-rclone-sync.ps1 -Action copy
.\scripts\zim-rclone-sync.ps1 -Action check
```

Logs: `E:\EMPIRE_HUB\99_INDEX\zim_pipeline.log`, `zim_rclone_upload.log`, `zim_rclone_check.log`.

**Monitor progress:** tail `zim_rclone_upload.log`, or `rclone size pool:ZIM_RESOURCES` (cloud total climbing toward ~719 GiB).

**After reboot:** remount `Z:` via `E:\cloud_archiver_hub.py` if you browse in Explorer; upload does **not** require `Z:` — rclone talks to `pool:` directly.

## Verification

1. `zim-rclone-sync.ps1 -Action check` — size-only, one-way (source → cloud).
2. Optional integrity on local set before/after: Kiwix `zimcheck` per file when `kiwix-tools` is installed (not required for upload itself).

## What this does not cover

- **16 ZIMs on the detached 25E1** (`E:\wikipedia` on old layout, ~461 GB) — separate pass when that drive is attached; do not assume union with the F: set without a census.
- **EMPIRE_HUB** Wikipedia tars (`02_RESOURCES`) — already on `pool:EMPIRE_HUB`; different format (markdown packs + dumps), not a substitute for ZIMs.

## Gates before deleting F: copies

1. `zim-rclone-sync.ps1 -Action check` exits **0**.
2. Architect confirms `rclone size pool:ZIM_RESOURCES` ≈ local source size.
3. Offline disc policy satisfied if you use the same rule as EMPIRE_HUB (`SPACE_RECOVERY.md`).

## Started

Initial upload logged in `zim_pipeline.log` when `copy` is first run (2026-10-08).
