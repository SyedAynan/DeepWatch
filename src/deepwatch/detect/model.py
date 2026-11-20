"""Baseline visual detector — Xception-style CNN backbone.

Milestone 1 bootstrap (per docs/DATASET_AND_EXPERIMENT_PLAN.md): we use a
pretrained backbone in the spirit of the UCF/Xception baselines that
DeepfakeBench implements. This module owns *model construction and loading*
only; preprocessing and scoring live in `pipeline.py` and `__init__`.

Two weight sources are supported, selected by `Detector.load`:
  * ``imagenet``     — torchvision/timm ImageNet weights. Honest bootstrap for
                       bring-up: produces a calibrated-shaped score with no
                       deepfake training, and is clearly labelled "backbone:
                       imagenet" in the audit log so it can never be mistaken
                       for a trained forensic result.
  * a checkpoint path — a DeepfakeBench/UCF Xception ``.pth``/``ckpt`` file the
                       user downloads. When present it is preferred.

Every load records the resolved weight source + SHA-256 so results are
reproducible (NFR-06); a checkpoint's hash is logged, never assumed.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Torch/timm are heavy imports done lazily inside ``load`` so that importing
# this module (e.g. for --help or the non-ML tests) stays fast and works on a
# machine where torch is still syncing.

DEFAULT_BACKBONE = "xception"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


@dataclass
class Detector:
    """A loaded binary real/fake classifier.

    Attributes
    ----------
    backbone:
        timm/torchvision architecture name (e.g. ``xception``).
    weight_source:
        ``"imagenet"`` or the checkpoint path the weights came from.
    weight_sha256:
        SHA-256 of the checkpoint file, or ``None`` for stock imagenet weights.
    device:
        ``"cuda"`` / ``"cpu"`` actually in use (never assumed — resolved).
    _model:
        The torch module (populated by ``load``).
    """

    backbone: str = DEFAULT_BACKBONE
    weight_source: str = "imagenet"
    weight_sha256: str | None = None
    device: str = "cpu"
    _model: Any = field(default=None, repr=False)

    @property
    def version_label(self) -> str:
        """Short identifier stored in the audit log's model_versions."""
        h = (self.weight_sha256 or "none")[:12]
        return f"{self.backbone}:{self.weight_source}:{h}"

    def load(self, device: str | None = None) -> Detector:
        """Build the model, load weights, move to device. Returns self."""
        import timm  # noqa: F401  (import kept explicit for error clarity)
        import torch

        model = _build_backbone(self.backbone, pretrained=(self.weight_source == "imagenet"))
        if self.weight_source != "imagenet":
            ckpt = Path(self.weight_source)
            if not ckpt.is_file():
                raise FileNotFoundError(f"detector checkpoint not found: {ckpt}")
            self.weight_sha256 = _sha256(ckpt)
            _load_checkpoint(model, ckpt)
        resolved = device or ("cuda" if torch.cuda.is_available() else "cpu")
        model.to(resolved).eval()
        self.device = resolved
        self._model = model
        return self

    def is_loaded(self) -> bool:
        return self._model is not None


def _build_backbone(backbone: str, pretrained: bool) -> Any:
    """Return a binary-head `backbone` model.

    Defaults to timm's ``xception`` (the DeepfakeBench/UCF backbone); any other
    timm architecture name works via ``Detector(backbone=...)``. Binary head =
    a single-logit layer scored with a sigmoid in the pipeline.
    """
    import timm

    try:
        return timm.create_model(
            backbone,
            pretrained=pretrained,
            num_classes=1,  # single logit -> sigmoid = P(fake)
        )
    except Exception as exc:
        raise RuntimeError(
            f"timm could not build {backbone!r}. Check timm version or pick a "
            "different backbone via Detector(backbone=...)."
        ) from exc


def _load_checkpoint(model: Any, ckpt_path: Path) -> None:
    """Load a DeepfakeBench/UCF state dict onto the model (best-effort).

    DeepfakeBench checkpoints come in a few shapes (raw state_dict, or wrapped
    under 'state_dict'/'model'). We try a strict load first, then fall back to
    matching intersecting keys so a backbone checkpoint still loads onto our
    binary head.
    """
    import torch

    blob = torch.load(ckpt_path, map_location="cpu")
    sd = blob
    for key in ("state_dict", "model", "model_state_dict"):
        if isinstance(blob, dict) and key in blob and isinstance(blob[key], dict):
            sd = blob[key]
            break
    if not isinstance(sd, dict):  # pragma: no cover
        raise RuntimeError(f"unrecognised checkpoint format: {ckpt_path}")

    cleaned = {k.replace("module.", "", 1): v for k, v in sd.items()}
    try:
        model.load_state_dict(cleaned, strict=True)
        return
    except RuntimeError:
        pass
    result = model.load_state_dict(cleaned, strict=False)
    # If nearly nothing matched, the checkpoint is probably a different arch.
    n_loaded = len(set(cleaned) - set(result.unexpected_keys))
    if n_loaded < len(list(model.state_dict())) * 0.5:  # pragma: no cover
        raise RuntimeError(
            f"checkpoint {ckpt_path.name} shares <50% keys with {type(model).__name__}; "
            "wrong backbone?"
        )
