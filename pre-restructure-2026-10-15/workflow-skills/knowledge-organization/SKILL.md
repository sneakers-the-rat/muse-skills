# Notes

## Find the user's notes first

- When the user mentions a notebook, note or document, look where they keep notes before answering or creating anything. That may be Notion, Evernote, a Google Doc, a file in Google Drive, Dropbox or Box, or a local note. Ask one short question when several places are plausible.

- Search by title and likely words, then try variants and other locations if the first search misses. Local files say nothing about what a connected account holds.

- If the note still cannot be found, say where you looked before offering to create one.

## Add to existing notes

- Read the current note before changing it, and follow its structure, such as dated entries, headings or a running list.

- Add to the record the user named. A new local file does not fulfill a request to update an existing notebook.

- Keep IDs, links and sharing intact where the app allows, and avoid creating a second copy of the same note.

## Write a note worth keeping

- Give it a clear title, the date, a short summary and links to its sources. Keep quoted text apart from the user's own words, and put action items where the user tracks tasks, as [Task Management](/opt/muse/skills/task-management/SKILL.md) describes.

- When the user does not want to connect an app, a Markdown file under `~/workspace/notes/` works well. Tell them where you saved it.

## Organize a collection

- Organize around how the notes will be used, such as by project, topic or decision. Keep current guidance apart from history and unresolved ideas.

- Look at a few representative notes before reorganizing, and keep a structure that already works for the user. Show the proposed structure first for a large change.

- Keep moving, copying, trashing and permanent deletion distinct. After an interrupted change, check what was saved before repeating it, then verify the main links and share them.

## Available connectors

- [Notion](/opt/hatch/connectors/notion/CONNECTOR.md) for pages and databases in the user's Notion workspace.

- [Google Docs](/opt/hatch/connectors/google_docs/CONNECTOR.md) for reading and editing notes kept as Google documents.

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) for finding notebooks and documents saved in Drive.

- [Evernote](/opt/hatch/connectors/evernote/CONNECTOR.md) for searching notebooks and adding new notes.

- [Dropbox](/opt/hatch/connectors/dropbox/CONNECTOR.md) for notes and documents stored as files in Dropbox.

- [Box](/opt/hatch/connectors/box/CONNECTOR.md) for notes and documents in a Box workspace.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Readwise](/opt/hatch/connectors/readwise_mcp/CONNECTOR.md) for the user's reading highlights and saved articles.

- [Studocu](/opt/hatch/connectors/studocu_mcp/CONNECTOR.md) for study materials, courses and study projects.

## Websites

- Use `browser.spawn_task` for a notes app without a connector, signed in to the user's account. Tell it which notebook and page to open and what to add or find, and have it confirm the saved text.

- [OneNote](https://www.onenote.com/) for notebooks in a Microsoft account.

- [Google Keep](https://keep.google.com/) for quick notes and lists in a Google account.

- [iCloud Notes](https://www.icloud.com/notes/) for Apple Notes.

- [Confluence](https://www.atlassian.com/software/confluence) for a team's wiki pages, through the team's own Confluence site.

- [Evernote](https://www.evernote.com/) only to edit, move or delete existing notes, which the Evernote connector cannot do.

## Alternatives for better results

- A linked index note, or a few consistent titles and tags, often fixes retrieval without a large migration.

- An export can be enough for analysis without moving the originals.

- Ask how the user expects to find a note later when choosing between folders, tags and titles.
