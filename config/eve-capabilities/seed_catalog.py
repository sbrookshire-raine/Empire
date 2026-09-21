"""Build and update the local EMPIRE capability and research catalog."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB = ROOT / "config" / "eve-capabilities" / "catalog.db"
DEFAULT_SOURCE = ROOT / "UPGRADE" / "osint-catalog.json"

LOCAL_SKILLS = {
    "thought-map": ("local/thought-map", "read.document", "Analyze an explicitly supplied signed directed graph.", "eve-skills/thought-map/src/local_thought_map/__main__.py"),
    "scenario-regret": ("local/scenario-regret", "query.data", "Rank supplied options across scenarios using minimax regret.", "eve-skills/scenario-regret/src/local_scenario_regret/__main__.py"),
    "forecast-baseline": ("local/forecast-baseline", "query.data", "Produce transparent univariate forecast baselines.", "eve-skills/forecast-baseline/src/local_forecast_baseline/__main__.py"),
    "topology-audit": ("local/topology-audit", "read.document", "Analyze declared dependencies and outage propagation.", "eve-skills/topology-audit/src/local_topology_audit/__main__.py"),
    "bayes-update": ("local/bayes-update", "query.data", "Update finite categorical hypotheses from explicit priors and likelihoods.", "eve-skills/bayes-update/src/local_bayes_update/__main__.py"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    return connection


def migrate(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS repositories (
            id TEXT PRIMARY KEY, url TEXT, description TEXT NOT NULL, category TEXT,
            eve_capability TEXT, trust_domain TEXT, primary_language TEXT, license_type TEXT,
            has_mcp INTEGER, has_cli INTEGER, score_mcp INTEGER, score_local INTEGER,
            score_cli INTEGER, score_functional INTEGER, stars INTEGER, deployment_modes TEXT,
            provenance TEXT NOT NULL DEFAULT 'osint-catalog', last_analyzed_at TEXT, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS capabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_id TEXT NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
            capability_name TEXT NOT NULL, UNIQUE(repo_id, capability_name)
        );
        CREATE TABLE IF NOT EXISTS local_skills (
            skill_name TEXT PRIMARY KEY, repo_id TEXT NOT NULL UNIQUE REFERENCES repositories(id) ON DELETE CASCADE,
            manifest_path TEXT NOT NULL, entrypoint TEXT NOT NULL, policy_id TEXT NOT NULL,
            manifest_sha256 TEXT, status TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS research_abstracts (
            id TEXT PRIMARY KEY, title TEXT NOT NULL, authors TEXT NOT NULL DEFAULT '[]',
            published_date TEXT, updated_date TEXT, abstract_summary TEXT NOT NULL,
            keywords TEXT NOT NULL DEFAULT '', source_url TEXT NOT NULL, local_file_path TEXT,
            content_hash TEXT NOT NULL, retrieved_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS worker_checkpoints (
            worker_name TEXT PRIMARY KEY, source_identity TEXT NOT NULL DEFAULT '', byte_offset INTEGER NOT NULL DEFAULT 0,
            last_event_id TEXT NOT NULL DEFAULT '', last_event_hash TEXT NOT NULL DEFAULT '', updated_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_repositories_capability ON repositories(eve_capability);
        CREATE INDEX IF NOT EXISTS idx_repositories_description ON repositories(description);
        CREATE INDEX IF NOT EXISTS idx_capabilities_repo ON capabilities(repo_id);
        CREATE INDEX IF NOT EXISTS idx_research_search ON research_abstracts(title, keywords);
        """
    )
    connection.execute("INSERT OR IGNORE INTO schema_version(version, applied_at) VALUES (?, ?)", (1, utc_now()))


def upsert_repository(connection: sqlite3.Connection, repo: dict[str, Any], provenance: str) -> str:
    repo_id = str(repo.get("id") or "").strip()
    description = str(repo.get("description") or "").strip()
    if not repo_id or not description:
        return "rejected"
    existed = connection.execute("SELECT 1 FROM repositories WHERE id = ?", (repo_id,)).fetchone()
    values = (
        repo_id, repo.get("url"), description, repo.get("category"), repo.get("eve_capability"),
        repo.get("trust_domain"), repo.get("primary_language"), repo.get("license_type"),
        int(bool(repo.get("has_mcp"))), int(bool(repo.get("has_cli"))), repo.get("score_mcp"),
        repo.get("score_local"), repo.get("score_cli"), repo.get("score_functional"), repo.get("stars"),
        json.dumps(repo.get("deployment_modes") or [], sort_keys=True), provenance,
        repo.get("last_analyzed_at"), utc_now(),
    )
    connection.execute(
        """
        INSERT INTO repositories
        (id, url, description, category, eve_capability, trust_domain, primary_language, license_type,
         has_mcp, has_cli, score_mcp, score_local, score_cli, score_functional, stars,
         deployment_modes, provenance, last_analyzed_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          url=excluded.url, description=excluded.description, category=excluded.category,
          eve_capability=excluded.eve_capability, trust_domain=excluded.trust_domain,
          primary_language=excluded.primary_language, license_type=excluded.license_type,
          has_mcp=excluded.has_mcp, has_cli=excluded.has_cli, score_mcp=excluded.score_mcp,
          score_local=excluded.score_local, score_cli=excluded.score_cli,
          score_functional=excluded.score_functional, stars=excluded.stars,
          deployment_modes=excluded.deployment_modes, provenance=excluded.provenance,
          last_analyzed_at=excluded.last_analyzed_at, updated_at=excluded.updated_at
        """,
        values,
    )
    for capability in repo.get("capabilities") or []:
        connection.execute("INSERT OR IGNORE INTO capabilities(repo_id, capability_name) VALUES (?, ?)", (repo_id, str(capability)))
    return "updated" if existed else "inserted"


def seed(source: Path, target: Path) -> dict[str, int]:
    data = json.loads(source.read_text(encoding="utf-8"))
    repositories = data.get("repositories")
    if not isinstance(repositories, list):
        raise ValueError("Catalog JSON must contain a repositories array")
    counts = {"inserted": 0, "updated": 0, "rejected": 0}
    connection = connect(target)
    try:
        migrate(connection)
        for repo in repositories:
            counts[upsert_repository(connection, repo, "osint-catalog")] += 1
        for skill_name, (repo_id, capability, description, entrypoint) in LOCAL_SKILLS.items():
            upsert_repository(connection, {
                "id": repo_id, "description": description, "category": "AI Tool",
                "eve_capability": capability, "trust_domain": "Local Evidence", "primary_language": "Python",
                "has_cli": True, "score_local": 5, "score_cli": 5, "score_functional": 5,
                "deployment_modes": ["local_binary"],
            }, "local-skill")
            manifest = ROOT / "eve-skills" / skill_name / "SKILL.md"
            connection.execute(
                """
                INSERT INTO local_skills
                (skill_name, repo_id, manifest_path, entrypoint, policy_id, status, updated_at)
                VALUES (?, ?, ?, ?, ?, 'installed', ?)
                ON CONFLICT(skill_name) DO UPDATE SET
                  repo_id=excluded.repo_id, manifest_path=excluded.manifest_path,
                  entrypoint=excluded.entrypoint, policy_id=excluded.policy_id,
                  status=excluded.status, updated_at=excluded.updated_at
                """,
                (skill_name, repo_id, str(manifest.relative_to(ROOT)).replace("\\", "/"), entrypoint, skill_name.replace("-", "_"), utc_now()),
            )
        connection.commit()
    finally:
        connection.close()
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--database", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    print(json.dumps(seed(args.source, args.database)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())