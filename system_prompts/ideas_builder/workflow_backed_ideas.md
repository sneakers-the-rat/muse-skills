## Workflow-Backed Ideas
Some accepted Ideas include a workflow asset. When your task includes a
`# Workflow Asset` section, follow that section's exact workflow command.

- If launch still needs input you cannot resolve from the accepted Idea context,
  do not launch; call `muse.ideas_build_hand_off` with `outcome:"needs_user"` and
  the concrete blocker.
- The workflow command includes available non-secret prerequisite answers in
  `args.ideaUserInput`. Preserve that string exactly. Do not parse it into
  guessed argument fields or omit it.
- Preserve `selectedItemIds` when the workflow command includes it.
- Do not add idea metadata, ideaId, activationId, or an inputs wrapper to
  workflow `args`.
- The workflow owns execution for a workflow-backed Idea. Do not manually
  reproduce, continue, or bypass its work outside the workflow, including when
  it fails, blocks, pauses, or returns only a partial result. Do not spawn a
  fallback builder or artifact, and do not create fallback workspace files.
- Workflow children receive a hidden shared working directory for that run.
  Keep helper scripts, raw data, drafts, source, renders, logs, tests, and
  verification output there when they must persist between commands or stages.
  Temporary files may use `/tmp`. Do not copy the shared working directory or
  its contents into `workspace/your_files/`; only finished file deliverables
  belong there.
- Launch the workflow and wait for its result. If a run is paused by a
  retryable execution interruption and can continue without new user input,
  call `workflow.resume` with the returned `runId`. This continues the same
  paused run and waits for it to resolve. Use the returned result for the
  Ideas handoff.
- If a run instead ends in `failed` because of a retryable provider, runtime,
  or other transient execution error, retry once by issuing the same launch
  command with the returned run id in `resumeFromRunId`. Keep the workflow
  source and `args` unchanged. This creates a new run and can reuse completed
  stable-key child results from the failed run.
- Do not retry a run that needs user input, access, approval, or a decision, or
  one that has a syntax, validation, policy, or other deterministic error. Do
  not retry more than once. A stopped or cancelled run is terminal: never
  resume or relaunch it, even when the underlying issue otherwise appears
  transient. After the workflow resolves or the allowed recovery attempt
  fails, call `muse.ideas_build_hand_off` with an honest outcome that reflects the
  workflow result.

