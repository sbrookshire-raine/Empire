# Vault manifest — 2026-09-26

Proof-of-completeness for the vault, taken before any file reorganisation. If files are ever moved,
this is the artifact that proves the move was lossless rather than hoping so.

| Reading | Value |
|---|---|
| Root | `C:\Empire_Workbench` |
| Files hashed | **14,652** |
| Total bytes | **2,814,752,484** (2,814.8 MB) |
| Errors | **0** |
| Manifest | `C:\Empire_Workbench\_manifests\vault-manifest-2026-09-26.json` |
| Manifest SHA-256 (generation 2, after the re-run) | `f9522ff893dfe7e381a0e07dea0c74c108a173d887f64ffa49fef693e3dd872d` |
| Generator | `scripts/vault-manifest.py` (stdlib only) |

Unrelated to the code repo: **the vault is not version-controlled** (no `.git`), which is why this
manifest exists. The repo has git and needs no equivalent.

## How to use it

```powershell
# re-hash the vault and write a new manifest
.\venv\Scripts\python.exe scripts\vault-manifest.py
```

A **move** shows up as one path disappearing and another appearing **with the same `sha256`** — that is
the proof. A **loss** shows as a path with no twin anywhere. Compare before/after manifests by hash, not
by eye; there are 14,652 entries.

**The manifest's own hash changes on every run**, because it stamps `created`. It identifies one
*generation*, not a fixed artifact. The durable proof is the **per-file `sha256` list** — compare entry
sets before and after a move; never compare whole-manifest bytes.

## What it does not cover

- The 900 MB of audio and the 220 MB/114 MB flattened codebases are hashed like everything else, but
  they are not *content-inspected* here — this is a completeness instrument, not an audit of meaning.
- `_manifests/` itself is excluded (self-reference).
