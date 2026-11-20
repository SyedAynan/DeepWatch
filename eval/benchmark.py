"""Benchmark evaluation — AUC / EER / separated FP-FN over a dataset manifest.

Phase-1 honesty rules (docs/DATASET_AND_EXPERIMENT_PLAN.md §3-4): report AUC,
EER, accuracy, and **false-positives and false-negatives separately** — never a
collapsed single figure. Every run can write into the append-only audit log so
a printed number is traceable to a run id.

Usage:
    uv run python eval/benchmark.py --dataset data/datasets/<name> \
        [--checkpoint models/<ckpt>.pth] [--limit N] [--db data/analysis_log.db]

With no --checkpoint it uses ImageNet weights — clearly labelled, valid only as
a pipeline sanity check, never reported as a forensic result.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Make ``src/`` importable when run as a plain script (``python eval/...``).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def _labels_scores(
    samples: list[dict], det, limit: int | None
) -> tuple[list[int], list[float], list[dict]]:
    from deepwatch.detect.pipeline import score_media

    y_true: list[int] = []
    y_score: list[float] = []
    rows: list[dict] = []
    usable = [s for s in samples if s["label"] in ("real", "fake")]
    if limit:
        usable = usable[:limit]
    for s in usable:
        try:
            ms = score_media(det, s["path"])
        except Exception as e:
            rows.append({"path": s["path"], "label": s["label"], "error": str(e)})
            continue
        y = 1 if s["label"] == "fake" else 0
        y_true.append(y)
        y_score.append(ms.score)
        rows.append({"path": s["path"], "label": s["label"], "score": ms.score})
    return y_true, y_score, rows


def _metrics(y_true: list[int], y_score: list[float]) -> dict:
    import numpy as np
    from sklearn.metrics import average_precision_score, roc_auc_score

    if len(set(y_true)) < 2:
        return {"error": "need both real and fake samples for AUC"}
    yt, ys = np.array(y_true), np.array(y_score)
    auc = float(roc_auc_score(yt, ys))
    ap = float(average_precision_score(yt, ys))
    pred = (ys >= 0.5).astype(int)
    fp = int(((pred == 1) & (yt == 0)).sum())
    fn = int(((pred == 0) & (yt == 1)).sum())
    tn = int(((pred == 0) & (yt == 0)).sum())
    tp = int(((pred == 1) & (yt == 1)).sum())
    fpr = fp / max(fp + tn, 1)
    fnr = fn / max(fn + tp, 1)
    return {
        "n": len(yt),
        "n_real": int((yt == 0).sum()),
        "n_fake": int((yt == 1).sum()),
        "auc": round(auc, 4),
        "ap": round(ap, 4),
        "accuracy": round(float((pred == yt).mean()), 4),
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "tp": tp,
        "fpr": round(fpr, 4),
        "fnr": round(fnr, 4),
        # NOT a true EER (which sweeps thresholds): balanced error AT threshold
        # 0.5. Full threshold-swept EER + ROC are a Phase-4 addition.
        "balanced_error@0.5": round((fpr + fnr) / 2, 4),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", required=True, help="dataset root (folder markers or manifest)")
    ap.add_argument("--checkpoint", default=None, help="model .pth; omit = imagenet (sanity only)")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--db", default=None, help="write run to this audit db (optional)")
    ap.add_argument("--out", default=None, help="write per-sample JSON here")
    args = ap.parse_args(argv)

    from deepwatch.db import audit
    from deepwatch.detect.model import Detector
    from deepwatch.ingest import datasets

    samples = datasets.scan(args.dataset)
    print(f"manifest: {json.dumps(datasets.summarize(samples))}")

    det = Detector(
        weight_source=args.checkpoint if args.checkpoint else "imagenet",
    ).load()
    print(f"detector: {det.version_label} on {det.device}")
    if det.weight_source == "imagenet":
        print("NOTE: imagenet weights — pipeline sanity check only, not a forensic result")

    y_true, y_score, rows = _labels_scores(samples, det, args.limit)
    m = _metrics(y_true, y_score)
    print("metrics:", json.dumps(m, indent=2))

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps({"metrics": m, "samples": rows}, indent=2))
        print(f"wrote per-sample results -> {args.out}")

    if args.db:
        conn = audit.connect(args.db)
        run_id = audit.create_run(
            conn,
            evidence_id=0 if _has_evidence_zero(conn) else _ensure_system_evidence(conn),
            model_versions={"detector": det.version_label},
        )
        audit.append_event(conn, run_id, "detect", {"dataset": args.dataset, "metrics": m})
        print(f"logged eval run {run_id} -> {args.db}")
    return 0 if "error" not in m else 2


def _has_evidence_zero(conn) -> bool:
    return conn.execute("SELECT 1 FROM evidence_item WHERE id=0").fetchone() is not None


def _ensure_system_evidence(conn) -> int:
    """A sentinel evidence row so eval runs (not tied to one upload) still log."""
    conn.execute(
        "INSERT OR IGNORE INTO evidence_item (id, sha256, original_path, media_type, filename, byte_size, ingested_at)"
        " VALUES (0, 'eval-dataset', 'dataset', 'dataset', 'benchmark', 0, 'system')"
    )
    conn.commit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
