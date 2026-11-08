# Home Assistant on This VM: Install and Setup Without a Browser

**Last verified:** 2026-10-29 with Home Assistant Core 2026.10.4 on a
uv-managed Python 3.14.10

Use this guide whenever Home Assistant on this VM comes up: to check on it,
install, start, stop, update or remove it, set it up, or add an integration.

## Why Not the Browser

- The browser cannot open a server on this VM. It runs on separate,
  isolated infrastructure, so `localhost` there is not this VM, and private
  addresses are refused. Do not retry `127.0.0.1:8123` in the browser.

- Every setup step the onboarding screens perform has a documented HTTP
  API. Call it with `exec` on `http://127.0.0.1:8123`. Loopback requests stay
  on the VM, need no proxy and raise no approval.

## The `home-assistant` Command

- Muse ships Home Assistant's install, its service and its setup. Do every
  lifecycle step with `/opt/muse/assets/home-assistant/home-assistant`, never
  by hand: do not install packages, write unit files, or onboard with your
  own requests. Each command prints one JSON object; `"ok": false` comes with
  an `error` to report.

| Command | What it does |
|---|---|
| `status` | Reports the state below; changes nothing |
| `install` | Installs, repairs, or upgrades to the release this Muse version pins, then starts it |
| `start` / `stop` | Starts Home Assistant and keeps it running, or stops it and keeps it stopped |
| `setup` | Onboards Home Assistant and stores its access token; resumes an interrupted setup |
| `rollback` | Returns to the release before the last upgrade and its database, setting aside changes made since; only with the user's agreement (see Install) |

- Read `status` before acting, and again after any command:

| Field | Meaning |
|---|---|
| `installed` | The Muse install exists in `~/homeassistant` |
| `running` / `ready` | The service runs / its API answers outside recovery mode. The first start can take minutes |
| `recovery_mode` | Home Assistant started in recovery mode, usually because its first-start downloads failed |
| `onboarded` / `credentials` | Setup is finished / the stored token works (`valid`, `invalid`, `missing`) |
| `link_routing` | Home Assistant is running and sends home-network traffic through the Home Link |
| `integrations` | Each integration the user added, with `connected` true only once it loaded |
| `update_available` | A newer pinned release is ready to install |
| `other_installs` | A Home Assistant installed some other way, when the Muse install is absent |
| `install_interrupted` | An install or rollback stopped partway; the service stays off until `start` or `install` finishes or undoes it |

## Install

- Install only after the user agrees, either by asking for it or by picking
  an offer to set it up: run `install`. Its downloads from GitHub and PyPI
  can each wait for an approval, so do not cap it with a short timeout.
  Running it again is safe. If they passed on an offer, do not raise it
  again unless they bring up Home Assistant.

- If `status` lists `other_installs`, check `trash.list` for a removed
  `~/homeassistant` first. If there is one, it holds the user's most recent
  Muse setup, and what was found elsewhere may be an older setup or the
  leftovers of an earlier move: offer to restore the removed setup (Remove
  Home Assistant, below) instead. Otherwise tell the user before installing
  where the other install is and offer to move it over: stop it and remove
  what starts it, copy its configuration directory to
  `~/homeassistant/config` only if that directory is missing or empty, then
  run `install`. Its integrations and owner account come along.

- On its first start Home Assistant downloads more packages and asks the user
  to let it reach PyPI (`pypi.org`, `files.pythonhosted.org`); tell them to
  expect those cards. If its downloads failed before the user answered, it
  starts in recovery mode: once the user has approved, if `recovery_mode` is
  true or `ready` stays false, run `stop` and then `start`.

- When `update_available` is true, tell the user, and run `install` only
  after they agree: an upgrade migrates Home Assistant's database.

- If an upgraded release misbehaves and `rollback_available` is true, you can
  offer `rollback`. Explain first that it restores the database and settings
  from before the upgrade, so history, settings and integrations changed since
  then are set aside, and run it only after the user agrees to that. It keeps
  what it replaced in the `replaced_database` directory it reports.

## Run, Stop and Start

- Once installed, Home Assistant keeps running, including after a VM restart,
  until the user asks to stop it: run `stop`, and `start` to resume.

- If `install_interrupted` is true, run `start`; it finishes or undoes the
  interrupted change first. Then read `status` again.

