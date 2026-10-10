# Framer portfolio import pack (demonstration hub)

Web portfolio fuel for the **Empire / Eve story** (from [ODYSSEY.md](../../docs/ODYSSEY.md)), not the live EMPIRE stack.

Generated from [`docs/PORTFOLIO.md`](../../docs/PORTFOLIO.md) and [`docs/PORTFOLIO_FRAMER.md`](../../docs/PORTFOLIO_FRAMER.md).  
**Synced:** 2026-10-08 · Regenerate when PORTFOLIO case studies or timeline change.

## Quick start (Framer CMS)

1. Open your Framer site → **CMS** (database icon).
2. Create a collection (or use existing) for each CSV below.
3. **⋯ menu → Import** (or **Add → Import CSV**) and pick the file.
4. Map columns to field types:

| CSV column | Suggested Framer field |
|------------|------------------------|
| `slug` | Plain text (use as slug / URL key) |
| `title`, `headline`, `name` | Plain text |
| `body`, `problem`, `approach`, `outcome` | **Formatted text** or Plain text |
| `sort_order` | Number |
| `year`, `era` | Plain text or Option |
| `image_url` | **Image** (empty until you upload; or paste URLs after hosting screenshots) |
| `visual_notes` | Plain text (hidden / dev notes) |

5. Bind collection lists to **Repeat** stacks on the canvas (Timeline, Slides, Case studies, Skills, Lessons).

## Files

| File | Collection purpose | Rows |
|------|-------------------|------|
| [`site-meta.csv`](site-meta.csv) | Hero + footer (single row) | 1 |
| [`timeline.csv`](timeline.csv) | Progression milestones | 14 |
| [`eras.csv`](eras.csv) | Four era bands for horizontal timeline | 4 |
| [`slides.csv`](slides.csv) | Full-viewport / deck sections | 15 |
| [`case-studies.csv`](case-studies.csv) | Project deep-dive cards | 7 |
| [`lessons.csv`](lessons.csv) | “What I learned” cards | 7 |
| [`skills.csv`](skills.csv) | Skills tags | 10 |
| [`portfolio-import.json`](portfolio-import.json) | Same data in one JSON (API / custom code) |

## Suggested page structure in Framer

```
Hero          ← bind site-meta (title, thesis, subtitle)
Timeline      ← Repeat eras + nested timeline (filter era slug) OR one Repeat on timeline sorted by sort_order
Pattern       ← static + site-meta.pattern_summary
Case studies  ← Repeat case-studies sorted by sort_order
Lessons       ← Repeat lessons
Skills        ← Repeat skills
Contact       ← site-meta.github_url, contact_line
Optional deck ← Repeat slides sorted by slide_number (scroll snap section)
```

## Images

`image_url` columns are **empty** on purpose. After import:

1. Upload screenshots to Framer Assets or your CDN.
2. Paste URLs into CMS image fields, or drag assets onto bound components.

See image hints in `visual_notes` (slides) and `image_hint` (case studies).

## Maintenance

When [`docs/ODYSSEY.md`](../../docs/ODYSSEY.md) changes → update [`docs/PORTFOLIO.md`](../../docs/PORTFOLIO.md) → edit these CSVs (or ask Cursor to regenerate the pack from PORTFOLIO).
