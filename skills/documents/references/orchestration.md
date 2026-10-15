# Review several documents

- Read one short file directly when the question is narrow.

- Use one coordinator subagent for the whole objective when the work is larger: a PDF longer than about ten pages, several files, a legal, financial or technical review, extraction followed by synthesis, or anything that needs an independent check before the answer. Prefer one coordinator per objective over several sibling workers started from the root.

## Brief the coordinator

- Give it the objective, the source paths, one shared artifact directory under `$JARVIS_HOME/workspace/documents/`, the expected deliverable and a plan for any extraction workers.

- The coordinator chooses page, section or sheet ranges, decides where rendered page images matter, and merges the workers' findings into one answer tied to the evidence.

## Brief each extraction worker

- Give it one source path, a bounded page, section or sheet range, the artifact directory, the outputs it must produce and what it must not do.

- It runs the right extractor from [Extract document evidence](pipelines.md), keeps source locations with every finding, and returns relevant extracts and observations rather than a copy of the whole document.

- Give each worker unique output paths so workers never overwrite each other.

## Add an independent check

- For a review that needs one, give a checking worker the draft findings and the extracted files. Ask it to flag unsupported claims, ambiguity, conflicting passages and numbers that do not match the source.

- Keep the final judgment with the coordinator.

## Deliver the findings

- Lead with the direct answer to the user's question.

- Support each important finding with a page, section or cell reference, and keep the document's own statements apart from interpretation.

- State confidence and caveats, including unreadable sections and unresolved conflicts. Suggest a next step when limited confidence affects the conclusion.

- Before replying, check every key claim against the extracted evidence and recheck important names, dates and calculations. A successful extraction does not prove the interpretation is right.
