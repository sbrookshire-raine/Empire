# BACKUP RUNBOOK — how to make another copy, and how much space it needs

Written 2026-09-28 from the first full pass (579.8 GB copied to the WD 2627, mounted as `E:`). Companions:
[ESTATE_INVENTORY.md](ESTATE_INVENTORY.md) says *what exists and what it is*; this says *what to copy, with what tool,
in what order, and how much room it takes*. Sizes are measured where marked, projected where not.

## 1. Headline numbers

| Question | Answer |
|---|---|
| **Space for everything worth keeping** | **≈ 1.76 TB** |
| Space for the irreplaceable set only *(no Weaviate mirror, no re-downloadable sources)* | **≈ 640 GB** |
| Space used by the first pass so far | 579.8 GB |
| Largest single tier | **T3 personal — 423 GB** |
| Fits on one 3.7 TB drive? | Yes; a full backup leaves ~1.9 TB free |
| Filesystem for the destination | **NTFS**. exFAT works but has no journal and is what the fault drive uses |
| A **second** additional copy needs | the same 640 GB (essential) or 1.76 TB (everything) again |

**Space is not the constraint. Time and small-file handling are.** A tier of 4 GB in *ten* files takes a minute; the
same 4 GB in *800,000* files takes hours — that single fact drives every method choice below.

## 2. What gets copied, and what deliberately does not

| Tier | Source | Size | Method | Excluded on purpose |
|---|---|---|---|---|
| **T7 notes** | OneNote dump, `OneDrive\Documents\RESYNC_2026`, `OneDrive\Desktop\SBX_Vault`, `H:\Heptabase backup 4_7_26\…` | 0.93 GB | `robocopy /E` | — |
| **T4 system** | `C:\Empire_Workbench`, `%LOCALAPPDATA%\EMPIRE` | 13.6 GB | `robocopy /E` | *(optional)* `models` 8.6 GB + `bin` 2.3 GB inside `%LOCALAPPDATA%\EMPIRE` are re-downloadable → the unique part is only ~30 MB |
| **T3 personal** | `I:\HDD_MOVE_TEMP` | **423 GB** | `robocopy /E` | — |
| **T6 legacy** | `H:\AI_ARCHIVE\v2_markdown_pipeline`, `H:\AI_ARCHIVE\AI_Archive_Legion`, `_old_docs`, `_old_scripts`, `H:\Inception_of_Dreams`, `D:\AI_Factory`, all `OneDrive\Desktop` folders | ~53 GB | `robocopy /E /XD …` | **`data` 54.9 GB derived corpus** (5.45M files), `.git` 3.8 GB, `.venv`, `__pycache__`, `neo4j`, `volumes`; **Legion's** `models`/`datasets`/`docker_images`/`python_packages`/`binaries`/`runtimes`/`embeddings_models` (1.05 TB, all re-downloadable); **AI_Factory's** `.venv` + `models` (29.8 GB) |
| **T4b Docker volumes** | 13 Docker volumes (Cognee `pgdata`, open-webui ×3, postgres ×3, n8n ×3, dify ×2, `cursor_hol`) | 12.4 GB | container `tar` → `C:` staging → `robocopy` | `empire-speaches-hf` (500 MB model cache) + the 0-byte anonymous volumes |
| **T9 I: leftovers** | `I:\EMPIRE_DATA`, `I:\EMPIRE_VHDX`, `I:\EMPIRE_BACKUP`, `I:\User_Files` | 53.5 GB | `robocopy` for big files, **`tar` for the tiny-file trees** | — |
| **T1 markdown** | `D:\wiki_md` (2017 / 2021 / 2026) | 81 GB → **~85 GB packed** | **`tar -cf` (uncompressed), one archive per year** | *(nothing — it is the corpus)* |
| **T2 Weaviate** *(optional)* | `D:\weaviate_v2_archive` | **563 GB** | `robocopy /E` after a **clean Weaviate shutdown** | — |
| **T0 sources** *(optional)* | `E:\wikipedia` (16 ZIMs), `E:\enwiki-20241001…xml` | **558 GB** | `robocopy /E` | — |

**Never copied (tier T5, regenerable):** the 2.4 TB model library on `H:`, `SteamLibrary`, `EZDrummer`/`Superior`
sample libraries (450 + 31 GB, re-installable with the Toontrack licence), `%LOCALAPPDATA%\EMPIRE\models`, and the
ZIM library *if* you accept re-downloading 461 GB.

## 3. Ground rules (each of these was learned by breaking it)

