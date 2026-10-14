"""Milestone-0 tests: hashing, preservation, and the audit log."""
from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path

from deepwatch.db import audit
from deepwatch.ingest import hasher, preserve


def test_sha256_file_and_bytes(tmp_path: Path):
    f = tmp_path / "a.bin"
    payload = b"deepwatch evidence payload" * 1000
    f.write_bytes(payload)
    assert hasher.sha256_file(f) == hashlib.sha256(payload).hexdigest()
    assert hasher.sha256_bytes(payload) == hashlib.sha256(payload).hexdigest()


def test_preserve_is_immutable_and_idempotent(tmp_path: Path):
    src = tmp_path / "clip.mp4"
    payload = b"fake video bytes" * 10_000
    src.write_bytes(payload)
    ev_dir = tmp_path / "evidence"

    m1 = preserve.preserve(src, ev_dir)
    m2 = preserve.preserve(src, ev_dir)

    assert m1["sha256"] == m2["sha256"]
    assert m1["media_type"] == "video"
    assert Path(m1["original_path"]).read_bytes() == payload
    assert len(list(ev_dir.iterdir())) == 1  # deduplicated by hash


def test_audit_log_is_append_only(tmp_path: Path):
    db = tmp_path / "log.db"
    conn = audit.connect(db)
    conn.execute(
        """INSERT INTO evidence_item
           (sha256, original_path, media_type, filename, byte_size, ingested_at)
           VALUES ('x', '/tmp/x', 'video', 'x', 1, 'now')"""
    )
    conn.commit()
    evidence_id = conn.execute("SELECT id FROM evidence_item").fetchone()[0]
    run_id = audit.create_run(conn, evidence_id, {"detector": "test"})
    audit.append_event(conn, run_id, "ingest", {"ok": True})
    audit.append_event(conn, run_id, "detect", {"score": 0.5})

    rows = conn.execute(
        "SELECT step FROM analysis_log WHERE run_id=? ORDER BY id", (run_id,)
    ).fetchall()
    assert [r[0] for r in rows] == ["ingest", "detect"]
    run = conn.execute(
        "SELECT status FROM analysis_run WHERE id=?", (run_id,)
    ).fetchone()
    assert run[0] == "queued"
