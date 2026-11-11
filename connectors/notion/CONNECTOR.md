# Notion

- Notion holds the user's pages, notes and databases. Run `/opt/hatch/bin/notion-cli`, which calls Notion's hosted MCP server.

## Connect

- Run `status` before any other work. If it reports `not_connected`, run `authorize-url` and share exactly `[Connect Notion](<connect_url>)`, without the raw URL, then wait for the user to finish. Never ask for tokens in chat or edit the stored credentials.

- After the user authorizes, the sign-in completes on its own. Run `status` again, and once it reports `connected`, its output also lists the tool names.

- If the sign-in does not complete on its own and the user has an authorization code, finish it with `exchange-code --code CODE`.

- A 401 triggers an automatic token refresh. If calls keep failing with `unauthorized`, run `refresh` or ask the user to authorize again. Run `disconnect` only when the user asks to disconnect.

```text
/opt/hatch/bin/notion-cli status
/opt/hatch/bin/notion-cli authorize-url
/opt/hatch/bin/notion-cli refresh
```

## Find and call a tool

- Never guess a tool name or argument shape.

- Find the tool with `list-tools`, which gives each tool's name and a one-line description.

- Before the first call of a write tool, or of any tool whose argument shape you haven't seen, run `describe-tool --name <tool>` and read its whole description and `input_schema`.

- `--arguments-json` must be one JSON object, and arrays or bare values are rejected.

- When `call-tool` returns `ok: false`, `error` says why; for a Notion tool error it holds Notion's message. A validation error means the arguments were wrong, so correct them against the schema instead of telling the user Notion can't do the task.

```text
/opt/hatch/bin/notion-cli list-tools
/opt/hatch/bin/notion-cli describe-tool --name <tool>
/opt/hatch/bin/notion-cli call-tool --name <tool> --arguments-json '<json-object>'
```

- `notion-search` finds pages and returns titles and links, and `notion-fetch` reads a page. Pages, folders, databases and views have their own create and update tools, and comments and attachments have create tools.

- When the user has set page content access to ask or deny, searches that return page content, such as `notion-ai-search` and the data source queries, are refused. Plain `notion-search` still returns titles and links.

## Read or edit the workspace

- Find the page or database and read its current structure before changing it. Use the IDs, pagination fields and update format from the schema.

- Confirm the user's intent before changing pages, databases or blocks. Each change also asks for approval as the user's connector settings require.

- After an uncertain write, read the target before trying again, because Notion may already have made the change.

- Read results keep Notion's raw dates and add UTC and local forms for creation and edit times and for timed properties. Date-only properties stay dates and must not be read as UTC instants.

## Add rows to a database

- Fetch the database with `notion-fetch`. The result lists each data source with its `collection://` URL and properties. If there are several, use the one the user means.

- Call `notion-create-pages` with a top-level `"parent": {"data_source_id": "<id>"}` and one `pages` entry per row that sets the row's properties by name. Take `<id>` from the data source's `collection://<id>` URL.

- Don't put `parent` inside a `pages` entry, because Notion rejects it.

- Don't pass `data_source_id` at the top level without `parent`. Such creates have saved pages with no title or properties.

- Fetch each new row and check its title and properties before telling the user it's saved.

## Related skills

- [Meeting Notes and Follow-ups](/opt/muse/skills/meeting-follow-up/SKILL.md)

- [Notes](/opt/muse/skills/knowledge-organization/SKILL.md)

- [Task Management](/opt/muse/skills/task-management/SKILL.md)

- Use `muse.skill_search` to find other skills and `muse.connector_search` to find other connectors.
