from __future__ import annotations

import hashlib
import io
from pathlib import Path

import pyarrow as pa

from research_core.util.io import canonical_json_bytes


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def sha256_json(payload: dict) -> str:
    return sha256_bytes(canonical_json_bytes(payload))


def canonical_table_sha256(table: pa.Table) -> str:
    sink = io.BytesIO()
    with pa.ipc.new_stream(sink, table.schema) as writer:
        writer.write_table(table)
    return sha256_bytes(sink.getvalue())