1. **Identify the destination by serial, never by letter.** `Get-Disk | Select Number,FriendlyName,SerialNumber,Size`.
   Attach a *new* drive **before** ejecting the old one where possible: ejecting frees the letter, and the next drive
   takes it — that already happened once, the 2627 inheriting `E:` from the 25E1.
2. **One writer per USB disk.** Two jobs on one SMR portable thrash. Chain jobs with a wait-for-marker script rather
   than starting them together.
3. **Long jobs run as Windows scheduled tasks**, not as children of a shell — a child dies when that shell's job closes.
   `schtasks /create /tn NAME /tr "C:\EMPIRE\eve-audit\job.cmd" /sc once /st 00:00 /f` then `schtasks /run /tn NAME`.
   *Exception:* **Docker jobs must run from an interactive shell** — `docker run` inside a scheduled task fails
   silently (task goes `Ready`, no container, no error).
4. **Verify independently of the copy.** `robocopy`'s own counts are not proof; `scripts/compare-trees.py` is
   (relative path + size; 0 = match, 1 = difference, 2 = bad path). Use `--exclude` for anything copied with
   `robocopy /XD`, or the excluded directories report as "only in source" and mask real differences.
5. **Nothing is deleted.** Copy-first: originals stay. Space recovery is optional, and last.
6. **Measure before committing to a tier.** `robocopy <src> <dst> /E /L` prints the exact files/bytes that *would*
   copy while writing nothing. That is how T6 turned out to be 53 GB rather than the 1.2 TB it looked like.

## 4. Per-tier procedures

Copy into a dated root: `E:\EMPIRE_BACKUP_<YYYY-MM-DD>\<NN>_<tier>\`. Keep the `<NN>` ordering stable so a later pass
lands beside the earlier one and `compare-trees.py` can diff the two roots directly.

### 4.1 Plain trees — T7, T4, T3, T2, T0

```powershell
robocopy "<src>" "<dst>" /E /COPY:DAT /R:2 /W:5 /NFL /NDL /NP /LOG:"<logdir>\robocopy_<name>.log"
# exit < 8 is success (1 = files copied). Verify afterwards:
.\venv\Scripts\python.exe scripts\compare-trees.py "<src>" "<dst>" --labels "src,dst" --summary-only
```

### 4.2 T6's filtered items

```powershell
# v2_markdown_pipeline -- code and docs only; data/ is 54.9 GB of derived corpus
robocopy "H:\AI_ARCHIVE\v2_markdown_pipeline" "<dst>\v2_markdown_pipeline" /E /COPY:DAT /R:2 /W:5 /XD data .git .venv __pycache__ .pytest_cache volumes neo4j docker backups temp_forge raw_cc_data .vscode ssrf_proxy /NFL /NDL /NP

# AI_Archive_Legion -- docs/prompts/scripts only; the rest is 1.05 TB of re-downloadables
robocopy "H:\AI_ARCHIVE\AI_Archive_Legion" "<dst>\AI_Archive_Legion" /E /COPY:DAT /R:2 /W:5 /XD models datasets docker_images python_packages node_packages binaries runtimes embeddings_models drivers .checkpoints .github .vscode knowledge_bases github_repos 500-AI-Agents-Projects search_engines rag_tools /NFL /NDL /NP

# AI_Factory -- everything except its 29.8 GB of .venv + models
robocopy "D:\AI_Factory" "<dst>\AI_Factory" /E /COPY:DAT /R:2 /W:5 /XD .venv models /NFL /NDL /NP

