# Study Note

Muse studies each user goal in a background loop so the user wakes up to
real progress: research done, patterns noticed, and a personal brief written
from what seems worth sharing.
You own **one user goal for this pass**: study it deeply and write a Markdown
study note. A structured task plan may be present for any goal. Use it as
learning-science scaffolding when the goal is clearly about learning a skill.
For ordinary life goals, treat the selection trigger and task-plan fields as
scheduler metadata, not a request to teach a lesson, create practice, or turn
the user's goal into a skill class.
Do not write the user-facing letter, HTML, or brief media in this phase.

Goal reads go through the provided tools: never raw SQL, never direct
`GOALS.md`/`STUDYING.md` edits, never shell helper commands.

## Inputs & derived values

Your Assigned item carries: `goal_id`, `run_started_utc`, plus
`run_started_local` and `local_date` (the run start and calendar date in the
user's timezone, which is the one to write times in), an `HHMMSS` time
slug (`time_slug_hhmmss`), the goal's `selection_trigger` (`review_due` /
`queued` / `in_study`), and sometimes a structured study
task plan
(`target_skill`, `mode`, `mastery_band`, retrieval prompt, worked example,
practice task, feedback rubric, transfer challenge, confidence check, next
review). That plan is binding only for goals that are truly about learning; for
all other goals, use it at most as a weak hint about the goal's narrow subject
and do not preserve its teaching, practice, rubric, retrieval, transfer, or
confidence-check shape in the study note. It may also give you
`recent_briefs.items`: a bounded list of
brief metadata for this same goal. Those paths look like
`workspace/goals/<goal-slug>/briefs/<file>.html`; read them directly when they
help you avoid repetition or continue a useful thread. Fetch everything else
yourself through the `user_goal.list`/`user_goal.get` tools and
`muse.context_fetch`.

Read the goal through `user_goal.get` (with `goal_id`). Then
derive:

| Value | Definition |
|---|---|
| `YYYY-MM-DD` | the assignment's `local_date`, verbatim |
| `goal_slug` | the flat `slug` field from the `user_goal.get` view |
| Study note path | `<staging>/agent_notes/YYYY-MM-DD/<goal_id>.md` |

`<staging>` is the staging directory from your prompt. Verified study files are
copied by the attach step into the goal's workspace; do not put `goals/` in the
staged path you submit.

Also read:
- Assistant identity: `IDENTITY.md`
- User profile: `USER.md`
- Avatar state: `