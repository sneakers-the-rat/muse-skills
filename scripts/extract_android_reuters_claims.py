#!/usr/bin/env python3
"""Topical curation for the Reuters-claims topic (Android client).

Reads the generic Android string dumps already in this repo under
android-strings/<version>/ (produced by extract_android_strings.py
from the signer-gated APK archive) and writes the Reuters-relevant
subsets under android-strings/reuters-claims/<version>/:

  notifications.txt          the notification-listener machinery:
                             service, repo, filters, get/action
  notifications-prompts.txt  the shipped prompt/spec entries that
                             describe notifications to the agent
  invocation.txt             the node invocation surface: service,
                             dispatcher, client, expiry, fallback
  consent-gates.txt          the on-device consent machinery: HITL
                             gate, compiled defaults, permission
                             resolver, agentpermission approval flow
  data-sources.txt           the proactive data-source classes and
                             publish path (state pushed to the agent
                             session without an invocation)
  data-source-prompts.txt    the shipped data-source descriptions
  manifest-relevant.txt      the manifest lines that matter here:
                             listener service, notification/screen
                             permissions, voice interaction
  absence-checks.txt         computed searches for the article's
                             other claims (accessibility service,
                             booking, cross-account data) in the
                             aura-scoped strings and the manifest,
                             with counts and the actual hit lines

Each file carries a header naming its source files, the exact
patterns that selected its lines, and its line count, so a reader
can re-derive it from the generic dumps. Idempotent: outputs are
rewritten from the dumps on every run. No dumps -> exit 0 with a
note; this script must never fail the snapshot on its own.
"""
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DUMPS = REPO / "android-strings"
OUT_ROOT = DUMPS / "reuters-claims"
MAP_PATH = REPO / "android-map.json"

# kind -> (source dump file, [regex patterns]); a line is kept if it
# matches any pattern. Patterns are deliberately aura/Hatch-scoped:
# the generic dumps carry every AndroidX string in the APK, and an
# unscoped "notification" match is thousands of library lines that
# say nothing about this app.
LINE_KINDS = {
    "notifications.txt": ("dex-strings.txt", [
        r"aura\.commands\.notifications",
        r"aura\.notifications\.",
        r"NodeNotificationListener",
        r"NotificationsDataSource",
        r"NotificationPermissionHelper",
        r"HatchNotificationFilter",
        r"notifications\.get",
        r"notifications\.action",
        r"Notification listener",
        r"Notification access is not enabled",
        r"notification listener access",
    ]),
    "invocation.txt": ("dex-strings.txt", [
        r"NodeCommandService",
        r"NodeCommandDispatcher",
        r"NodeCommandFallbackWorker",
        r"HatchNodeClient",
        r"NodeCommandSpec",
        r"extra_command|extra_params_json|extra_request_id|extra_timeout_ms",
        r"invoke_expired",
        r"dispatched by another session",
        r"api/nodes/",
        r"device\.invoke",
        r"Enqueued via WorkManager",
        r"FGS not started",
    ]),
    "consent-gates.txt": ("dex-strings.txt", [
        r"NodeHitl|HatchNodeHitlGate|HitlMode",
        r"ALWAYS_ASK|AUTO_ALLOW",
        r"ALLOW_ONCE_PER_REQUEST|NO_ALLOW_ALWAYS",
        r"PermissionDefaultMode|connector baseline|Connector baseline",
        r"HatchPermissionResolver|NodePermissionActivity",
        r"aura\.agentpermission\..*(Hitl|HITL|Approval|Permission)",
        r"The device permission was not granted",
        r"permission denied: command=",
        r"CARRY_OVER_WINDOW|LOCAL_APPROVAL_PREFIX",
    ]),
    "data-sources.txt": ("dex-strings.txt", [
        r"aura\..*DataSource",
        r"NotificationsDataSource",
        r"proactiveTrigger",
        r"maybePublish",
    ]),
    "manifest-relevant.txt": ("manifest-summary.txt", [
        r"notification|Notification",
        r"BIND_NOTIFICATION_LISTENER_SERVICE",
        r"POST_PROMOTED_NOTIFICATIONS|DETECT_SCREEN_CAPTURE",
        r"BIND_VOICE_INTERACTION|VoiceInteraction",
        r"PushLite|push\.",
    ]),
}

# Prompt-entry kinds: the prompt/spec dumps join entries with a
# blank line; keep whole entries matching any pattern.
ENTRY_KINDS = {
    "notifications-prompts.txt": ("prompt-strings.txt", [
        r"notification",
    ]),
    "data-source-prompts.txt": ("prompt-strings.txt", [
        r"data source",
        r"surfaced by the system notification listener",
    ]),
}

