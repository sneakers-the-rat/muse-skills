# Extract document evidence

- The bundled extractors turn a PDF, DOCX or XLSX file into text with source locations, so findings can cite where each fact came from. Each script prints its manifest JSON to stdout and writes its files to the output directory.

- Treat the file path as the source of truth. Do not assume the document's contents are already in context, and do not claim anything you did not extract or see on a rendered page.

## Choose output paths

- Use explicit `$JARVIS_HOME` paths so root agents and subagents find the same files.

- Give every document and task its own output directory, such as `report-<slug-or-id>`. A shared path like `workspace/documents/report` lets one task overwrite another's evidence.

- Keep the extracted files until the answer is delivered, so every claim stays reproducible.

## PDF

How to work with a PDF:

1. Prefer reviewing pages visually. Render them as PNG with `--render-pages`, which runs Poppler's `pdftoppm` from the runtime image, and read each image. For a long document, render in batches and say which pages you could not read. If you can't render the pages, work from the text and say what you couldn't check.
2. Use the extracted text for wording and quick checks, not to understand layout, tables, charts or figures; they do not survive extraction.
3. After creating or editing a PDF, read every rendered page before delivering it, as the [PDF guide](../pdf/GUIDE.md) describes, and check that nothing is misaligned, cramped or hard to read.

- Extract text and chunks:

```sh
python3 "/opt/muse/skills/documents/scripts/extract_pdf.py" \
  --input "$JARVIS_HOME/workspace/user/files/report.pdf" \
  --outdir "$JARVIS_HOME/workspace/documents/report-<slug-or-id>" \
  --chunk-chars 3500 \
  --overlap-chars 300
```

- Render pages when layout, tables, figures or scan quality matter:

```sh
python3 "/opt/muse/skills/documents/scripts/extract_pdf.py" \
  --input "$JARVIS_HOME/workspace/user/files/report.pdf" \
  --outdir "$JARVIS_HOME/workspace/documents/report-<slug-or-id>" \
  --render-pages 1,3-5 \
  --dpi 180
```

- Without `--render-pages` the script renders pages with little text or embedded images on its own. It does not spot columns, tables or vector drawings, so name those pages yourself.

- `--max-render-pages` (default 8) caps an explicit `--render-pages` list too. For more pages, raise it or render in batches; the manifest's `render_errors` names any pages left out.

- Add `--layout` to keep columns side by side in the text, for searching or quoting. Use rendered pages, not this text, to read tables, calendars or forms.

- The output directory holds:
  - `manifest.json`
  - `pages.jsonl`
  - `chunks.jsonl`
  - `renders/page-XXXX.png` and `render_index.json` when pages were rendered

- Read rendered PNGs with `muse.read` when page layout matters.

## DOCX

```sh
python3 "/opt/muse/skills/documents/scripts/extract_docx.py" \
  --input "$JARVIS_HOME/workspace/user/files/contract.docx" \
  --outdir "$JARVIS_HOME/workspace/documents/contract-<slug-or-id>" \
  --chunk-chars 3000 \
  --overlap-chars 250
```

- The output directory holds `manifest.json`, `segments.jsonl` and `chunks.jsonl`.

## XLSX

```sh
python3 "/opt/muse/skills/documents/scripts/extract_xlsx.py" \
  --input "$JARVIS_HOME/workspace/user/files/finance.xlsx" \
  --outdir "$JARVIS_HOME/workspace/documents/finance-<slug-or-id>" \
  --chunk-chars 3000 \
  --overlap-chars 250
```

- Add `--sheet-names Summary,Q1` to extract only those sheets.

- The output directory holds `manifest.json`, `rows.jsonl` and `chunks.jsonl`.

## Check extractor dependencies

- Run this when an extractor might be unavailable:

```sh
command -v pdfinfo pdftotext pdfimages pdftoppm
python3 - <<'PY'
import importlib.util
for mod in ("docx", "openpyxl"):
    ok = importlib.util.find_spec(mod) is not None
    print(f"{mod}: {'ok' if ok else 'missing'}")
PY
```

- The PDF extractor uses the poppler tools above; the DOCX and XLSX extractors use the Python modules.

- If a dependency is missing, report exactly what is unavailable and continue with the best remaining route, such as reading the file with `muse.read`.

## Cite the extracted evidence

- Give each finding an explicit reference to the source file or the extracted line:

```text
workspace/user/files/report.pdf#page=12
workspace/user/files/contract.docx#segment=14
workspace/user/files/finance.xlsx#sheet=Summary&row=22
workspace/documents/report-<slug-or-id>/pages.jsonl#line=38
workspace/documents/contract-<slug-or-id>/segments.jsonl#line=14
workspace/documents/finance-<slug-or-id>/rows.jsonl#line=22
workspace/documents/report-<slug-or-id>/renders/page-0012.png
```

- Note uncertainty from scans, missing tables or ambiguous passages beside the finding it affects.
