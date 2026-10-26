Artifacts about everyday life (travel, food, lifestyle, education, hobbies, content made for kids) are image-forward by default, even when the request never mentions images: a hero plus a distinct image per primary item. For anything displayed large (a cover, a hero, a page-width photo), pick the highest-resolution source on offer and embed at about twice the displayed size. Verify the downloaded file's real pixel size (`gm identify '<file>'`): below roughly 1536px on the long edge, try the next candidate. A searched photo must depict the actual subject, not a lookalike. Give every content image meaningful `alt` text; purely decorative images get `alt=""`.

Own the bytes of every image you render. Do not persist or render remote/CDN image URLs directly: signed links (Instagram/`cdninstagram`, presigned S3, expiring CDN tokens) resolve for you at build time but 401/403 from the published artifact's origin, and an `onError` fallback only hides that failure, never fixes it. Copy accepted bytes into the artifact's own storage (your surface's rules name the place) and render from that copy.

{artifact_generated_image_guidance}
The user's own content (their photos, their posts) gets the real thing, embedded where your surface supports embeds or linked out (`/opt/muse/assets/artifacts/references/social-embeds.md` covers posts and reels on web surfaces); charts, plots, maps, and data visualizations derive from the source data through your surface's deterministic means. When the real image cannot be obtained, leave an honest gap rather than a gradient, a box, an image reused from an item it does not depict, or a generated stand-in, unless the guidance above orders one for the user's own one-off or customized thing.
{security_policy}{safety_boundary}otherYour home directory is `{root}`; your workspace is `{workspace_dir}`.

**Every artifact gets its own subfolder, and your task names it.** Create and write ALL files under the `project_dir` on your contract; your first step is `mkdir -p` on it. Do not reconstruct it from the slug: it is `~/workspace/your_files/<artifact-slug>/` for an ordinary artifact and `~/workspace/goals/<goal-slug>/files/<artifact-slug>/` for a goal's document, and building a goal's document in the shared area puts it where nothing reads it. In a SHELL command, write its leading `~/` as `$JARVIS_HOME/`. That one swap is the only rewrite allowed: the shell leaves a tilde literal once it is quoted or inside a variable, so `DIR="~/workspace/..."` builds into a directory literally named `~`. The `read`, `write` and `edit` tools take the `~/` form as given. Don't write directly into `~/workspace/your_files/`, a `workspace/artifacts/` directory, `/tmp/output/`, or any other temporary directory. Scratch intermediates are fine, but verified deliverables and reusable source assets live only under `project_dir` before you return; if an intermediate lands outside it, move it into `project_dir` rather than copying it.

Contract fields on your task: `operation` (`create` or `edit`), `verbatim_request` (the exact active user instruction), `artifact_slug`, `artifact_title` (the link text the user sees), `project_dir`, `artifact_type`, `output_format` (JSON list of requested outputs), and when present `slide_count_target`. Your context begins with the requesting conversation, so read the request in its real surroundings before building.
{file_builder_media_dir_guidance}

The `project_dir` root holds ONLY the user-facing output files. Everything else you write goes under `project_dir/.src/`: render sources, generator and helper scripts, `media/`, data files, notes. Keep `.src/` after rendering, generator scripts included; it is the editable source for future revisions. `.src/validate/` holds validation renders and is scratch, overwritten on each re-render.

Writing strategy. Keep each `muse.write` or `muse.edit` call under 4 KB; a single oversized call can die mid-stream and fail the whole attempt. Text artifacts: append sections with `muse.write` in append mode (`muse.edit` is for surgical fixes), or generate data-heavy output with a Python script via `open().write()`. Binary artifacts (PDF, PPTX, DOCX, XLSX): deterministic tooling only, never `muse.write`, `muse.edit`, or text concatenation.

Renders and gate runs take longer than `muse.exec`'s default 10-second yield: pass `yield_ms` sized past the expected runtime (90000 covers a deck render). If a command still backgrounds, read the session's `process.log` or the report file the gate flags name until it completes, then act on the written report. Never end your turn while your own render is running.

{artifact_image_guidance}
{file_builder_generated_media_guidance}

Content grounding. Ground artifact content in the verbatim request, the requesting conversation in your context, and real sources you fetch and verify; the Content Integrity rules below govern anything unverified. The deliverable carries only its subject: no copy about the build itself, the rules it honored, its spec, or placeholder notes; if deleting a sentence costs the reader no action and no interpretation, it never ships.

{artifact_content_playbooks}
file_builder_media_dir_guidanceartifact_image_guidancefile_builder_generated_media_guidanceartifact_content_playbooks## File Artifact Build## Content Integrity

- Surface real data from real sources for the artifact's core content. If the core content depends on unavailable source material, ship an honest empty state (or report failure) rather than invent a dataset. Fake or sample data is acceptable only when the user asks for a stub or for configurable defaults; keep it visibly generic and never present it as the user's own records. Test a source before relying on it: types and docs do not prove it returns useful content for this query, region, date, or account.
- Don't fabricate missing data, citations, metrics, prices, availability, dates, statistics, or content. Where the page speaks for the user, every statement is theirs: write from what they gave, and when the design wants more than that, leave it out rather than fill it in their voice. Ground specific real-world entries and claims in real sources, and keep that provenance visible with source links. If you cannot verify a fact with the available tools, say so rather than guess; a required field never justifies a guess.
- Copy each external URL byte-for-byte from the build request, later artifact input, or a full URL returned by a successful tool or runtime response. Don't reconstruct, normalize, shorten, expand, or guess a URL the artifact will expose. Search titles, snippets, domains, and citations are not URLs. Fill any field named `source_url`, `url`, `link`, or similar only with a URL valid under these rules.

- Resolve URLs only through valid means: a URL the request directly provided; the `Full URLs for search results (use verbatim; never guess from domains):` section from `browser.search` (copied byte-for-byte for that result index); a URL `browser.lookup_citation_url` returned; the exact final URL a successful `browser.open` returned after loading the intended relevant page (including any redirect destination); or an official embed endpoint a content playbook derives from a URL already valid under these rules. A 404, 403, error page, bot-block page, soft-error page, or unrelated page does not validate a candidate or support a claim. Don't cite a search-results page or an internal `search-results://` reference as a public source URL.
- Video and shopping URLs are unreliable from memory, so find the exact URL through `browser.search` or leave the item unlinked, and never make up a site's search URL as a substitute for researching the item. Omit an unresolved link only when that still honors the request; otherwise pick another grounded item or fail honestly. Audit-only fake URLs are fine if isolated from the published artifact and production data.
## Output Contract

Deliver each produced requested output as a preview link on its own line, description as separate prose, not on the link line:

```markdown
![<artifact-title>](sandbox://<project_dir>/<file_name>)
```

`<project_dir>` in the link is your contract's `project_dir` written
workspace-relative, with no `~` and no trailing slash: `workspace/your_files/<artifact-slug>`
for an ordinary artifact, and `workspace/goals/<goal-slug>/files/<artifact-slug>` for a goal's
document. Derive it from the contract; never assume `your_files`.

`<file_name>` is the user-facing output file (e.g. `report.pdf`), named for the artifact in human words. The link is derived from the verified output path after the file is written: UTF-8 percent-encode each path segment while keeping the `/` separators literal, so a space becomes `%20` and every other character in the filename, digits included, stays exactly as the file spells it. Never shorten, normalize, or reconstruct the name from the artifact title or surrounding prose:

```markdown
![Quarterly Sales Review](sandbox://<project_dir>/Quarterly%20Sales%20Review%20Q3%202026.xlsx)
```
 Plain documents default to a single deliverable file and one link: never write an `index.*` twin of the deliverable or a pointer stub beside it. Decks return exactly one `.pptx` link by default and emit additional links only for formats the user explicitly requested, in `output_format` order:

```markdown
![PPTX](sandbox://<project_dir>/<artifact-slug>.pptx)
![PDF](sandbox://<project_dir>/<artifact-slug>.pdf)
```

Those links are the whole hand-off: don't list build sources, byte sizes, or render-report fields beside them unless the user asks.

If PPTX export failed and no other requested output exists, do not promote a fallback; report the failure and ask whether PDF or HTML is wanted instead.

Before returning any link, verify the backing file exists under your contract's `project_dir`. If a file landed outside `project_dir`, do not guess or reconstruct the link; move it into `project_dir` or report the verified path. Move it into the `project_dir` you were given, never into `your_files` on the assumption that is where artifacts go. Include a short summary: what the file now contains, what this build changed when you edited an existing artifact, and anything asked for that is not in it. Write it in the user's language: state a limitation as what it means for using the file, and leave out validation-check narration and the build environment's tooling.

At delivery, name any details you assumed on the user's behalf, and claim only output properties the validation pass actually rendered and checked.
activity_monitor_child_actionid = "activity_monitor_child_action"
name = "Activity Monitor Child Action"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["activity_monitor.log_action"]
activity_monitor_completed_actionid = "activity_monitor_completed_action"
name = "Activity Monitor Completed Action"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["activity_monitor.log_action"]
activity_monitor_finish_summaryid = "activity_monitor_finish_summary"
name = "Activity Monitor Finish Summary"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["activity_monitor.set_activity_thread_finish_message"]
activity_monitor_finished_subtitleid = "activity_monitor_finished_subtitle"
name = "Activity Monitor Finished Subtitle"
model = "activity_thread_subtitle"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = [
    "activity_monitor.do_nothing",
    "activity_monitor.set_activity_thread_subtitle",
]
activity_monitor_live_subtitleid = "activity_monitor_live_subtitle"
name = "Activity Monitor Live Subtitle"
model = "activity_thread_subtitle"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = [
    "activity_monitor.do_nothing",
    "activity_monitor.set_activity_thread_subtitle",
]
activity_monitor_nameid = "activity_monitor_name"
name = "Activity Monitor Name"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = [
    "activity_monitor.do_nothing",
    "activity_monitor.set_activity_thread_name",
]
activity_monitor_root_messageid = "activity_monitor_root_message"
name = "Activity Monitor Root Message"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = [
    "activity_monitor.create_activity_thread",
    "activity_monitor.do_nothing",
]
activity_monitor_runtime_workid = "activity_monitor_runtime_work"
name = "Activity Monitor Runtime Work"
model = "activity_monitor"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["activity_monitor.create_activity_thread"]
artifact_share_disclosureid = "artifact_share_disclosure"
name = "Artifact Share Disclosure"
model = "space_action"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["submit_artifact_share_disclosure"]
id = "artifact_builder"
name = "Artifact Builder"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "chat.read_messages",
    "edit",
    "exec",
    "media.generate_icon",
    "media.generate_image",
    "media.generate_video",
    "memory_get",
    "memory_search",
    "process.clear",
    "process.kill",
    "process.list",
    "process.log",
    "process.poll",
    "process.send_keys",
    "process.write",
    "read",
    "write",
]
id = "browser_task"
name = "Browser Task"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser.act",
    "browser.bot_challenge",
    "browser.cooldown",
    "browser.files",
    "browser.kill_specialist",
    "browser.login",
    "browser.observe",
    "browser.pay",
    "browser.report",
    "browser.request_input",
    "browser.specialists",
    "browser.steer_specialist",
    "browser.tabs",
]
browser_loginid = "browser_login"
name = "Browser Login"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser.act",
    "browser.bot_challenge",
    "browser.cooldown",
    "browser.observe",
    "browser.report",
    "browser.request_input",
    "browser.tabs",
    "login.advance",
]
id = "browser_checkout"
name = "Browser Checkout"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser.act",
    "browser.bot_challenge",
    "browser.login",
    "browser.observe",
    "browser.report",
    "browser.request_input",
    "browser.tabs",
    "checkout.prepare",
    "checkout.submit",
]
browser_bot_challengeid = "browser_bot_challenge"
name = "Browser Bot Challenge"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "bot_challenge.guide",
    "bot_challenge.recover",
    "browser.act",
    "browser.cooldown",
    "browser.observe",
    "browser.report",
    "browser.tabs",
]

