---
name: officecli-document-automation
description: Drives OfficeCLI, a single-binary, dependency-free CLI that lets an agent create, inspect, and edit Word/Excel/PowerPoint documents (create, add, set, get, view, query, merge, dump, batch, validate) without installing Microsoft Office. Use whenever a user asks to generate, edit, template-merge, convert, or extract structured data from a .docx/.xlsx/.pptx file. Infra-agnostic document-automation CLI with no dependency on Ollama/PocketBase/Cognee/FastMCP/HTMX-Alpine.
icon: file-text
color: Teal
---

# OfficeCLI Document Automation

OfficeCLI ships as a self-contained binary (.NET runtime embedded) — no dependencies
to install, and no Microsoft Office installation required.

## Core commands

- `create` — create a new Word/Excel/PowerPoint document.
- `add` — append content (paragraph, row, slide, etc.) to an existing document.
- `set` — set a specific field/cell/property value.
- `get` / `view` — read a specific field/cell/property or render a quick view.
- `query` — run a structured query against the document's data (e.g. table rows).
- `merge` — template-merge data into a document template.
- `dump` — export the document's structured content (e.g. to JSON) for downstream use.
- `batch` — run a sequence of the above operations from a script/manifest.
- `validate` — check a document for structural/schema issues before shipping it.

## How to use this skill

1. Confirm the target file type (.docx/.xlsx/.pptx) and the exact operation the user
   wants (generate new, edit existing, template-merge, extract data, or convert).
2. Invoke the OfficeCLI binary with the matching subcommand above, pointing at the
   user's file.
3. For template-merge requests, first inspect the template's merge fields (`dump` or
   `query`) before merging so field names are known to be correct.
4. Return the resulting file (or extracted data) to the user; run `validate` before
   handing back a generated/edited document when structural correctness matters.

## Build1 Integration

None — this is a pure document-automation CLI with no cloud dependency and no overlap
with Ollama/PocketBase/Cognee/FastMCP/HTMX-Alpine. It can be invoked as a plain shell
tool regardless of which stack the surrounding agent runs on.
