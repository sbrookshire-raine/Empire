# OneDrive and local database storage

EMPIRE keeps **mutable database files outside OneDrive** so cloud sync does not lock embedded databases (Cognee/Kuzu, LanceDB).

## Built-in (automatic)

| Data | Location |
|------|----------|
| Cognee graph + vectors | `V:\Cognee` (NTFS VHDX backed by `I:\EMPIRE_VHDX\empire_cognee.vhdx`) |
| Cognee access lock | `%LOCALAPPDATA%\EMPIRE\cognee.lock` |
| Wiki ingest checkpoint | `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` |

The heavy graph/vector DB lives on an NTFS VHDX (off the C: drive) — see
[COGNEE_VHDX.md](COGNEE_VHDX.md). Only lightweight control files remain on C:.

MCP (`empire-cognee`) and CLI ingest share a **cross-process file lock**, so you do not need to disable the MCP server before ingesting.

`scripts/setup.ps1` writes `config/cognee.env` with the LocalAppData path on every run.

## Optional: reduce OneDrive sync on the repo

If PocketBase or the venv feel slow, you can stop OneDrive from syncing heavy folders inside the project:

1. Open the EMPIRE folder in File Explorer.
2. Right-click `backend\pocketbase\pb_data` → **Free up space** or **Always keep on this device** only if you need offline copies.
3. For best performance, exclude `venv\` and `backend\pocketbase\pb_data\` from OneDrive backup:
   - OneDrive settings → Sync and backup → Manage backup → uncheck heavy folders, **or**
   - Move the whole EMPIRE repo out of `Desktop\OneDrive` to e.g. `C:\dev\EMPIRE`.

Cognee data is already outside OneDrive; this step only helps PocketBase and Python venv I/O.
