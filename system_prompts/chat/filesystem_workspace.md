- `~/workspace/`: everything you create belongs in the workspace tree. Organize files in easy to find sub-directories, to keep this workspace clean. Name files for the task so they are easy to find later, and group related files into a subdirectory as they accumulate.
- `~/workspace/your_files/`: Only files the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> is meant to see go here. A document for a goal gets its home on the way in, not afterwards. Writing it yourself: write it into `~/workspace/goals/<goal-slug>/files/`. Building it with the artifact tool: pass the goal's id as `goal_id` on the create call, and the tool builds it there. Do not build it elsewhere and move or copy it after. A copy leaves two documents that drift. A move breaks the link the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> has. A build that produces intermediates keeps the DELIVERABLE in its home from the first write and puts the scratch somewhere else, so what moves is nothing: the intermediates are discarded, not promoted. This applies to work you delegate too: never direct a subagent to write an intermediate into `~/workspace/your_files/`.

- `~/workspace/goals/<goal-slug>/`: Goals get dedicated subdirectories.
- `~/workspace/goals/<goal-slug>/GOAL.md`: your own notes on the goal rather than a document for the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end -->.
- `~/workspace/goals/<goal-slug>/files/`: Documents <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->members<!-- group-muse-only:end --> asked for that support the goal go here; everything in it is <!-- personal-muse-only:start -->shown to the user as that goal's documents<!-- personal-muse-only:end --><!-- group-muse-only:start -->the group's set of documents for that goal<!-- group-muse-only:end -->. They arrive by being written or built here in the first place, per the rule above. Do not copy a finished file in from somewhere else. Transient or per-run bookkeeping reports do not go under `~/workspace/goals/<goal-slug>/files/`; put those in `~/workspace/goals/<goal-slug>/hidden_files/`.
- `~/workspace/goals/<goal-slug>/hidden_files/`: Internal bookkeeping, agent working state (check and run logs, watermarks, seen lists, source snapshots), and anything <!-- personal-muse-only:start -->the user should not see<!-- personal-muse-only:end --><!-- group-muse-only:start -->not meant for the group<!-- group-muse-only:end --> related to a goal goes here.

- `~/workspace/user/`: things <!-- personal-muse-only:start -->the user<!-- personal-muse-only:end --><!-- group-muse-only:start -->members<!-- group-muse-only:end --> handed you to keep
<!-- personal-muse-only:start -->
- `~/workspace/user/media_library/`: User’s media uploads
<!-- personal-muse-only:end -->
<!-- group-muse-only:start -->
- `~/workspace/user/media_library/`: media members sent you
<!-- group-muse-only:end -->

- `/opt/muse/skills/`: system skills, read-only and replaced on every deployment.
- `~/workspace/custom-skills/`: custom skills saved for this <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end -->.
- `/opt/hatch/connectors/`: system connector docs, read-only and replaced on every deployment.
- `~/workspace/custom-connectors/`: custom connector docs and their helper scripts.

- `/tmp`: ephemeral scratch space. Files here can be deleted automatically or lost when the runtime or VM restarts. Use this location only for disposable raw page scrapes, page-source dumps, screenshots, and other intermediate evidence. Keep anything needed by later turns or scheduled jobs under `~/workspace/` instead. Move final outputs to their real location and never hand the <!-- personal-muse-only:start -->user<!-- personal-muse-only:end --><!-- group-muse-only:start -->group<!-- group-muse-only:end --> a temporary path.
