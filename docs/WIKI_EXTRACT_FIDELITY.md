# Wikipedia extract source fidelity (Phase 0)

**Date:** 2026-09-15  
**Corpus:** `D:\wiki_md\2026` via Title DNS (`I:\EMPIRE_DATA\wiki-reports\2026\title-index.sqlite`)  
**Sample:** 20 resolved pages (places, products, shows, lists, bios)

## Findings

| Signal | Count / note |
|--------|----------------|
| YAML frontmatter | 20/20 |
| Markdown headings (`#` / `##`) | 20/20 |
| Markdown lists | 19/20 |
| MediaWiki `{|` tables | **12/20** — structure **retained** |
| `| key = value` lines | 14/20 — partial / stripped infobox residue common |
| Full `{{Infobox …}}` templates | **2/20** (e.g. Python, Nintendo Switch) |
| HTML `<table>` | 0/20 |
| Hash-style `# Title \| key =` lead noise | 0 in this sample (still handled in lead stripper) |

Examples:

- **The Following** — ratings wikitable present (`{| class="wikitable…`).
- **PlayStation 2 / Nintendo Switch** — tech wikitables present; Switch also has `{{Infobox information appliance}}`.
- **Running Up That Hill** — top-of-page pipe KV fields (`length`, `label`, `writer`) without full Infobox wrapper.
- **Cheddar cheese / WWII / Einstein** — prose + lists; little or no `{|` (extract may be `empty`/`unsupported` for table asks — fail closed).
- **Paris** — false-positive `|` lines inside prose; extractor must require `key = value` shape.

## Classification

| Class | Meaning for EMPIRE |
|-------|---------------------|
| **Literal-parseable** | `{|` tables, MD lists/headings, pipe KV, some Infobox templates — **majority of automation extracts** |
| **Expansion-needed** | Template/Lua-generated cells often blank or image-only after conversion |
| **Already-lossy** | Many pages lack full Infobox; scalars (population) may live only in prose — v1 extract does **not** invent from prose |

## Parser decision

- **No new pip dependency for v1.** Deterministic regex/AST-light parsers in `pipeline/wiki_extract.py` cover `{|`, pipe KV, `{{Infobox`, MD lists, MD pipe tables.
- Revisit **MIT `mwparserfromhell`** or **GPL `wikitextparser`** only if construct F1 stays &lt;0.80 on the gold set after two bounded fixes.
- Do **not** migrate Title DNS or links stores based on this sample.

## Gate for later phases

Proceed to Evidence JSON + fail-closed injection. DuckDB/ZIM remain gated per plan.