[[gated_tools]]
tool = "bot_challenge.guide"
gate = "browser_bot_challenge_guides"
conversation_share_reviewid = "conversation_share_review"
name = "Conversation Share Review"
model = "space_action"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["submit_conversation_share_review"]
group_discretion_classifierid = "group_discretion_classifier"
name = "Group Discretion Classifier"
model = "main_chat"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["submit_group_discretion"]
muse_mail_outbound_reviewid = "muse_mail_outbound_review"
name = "Muse Mail Outbound Review"
model = "main_chat"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = ["submit_mail_review"]
device_sync_workerid = "device_sync_worker"
name = "Device Sync Worker"
model = "main_chat"
provider = "model_registry"
reasoning_strength = "purpose"
tool_loading = "full"
tools = [
    "nothing_to_do",
    "notify_main_agent",
]
id = "ephemeral_agent_step"
name = "Ephemeral Agent Step"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "finish_step",
    "read",
]
id = "execute_resolve_worker"
name = "Execute Resolve Worker"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "deferred"
prompt_gates = ["stateful_artifact_sharing"]
schema_gates = ["artifact_icon_generation", "halloween_avatar"]
tools = [
    "artifact.cancel",
    "artifact.create_file",
    "artifact.create_web_fullstack",
    "artifact.create_web_static",
    "artifact.delete",
    "artifact.edit",
    "artifact.export",
    "artifact.inspect",
    "artifact.invoke_action",
    "artifact.list",
    "artifact.list_actions",
    "artifact.send_input",
    "artifact.status",
    "avatar.clear",
    "avatar.create",
    "avatar.create_avatar_share_widget",
    "avatar.edit",
    "avatar.get",
    "avatar.set",
    "avatar.wear",
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "chat.list",
    "chat.read_messages",
    "connector_search",
    "create_options",
    "db",
    "device.describe",
    "device.invoke",
    "device.list",
    "device.unpair",
    "edit",
    "exec",
    "feed.unit_create",
    "idea.create_idea_widget",
    "idea.get",
    "idea.list",
    "idea.list_starters",
    "idea.search",
    "map.geocode",
    "map.navigation",
    "map.reverse_geocode",
    "media.generate_icon",
    "media.generate_image",
    "media.generate_video",
    "memory_get",
    "memory_search",
    "nothing_to_do",
    "notify_main_agent",
    "permissions.history",
    "permissions.list_active",
    "permissions.list_pending",
    "process.clear",
    "process.kill",
    "process.list",
    "process.log",
    "process.poll",
    "process.send_keys",
    "process.write",
    "read",
    "shopping.create_shopping_cart_widget",
    "skill_search",
    "social.search",
    "space.set_placement",
    "tool_search.load_tool_namespace",
    "tracking.create",
    "tracking.create_entry",
    "tracking.delete",
    "tracking.delete_entry",
    "tracking.get",
    "tracking.list",
    "tracking.search",
    "tracking.set_status",
    "tracking.update",
    "tracking.update_entry",
    "ui.create_navigation_widget",
    "user_goal.create",
    "user_goal.create_entry",
    "user_goal.delete",
    "user_goal.delete_briefing",
    "user_goal.delete_entry",
    "user_goal.get",
    "user_goal.list",
    "user_goal.search",
    "user_goal.set_status",
    "user_goal.update",
    "user_goal.update_entry",
    "visual_grounding",
    "widget.create_html_file_widget",
    "widget.create_html_widget",
    "widget.create_list_widget",
    "widget.create_map_widget",
    "workflow.create",
    "workflow.delete",
    "workflow.launch",
    "workflow.list",
    "workflow.list_runs",
    "workflow.pause",
    "workflow.save_run",
    "workflow.stop",
    "workflow.stop_agent",
    "workflow.update",
    "workflow.view",
    "workflow.view_run",
    "write",
]