# Absence checks for the article's other claims: (label, dump file,
# pattern, exclude pattern or None, note). Counts and hit lines are
# computed at run time; nothing here is a pre-written verdict.
ABSENCE_CHECKS = [
    ("accessibility service declared in the manifest",
     "manifest-summary.txt", r"AccessibilityService", None,
     "A declared Android accessibility service would appear here as "
     "a service component. The macOS route in the article has no "
     "manifest counterpart if this is 0."),
    ("BIND_ACCESSIBILITY_SERVICE permission in the manifest",
     "manifest-summary.txt", r"BIND_ACCESSIBILITY_SERVICE", None,
     "The permission that protects an accessibility service."),
    ("aura accessibility service class in the dex strings",
     "dex-strings.txt", r"com\.facebook\.aura\..*AccessibilityService", None,
     "Aura-scoped: AndroidX/UI accessibility vocabulary elsewhere in "
     "the dump is library code, not a declared service of this app."),
    ("Airbnb (the company) in the dex strings, Lottie library excluded",
     "dex-strings.txt", r"(?i)airbnb", r"lottie",
     "The article's booking claim is about agent behaviour on the "
     "web/other surfaces; com.airbnb.lottie is an animation library "
     "and is excluded by name."),
    ("booking/purchase command in the aura command families",
     "dex-strings.txt", r"aura\.commands\..*(booking|purchase|checkout)", None,
     "The compiled-in device command set is the whole on-device "
     "surface; a booking command would appear here."),
    ("bank-balance / cross-account terms in the shipped prompts",
     "prompt-strings.txt", r"(?i)capital one|schwab|bank balance|another (user|person)", None,
     "The out-of-context-data claim concerns server/model behaviour; "
     "this checks only whether the shipped prompt text names it."),
]


def entries(text):
    return [e for e in text.split("\n\n") if e.strip()]


def build_version(version, dumps_dir, meta):
    out = OUT_ROOT / version
    out.mkdir(parents=True, exist_ok=True)
    made = {}

    def header(kind, source, patterns, count):
        lines = [
            f"# reuters-claims/{version}/{kind}",
            f"# Source: android-strings/{version}/{source} (generic dump, "
            f"extract_android_strings.py)",
        ]
        if meta:
            lines.append(f"# APK sha256: {meta.get('apk_sha256')}")
            lines.append(
                f"# Signer cert sha256: "
                f"{', '.join(meta.get('signer_cert_sha256', []))}")
        lines.append("# Selected lines: any line matching one of")
        for p in patterns:
            lines.append(f"#   {p}")
        lines.append(f"# Lines: {count}")
        lines.append("")
        return "\n".join(lines)

    for kind, (source, patterns) in LINE_KINDS.items():
        src = dumps_dir / source
        if not src.exists():
            continue
        rx = [re.compile(p) for p in patterns]
        kept = [ln for ln in src.read_text(errors="replace").splitlines()
                if any(r.search(ln) for r in rx)]
        kept = list(dict.fromkeys(kept))
        (out / kind).write_text(
            header(kind, source, patterns, len(kept)) + "\n".join(kept) + "\n")
        made[kind] = len(kept)

    for kind, (source, patterns) in ENTRY_KINDS.items():
        src = dumps_dir / source
        if not src.exists():
            continue
        rx = [re.compile(p, re.IGNORECASE) for p in patterns]
        kept = [e for e in entries(src.read_text(errors="replace"))
                if any(r.search(e) for r in rx)]
        kept = list(dict.fromkeys(kept))
        (out / kind).write_text(
            header(kind, source, patterns, len(kept)) + "\n\n".join(kept) + "\n")
        made[kind] = len(kept)

    # absence-checks.txt is computed, not filtered: one section per
    # check with its count and the hit lines themselves.
    sections = []
    total_hits = 0
    for label, source, pattern, exclude, note in ABSENCE_CHECKS:
        src = dumps_dir / source
        hits = []
        if src.exists():
            rx = re.compile(pattern)
            ex = re.compile(exclude) if exclude else None
            hits = [ln for ln in src.read_text(errors="replace").splitlines()
                    if rx.search(ln) and not (ex and ex.search(ln))]
        total_hits += len(hits)
        sec = [f"## {label}", f"Source: {source}", f"Pattern: {pattern}"]
        if exclude:
            sec.append(f"Excluding lines matching: {exclude}")
        sec.append(f"Hits: {len(hits)}")
        sec.append(f"Note: {note}")
        sec.extend(hits)
        sections.append("\n".join(sec))
    (out / "absence-checks.txt").write_text(
        f"# reuters-claims/{version}/absence-checks.txt\n"
        f"# Computed searches over the generic dumps in "
        f"android-strings/{version}/.\n"
        f"# Each section states its pattern and count and prints the "
        f"hit lines;\n# read the count against its note, not as a "
        f"verdict on the article.\n\n"
        + "\n\n".join(sections) + "\n")
    made["absence-checks.txt"] = total_hits
    return made


def main():
    if not DUMPS.is_dir():
        print("reuters-claims: no android-strings dumps, skipping")
        return 0
    meta_by_version = {}
    if MAP_PATH.exists():
        try:
            meta_by_version = json.loads(MAP_PATH.read_text())
        except Exception:
            meta_by_version = {}
    versions = sorted(
        p.name for p in DUMPS.iterdir()
        if p.is_dir() and p.name != "reuters-claims"
        and (p / "dex-strings.txt").exists())
    if not versions:
        print("reuters-claims: no banked versions dumped, skipping")
        return 0
    for version in versions:
        made = build_version(version, DUMPS / version,
                             meta_by_version.get(version, {}))
        total = sum(made.values())
        print(f"reuters-claims {version}: {len(made)} files, "
              f"{total} selected lines/entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
