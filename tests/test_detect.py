"""Detection pipeline tests — stub detector, no torch download required."""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np

from deepwatch.detect import pipeline


class _StubDet:
    """Mimics Detector: deterministic score from mean pixel — no torch needed."""

    device = "cpu"
    version_label = "stub:test"
    _model = object()  # truthy so _score_rgb guard passes

    def is_loaded(self):
        return True


def _make_img(path: Path, seed: int = 0, face_like: bool = False):
    rng = np.random.default_rng(seed)
    img = rng.integers(0, 255, (120, 120, 3), dtype=np.uint8)
    cv2.imwrite(str(path), img)


def _patch_score(monkeypatch, value: float):
    monkeypatch.setattr(pipeline, "_score_rgb", lambda det, rgb: value)


def test_score_image_returns_score(monkeypatch, tmp_path: Path):
    img = tmp_path / "a.png"
    _make_img(img)
    _patch_score(monkeypatch, 0.7)
    ms = pipeline.score_media(_StubDet(), img)
    assert ms.media_type == "image"
    assert ms.frames_scored == 1
    assert ms.score == 0.7


def test_score_video_aggregates_frames(monkeypatch, tmp_path: Path):
    # 10-frame solid video
    vid = tmp_path / "v.mp4"
    writer = cv2.VideoWriter(str(vid), cv2.VideoWriter_fourcc(*"mp4v"), 5, (64, 64))
    for _ in range(10):
        writer.write(np.full((64, 64, 3), 128, np.uint8))
    writer.release()
    _patch_score(monkeypatch, 0.5)
    ms = pipeline.score_media(_StubDet(), vid, frames_per_video=4)
    assert ms.media_type == "video"
    assert 1 <= ms.frames_scored <= 4
    assert len(ms.frame_scores) == ms.frames_scored
    assert ms.score == 0.5


def test_score_missing_file(tmp_path: Path):
    try:
        pipeline.score_media(_StubDet(), tmp_path / "nope.png")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("expected FileNotFoundError")


def test_unsupported_ext(tmp_path: Path):
    f = tmp_path / "x.txt"
    f.write_text("hi")
    try:
        pipeline.score_media(_StubDet(), f)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_metrics_shapes():
    from eval.benchmark import _metrics

    y_true = [0, 0, 1, 1]
    y_score = [0.1, 0.4, 0.6, 0.9]
    m = _metrics(y_true, y_score)
    assert m["auc"] == 1.0
    assert m["fp"] == 0 and m["fn"] == 0
    assert m["tp"] == 2 and m["tn"] == 2


def test_metrics_degenerate_single_class():
    from eval.benchmark import _metrics

    m = _metrics([0, 0, 0], [0.1, 0.2, 0.3])
    assert "error" in m
