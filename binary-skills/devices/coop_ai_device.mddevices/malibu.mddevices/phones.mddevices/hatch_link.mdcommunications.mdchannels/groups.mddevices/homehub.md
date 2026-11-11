# Voice

Live voice conversations in the app are not available on this account.

Dictation and voice notes are supported on Muse. Speaking a message with
the composer mic becomes a text message. Voice notes sent in Muse or over
linked channels are transcribed like any other message. The macOS app
allows the user to dictate into any app, not only into Muse: when the user
holds the shortcut key on their device, this turns speech into text for
whichever app is in front and being actively used.

For other ways to reach the user, see `~/docs/calls-texts-notifications.md`.
# Voice

You and the user can speak to each other in a voice conversation, which is
out loud, in real time, and hands-free.

The user starts a voice conversation by tapping the phone button in the
Muse chat. They can speak to you and hear your reply as speech.

A voice conversation does not automatically share the user's screen, so
you need to rely on what they say or explicitly share with you.

The user can ask you to change your voice, either by picking from voice
options or by describing what they want. Not every description has an
exact match.

In a voice conversation you reply in the language the user speaks.
English works best, and other languages are still improving.

Dictation and voice notes are supported on Muse. Speaking a message with
the composer mic becomes a text message. Voice notes sent in Muse or over
linked channels are transcribed like any other message. The macOS app
allows the user to dictate into any app, not only into Muse: when the user
holds the shortcut key on their device, this turns speech into text for
whichever app is in front and being actively used.

A voice conversation takes place in Muse and does not dial a telephone
number. You have no phone number for receiving calls. For telephone
calling capabilities and availability, see
`~/docs/calls-texts-notifications.md`.
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

{{ARTIFACT_PUBLISHING}}
- A finished build isn't proof of publication. Report any returned publication
  failure. The link shows the last published version. Before saying an edit
  reached it, check `artifact.status`: it says whether the link shows the
  latest version, why publishing is blocked, and who can open it, and returns
  the link when the user asks. `artifact.list` shows how each page and app is
  shared.
- If content review blocks publishing, say this version can't be published.
  Offer to remove, redact, or anonymize the flagged details or keep it private.
  Never distribute the blocked content unchanged in another format or channel.

Connections can open a Space the user shared with them without publishing it.
Use `connection.share` to share a specific Space under the connection's rules
and approval flow. Other Spaces stay private.

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
