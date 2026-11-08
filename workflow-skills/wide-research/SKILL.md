# Wide Research

## Purpose
Coordinate one manager subagent that fans out the same research task across many independent inputs and returns a single normalized result set.

## When to Use
- The task can be split into many independent subtasks (for example, one company/person/topic per input).
- Each subtask should return the same structured fields.
- The user asks for "wide research", "parallel research", or high-volume lookup/screening.

Do not use this workflow for single-item tasks or when subtasks depend on each other.

## Tooling
Use exactly one manager subagent for the overall operation.

Manager input contract:
- `operation_brief`: one concise sentence.
- `inputs`: one independent item per element.
- `output_schema`: required fields and allowed types.
- `worker_prompt_template`: per-input instructions.
- `completion_format`: exact JSON object shape for the manager's final response.

Manager output contract:
- `total`
- `success_count`
- `failure_count`
- `results`
- `failures`
- `notes`

## Operating Rules
1. Deduplicate and normalize the input list before spawning the manager.
2. Keep the output schema minimal and explicit; avoid optional or free-form fields unless the user asked for them.
3. Use one manager coordinator for one user goal; do not fan out multiple sibling root-level subagents.
4. Instruct the manager to assign one worker per input and keep each worker scoped to its own item. For a long batch, use workflow.launch_async with stable item keys and inspect it with workflow.view_run. Put work in functions passed to `parallel` with explicit concurrency; creating all worker promises first starts them all immediately. Await each item's dependencies, and keep coordination in the workflow instead of shared counters or flag files.
5. Complete one item, inspect its CPU, memory and service requirements, then increase concurrency only while those requirements fit. Browser queue entries retain accepted work. Do not resubmit waiting browser tasks. After failure, address the cause and retry only the missing work, preserving completed results and checkpoints.
6. Reply to the user immediately that wide research has started; do not block on completion.
7. In the final user-facing output, report verified coverage (`success_count/total`) and unresolved gaps. Distinguish pending, failed, stopped, and never-started inputs. Count completed items once, even if they needed several attempts.

## Available connectors

- This skill uses native tools and does not require an account connector.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
