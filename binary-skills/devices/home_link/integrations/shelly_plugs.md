# Shelly Plugs (Gen 4): Switching and Power Metering

**Last verified:** 2026-09-21 on a Shelly Plug US Gen 4 (model S4PL-00116US,
firmware 2.0.0)

Use this guide when fresh discovery identifies a Shelly smart plug and the user
asks to switch it or to read what it is drawing.

## Identifying the Plug

- **mDNS** is the strongest signal. Shelly plugs advertise over `_http._tcp`
  with a hostname built from the model and the device MAC, such as
  `ShellyPlugUSG4-<MAC>.local`, where `<MAC>` is the twelve hex digits with no
  separators. The device reports its own MAC the same way, without colons.
- **The MAC vendor prefix** is supporting evidence, not proof. Shelly hardware
  has shipped under more than one prefix, so a match is a positive signal and a
  miss proves nothing. Resolve the current prefixes the way
  `~/docs/devices/home_link.md` requires: look up the manufacturer's public
  vendor prefixes, then compare them against the discovery result locally.
  Send only a vendor prefix to an online lookup, never a full MAC address.
- **Confirm before acting.** Request `Shelly.GetDeviceInfo` and check `model`,
  `app`, and `gen`. That answer, not the hostname, is what establishes the
  device is what you think it is.

Addresses are DHCP by default. Identify the plug by MAC or hostname and take
its address from the current discovery result every time. Never reuse a
remembered address.

## Check the Generation First

The API depends on the generation, and the two are not compatible.

- `gen` 2 or higher, which covers Gen 4, uses the RPC API described below.
- `gen` 1 predates RPC entirely and uses `/relay/0?turn=on`. If you find a
  Gen 1 device, the rest of this guide does not apply.

## Recommended Path

1. Re-discover the plug and take its address and port from the current result.
2. Reach it through the Home Link CONNECT proxy. It serves a documented HTTP
   API, so the HTTP section of `~/docs/devices/home_link.md` applies,
   including its approval and redirect rules.
3. Call `Shelly.GetDeviceInfo` to confirm the model and generation, and to read
   `auth_en`.
4. Read `Switch.GetStatus?id=0` before acting, so you know the state you are
   changing and can tell a no-op from a real change. A plug has one switch, at
   `id=0`.
5. Switch with `Switch.Set?id=0&on=true` or `on=false`. The reply is
   `{"was_on": <bool>}`, which is the state *before* the call, not the result.
   Treating it as the new state inverts the meaning.
6. Read the state back. `Switch.GetStatus?id=0` gives `output` for the relay
   and `apower` for watts actually drawn. `output` alone says the relay moved;
   `apower` is what shows the attached load responded. Confirm both before
   telling the user it worked.

For an action that should not be left latched on, `Switch.Set` also accepts
`toggle_after=<seconds>`, which reverts the plug without needing a second call
to survive.

## Endpoints

| Action | Path |
|---|---|
| Device model, generation, firmware, `auth_en` | `/rpc/Shelly.GetDeviceInfo` |
| Full device status | `/rpc/Shelly.GetStatus` |
| One switch's status | `/rpc/Switch.GetStatus?id=0` |
| Turn on or off | `/rpc/Switch.Set?id=0&on=true` |
| Turn on or off, reverting later | `/rpc/Switch.Set?id=0&on=true&toggle_after=60` |
| Toggle | `/rpc/Switch.Toggle?id=0` |
| Switch configuration, including auto-off | `/rpc/Switch.SetConfig` |
| Schedules | `/rpc/Schedule.List`, `Schedule.Create`, `Schedule.Delete` |

## Auth

Read `auth_en` from `Shelly.GetDeviceInfo` rather than assuming. A plug on a
home network is often left unauthenticated, and plain HTTP works. That is a
property of the individual device, not of the model.

When `auth_en` is true the device wants HTTP digest auth, and the user name is
always `admin`. Do not put the password in the command. If no stored credential
exists for the plug, follow the credential rules in
`~/docs/devices/home_link.md` and explain that setup is required.

## Other Capabilities

Worth knowing about, though most requests will not need them:

- Power metering beyond `apower`: voltage, current, frequency, and cumulative
  energy in watt-hours under `aenergy`, with recent per-minute history.
- A built-in light sensor, reported under `illuminance:0`.
- Overpower and overcurrent protection thresholds, in the switch config.
- BLE and BTHome, MQTT, the vendor cloud, and Matter. These are alternative
  control planes. Prefer the local RPC API over the network the Link already
  reaches.
enabledchannel-availability.mdchannels/telegram.mdchannels/whatsapp.mdchannels/messenger.mdapp.mdpython_space_migration.mdhtml-widgets.mdworkflows.mddevices/coop_ai_device.mddevices/malibu.mddevices/phones.mddevices/hatch_link.mdcommunications.mdchannels/groups.mddevices/homehub.md# Voice

Live voice conversations in the app are not available on this account.

Dictation and voice notes work on both mobile apps. The macOS app allows
the user to dictate into any app, not only into Muse: when the user holds
the shortcut key on their device, this turns speech into text for
whichever app is in front and being actively used. Speaking a message with
the composer mic becomes a text message. Voice notes sent in the app or
over linked channels are transcribed like any other message.

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

Dictation and voice notes work on both mobile apps. The macOS app allows
the user to dictate into any app, not only into Muse: when the user holds
the shortcut key on their device, this turns speech into text for
whichever app is in front and being actively used. Speaking a message with
the composer mic becomes a text message. Voice notes sent in the app or
over linked channels are transcribed like any other message.

A voice conversation takes place in the Muse app and does not dial a
telephone number. You have no phone number for receiving calls. For
telephone calling capabilities and availability, see
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