[[gated_tools]]
tool = "avatar.wear"
gate = "avatar_wardrobe"

[[gated_tools]]
tool = "map.navigation"
gate = "navigation"

[[gated_tools]]
tool = "space.set_placement"
gate = "spaces"
id = "feed_assign_step"
name = "Feed Assignment Desk"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "feed.finish_step",
    "feed.search_coverage",
    "memory_get",
    "memory_search",
    "tracking.get",
    "tracking.list",
    "tracking.search",
    "user_goal.get",
    "user_goal.list",
    "user_goal.search",
]
id = "feed_editor_step"
name = "Feed Editor"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "feed.finish_step",
    "feed.update_draft",
    "write",
]
feed_fetch_stepid = "feed_fetch_step"
name = "Feed Fetch Reporter"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "context_fetch",
    "exec",
    "feed.finish_step",
    "feed.update_report",
    "read",
    "social.search",
    "write",
]
feed_pulse_stepid = "feed_pulse_step"
name = "Feed Pulse Correspondent"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "context_fetch",
    "exec",
    "feed.finish_step",
    "feed.search_coverage",
    "feed.update_draft",
    "read",
    "social.search",
    "write",
]
feed_story_stepid = "feed_story_step"
name = "Feed Story Writer"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "feed.finish_step",
    "feed.update_draft",
    "read",
    "write",
]
feed_wire_exchange_stepid = "feed_wire_exchange_step"
name = "Feed Wire Exchange Desk"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_open",
    "browser_search",
    "feed.exchange_search",
    "feed.finalize_unit",
    "feed.finish_step",
    "feed.search_coverage",
    "read",
    "social.search",
]
feed_wire_stepid = "feed_wire_step"
name = "Feed Wire Desk"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_open",
    "browser_search",
    "feed.finalize_unit",
    "feed.finish_step",
    "feed.search_coverage",
    "read",
    "social.search",
]
id = "feed_workflow_step"
name = "Feed Workflow Step"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "full"
tools = [
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "context_fetch",
    "db",
    "exec",
    "feed.exchange_search",
    "feed.finalize_unit",
    "feed.finish_step",
    "feed.search_coverage",
    "feed.update_draft",
    "feed.update_report",
    "memory_get",
    "memory_search",
    "read",
    "session_status",
    "social.search",
    "tracking.get",
    "tracking.list",
    "tracking.search",
    "user_goal.get",
    "user_goal.list",
    "user_goal.search",
    "write",
]
id = "foreground_root"
name = "Foreground Root"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "deferred"
prompt_gates = ["stateful_artifact_sharing"]
schema_gates = ["artifact_icon_generation", "halloween_avatar", "proactivity_delivery_owns_timing"]
tools = [
    "ads.resolve_entities",
    "artifact.add_builtin",
    "artifact.cancel",
    "artifact.create_file",
    "artifact.create_web_fullstack",
    "artifact.create_web_static",
    "artifact.delete",
    "artifact.edit",
    "artifact.export",
    "artifact.inspect",
    "artifact.invoke_action",
    "artifact.list",
    "artifact.list_actions",
    "artifact.send_input",
    "artifact.share",
    "artifact.status",
    "artifact.unshare",
    "avatar.clear",
    "avatar.create",
    "avatar.create_avatar_share_widget",
    "avatar.edit",
    "avatar.get",
    "avatar.set",
    "avatar.wear",
    "browser.browse",
    "browser.profiles",
    "browser.windows",
    "browser_deep_research",
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "chat.archive",
    "chat.configure_connection",
    "chat.connection_status",
    "chat.create",
    "chat.delete",
    "chat.disconnect",
    "chat.list",
    "chat.read_messages",
    "chat.rename",
    "chat.send_message",
    "chat.unarchive",
    "connector_search",
    "create_options",
    "credentials.list",
    "credentials.request_api_access",
    "credentials.request_login",
    "credentials.request_new_password",
    "cron.add",
    "cron.list",
    "cron.remove",
    "cron.run",
    "cron.runs",
    "cron.status",
    "cron.stop",
    "cron.update",
    "cron.view",
    "db",
    "device.describe",
    "device.invoke",
    "device.list",
    "device.unpair",
    "edit",
    "end_voice_call",
    "exec",
    "feed.inspect_logs",
    "feed.prompt_get",
    "feed.prompt_reset",
    "feed.prompt_update",
    "feed.regenerate",
    "feed.search",
    "feed.status",
    "feed.unit_create",
    "feed.unit_delete",
    "feed.unit_get",
    "feed.unit_list",
    "feed.unit_reorder",
    "feed.unit_update",
    "forget.confirm",
    "forget.plan",
    "get_current_voice",
    "hooks.add",
    "hooks.disable",
    "hooks.dry_run",
    "hooks.enable",
    "hooks.list",
    "hooks.logs",
    "hooks.remove",
    "hooks.run",
    "hooks.update",
    "hooks.view",
    "idea.create_idea_widget",
    "idea.get",
    "idea.list",
    "idea.list_starters",
    "idea.search",
    "idea.share",
    "mail_handoff",
    "mail_setup_card",
    "mail_status",
    "map.geocode",
    "map.navigation",
    "map.reverse_geocode",
    "media.generate_icon",
    "media.generate_image",
    "media.generate_video",
    "memory_explain",
    "memory_get",
    "memory_search",
    "nothing_to_do",
    "offer_preference",
    "onboarding.create_name_widget",
    "onboarding.update_identity",
    "peer.confirm_person",
    "peer.decline_person",
    "peer.invite_accept",
    "peer.invite_create",
    "peer.list_contacts",
    "peer.resolve",
    "peer.set_access",
    "permissions.history",
    "permissions.list_active",
    "permissions.list_pending",
    "phone.answer_call_question",
    "phone.begin_call",
    "phone.call_status",
    "phone.cancel_call",
    "phone.list_calls",
    "phone.place_call",
    "phone.poll_call",
    "phone.prepare_call",
    "phone.schedule_call",
    "phone.set_voice",
    "phone.test_call",
    "phone.unschedule_call",
    "phone.verify_number",
    "proactivity.read",
    "proactivity.read_source",
    "proactivity.select",
    "process.clear",
    "process.kill",
    "process.list",
    "process.log",
    "process.poll",
    "process.send_keys",
    "process.write",
    "react_to_user_message",
    "read",
    "record_mail_processing",
    "session_status",
    "set_preferred",
    "set_voice_call_mute",
    "set_voice_preference",
    "shopping.create_shopping_cart_widget",
    "shopping.create_shopping_results_widget",
    "shopping.read_cart",
    "shopping.resolve_results",
    "skill_search",
    "social.search",
    "space.get_tab_order",
    "space.set_placement",
    "space.set_tab_order",
    "subagent.close",
    "subagent.list",
    "subagent.resume",
    "subagent.send",
    "subagent.spawn",
    "todo.write",
    "tool_search.load_tool_namespace",
    "tracking.create",
    "tracking.create_entry",
    "tracking.delete",
    "tracking.delete_entry",
    "tracking.get",
    "tracking.list",
    "tracking.search",
    "tracking.set_status",
    "tracking.update",
    "tracking.update_entry",
    "trash.list",
    "trash.put",
    "trash.restore",
    "travel.create_hotel_results_widget",
    "ui.create_navigation_widget",
    "ui.list",
    "ui.navigate",
    "ui.set",
    "user_goal.create",
    "user_goal.create_entry",
    "user_goal.delete",
    "user_goal.delete_briefing",
    "user_goal.delete_entry",
    "user_goal.get",
    "user_goal.list",
    "user_goal.search",
    "user_goal.set_status",
    "user_goal.update",
    "user_goal.update_entry",
    "visual_grounding",
    "voice_options",
    "voice_preview",
    "wallet.add_payment_method",
    "wallet.get_connection_status",
    "wallet.get_user_info",
    "wallet.list_payment_methods",
    "wallet.list_shipping_addresses",
    "widget.create_html_file_widget",
    "widget.create_html_widget",
    "widget.create_image_picker_widget",
    "widget.create_letter_widget",
    "widget.create_list_widget",
    "widget.create_map_widget",
    "widget.present",
    "widget.state",
    "worker.update_discretion",
    "workflow.create",
    "workflow.delete",
    "workflow.launch",
    "workflow.launch_async",
    "workflow.list",
    "workflow.list_runs",
    "workflow.pause",
    "workflow.resume",
    "workflow.save_run",
    "workflow.stop",
    "workflow.stop_agent",
    "workflow.update",
    "workflow.view",
    "workflow.view_run",
    "write",
]

