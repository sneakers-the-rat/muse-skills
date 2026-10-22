## Activation-Authored Execution
Generated Ideas normally defer exact execution instructions until this build,
when live tools, connections, files, and user context can be checked. When the
task includes an `# Activation Execution Contract` and does not include a
`# Workflow Asset`:

- Treat the contract outcome, activation requirements, ordered execution
  claims, and completion evidence as the frozen promise boundary. The prose
  build plan may add implementation detail but cannot weaken or expand it.
- Before the first action that mutates durable state, turn the contract into
  the smallest executable plan for the current environment. Trace every
  promised outcome to a real action and an observable check. Do not create a
  workflow file merely to package that plan.
- Recheck live requirements immediately before dependent work. Treat `available`
  only as a non-drifting fact; resolve `check_at_activation` from current state.
  Never reinterpret `needs_user` as permission to guess: while a
  `needs_user` requirement is unresolved, do not execute the work that depends
  on it, and report it through the handoff.
- Execute and verify one dependency boundary at a time. Preserve successful
  work when later steps fail. Make one safe corrective attempt for an
  actionable deterministic failure when the correction cannot create duplicate
  external effects; otherwise stop that branch.
- Collect the contract's required completion evidence from real product state,
  output, or tool results. A file existing, an asynchronous request being
  accepted, or a partial artifact is not completion unless that is the stated
  outcome. If any required evidence is missing, use `partial`, `needs_user`, or
  `failed`, and name the exact gap.

