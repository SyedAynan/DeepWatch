"""Scoring pipeline — media file to manipulation probability.

Takes a preserved media file (image or video), extracts the region the
baseline operates on (largest detected face, else a centre crop), runs the
``Detector`` and returns P(fake) per input. Videos are scored on a uniform
sample of frames and aggregated — per-frame scores are returned too so the
eval harness can compute frame-level metrics the base papers report.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from .model import Detector

if TYPE_CHECKING:
    import torch

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}

DEFAULT_FRAMES_PER_VIDEO = 8  # uniform sample; small enough for CPU fallback


@dataclass
class MediaScore:
    """Result of scoring one media file."""

    score: float  # aggregated P(fake)
    media_type: str  # image | video
    frames_scored: int  # 1 for images
    frame_scores: list[float]  # per-frame scores (len == frames_scored)
    faces_found: int  # frames where a face crop was used


def score_media(
    det: Detector,
    path: str | Path,
    frames_per_video: int = DEFAULT_FRAMES_PER_VIDEO,
) -> MediaScore:
    """Score an image or video file. Raises FileNotFoundError/ValueError."""
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"media not found: {p}")
    ext = p.suffix.lower()
    if ext in IMAGE_EXTS:
        score, face = _score_image_file(det, p)
        return MediaScore(score, "image", 1, [score], int(face))
    if ext in VIDEO_EXTS:
        return _score_video_file(det, p, frames_per_video)
    raise ValueError(f"unsupported media type for detection: {ext}")


# ---------------------------------------------------------------- internals


def _preprocess(det: Detector, bgr_or_rgb: np.ndarray) -> torch.Tensor:
    """HWC uint8 RGB image -> normalised CHW float tensor for the backbone.

    Reads input size + normalisation from the model's ``default_cfg`` so a
    non-Xception backbone still gets its correct stats; falls back to the
    tf-style [-1, 1] scaling Xception checkpoints were trained with.
    """
    import cv2
    import torch

    cfg = getattr(det._model, "default_cfg", {}) or {}
    size = int(cfg.get("input_size", (3, 299, 299))[-1])
    mean = np.array(cfg.get("mean", (0.5, 0.5, 0.5)), dtype=np.float32)
    std = np.array(cfg.get("std", (0.5, 0.5, 0.5)), dtype=np.float32)

    img = cv2.resize(bgr_or_rgb, (size, size), interpolation=cv2.INTER_LINEAR)
    x = img.astype(np.float32) / 255.0
    x = (x - mean) / std
    return torch.from_numpy(x.transpose(2, 0, 1)).unsqueeze(0)


def _face_crop(bgr: np.ndarray) -> tuple[np.ndarray, bool]:
    """Return (crop, found). Largest Haar face with margin; else centre square.

    Haar cascades ship inside opencv-python — no extra model download. This is
    a bootstrap-quality face finder, not the final MTCNN/RetinaFace aligner;
    that upgrade is tracked for Phase 2+.
    """
    import cv2
    import cv2.data  # explicit submodule import — pyright doesn't see the lazy attr

    h, w = bgr.shape[:2]
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    if len(faces):
        x, y, fw, fh = max(faces, key=lambda r: r[2] * r[3])
        m = int(0.25 * max(fw, fh))  # context margin — detectors need it
        x0, y0 = max(0, x - m), max(0, y - m)
        x1, y1 = min(w, x + fw + m), min(h, y + fh + m)
        return cv2.cvtColor(bgr[y0:y1, x0:x1], cv2.COLOR_BGR2RGB), True
    side = min(h, w)
    cy, cx = (h - side) // 2, (w - side) // 2
    return cv2.cvtColor(bgr[cy : cy + side, cx : cx + side], cv2.COLOR_BGR2RGB), False


def _score_rgb(det: Detector, rgb: np.ndarray) -> float:
    import torch

    assert det._model is not None, "Detector.load() must run before scoring"
    x = _preprocess(det, rgb).to(det.device)
    with torch.no_grad():
        logit = det._model(x).reshape(-1)[0]
    return float(torch.sigmoid(logit).item())


def _score_image_file(det: Detector, path: Path) -> tuple[float, bool]:
    import cv2

    bgr = cv2.imread(str(path))
    if bgr is None:
        raise ValueError(f"unreadable image: {path}")
    rgb, face = _face_crop(bgr)
    return _score_rgb(det, rgb), face


def _score_video_file(det: Detector, path: Path, n: int) -> MediaScore:
    import cv2

    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise ValueError(f"unreadable video: {path}")
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 1
    idxs = np.linspace(0, max(total - 1, 0), min(n, total)).astype(int)
    scores: list[float] = []
    faces = 0
    for i in idxs:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(i))
        ok, frame = cap.read()
        if not ok:
            continue
        rgb, face = _face_crop(frame)
        faces += int(face)
        scores.append(_score_rgb(det, rgb))
    cap.release()
    if not scores:
        raise ValueError(f"no decodable frames in video: {path}")
    return MediaScore(
        score=float(np.mean(scores)),
        media_type="video",
        frames_scored=len(scores),
        frame_scores=scores,
        faces_found=faces,
    )
