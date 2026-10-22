# Artifacts

Artifacts are what you build for the user, and the main way to
deliver anything bigger than a chat message. There are three kinds:

- Documents: generated files (PDF, Word, spreadsheets, slide decks,
  markdown). Once downloaded, they are the user's to keep and work
  offline like any file.
- Pages: static websites hosted live from your computer. Nothing
  installs on the user's device and there is no offline mode.
- Interactive apps: hosted live like pages, and they can also store
  their own data. Pages and documents hold no live state of their own.

An artifact and its data live on your computer, in the user's own
Muse environment: an interactive app keeps its records in its own
database there, persisting across restarts and updates. Nothing is
hosted anywhere else until the user publishes.

## Location

Artifacts live in the Library on every platform. On web, you can
navigate directly via the /artifacts URL.
Library mechanics (what collects there and how downloads work) are in
`~/docs/files-and-library.md`. Per-platform screen layouts are in
`~/docs/client-surfaces.md`.

## Sharing & Publishing

Publishing gives an artifact a share link. On web, Share settings let the user
make it public or limit access to selected people. Share is in the artifact menu;
platform locations are in `~/docs/client-surfaces.md`.

- On web, Share opens Publish settings: publish once, or turn on automatic
  publishing (off by default) so later successful builds publish without
  asking again. Native apps keep their existing controls.
- To publish or change sharing, the user opens the artifact and chooses Share
  from its menu.
- A finished build isn't proof of publication. Report any returned publication
  failure. `artifact.status` checks publication and returns the share link
  when the user asks. It does not report the audience; direct audience questions
  to the artifact's Share settings.
- If content review blocks publishing, say this version can't be published.
  Offer to remove, redact, or anonymize the flagged details or keep it private.
  Never distribute the blocked content unchanged in another format or channel.
- The share link shows the last published version. Turning off automatic
  publishing keeps the link and its audience; Stop sharing takes it down and
  turns off automatic publishing. Unpublished artifacts are visible only to
  their owner.

Artifacts have no direct social-post action. Users can share individual chat
messages through the platform share sheet; connector posting capabilities are
in `~/docs/connectors.md`.

## Deletion

Deleting an artifact is permanent: it removes the artifact and its data,
tears down hosting, and revokes any share. The 30 day trash for
workspace files is separate and not available for Artifacts. Always warn
the user before deleting an artifact. `artifact.list` is the source of
truth for which pages and apps exist (documents are files in
`workspace/your_files` or a goal's `files` folder); a claim that nothing
was deleted is only as good as a fresh listing.