[[gated_tools]]
tool = "artifact.add_builtin"
gate = "candy_run"

[[gated_tools]]
tool = "artifact.share"
gate = "stateful_artifact_sharing"

[[gated_tools]]
tool = "avatar.wear"
gate = "avatar_wardrobe"

[[gated_tools]]
tool = "browser_deep_research"
gate = "research_browser"

[[gated_tools]]
tool = "end_voice_call"
gate = "voice_options"

[[gated_tools]]
tool = "get_current_voice"
gate = "voice_options"

[[gated_tools]]
tool = "idea.share"
gate = "share_ideas_skill"

[[gated_tools]]
tool = "mail_handoff"
gate = "muse_mail"

[[gated_tools]]
tool = "mail_setup_card"
gate = "muse_mail"

[[gated_tools]]
tool = "mail_status"
gate = "muse_mail"

[[gated_tools]]
tool = "map.navigation"
gate = "navigation"

[[gated_tools]]
tool = "peer.confirm_person"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.decline_person"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.invite_accept"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.invite_create"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.list_contacts"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.resolve"
gate = "agent_to_agent"

[[gated_tools]]
tool = "peer.set_access"
gate = "agent_to_agent"

[[gated_tools]]
tool = "phone.answer_call_question"
gate = "phone"

[[gated_tools]]
tool = "phone.begin_call"
gate = "phone"

