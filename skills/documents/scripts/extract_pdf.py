#!/usr/bin/env python3
"""Deterministic local PDF extraction pipeline for the documents skill.

Outputs:
- manifest.json
- pages.jsonl
- chunks.jsonl
- renders/page-XXXX.png (optional)
- render_index.json (optional)
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


def parse_page_ranges(raw: str, page_count: int) -> list[int]:
    pages: set[int] = set()
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_s, end_s = token.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            if start > end:
                start, end = end, start
            for page in range(start, end + 1):
                if 1 <= page <= page_count:
                    pages.add(page)
        else:
            page = int(token)
            if 1 <= page <= page_count:
                pages.add(page)
    return sorted(pages)


def normalize_text(text: str) -> str:
    text = text.replace("\x00", "")
    # Compact excessive blank lines while preserving paragraph boundaries.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def iter_chunks(
    pages: list[dict], chunk_chars: int, overlap_chars: int
) -> Iterable[dict]:
    chunk_id = 1
    i = 0
    while i < len(pages):
        start_page = pages[i]["page"]
        buf: list[str] = []
        end_page = start_page
        char_count = 0
        j = i
        while j < len(pages):
            page_text = pages[j]["text"]
            if not page_text:
                j += 1
                end_page = pages[j - 1]["page"]
                continue
            extra = len(page_text) + (2 if buf else 0)
            if buf and char_count + extra > chunk_chars:
                break
            if buf:
                buf.append("\n\n")
            buf.append(page_text)
            char_count += extra
            end_page = pages[j]["page"]
            j += 1
        text = "".join(buf).strip()
        if text:
            yield {
                "chunk_id": chunk_id,
                "start_page": start_page,
                "end_page": end_page,
                "char_count": len(text),
                "text": text,
            }
            chunk_id += 1
        if j >= len(pages):
            break
        # Move forward with overlap by characters.
        if overlap_chars <= 0:
            i = j
            continue
        rewind = 0
        k = j - 1
        while k >= i and rewind < overlap_chars:
            rewind += len(pages[k]["text"])
            k -= 1
        i = max(i + 1, k + 1)


def choose_render_pages(
    pages: list[dict], explicit_pages: list[int] | None, max_pages: int
) -> list[int]:
    if explicit_pages is not None:
        return explicit_pages[:max_pages]
    selected: list[int] = []
    for row in pages:
        low_text = row["char_count"] < 80
        image_rich = row["image_count"] > 0
        if low_text or image_rich:
            selected.append(row["page"])
        if len(selected) >= max_pages:
            break
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text and page renders from a PDF.")
    parser.add_argument("--input", required=True, help="PDF path")
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=3500,
        help="Approximate max chars per text chunk (default: 3500)",
    )
    parser.add_argument(
        "--overlap-chars",
        type=int,
        default=300,
        help="Approximate chunk overlap in chars (default: 300)",
    )
    parser.add_argument(
        "--render-pages",
        default="",
        help="1-indexed pages/ranges to render, e.g. '1,3-5'. Default auto-selects pages.",
    )
    parser.add_argument(
        "--max-render-pages",
        type=int,
        default=8,
        help="Max rendered pages (default: 8)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=180,
        help="Render DPI for pdf2image (default: 180)",
    )
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    outdir = Path(args.outdir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"error: input does not exist: {input_path}", file=sys.stderr)
        return 2
    if input_path.suffix.lower() != ".pdf":
        print(f"error: input is not a .pdf file: {input_path}", file=sys.stderr)
        return 2

    try:
        import fitz  # type: ignore
    except Exception as exc:  # pragma: no cover
        print(f"error: PyMuPDF import failed: {exc}", file=sys.stderr)
        return 2

    doc = fitz.open(str(input_path))
    pages: list[dict] = []
    for idx in range(len(doc)):
        page = doc[idx]
        raw_text = page.get_text("text") or ""
        text = normalize_text(raw_text)
        image_count = len(page.get_images(full=True))
        pages.append(
            {
                "page": idx + 1,
                "char_count": len(text),
                "image_count": image_count,
                "has_text": bool(text),
                "text": text,
            }
        )

    pages_path = outdir / "pages.jsonl"
    with pages_path.open("w", encoding="utf-8") as f:
        for row in pages:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    chunks = list(iter_chunks(pages, args.chunk_chars, args.overlap_chars))
    chunks_path = outdir / "chunks.jsonl"
    with chunks_path.open("w", encoding="utf-8") as f:
        for row in chunks:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    explicit_pages = (
        parse_page_ranges(args.render_pages, len(pages)) if args.render_pages.strip() else None
    )
    render_pages = choose_render_pages(pages, explicit_pages, args.max_render_pages)
    render_artifacts: list[dict] = []
    render_errors: list[str] = []

    if render_pages:
        try:
            from pdf2image import convert_from_path  # type: ignore

            renders_dir = outdir / "renders"
            renders_dir.mkdir(parents=True, exist_ok=True)
            for page_num in render_pages:
                images = convert_from_path(
                    str(input_path),
                    dpi=args.dpi,
                    first_page=page_num,
                    last_page=page_num,
                    fmt="png",
                    single_file=True,
                )
                if not images:
                    continue
                out_name = f"page-{page_num:04d}.png"
                out_path = renders_dir / out_name
                images[0].save(out_path, "PNG")
                render_artifacts.append(
                    {
                        "page": page_num,
                        "path": str(out_path),
                    }
                )
        except Exception as exc:  # pragma: no cover
            render_errors.append(f"pdf2image render failed: {exc}")

    if render_artifacts or render_errors:
        render_index = {
            "requested_pages": render_pages,
            "renders": render_artifacts,
            "errors": render_errors,
        }
        with (outdir / "render_index.json").open("w", encoding="utf-8") as f:
            json.dump(render_index, f, indent=2, ensure_ascii=False)

    total_chars = sum(row["char_count"] for row in pages)
    text_pages = sum(1 for row in pages if row["has_text"])
    empty_pages = len(pages) - text_pages
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    manifest = {
        "input_path": str(input_path),
        "output_dir": str(outdir),
        "generated_at_utc": now,
        "file_size_bytes": os.path.getsize(input_path),
        "page_count": len(pages),
        "text_pages": text_pages,
        "empty_text_pages": empty_pages,
        "total_text_chars": total_chars,
        "chunk_count": len(chunks),
        "chunk_chars": args.chunk_chars,
        "overlap_chars": args.overlap_chars,
        "rendered_pages": [r["page"] for r in render_artifacts],
        "render_errors": render_errors,
    }
    with (outdir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