- If `running` is true but `link_routing` is false, a newer routing module
  applies at the next start, and `start` alone does nothing on a running
  service: to restart, run `stop` and then `start`, then read `status` again.

- If `running` is false although it was not stopped, read `journalctl -u
  home-assistant.service`, fix the cause, then run `start`. Report a failure
  you cannot fix instead of retrying.

- Never delete, disable or mask `home-assistant.service` or
  `home-assistant-ensure.timer`, and never write a replacement. Muse provides
  them on every VM, including VMs without Home Assistant.

## Set It Up

- When `ready` is true and `onboarded` is not, or `credentials` is not
  `valid`, run `setup`. It creates the owner account with a generated
  password, stores the password and a long-lived access token in
  `~/homeassistant/config/muse_owner.json` (mode 0600), and resumes from the
  stored password if it stopped partway.

- If `setup` reports an owner without stored credentials, Home Assistant was
  set up some other way; ask the user how they want to sign in.

- Use the token for the API calls below. Read it from that file inside the
  command that uses it, never by printing it. Never show the password or
  token in chat, even when asked.

## Remove Home Assistant

- Only when the user asks to remove it: run `stop`, then move the whole
  `~/homeassistant` directory to the trash with `trash.put`, and check that it
  succeeded; if it did not, stop and report that. It holds the configuration,
  owner account and token, and any database copies kept by upgrades
  (`previous/`) and rollbacks (`replaced-*`). Tell the user it can be
  restored for 30 days.

- To bring a removed setup back: if `~/homeassistant` exists again, run
  `stop`, move it to the trash with `trash.put` and check it succeeded. Then
  find the removed entry with `trash.list`, `trash.restore` it to
  `~/homeassistant`, check that it succeeded, and run `start`, which resumes
  it at the release it had. Then read `status`: if `update_available` is
  true, handle it as an update, which needs the user's agreement.

## Add an Integration

- Integrations are added through config flows over HTTP on
  `http://127.0.0.1:8123`, with the stored token as a bearer token:

| Action | Request |
|---|---|
| Start a flow | `POST /api/config/config_entries/flow` with `{"handler": "<domain>"}` |
| Answer a step | `POST /api/config/config_entries/flow/<flow_id>` with the fields of the returned `data_schema` |
| List entries | `GET /api/config/config_entries/entry` |

- Read each reply's `type`. `form` asks for the next step's fields, `abort`
  gives a reason, and `create_entry` means it is done. Before reporting
  success, check that `status` lists the integration as `connected`.

- If a form asks for a third-party password or API key, stop that flow. The
  user has no Home Assistant screen to enter it on, and the credential must not
  pass through chat. Tell the user that this integration cannot be set up from
  Muse yet.

## Reaching Home Devices

- While `status` reports `link_routing`, Home Assistant reaches private
  home-network addresses through the Link. Its other connections leave the VM as usual.

- Add a device by the IPv4 address and port from a fresh Link discovery. Home
  Assistant's own discovery (mDNS, SSDP and other UDP or multicast protocols)
  does not cross the Link, and neither do integrations that need UDP.

- The first connection to each device raises a Home Link approval for that
  address. Tell the user to expect it. Setup can fail while the approval waits;
  after the user answers, start the integration's config flow again.

- Before telling the user a device works, check that `status` lists its
  integration as `connected` and read one of its states.
channel-availability.mdchannels/telegram.mdchannels/whatsapp.mdchannels/messenger.mdapp.mdpython_space_migration.mdhtml-widgets.mdworkflows.mddevices/coop_ai_device.mddevices/malibu.mddevices/phones.mddevices/hatch_link.mdcommunications.mdchannels/groups.mddevices/homehub.md# Voice

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

Publishing gives a page or app a share link. Invite lets the user make it
public or limit access to selected people. Invite is in its menu;
platform locations are in `~/docs/client-surfaces.md`.

- Shared pages and apps usually publish later successful builds.
  `artifact.unshare` takes a link down.
- To publish or change sharing, open Invite with `ui.navigate` target
  `space.share` if `ui.list` shows it; the user decides there. Otherwise,
  tell them where Invite is. Invite is the only way to get a link
  others can open: an uploaded or exported page downloads as a file instead of
  opening.
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
