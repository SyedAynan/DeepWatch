"""Dataset bootstrap — manifest loader for DeepWatch evaluation.

Phase-1 strategy (per docs/DATASET_AND_EXPERIMENT_PLAN.md): FaceForensics++ is
gated (~1 week form), so we bootstrap on openly available sets first —
DeepfakeBench preprocessed packs, DFDC preview, and Celeb-DF. This module reads
a directory of media into a manifest of (path, label) pairs that the eval
harness consumes. Labels come from folder names (`real`/`fake` or per-method
subfolders) or an optional CSV/JSON manifest if the dataset ships one.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

MEDIA_EXTS = {
    "image": {".png", ".jpg", ".jpeg", ".webp", ".bmp"},
    "video": {".mp4", ".mov", ".avi", ".mkv", ".webm"},
    "audio": {".wav", ".mp3", ".flac", ".ogg", ".m4a"},
}

# folder-name fragments that mark a sample as manipulated vs authentic
FAKE_MARKERS = {"fake", "fakes", "manipulated", "deepfake", "deepfakes",
                "face2face", "faceswap", "neuraltextures", "faceshifter",
                "deepfakedetection", "forged", "synthetic", "generated"}
REAL_MARKERS = {"real", "original", "originals", "bonafide", "bona_fide",
                "authentic", "youtube", "pristine"}


def _label_from_parts(path: Path) -> str | None:
    parts = {p.lower() for p in path.parts}
    if parts & FAKE_MARKERS:
        return "fake"
    if parts & REAL_MARKERS:
        return "real"
    return None


def scan(root: str | Path, exts: set[str] | None = None) -> list[dict]:
    """Walk `root` and return [{path, label, media_type}] for known media.

    If a `manifest.csv`/`manifest.json` with a `label` column exists at the
    root it takes precedence; otherwise labels come from folder markers.
    """
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"dataset root not found: {root}")

    exts = exts or set().union(*MEDIA_EXTS.values())
    samples: list[dict] = []

    csv_manifest = root / "manifest.csv"
    json_manifest = root / "manifest.json"
    if csv_manifest.is_file():
        with csv_manifest.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                p = root / row["path"]
                lab = row.get("label", "").strip().lower()
                samples.append({
                    "path": str(p), "label": lab or _label_from_parts(p) or "unknown",
                    "media_type": _media_type(p.suffix)})
        return samples
    if json_manifest.is_file():
        data = json.loads(json_manifest.read_text(encoding="utf-8"))
        for row in data:
            p = root / row["path"]
            lab = str(row.get("label", "")).strip().lower()
            samples.append({
                "path": str(p), "label": lab or _label_from_parts(p) or "unknown",
                "media_type": _media_type(p.suffix)})
        return samples

    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in exts:
            samples.append({
                "path": str(p),
                "label": _label_from_parts(p) or "unknown",
                "media_type": _media_type(p.suffix)})
    return samples


def _media_type(suffix: str) -> str:
    s = suffix.lower()
    for kind, exts in MEDIA_EXTS.items():
        if s in exts:
            return kind
    return "unknown"


def summarize(samples: list[dict]) -> dict:
    """Return label/type counts — used by the eval harness and docs."""
    out: dict[str, int] = {}
    for s in samples:
        key = f"{s['media_type']}:{s['label']}"
        out[key] = out.get(key, 0) + 1
    return out
