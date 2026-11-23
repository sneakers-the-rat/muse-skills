# mac-app/ — string extraction of the Muse macOS app (Endo)

Static string/prompt extraction of the banked Muse macOS desktop
app, mirroring this repo's `binary-strings/` + `system_prompts/` (VM
hatch binary) extractions. Produced by
`scripts/extract_mac_strings.py`, wired into `scripts/sync-skills.sh`
alongside the Android/binary steps. Provenance manifest:
`../mac-app-map.json` — the analogue of `../binary-map.json`.

**Flat layout, version as metadata.** This tree has no version
directory: the repo is a continuous, versioned backup, so git history
is the versioning. `../mac-app-map.json` records which app version
the strings currently in this tree correspond to (version, build,
bundle id, DMG sha256, per-binary hashes and counts, per-output-file
sha256), so any given commit answers "what version are these
strings?" from the manifest alone — and a diff between commits shows
exactly what changed between app versions. When a new version is
banked, the extractor replaces this tree in place and the map's
version fields move with it. (This layout was restructured from an
initial `mac-app/<version>/` tree on 2026-11-23 at the user's
direction; the flattened files are byte-identical to the versioned
ones — see the addendum in
`~/workspace/your_files/mac-app-extraction/REPORT.md`.)

Nothing here was executed: bytes were read from the banked DMG's
extracted app copy, never launched.

## Source artifact

| | |
|---|---|
| App | Muse (Endo), bundle id `com.meta.endo` |
| Version banked | 13.1, build 1119850179 |
| DMG | `~/workspace/your_files/mac-app-archive/versions/13.1/app.dmg` |
| DMG sha256 | `00cfff39d21c5b5fb694487c8395dbb74b387e1448c0b07208879a8286529e80` |
| DMG size | 94,482,346 bytes |
| Analysis source | `~/workspace/mac-inspect/analysis/13.1/` (mac-inspect toolkit; full write-up in its `REPORT.md`) |

## Layout — `mac-app/` (flat; version recorded in `../mac-app-map.json`)

| Path | What it is | Analogue |
|---|---|---|
| `strings/<Binary>.strings.txt` | Every unique printable string (ASCII + UTF-16LE, min 5) of each of the bundle's 5 Mach-O binaries, sorted | `android-strings/<v>/native-strings/`, `binary-strings/` |
| `strings/census.json` | Per-binary size, sha256, total/unique string counts, prompt-like counts | Android `so_strings` census |
| `strings/prompt-like.txt` | Prompt-like filter over all 5 binaries: long, instruction-like strings, grouped by binary | mac-inspect `prompt-like.txt` |
| `prompt-strings.txt` | The main binary's prompt-like subset — the instruction-bearing / system-prompt-flavoured strings | `android-strings/<v>/prompt-strings.txt`, `system_prompts/` |
| `tool-prompts/spec-descriptions.txt` | All shipped NodeCommandSpec description fragments verbatim, in both recovered sets (short one-line specs; long guidance fragments) | `android-strings/<v>/spec-descriptions.txt` |
| `tool-prompts/long-fragments.txt` / `short-fragments.txt` | The two fragment sets separately. The short/fragmentary set is kept and labelled, never dropped — Mac specs are stored as fragments split at format placeholders | VM extraction's bare-prompt / skipped class |
| `tool-prompts/<command>.txt` | One file per device command, with every fragment that names that command | `binary-strings/tools/<tool>.json` (per-tool prompts) |
| `tool-prompts/tools-manifest.json` | Per-command status: `described_long` / `fragmentary_only` / `name_only` (attested in the catalog, named by no fragment — the skipped class, surfaced rather than hidden), plus fragment attribution counts and the gateway/plumbing name list | `binary-strings/tools-manifest.json` |
| `command-catalog.txt` | Recovered node/gateway command-name strings | Android command catalog in `spec-descriptions.txt` / dex strings |
| `urls.txt` | URL strings from the main binary, with plist/feed notes | `urls.txt` in the mac-inspect analysis |
| `entitlements.txt` | Signed entitlements of all 5 binaries (main app's full set; the other four have no entitlements blob) | Android `manifest-summary.txt` permissions half |
| `manifest-summary.txt` | The bundle's Info.plists: bundle id, versions, minimum macOS, URL schemes, every TCC `NS*UsageDescription`, Sparkle keys | `android-strings/<v>/manifest-summary.txt` |
| `objc-census/` | ObjC/Swift census of the main binary (arm64 slice): `classes.txt`, `protocols.txt`, `selectors.txt`, `swift-names.txt`, `summary.json` | Android dex class census |
| `keyword-hits.txt` | Topical greps (14 topics) over the string + ObjC layers from the analysis | `binary-strings/` topical curations |

## Scope decision — embedded web client

`Contents/Resources/hatch/index.html` (~41 MB, the embedded web chat
UI) is **excluded** from this native extraction: the node
implementation is native, not web, and the web client's strings
belong to the frontend source. Its size and sha256 are recorded in
`mac-app-map.json` under `web_client_excluded`, so the exclusion is
auditable.

## Regeneration

```
python3 scripts/extract_mac_strings.py           # hash-gated, idempotent
python3 scripts/extract_mac_strings.py --force   # regenerate anyway
```

Deterministic: no timestamps in any generated file; a rerun over
unchanged inputs produces byte-identical output (and is skipped
entirely when `mac-app-map.json` already records this version with a
matching DMG sha256 and analysis-input fingerprint).
