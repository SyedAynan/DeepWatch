"""DeepWatch command-line interface.

Currently implements the ingest path (Milestone 0): preserve the upload,
hash it, open an analysis run, and log the ingest event. Detection and
fusion arrive in later milestones — every step is recorded, never invented.
"""

from __future__ import annotations

import argparse
import json
import sys

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


def cmd_detect(path: str, db: str, checkpoint: str | None) -> int:
    """Ingest a file, run the baseline detector, log the score."""
    from .detect.model import Detector
    from .detect.pipeline import score_media

    conn = audit.connect(db)
    meta = preserve.preserve(path)
    evidence_id = _register_evidence(conn, meta)
    det = Detector(
        weight_source=checkpoint if checkpoint else "imagenet",
    ).load()
    run_id = audit.create_run(
        conn,
        evidence_id,
        model_versions={"detector": det.version_label, "audio": "none-m0"},
    )
    audit.append_event(conn, run_id, "ingest", meta)
    ms = score_media(det, meta["original_path"])
    detail = {
        "visual_score": ms.score,
        "media_type": ms.media_type,
        "frames_scored": ms.frames_scored,
        "faces_found": ms.faces_found,
    }
    audit.append_event(conn, run_id, "detect", detail)
    out = {
        "run_id": run_id,
        "evidence": meta,
        "visual_score": ms.score,
        "media_type": ms.media_type,
        "frames_scored": ms.frames_scored,
        "detector": det.version_label,
        "device": det.device,
    }
    print(json.dumps(out, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="deepwatch", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_ing = sub.add_parser("ingest", help="Preserve + hash a media file")
    p_ing.add_argument("file")
    p_ing.add_argument("--db", default=str(audit.DEFAULT_DB))

    p_det = sub.add_parser("detect", help="Ingest + run baseline detector")
    p_det.add_argument("file")
    p_det.add_argument("--db", default=str(audit.DEFAULT_DB))
    p_det.add_argument(
        "--checkpoint", default=None, help="model .pth; omit = imagenet (sanity only)"
    )
    args = ap.parse_args(argv)

    try:
        if args.cmd == "ingest":
            return cmd_ingest(args.file, args.db)
        if args.cmd == "detect":
            return cmd_detect(args.file, args.db, args.checkpoint)
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
