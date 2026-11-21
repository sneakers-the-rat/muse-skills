# reuters_claims — the Android client and the Reuters investigation

A topical view of this archive. The Android string dumps sort by
kind — every dex string in one file, every resource string in
another — so the material bearing on one subject, the claims in
the Reuters investigation of 2026-11-18 ("Meta bets big on Muse
AI agent, early safety mishaps surface"), scatters across them.
This directory regroups that material as symlinks to the canonical
files, so the claims read in one place. Nothing here is a copy.

The curated subsets under `android-strings/reuters-claims/` were
produced by `scripts/extract_android_reuters_claims.py`, which
selects lines from the generic dumps of the latest banked APK
(Android 17.0.0.4.160, from the signer-gated archive; provenance in
`android-map.json`) by the patterns recorded in each file's
header. The full investigation report lives outside this repo at
`~/workspace/android-inspect/analysis/17.0.0.4.160/REPORT.md`.

## The story, claim by claim

**Signal on Android — confirmed in code.** The article reported
Muse reading Signal messages on Android via the push-notification
permission. The mechanism is a designed feature: the manifest
declares `NodeNotificationListenerService`
(`BIND_NOTIFICATION_LISTENER_SERVICE`), which receives every
app's notifications after the originating app has decrypted them
(`manifest/`, `notifications/`). It is consumed two ways: on
demand via `notifications.get` / `notifications.action`, and
proactively — the listener republishes the whole live
notification set into the agent session as a data source, with no
invocation (`data-sources/`). The on-device policy gate does not
prompt for it by default: `notifications.get` is a read, and the
compiled HITL default is READ → ALLOW (`consent-gates/`). The
only consent moment is the one-time Android notification-access
grant under Settings → Special app access — which matches the
article's account of the permission being set up and the access
then simply working. Nothing here breaks Signal's encryption;
the read is post-decryption, at the OS layer.

**The invocation surface behind it** (`invocation/`): there is
no shell or exec on the device. A fixed, compiled-in command set
flows gateway → `HatchNodeClient` → `NodeCommandService` →
dispatcher → per-family spec handlers, and the agent-facing
descriptions of those commands — the prompts for this surface —
ship inside the APK as string constants.

**The article's other claims are not settled by this material**,
and this topic does not pretend otherwise (`other-claims/`):
the macOS accessibility/screenshot route has no counterpart in
this build (no accessibility service is declared — the computed
searches are printed there with their counts); the iPhone
contrast, the out-of-context messages that looked like other
people's data, the fabricated purchase information, and the
unauthorized Airbnb booking are server- or web-surface behaviour
that an Android APK cannot prove or refute.

## Index

## notifications (2)

The notification-listener machinery: the service, its repository and filters, the get/action commands, and the shipped prompt entries that describe notifications to the agent.

- [notifications.txt](../../android-strings/reuters-claims/17.0.0.4.160/notifications.txt) — `android-strings/reuters-claims/17.0.0.4.160/notifications.txt`
- [notifications-prompts.txt](../../android-strings/reuters-claims/17.0.0.4.160/notifications-prompts.txt) — `android-strings/reuters-claims/17.0.0.4.160/notifications-prompts.txt`

## invocation (3)

How a command reaches the phone: the node service, dispatcher and client, the expiry and session-binding strings, and the full shipped spec/prompt sets the surface is described by.

- [invocation.txt](../../android-strings/reuters-claims/17.0.0.4.160/invocation.txt) — `android-strings/reuters-claims/17.0.0.4.160/invocation.txt`
- [spec-descriptions.txt](../../android-strings/17.0.0.4.160/spec-descriptions.txt) — `android-strings/17.0.0.4.160/spec-descriptions.txt`
- [prompt-strings.txt](../../android-strings/17.0.0.4.160/prompt-strings.txt) — `android-strings/17.0.0.4.160/prompt-strings.txt`

## consent-gates (1)

The two on-device gates: Android runtime/special-access permissions, and the agent-policy HITL gate with its compiled READ → ALLOW / WRITE → ASK defaults.

- [consent-gates.txt](../../android-strings/reuters-claims/17.0.0.4.160/consent-gates.txt) — `android-strings/reuters-claims/17.0.0.4.160/consent-gates.txt`

## data-sources (2)

The quieter half: components that publish device state into the agent session as it changes, without any invocation, and their shipped descriptions.

- [data-sources.txt](../../android-strings/reuters-claims/17.0.0.4.160/data-sources.txt) — `android-strings/reuters-claims/17.0.0.4.160/data-sources.txt`
- [data-source-prompts.txt](../../android-strings/reuters-claims/17.0.0.4.160/data-source-prompts.txt) — `android-strings/reuters-claims/17.0.0.4.160/data-source-prompts.txt`

## manifest (2)

The manifest lines that matter for these claims — the listener service, the notification and screen permissions, the voice-interaction services — plus the full manifest summary.

- [manifest-relevant.txt](../../android-strings/reuters-claims/17.0.0.4.160/manifest-relevant.txt) — `android-strings/reuters-claims/17.0.0.4.160/manifest-relevant.txt`
- [manifest-summary.txt](../../android-strings/17.0.0.4.160/manifest-summary.txt) — `android-strings/17.0.0.4.160/manifest-summary.txt`

## other-claims (1)

Computed searches for the article's remaining claims in the aura-scoped strings and the manifest, with patterns, counts and the hit lines themselves.

- [absence-checks.txt](../../android-strings/reuters-claims/17.0.0.4.160/absence-checks.txt) — `android-strings/reuters-claims/17.0.0.4.160/absence-checks.txt`

## full-dumps (2)

The generic dumps the curated subsets were selected from, linked whole so any selection can be re-derived or widened.

- [dex-strings.txt](../../android-strings/17.0.0.4.160/dex-strings.txt) — `android-strings/17.0.0.4.160/dex-strings.txt`
- [resources-strings.txt](../../android-strings/17.0.0.4.160/resources-strings.txt) — `android-strings/17.0.0.4.160/resources-strings.txt`

