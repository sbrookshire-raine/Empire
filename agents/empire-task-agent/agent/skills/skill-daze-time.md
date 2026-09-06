Use when the user asks about their day schedule, free time, overbooking, exercise/meditation slots, or DAZE / radial day planning — and **Time Reclaim** is enabled in the Toolbelt.

## Mission

Help the Architect see the day as a **finite circle**. List blocks, flag overlaps, and point to free windows for body and mind. Do not invent schedule data.

## Tools

1. `daze_list_day` — blocks (+ conflicts) for a date
2. `daze_upsert_block` — add/update a block (`start_minute` / `end_minute`, 0–1440)
3. `daze_free_windows` — gaps ≥ N minutes for coaching

## How to answer

1. Call tools silently first.
2. Speak in plain language: what’s booked, what’s free, where conflicts are.
3. Prefer suggesting **body** / **rest** into free windows when the user wants time reclamation.
4. If Time Reclaim is off, tell them to enable it in the Toolbelt — do not invent a schedule.
5. Point them to http://127.0.0.1:8080/daze.html for the radial dial when useful.

## Hard rules

- Local PocketBase only — never Firebase / cloud calendars.
- Minutes are 0–1440 (midnight→midnight).
- PocketBase **Tasks** are not day blocks; do not create tasks for schedule arcs unless asked.