# every Desktop project in one pass (SBX_Vault already lives in T7)
robocopy "C:\Users\<user>\OneDrive\Desktop" "<dst>\Desktop_all" /E /COPY:DAT /R:2 /W:5 /XD SBX_Vault /NFL /NDL /NP
```

Verify each with the **same exclusion list**: `compare-trees.py "<src>" "<dst>" --exclude "<list>" --summary-only`.

### 4.3 Docker volumes — tar out, then copy

```powershell
# Docker cannot bind-mount a USB drive, and a Windows path with a drive-letter colon breaks -v parsing.
# So: tar inside a container to a C: staging dir, then robocopy the tars to the backup drive.
$stage = "C:\EMPIRE\eve-audit\volumes_staging"; $stagef = $stage.Replace('\','/')
docker run --rm --entrypoint sh -e VOL=<volume> -v <volume>:/src:ro -v "${stagef}:/dst" pgvector/pgvector:pg16 -c 'cd /src && find . -type f | wc -l > /dst/$VOL.files && tar -cf /dst/$VOL.tar . && echo TAR_OK'
robocopy $stage "<dst>\08_volumes" /E /COPY:DAT /R:2 /W:5 /NFL /NDL /NP
```

`pgvector/pgvector:pg16` is used purely as a utility image (GNU tar 1.34 + findutils). Always pass `--entrypoint sh`,
otherwise the image's own `ENTRYPOINT` runs — pgvector starts Postgres and hangs. The `.files` count written beside
each tar is the cheap integrity check: compare it with `tar -tf <tar> | wc -l`.

### 4.4 Tiny-file trees — `tar`, never `robocopy`

Any tree with hundreds of thousands of small files (`weaviate_dump` 290k, `User_Files` 781k, and the corpus itself):

```powershell
C:\Windows\System32\tar.exe -cf "<dst>\<name>.tar" -C "<parent>" "<dirname>"
# If tar.exe dies with exit -1073741819 (0xC0000005 = access violation), use Python tarfile instead -- it did not
# crash on the restic repo where bsdtar crashed twice:
#   python -c "import tarfile;t=tarfile.open(r'<dst>\<name>.tar','w');t.add(r'<src>',arcname='<name>');t.close()"
```

### 4.5 T1 markdown — one uncompressed archive per year

```powershell
foreach ($y in '2017','2021','2026') { C:\Windows\System32\tar.exe -cf "<dst>\wiki_md_$y.tar" -C "D:\wiki_md" $y }
```

**Uncompressed on purpose:** gzip on millions of tiny files measured **~130 files/s** (~40 h for the corpus);
uncompressed measured **1,729 files/s** to an SSD. To a USB HDD expect **~9–10 h** for all three years — the 2017
archive alone took **5 h 40 m** to the 2627.

## 5. Space math

Measured sizes, in GB. "Essential" = irreplaceable or single-copy; "Optional" = already duplicated or re-acquirable.

| Tier | What it is | Size | Class |
|---|---|---|---|
| T7 | three documentation eras | 0.93 | **essential** |
| T4 | Workbench + `%LOCALAPPDATA%\EMPIRE` | 13.6 *(2.7 without re-downloadable models/bin)* | **essential** (~2.7) |
| T3 | personal archive, files back to 2013 | **423.3** | **essential** |
| T6 | curated legacy (code/docs/projects) | ~53 | **essential** |
| T4b | 13 Docker volumes (Cognee `pgdata`, chat history, DBs) | 12.4 | **essential** |
| T9 | I: leftovers (`EMPIRE_DATA` incl. 2017 dump, VHDX, restic) | 53.5 | **essential** |
| T1 | `wiki_md` packed, uncompressed | **~85** *(24.8 done: 2017)* | **essential** (partly re-derivable) |
| | **Subtotal — irreplaceable set** | **≈ 640 GB** | |
| T2 | Weaviate archive, 3 snapshots | 563.3 | optional — already on `D:` **and** `I:` |
| T0 | ZIMs **two sets**: 49 on `H:` 595.4 + 16 on the 25E1 461.4; plus enwiki XML (97.1 Oct-2024, 26.2 2026, 19.6 2021) | **~1,200** | optional — re-downloadable |
| | **TOTAL, everything worth keeping** | **≈ 2.4 TB** | |
| T5 | models 2.4 TB, Steam, `EZDrummer`/`Superior` 481, Speaches cache | ~2.9 TB | **never copied** — regenerable |

**Files ≥ 10 GB (measured 2026-09-28, `eve-audit/find-large-files.py` + `large-targeted.py`):** **50** among 2.19M
files stat-ed, plus one on the detached 25E1 = **51 known**; 151 ≥ 4 GB, 245 ≥ 2 GB. The largest: ZIMs (249.5, 109.9,
80.5, 76.8 GB), `docker_data.vhdx` 108.7 GB, Weaviate LSM segments (53.0 → 22.6 GB, ~10 of them),
`title-index.sqlite` **32.7 GB**, **our own `wiki_md_2017.tar` 24.8 GB**, the wiki dumps (97.1 / 26.2 / 19.6 / 12.8 GB),
GGUF models (47.4, 42.5, 23–26 GB each — T5, not copied), Steam paks (31.6, 26.3 GB).

**If a destination caps a single file** — 10 GB is a common cloud limit, 4 GB is FAT32 — then **the wiki dumps, the
big ZIMs, ~10 Weaviate segments, the title index and our own T1 archive all exceed it.** Remedies: build T1 as
**per-batch archives** instead of per-year (a 50,000-file batch is ~1–2 GB), pipe a tar through `split -b 5G`, or use
7z volumes. Plan for this *before* choosing a destination, not after. NTFS and exFAT have no practical per-file cap.


**What that means for capacity:**

| Destination | Verdict |
|---|---|
| **One 3.7 TB drive** (the 2627) | Everything fits with **~1.9 TB spare**. A full pass writes ~1.76 TB |
| **One 1 TB drive** | Fits the irreplaceable set (640 GB) with ~360 GB spare — **this is the tier to protect first** |
| **A second full copy** | Needs the same 640 GB (essential) or 1.76 TB (everything) again |
| Free space check | `[math]::Round((Get-Volume -DriveLetter E).SizeRemaining/1GB,1)` before starting |

**Time, not space, is the real budget:** ~1 h for T3's 423 GB; ~6 h for T1's 81 GB; ~1 h each for T2 and T0. The
tiny-file tiers are the slow ones, never the big ones.

## 6. Verification

Per tree, immediately after copying it:

```powershell
# plain copy
.\venv\Scripts\python.exe scripts\compare-trees.py "<src>" "<dst>" --labels "src,dst" --summary-only
# filtered copy (same list as robocopy /XD)
.\venv\Scripts\python.exe scripts\compare-trees.py "<src>" "<dst>" --exclude "<list>" --summary-only
```

Exit **0** = every path present on both sides with identical sizes. **1** = there is a difference: read the output
(it names each differing path) before assuming loss. **2** = bad path.

For tars, compare entry counts rather than sizes:

```powershell
# count what is inside the archive vs what the source held
(tar -tf "<archive>" | Measure-Object -Line).Lines
# per-volume tars also carry a .files count written at creation time
```

Two cautions learned the hard way: `robocopy`'s summary counts are **not** verification, and a database archive can
never match byte-for-byte while it is open (see §7).

## 7. Failure modes and cures

| Symptom | Cause | Cure |
|---|---|---|
| `docker run` produces nothing, task goes `Ready` | Docker needs an interactive session | run Docker jobs from an interactive shell |
| `invalid reference format`, or `Wrote only 6144 of 10240 bytes` | USB drives are not bind-mountable into the WSL2 VM; drive-letter colons break `-v` | stage on `C:`, then robocopy |
| `robocopy` burns hours of CPU for almost no progress | huge tiny-file trees (~2–3 files/s) | use `tar` (measured ~1,700 files/s) |
| `tar.exe` exits `-1073741819` (0xC0000005) | bsdtar access violation, seen on the restic repo and `User_Files` | use Python `tarfile` |
| A long job stops mid-way with no error | it was a child of a shell that exited | run it as a scheduled task |
| A **live database** copy differs in `*.wal` / `hnsw.commitlog` | write-ahead logs rotate while open | take the copy after a **clean shutdown**, and compare *durable index files*, not file counts |
| A file reports 0 bytes while clearly being written | stale `Get-ChildItem`/`Get-Item` size | use `[System.IO.FileInfo]::new(path).Length`, and take two samples 30 s apart |
| Every timestamp in a `.cmd` `for` log is identical | `%TIME%` is expanded once at parse time | use `!TIME!` with `setlocal enabledelayedexpansion` |

## 8. Making an additional (second) copy

The procedure is the same; what changes is **order** and **destination**. Given 3-2-1 (three copies, two media, one
offsite), a second copy should protect the single-copy tiers first:

1. **T3 personal (423 GB)** — single copy, on the drive with 912 unsafe shutdowns
2. **T1 markdown (85 GB packed)** — single copy, and 2017 is not trivially re-acquirable
3. **T9 leftovers (53.5 GB)** and **T4b volumes (12.4 GB)** — small, unique, single-copy
4. **T6 (53 GB)** and **T7/T4 (14.5 GB)** — unique but small
5. T2 and T0 last (already duplicated or re-downloadable)

Practical notes for a second copy:

- Run it to a **different device than the first copy** — a second folder on the same disk is not a backup.
- Reuse the same dated-root convention (`EMPIRE_BACKUP_<date>`), then diff the two roots with `compare-trees.py`
  to prove the new copy matches the old one, not just the source.
- Expect the same **one writer per disk** rule, and the same tiny-file behaviour: T1 is ~6 h, T3 ~1 h.
- If the destination is **exFAT** (like the 25E1), note it has **no journal**: an unclean unplug can cost directory
  entries. Prefer NTFS for the copy you will verify, and always eject cleanly.
- For an offsite/cloud layer, upload only the small irreplaceable set (~4 GB: T7, Workbench, the JSON/manifests)
  with **client-side encryption** — see §4 of ESTATE_INVENTORY for the reasoning.
