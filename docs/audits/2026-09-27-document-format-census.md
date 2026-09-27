# Document format census (P11)

Measured 2026-09-27 by `scripts/document-format-census.py`.
Roots scanned: `C:\Empire_Workbench`, `C:\EMPIRE\data`, `C:\EMPIRE\mock_data_ingest`.
**14,728 files, 2,817.8 MB** across 34 extensions.

## There is no single supported-format set: there are four

| Door | Accepts | Decided at |
|------|---------|------------|
| Workbench upload -> memory | .docx .eml .md .mdx .pdf .pptx .txt .xlsx | `pipeline/ingest_files.py:21` |
| Cognee mock ingest (MCP) | .json .md | `pipeline/normalizer.py:28-40` (raises otherwise) |
| read_document (Eve reads) | .csv .docx .eml .htm .html .json .jsonl .md .mdx .pdf .pptx .tsv .txt .xlsx | `pipeline/read_document.py:34-39` |
| query_data | .csv .tsv | `pipeline/query_data.py:113` |

A format's fate therefore depends on the *door*, not the extension: `.txt` is storable but not
cognee-ingestable, `.json` is the reverse, and `.docx` can be read but not remembered.

## Measured distribution

| ext | files | MB | bucket | why |
|-----|------:|---:|--------|-----|
| `.md` | 13,461 | 1,094.4 | storable | workbench upload -> memory |
| `.mp3` | 89 | 944.4 | audio | needs transcription (P8) |
| `.txt` | 276 | 594.9 | storable | workbench upload -> memory |
| `.mp4` | 1 | 74.8 | video | needs transcription (P8 family); large, decide by value |
| `.wav` | 3 | 32.1 | audio | needs transcription (P8) |
| `.synth` | 5 | 19.8 | unknown | no door claims this extension |
| `.zip` | 59 | 18.6 | archive | container; nothing unpacks it |
| `.pce` | 33 | 14.8 | non-document | emulator ROM / MIDI - identified from magic bytes, not knowledge |
| `.csv` | 81 | 6.8 | data | query_data / read-only; not storable |
| `.sfc` | 3 | 5.2 | non-document | emulator ROM / MIDI - identified from magic bytes, not knowledge |
| `.py` | 382 | 3.7 | code | source code; belongs to structural reach (P9), not document ingest |
| `.json` | 52 | 3.4 | cognee-only | MCP cognee ingest only; NOT uploadable to memory |
| `.png` | 14 | 1.2 | image | needs OCR (P11 gate) |
| `.nes` | 3 | 1.0 | non-document | emulator ROM / MIDI - identified from magic bytes, not knowledge |
| `.docx` | 3 | 0.7 | storable | workbench upload -> memory |
| `.html` | 4 | 0.7 | read-only | Eve can read it; not storable |
| `.eml` | 3 | 0.4 | storable | workbench upload -> memory |
| `.gb` | 1 | 0.3 | non-document | emulator ROM / MIDI - identified from magic bytes, not knowledge |
| `.pdf` | 2 | 0.1 | storable | workbench upload -> memory |
| `.mid` | 4 | 0.1 | non-document | emulator ROM / MIDI - identified from magic bytes, not knowledge |
| `.pyc` | 6 | 0.1 | code | source code; belongs to structural reach (P9), not document ingest |
| `.mdx` | 12 | 0.1 | storable | workbench upload -> memory |
| `.jsonl` | 7 | 0.0 | read-only | Eve can read it; not storable |
| `(none)` | 175 | 0.0 | internal | tool state, not content |
| `.db` | 1 | 0.0 | unknown | no door claims this extension |
| `.yaml` | 24 | 0.0 | config | structured config/data, not prose |
| `.gz` | 1 | 0.0 | archive | container; nothing unpacks it |
| `.sh` | 2 | 0.0 | code | source code; belongs to structural reach (P9), not document ingest |
| `.js` | 1 | 0.0 | code | source code; belongs to structural reach (P9), not document ingest |
| `.go` | 1 | 0.0 | code | source code; belongs to structural reach (P9), not document ingest |
| `.xml` | 1 | 0.0 | config | structured config/data, not prose |
| `.bat` | 2 | 0.0 | code | source code; belongs to structural reach (P9), not document ingest |
| `.gdoc` | 15 | 0.0 | cloud-stub | pointer to cloud content; the bytes are not the document |
| `.gsheet` | 1 | 0.0 | cloud-stub | pointer to cloud content; the bytes are not the document |

## Buckets

| bucket | files | MB |
|--------|------:|---:|
| storable | 13,757 | 1,690.6 |
| audio | 92 | 976.5 |
| video | 1 | 74.8 |
| non-document | 44 | 21.5 |
| unknown | 6 | 19.8 |
| archive | 60 | 18.6 |
| data | 81 | 6.8 |
| code | 394 | 3.8 |
| cognee-only | 52 | 3.4 |
| image | 14 | 1.2 |
| read-only | 11 | 0.7 |
| internal | 175 | 0.0 |
| config | 25 | 0.0 |
| cloud-stub | 16 | 0.0 |

## Unclaimed formats, identified from their bytes

- `.synth` -> ZIP container (Office/openxml or zip) (sample: `1503-Danny-Baranowsky-Gerudo-Valley-Cadence-of-Hyrule-daylightsilence.synth`)
- `.db` -> binary, magic 53514c6974652066 (sample: `_smoke_memory.db`)

## What this gates

**The biggest finding is a negative one.** The `non-document` bucket — emulator ROMs and MIDI, identified
from magic bytes rather than inferred from extensions — is content that no document brick should ever touch.
Together with `code` (which belongs to P9's structural reach) it accounts for most of what first looked like
"501 unclassified files". A converter proposed for that pile would have been waste.

The actionable items, in cheapness order:

1. **`md-variant` and `mail` are ~free.** `.mdx` is markdown with a different extension and `.eml` is
   text-encoded mail: both are text a reader already exists for. This is a routing change, not a component.
2. **`office-gap` is a capability fix, not a volume win.** Docling is installed and already converts
   docx/pptx/xlsx, but `pipeline/ingest_files.py:124` routes **only** `.pdf` through it. Correct to fix — and
   the census shows only a handful of Office files locally, so it must not be sold as a big win.
3. **`audio` is the only large measured target** (see the bucket table), and it is P8 — now unblocked by P3's
   retry/quarantine, since a batch this size *will* have partial failures.
4. **`image` is the only bucket that genuinely needs OCR**, which is what gates `surya`.
5. **`cloud-stub` needs nothing**: `.gdoc`/`.gsheet` are pointers whose bytes are not the document.

Method: the accept-lists are **imported from the modules themselves**, so this census fails loudly rather
than silently drifting when a door changes; and unclaimed formats are identified by reading their bytes.