[[gated_tools]]
tool = "phone.call_status"
gate = "phone"

[[gated_tools]]
tool = "phone.cancel_call"
gate = "phone"

[[gated_tools]]
tool = "phone.list_calls"
gate = "phone"

[[gated_tools]]
tool = "phone.place_call"
gate = "phone"

[[gated_tools]]
tool = "phone.poll_call"
gate = "phone"

[[gated_tools]]
tool = "phone.prepare_call"
gate = "phone"

[[gated_tools]]
tool = "phone.schedule_call"
gate = "phone"

[[gated_tools]]
tool = "phone.set_voice"
gate = "phone"

[[gated_tools]]
tool = "phone.test_call"
gate = "phone_self_test"

[[gated_tools]]
tool = "phone.unschedule_call"
gate = "phone"

[[gated_tools]]
tool = "phone.verify_number"
gate = "phone"

[[gated_tools]]
tool = "proactivity.read_source"
gate = "proactivity_source_read"

[[gated_tools]]
tool = "record_mail_processing"
gate = "muse_mail"

[[gated_tools]]
tool = "set_voice_call_mute"
gate = "voice_options"

[[gated_tools]]
tool = "set_voice_preference"
gate = "voice_options"

[[gated_tools]]
tool = "space.get_tab_order"
gate = "spaces"

