"""Structured-event arXiv metadata scavenger."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import deque
from pathlib import Path
from typing import Any

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ambient_events import event_text, parse_event, research_triggered

ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = Path(os.environ.get("EMPIRE_AUDIT_LOG", ROOT / "eve-audit" / "active_chat.log"))
CATALOG_DB = Path(os.environ.get("EMPIRE_CATALOG_DB", ROOT / "config" / "eve-capabilities" / "catalog.db"))
OLLAMA_URL = os.environ.get("EMPIRE_OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/") + "/api/generate"
# `llama3:8b` is not an installed tag, so this worker never completed a cycle either (found
# 2026-09-24). Installed default + CPU pin, so a scavenge pass never evicts the chat model.
OLLAMA_MODEL = os.environ.get("EMPIRE_RESEARCH_MODEL", "qwen2.5:7b-instruct")
OLLAMA_OPTIONS = {"num_gpu": int(os.environ.get("EMPIRE_RESEARCH_NUM_GPU", "0"))}
MAX_REQUESTS_PER_HOUR = 15
ARXIV_URL = "https://export.arxiv.org/api/query"
REQUEST_TIMES: deque[float] = deque()


def extract_query(events: list[dict[str, Any]]) -> str:
    context = "\n".join(event_text(event)[:1500] for event in events[-5:])
    prompt = f"Return only a short arXiv search query, maximum 4 words.\n{context}"
    payload = json.dumps(
        {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False, "options": OLLAMA_OPTIONS}
    ).encode("utf-8")
    request = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    query = result.get("response", "").strip() if isinstance(result, dict) else ""
    if not query or len(query) > 120 or any(ord(char) < 32 for char in query):
        return ""
    words = query.split()
    return " ".join(words[:4])


def harvest(query: str, opener=urllib.request.urlopen) -> int:
    current_time = time.time()
    while REQUEST_TIMES and REQUEST_TIMES[0] <= current_time - 3600:
        REQUEST_TIMES.popleft()
    if len(REQUEST_TIMES) >= MAX_REQUESTS_PER_HOUR:
        return 0
    REQUEST_TIMES.append(current_time)
    encoded = urllib.parse.urlencode({"search_query": f"all:{query}", "start": 0, "max_results": 5})
    request = urllib.request.Request(f"{ARXIV_URL}?{encoded}", headers={"User-Agent": "EMPIRE-ResearchScavenger/1.0"})
    with opener(request, timeout=30) as response:
        root = ET.fromstring(response.read())
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    rows = []
    for entry in root.findall("atom:entry", namespace):
        identifier = (entry.findtext("atom:id", "", namespace) or "").strip()
        title = " ".join((entry.findtext("atom:title", "", namespace) or "").split())
        abstract = " ".join((entry.findtext("atom:summary", "", namespace) or "").split())
        if not identifier or not title or not abstract:
            continue
        authors = [name.text or "" for name in entry.findall("atom:author/atom:name", namespace)]
        pdf_url = f"https://arxiv.org/pdf/{identifier.rsplit('/', 1)[-1]}.pdf"
        digest = hashlib.sha256(f"{identifier}\n{title}\n{abstract}".encode()).hexdigest()
        rows.append((identifier, title, json.dumps(authors), entry.findtext("atom:published", "", namespace), entry.findtext("atom:updated", "", namespace), abstract, query, identifier, pdf_url, digest, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
    with sqlite3.connect(CATALOG_DB) as connection:
        connection.executemany(
            """
            INSERT INTO research_abstracts
            (id, title, authors, published_date, updated_date, abstract_summary, keywords,
             source_url, local_file_path, content_hash, retrieved_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET title=excluded.title, authors=excluded.authors,
              published_date=excluded.published_date, updated_date=excluded.updated_date,
              abstract_summary=excluded.abstract_summary, keywords=excluded.keywords,
              source_url=excluded.source_url, local_file_path=excluded.local_file_path,
              content_hash=excluded.content_hash, retrieved_at=excluded.retrieved_at
            """,
            rows,
        )
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    if args.once:
        if not LOG_PATH.exists():
            return 0
        events = []
        for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
            event = parse_event(line)
            if event:
                events.append(event)
        candidates = [event for event in events if research_triggered(event)]
        if candidates:
            query = extract_query(events)
            if query:
                harvest(query)
        return 0
    events: list[dict[str, Any]] = []
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.touch(exist_ok=True)
    with LOG_PATH.open("r", encoding="utf-8") as stream:
        stream.seek(0, os.SEEK_END)
        while True:
            line = stream.readline()
            if not line:
                time.sleep(1)
                continue
            event = parse_event(line)
            if not event:
                continue
            events.append(event)
            events = events[-10:]
            if research_triggered(event):
                query = extract_query(events)
                if query:
                    harvest(query)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())