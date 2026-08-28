---
name: exercises-dataset-lookup
description: Reference-lookup skill for a static fitness exercise dataset (1,324 exercises with body-part/equipment/muscle taxonomy, 9-language instructions, thumbnail + GIF assets). Use when a user asks for exercise data, instructions, or images for a specific exercise/muscle group, or wants to build a workout feature. Touches PocketBase (as optional storage for the dataset) and Cognee (optional semantic search over instructions) when used inside Build1; the raw dataset itself is infra-agnostic static data.
icon: dumbbell
color: Orange
---

# Exercises Dataset — Reference Lookup

A static data + media asset set (MIT-licensed code/data; media used under the original creator's terms — check `NOTICE.md`). No CLI/API to run — query the shipped files directly.

## Where things live

- `data/exercises.json` — 1,324 exercise records.
- `data/exercises.schema.json` — formal JSON Schema (Draft 2020-12) for validating filters/additions.
- `images/` — 180×180 thumbnails (filenames match each record's `image` field).
- `videos/` — animation GIFs (filenames match each record's `gif_url` field).
- `index.html` — a standalone client-side exercise browser.
- `setup.html` — developer guide for DB import / API integration.

## Record schema

`id`, `name`, `category`/`body_part` (e.g. "upper arms", "chest", "back"), `equipment` (e.g. "dumbbell", "body weight"), `muscle_group` (primary), `secondary_muscles` (array), `instructions.<lang>` / `instruction_steps.<lang>` for `en, es, it, tr, ru, zh, hi, pl, ko`, plus `image`/`gif_url` and `attribution`/`media_id`.

Body-part distribution: Upper Arms 292, Upper Legs 227, Back 203, Waist 169, Chest 163, Shoulders 143, Lower Legs 59, Lower Arms 37, Cardio 29, Neck 2.

## How to answer a request

1. **"Exercises for <body part / muscle / equipment>"** — filter `exercises.json` by `body_part`/`category`, `muscle_group`, or `equipment`; return matching `name` + `instructions.<lang, default en>`.
2. **"How do I do a <named exercise>?"** — find the record by `name` (case-insensitive), return `instructions.<lang>` or `instruction_steps.<lang>`, and reference its `image`/`gif_url`.
3. **"In <language>"** — read `instructions.<lang-code>` for the same record; supported: en, es, it, tr, ru, zh, hi, pl, ko.
4. **"Build a fitness app / import into a DB"** — point to `setup.html` and `exercises.schema.json` (see Build1 Integration below for the Build1-specific path).
5. Cite media attribution per `NOTICE.md` if the user redistributes images/GIFs beyond private use.

## Output

Return only the specific fields requested (name, instructions, muscle data) and, where useful, the relative asset path so it can be embedded. Never invent exercises or instructions not present in `exercises.json`.

## Build1 Integration

To power a workout feature in Build1:
- **PocketBase**: import `data/exercises.json` rows into a PocketBase `exercises` collection (one field per schema key) so the HTMX/Alpine frontend can filter/query it via PocketBase's REST API instead of shipping the raw JSON to the client.
- **Cognee**: optionally run `cognee.add()` + `cognee.cognify()` over the `instructions.en` text so a FastMCP tool can expose natural-language queries like "exercises that help lower back pain" via `cognee.search()`.
- **Frontend**: serve `images/` and `videos/` as static assets referenced by PocketBase records' relative paths; render filtered results as HTMX-swapped partials.
- No Ollama/inference dependency is required unless you add the Cognee semantic-search layer, which itself should run against local Ollama per the `cognee-memory-pipeline` skill.