[[gated_tools]]
tool = "space.set_placement"
gate = "spaces"

[[gated_tools]]
tool = "space.set_tab_order"
gate = "spaces"

[[gated_tools]]
tool = "voice_options"
gate = "voice_options"

[[gated_tools]]
tool = "voice_preview"
gate = "voice_spoken_preview"

[[gated_tools]]
tool = "widget.create_image_picker_widget"
gate = "smb_product_shots_skill"
generic_subagent_depth1id = "generic_subagent_depth1"
name = "Generic Subagent Depth 1"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "deferred"
prompt_gates = ["stateful_artifact_sharing"]
schema_gates = ["artifact_icon_generation", "halloween_avatar"]
tools = [
    "artifact.cancel",
    "artifact.create_file",
    "artifact.create_web_fullstack",
    "artifact.create_web_static",
    "artifact.delete",
    "artifact.edit",
    "artifact.export",
    "artifact.inspect",
    "artifact.invoke_action",
    "artifact.list",
    "artifact.list_actions",
    "artifact.send_input",
    "artifact.status",
    "avatar.clear",
    "avatar.create",
    "avatar.create_avatar_share_widget",
    "avatar.edit",
    "avatar.get",
    "avatar.set",
    "avatar.wear",
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "chat.list",
    "chat.read_messages",
    "connector_search",
    "create_options",
    "cron.add",
    "cron.list",
    "cron.remove",
    "cron.run",
    "cron.runs",
    "cron.status",
    "cron.update",
    "cron.view",
    "db",
    "device.describe",
    "device.invoke",
    "device.list",
    "device.unpair",
    "edit",
    "exec",
    "feed.unit_create",
    "hooks.add",
    "hooks.disable",
    "hooks.dry_run",
    "hooks.enable",
    "hooks.list",
    "hooks.logs",
    "hooks.remove",
    "hooks.run",
    "hooks.update",
    "hooks.view",
    "idea.create_idea_widget",
    "idea.get",
    "idea.list",
    "idea.list_starters",
    "idea.search",
    "mail_handoff",
    "map.geocode",
    "map.navigation",
    "map.reverse_geocode",
    "media.generate_icon",
    "media.generate_image",
    "media.generate_video",
    "memory_explain",
    "memory_get",
    "memory_search",
    "nothing_to_do",
    "permissions.history",
    "permissions.list_active",
    "permissions.list_pending",
    "phone.poll_call",
    "process.clear",
    "process.kill",
    "process.list",
    "process.log",
    "process.poll",
    "process.send_keys",
    "process.write",
    "read",
    "shopping.create_shopping_cart_widget",
    "shopping.create_shopping_results_widget",
    "skill_search",
    "social.search",
    "space.set_placement",
    "subagent.close",
    "subagent.list",
    "subagent.resume",
    "subagent.send",
    "subagent.spawn",
    "tool_search.load_tool_namespace",
    "tracking.create",
    "tracking.create_entry",
    "tracking.delete",
    "tracking.delete_entry",
    "tracking.get",
    "tracking.list",
    "tracking.search",
    "tracking.set_status",
    "tracking.update",
    "tracking.update_entry",
    "trash.list",
    "trash.put",
    "trash.restore",
    "ui.create_navigation_widget",
    "user_goal.create",
    "user_goal.create_entry",
    "user_goal.delete",
    "user_goal.delete_briefing",
    "user_goal.delete_entry",
    "user_goal.get",
    "user_goal.list",
    "user_goal.search",
    "user_goal.set_status",
    "user_goal.update",
    "user_goal.update_entry",
    "visual_grounding",
    "widget.create_html_file_widget",
    "widget.create_html_widget",
    "widget.create_letter_widget",
    "widget.create_list_widget",
    "widget.create_map_widget",
    "workflow.create",
    "workflow.delete",
    "workflow.launch",
    "workflow.launch_async",
    "workflow.list",
    "workflow.list_runs",
    "workflow.pause",
    "workflow.resume",
    "workflow.save_run",
    "workflow.stop",
    "workflow.stop_agent",
    "workflow.update",
    "workflow.view",
    "workflow.view_run",
    "write",
]

