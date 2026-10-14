"""DeepWatch command-line interface.

Currently implements the ingest path (Milestone 0): preserve the upload,
hash it, open an analysis run, and log the ingest event. Detection and
fusion arrive in later milestones — every step is recorded, never invented.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .db import audit
from .ingest import preserve


def _register_evidence(conn, meta: dict) -> int:
    """Insert the evidence row if new and return its id."""
    conn.execute(
        """INSERT OR IGNORE INTO evidence_item
           (sha256, original_path, media_type, filename, byte_size, ingested_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            meta["sha256"],
            meta["original_path"],
            meta["media_type"],
            meta["filename"],
            meta["byte_size"],
            audit.utc_now(),
        ),
    )
    conn.commit()
    row = conn.execute(
        "SELECT id FROM evidence_item WHERE sha256 = ?", (meta["sha256"],)
    ).fetchone()
    return int(row[0])


def cmd_ingest(path: str, db: str) -> int:
    conn = audit.connect(db)
    meta = preserve.preserve(path)
    evidence_id = _register_evidence(conn, meta)
    run_id = audit.create_run(
        conn,
        evidence_id,
        model_versions={"detector": "none-m0", "audio": "none-m0"},
    )
    audit.append_event(conn, run_id, "ingest", meta)
    out = {"run_id": run_id, "evidence": meta}
    print(json.dumps(out, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="deepwatch", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_ing = sub.add_parser("ingest", help="Preserve + hash a media file")
    p_ing.add_argument("file")
    p_ing.add_argument("--db", default=str(audit.DEFAULT_DB))
    args = ap.parse_args(argv)

    if args.cmd == "ingest":
        try:
            return cmd_ingest(args.file, args.db)
        except FileNotFoundError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
