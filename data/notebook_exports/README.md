# Notebook exports — drop them here, she reads and cites them

**One breath:** export a notebook from whatever tool you use, save it into **this folder**, and ask Eve
about it. She reads the file on demand (`read_document`) and **names the file** in her answer, so you can
open it and check her. Nothing here talks to a cloud service: the export is a file, the reading is local,
the answering is local.

## The flow

1. **Export.** From NotebookLM (or any notes tool): *Download* the sources/notes, or *Export to Docs* and
   save as `.docx` / `.md`. Notes you paste into a plain `.md` work best.
2. **Save it**, one file per notebook, named so you recognise it later:
   `data/notebook_exports/<topic>-notes.md`. Subfolders are fine — see *Where the file must live* below.
3. **Ask.** "Using my notebook export on X, what does it say about Y?" — she calls `read_document` on the
   file and answers from its contents, citing `X-notes.md`.
4. **Check her.** Her answer should name the file. If it doesn't, she answered from general knowledge
   instead of your export — ask again and name the file explicitly.

## Where the file must live (measured 2026-09-25)

`read_document` accepts three roots (`pipeline/read_document.py`):

| Root | Note |
|---|---|
| `C:\Empire_Workbench` | your live workbench data — **relative paths resolve against this one** |
| `C:\EMPIRE\docs` | repo docs |
| `C:\EMPIRE\data` | this folder lives here, so it is readable — **reference it by full path** |

Measured, so you don't repeat the mistake: `read_document data\notebook_exports\foo.md` resolves to
`C:\Empire_Workbench\data\notebook_exports\foo.md` and fails; the same file reads fine as
`C:\EMPIRE\data\notebook_exports\foo.md` — `ok: true`, engine `direct`, provenance-stamped,
`truncated: false`. So if she misses on a bare filename, give her the full path. `EMPIRE_READ_DOC_ROOTS`
overrides the root list if you would rather anchor everything to the workbench.

## What she can read

| Format | Path | Notes |
|---|---|---|
| `.md` `.txt` `.csv` `.tsv` `.json` `.jsonl` | direct | cheapest — no conversion |
| `.html` `.htm` | direct | |
| `.pdf` `.docx` `.pptx` `.xlsx` | Docling / MarkItDown | CPU-side conversion, slower, no GPU |

Both `docs/` and `data/` are readable roots (`EMPIRE_READ_DOC_ROOTS` overrides the list); files are capped
by size, and when a file is longer than one read she is told it was truncated rather than left to imply
she saw all of it.

## Why a folder and not a memory ingest

Read-on-demand costs **no memory and no ingestion time**, and citation is *checkable*: a local file has a
stable name, so "she cited `yt-dlp-notes.md`" is something you can verify with one look — unlike a recalled
chunk. Ingest these into Cognee later only if you want her to *search across* many notebooks at once
rather than read the one you point at.

## Keep it tidy

This folder is source material, not scratch. Delete exports you are done with; `data/notebook_exports/`
is not ingested automatically by any script, so nothing here reaches memory unless you ask for it.