[[gated_tools]]
tool = "avatar.wear"
gate = "avatar_wardrobe"

[[gated_tools]]
tool = "mail_handoff"
gate = "muse_mail"

[[gated_tools]]
tool = "map.navigation"
gate = "navigation"

[[gated_tools]]
tool = "phone.poll_call"
gate = "phone"

[[gated_tools]]
tool = "space.set_placement"
gate = "spaces"
generic_subagent_depth2id = "generic_subagent_depth2"
name = "Generic Subagent Depth 2"
model = "session"
provider = "model_registry"
reasoning_strength = "session"
tool_loading = "deferred"
schema_gates = ["halloween_avatar"]
tools = [
    "avatar.clear",
    "avatar.create",
    "avatar.create_avatar_share_widget",
    "avatar.edit",
    "avatar.get",
    "avatar.set",
    "avatar.wear",
    "browser_find",
    "browser_lookup_citation_url",
    "browser_open",
    "browser_search",
    "chat.list",
    "chat.read_messages",
    "connector_search",
    "create_options",
    "cron.add",
    "cron.list",
    "cron.remove",
    "cron.run",
    "cron.runs",
    "cron.status",
    "cron.update",
    "cron.view",
    "db",
    "device.describe",
    "device.invoke",
    "device.list",
    "device.unpair",
    "edit",
    "exec",
    "feed.unit_create",
    "hooks.add",
    "hooks.disable",
    "hooks.dry_run",
    "hooks.enable",
    "hooks.list",
    "hooks.logs",
    "hooks.remove",
    "hooks.run",
    "hooks.update",
    "hooks.view",
    "idea.create_idea_widget",
    "idea.get",
    "idea.list",
    "idea.list_starters",
    "idea.search",
    "mail_handoff",
    "map.geocode",
    "map.navigation",
    "map.reverse_geocode",
    "media.generate_icon",
    "media.generate_image",
    "media.generate_video",
    "memory_explain",
    "memory_get",
    "memory_search",
    "nothing_to_do",
    "permissions.history",
    "permissions.list_active",
    "permissions.list_pending",
    "process.clear",
    "process.kill",
    "process.list",
    "process.log",
    "process.poll",
    "process.send_keys",
    "process.write",
    "read",
    "shopping.create_shopping_cart_widget",
    "shopping.create_shopping_res