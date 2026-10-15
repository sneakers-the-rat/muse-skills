#!/usr/bin/env python3
"""Deterministic local XLSX extraction pipeline for the documents skill.

Outputs:
- manifest.json
- rows.jsonl
- chunks.jsonl
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable


def normalize_cell_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        text = format(value, "g")
    else:
        text = str(value)
    text = text.replace("\x00", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_sheet_names(raw: str) -> list[str]:
    out: list[str] = []
    for token in raw.split(","):
        value = token.strip()
        if value and value not in out:
            out.append(value)
    return out


def iter_chunks(rows: list[dict], chunk_chars: int, overlap_chars: int) -> Iterable[dict]:
    chunk_id = 1
    i = 0
    while i < len(rows):
        sheet_name = rows[i]["sheet"]
        start_row = rows[i]["row_index"]
        buf: list[str] = []
        end_row = start_row
        char_count = 0
        j = i
        while j < len(rows):
            if rows[j]["sheet"] != sheet_name and buf:
                break
            row_text = rows[j]["text"]
            extra = len(row_text) + (1 if buf else 0)
            if buf and char_count + extra > chunk_chars:
                break
            if buf:
                buf.append("\n")
            buf.append(row_text)
            char_count += extra
            end_row = rows[j]["row_index"]
            j += 1

        text = "".join(buf).strip()
        if text:
            yield {
                "chunk_id": chunk_id,
                "sheet": sheet_name,
                "start_row": start_row,
                "end_row": end_row,
                "char_count": len(text),
                "text": text,
            }
            chunk_id += 1

        if j >= len(rows):
            break

        if overlap_chars <= 0:
            i = j
            continue

        rewind = 0
        k = j - 1
        while k >= i and rewind < overlap_chars and rows[k]["sheet"] == sheet_name:
            rewind += len(rows[k]["text"])
            k -= 1
        i = max(i + 1, k + 1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract deterministic text from XLSX files.")
    parser.add_argument("--input", required=True, help="XLSX path")
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument(
        "--sheet-names",
        default="",
        help="Optional comma-separated sheet names to include",
    )
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=3000,
        help="Approximate max chars per text chunk (default: 3000)",
    )
    parser.add_argument(
        "--overlap-chars",
        type=int,
        default=250,
        help="Approximate chunk overlap in chars (default: 250)",
    )
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"error: input does not exist: {input_path}", file=sys.stderr)
        return 2
    if input_path.suffix.lower() != ".xlsx":
        print(f"error: input is not a .xlsx file: {input_path}", file=sys.stderr)
        return 2

    try:
        import openpyxl  # type: ignore
    except Exception as exc:  # pragma: no cover
        print(f"error: openpyxl import failed: {exc}", file=sys.stderr)
        return 2

    workbook = openpyxl.load_workbook(
        filename=str(input_path),
        read_only=True,
        data_only=True,
    )

    requested_sheets = parse_sheet_names(args.sheet_names)
    available_sheet_names = [ws.title for ws in workbook.worksheets]
    if requested_sheets:
        sheet_names = [name for name in requested_sheets if name in available_sheet_names]
    else:
        sheet_names = available_sheet_names

    rows: list[dict] = []
    sheet_summaries: list[dict] = []
    for worksheet in workbook.worksheets:
        if worksheet.title not in sheet_names:
            continue
        non_empty_rows = 0
        for row_index, row in enumerate(worksheet.iter_rows(values_only=True), start=1):
            values = [normalize_cell_value(cell) for cell in row]
            values = [value for value in values if value]
            if not values:
                continue
            text = " | ".join(values)
            rows.append(
                {
                    "sheet": worksheet.title,
                    "row_index": row_index,
                    "non_empty_cells": len(values),
                    "char_count": len(text),
                    "values": values,
                    "text": text,
                }
            )
            non_empty_rows += 1
        sheet_summaries.append(
            {
                "sheet": worksheet.title,
                "non_empty_rows": non_empty_rows,
            }
        )

    chunks = list(iter_chunks(rows, args.chunk_chars, args.overlap_chars))

    with (outdir / "rows.jsonl").open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    with (outdir / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for row in chunks:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    total_chars = sum(row["char_count"] for row in rows)
    manifest = {
        "input_path": str(input_path),
        "output_dir": str(outdir),
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "file_size_bytes": os.path.getsize(input_path),
        "sheet_count": len(sheet_summaries),
        "requested_sheet_names": requested_sheets,
        "included_sheet_names": sheet_names,
        "missing_requested_sheets": [
            name for name in requested_sheets if name not in available_sheet_names
        ],
        "non_empty_row_count": len(rows),
        "total_text_chars": total_chars,
        "chunk_count": len(chunks),
        "chunk_chars": args.chunk_chars,
        "overlap_chars": args.overlap_chars,
        "sheets": sheet_summaries,
    }

    with (outdir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
