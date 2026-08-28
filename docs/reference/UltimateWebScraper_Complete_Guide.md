# Ultimate Web Scraper — Complete Documentation & Guides

*This document was scraped from the official Ultimate Web Scraper documentation and cleaned/reformatted for ingestion into NotebookLM as a learning-plan source.*

**Source:** https://ultimatewebscraper.com/docs/guides (and the full `/docs/*` documentation tree)
**Total pages:** 42
**Date scraped:** July 18, 2026

---

## Table of Contents

- [Overview](#overview)
  - [FAQ & Limitations](#faq-limitations)
  - [Ultimate Web Scraper Documentation](#ultimate-web-scraper-documentation)
- [Getting Started](#getting-started)
  - [Install the Chrome Extension](#install-the-chrome-extension)
  - [Local Extension vs. Cloud Platform](#local-extension-vs-cloud-platform)
  - [Quickstart: Your First Extraction](#quickstart-your-first-extraction)
- [Chrome Extension Tools](#chrome-extension-tools)
  - [Data Table](#data-table)
  - [Email Extractor](#email-extractor)
  - [Exporting Data](#exporting-data)
  - [Image Downloader](#image-downloader)
  - [Chrome Extension](#chrome-extension)
  - [List Extractor](#list-extractor)
  - [Page Extractor](#page-extractor)
  - [Page Text Extractor](#page-text-extractor)
  - [Recipes](#recipes)
  - [Shopify Extractor](#shopify-extractor)
  - [Sitemap Explorer](#sitemap-explorer)
  - [Social Link Extractor](#social-link-extractor)
- [Cloud Platform](#cloud-platform)
  - [Cookies & Sessions: Scrape Behind Logins in the Cloud](#cookies-sessions-scrape-behind-logins-in-the-cloud)
  - [How Cloud Credits Work](#how-cloud-credits-work)
  - [The Cloud Dashboard: Tasks, Data & Workspaces](#the-cloud-dashboard-tasks-data-workspaces)
  - [Cloud Platform Overview: Scraping in Cloud Browsers](#cloud-platform-overview-scraping-in-cloud-browsers)
  - [Cloud Integrations: Google Sheets & Webhooks](#cloud-integrations-google-sheets-webhooks)
  - [Proxies & Page Unblocker for Cloud Scraping](#proxies-page-unblocker-for-cloud-scraping)
  - [Running Cloud Tasks: The Run in Cloud Wizard](#running-cloud-tasks-the-run-in-cloud-wizard)
  - [Cloud Scheduling: Recurring Web Scraping](#cloud-scheduling-recurring-web-scraping)
- [AI Agents & MCP](#ai-agents-mcp)
  - [AI-Started Extractions](#ai-started-extractions)
  - [What AI Agents Can Do](#what-ai-agents-can-do)
  - [AI Agents & MCP Overview](#ai-agents-mcp-overview)
  - [AI Connection Security](#ai-connection-security)
- [Guides](#guides)
  - [How to Bulk Download Images from Any Webpage](#how-to-bulk-download-images-from-any-webpage)
  - [Discover Every URL a Website Publishes](#discover-every-url-a-website-publishes)
  - [Export Any Shopify Store to a Re-importable CSV](#export-any-shopify-store-to-a-re-importable-csv)
  - [Turn Webpages into Clean Text for AI and LLM Projects](#turn-webpages-into-clean-text-for-ai-and-llm-projects)
  - [Extract the Same Data from Hundreds of Pages](#extract-the-same-data-from-hundreds-of-pages)
  - [Extract Google Maps Listings into a Spreadsheet](#extract-google-maps-listings-into-a-spreadsheet)
  - [How to Find Email Addresses on Any Website](#how-to-find-email-addresses-on-any-website)
  - [Find Social Media Profiles for a List of Websites](#find-social-media-profiles-for-a-list-of-websites)
  - [Guides](#guides-2)
  - [Schedule Recurring Extractions for Price Monitoring](#schedule-recurring-extractions-for-price-monitoring)
  - [How to Scrape Any List or Table from a Website](#how-to-scrape-any-list-or-table-from-a-website)
  - [How to Scrape Pages Behind a Login](#how-to-scrape-pages-behind-a-login)
  - [Scrape Product Data with Zero Configuration](#scrape-product-data-with-zero-configuration)

---

## Overview

### FAQ & Limitations

*Quick answers about Ultimate Web Scraper — what it can extract, free limits, pagination, logins, captchas, scheduling, and known limitations.*

**Source:** https://ultimatewebscraper.com/docs/faq

#### Capabilities


> **Note:** Answers to these FAQ questions are loaded dynamically on the live site and were not present in the static page content during scraping. Visit the [FAQ page](https://ultimatewebscraper.com/docs/faq) directly to read full answers.

###### Can it extract a table or list from a page in one click?

###### Does it handle infinite scroll, 'Next' buttons, and 'Load more' buttons?

###### Can it scrape many similar pages at once?

###### Can it extract product data without configuring anything?

###### Can it find emails or social profiles across a whole website?

###### Can it schedule recurring extractions or run without my computer?

###### Can I connect Claude or another AI assistant to my data?

###### Can I scrape pages behind a login?

###### Does it solve captchas?

#### Known limitations

- **LinkedIn is not supported** — it's blocked as a target in every tool, including for AI agents.
- **Shadow DOM and cross-origin iframes** aren't reachable by element picking.
- **Browser-internal pages** (chrome://, extension pages, non-http(s)) can't be scanned.
- **Content that requires interaction to appear** (beyond scrolling/pagination) isn't captured; JS-rendered content is handled via configurable load waits.
- **Images download as individual files** into one folder — not a ZIP.
- **Tables can't be merged** with each other (column merge within a table is supported), and there's no Markdown export.
- **Local data is device-local.** Uninstalling the extension or clearing browser data deletes local results; retention keeps the newest 100/500/1,000 tables (configurable). Cloud results persist in the dashboard.

#### Support

- Feature requests: [ultimatewebscraper.featurebase.app](https://ultimatewebscraper.featurebase.app/)
- Community: [reddit.com/r/ultimatewebscraper](https://www.reddit.com/r/ultimatewebscraper)
- Contact support directly from the extension's Settings panel.

[Schedule Recurring Extractions for Price Monitoring

Turn any extraction into a scheduled cloud task — from every 10 minutes to monthly — with results flowing into Google Sheets or a webhook automatically.](https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions)


---

### Ultimate Web Scraper Documentation

*Learn how to extract data from any website with the Ultimate Web Scraper Chrome extension and Cloud Platform. Point-and-click scraping, no code required.*

**Source:** https://ultimatewebscraper.com/docs

**Ultimate Web Scraper** (also known as Panda Extract) is a point-and-click web data extraction toolkit made of two parts that work together:

- **The Chrome extension** — lives in Chrome's side panel and extracts data directly in your browser. Everything runs locally: results are stored on your machine, extraction is free and uncapped, and your data never leaves your computer unless you choose to send it somewhere.
- **The Cloud Platform** — runs and schedules extractions in cloud browsers, with built-in proxies, anti-blocking, integrations like Google Sheets and webhooks, and a web dashboard for your results. No computer needed.

No code, no selectors to write by hand, no scraping scripts to maintain.

- [Getting started](https://ultimatewebscraper.com/docs/getting-started/installation) — Install the extension and run your first extraction in under a minute.
- [Chrome extension tools](https://ultimatewebscraper.com/docs/extension) — Seven extraction tools: lists, pages, emails, images, Shopify stores and more.
- [Cloud Platform](https://ultimatewebscraper.com/docs/cloud) — Run extractions in cloud browsers on a schedule, with proxies and integrations.
- [AI connections (MCP)](https://ultimatewebscraper.com/docs/ai) — Connect Claude and other AI agents to your scraped data. Rolling out now.
- [Guides](https://ultimatewebscraper.com/docs/guides) — Step-by-step recipes for common jobs: leads, catalogs, images, monitoring.
- [FAQ](https://ultimatewebscraper.com/docs/faq) — Quick answers: what's possible, what's free, and known limitations.

#### The tools

Everything in the app is organized around **seven extraction tools** — each built for one kind of job, each with its own identity in the side panel. If you know what you want to extract, you know which tool to open:

[List ExtractorTurn any list, table, or grid into a spreadsheet by clicking one itemSearch results, product grids, directories, job boards, tables — with infinite scroll, pagination, and Load More handling](https://ultimatewebscraper.com/docs/extension/list-extractor)[Page ExtractorVisit a list of URLs and extract the same fields from every pageProduct pages, profiles, articles, Google Maps places — one structured row per URL, with zero-config structured-data extraction](https://ultimatewebscraper.com/docs/extension/page-extractor)[Image DownloaderFind and bulk-download every image on a pageImages incl. lazy-loaded and CSS backgrounds, grouped by size, filtered, and saved with smart filenames](https://ultimatewebscraper.com/docs/extension/image-downloader)[Email ExtractorFind email addresses across whole websitesStandard, obfuscated ('name at domain dot com') and mailto emails, with deep scanning of sub-pages](https://ultimatewebscraper.com/docs/extension/email-extractor)[Shopify ExtractorExport a Shopify store's whole catalog as a re-importable CSVEvery product and variant — prices, options, images, barcodes — as a Shopify-import-ready CSV](https://ultimatewebscraper.com/docs/extension/shopify-extractor)[Social Link ExtractorFind social media profiles for any list of websitesX, Facebook, Instagram, YouTube, TikTok, GitHub, Pinterest profiles + custom patterns, one column per platform](https://ultimatewebscraper.com/docs/extension/social-link-extractor)[Page Text ExtractorTurn webpages into clean, AI-ready text with metadataBoilerplate-free article text plus title, description, author, publish date, and word count per page](https://ultimatewebscraper.com/docs/extension/page-text-extractor)

Every result lands in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — a spreadsheet-like workspace where you edit, clean, and [export](https://ultimatewebscraper.com/docs/extension/exporting-data) your data. The [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) feeds tools with URLs, and [Recipes](https://ultimatewebscraper.com/docs/extension/recipes) save any setup for re-running.

#### How the pieces fit

1. **Extract locally, for free.** All seven tools run in your browser with no page or row caps.
2. **Save what works as a [recipe](https://ultimatewebscraper.com/docs/extension/recipes)** so you can re-run it anytime — or share it as a file.
3. **Send it to the [cloud](https://ultimatewebscraper.com/docs/cloud)** to run on a schedule, behind proxies, without keeping your computer on.
4. **Connect [AI agents](https://ultimatewebscraper.com/docs/ai)** to analyze, clean, and even launch extractions from a chat.

[Install the Chrome Extension

Install Ultimate Web Scraper from the Chrome Web Store and open the side panel. Setup takes under a minute — no account required to start extracting.](https://ultimatewebscraper.com/docs/getting-started/installation)


---

## Getting Started

### Install the Chrome Extension

*Install Ultimate Web Scraper from the Chrome Web Store and open the side panel. Setup takes under a minute — no account required to start extracting.*

**Source:** https://ultimatewebscraper.com/docs/getting-started/installation

*[Screenshot: The extension's side panel open on a webpage, freshly installed, showing the tools grid]*

#### Install from the Chrome Web Store

##### Add the extension

Install **Ultimate Web Scraper** from the [Chrome Web Store](https://chromewebstore.google.com/detail/ultimate-web-scraper/pdeldjlcnhallaapdggcmhpailpnnkmg). It works on Chrome and Chromium-based browsers that support side panels.

##### Pin it (optional)

Click the puzzle-piece icon in Chrome's toolbar and pin Ultimate Web Scraper so it's always one click away.

##### Open the side panel

Click the extension icon. The side panel opens with the tools grid — that's home base for every extraction.

No account or sign-up is needed for local extraction. You only sign in when you want to use the [Cloud Platform](https://ultimatewebscraper.com/docs/cloud).

#### Where your data lives

Extraction runs **locally in your browser**, and results are stored locally in your browser's storage. Data leaves your machine only when you explicitly use cloud features, Google Sheets export, or webhooks. See [Local vs. Cloud](https://ultimatewebscraper.com/docs/getting-started/local-vs-cloud) for the full picture.

#### Next step

Run your [first extraction](https://ultimatewebscraper.com/docs/getting-started/quickstart) — it takes one click.

[Quickstart: Your First Extraction

Extract a list from any webpage in one click with Quick List Extraction, then export it as a spreadsheet. A 60-second tour of the core workflow.](https://ultimatewebscraper.com/docs/getting-started/quickstart)


---

### Local Extension vs. Cloud Platform

*Understand the two halves of Ultimate Web Scraper — free local extraction in your browser, and scheduled cloud extraction with proxies and integrations.*

**Source:** https://ultimatewebscraper.com/docs/getting-started/local-vs-cloud

Ultimate Web Scraper has two execution environments. Knowing which one you're using explains where your data is, what it costs, and what features are available.

#### The Chrome extension (local)

Everything in the [extension's tools](https://ultimatewebscraper.com/docs/extension) runs **inside your own browser**:

- Pages are loaded in your tabs, with your session — sites see a normal logged-in visitor.
- Results are stored **locally** in your browser's storage and shown in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table).
- Local extraction is **free with no page or row caps**, and never consumes cloud credits.
- Your data leaves the machine only if you export to Google Sheets or use cloud features.

The trade-offs: your computer has to be on and the browser open, there are no proxies, and there's no scheduling.

#### The Cloud Platform

The [Cloud Platform](https://ultimatewebscraper.com/docs/cloud) runs the same kinds of extractions in **cloud browsers**:

- Runs happen on our infrastructure — close your laptop, results keep coming.
- [Schedules](https://ultimatewebscraper.com/docs/cloud/scheduling) from every 10 minutes to monthly.
- ISP and residential [proxies with location choice](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking), plus automatic unblocking for supported challenges.
- [Google Sheets and webhook integrations](https://ultimatewebscraper.com/docs/cloud/integrations).
- Results live in the [web dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard), where your [AI agents can reach them too](https://ultimatewebscraper.com/docs/ai).

Cloud runs require a paid plan and consume [credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — 1 credit per page extracted.

#### The recommended workflow

**Build and test locally.** Configure an extraction with the extension on your machine — it's free, instant, and interactive.

**Send it to the cloud.** Use **Run in Cloud** in the side panel to hand that working configuration to a cloud browser.

**Schedule and integrate.** Add a schedule, proxies, Google Sheets export, or a webhook — and manage everything from the dashboard.

#### Side by side

|  | Extension (local) | Cloud Platform |
| --- | --- | --- |
| Cost | Free, uncapped | Paid plan + credits (1 credit/page) |
| Where it runs | Your browser | Cloud browsers |
| Computer needed | Yes, browser open | No |
| Scheduling | No | Yes, 11 presets |
| Proxies | No | ISP & residential, location choice |
| Captcha/unblocking | No | Supported challenges auto-handled |
| Results stored | Locally in your browser | Cloud dashboard |
| Integrations | Google Sheets export, clipboard, files | Google Sheets, webhooks, exports |
| AI agent access | No (local data stays private) | Yes, via [MCP](https://ultimatewebscraper.com/docs/ai) |

[Quickstart: Your First Extraction

Extract a list from any webpage in one click with Quick List Extraction, then export it as a spreadsheet. A 60-second tour of the core workflow.](https://ultimatewebscraper.com/docs/getting-started/quickstart)


---

### Quickstart: Your First Extraction

*Extract a list from any webpage in one click with Quick List Extraction, then export it as a spreadsheet. A 60-second tour of the core workflow.*

**Source:** https://ultimatewebscraper.com/docs/getting-started/quickstart

The fastest way to understand Ultimate Web Scraper is to grab a list off a page.

*[Screenshot: The side panel with the yellow Quick List Extraction button highlighted]*

#### One-click list extraction

##### Open a page with a list

Any repeating content works: search results, product grids, directories, tables, job boards.

##### Click the yellow cursor button

At the top of the side panel, click the yellow cursor — **Quick List Extraction**. An element picker appears on the page.

##### Click one item in the list

Hover over the list — the extension highlights the detected list container and tells you how many items it found ("List with 24 items found — Smart detection"). Click to select.

##### See your data instantly

The **Data Table** opens in a new tab with every visible item as a structured row — titles, links, images, prices, and ratings automatically detected and typed.

> **Quick vs. full extraction**
>
> Quick List Extraction grabs the items **currently visible** on the page — perfect for instant one-shot grabs. To also load more items with auto-scroll, pagination, or "Load more" buttons, open the full [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) tool.

#### What just happened?

- Field detection was automatic: all visible text, links, and images were captured per item and organized into typed columns (Title, Price, Link, Image, Rating…).
- The rows were saved **locally in your browser** — nothing was uploaded anywhere.
- The extraction was free. Local extraction is always free and uncapped.

#### Clean it up and export

In the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) you can rename or delete columns, edit cells, merge columns, filter out empty rows, and sort. When you're happy, use the **Export** menu to copy the data or download it as CSV, Excel, JSON, or Google Sheets (see [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) for all formats).

#### Where to go next

- [List Extractor in depth](https://ultimatewebscraper.com/docs/extension/list-extractor) — Auto-scroll, pagination, Load More, speed profiles.
- [Extract from many pages](https://ultimatewebscraper.com/docs/extension/page-extractor) — Visit a list of URLs and pull the same fields from each.
- [Save it as a recipe](https://ultimatewebscraper.com/docs/extension/recipes) — Re-run this exact extraction anytime, or share it.
- [Run it in the cloud](https://ultimatewebscraper.com/docs/cloud) — Schedule it, add proxies, and get results in the dashboard.


---

## Chrome Extension Tools

### Data Table

*The spreadsheet-like workspace where every extraction lands. Edit cells, rename and retype columns, filter, search, and clean data — all stored locally.*

**Source:** https://ultimatewebscraper.com/docs/extension/data-table

The spreadsheet workspace where every result lands: edit, clean, merge, export

Every extraction lands in the **Data Table** — a spreadsheet-like workspace that opens in its own browser tab. Open it anytime with the **DATA** button in the side panel; it also opens automatically for List Extractor previews and from every tool's progress overlay.

TextPriceDateImageLinktyped columns — edit, clean, merge, export

Every extraction lands here — typed columns you edit, clean, and export.

*[Screenshot: The Data Table with an extraction loaded, showing typed columns and image thumbnails]*

#### Local storage and retention

All rows are stored **locally in your browser** — nothing is uploaded unless you export to Google Sheets or use [cloud](https://ultimatewebscraper.com/docs/cloud) features. Duplicate rows within a table are skipped automatically.

Retention keeps the newest **500 tables by default**, configurable to the last 100, 500, or 1,000 in Settings → Data Management. There's no row cap per table. Since data is device-local, uninstalling the extension or clearing site data deletes it.

#### Working with tables

- **Table selector:** every table listed newest-first with favicon, name, live row count, tool tag, and date — searchable, with the most recent auto-opened.
- **Live mode:** while an extraction runs, the open table refreshes every few seconds with a new-rows indicator (pausable).
- **Sample tables** are bundled so you can try every feature — including all exports — for free.
- **CSV import:** bring any CSV in as a new table.

#### Editing

- **Cells:** inline editing, with modification history.
- **Columns:** rename; change type (10 types: text, number, price, date, link, image, email, phone, address, metadata); drag to reorder; resize; delete; and **merge** two or more columns into a new combined column with a separator of your choice.
- **Sorting:** click any header (ascending/descending); the default order is the original input order.
- **Search:** case-insensitive across all columns — and applied before exports, so you can export just the matching rows.

#### Cleanup filters

Rule-based (not AI) one-click cleanup: remove empty rows and columns, remove duplicate or repeating columns, hide mostly-empty columns, and prioritize data density. Image display options control thumbnail size and how image lists render.

#### Images

Image columns render as **thumbnails** with a lightbox gallery. The **bulk image download modal** downloads all images or specific image columns, with sequential, by-column, or custom-pattern naming.

#### What it doesn't do

- **No table-to-table merging** — two tables can't be combined into one (column merge works within a single table only).
- **No local AI features** — there's no LLM-based cleanup in the extension. AI cleanup (rename, retype, merge, delete columns by asking an agent) exists for **cloud** tables via MCP — see [AI connections](https://ultimatewebscraper.com/docs/ai).

#### Related

- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — CSV, Excel, JSON, Google Sheets, Shopify CSV — and what's free.
- [Recipes](https://ultimatewebscraper.com/docs/extension/recipes) — Save the extraction that produced a table and re-run it.
- [AI connections (MCP)](https://ultimatewebscraper.com/docs/ai) — Let AI agents query and clean your cloud tables.


---

### Email Extractor

*Find email addresses across many pages at once, with deep scanning of internal links, obfuscated-email detection, custom patterns, and domain filters.*

**Source:** https://ultimatewebscraper.com/docs/extension/email-extractor

Find email addresses across whole websites Free & uncapped locally Runs in cloud Recipes supported

The Email Extractor finds email addresses across one or many pages — and, with deep scanning, across the pages those pages link to. Point it at a list of company websites and it comes back with one row of emails per site.

acme.com@deep scanEMAILSa site + its linked pagesemails, per site

Each site and the pages it links to are scanned — emails collected per site.

*[Screenshot: The progress overlay with the emails found counter and per-domain breakdown]*

#### Adding URLs

Three sources:

- **Manual Input** — type or paste URLs directly.
- **Upload CSV** — pick the column that contains URLs.
- **Data Source** — reuse a URL column from a previous extraction (for example, a website column scraped with the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor)).

#### Deep scan

Deep scanning is **on by default**: for each URL you give it, the tool also follows the page's internal links and scans those pages for emails — which is usually where contact and about pages live.

| Setting | Default | Range |
| --- | --- | --- |
| Depth | 1 (the seed page's direct links) | 1–5 |
| Max links followed per page | 10 | 1–50 |
| Stay on domain | on | Only follows same-hostname links |
| Delay between requests | 1500 ms | 0–5000 ms |

Mailto/tel/javascript links, page fragments, and asset files (documents, images, media, scripts) are skipped automatically. Each URL gets up to 2 attempts; permanent errors like 404s aren't retried, and failures never stop the batch.

#### What it detects

Detection runs on the page's rendered text plus mailto links:

- **Standard addresses**, including variants with spaces around the @ sign.
- **Obfuscated addresses**, normalized to real ones: "name (at) domain dot com", `[at]` and `{at}` style brackets, "at … dot …" spellings, and similar tricks.
- **Mailto links**, with query parameters stripped.
- **Custom regex patterns** you supply (one per line; off by default).

Results are deduplicated globally across all scanned pages, lowercased, and validated. An optional **domain filter** keeps only addresses from domains you list.

You can also toggle on **social link collection** to capture social profiles in the same run — that's the full [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) engine.

#### Output

One row per seed URL, in input order, streamed live into the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table):

| Column | Content |
| --- | --- |
| URL | The seed URL |
| Emails | All emails found, comma-joined |
| Email Count | How many |

With social collection on, you also get one column per social platform.

#### Recipes

Recipes are fully supported. Deep scan, obfuscation handling, custom patterns, and domain filters are all included; the Faster Extraction toggle runs several tabs in parallel for large jobs.

#### Limitations

- LinkedIn URLs can't be scanned as targets.
- Emails that only exist inside images, or that require interaction to reveal, aren't detected.
- Content that never renders into the page isn't captured (the tool waits for contact signals to settle, which covers most JavaScript-rendered pages).

#### Related

- [Guide: Find emails on any website](https://ultimatewebscraper.com/docs/guides/find-emails-on-any-website) — A lead-list walkthrough from URL list to export.
- [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) — The same engine, tuned for social profiles.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Get your email list out as CSV, Excel, or Sheets.


---

### Exporting Data

*Export your extracted tables as CSV, Excel, JSON, Google Sheets, or Shopify CSV — all from the Data Table's Export menu. Filter first to export just the rows you want.*

**Source:** https://ultimatewebscraper.com/docs/extension/exporting-data

Every extraction runs locally with no page or row caps, and you get your results out from the [Data Table's](https://ultimatewebscraper.com/docs/extension/data-table) **Export** menu.

CSVXLSXJSONSheetsyour tableevery format

One table, out to CSV, Excel, JSON, or Google Sheets.

*[Screenshot: The Export menu open, showing all formats]*

#### Formats

| Format | Details |
| --- | --- |
| CSV | UTF-8 with BOM, properly escaped |
| Excel (.xlsx) | Styled header, autofilter, frozen header row |
| JSON | Pretty-printed |
| Google Sheets | Copies the data and opens a new sheet to paste into |
| Shopify CSV | Import-ready format; appears on Shopify tables only |
| Copy to Clipboard | Tab-separated values, paste anywhere |

A couple of details worth knowing:

- Your current table **search is applied before export** — filter first to export just the rows you want.
- Which formats and export volumes are included depends on your plan — see [pricing](https://ultimatewebscraper.com/pricing) for what each plan covers.

#### Try every format with sample tables

The bundled **sample tables let you try every export format** — CSV, Excel, JSON, Google Sheets, whatever fits your workflow — so you can confirm the output works for you before committing to a real job.

#### Where exports don't apply

- **Sitemap Explorer** has its own URL CSV export — [discovered URL lists](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) download as a one-column CSV.
- **Image downloads** aren't table exports: the [Image Downloader](https://ultimatewebscraper.com/docs/extension/image-downloader) saves image files directly, and the Data Table has a separate bulk image-download modal for image columns.
- **Cloud tables** export from the web dashboard — see the [Cloud Platform](https://ultimatewebscraper.com/docs/cloud).

> **Your data is always yours**
>
> Viewing, editing, cleaning, and searching your extracted data in the Data Table are never gated — everything you extract stays fully accessible.

#### Related

- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Clean and filter your data before exporting it.
- [Shopify Extractor](https://ultimatewebscraper.com/docs/extension/shopify-extractor) — Produces the import-ready Shopify CSV format.
- [Pricing](https://ultimatewebscraper.com/pricing) — What each plan includes.


---

### Image Downloader

*Scan a page for every image — including lazy-loaded images and CSS backgrounds — filter by size or type, and download them all into one organized folder.*

**Source:** https://ultimatewebscraper.com/docs/extension/image-downloader

Find and bulk-download every image on a page Free in your browser Extension only No recipes

The Image Downloader finds every image on a page and downloads the ones you want in bulk. Open the tool and it **automatically scans the current tab** — no setup step.

gallery.example.comcollect allevery image on the pageone tidy folder

Every image on the page, saved into one organized folder.

*[Screenshot: The image grid grouped by size with the filters visible]*

#### Scanning

Images appear grouped by **size category** (Tiny up to Extra Large) and by similar dimensions, largest groups first. From there you can:

- **Filter** by search text (alt text, URL, dimensions), min/max width and height, file extension, image type, size category, or whether the image has alt text.
- **Auto-scroll** — turn it on and re-scan to capture lazy-loaded and infinite-scroll images. The tool steps down the page nudging images to load, keeps collecting even on virtualized pages, then restores your scroll position.
- Download **per image**, **per group**, or **Download all**.

#### What it finds

- `<img>` tags, including common lazy-load attributes and the largest candidate from srcset.
- **CSS background images** and pseudo-element content images.
- Excluded: `data:` URIs, hidden images, and very small icons. Duplicates are removed by URL.

#### Three source modes

| Mode | What it scans |
| --- | --- |
| **Scan Page** | The current tab |
| **Scan Pages** | A list of page URLs, batch-scanned in background tabs (1–5 in parallel) with pre-scan filters like "Large only" or "Photos only" |
| **Import URLs** | Direct image URLs — pasted, from a CSV, or from a data source — downloaded directly |

#### How downloads work

- Images download as **individual files, not a ZIP**, with no per-file save dialogs.
- Everything lands in a **timestamped folder** inside your Downloads directory, e.g. `images_2026-07-11_14-30-00`.
- **Smart filenames:** original filename (optional), falling back to sanitized alt text, falling back to a dimensions-based name — with automatic deduplication.
- **Multi-page organization** (Scan Pages mode): keep all files together, create a subfolder per page, or prefix filenames with the page name.
- Downloads run a few at a time and can be cancelled.

#### Limitations

Single-page scanning, all filters, auto-scroll, and downloads run right in your browser. Scan Pages and Import URLs handle multi-page and direct-URL jobs; bulk-downloading images from a table's image columns lives in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table).

- **No recipes** — this tool is interactive rather than a saved automation.
- `data:`-URI images can't be captured.
- Imported URLs blocked by CORS land in an "Unknown" size group but remain downloadable.
- LinkedIn is not supported, and browser-internal pages can't be scanned.

#### Related

- [Guide: Bulk download images](https://ultimatewebscraper.com/docs/guides/bulk-download-images) — From product page to organized image folder.
- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Image thumbnails, lightbox, and bulk download from image columns.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Every format for getting your data out.


---

### Chrome Extension

*Seven point-and-click extraction tools that live in Chrome's side panel. Everything runs locally in your browser — free, uncapped, and no code required.*

**Source:** https://ultimatewebscraper.com/docs/extension

The Ultimate Web Scraper extension lives in Chrome's **side panel** and turns web pages into structured data with clicks, not code. Extraction runs entirely in your browser: results stay on your machine, and running any tool locally is free with no page or row caps.

Any web pageOne of 7 toolsData TableCSV · XLSX · JSONeverything runs locally, in your browser

One flow: any page → a purpose-built tool → the Data Table → your export.

*[Screenshot: The side panel home screen showing the 7-tool grid]*

#### The side panel

Open the side panel and you'll find:

- **Quick List Extraction** — the yellow cursor button. One click starts an element picker and instantly grabs any visible list or table on the current page. It's the fastest path from "I see a list" to "I have a spreadsheet" (see the [Quickstart](https://ultimatewebscraper.com/docs/getting-started/quickstart)).
- **A grid of seven tools** — each built for a specific job, listed below.
- **Recipes** — saved extraction setups you can re-run or share (see [Recipes](https://ultimatewebscraper.com/docs/extension/recipes)).
- **Cloud section** — send a tested extraction to the [Cloud Platform](https://ultimatewebscraper.com/docs/cloud) to run on a schedule without your computer.
- **Nav buttons** — MENU (home), CLOUD (web dashboard), and DATA, which opens the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) in its own tab.

#### The seven tools

Each tool is built for one job, with its own color and icon in the side panel — pick the tool that matches what you're extracting:

[List ExtractorTurn any list, table, or grid into a spreadsheet by clicking one itemSearch results, product grids, directories, job boards, tables — with infinite scroll, pagination, and Load More handling](https://ultimatewebscraper.com/docs/extension/list-extractor)[Page ExtractorVisit a list of URLs and extract the same fields from every pageProduct pages, profiles, articles, Google Maps places — one structured row per URL, with zero-config structured-data extraction](https://ultimatewebscraper.com/docs/extension/page-extractor)[Image DownloaderFind and bulk-download every image on a pageImages incl. lazy-loaded and CSS backgrounds, grouped by size, filtered, and saved with smart filenames](https://ultimatewebscraper.com/docs/extension/image-downloader)[Email ExtractorFind email addresses across whole websitesStandard, obfuscated ('name at domain dot com') and mailto emails, with deep scanning of sub-pages](https://ultimatewebscraper.com/docs/extension/email-extractor)[Shopify ExtractorExport a Shopify store's whole catalog as a re-importable CSVEvery product and variant — prices, options, images, barcodes — as a Shopify-import-ready CSV](https://ultimatewebscraper.com/docs/extension/shopify-extractor)[Social Link ExtractorFind social media profiles for any list of websitesX, Facebook, Instagram, YouTube, TikTok, GitHub, Pinterest profiles + custom patterns, one column per platform](https://ultimatewebscraper.com/docs/extension/social-link-extractor)[Page Text ExtractorTurn webpages into clean, AI-ready text with metadataBoilerplate-free article text plus title, description, author, publish date, and word count per page](https://ultimatewebscraper.com/docs/extension/page-text-extractor)

#### Around the tools

Three features complete the workflow — URL discovery before a run, and your results workspace after:

[Sitemap ExplorerDiscover every URL a website publishes — up to 50,000 per site, free](https://ultimatewebscraper.com/docs/extension/sitemap-explorer)[Data TableThe spreadsheet workspace where every result lands: edit, clean, merge, export](https://ultimatewebscraper.com/docs/extension/data-table)[RecipesSave any extraction setup as a re-runnable, shareable recipe](https://ultimatewebscraper.com/docs/extension/recipes)

The grid above includes the [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) (reachable from inside the Page Extractor), the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) where every result lands, and [Recipes](https://ultimatewebscraper.com/docs/extension/recipes) for saving setups.

#### Behaviors every tool shares

- **Results stream to the Data Table.** Every tool writes rows live into the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — a spreadsheet-like tab where you edit, clean, and [export](https://ultimatewebscraper.com/docs/extension/exporting-data).
- **Progress overlays with Stop.** Long runs show live counts; you can stop at any time and keep the partial results, then jump straight to "View data & export CSV".
- **Welcome screens.** Each tool introduces itself on first use; you can re-open the intro anytime from the tool's About button.
- **Some pages are off-limits.** LinkedIn is not supported as a target in any tool, and browser-internal pages (like `chrome://` pages) can't be scanned.

#### Free and local

All seven tools run locally in your browser with no page or row caps. Cloud runs and some advanced options are part of the paid plans — see [pricing](https://ultimatewebscraper.com/pricing) for what's included.

[List Extractor

Turn any repeating list, grid, or table into a spreadsheet with one click. Handles infinite scroll, pagination, and Load More — free and uncapped locally.](https://ultimatewebscraper.com/docs/extension/list-extractor)


---

### List Extractor

*Turn any repeating list, grid, or table into a spreadsheet with one click. Handles infinite scroll, pagination, and Load More — free and uncapped locally.*

**Source:** https://ultimatewebscraper.com/docs/extension/list-extractor

Turn any list, table, or grid into a spreadsheet by clicking one item Free & uncapped locally Runs in cloud Recipes supported

The List Extractor turns any repeating content on a page — search results, product grids, directories, tables — into structured rows. You click one item; it detects the whole list.

shop.example.com/resultsdetect patternclick one itemthe whole list, as rows

Click one item — every match on the page becomes a row.

*[Screenshot: The element picker highlighting a list on a page with the 'List with N items found' tooltip visible]*

#### How it works

##### Select the list

Click **Click to Select List**. An element picker appears on the page: hovering highlights the detected list container and shows how many items were found ("List with 24 items found — Smart detection"). Click to select it.

##### See an instant preview

The moment you select, the tool extracts the currently visible items and opens the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) with a live preview — so you know within seconds whether the selection is right.

##### Choose how to load more items

Pick one of three methods (default: **Auto-Scroll**), then start the extraction. Rows stream into the Data Table as they're found.

#### The three load-more methods

*[Screenshot: The Load More Items step showing the Auto-Scroll, Pagination, and Load More options]*

| Method | How it works | When it stops |
| --- | --- | --- |
| **Auto-Scroll** (default) | Scrolls the page or container to trigger infinite scroll, extracting items as they appear | At the bottom, or when scrolling stops surfacing new items |
| **Pagination** | You pick the "Next" button or link with the picker; the tool extracts a page, clicks Next, waits for the page to change, and repeats | When no valid Next button is found |
| **Load More** | You pick a same-page "Load more" button; the tool clicks it repeatedly and extracts each new batch | When clicking stops surfacing new items |

There is **no row or page cap** — pagination and Load More run until the content is exhausted or you press Stop (partial results are kept). Pagination is click-based; there's no URL-pattern page generation.

#### What gets captured

Field detection is automatic. For each item, the tool captures:

- All visible **text**, deduplicated per element
- **Links** — `<a>` hrefs, resolved to absolute URLs
- **Images** — including lazy-loaded sources, with alt text captured as a description
- **CSS background images** and video posters
- **ARIA labels** on image-role elements (how star ratings on sites like Google Maps get captured)

Columns are auto-typed (text, link, image, number, price, date, rating, time) and auto-named (Title, Description, Price, Author, Date, Rating, Reviews, Link, Image). You can't pre-select fields — extract everything, then remove unwanted columns in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table).

#### Speed profiles

Three profiles — **Slow**, **Normal**, and **Fast** (the default) — control how long the tool waits for content to load, how quickly it scrolls, and how patiently it retries. Fast suits most sites; switch to Normal or Slow for pages that load content sluggishly and appear to miss items. Every timing value is individually editable and your changes persist.

#### Recipes

**Fully supported.** Save the selection, load-more method, and timing as a [recipe](https://ultimatewebscraper.com/docs/extension/recipes); running it auto-navigates your tab to the saved source URL. Extraction runs locally with no page or row caps.

#### Limitations

- List items must be **direct children of one container**, and smart detection needs at least 3 similar items.
- **No shadow DOM or iframe traversal** — content inside shadow roots or cross-origin iframes isn't reachable.
- The instant preview covers only items currently rendered on the page; run a full extraction to get the rest.
- LinkedIn is not supported.

#### Related

- [Guide: Scrape any list](https://ultimatewebscraper.com/docs/guides/scrape-any-list) — A step-by-step walkthrough with a real example.
- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Extracted a column of links? Visit each one and pull details.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Get your list out as CSV, Excel, JSON, or Google Sheets.


---

### Page Extractor

*Visit a list of URLs and extract the same fields from every page — one row per URL. Feed it CSVs, previous extractions, or sitemaps. No URL count cap.*

**Source:** https://ultimatewebscraper.com/docs/extension/page-extractor

Visit a list of URLs and extract the same fields from every page Free & uncapped locally Runs in cloud Recipes supported

The Page Extractor visits a list of URLs and pulls the same fields from every page — **one row per URL**. It's built for "collection of similar pages" jobs: product pages, profiles, articles, Google Maps places.

URL LISTvisit eacha list of URLsone row per page

Point it at a list of URLs; it visits each and fills one row per page.

*[Screenshot: Page Extractor step 1 with a URL list loaded]*

#### Step 1: Where the URLs come from

Five sources (there's no free-text paste box in this tool):

| Source | What it does |
| --- | --- |
| **Upload CSV** | Auto-detects which columns contain URLs; you pick the column |
| **Data Source** | Pulls a URL column from a previous extraction stored locally — this is how [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) results chain into the Page Extractor: extract a list of links, then visit each link |
| **Sitemap Explorer** | Discovers URLs from the current site's sitemaps — see [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) |
| **Cloud Data Source** | Cloud-synced tables, when you're signed in to the [cloud](https://ultimatewebscraper.com/docs/cloud) |
| **Recipe** | Prefilled by a saved [recipe](https://ultimatewebscraper.com/docs/extension/recipes) |

The first URL loads into your active tab so you can pick elements against a real page. Individual URLs can be removed before starting.

#### Step 2: What to extract

You build an ordered list of extraction steps; each step adds columns to the row:

- **Element picker** — click elements on the loaded page to define fields. Each picked element gets robust multi-selector fallbacks.
- **Automatic Extract** — zero-config structured-data extraction (see below).
- **Phone Numbers** — regex plus `tel:` link detection across the page. Free.
- **Google Maps** — place name, rating, address, phone, website, hours and more from Google Maps listings. Offered when Maps URLs are detected in your list; needs no picked elements.

#### Automatic Extract: structured data without selectors

If a page publishes structured data, you may not need to pick anything. Automatic Extract reads a page's **JSON-LD, microdata, and Open Graph/Twitter/standard meta tags**, identifies the page's subject entity (Product, Article, JobPosting, Event, Recipe, LocalBusiness, real-estate listing and more), and flattens it into one clean row per URL. If the first page you load contains structured data, the step is added for you automatically.

For products, columns include: name, price, availability, currency, brand, color, size, material, rating with review count, category, SKU, GTIN, MPN, images, and more. It works on any site with structured data — WooCommerce, Magento, custom stores, news sites, job boards.

*[Screenshot: The Data Table showing auto-extracted product columns from Automatic Extract]*

**Variants consolidate into one row per URL** — a product with 12 variants stays one row, with multi-value cells joined by commas. Known limits: it doesn't read JavaScript globals or RDFa, and list-style pages collapse to a single row.

#### Configuration highlights

| Setting | Default | Notes |
| --- | --- | --- |
| Concurrent tabs | 1 | Run several tabs in parallel with the Faster Extraction toggle for large batches |
| Request delay | 1000 ms | 0–5000 ms |
| Page timeout | 30 s | 5–120 s |
| Anti-bot randomization | off | When on: randomized delay variation plus extra random pauses between pages |
| Retries | 2 attempts per URL | Transient failures (timeouts, network errors) retry with backoff; permanent ones (404, blocked) don't. Failures are reported per URL and **never abort the batch** |

There is **no cap on URL count** — you can process as many pages as you like.

#### Recipes

Recipes are fully supported — URLs, steps, picked elements, and configuration all round-trip.

#### Related

- [Guide: Extract data from multiple pages](https://ultimatewebscraper.com/docs/guides/extract-data-from-multiple-pages) — The full list-to-details workflow, end to end.
- [Guide: Scrape products without selectors](https://ultimatewebscraper.com/docs/guides/scrape-product-data-without-selectors) — Put Automatic Extract to work on product catalogs.
- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Discover thousands of URLs to feed into this tool.


---

### Page Text Extractor

*Extract clean plain text plus title, author, date, and word count from a list of pages. Navigation, ads, and boilerplate are stripped automatically.*

**Source:** https://ultimatewebscraper.com/docs/extension/page-text-extractor

Turn webpages into clean, AI-ready text with metadata Free & uncapped locally Extension only Recipes supported

The Page Text Extractor pulls clean, readable text and metadata from a list of pages — one row per page. It's built for feeding content to AI: no nav menus, no ads, no cookie banners, just the article.

blog.example.com/poststrip boilerplate1,240 wordsa cluttered pageclean text + metadata

Nav, ads, and boilerplate stripped — just the article, plus metadata.

*[Screenshot: The Data Table with clean text content, title, author, and date columns]*

#### How it works

1. Add URLs by **manual paste, CSV upload, or Data Source** (a URL column from a previous extraction — for example, article links gathered with the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor)).
2. Confirm the list; the first URL loads as a preview.
3. Start the extraction. Pages are processed in the background with a live progress overlay, and rows stream into the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table).

#### What you get per page

| Column | Content |
| --- | --- |
| url | Source URL |
| title | Page title, upgraded from social meta tags or the main heading when those are richer |
| description | Meta description |
| content | The main content as plain text |
| word\_count | Word count of the content |
| author | Author, from meta tags and common author markup |
| publish\_date | Publication date, from article metadata and common date markup |

Content extraction targets the page's main content container and **always strips** scripts, styles, navigation, headers, footers, sidebars, ads, social-share widgets, and comments. Output is plain, whitespace-normalized text — not Markdown or HTML.

#### Use cases

- **LLM corpora** — build clean text datasets for retrieval, fine-tuning, or analysis without writing a scraper per site.
- **Content audits** — word counts, authors, and publish dates for every page of a blog in one table.
- **Research** — collect the readable text of dozens of sources into one searchable place.

#### Options

Sensible defaults: 1000 ms delay between requests, 30 s page timeout, wait-for-page-load on. The Faster Extraction toggle runs several tabs in parallel, and there's no cap on how many URLs you can process.

**Recipes are fully supported** — save a URL list and configuration, re-run it anytime.

#### Limitations

- Content that requires interaction to render isn't captured (standard page loads and JavaScript-rendered content are handled via load waits).
- LinkedIn URLs are blocked.
- There's no direct Markdown export — output is plain text, exported via the [Data Table](https://ultimatewebscraper.com/docs/extension/exporting-data).

#### Related

- [Guide: Extract clean text for AI](https://ultimatewebscraper.com/docs/guides/extract-clean-text-for-ai) — Build an LLM-ready text corpus step by step.
- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Discover every article URL on a site to feed this tool.
- [AI connections (MCP)](https://ultimatewebscraper.com/docs/ai) — Let AI agents query your cloud tables directly.


---

### Recipes

*Save any extraction setup as a named recipe, re-run it in one click, and share it as a JSON file. Free, unlimited, and supported in five of the seven tools.*

**Source:** https://ultimatewebscraper.com/docs/extension/recipes

Save any extraction setup as a re-runnable, shareable recipe

A **recipe** is a saved extraction configuration — URLs, selectors, steps, and timing — with a name. Once something works, save it and re-run it anytime instead of setting it up again.

123re-runa saved setupthe same result, again

Save a working setup once, re-run it in one click.

*[Screenshot: The Recipes manager listing saved recipes with Run buttons]*

#### Which tools support recipes

| Tool | Recipes |
| --- | --- |
| [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) | Yes |
| [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) | Yes |
| [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) | Yes |
| [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) | Yes |
| [Page Text Extractor](https://ultimatewebscraper.com/docs/extension/page-text-extractor) | Yes |
| [Shopify Extractor](https://ultimatewebscraper.com/docs/extension/shopify-extractor) | No — its live store-detection flow replaces recipes |
| [Image Downloader](https://ultimatewebscraper.com/docs/extension/image-downloader) | No — it's an interactive tool, not a saved automation |

#### Saving and running

- **Save:** each supported tool has a "Save as recipe" button in its header and in the completion overlay. Name it (a name is pre-suggested from the page title) and optionally describe it.
- **Run:** open the Recipes manager from the side panel home screen and hit Run — the tool opens prefilled and ready. List Extractor recipes also **auto-navigate your tab to the saved source URL**.
- **Manage:** rename, edit the underlying JSON (validated as you type), or delete.

#### Sharing recipes

Recipes **export and import as JSON files** — a single recipe or all of them as one bundle. That's the mechanism for sharing a working setup with a teammate or moving it to another machine.

**Imports never overwrite:** if an imported recipe collides with an existing one, it gets a fresh identity and an "(imported)" suffix instead of replacing anything.

#### Compatibility

Recipes are versioned. A recipe saved by a newer extension version, or containing actions that can't run, shows an **"Outdated" or incompatible badge** with the reason instead of a Run button — it stays editable and exportable, so nothing is lost.

#### Storage

Recipes are stored **locally in your browser** (no cloud sync); session-specific settings like concurrency are stripped on save, so a shared recipe runs cleanly for anyone.

> **🆓 Free and unlimited**
>
> Recipes are free and unlimited — save as many as you like.

#### Recipes vs. cloud scheduling

A recipe re-runs on demand, on your machine. To run an extraction **on a schedule without your computer**, send it to the [Cloud Platform](https://ultimatewebscraper.com/docs/cloud) instead.

#### Related

- [Guide: Schedule recurring extractions](https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions) — From a working local setup to a cloud schedule.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — The most common tool to save recipes from.
- [Cloud Platform](https://ultimatewebscraper.com/docs/cloud) — Scheduled runs, proxies, and a web dashboard.

[Exporting Data

Export your extracted tables as CSV, Excel, JSON, Google Sheets, or Shopify CSV — all from the Data Table's Export menu. Filter first to export just the rows you want.](https://ultimatewebscraper.com/docs/extension/exporting-data)


---

### Shopify Extractor

*Pull a Shopify store's whole catalog — one row per variant — and export a Shopify-import-ready CSV with 35 columns and safe defaults. Extraction is free.*

**Source:** https://ultimatewebscraper.com/docs/extension/shopify-extractor

Export a Shopify store's whole catalog as a re-importable CSV Extraction free Extension only No recipes

The Shopify Extractor pulls a Shopify store's entire product catalog — or just the collections you pick — into the Data Table, **one fully-populated row per variant**, and can export a CSV that re-imports cleanly into another Shopify store.

acme-store.comread catalogCSVa Shopify storeimport-ready CSV

A store's whole catalog, exported as an import-ready CSV.

*[Screenshot: The detected store card showing the store's name, product count, and collections]*

#### Automatic store detection

The extension recognizes Shopify stores automatically, including stores on custom domains. When you're on one, the side panel home screen shows a **"Shopify store detected" banner** recommending the tool (toggleable in Settings → Notifications). Only Shopify is detected — for products on other platforms, use the [Page Extractor's Automatic Extract](https://ultimatewebscraper.com/docs/extension/page-extractor#automatic-extract-structured-data-without-selectors) instead.

#### Running an extraction

##### Open the tool on a store page

It scans the store and shows a card with the store's name, currency, product count, and collections.

##### Choose the scope

**Whole catalogue**, or a multi-select list of **Collections**.

##### Optionally fetch full product details

A slower second pass that adds data the bulk feed lacks: inventory quantities, barcodes (UPC/EAN), clean descriptions, weight, and price ranges.

##### Start

Products stream into the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) with live product and variant counts. Stopping early keeps partial results. Switching tabs to a different store rescans automatically.

#### How it extracts

It reads the store's public product data and works on custom domains. It paces itself politely, backing off automatically when the store rate-limits, and keeps whatever it has if a store cuts it off. Products appearing in multiple selected collections are written once.

#### The Shopify-import CSV

*[Screenshot: The Export menu showing the Shopify CSV option]*

The export is a **35-column, Shopify-import-ready CSV**: handle, title, description HTML, vendor, type, tags, option names and values, variant SKU, price, compare-at price, barcode, weight, images with positions and alt text, SEO fields, status, and the rest of Shopify's import format.

Fields a storefront doesn't expose get **safe defaults** (status active, inventory policy deny, manual fulfillment) so the file imports without surprises. Notably, **variant inventory quantity is deliberately omitted** — only about half of stores expose it, and omitting the column prevents an import from zeroing out your inventory.

The Data Table also holds extra columns that aren't in the CSV (product and variant IDs, product URL, availability, currency, collection, timestamps), and merchant-only data (metafields, cost of goods, draft products) is not obtainable at all.

#### Edge cases

- **Password-protected (pre-launch) stores** are detected and refused with a friendly explanation.
- **Headless storefronts and WAF-blocked stores** are detected up front with a "can't extract" screen and guidance — the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) is the suggested fallback.

#### Recipes

- **Recipes: not supported** — the live store-detection flow replaces them.
- **Extraction is free.** The Shopify CSV export appears in the Data Table's Export menu on Shopify tables — see [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data).

#### Related

- [Guide: Export a Shopify store to CSV](https://ultimatewebscraper.com/docs/guides/export-shopify-store-to-csv) — Catalog to re-importable CSV, start to finish.
- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Automatic Extract covers products on non-Shopify platforms.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — All export formats, including the Shopify CSV.


---

### Sitemap Explorer

*Discover up to 50,000 URLs from a site's sitemaps, filter them in a searchable tree, and hand them straight to the Page Extractor. Free for everyone.*

**Source:** https://ultimatewebscraper.com/docs/extension/sitemap-explorer

Discover every URL a website publishes — up to 50,000 per site, free

The Sitemap Explorer discovers the URLs a site publishes in its sitemaps — up to **50,000** of them — so you can select exactly the pages you want and hand them to the [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor), or export them as a CSV.

example.comsitemap.xmlread sitemapsa websiteevery URL, grouped

Every URL a site publishes, grouped into a selectable tree.

*[Screenshot: The sitemap tree with URL groups expanded and checkboxes selected]*

#### How discovery works

The scan runs **entirely locally, inside your active tab**, using your own browser session — which helps get past bot protection, and means nothing leaves your machine.

1. It finds the site's sitemaps automatically, checking the common places sites publish them. You can also paste a known sitemap URL from the same site.
2. Sitemap **indexes are walked recursively** (up to 5 levels deep), and compressed `.gz` sitemaps are decompressed on the fly.
3. URLs are deduplicated, normalized, and organized into a **tree grouped by URL path** — so `/collections/shoes` pages become their own branch you can select in one click.

Switching to a different site in your browser automatically rescans the new site.

#### Selecting URLs

- **Tri-state checkboxes** let you select a whole group or subtree, then carve out branches you don't want.
- **Search** across the tree (multi-word), with matches auto-expanded; "Select all", "Select matches", and "Clear" shortcuts; a live count of selected URLs.
- **Stop early, keep results.** You can stop a scan at any point and work with what's been found so far.

#### Limits

A single scan collects up to **50,000 URLs** (results beyond that are marked "capped"). Sitemap indexes are followed several levels deep, so large multi-sitemap sites are covered in one pass.

#### What to do with the results

- **Continue** hands the selected URLs directly to the [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) to extract data from each page.
- **Export CSV** downloads the selected URLs as a one-column CSV — useful for any other workflow.

> **🆓 Free for everyone**
>
> Discovery, selection, and the URL CSV export are all free.

#### Related

- [Guide: Discover URLs with Sitemap Explorer](https://ultimatewebscraper.com/docs/guides/discover-urls-with-sitemap-explorer) — A worked example from sitemap to selected URL set.
- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Extract the same fields from every discovered URL.
- [Guide: Extract data from multiple pages](https://ultimatewebscraper.com/docs/guides/extract-data-from-multiple-pages) — Combine URL discovery with bulk extraction.


---

### Social Link Extractor

*Detect Twitter/X, Facebook, Instagram, YouTube, TikTok, GitHub, and Pinterest profile links across many pages — one column per platform.*

**Source:** https://ultimatewebscraper.com/docs/extension/social-link-extractor

Find social media profiles for any list of websites Free & uncapped locally Runs in cloud Recipes supported

The Social Link Extractor finds social media profile links across one or many pages. Give it a list of company websites and it returns each site's Twitter/X, Instagram, Facebook and other profiles — one column per platform.

acme.comfind profilesany websiteone column per platform

One row per site, one column per platform.

*[Screenshot: The results table with one column per social platform]*

It shares its engine with the [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor): same URL sources (manual input, CSV upload, Data Source), same deep scan of internal links, same configuration. The difference is that **social link detection is always on** here, and email extraction becomes the optional add-on.

#### Platforms detected

Seven built-in platforms, all enabled by default:

| Platform | What's matched |
| --- | --- |
| Twitter/X | Profile URLs on both domains |
| Facebook | Pages and profiles, including fb.com |
| Instagram | Profile URLs |
| YouTube | Channels in every URL style, including @handles |
| TikTok | @handles |
| GitHub | User and organization profiles |
| Pinterest | Profile URLs |

You can add **custom URL patterns** (your own regex) — each pattern gets its own output column. Handy for platforms not on the list, or for site-specific profile URLs.

#### How detection works

The tool scans **both link hrefs and URLs written in the page text** — so a profile mentioned in a footer paragraph is caught even if it isn't a clickable link. Results are deduplicated per platform.

Deep scanning (on by default) follows each page's internal links — depth 1–5, up to 50 links per page, same-domain by default — since social icons often live on contact and about pages. See the [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) page for the full crawling options.

> **LinkedIn is not supported**
>
> LinkedIn is blocked as a target in every tool.

#### Output

One row per seed URL, in input order: the URL, a combined Social Links column, and **one column per platform** (plus columns for any custom patterns). Toggle on the email add-on and you also get Emails and Email Count columns in the same run.

#### Recipes

Recipes are fully supported. All platforms, custom patterns, and deep scanning are included; the Faster Extraction toggle runs several tabs in parallel for large jobs.

#### Related

- [Guide: Find social media profiles](https://ultimatewebscraper.com/docs/guides/find-social-media-profiles) — Build a company-to-socials sheet step by step.
- [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) — The same engine, tuned for email discovery.
- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Clean up the results before exporting.


---

## Cloud Platform

### Cookies & Sessions: Scrape Behind Logins in the Cloud

*Clone your current browser session's cookies and localStorage into a cloud browser so logged-in extractions keep working when they run without you.*

**Source:** https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions

Some pages only show their data to logged-in users. Locally that's a non-issue — the extension runs in your own browser, with your session, so it sees exactly what you see. A cloud browser starts logged out. **Cookies & Storage cloning** fixes that.

#### How it works

When creating a task in the [Run in Cloud wizard](https://ultimatewebscraper.com/docs/cloud/running-tasks), expand the **Cookies & Storage** group. Enabling it clones your **current browser session's cookies and localStorage** into the cloud browser, so the cloud run visits the target site as your logged-in session.

*[Screenshot: The Cookies & Storage toggle in the Run in Cloud wizard]*

That makes logged-in extractions work in the cloud: member directories, dashboards, gated listings — anything your account can see, the cloud browser can now extract, including on a [schedule](https://ultimatewebscraper.com/docs/cloud/scheduling) while you're away.

> **🔒 Only when you use it**
>
> Session cloning only reads the current site's cookies and storage, and only when you enable it for a task — nothing is accessed at install time or in the background. If you never clone a session, nothing is ever read.

#### Local vs. cloud with logins

|  | Extension (local) | Cloud with session cloning |
| --- | --- | --- |
| How it authenticates | Uses your live browser session natively | Copies your session's cookies and localStorage at task creation |
| Setup | None — just be logged in | Enable Cookies & Storage in the wizard |
| Stays valid | As long as you're logged in | Until the cloned session expires on the site's side |

If a site logs sessions out quickly, a long-running schedule may eventually hit expired cookies — recreate the task while logged in to refresh the cloned session.

> **⚠️ Use your own accounts, respect site terms**
>
> Session cloning is meant for extracting data that **your own account** legitimately has access to. Check the target site's terms of service before scraping logged-in areas, never clone sessions for accounts that aren't yours, and be conservative with scheduling frequency on authenticated sites.

#### When you don't need this

Leave Cookies & Storage off (the default) for public pages — most extractions don't need a session, and the [proxy and unblocking settings](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking) cover ordinary anti-bot friction.

#### Related

- [Guide: scrape behind logins](https://ultimatewebscraper.com/docs/guides/scrape-behind-logins) — A step-by-step walkthrough for authenticated extractions.
- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — Where the Cookies & Storage group lives in the wizard.
- [Local vs. cloud](https://ultimatewebscraper.com/docs/getting-started/local-vs-cloud) — How local and cloud execution differ.


---

### How Cloud Credits Work

*Understand cloud credits — 1 credit per page extracted — how they're granted and topped up, and why local extension use is always free and unlimited.*

**Source:** https://ultimatewebscraper.com/docs/cloud/credits-and-plans

The Cloud Platform runs in cloud browsers and is metered in **credits**. The model is simple, and the most important rule comes first: **the extension's local tools never consume credits and are always unlimited**, whether or not you have a cloud plan.

#### How credits work

- **1 cloud credit = 1 page extracted in the cloud.** A cloud run over 500 URLs costs about 500 credits.
- **AI features also consume credits.** The [Page Unblocker](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking) uses credits on top of the per-page cost when it handles a challenge.
- **Credits are granted up front** with your plan, and can be **topped up** if you run out before renewal.

Because [scheduled tasks](https://ultimatewebscraper.com/docs/cloud/scheduling) re-extract their pages on every run, schedule frequency is the main lever on credit consumption — a task that runs more often, over more pages, uses more credits.

#### Plans and prices

Cloud plans differ by credit allowance and features. **Current plans, prices, and allowances live on the [pricing page](https://ultimatewebscraper.com/pricing)** — they aren't listed here so you always see live numbers. Any paid cloud plan also unlocks the extension's full feature set, so one subscription covers both the extension and the cloud.

#### Local stays free

Without a cloud plan you can still use every local extension tool with no page or row caps — credits only apply to cloud runs. Creating a cloud task without an active plan shows an upgrade prompt.

> **💡 Budgeting rule of thumb**
>
> Estimate credits as pages per run × runs per period. Test locally first (free), check the URL count, then pick a schedule your allowance supports comfortably.

#### Related

- [Pricing](https://ultimatewebscraper.com/pricing) — Current plan prices and credit allowances.
- [Scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling) — How run frequency drives credit consumption.
- [Local vs. cloud](https://ultimatewebscraper.com/docs/getting-started/local-vs-cloud) — What's free locally vs. metered in the cloud.

[The Cloud Dashboard: Tasks, Data & Workspaces

Manage cloud automations, run history, data tables, exports, workspaces, and billing from one web dashboard — everything your cloud runs produce.](https://ultimatewebscraper.com/docs/cloud/dashboard)


---

### The Cloud Dashboard: Tasks, Data & Workspaces

*Manage cloud automations, run history, data tables, exports, workspaces, and billing from one web dashboard — everything your cloud runs produce.*

**Source:** https://ultimatewebscraper.com/docs/cloud/dashboard

The [cloud dashboard](https://ultimatewebscraper.com/cloud) is the web home of the Cloud Platform. Every cloud task you create, every run it performs, and every table it produces lives here — open it from any browser, no extension required.

*[Screenshot: A cloud data table open in the dashboard with rows and export options]*

You can also jump to it from the extension: the **CLOUD** button in the side panel's action bar and the **Dashboard** button in the cloud section both open it in a new tab.

#### Automations and tasks

The dashboard lists your cloud automations with their **run history**. Each run has a **timeline** showing how it progressed — what was extracted, what failed, and why. This is where you check on [scheduled tasks](https://ultimatewebscraper.com/docs/cloud/scheduling) and confirm that recurring runs are producing what you expect.

#### Cloud data tables

Every run's results are stored as a data table. The dashboard's table view is built for large results:

- **Virtualized viewing** — big tables stay fast to scroll and browse.
- **Editing** — fix cells and adjust columns directly in the browser.
- **Filtering** — narrow rows down before exporting.
- **Exports** — CSV, Excel, JSON, Clipboard, and Google Sheets.
- **Batch image download** — grab all images referenced in a table at once.

Cloud tables are separate from the extension's local Data Table: local results stay on your machine, cloud results live here. Cloud tables are also what [AI agents can reach over MCP](https://ultimatewebscraper.com/docs/ai).

#### Profile and workspaces

Cloud accounts support **multiple workspaces**, each with its own automations, tables, and credit balance. A **shared workspace** lets teammates work from the same automations and data. You switch workspaces in the dashboard (and in the extension's settings).

#### Billing and subscription

Your plan, credit balance, and subscription management live in the dashboard's billing area. This is also where plan changes and top-ups happen — see [Credits & plans](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) for how the model works, and [/pricing](https://ultimatewebscraper.com/pricing) for current prices.

#### Integrations

The dashboard's integrations area covers the services your tasks export to, such as Google Sheets. Per-task integration settings are chosen when [creating the task](https://ultimatewebscraper.com/docs/cloud/running-tasks); see [Integrations](https://ultimatewebscraper.com/docs/cloud/integrations) for the export modes.

#### Related

- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — Create the tasks whose runs and tables appear here.
- [Cloud credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — How cloud credits are metered and topped up.
- [AI connections](https://ultimatewebscraper.com/docs/ai) — Query and clean cloud tables with an AI agent.


---

### Cloud Platform Overview: Scraping in Cloud Browsers

*Run and schedule web scraping in cloud browsers with built-in proxies, anti-blocking, and a results dashboard — no computer needed. Start here.*

**Source:** https://ultimatewebscraper.com/docs/cloud

The Cloud Platform runs your extractions in **cloud browsers** — so your scrapers keep working after you close your laptop, on a recurring schedule if you want, with proxies and anti-blocking built in. Results land in a web [dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) instead of your local browser.

*[Screenshot: The cloud dashboard overview with automations and recent runs]*

#### What the cloud gives you

- **Runs without your computer.** Tasks execute on cloud infrastructure; you check results whenever you like.
- **[Scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling)** from every 10 minutes to monthly.
- **[Proxies and unblocking](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking)** — ISP or residential proxies with location choice, plus automatic handling of supported challenges.
- **[Integrations](https://ultimatewebscraper.com/docs/cloud/integrations)** — push results to Google Sheets or a webhook on every run.
- **A web dashboard** at [/cloud](https://ultimatewebscraper.com/cloud) with run history, data tables, exports, and workspaces.

Cloud runs require a paid plan and consume [credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — 1 credit per page extracted. Local extraction in the extension stays free and unlimited.

#### What can run in the cloud today

| Tool | Cloud support |
| --- | --- |
| [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) | Yes |
| [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — including Google Maps mode | Yes |
| [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) | Yes |
| [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) | Yes |
| Image Downloader | Not yet |
| Shopify Extractor | Not yet |

More cloud tools are planned.

#### The recommended flow

**Build and test locally.** Configure the extraction in the extension and run it on your machine — it's free, instant, and easy to iterate on.

**Send it to the cloud.** Open **Run in Cloud** in the side panel and pick that working automation. See [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks).

**Schedule, integrate, monitor.** Add a schedule, proxies, or a Google Sheets export, then follow results in the dashboard.

There is no free-form "paste a URL" box in the cloud wizard — you always start from a configuration you've already run locally, which is what makes cloud runs reliable.

#### Explore the section

- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — The Run in Cloud wizard: pick an automation, configure, and launch.
- [Scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling) — 11 presets, from every 10 minutes to monthly.
- [Integrations](https://ultimatewebscraper.com/docs/cloud/integrations) — Google Sheets and webhook exports, configured per task.
- [Proxies & unblocking](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking) — ISP and residential proxies, plus the Page Unblocker.
- [Cookies & sessions](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) — Clone your session so logged-in extractions work in the cloud.
- [The dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) — Tasks, run history, data tables, workspaces, and billing.
- [Cloud credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — How cloud credits are metered and topped up.

#### Related

- [Local vs. cloud](https://ultimatewebscraper.com/docs/getting-started/local-vs-cloud) — How the extension and the Cloud Platform fit together.
- [Schedule recurring extractions](https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions) — A step-by-step guide to your first scheduled cloud task.

[Running Cloud Tasks: The Run in Cloud Wizard

Send a tested local extraction to a cloud browser with the Run in Cloud wizard — pick an automation, configure proxies and integrations, then run.](https://ultimatewebscraper.com/docs/cloud/running-tasks)


---

### Cloud Integrations: Google Sheets & Webhooks

*Send cloud extraction results straight to Google Sheets or a webhook, export from the dashboard in any format, or query your data with AI agents.*

**Source:** https://ultimatewebscraper.com/docs/cloud/integrations

Cloud tasks can push their results out automatically on every run. Both integrations are configured per task in the [Run in Cloud wizard](https://ultimatewebscraper.com/docs/cloud/running-tasks), under the **Integrations** group, and both are **off by default**.

*[Screenshot: The Integrations config with Google Sheets and Webhook toggles]*

#### Google Sheets export

Sends each run's results to a Google spreadsheet. Three modes control what happens on recurring runs:

| Mode | Behavior |
| --- | --- |
| Create new | Each run creates a fresh sheet |
| Replace | Each run overwrites the sheet's contents |
| Append | Each run adds rows to the existing sheet |

**Append** pairs naturally with [scheduled tasks](https://ultimatewebscraper.com/docs/cloud/scheduling) — a price monitor that appends daily builds a history you can chart directly in Sheets. **Replace** suits "always show me the current state" jobs like a refreshed lead list.

#### Webhook export

Sends each run's results to a URL you provide, so your own tools can react the moment a run finishes — update a database, trigger a Zap, post to Slack, whatever sits behind your endpoint. Configure it in the same Integrations group when creating the task.

#### Where results always live

Integrations are additive — with or without them, every run's results are stored as data tables in the [cloud dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard). From there you can view, edit, and filter tables, and export to:

- CSV
- Excel
- JSON
- Clipboard
- Google Sheets

So you don't need to configure an integration up front: you can always pull data out of the dashboard later. Integrations matter when you want data delivered **automatically on every scheduled run**.

#### Third option: AI agents

Your cloud tables are also reachable by AI agents. Connect Claude or another MCP-capable assistant to your workspace and it can query, analyze, clean, and export your cloud data in plain language — see [AI connections](https://ultimatewebscraper.com/docs/ai).

#### Choosing a path

| You want to… | Use |
| --- | --- |
| Look at results, clean them, export occasionally | The [dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) |
| Keep a spreadsheet continuously up to date | Google Sheets export |
| Feed results into your own system on every run | Webhook export |
| Ask questions about the data conversationally | [AI agents / MCP](https://ultimatewebscraper.com/docs/ai) |

#### Related

- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — Where the Integrations group lives in the wizard.
- [The dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) — Data tables, editing, and manual exports.
- [AI connections](https://ultimatewebscraper.com/docs/ai) — Let AI agents query and clean your cloud data over MCP.


---

### Proxies & Page Unblocker for Cloud Scraping

*Choose ISP or residential proxies with country and city targeting, and let the Page Unblocker solve Cloudflare Turnstile challenges automatically.*

**Source:** https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking

Cloud browsers come with two anti-blocking features you configure per task in the [Run in Cloud wizard](https://ultimatewebscraper.com/docs/cloud/running-tasks): **Browser Location** (which proxy the cloud browser uses) and the **Page Unblocker** (what happens when a page throws a challenge).

*[Screenshot: The Browser Location settings with proxy type and country selection]*

#### Browser Location (proxies)

Every cloud run goes through a proxy. You choose the type and where it appears to be from:

- **Proxy type:** ISP or Residential.
- **Location:** pick a country, and optionally a city.
- **Default:** ISP proxy with a random location — no configuration needed for most sites.

##### ISP vs. residential — when to use which

|  | ISP | Residential |
| --- | --- | --- |
| What it is | IPs registered to internet service providers, served from stable infrastructure | IPs from real consumer connections |
| Best for | Most sites; fast, reliable default | Sites that aggressively block datacenter-adjacent traffic |
| Rule of thumb | Start here | Switch if ISP runs get blocked |

Location targeting matters when a site serves different content per region — prices, availability, listings, or language. Set the country (and city, if offered) to match the market you want to see.

#### Page Unblocker

The Page Unblocker handles challenge pages and blocking overlays during a cloud run:

- **Cloudflare Turnstile challenges are solved automatically** — the run continues and the page is extracted.
- **Other captcha types are detected but not solved.** DataDome, reCAPTCHA, and hCaptcha are recognized, but those pages fail with a clear error rather than hanging.
- **It consumes [credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans)** — like other AI features, unblocking uses your credit balance on top of the 1-credit-per-page extraction cost.

> **Failed pages don't kill the run**
>
> A page that hits an unsolvable captcha errors out individually; the rest of the task keeps running. Check the run timeline in the [dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) to see which pages failed and why.

#### A practical escalation path

**Run with defaults** — ISP proxy, random location. This works for most sites.

**Getting blocked?** Enable the Page Unblocker if the blocks are Cloudflare challenges.

**Still blocked?** Switch Browser Location to a Residential proxy, and pick a country close to the site's audience.

Note that locally, the extension has no proxy or captcha handling at all — it browses as you. Proxies and unblocking are cloud-only capabilities.

#### Related

- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — Where Browser Location and Page Unblocker live in the wizard.
- [Cloud credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — How extraction and unblocking consume credits.
- [Cookies & sessions](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) — Another way past barriers: bring your logged-in session.


---

### Running Cloud Tasks: The Run in Cloud Wizard

*Send a tested local extraction to a cloud browser with the Run in Cloud wizard — pick an automation, configure proxies and integrations, then run.*

**Source:** https://ultimatewebscraper.com/docs/cloud/running-tasks

Cloud tasks are created from the extension's side panel with a two-step **Run in Cloud** wizard. You hand a working local extraction to a cloud browser, tune how it should run, and launch it.

*[Screenshot: The Run in Cloud wizard step 2 with schedule and config categories visible]*

Open the wizard from the **Run in Cloud** card on the side panel home screen, or from the cloud button inside a supported tool.

#### Step 1 — Select an automation

You pick a **previously-run local automation** from your history. The list shows your past runs, filtered to the [cloud-supported task types](https://ultimatewebscraper.com/docs/cloud): List Extractor, Page Extractor (including Google Maps mode), Email Extractor, and Social Link Extractor.

*[Screenshot: Step 1 list of local automations to pick from]*

> **There is no URL box**
>
> The wizard intentionally has no free-form URL input. You configure and test the extraction locally first — where iteration is free and instant — then send the proven setup to the cloud. If you haven't run anything yet, two demo automations are available so you can try the flow.

#### Step 2 — Configure

The configure screen shows a preview card for the selected automation, the [schedule picker](https://ultimatewebscraper.com/docs/cloud/scheduling), and expandable configuration groups:

| Group | What it controls | Default |
| --- | --- | --- |
| Automation | The extraction itself: URLs, selectors, pagination | As tested locally |
| Page Unblocker | Captcha and block handling ([details](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking)) | — |
| Integrations | [Google Sheets and webhook exports](https://ultimatewebscraper.com/docs/cloud/integrations) | Off |
| Browser Location | [ISP or residential proxy](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking), country/city | ISP, random location |
| User Agent & Viewport | Device presets | Your current browser |
| Data Cleanup | Remove empty, duplicate, sparse, and repeating rows and columns | On |
| Cookies & Storage | [Clone your session](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) into the cloud browser | Off |

The defaults are sensible: most tasks only need a schedule, and perhaps a proxy location or a Sheets export.

#### Launch

Submit with **Run Now** (one-off) or **Run & Schedule** (recurring). Either way, **the task always runs immediately on creation** — a scheduled task doesn't wait for its first slot, so you can verify it works right away.

The success screen links to the [dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard), where you'll see the run's timeline and its results table as rows come in. Each page the cloud browser extracts consumes one [credit](https://ultimatewebscraper.com/docs/cloud/credits-and-plans).

#### Related

- [Scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling) — Turn a one-off task into a recurring one with 11 presets.
- [Proxies & unblocking](https://ultimatewebscraper.com/docs/cloud/proxies-and-unblocking) — Pick the right proxy type and handle blocked pages.
- [The dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard) — Where your cloud runs and results live.


---

### Cloud Scheduling: Recurring Web Scraping

*Schedule cloud extractions from every 10 minutes to monthly with 11 built-in presets. Ideal for price monitoring, lead lists, and content tracking.*

**Source:** https://ultimatewebscraper.com/docs/cloud/scheduling

Every cloud task can run on a recurring schedule. You pick a preset when creating the task in the [Run in Cloud wizard](https://ultimatewebscraper.com/docs/cloud/running-tasks) — choose **Run & Schedule** instead of **Run Now** — and the cloud re-runs the extraction for you from then on.

*[Screenshot: The schedule picker showing the presets from every 10 minutes to monthly]*

#### The 11 presets

| Preset | Behavior |
| --- | --- |
| Off | Runs once, no recurrence |
| Every 10 minutes | High-frequency monitoring |
| Every 30 minutes |  |
| Hourly |  |
| Every 6 hours |  |
| Every 12 hours |  |
| Daily | Runs at midnight UTC |
| Every 2 days | Runs at midnight UTC |
| Every 3 days | Runs at midnight UTC |
| Weekly | Runs Sundays at midnight UTC |
| Monthly | Runs on the 1st at midnight UTC |

Two things to know:

- **Day-level schedules run at midnight UTC.** Daily, multi-day, weekly, and monthly presets all fire at 00:00 UTC; a specific time of day isn't available.
- **There is no custom cron field in the UI.** If none of the presets fit exactly, choose the nearest one.

Regardless of the schedule, the task also [runs immediately when you create it](https://ultimatewebscraper.com/docs/cloud/running-tasks), so you can confirm it works before the first scheduled run.

#### What scheduling costs

Each scheduled run extracts pages, and each page consumes one [cloud credit](https://ultimatewebscraper.com/docs/cloud/credits-and-plans). A frequent schedule on a large URL list adds up — pick the slowest interval that still fits your use case.

#### Common use cases

- **Price monitoring.** Re-extract product pages daily or hourly and watch prices change over time in the [dashboard](https://ultimatewebscraper.com/docs/cloud/dashboard), or push each run to Google Sheets.
- **Lead list refresh.** Re-run an Email Extractor or Google Maps task weekly so your list stays current without manual work.
- **Content tracking.** Check a news section, job board, or listing site every few hours and let a [webhook](https://ultimatewebscraper.com/docs/cloud/integrations) notify your own tooling.

#### Managing schedules

Scheduled tasks, their run history, and per-run timelines all live in the [cloud dashboard](https://ultimatewebscraper.com/cloud). That's where you review what each run produced and manage the automation going forward.

#### Related

- [Guide: schedule recurring extractions](https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions) — A full walkthrough, from local test to recurring cloud task.
- [Running cloud tasks](https://ultimatewebscraper.com/docs/cloud/running-tasks) — How the Run in Cloud wizard works, step by step.
- [Cloud credits](https://ultimatewebscraper.com/docs/cloud/credits-and-plans) — How recurring runs consume credits.


---

## AI Agents & MCP

### AI-Started Extractions

*Ask Claude or any MCP agent to extract product data, emails, social links, phone numbers, or Google Maps places — with credit estimates before anything runs.*

**Source:** https://ultimatewebscraper.com/docs/ai/agent-extractions

With a full-access connection, you can ask your AI assistant to **start a new extraction** for you. These are zero-configuration extractions — no element picking, no selectors — the same technology behind the extension's automatic extraction modes, running in cloud browsers.

#### What agents can extract

| Type | What you get |
| --- | --- |
| **Product pages** | Structured product data (name, price, availability, brand, ratings, images…) from any site that publishes structured data — the catalogue use case |
| **Emails** | Email addresses found across the given pages |
| **Social links** | Social media profile links (7 platforms) |
| **Phone numbers** | Phone numbers found on the given pages |
| **Google Maps** | Place name, rating, address, phone, website, hours from Maps listings |

#### Where the URLs come from

- **Straight from the chat** — paste up to 500 URLs into the conversation.
- **From an existing table** — point the agent at a link column of a table you've already scraped. This is the path for big jobs: thousands of URLs, no pasting. It's also how chaining works: scrape a list once, then have the agent visit every link in it.

#### Credit safety: estimate first, run on confirmation

An agent-started extraction **never begins silently**. The first request returns a credit estimate — *"1,240 URLs ≈ 1,240 credits, you have 8,400"* — so the agent can check with you before committing. Extractions cost about **1 credit per page**, the same as any cloud run, and runs are refused when your balance is empty. Credits can never go negative.

#### Scheduling

Agent-created extractions can carry a recurring schedule, like any other cloud task — so "*check these 200 product pages every morning*" is a single instruction.

#### Guardrails

The same rules as the rest of the product apply: LinkedIn is refused, and page extractions stay on a single domain. Runs are asynchronous — the agent gets a run ID immediately and checks progress rather than blocking your conversation.

#### Example conversation

> **You:** Take the "Company URL" column from my YC directory table and find contact emails for each company.
>
> **Agent:** That's 486 URLs — an email extraction will use about 486 credits (you have 9,200). Run it?
>
> **You:** Yes.
>
> **Agent:** Started. I'll check progress… Done — 1,832 emails across 431 companies, saved as a new table. Want it in Google Sheets?


---

### What AI Agents Can Do

*Connected AI agents can query scraped tables of any size, clean columns, export data, operate automations, and answer product questions from the docs.*

**Source:** https://ultimatewebscraper.com/docs/ai/capabilities

Once connected over MCP, an AI assistant gets a focused set of capabilities over your cloud workspace, grouped into six areas.

#### Understand your workspace

The agent can read your plan, credit balance, and its own access level — so it can answer "how many credits do I have left?" and warn you before starting anything expensive.

#### Work with your data

- **Browse tables** — list all result tables, grouped by the automation that produced them.
- **Inspect** — read a table's schema, row count, and a small sample.
- **Query without limits** — filter, aggregate, group, and sort tables **server-side**. The full table is never loaded into the AI's context, so a 100,000-row table is as easy to analyze as a 100-row one.
- **Export** — generate CSV, JSON, or Excel downloads, or send a table straight to Google Sheets.

> **Big-table safety**
>
> Large tables are never streamed into the conversation. The agent sees the schema plus a sample, then asks the server precise questions. Oversized responses are refused with a hint to narrow the query.

#### Clean your data

With a full-access token, agents can tidy tables the way you would by hand:

- Rename columns or change their type
- Delete irrelevant columns
- Merge 2–5 columns into one (street + city + zip → Address)

#### Operate your automations

- List automations and their run history (available to every token, including read-only)
- Check a run's live progress
- Start or stop a run (full access)

This is what makes "re-run my competitor price scrape and put results in Sheets" a one-sentence job.

#### Start new extractions

Agents can create **zero-configuration extractions** — product data, emails, social links, phone numbers, and Google Maps places — from a list of URLs or from a column of an existing table. This is powerful enough to get [its own page](https://ultimatewebscraper.com/docs/ai/agent-extractions).

#### Get product help

The agent has this documentation at its fingertips: it can search and read every docs page — the extension tools, the Cloud Platform, credits, guides — and answer questions from what the docs actually say, with a link to the right page.

Ask things like "how do I schedule a daily scrape?", "can the List Extractor handle infinite scroll?", or "what happens when I run out of credits?" and you get the concrete steps instead of a guess. Available to every token, including read-only.

#### Access levels

|  | Read-only token | Full-access token |
| --- | --- | --- |
| Read workspace info, tables, runs | ✔ | ✔ |
| Query & export tables | ✔ | ✔ |
| Search & read the product docs | ✔ | ✔ |
| Clean tables (rename/delete/merge) | — | ✔ |
| Start & stop runs | — | ✔ |
| Create new extractions | — | ✔ |

Choose read-only when you want an analyst; choose full access when you want an operator. Details in [Security](https://ultimatewebscraper.com/docs/ai/security).


---

### AI Agents & MCP Overview

*Connect Claude and other AI assistants to your Ultimate Web Scraper cloud workspace via MCP. Analyze, clean, and launch extractions in plain language.*

**Source:** https://ultimatewebscraper.com/docs/ai

> **Early access**
>
> AI connections are **rolling out now**. The MCP server is live for cloud workspaces, with broader public availability on the way.

**Ultimate Web Scraper speaks MCP** (Model Context Protocol) — the open standard that lets AI assistants like Claude, Claude Code, and other MCP-compatible clients connect to your tools. Once connected, your AI assistant can work with your scraped data conversationally:

- *"Which of the 2,000 companies I scraped yesterday don't have an email address?"*
- *"Clean up this table — drop the junk columns and merge street, city, and zip into one address."*
- *"Run my price-monitoring automation again and tell me when it's done."*
- *"Take the product links from that table and extract full product data for each."*

#### How it works

Your AI assistant connects to your **cloud workspace** with a personal access token you create in the dashboard. From then on, the agent can list your result tables, query them, clean them, check on runs, start new extractions, and answer questions about how the product works straight from these docs — all through natural conversation, and all scoped to your workspace.

- [What agents can do](https://ultimatewebscraper.com/docs/ai/capabilities) — Query tables of any size, clean columns, export, operate automations, and get product help.
- [AI-started extractions](https://ultimatewebscraper.com/docs/ai/agent-extractions) — Ask your assistant to extract product data, emails, social links, phones, or Google Maps places.
- [Security model](https://ultimatewebscraper.com/docs/ai/security) — Workspace-scoped tokens, read-only mode, revocation, and credit safety.

#### Cloud-only, by design

AI agents connect to your **cloud** workspace only. Data extracted locally with the Chrome extension stays on your machine — it is never exposed to agents unless you run the extraction in the cloud. This is the same privacy boundary as the rest of the product: local means local.

Selector-based scrapers (like List Extractor configurations) are still authored visually in the extension. Agents can **run** them in the cloud and use their results — building them stays point-and-click.

#### Which AI apps work?

Any MCP-compatible client, including:

- **Claude** (web and desktop) via custom connectors
- **Claude Code** in the terminal
- **Cursor** and other MCP-capable editors and agents

#### Requirements

- A cloud workspace on a **paid plan** (token creation is part of paid plans — see [Credits & plans](https://ultimatewebscraper.com/docs/cloud/credits-and-plans))
- Reading, querying, cleaning, and exporting data consume **no credits**; agent-started extractions consume credits like any other cloud run

[What AI Agents Can Do

Connected AI agents can query scraped tables of any size, clean columns, export data, operate automations, and answer product questions from the docs.](https://ultimatewebscraper.com/docs/ai/capabilities)


---

### AI Connection Security

*How Ultimate Web Scraper keeps AI agent access safe — workspace-scoped tokens shown once, read-only mode, instant revocation, rate limits, and credit protection.*

**Source:** https://ultimatewebscraper.com/docs/ai/security

Giving an AI agent access to your data deserves a clear security model. Here's ours.

#### Tokens

- **Created by you, in the dashboard.** Each connection uses a personal access token you generate and name.
- **Shown once.** The token value is displayed a single time at creation; only a hash is stored. If you lose it, you revoke it and make a new one.
- **Workspace-scoped.** A token can only ever reach the workspace it was created in — never another workspace, and never anyone else's data.
- **Capped and revocable.** You can keep several active tokens and revoke any of them instantly from the dashboard. Tokens stop working immediately if the user who created them leaves the workspace.
- **Rate-limited** against runaway clients.

#### Access levels

Every token is created with one of two levels:

- **Read-only** — the agent can analyze tables, query data, and check run status. It cannot change anything or spend anything.
- **Full access** — adds cleanup operations, starting/stopping runs, and creating new extractions.

Start read-only; upgrade to full access when you trust the workflow.

#### Credit protection

- Reading, querying, cleaning, and exporting data consume **no credits**.
- Anything that would spend credits (starting an extraction) returns a **cost estimate first** so the agent can confirm with you, and runs are refused when the balance is empty — balances can't go negative.

#### Privacy boundaries

- **Local data stays local.** Agents can only see cloud data. Tables in the Chrome extension's local storage are never exposed.
- **No cross-workspace access.** Team members' other workspaces are invisible to a token.
- **Large-response protection.** The server refuses to dump oversized data into a conversation and asks the agent to narrow its query instead.

#### Good practices

1. Create one token per AI client, named after it ("Claude Desktop", "Cursor — laptop"), so revocation is surgical.
2. Prefer read-only tokens for analysis-only workflows.
3. Revoke tokens you no longer use — creating a fresh one takes seconds.

[AI-Started Extractions

Ask Claude or any MCP agent to extract product data, emails, social links, phone numbers, or Google Maps places — with credit estimates before anything runs.](https://ultimatewebscraper.com/docs/ai/agent-extractions)


---

## Guides

### How to Bulk Download Images from Any Webpage

*Scan a page with the Image Downloader, filter by size and type, and download everything into one folder — no per-file dialogs, lazy-loading handled.*

**Source:** https://ultimatewebscraper.com/docs/guides/bulk-download-images

The Image Downloader finds every image on a page — including CSS backgrounds and lazy-loaded ones — lets you filter the haul, and downloads it all in one go.

##### Open the tool — scanning is automatic

Open **Image Downloader** from the side panel on the page you want. It immediately scans the current tab and shows everything it found: regular images (with lazy-load attributes and srcset handled — the largest candidate wins), CSS background images, and pseudo-element images. Results are grouped by size category, largest first; tiny icons are excluded automatically.

*[Screenshot: The Image Downloader right after an automatic scan of a gallery page, image thumbnails grouped by size category with the largest group expanded at the top]*

##### Enable auto-scroll for lazy-loading pages

If the page loads images as you scroll (most galleries and product grids do), turn on **Auto-scroll** and re-scan. The tool steps down the page, nudging lazy images to load and collecting continuously — it even survives virtualized lists that unload images as they scroll away — then restores your scroll position.

##### Filter down to what you want

Use the filters: min/max width and height, file extensions, image type, size categories, alt-text search. Getting rid of trackers, spacers, and thumbnails takes a couple of clicks.

*[Screenshot: The Image Downloader's filter panel with a minimum width set and a file-extension filter applied, the results grid narrowed to large photos]*

##### Download

Click **Download all** (or download a single group or image). Files download individually — no ZIP — into a timestamped folder like `images_2026-07-11_14-30-00` in your Downloads directory, with **no per-file save dialogs**. Downloads run a few at a time and can be cancelled.

#### How files are named

Each file gets the best available name, in order: the original filename (optional toggle), then the image's alt text (sanitized), then a generated `image_WIDTHxHEIGHT_N` name. Collisions are deduplicated with numeric suffixes, so nothing gets overwritten.

#### More modes: many pages, or direct URLs

Two additional source modes handle bigger jobs:

- **Scan Pages** — batch-scan a list of page URLs in background tabs (up to 5 in parallel). Set pre-scan filters first — size categories, file types, or quick presets like "Large only" and "Photos only" — so only wanted images are collected. Choose how downloads are organized: all together, a folder per page, or the page name as a filename prefix.
- **Import URLs** — paste, upload, or pull from a previous extraction a list of **direct image links**, downloaded straight to disk. Perfect follow-up to a List Extractor run that captured an image column.

Single-page scanning, all filters, auto-scroll, and downloads all run right in your browser.

> **⚠️ Limitations**
>
> Inline `data:` URI images can't be captured, and browser-internal pages can't be scanned. Imported URLs blocked by CORS land in an "Unknown" size group but remain downloadable.

#### Related

- [Image Downloader](https://ultimatewebscraper.com/docs/extension/image-downloader) — Full reference: scan modes, filters, naming, auto-scroll settings.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Capture image URLs from a list to feed Import URLs mode.
- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Bulk-download images straight from a results table.


---

### Discover Every URL a Website Publishes

*Use the free Sitemap Explorer to map a site's sitemap into a searchable tree, select the branch you need, and feed it to the Page Extractor or a CSV.*

**Source:** https://ultimatewebscraper.com/docs/guides/discover-urls-with-sitemap-explorer

Before you can scrape "all the product pages" or "every blog post", you need their URLs. The Sitemap Explorer reads a site's sitemaps — the URL lists sites publish for search engines — and turns them into a selectable tree. It's free, and it runs entirely locally.

##### Open it on the target site

Navigate to the site, then open **Sitemap Explorer** from the side panel (it's also available as a URL source inside the Page Extractor). Switching browser tabs to a different site automatically rescans.

##### Let discovery run

The tool finds sitemaps automatically, checking the common places sites publish them. Sitemap indexes are followed and compressed sitemaps are handled for you. If you already know a sitemap URL on this site, you can paste it directly. You can stop a long scan early and keep what's been found.

##### Browse the URL tree

Discovered URLs are deduplicated and grouped by path into a hierarchical tree — `/products/...`, `/blogs/...`, `/pages/...` each become their own branch with counts. Use the **tri-state checkboxes** to select a whole branch, or select a parent and carve out sub-branches you don't want. The multi-word **search** filters and auto-expands matches, with "Select matches" to grab everything a query hits.

*[Screenshot: The Sitemap Explorer's hierarchical URL tree with per-branch counts and tri-state checkboxes, the /products branch fully selected]*

##### Select the branch you need

For a store, that's typically the products branch; for a content site, the blog branch. The live counter shows exactly how many URLs you've selected.

##### Hand the URLs off

Two exits:

- **Continue** sends the selected URLs straight into the [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — ideal with [Automatic Extract](https://ultimatewebscraper.com/docs/guides/scrape-product-data-without-selectors) for product data.
- **Export CSV** downloads the selection as a one-column URL CSV, usable in any tool that accepts CSV upload (Page Text Extractor, Email Extractor, or anything outside the extension).

*[Screenshot: The Sitemap Explorer's footer with the live selected-URL counter and the Continue and Export CSV buttons]*

#### Scale and privacy

The Explorer collects up to **50,000 URLs** per scan (results beyond that are marked as capped). Everything is **free**: discovery, selection, and the URL CSV export.

It also runs **locally, inside the active tab, with your own session** — nothing leaves your machine, and because requests carry your cookies, sitemaps behind mild bot protection often load where an external crawler would be blocked.

> **💡 No sitemap?**
>
> Not every site publishes one. If discovery comes up empty, scrape a category or listing page with the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) to collect URLs instead — see [Extract data from multiple pages](https://ultimatewebscraper.com/docs/guides/extract-data-from-multiple-pages).

#### Related

- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Full reference: discovery order, limits, selection tools.
- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Where selected URLs usually go next.
- [Page Text Extractor](https://ultimatewebscraper.com/docs/extension/page-text-extractor) — Turn a whole site's URLs into clean text.


---

### Export Any Shopify Store to a Re-importable CSV

*Pull any Shopify store's full catalogue with the Shopify Extractor and export a 35-column, import-ready Shopify CSV — one clean row per variant.*

**Source:** https://ultimatewebscraper.com/docs/guides/export-shopify-store-to-csv

The Shopify Extractor pulls an entire store catalogue — or just the collections you pick — into the Data Table, then exports a CSV formatted to re-import cleanly into another Shopify store.

##### Open the store — detection is automatic

Visit any Shopify store (custom domains included). The extension detects Shopify automatically and shows a **"Shopify store detected"** banner on the side panel home screen, with a "Recommended" badge on the Shopify Extractor card.

*[Screenshot: The side panel home screen on a Shopify store with the 'Shopify store detected' banner and the Recommended badge on the Shopify Extractor card]*

##### Open the Shopify Extractor

The tool scans the store and shows a store card: name, currency, country, domain, product count, and collections. It works reliably on custom domains and most stores.

##### Choose your scope

Pick **Whole catalogue** or select specific **Collections** from the multi-select picker. Products appearing in multiple selected collections are written once.

##### Optionally fetch full product details

Toggle **"Fetch full product details"** for a slower second pass that adds data the bulk feed lacks: inventory quantities, barcodes (UPC/EAN), clean descriptions, weight, and price ranges. Skip it when you just need titles, prices, and images fast.

##### Run the extraction

Start it and watch product and variant counts stream live. Results land in the Data Table with **one row per variant**, per-variant images resolved. Stopping early keeps everything collected so far. Extraction is free — no caps.

##### Export the Shopify CSV

In the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table), open the **Export** menu — a **Shopify CSV** option appears on Shopify tables. See [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) for all formats.

*[Screenshot: The Data Table's Export menu open on a Shopify table, with the Shopify CSV option visible among the export formats]*

#### What's in the CSV

The file has **35 import-ready columns** in Shopify's own import format: Handle, Title, Body (HTML), Vendor, Type, Tags, Options 1–3, Variant SKU, Variant Price, Variant Compare At Price, Variant Barcode, images, SEO fields, and more — one row per variant, with extra product images on their own handle-only rows, exactly as Shopify expects.

A few deliberate choices keep imports safe:

- **Safe defaults** fill fields stores don't publish: Status `active`, Inventory Policy `deny`, Fulfillment Service `manual`, Weight Unit `g`, Gift Card `FALSE`.
- **Variant Inventory Qty is deliberately omitted.** Only about half of stores expose stock levels publicly; leaving the column out means an import will never silently zero your inventory.
- Merchant-only fields (Product Category, SEO overrides, Cost per item) are left blank — they're not public data.

The Data Table also holds extra columns that aren't part of the CSV — Product URL, Availability, Currency, Collection, timestamps, and IDs — useful for analysis even if they don't travel into the import file.

#### Edge cases

- **Password-protected (pre-launch) stores** are detected and refused with a friendly message — use the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) on whatever pages you can see.
- **Headless storefronts and WAF-blocked stores** are caught up-front by a reachability probe with a "can't extract" screen and the same List Extractor suggestion.
- If a run is interrupted mid-way, whole-catalogue mode automatically recovers and keeps going.

#### Related

- [Shopify Extractor](https://ultimatewebscraper.com/docs/extension/shopify-extractor) — Full reference: detection, settings, and captured fields.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — All export formats and gating.
- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Clean and edit the catalogue before exporting.


---

### Turn Webpages into Clean Text for AI and LLM Projects

*Extract boilerplate-free plain text plus title, author, date, and word count from any list of URLs with the Page Text Extractor — one row per page.*

**Source:** https://ultimatewebscraper.com/docs/guides/extract-clean-text-for-ai

Feeding webpages to an LLM means stripping the junk first: navigation, ads, footers, share widgets. The Page Text Extractor does exactly that — give it a list of URLs, get back one clean row per page with the main content as plain text plus useful metadata.

##### Add your URLs

Open **Page Text Extractor** from the side panel. Paste URLs manually, **upload a CSV**, or use **Data Source** to pull a URL column from a previous extraction. The first URL loads as a preview so you can sanity-check the target.

*[Screenshot: The Page Text Extractor's URL input with a pasted list of article URLs and the first page loaded as a preview in the active tab]*

##### Adjust configuration if needed

The defaults work for most sites: a short delay between requests and a page-load wait so JavaScript-rendered articles finish rendering before extraction. Slow sites may want a longer load timeout.

##### Run the extraction

Start it and let it work through the list in the background. Each page becomes one row with these columns:

| Column | Content |
| --- | --- |
| url | Source URL |
| title | Page title, upgraded from og:title or the h1 when longer |
| description | Meta or social description |
| content | Main content as plain text |
| word\_count | Word count of the content |
| author | Author from metadata or common byline selectors |
| publish\_date | Publish date from article metadata or date elements |

*[Screenshot: The Data Table with one row per page, showing the title, content, word\_count, author, and publish\_date columns filled with clean article data]*

##### Export your corpus

Review in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) and export as CSV or JSON — see [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data). JSON is usually the friendliest format for ingestion pipelines.

#### What "clean" means here

Extraction targets the page's main content container (`main`, `article`, common content classes) and **always strips** scripts, styles, navigation, headers, footers, sidebars, ads, social/share widgets, and comment sections. The output is plain, whitespace-normalized text — not HTML, not Markdown — ready to chunk and embed.

#### Use cases

- **RAG corpora** — turn a documentation site or blog into embedding-ready text with source URLs attached.
- **Content audits** — word counts, authors, and publish dates across an entire site in one table.
- **Research datasets** — clean article text at scale, with metadata for filtering.

#### Cover a whole site

Pair it with the [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer): discover every URL the site publishes, export the selection as a URL CSV, and upload that CSV here. That's whole-site coverage in two steps, and both discovery and extraction run locally; the Faster Extraction toggle runs several tabs in parallel.

> **💾 Repeatable corpora**
>
> Save the setup as a [recipe](https://ultimatewebscraper.com/docs/extension/recipes) to re-run the same URL list later — useful for keeping a corpus fresh.

#### Related

- [Page Text Extractor](https://ultimatewebscraper.com/docs/extension/page-text-extractor) — Full reference: columns, configuration, limits.
- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Discover every URL for whole-site text extraction.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Get your corpus out as CSV or JSON.


---

### Extract the Same Data from Hundreds of Pages

*Chain the List Extractor and Page Extractor to visit every link in a list and pull the same fields from each page — one clean row per URL.*

**Source:** https://ultimatewebscraper.com/docs/guides/extract-data-from-multiple-pages

The most powerful pattern in Ultimate Web Scraper is chaining: first scrape a list of links, then visit every link and extract the details each page holds. Product listings to product pages, directory entries to profiles, article indexes to full articles — it's all the same workflow.

##### Scrape the list of links

Use the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) on the listing or search-results page (see [How to scrape any list](https://ultimatewebscraper.com/docs/guides/scrape-any-list)). Links are captured automatically as absolute URLs, so your results will include a link column pointing at each detail page.

##### Open the Page Extractor and pick "Data Source"

Open **Page Extractor** from the side panel. In **Step 1 — Select URLs**, choose **Data Source**: it lists your recent extractions stored locally. Pick the table you just created, then pick its link column. The URL list fills in, and the first URL loads in the active tab so you can define fields against a real page.

You can also feed URLs from a **CSV upload** or straight from the [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — any list of similar pages works.

*[Screenshot: The Page Extractor's Step 1 with the Data Source option open, showing a recent extraction table selected and its link column chosen, the URL list filled in below]*

##### Define what to extract

In **Step 2 — Select What To Extract**, use the **element picker** to click the fields you want on the loaded first page — title, price, description, whatever the pages share. Each picked element becomes a column, with robust fallback selectors behind it.

If the pages carry structured data (most product and article pages do), the tool auto-adds an **Automatic Extract** step, which pulls names, prices, ratings, and more with zero configuration — often you don't need to pick anything at all. See [Scrape product data without selectors](https://ultimatewebscraper.com/docs/guides/scrape-product-data-without-selectors).

*[Screenshot: The element picker on a product detail page with the title and price fields already picked and listed as columns in the Page Extractor's Step 2]*

##### Run it

Click **Start extraction**. The extractor visits each URL in order and writes **one row per URL** into the Data Table, preserving your input order. The progress overlay shows per-URL status live.

Failures don't derail the run: transient errors (timeouts, network hiccups) are retried automatically, permanent ones (404s, blocks) are skipped, and everything is categorized and reported at the end — the batch never aborts because a few pages misbehaved.

##### Review and export

Open the Data Table, clean up columns, and export. If this is a job you'll repeat, save it as a [recipe](https://ultimatewebscraper.com/docs/extension/recipes) — the URLs, steps, and settings all round-trip.

#### Speed

By default the extractor processes pages in a single tab, navigating URL by URL. The **Faster Extraction** toggle runs several tabs in parallel — roughly 5x faster on large batches. There's no cap on how many URLs you can process.

> **🤝 Be a good citizen**
>
> For large batches on one site, consider raising the request delay or enabling anti-bot randomization in the Configuration panel — steadier pacing means fewer blocks and cleaner results.

#### Related

- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — URL sources, extraction steps, and all configuration options.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Capture the list of links that feeds this workflow.
- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Another way to source hundreds of URLs in seconds.


---

### Extract Google Maps Listings into a Spreadsheet

*Collect Google Maps place URLs, then let the Page Extractor's Maps action pull names, ratings, addresses, phones, websites, and hours per listing.*

**Source:** https://ultimatewebscraper.com/docs/guides/extract-google-maps-listings

Local business research, lead lists, competitor mapping — Google Maps holds the data, and the Page Extractor's dedicated Maps action gets it out. Feed it place URLs; get back one structured row per listing.

##### Collect Google Maps place URLs

You need URLs of individual Maps listings. A practical way to gather them: run a Google Maps search (e.g. "dentists in Austin"), then use the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) on the results panel — it captures each result's link along with visible names and ratings. Alternatively, upload a CSV of place URLs you already have.

##### Feed them to the Page Extractor

Open **Page Extractor** and load your URLs — via **Data Source** (pointing at the List Extractor table's link column) or CSV upload.

##### Choose the Google Maps action

When the tool detects Google Maps URLs in your list, it offers the **Extract: Google Maps** action in Step 2. Select it — no element picking needed; the action knows Maps listings.

*[Screenshot: The Page Extractor's Step 2 offering the 'Extract: Google Maps' action after Maps place URLs were detected in the URL list]*

##### Run and export

Start the extraction. Each place becomes one row with **place name, rating, address, phone, website, opening hours** and more. Clean up in the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) and export.

*[Screenshot: The Data Table with one row per Google Maps place, showing name, rating, address, phone, website, and hours columns]*

#### Running it in the cloud

Google Maps extractions are also supported as **cloud tasks**: run your Maps setup once locally, then send it to the [Cloud Platform](https://ultimatewebscraper.com/docs/cloud/scheduling) to run on cloud browsers — on a schedule if you want, with results in the web dashboard. Cloud runs require a paid plan and consume 1 credit per page.

AI agents connected to your cloud workspace can start `google_maps` extractions too — hand Claude a list of place URLs (or a column of an existing cloud table) and it creates the run for you. See [agent-created extractions](https://ultimatewebscraper.com/docs/ai/agent-extractions).

> **🐢 Pace yourself**
>
> Maps pages are JavaScript-heavy. If rows come back thin, raise the request delay or the content-wait timeout in the Page Extractor's configuration so each listing fully renders before extraction.

#### What you get per listing

| Field | Example |
| --- | --- |
| Place name | "Bright Smile Dental" |
| Rating | 4.7 |
| Address | Street, city, state |
| Phone | Formatted phone number |
| Website | The business's own site |
| Hours | Opening hours |

Combine the website column with the [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) for a full lead-enrichment pipeline: Maps listing to website to contact email, all inside the extension.

#### Related

- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — The tool behind the Google Maps action.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Collect place URLs from Maps search results.
- [Cloud scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling) — Run Maps extractions on a recurring schedule.


---

### How to Find Email Addresses on Any Website

*Use the Email Extractor's deep scan to crawl one site or thousands, catching plain, obfuscated, and mailto emails — free, with no page caps.*

**Source:** https://ultimatewebscraper.com/docs/guides/find-emails-on-any-website

The Email Extractor visits a list of websites, follows their internal links, and collects every email address it finds — including cleverly disguised ones. It's free with no caps on how many sites you scan.

##### Enter your URLs

Open **Email Extractor** from the side panel. Add the sites you want to scan: type them in manually, **upload a CSV** and pick the URL column, or use **Data Source** to pull a URL column from a previous extraction (for example, a scraped directory of company websites).

##### Check the deep scan settings

**Deep scanning is on by default**, and it's what makes the tool thorough. For each seed URL it also follows that page's direct links — depth 1 — visiting **up to 10 links per page** by default, and staying **on the same domain** so it doesn't wander off-site. Contact, About, and Team pages get scanned automatically this way even when the homepage has no email on it.

##### Run the extraction

Click **Start extraction**. The overlay shows emails found, unique emails, a per-domain breakdown, and sub-pages scanned in real time. Failures are retried where sensible and never abort the batch.

*[Screenshot: The Email Extractor's progress overlay mid-run, showing live counts for emails found, unique emails, sub-pages scanned, and a per-domain breakdown]*

##### Review the results

Each seed URL becomes one row in the Data Table: the URL, its unique emails (comma-joined), and an email count. Results are deduplicated globally, lowercased, and validated. Export from the [Data Table](https://ultimatewebscraper.com/docs/extension/exporting-data) when you're done.

*[Screenshot: The Data Table with one row per scanned site: URL column, comma-joined unique emails column, and an email count column]*

#### What gets detected

The extractor works on the page's rendered text plus its links, so it catches:

- **Standard addresses**, including ones written with spaces around the @ sign.
- **Obfuscated forms**, normalized back to real addresses: `name (at) domain.com`, `[at]`, `{at}`, `_at_` spellings, "at ... dot ..." phrasings, and similar.
- **mailto links**, with tracking parameters stripped.

Emails rendered inside images, or hidden behind interactions (click-to-reveal), are not detected.

#### Tips for better results

- **Raise depth and links-per-page for thoroughness.** Depth goes up to 5 and links-per-page up to 50 — useful for larger sites where contact info sits deeper. More pages means longer runs.
- **Use the domain filter** (an allow-list) when you only want emails on certain domains — handy for excluding gmail.com noise or keeping only corporate addresses.
- **Add custom regex patterns** if you're after unusual formats — one pattern per line in the configuration.

#### Speed and scale

Deep scan, all detection patterns, domain filters, custom patterns, and unlimited URLs are all included. The **Faster Extraction** toggle runs several tabs in parallel for big jobs. Export the results from the [Data Table](https://ultimatewebscraper.com/docs/extension/exporting-data) in any format.

> **⚠️ LinkedIn**
>
> LinkedIn itself can't be used as a seed URL — it's blocked in every tool. Emails found on other sites are unaffected.

#### Related

- [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) — Full reference: crawl settings, detection, configuration.
- [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) — Same engine, tuned for social profiles — with emails as an add-on.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Get your email list into CSV, Excel, or Sheets.


---

### Find Social Media Profiles for a List of Websites

*Enrich a lead list with the Social Link Extractor — one column per platform across 7 networks, plus custom patterns and optional email collection.*

**Source:** https://ultimatewebscraper.com/docs/guides/find-social-media-profiles

Got a list of company websites and need their Twitter, Instagram, and Facebook pages? The Social Link Extractor visits each site and returns the profile links it finds — one column per platform, one row per site.

##### Add your websites

Open **Social Link Extractor** from the side panel. Add URLs by typing them in, **uploading a CSV**, or picking a URL column from a previous extraction via **Data Source** — the natural follow-up to scraping a directory or lead list with the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor).

##### Choose what to extract

"Extract Social Links" is always on in this tool. Optionally enable **Extract Emails** as an add-on to collect email addresses in the same pass — one crawl, both datasets.

##### Tune the scan (optional)

Deep scanning is on by default: for each site the tool also follows up to 10 of its same-domain links (depth 1), which is usually where footer-less sites hide their social icons — About and Contact pages. All seven platform detectors are on by default: **Twitter/X, Facebook, Instagram, YouTube, TikTok, GitHub, Pinterest**. You can also add **custom URL patterns** (your own regex), each becoming an extra column.

*[Screenshot: The Social Link Extractor's settings panel showing the seven platform toggles all enabled, the deep scan option, and the custom URL patterns field]*

##### Run and review

Start the extraction. Each seed URL becomes one row: the URL, a combined social-links column, and **one column per platform**, deduplicated per platform. Detection scans both link hrefs and URLs written in page text, so even non-linked handles pasted into a footer get caught. Export from the [Data Table](https://ultimatewebscraper.com/docs/extension/exporting-data).

*[Screenshot: The Data Table with one row per website and one column per social platform, profile URLs filled in for Twitter, Instagram, and Facebook]*

#### Use case: enriching a lead list

The classic pipeline:

1. Scrape a directory or search results into a table with the List Extractor — company names plus website links.
2. Feed the website column into the Social Link Extractor via Data Source, with Extract Emails enabled.
3. Get back the same list enriched with per-platform profile columns and contact emails, ready to merge into your CRM.

#### Note: LinkedIn is not supported

LinkedIn is blocked as a target in every tool.

#### Speed and scale

All platforms, custom patterns, deep scanning, and the email add-on are included, with no URL caps. The **Faster Extraction** toggle runs several tabs in parallel for big jobs. Export the results from the [Data Table](https://ultimatewebscraper.com/docs/extension/exporting-data) in any format.

#### Related

- [Social Link Extractor](https://ultimatewebscraper.com/docs/extension/social-link-extractor) — Full reference: platforms, patterns, crawl settings.
- [Email Extractor](https://ultimatewebscraper.com/docs/extension/email-extractor) — The same engine focused on email discovery.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Build the lead list that feeds this workflow.


---

### Guides

*Step-by-step guides for common web scraping jobs — lists, product data, emails, images, Shopify exports, Google Maps, logins, and scheduled monitoring.*

**Source:** https://ultimatewebscraper.com/docs/guides

Each guide walks through one real-world job from start to finished spreadsheet, using the exact tool and settings for it. If you're brand new, do the [Quickstart](https://ultimatewebscraper.com/docs/getting-started/quickstart) first — it takes 60 seconds.

- [Scrape any list or table](https://ultimatewebscraper.com/docs/guides/scrape-any-list) — Turn any repeating list, grid, or table into a spreadsheet — with infinite scroll, pagination, or Load More.
- [Extract data from hundreds of pages](https://ultimatewebscraper.com/docs/guides/extract-data-from-multiple-pages) — Chain a list of links into the Page Extractor and get one row per URL.
- [Scrape product data without selectors](https://ultimatewebscraper.com/docs/guides/scrape-product-data-without-selectors) — Zero-config product extraction from structured data — names, prices, ratings, SKUs.
- [Export a Shopify store to CSV](https://ultimatewebscraper.com/docs/guides/export-shopify-store-to-csv) — Pull a whole catalogue and export a re-importable Shopify CSV.
- [Find emails on any website](https://ultimatewebscraper.com/docs/guides/find-emails-on-any-website) — Deep-scan sites for email addresses, including obfuscated ones.
- [Find social media profiles](https://ultimatewebscraper.com/docs/guides/find-social-media-profiles) — Enrich a list of websites with profile links across 7 platforms.
- [Bulk download images](https://ultimatewebscraper.com/docs/guides/bulk-download-images) — Scan, filter, and download every image on a page — or across many pages.
- [Extract clean text for AI](https://ultimatewebscraper.com/docs/guides/extract-clean-text-for-ai) — Turn webpages into boilerplate-free plain text with metadata for LLM projects.
- [Discover URLs with Sitemap Explorer](https://ultimatewebscraper.com/docs/guides/discover-urls-with-sitemap-explorer) — Map every URL a site publishes and hand the branch you need to another tool.
- [Extract Google Maps listings](https://ultimatewebscraper.com/docs/guides/extract-google-maps-listings) — Turn Maps place URLs into a spreadsheet of names, ratings, phones, and hours.
- [Scrape behind logins](https://ultimatewebscraper.com/docs/guides/scrape-behind-logins) — Extract pages only visible to your account, locally or in the cloud.
- [Schedule recurring extractions](https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions) — Monitor prices and content on a schedule with cloud runs, Sheets, and webhooks.

[How to Scrape Any List or Table from a Website

Turn any repeating list, grid, or table into a spreadsheet with the List Extractor — including infinite scroll, pagination, and Load More buttons.](https://ultimatewebscraper.com/docs/guides/scrape-any-list)


---

### Schedule Recurring Extractions for Price Monitoring

*Turn any extraction into a scheduled cloud task — from every 10 minutes to monthly — with results flowing into Google Sheets or a webhook automatically.*

**Source:** https://ultimatewebscraper.com/docs/guides/schedule-recurring-extractions

Price monitoring, content change tracking, fresh lead feeds — recurring jobs shouldn't need your laptop open. Build the extraction once, send it to the Cloud Platform, and it runs on a schedule in cloud browsers with results waiting in your dashboard.

##### Build and test the extraction locally

Configure the job in the extension — a [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) run on a category page, a [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) batch over product URLs — and run it locally until the output looks right. Cloud tasks are created **from your local run history**, so a working local run is the starting point. List, Page, Email, and Social extractions can run in the cloud.

##### Open the Run in Cloud wizard

From the side panel's **Run in Cloud** card (or the cloud button inside a tool), pick the automation you just ran from the list.

##### Pick a schedule

Choose a preset: run once, **every 10 minutes**, every 30 minutes, hourly, every 6 or 12 hours, daily, every 2 or 3 days, weekly, or **monthly**. Day-level schedules run at **midnight UTC**. For price monitoring, hourly to daily is the usual sweet spot. The task also runs immediately on creation, so you get a first result right away.

*[Screenshot: The Run in Cloud wizard's schedule picker showing the presets from run once and every 10 minutes up to monthly, with daily selected]*

##### Wire up where the data goes

In the **Integrations** section, add one or both:

- **Google Sheets** — create, replace, or **append** to a sheet on every run. Append mode builds a growing price history automatically, timestamped run by run.
- **Webhook** — each run's results are pushed to your endpoint, ready for your own alerting or database.

Both are off by default. You can also tune the proxy location, user agent, data cleanup, and [session cloning](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) here.

*[Screenshot: The Integrations section of the Run in Cloud wizard with Google Sheets in append mode enabled and a webhook endpoint configured]*

##### Submit and monitor

Click **Run & Schedule**. From then on, watch it in the [cloud dashboard](https://ultimatewebscraper.com/docs/cloud/scheduling): run history with timelines, the resulting data tables (editable, filterable, exportable), and your credit balance.

#### What it costs

Cloud scheduling requires a **paid plan**. Each run consumes **1 credit per page extracted** — a 50-product price check running daily uses 50 credits a day. See [pricing](https://ultimatewebscraper.com/pricing) for plans and allowances. Local extension use never touches credits.

> **🛡️ Blocked pages**
>
> Cloud runs come with proxies and anti-blocking built in, and the optional Page Unblocker handles Cloudflare Turnstile challenges automatically (it consumes credits). Other captcha types are detected but fail the page.

#### Tips for reliable monitoring

- **Append, don't replace**, in Google Sheets when you want history — replace mode is for "latest snapshot" dashboards.
- **Match the schedule to the data.** Prices rarely change more than daily; every-10-minutes is better spent on availability or breaking content.
- **Keep the data cleanup defaults on** — empty and duplicate rows are removed before your data lands in Sheets.

#### Related

- [Cloud scheduling](https://ultimatewebscraper.com/docs/cloud/scheduling) — All schedule presets and how runs are managed.
- [Integrations](https://ultimatewebscraper.com/docs/cloud/integrations) — Google Sheets and webhook delivery in depth.
- [Cookies and sessions](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) — Schedule extractions behind logins.

[How to Scrape Pages Behind a Login

Extract members-only pages using your own browser session locally, or clone cookies into a cloud browser for scheduled logged-in extractions.](https://ultimatewebscraper.com/docs/guides/scrape-behind-logins)


---

### How to Scrape Any List or Table from a Website

*Turn any repeating list, grid, or table into a spreadsheet with the List Extractor — including infinite scroll, pagination, and Load More buttons.*

**Source:** https://ultimatewebscraper.com/docs/guides/scrape-any-list

Search results, product grids, directories, job boards, HTML tables — if content repeats on a page, the List Extractor can turn it into rows. You click one item; it captures the whole list.

##### Select the list

Open the page, open **List Extractor** from the side panel, and click **Click to Select List**. An element picker appears on the page: hover over the list and the extension highlights the detected container with a count like "List with 24 items found — Smart detection". Click to select it.

*[Screenshot: The element picker highlighting a detected list container on an e-commerce product grid, with the 'List with 24 items found — Smart detection' badge visible]*

##### Check the instant preview

The moment you select, the Data Table opens with a live preview of the currently visible items. Field detection is automatic — text, links, images, prices, ratings, and dates are captured and organized into typed columns. If the preview looks wrong, re-pick a different item.

##### Choose how to load more items

Most lists don't show everything at once. Pick the load-more method that matches the page (default is Auto-Scroll):

- **Auto-Scroll** — for infinite-scroll pages. The tool scrolls and extracts items as they appear, stopping when scrolling produces no new content.
- **Pagination** — for pages with a "Next" button or link. You pick the Next button once with the picker; the tool then extracts, clicks Next, waits for the page to change, and repeats until no valid Next button remains.
- **Load More** — for buttons that add items to the same page. The tool clicks the button repeatedly, extracting new items each cycle.

*[Screenshot: The List Extractor's load-more method selector showing the Auto-Scroll, Pagination, and Load More options with Auto-Scroll selected]*

##### Pick a speed profile

Choose Slow, Normal, or Fast (the default). Fast works on most sites; switch to Normal or Slow for pages that load content sluggishly, so items have time to render before each extraction pass. Every timing value is editable if you need finer control.

##### Run the extraction

Click **Start extraction**. A progress overlay shows a live item count while rows stream into the Data Table. You can stop at any time and keep everything collected so far. There's no row or page cap — the run continues until the content is exhausted or you stop it.

##### Clean up and export

In the [Data Table](https://ultimatewebscraper.com/docs/extension/data-table), remove unwanted columns, rename headers, filter out empty rows, and merge columns if needed. Then export via the **Export** menu — CSV, Excel, JSON, or Google Sheets. See [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data).

> **💾 Save it as a recipe**
>
> Happy with the setup? Save it as a [recipe](https://ultimatewebscraper.com/docs/extension/recipes) — selectors, load-more method, and timing are stored, and running it later auto-navigates to the saved page.

#### Troubleshooting

**The list isn't detected.** Smart detection requires the list items to be direct children of a single container, with at least 3 similar items. Very short lists (2 items) or layouts where each "item" lives in its own separate wrapper may not be recognized — try hovering over a different part of an item, or a different item.

**Some content is missing from rows.** Content inside shadow DOM or cross-origin iframes is not reachable — the picker and extractor work on the top document only. Embedded widgets (maps, third-party review frames) fall into this category.

**The preview only shows a few items.** That's expected: the instant preview covers items currently rendered on the page. The full run with your chosen load-more method collects the rest.

#### Related

- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Full reference: options, speed profiles, limitations.
- [Data Table](https://ultimatewebscraper.com/docs/extension/data-table) — Edit, filter, and clean your results.
- [Exporting data](https://ultimatewebscraper.com/docs/extension/exporting-data) — Every export format, and how to filter before exporting.


---

### How to Scrape Pages Behind a Login

*Extract members-only pages using your own browser session locally, or clone cookies into a cloud browser for scheduled logged-in extractions.*

**Source:** https://ultimatewebscraper.com/docs/guides/scrape-behind-logins

Dashboards, member directories, order histories, gated catalogues — if a page needs a login, you can still extract it. The rule of thumb: **if you can see it in your browser, you can extract it.**

##### Log in as usual

Sign in to the site in Chrome, exactly as you normally would. The extension runs inside your browser and uses **your existing session** — there's no separate login to configure, no credentials to hand over.

##### Extract like any other page

Use whichever tool fits the job — [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) for gated lists and tables, [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) for batches of member-only detail pages. Because extraction happens locally in your logged-in browser, gated pages render just as you see them. Results stay in your local Data Table.

#### Logged-in extractions in the cloud

Cloud runs happen in a **cloud browser** that starts with no session — so a login wall would stop it. The fix is session cloning:

##### Build and test the extraction locally

Run it once in your logged-in browser to confirm it works.

##### Enable Cookies and Storage cloning

In the **Run in Cloud** wizard, open the **Cookies & Storage** section and enable cloning. Your current session's cookies and localStorage for the target site are replicated into the cloud browser, so it arrives already logged in as you.

*[Screenshot: The Run in Cloud wizard's Cookies & Storage section expanded, with session cloning enabled for the target site]*

##### Run or schedule

Submit the task. The cloud browser loads the pages with your session, on a schedule if you set one. See [Cookies and sessions](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) for details, including what happens when sessions expire.

> **⚠️ Use it responsibly**
>
> Session-based extraction is for **your own accounts** and data you're entitled to access. Respect each site's terms of service and rate limits, and don't extract other people's private data. You are responsible for how you use your sessions.

#### What's not possible

**LinkedIn is blocked regardless of login state** — every tool refuses LinkedIn URLs, locally and in the cloud, and being signed in doesn't change that.

Beyond that, the usual limits apply: content inside cross-origin iframes or shadow DOM isn't reachable, and pages that require interaction to reveal content (beyond scrolling/pagination the tools handle) won't render it for extraction.

#### Related

- [Cookies and sessions](https://ultimatewebscraper.com/docs/cloud/cookies-and-sessions) — How session cloning works for cloud runs.
- [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) — Extract gated lists and tables locally.
- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Batch-extract member-only pages.


---

### Scrape Product Data with Zero Configuration

*Automatic Extract reads a page's structured data — JSON-LD, microdata, meta tags — and returns names, prices, SKUs, and ratings with no selectors.*

**Source:** https://ultimatewebscraper.com/docs/guides/scrape-product-data-without-selectors

Most modern e-commerce sites (and news sites, and job boards) embed structured data in every page for search engines. The Page Extractor's **Automatic Extract** step reads it directly — no element picking, no selectors, no configuration.

##### Collect the product URLs

You need a list of product page URLs. The fastest source is usually the [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer): open it on the store, let it discover the sitemap, and select the products branch of the URL tree. Alternatively, scrape a category page with the [List Extractor](https://ultimatewebscraper.com/docs/extension/list-extractor) or upload a CSV.

##### Load them into the Page Extractor

Open **Page Extractor** and add your URLs in Step 1 — via Sitemap Explorer, Data Source, or CSV upload. The first URL loads in the active tab.

##### Let Automatic Extract take over

If the first page contains structured data, the tool detects it and **auto-adds the Automatic Extract step** — you'll see it appear in Step 2 without doing anything. It even probes a few times to catch structured data that's injected late by JavaScript. If it doesn't appear automatically, you can add it manually.

*[Screenshot: The Page Extractor's Step 2 with the Automatic Extract step auto-added after a product page loaded, no manually picked fields present]*

##### Run and review

Start the extraction. Each page becomes one row with columns drawn from the page's structured data. For products, that typically includes:

| Column group | Examples |
| --- | --- |
| Identity | Name, Brand, Category, Type |
| Pricing | Price, All Prices, Currency, Offers count |
| Stock | Availability |
| Attributes | Color, Size, Material, Weight |
| Social proof | Rating (e.g. "4.6 (1,203)"), Reviews |
| Identifiers | SKU, GTIN-8/12/13/14, MPN, Variant SKUs |
| Media | Image(s) |

Prices and enumerations are normalized, and cross-referenced entities are resolved for you.

*[Screenshot: The Data Table with one row per product page, showing automatically extracted Name, Brand, Price, Rating, and SKU columns]*

#### How variants are handled

Product variants **consolidate into one row per URL** — sizes, colors, and per-variant prices are joined into multi-value cells rather than exploded into separate rows. The complete raw structured data is preserved in a `_raw_jsonld` column if you need every detail.

#### Where it works — and where it doesn't

Automatic Extract is generic: it reads **JSON-LD, microdata, and Open Graph/Twitter/standard meta tags**, so it works on WooCommerce, Magento, custom stores, news sites, job boards — anywhere structured data exists. It picks the page's subject entity (Product, Article, JobPosting, Event, Recipe, LocalBusiness, and more) and flattens it into a row.

Its limits are the flip side of the same design:

- **Sites without structured data return little or nothing.** Use the element picker in the Page Extractor to define fields manually instead — both steps can coexist in one run.
- It reads markup, not JavaScript state: data that lives only in JS variables isn't captured.
- Listing pages (a page describing many products) collapse to one row — feed it detail pages, not category pages.

> **🛍️ Scraping a Shopify store?**
>
> For a whole Shopify catalogue, skip this workflow entirely — the dedicated [Shopify Extractor](https://ultimatewebscraper.com/docs/extension/shopify-extractor) pulls the full catalogue in one pass, one row per variant. See [Export any Shopify store to CSV](https://ultimatewebscraper.com/docs/guides/export-shopify-store-to-csv).

#### Related

- [Page Extractor](https://ultimatewebscraper.com/docs/extension/page-extractor) — Automatic Extract, element picking, and all URL sources.
- [Sitemap Explorer](https://ultimatewebscraper.com/docs/extension/sitemap-explorer) — Discover every product URL a store publishes.
- [Shopify Extractor](https://ultimatewebscraper.com/docs/extension/shopify-extractor) — Whole-catalogue extraction for Shopify stores.


---
