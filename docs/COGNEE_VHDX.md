# Cognee storage on an NTFS VHDX (off the C: drive)

EMPIRE's hard rule is **keep heavy storage off the C: Core Runtime drive**. Cognee's
databases (`lancedb` + `kuzu` + `sqlite`) need real NTFS semantics — they **cannot** run on
the 4TB `I:` drive because it is formatted **exFAT** (lancedb fails with `Incorrect function`,
os error 1; kuzu/sqlite are unreliable).

The fix: a **dynamically-expanding NTFS VHDX** whose backing file physically lives on `I:`,
but which presents a normal NTFS volume once mounted. Cognee is pointed at that volume.

| Property | Value |
|----------|-------|
| VHDX backing file | `I:\EMPIRE_VHDX\empire_cognee.vhdx` |
| Type | dynamically expanding (grows as data is written) |
| Max capacity | 2 TB (`maximum=2097152` MB in diskpart) |
| Filesystem / label | NTFS / `EMPIRE_COGNEE` |
| Mount point | drive **`V:`** |
| Cognee root | `V:\Cognee` |

> The concurrent Weaviate export writes to `I:\EMPIRE_DATA\weaviate_dump`. The VHDX lives in a
> **separate** folder (`I:\EMPIRE_VHDX`) and never touches that path.

## What stays on C: (by design)

Only the **heavy** graph/vector DB moves to the VHDX. Lightweight cross-process control files
stay on `C:` under `%LOCALAPPDATA%\EMPIRE`, matching the original design:

- `%LOCALAPPDATA%\EMPIRE\cognee.lock` — cross-process lock (MCP + CLI safe together)
- `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` — resumable ingest checkpoint

## One-time creation (requires Administrator)

Creating/attaching/formatting a VHDX with `diskpart` requires elevation. Run once, as admin:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\create-cognee-vhdx.ps1"
```

This runs the diskpart sequence (`create vdisk … maximum=2097152 type=expandable` → `attach` →
`create partition primary` → `format fs=ntfs quick label=EMPIRE_COGNEE` → `assign letter=V`)
and creates `V:\Cognee`.

## Mounting (requires Administrator)

`scripts\mount-cognee-vhdx.ps1` idempotently attaches the VHDX and ensures it is at `V:`. It is
safe to run repeatedly (no-op if already mounted).

On Hyper-V hosts, `Mount-DiskImage` returns Access Denied. The script prefers **`Mount-VHD`**
and falls back to `Mount-DiskImage`.

Preferred operator command (prompts UAC if needed):

```powershell
.\scripts\start-stack.ps1
```

Or mount only:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1"
```

It is also called near the **top of `scripts\start-stack.ps1`** and `scripts\roll-in.ps1`.

### Auto-mount at logon

Because mounting needs elevation, register a Task Scheduler job with highest privileges
(run once, as admin):

```powershell
schtasks /Create /TN "EMPIRE Mount Cognee VHDX" /RL HIGHEST /SC ONLOGON /F /TR 'powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1"'
```

Remove the task later with:

```powershell
schtasks /Delete /TN "EMPIRE Mount Cognee VHDX" /F
```

## Detaching

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\EMPIRE\scripts\mount-cognee-vhdx.ps1" -Detach
# or:  Dismount-DiskImage -ImagePath "I:\EMPIRE_VHDX\empire_cognee.vhdx"
```

## Where the config points

`EMPIRE_COGNEE_ROOT` (when set) always wins; otherwise these all default to `V:\Cognee`:

- `config\cognee.env` → `SYSTEM_ROOT_DIRECTORY=V:\Cognee`
- `pipeline\cognee_client.py` → `DEFAULT_COGNEE_ROOT = r"V:\Cognee"`
- `scripts\setup.ps1` → `$cogneeSystemDir` default `V:\Cognee`
- `.cursor\mcp.json` (`empire-wiki`) → `EMPIRE_COGNEE_ROOT=V:/Cognee`

## If `V:` is already taken

Pick any free letter, then use it consistently: re-run `create-cognee-vhdx.ps1` with the new
letter (edit `$DriveLetter`), update the four config locations above, and update the mount
script's `$DriveLetter`.
