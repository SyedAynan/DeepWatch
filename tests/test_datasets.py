"""Tests for the dataset manifest loader."""
from __future__ import annotations

import json
from pathlib import Path

from deepwatch.ingest import datasets


def _touch(p: Path, payload: bytes = b"x"):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(payload)


def test_scan_uses_folder_markers(tmp_path: Path):
    _touch(tmp_path / "original" / "a.png")
    _touch(tmp_path / "deepfakes" / "b.png")
    _touch(tmp_path / "DeepFakeDetection" / "c.mp4")
    _touch(tmp_path / "youtube" / "d.mp4")
    samples = datasets.scan(tmp_path)
    lab = {Path(s["path"]).name: s["label"] for s in samples}
    assert lab["a.png"] == "real"
    assert lab["b.png"] == "fake"
    assert lab["c.mp4"] == "fake"
    assert lab["d.mp4"] == "real"


def test_scan_manifest_csv_takes_precedence(tmp_path: Path):
    _touch(tmp_path / "clips" / "x.mp4")
    _touch(tmp_path / "clips" / "y.mp4")
    (tmp_path / "manifest.csv").write_text(
        "path,label\nclips/x.mp4,fake\nclips/y.mp4,real\n", encoding="utf-8")
    samples = datasets.scan(tmp_path)
    lab = {Path(s["path"]).name: s["label"] for s in samples}
    assert lab == {"x.mp4": "fake", "y.mp4": "real"}


def test_scan_manifest_json(tmp_path: Path):
    _touch(tmp_path / "m" / "z.png")
    (tmp_path / "manifest.json").write_text(
        json.dumps([{"path": "m/z.png", "label": "fake"}]), encoding="utf-8")
    samples = datasets.scan(tmp_path)
    assert samples[0]["label"] == "fake"


def test_summarize_counts(tmp_path: Path):
    _touch(tmp_path / "real" / "r1.png")
    _touch(tmp_path / "fake" / "f1.png")
    _touch(tmp_path / "fake" / "f2.png")
    s = datasets.scan(tmp_path)
    sm = datasets.summarize(s)
    assert sm["image:fake"] == 2 and sm["image:real"] == 1


def test_scan_missing_root(tmp_path: Path):
    try:
        datasets.scan(tmp_path / "nope")
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("expected FileNotFoundError")
