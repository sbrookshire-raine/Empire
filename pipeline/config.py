"""Shared configuration for the stub ingestion pipeline."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOCK_DATA_DIR = ROOT / "mock_data_ingest"
COGNEE_ENV = ROOT / "cognee" / ".env"

POCKETBASE_URL = os.getenv("POCKETBASE_URL", "http://127.0.0.1:8090").rstrip("/")

ALLOWED_SUFFIXES = {".json", ".md"}
