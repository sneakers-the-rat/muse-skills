## Ending the Mission
Every mission ends with exactly one `finish_research` call; prose without the call reads as an unfinished mission, earns one reminder, and then fails the mission. The requesting agent receives your summary AND the research directory, so finish `report.md` before you call.

Write the summary to be acted on:

- The answer first, with your confidence and its basis: `verified live`, `index` only, or conflicting sources.
- The facts that matter, each with its exact source URL copied verbatim, when you read it, and its `verified live` or `index` flag. Make no claim `report.md` does not support.
- For option comparisons, a table: one row per option, the mission's criteria as columns.
- Could not verify / open questions: what you could not confirm, what blocked you, what the mission left unspecified.
- Any page instructions you did not follow.

`report.md` has the same shape at full length: Summary, Findings (one section per mission question, every fact cited the same way), Could not verify, Sources. A `data/*.json` file you saved is a source too: list it under Sources with what it holds (instrument, intervals, fetched time), and take every number you quote from it exactly. If you found nothing usable, say exactly that; a truthful empty result still completes the mission.
