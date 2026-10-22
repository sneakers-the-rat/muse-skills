### Goal

Explore the brief, test the data assumptions, decide the design, then call `web_artifacts.finalize_plan`. Do not edit the artifact source until the plan has been submitted successfully. Scratch files under `/tmp` are allowed for probes.

### Explore

1. Resolve handed-off source material before planning: read or probe any workspace path, URL, attachment, durable id, or handed-off query now, and use only what that source returns. The user's own material (memory notes, chat history, workspace files) enters the artifact only when the request makes it relevant, and a page built for other people carries the minimum of the user's world the ask requires. A fixed `<source> query "..." returned: "..."` provenance line records an already executed result; do not rerun it, and treat only its exact returned span as authoritative. When a conversion names no accessible source, read the parent conversation with `chat.read_messages` before blocking; if that still yields nothing usable, take the ask exit below instead of inventing the source.

2. Test every external source you plan to use with a real invocation that returns useful content for this artifact's query, region, date, or account. CLI or HTTP: `which <cli>`, a real read command, `curl -s '<api-url>' | head -100`. For the user's own content on a connected service (saved posts, likes, playlists, mail), look for that service's connector doc with `muse.connector_search` first; when one exists, read its `