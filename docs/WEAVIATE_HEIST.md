# One-time Weaviate → Markdown heist (2017 WikiChunk)

Location 2 (`D:\weaviate_v2_archive\weaviate`) is a **524 GB Weaviate v2 binary DB**, not
Markdown. EMPIRE does **not** keep Weaviate as a runtime dependency. Boot it only long enough
to dump collections to staging on `I:`, then tear it down.

| Item | Value |
|------|-------|
| Source (read) | `D:\weaviate_v2_archive\weaviate` |
| Staging (write) | `I:\EMPIRE_DATA\weaviate_dump\{year}\` |
| Cognee (NTFS VHDX) | `V:\Cognee` |
| Collections | `WikiChunk` (2017 / `snapshot_id=20170301`), `WikiChunk2021`, `WikiChunk2026` |
| Approx. object counts | WikiChunk ≈ 12.5M · WikiChunk2021 ≈ 15.2M · WikiChunk2026 ≈ 18.5M |

## Why base `WikiChunk` is 2017

Schema has a `snapshot_id` property. Sample objects in `WikiChunk` carry
`snapshot_id: "20170301"` (and `doc_id` / `chunk_id` prefixed `wikipedia:20170301:…`).
`WikiChunk2021` → `20210501`, `WikiChunk2026` → `20260401`. The unlabeled collection name
is therefore **confirmed 2017 by object flags**, not only by convention.

## Temporary Docker boot

Port **8080** is often taken (`media-weaviate` / EMPIRE frontend). Use **8091**.

A pure `:ro` volume mount **fails** (Weaviate must open Bolt `schema.db` for write). Mount
RW, but the export script issues **GET only** — no schema/object mutations.

```powershell
docker rm -f empire-weaviate-heist-2017 2>$null

docker run -d --name empire-weaviate-heist-2017 `
  -p 8091:8080 -p 50052:50051 `
  -e AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=false `
  -e AUTHENTICATION_APIKEY_ENABLED=true `
  -e AUTHENTICATION_APIKEY_ALLOWED_KEYS=WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih `
  -e AUTHENTICATION_APIKEY_USERS=hello@dify.ai `
  -e AUTHORIZATION_ADMINLIST_ENABLED=true `
  -e AUTHORIZATION_ADMINLIST_USERS=hello@dify.ai `
  -e PERSISTENCE_DATA_PATH=/var/lib/weaviate `
  -e DISABLE_TELEMETRY=true `
  -e QUERY_DEFAULTS_LIMIT=25 `
  -e DEFAULT_VECTORIZER_MODULE=none `
  -e CLUSTER_HOSTNAME=node1 `
  -v "D:/weaviate_v2_archive/weaviate:/var/lib/weaviate" `
  semitechnologies/weaviate:1.27.0 `
  --host 0.0.0.0 --port 8080 --scheme http

# Wait until ready:
# GET http://127.0.0.1:8091/v1/.well-known/ready
# Header: Authorization: Bearer WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih
```

## Bounded verification export (do this first)

From `C:\EMPIRE`:

```powershell
.\venv\Scripts\python.exe -m pipeline.weaviate_export `
  --collection WikiChunk `
  --url http://127.0.0.1:8091 `
  --api-key WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih `
  --limit 50 `
  --out I:\EMPIRE_DATA\weaviate_dump `
  --out-subdir 2017 `
  --snapshot-id 20170301 `
  --snapshot-year 2017
```

Confirm a sample file under `I:\EMPIRE_DATA\weaviate_dump\2017\` has frontmatter
`snapshot_id: "20170301"` and `snapshot_year: "2017"`.

## Full heist (multi-hour; run only when ready)

`--limit 0` = all objects (~12.5M for 2017). Prefer a long-lived PowerShell window / overnight
job. Expect many hours and large disk use on `I:`.

```powershell
.\venv\Scripts\python.exe -m pipeline.weaviate_export `
  --collection WikiChunk `
  --url http://127.0.0.1:8091 `
  --api-key WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih `
  --limit 0 `
  --page-size 100 `
  --out I:\EMPIRE_DATA\weaviate_dump `
  --out-subdir 2017 `
  --snapshot-id 20170301 `
  --snapshot-year 2017
```

Optional later: repeat with `--collection WikiChunk2021 --out-subdir 2021` /
`WikiChunk2026` / `2026` if you want Weaviate-sourced staging for those years too
(Markdown on `D:\wiki_md` is usually preferred for 2021/2026).

## Tear down (required)

```powershell
docker stop empire-weaviate-heist-2017
docker rm empire-weaviate-heist-2017
```

## Ingest pilot into Cognee (`wikipedia_2017` on `V:\Cognee`)

Requires: VHDX mounted (`V:\Cognee`), Ollama up, PocketBase optional for job records.

```powershell
.\venv\Scripts\python.exe -m pipeline.wiki_ingest `
  --export-dir I:\EMPIRE_DATA\weaviate_dump\2017 `
  --dataset wikipedia_2017 `
  --mode fast `
  --limit 20 `
  --no-resume
```

Cross-year recall (all datasets):

```powershell
.\venv\Scripts\python.exe -m pipeline.cognee_worker recall --query "Commonwealth Association of Planners"
```
