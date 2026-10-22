# Personal Brief

One user goal for this pass: its study found something fundamentally
new, and you write the personal Letter and render the finished Muse
Letter artifact in this same turn. The Letter voice rules, the
rendering fidelity contract, and the design doctrine are in your
system prompt; this assignment carries the mechanics.

Your Assigned item carries `goal_id`, the staged study note's
`note_path`, the full study output, and `briefing_reason`, one
sentence on why the study ruled this worth a Letter. Read the staged
study note at `note_path` inside your staging surface, then `USER.md`
and `IDENTITY.md`; your system prompt's Writing the Letter law governs
how the note becomes the Letter.

The note's `## Already Covered in Main Chat` section lists what the user
and the main agent already covered about this goal in main chat. Read
that section before you draft. Your system prompt's Writing the Letter
law governs what the Letter may do with what it lists.

Goal reads go through `user_goal.get` (with `goal_id`);
goal write actions are rejected on this turn. Never raw
SQL, never direct `GOALS.md` or `STUDYING.md` edits. Treat tool output
as authoritative and never hide a failed tool call. Use shell execution
only for bounded checks over files you staged in this run. Do not
reproduce a failed first-party browser or media call with shell/curl; a
terminal media outage ends honestly in `skip_reason`.

Derive:

| Value | Definition |
|---|---|
| `YYYY-MM-DD HH.MM.SS` | the VM's current **local** date and time |
| `goal-slug` | the flat `slug` field from the `user_goal.get` view |
| `<Brief title>` | the Letter's title, written to the title law in your system prompt |

Files to stage, in order:

1. The fresh Markdown Letter draft at
   `goals/briefs/<goal-slug>/drafts/<Brief title> (<YYYY-MM-DD HH.MM.SS>).md`,
   in this simple shape:

   ```markdown
   # <Brief title>

   <the letter>
   ```

2. The rendered artifact at
   `goals/briefs/<goal-slug>/<Brief title> (<YYYY-MM-DD HH.MM.SS>).html`,
   built from that draft under the rendering law in your system prompt
   and the design assets below.

3. Every local image under the staged `goals/briefs/<goal-slug>/media/`
   directory, the generated hero included. In the staged HTML,
   reference every local image only with a staging-relative path such
   as `media/example.webp`; the attach step rewrites it to its durable
   workspace URL. List every local media file in `brief.media_paths`
   and set `brief.hero_image_path` to the generated visual opening.

Include the canonical `NOTEBOOK_BRIEF.css` link once so the attach
step can inline it. Brief-specific CSS may support unique content
without replacing the shared page, typography, or signature styles.
Keep the artifact read-only and self-contained apart from links and
sourced media.

Complete the required diagnostic scores honestly; they are recorded
with the brief as calibration diagnostics and do not gate storage.

End the turn with one `muse.finish_step` call carrying:

- `goal_id`
- `note_path`
- `draft_path`
- `brief_display_title`
- `delivery_message`
- exactly one of:
  - a completed `brief` with `path`, `hero_image_path`, `media_paths`,
    and `scores`
  - `skip_reason` when a terminal media outage prevented a valid
    artifact; the Letter draft, its title, and its delivery message
    still exist and still ride this same output
