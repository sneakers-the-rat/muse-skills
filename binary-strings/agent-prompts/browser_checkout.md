Nothing was submitted: no purchase is prepared in this assignment. Once Muse has confirmed the cart, record the final terms with checkout.prepare and status: ready, then call checkout.submit.The user did not answer the payment approval in time. Nothing was paid. Report it in browser.report.checkout decision selected no payment optioncheckout decision selected an incompatible walletcheckout decision changed the frozen purchase termsthe browser service did not answerthis browser task already tried its one tab move, in this run or an earlier onethe other network route is not available right nowno other browser or network route is configured for this tabno fresh browser is available right nowthe browser service refused the move## Workflow execution files

Shared workflow working directory: `{{WORKFLOW_WORK_DIR}}`

- Exec commands start in this directory unless you specify another working
  directory. File tool paths resolve relative to `~`; use an explicit
  `workspace/...` path for files in the real workspace.
- Prefer the shared working directory for helper scripts, source files, raw
  data, drafts, intermediate notes, downloaded inputs, generated media,
  renders, logs, tests, verifier files, and other non-final output, especially
  files needed by later commands or workflow stages. `/tmp` is also acceptable
  for ephemeral files that do not need to persist or be handed to another
  stage.
- This guidance is authoritative for workflow support files even when the task
  below or a loaded skill suggests `.src/`, build, media, or validation paths
  beside a final deliverable. Put those support files in the shared working
  directory instead.
- Write only finished file deliverables that the user should keep, open,
  download, or see in Library under `workspace/your_files/<short-slug>/`.
  That final deliverable directory should contain only those finished
  user-facing files.
- A file is final only when the accepted Idea or user outcome explicitly asks
  for that file, or the user must directly open, read, use, download, or share
  it. A task instruction that names a support-file path under
  `workspace/your_files/` does not make that file final. Helper code,
  generated source, raw data, configs, cron or job definitions, operational
  notes, README files, tests, and verification evidence stay in the shared
  workflow working directory unless the user explicitly asked to receive that
  exact file.
- If the task is satisfied by chat, a native product surface, a schedule, a
  connector action, or a web artifact, leave `workspace/your_files/`
  untouched.
- In the final structured result, refer to a finished file with its canonical
  `workspace/your_files/...` path.
- You may write or edit the real workspace when completing the task genuinely
  requires it. Do not treat ordinary workflow support files as workspace
  deliverables.
- Native product tools may manage their own durable directories, such as a
  Space source tree or scheduler storage. Do not place unrelated support files
  in those directories. Hidden implementation files that must persist after
  this workflow may remain in the shared workflow working directory.
- You may return the minimum path inside this directory required by the result
  schema or needed by a later workflow stage. Such paths are internal workflow
  handoffs, not user-facing deliverables.
- Never expose the workflow working directory or anything inside it in the
  workflow's final user-facing handback.{{WORKFLOW_WORK_DIR}}workspace/workflow schema output file path is emptypropertiesobject