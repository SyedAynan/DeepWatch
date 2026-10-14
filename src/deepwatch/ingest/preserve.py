"""Evidence preservation — store an immutable copy of each upload.

The original is copied verbatim into data/evidence/<sha256>.<ext> so that
analysis always runs on a copy and the pristine input is retained for
re-examination. Never mutate the preserved file.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from .hasher import sha256_file

EVIDENCE_DIR = Path("data/evidence")


def preserve(source: str | Path, evidence_dir: Path = EVIDENCE_DIR) -> dict:
    """Copy `source` into the evidence store keyed by its SHA-256.

    Returns a dict with the evidence hash, stored path, size, and media kind.
    Idempotent: re-uploading the same content returns the existing record.
    """
    src = Path(source)
    if not src.is_file():
        raise FileNotFoundError(f"upload not found: {src}")

    digest = sha256_file(src)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    dest = evidence_dir / f"{digest}{src.suffix.lower()}"
    if not dest.exists():
        shutil.copy2(src, dest)  # copy2 preserves metadata (immutable input)

    return {
        "sha256": digest,
        "original_path": str(dest),
        "byte_size": dest.stat().st_size,
        "media_type": _media_type(dest.suffix),
        "filename": src.name,
    }


def _media_type(suffix: str) -> str:
    s = suffix.lower()
    if s in {".png", ".jpg", ".jpeg", ".webp", ".bmp"}:
        return "image"
    if s in {".mp4", ".mov", ".avi", ".mkv", ".webm"}:
        return "video"
    if s in {".wav", ".mp3", ".flac", ".ogg", ".m4a"}:
        return "audio"
    return "unknown"
