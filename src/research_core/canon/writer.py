from __future__ import annotations

from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from research_core.util.hashing import canonical_table_sha256, sha256_file


def canonical_arrow_schema(keep_updown: bool) -> pa.Schema:
    fields = [
        pa.field("ts", pa.timestamp("ns", tz="America/New_York"), nullable=False),
        pa.field("instrument", pa.string(), nullable=False),
        pa.field("tf", pa.string(), nullable=False),
        pa.field("open", pa.float64(), nullable=False),
        pa.field("high", pa.float64(), nullable=False),
        pa.field("low", pa.float64(), nullable=False),
        pa.field("close", pa.float64(), nullable=False),
        pa.field("volume", pa.float64(), nullable=False),
    ]
    if keep_updown:
        fields.extend(
            [
                pa.field("up", pa.float64(), nullable=False),
                pa.field("down", pa.float64(), nullable=False),
            ]
        )
    return pa.schema(fields)


def write_canon_parquet(df: pd.DataFrame, output_path: Path, keep_updown: bool) -> dict[str, str | int]:
    schema = canonical_arrow_schema(keep_updown=keep_updown)
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    pq.write_table(table, output_path, compression="snappy", use_dictionary=False)

    return {
        "parquet_bytes_sha256": sha256_file(output_path),
        "canonical_table_sha256": canonical_table_sha256(table),
        "bytes": output_path.stat().st_size,
    }
