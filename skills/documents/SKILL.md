# Documents

## Find the file and choose the format

- Start from the user's question or audience. Find the existing file before making another copy, and keep its format, comments and collaboration features when the task depends on them.

- Choose the format for what the reader will do with it. Word suits text someone will keep editing, PDF a fixed layout for printing or sharing, a spreadsheet numbers people will change, a deck a story told slide by slide, and Markdown text that needs easy revision or pasting elsewhere.

- Use `artifact.list` and `artifact.inspect` to find an existing Muse artifact. Use `artifact.create_file` for a new file and `artifact.edit` to revise one. Read `~/docs/artifacts.md` for the delivery flow.

- These tools run a file builder that reads the format guide for its kind: [Word documents](document/GUIDE.md), [PDFs](pdf/GUIDE.md), [spreadsheets](spreadsheet/GUIDE.md), [presentations](presentation/GUIDE.md) or [Markdown](markdown/GUIDE.md). Read a guide yourself when you need its rules to plan or explain a file.

## Read with evidence

- Work from extracted text with source locations instead of loading a whole document at once. [Extract document evidence](references/pipelines.md) covers the bundled PDF, DOCX and XLSX extractors and how to cite their output.

- Split a long, multi-file or high-stakes review between a coordinator and extraction tasks, as [Review several documents](references/orchestration.md) describes.

- Tie every quotation and finding to a file and its page, section, slide or cell. Inspect rendered pages when scans, charts or layout affect the answer.

- A failed extraction does not mean the source lacks the information. Say which parts could not be read.

## Write and revise

- Lead with the point the reader needs. Use headings that explain the structure, concrete language and claims the evidence supports. Keep assumptions and recommendations apart from source facts.

- When editing, preserve the user's meaning, wording and requested scope. Keep formulas, sheet names, slide order and other structure unless changing them is the request.

- Keep an editable source for every file so later revisions start from it rather than from a rendered copy.

## Check and deliver

- Verify consequential names, numbers, dates, calculations and links against the source. Check the actual output, including its page or slide layout.

- Use `artifact.status` for an unfinished build and `artifact.export` for supported exports. Return the finished artifact or file.

- Sharing beyond this conversation is a separate action, through the sharing steps in `~/docs/artifacts.md` or the destination's connector.

## Available connectors

- [Google Docs](/opt/hatch/connectors/google_docs/CONNECTOR.md) for reading and editing the user's documents in place.

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) for finding the user's files and saving finished ones.

- [Google Sheets](/opt/hatch/connectors/google_sheets/CONNECTOR.md) for editing a live workbook without replacing it.

- [Google Slides](/opt/hatch/connectors/google_slides/CONNECTOR.md) for reading a deck or putting a finished deck into Google Slides.

- [Canva](/opt/hatch/connectors/canva/CONNECTOR.md) for designed layouts, brand templates and exports in the user's Canva account.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Studocu](/opt/hatch/connectors/studocu_mcp/CONNECTOR.md) for the user's study materials and study projects.

- [Gamma](/opt/hatch/connectors/gamma_mcp/CONNECTOR.md) for generating and exporting presentations and documents in Gamma.

## Websites

- [Microsoft 365](https://www.microsoft365.com/) for Word, Excel and PowerPoint files whose comments, tracked changes or macros must survive. Use `browser.spawn_task` in the user's signed-in account, name the exact file and the change, and have the task report what it saved.

- [Overleaf](https://www.overleaf.com/) for an existing LaTeX project the user keeps there.

- [Adobe Acrobat online](https://www.adobe.com/acrobat/online.html) for a PDF operation the local tools cannot do, only when uploading the file to Adobe fits the user's request.

## Alternatives for better results

- A short memo, a checklist or a few annotated pages often answer the question better than a long report.

- Edit a cloud document in its own app when downloading and rebuilding it would lose comments, tracked changes or live formulas.

- A local file is a complete option when the user does not want to connect an account.
