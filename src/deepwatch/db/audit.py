"""SQLite audit-log bootstrap and append-only event writer."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

SCHEMA_PATH = Path(__file__).with_name("schema.sql")
DEFAULT_DB = Path("data/analysis_log.db")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect(db_path: str | Path = DEFAULT_DB) -> sqlite3.Connection:
    """Open and initialise the local audit database."""
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.execute(
        "INSERT OR IGNORE INTO schema_version(version, applied_at) VALUES (?, ?)",
        (1, utc_now()),
    )
    conn.commit()
    return conn


def create_run(conn: sqlite3.Connection, evidence_id: int, model_versions: dict) -> str:
    """Create a queued analysis run and return its UUID."""
    run_id = str(uuid4())
    conn.execute(
        """INSERT INTO analysis_run
           (id, evidence_id, status, model_versions, started_at)
           VALUES (?, ?, 'queued', ?, ?)""",
        (run_id, evidence_id, json.dumps(model_versions, sort_keys=True), utc_now()),
    )
    conn.commit()
    return run_id


def append_event(conn: sqlite3.Connection, run_id: str, step: str, detail: dict) -> None:
    """Append one immutable analysis event. There is intentionally no update API."""
    conn.execute(
        "INSERT INTO analysis_log(run_id, step, detail, logged_at) VALUES (?, ?, ?, ?)",
        (run_id, step, json.dumps(detail, sort_keys=True), utc_now()),
    )
    conn.commit()
