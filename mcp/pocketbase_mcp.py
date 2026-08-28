"""FastMCP server exposing PocketBase CRUD as AI tools."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env.local")
load_dotenv(ROOT / ".env")

POCKETBASE_URL = os.getenv("POCKETBASE_URL", "http://127.0.0.1:8090").rstrip("/")
ADMIN_EMAIL = os.getenv("POCKETBASE_ADMIN_EMAIL", "admin@empire.local")
ADMIN_PASSWORD = os.getenv("POCKETBASE_ADMIN_PASSWORD", "empire-admin-change-me")

mcp = FastMCP("empire-pocketbase")

_token_cache: str | None = None


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


async def _get_token(client: httpx.AsyncClient) -> str:
    global _token_cache
    if _token_cache:
        return _token_cache

    response = await client.post(
        f"{POCKETBASE_URL}/api/collections/_superusers/auth-with-password",
        json={"identity": ADMIN_EMAIL, "password": ADMIN_PASSWORD},
    )
    response.raise_for_status()
    _token_cache = response.json()["token"]
    return _token_cache


async def _request(
    method: str,
    path: str,
    *,
    json_body: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
    auth: bool = True,
) -> Any:
    async with httpx.AsyncClient(timeout=30.0) as client:
        headers: dict[str, str] = {}
        if auth:
            token = await _get_token(client)
            headers["Authorization"] = f"Bearer {token}"

        response = await client.request(
            method,
            f"{POCKETBASE_URL}{path}",
            json=json_body,
            params=params,
            headers=headers,
        )
        response.raise_for_status()
        if response.content:
            return response.json()
        return {}


@mcp.tool()
async def pb_health() -> str:
    """Check whether PocketBase is reachable."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"{POCKETBASE_URL}/api/health")
        response.raise_for_status()
        return _json(response.json())


@mcp.tool()
async def pb_list_collections() -> str:
    """List PocketBase collection names available to the admin API."""
    data = await _request("GET", "/api/collections", params={"page": 1, "perPage": 200})
    names = [item.get("name") for item in data.get("items", []) if item.get("name")]
    return _json({"collections": names})


@mcp.tool()
async def pb_list_records(
    collection: str,
    filter: str = "",
    sort: str = "-created",
    page: int = 1,
    per_page: int = 50,
) -> str:
    """List records from a PocketBase collection with optional filter and pagination."""
    params: dict[str, Any] = {"page": page, "perPage": per_page, "sort": sort}
    if filter:
        params["filter"] = filter

    if collection in {"tasks", "ingestion_jobs", "sources"}:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                f"{POCKETBASE_URL}/api/collections/{collection}/records",
                params=params,
            )
            response.raise_for_status()
            return _json(response.json())

    data = await _request(
        "GET",
        f"/api/collections/{collection}/records",
        params=params,
        auth=True,
    )
    return _json(data)


@mcp.tool()
async def pb_get_record(collection: str, record_id: str) -> str:
    """Fetch a single PocketBase record by collection and id."""
    if collection in {"tasks", "ingestion_jobs", "sources"}:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                f"{POCKETBASE_URL}/api/collections/{collection}/records/{record_id}"
            )
            response.raise_for_status()
            return _json(response.json())

    data = await _request("GET", f"/api/collections/{collection}/records/{record_id}")
    return _json(data)


@mcp.tool()
async def pb_create_record(collection: str, data_json: str) -> str:
    """Create a PocketBase record. data_json must be a JSON object string."""
    payload = json.loads(data_json)
    if collection in {"tasks", "ingestion_jobs", "sources"}:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{POCKETBASE_URL}/api/collections/{collection}/records",
                json=payload,
            )
            response.raise_for_status()
            return _json(response.json())

    data = await _request(
        "POST",
        f"/api/collections/{collection}/records",
        json_body=payload,
    )
    return _json(data)


@mcp.tool()
async def pb_update_record(collection: str, record_id: str, data_json: str) -> str:
    """Update a PocketBase record. data_json must be a JSON object string."""
    payload = json.loads(data_json)
    if collection in {"tasks", "ingestion_jobs", "sources"}:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.patch(
                f"{POCKETBASE_URL}/api/collections/{collection}/records/{record_id}",
                json=payload,
            )
            response.raise_for_status()
            return _json(response.json())

    data = await _request(
        "PATCH",
        f"/api/collections/{collection}/records/{record_id}",
        json_body=payload,
    )
    return _json(data)


@mcp.tool()
async def pb_delete_record(collection: str, record_id: str) -> str:
    """Delete a PocketBase record by collection and id."""
    if collection in {"tasks", "ingestion_jobs", "sources"}:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.delete(
                f"{POCKETBASE_URL}/api/collections/{collection}/records/{record_id}"
            )
            response.raise_for_status()
            return _json({"deleted": True, "collection": collection, "id": record_id})

    await _request("DELETE", f"/api/collections/{collection}/records/{record_id}")
    return _json({"deleted": True, "collection": collection, "id": record_id})


@mcp.tool()
async def pb_search_tasks(query: str, page: int = 1, per_page: int = 50) -> str:
    """Search tasks by title or description substring."""
    safe = query.replace('"', '\\"')
    filter_expr = f'title ~ "{safe}" || description ~ "{safe}"'
    return await pb_list_records("tasks", filter=filter_expr, page=page, per_page=per_page)


if __name__ == "__main__":
    mcp.run()
