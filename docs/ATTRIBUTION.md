# Attribution — credits, not a licence gate

**Decision (2026-09-26, contradiction C5):** attribution exists for honesty and for the project's
showcase value. It is **not** a licence gate — a piece is never rejected for licence reasons. Pieces are
rejected only for **technical** non-conformance (`docs/LEGO_CONTRACT.md`).

This matters because EMPIRE is public on GitHub and was grown from many sources: Gemini, Composer 2,
Deepseek, other models and tools, plus vendored projects and third-party documentation.

## What to record for a piece

| Field | Meaning |
|---|---|
| `origin` | the model, tool, project or person it came from (`Gemini`, `Composer 2`, `Deepseek`, `vendored: <project>`, `architect`, `mixed`) |
| `role` | `generated` · `adapted` · `authored` · `vendored` |
| `date` | when it landed (commit date is fine) |
| `source` | a link or path when one exists |

Where it goes: a header comment on the file, or a row in the register below. Credits are **additive** —
never delete one to tidy a file.

## Register (started 2026-09-26)

| Surface | Origin | Role | Note |
|---|---|---|---|
| `docs/reference/` (47 files) | vendor documentation (Gumloop, Dify, AnythingLLM, Cursor, FlutterFlow, Ollama, Magic Patterns) | vendored | reference only; never ingested |
| `tools/archify/` (302 files) | vendored project with its own CI | vendored | has upstream workflows |
| `D:\wiki_md\2017` (5.35 M files) | Wikipedia text, converted by `pipeline/wiki_xml_convert.py` | adapted | the converter is the recipe; the corpus is its output |
| `config/lego-bricks.json`, `LEGO_INDEX.md` | architect-authored brick catalog | authored | seeds the LEGO contract |
| Model-assisted code throughout | **mixed** — see git history per file | generated/adapted | no per-file headers exist yet (`scripts/audit-empire.py` counts these; it reads **1** today) |

## Measured state

- Files carrying an SPDX / licence / copyright header: **1 of the whole codebase** (the count is reported
  by `scripts/audit-empire.py` as `files_with_licence_header`).
- No repo-level licence file is required by the C5 decision. If that changes, this page is where the
  decision gets recorded — not in a scattered set of file headers.

## What this means going forward

New pieces add an `origin` line. Existing pieces gain one opportunistically, when a file is already
being touched for another reason. That keeps the register honest without a mass-rewrite that would
churn the whole history for a field nobody reads until it's needed.
