"""Evidence hashing utilities.

Computes SHA-256 over uploaded media before any analysis. The hash is the
evidence's integrity anchor — any tampering after ingest changes it.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

_CHUNK = 1024 * 1024  # 1 MiB


def sha256_file(path: str | Path) -> str:
    """Return the hex SHA-256 digest of a file, read in chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(_CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    """Return the hex SHA-256 digest of an in-memory byte string."""
    return hashlib.sha256(data).hexdigest()
