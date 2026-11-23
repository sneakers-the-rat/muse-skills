#!/usr/bin/env python3
"""Dump the important strings of the banked Muse macOS app (Endo)
into this repo under mac-app/ — a FLAT tree, no version directory:

  strings/<Binary>.strings.txt  every unique printable string of each
                                of the 5 Mach-O binaries in the bundle
                                (ASCII + UTF-16LE, min length 5, sorted)
  strings/census.json           per-binary size / sha256 / counts
  strings/prompt-like.txt       the prompt-like filter over all five
                                binaries (long, instruction-like strings)
  prompt-strings.txt            the main binary's prompt-like subset —
                                the analogue of android-strings'
                                prompt-strings.txt (system-prompt /
                                instruction-bearing strings)
  tool-prompts/                 the shipped NodeCommandSpec descriptions
    spec-descriptions.txt       all spec fragments verbatim, in the two
                                sets the analysis recovered: one-line
                                complete specs (short) and long spec /
                                guidance fragments (>=200 chars)
    long-fragments.txt          the long set alone
    short-fragments.txt         the short / fragmentary set alone —
                                kept and labelled, never dropped: the
                                Mac specs are stored as fragments split
                                at format placeholders, so this is the
                                analogue of the VM extraction's
                                bare-prompt / skipped class
    <command>.txt               one file per device command, holding
                                every fragment that names that command
    tools-manifest.json         per-command status: described_long /
                                fragmentary_only / name_only (a command
                                attested in the catalog but named by no
                                recovered fragment — the analogue of
                                the VM tools-manifest's name_only)
  command-catalog.txt           the recovered node/gateway command names
  urls.txt                      URL strings from the main binary
  entitlements.txt              signed entitlements of all 5 binaries
  manifest-summary.txt          the bundle's Info.plists (bundle id,
                                versions, TCC usage descriptions,
                                Sparkle keys) — the analogue of
                                android-strings' manifest-summary.txt
  objc-census/                  ObjC/Swift census of the main binary:
                                classes.txt, protocols.txt,
                                selectors.txt, swift-names.txt,
                                summary.json (arm64 slice, canonical)
  keyword-hits.txt              the analysis' topical string greps
                                (14 topics over strings + ObjC layers)
  ../mac-app-map.json           provenance: the app version, build and
                                bundle id these files correspond to,
                                DMG sha256/size, per-file sha256 of
                                every output

The tree is deliberately flat: this repo is a continuous, versioned
backup, so git history is the versioning. The version is metadata —
mac-app-map.json records which app version / build / DMG the strings
currently in the tree were extracted from — so a diff between two
commits shows exactly what changed between app versions, instead of
two near-identical version directories that cannot be compared.
When a new version is banked, its dump replaces the tree in place and
the map's version fields move with it.

Sources of truth (all read-only, nothing executed):
  * banked DMG + manifest: ~/workspace/your_files/mac-app-archive/
    versions/<version>/ (app.dmg, manifest.json) — the DMG sha256 is
    the hash gate, exactly as the APK sha256 gates the Android dump.
  * extracted app copy + curated analysis artifacts:
    ~/workspace/mac-inspect/analysis/<version>/ (the mac-inspect
    toolkit's output: strings are re-derived here from the app copy's
    binaries with the same regexes as mac-inspect's macho_strings.py;
    spec fragments, catalog, urls, entitlements, plist summary, ObjC
    census and keyword hits are taken from the toolkit's curated
    files, which are the recovered form of that material).

Scope decision — embedded web client: Contents/Resources/hatch/
index.html (the embedded web chat UI, ~41 MB) is OUT of scope for
this native extraction. The node implementation is native, not web
(REPORT.md §1/§5), and the web client's strings belong to the
frontend source, not to Endo. Its size and sha256 are recorded in
mac-app-map.json so the exclusion is auditable, not silent.

The dump is deterministic (no timestamps anywhere) and idempotent:
when mac-app-map.json already records this version with a matching
DMG sha256 and analysis-input fingerprint, the dump is skipped, so
hourly runs only write when a new version is banked or the analysis
changes. --force regenerates. Only the newest banked version is
dumped — the flat tree always corresponds to the map's one recorded
version. No banked version -> exit 0 with a note; this script must
never fail the snapshot on its own (it still returns non-zero on a
genuine extraction error once a banked version is present and gated
in).
"""
import hashlib
import json
import pathlib
import re
import sys

HOME = pathlib.Path.home()
REPO = pathlib.Path(__file__).resolve().parent.parent
ARCHIVE = HOME / "workspace" / "your_files" / "mac-app-archive"
ANALYSIS_ROOT = HOME / "workspace" / "mac-inspect" / "analysis"
OUT_ROOT = REPO / "mac-app"
MAP_PATH = REPO / "mac-app-map.json"

# The 5 Mach-O binaries of the bundle, label -> path inside Muse.app.
BINARIES = {
    "Muse": "Contents/MacOS/Muse",
    "EndoCrashpadHandler": "Contents/MacOS/EndoCrashpadHandler",
    "Sparkle": "Contents/Frameworks/Sparkle.framework/Versions/B/Sparkle",
    "Autoupdate": "Contents/Frameworks/Sparkle.framework/Versions/B/Autoupdate",
    "Updater": "Contents/Frameworks/Sparkle.framework/Versions/B/Updater.app/Contents/MacOS/Updater",
}
MAIN_BINARY = "Muse"
WEB_CLIENT = "Contents/Resources/hatch/index.html"

# String extraction: the same patterns as mac-inspect/macho_strings.py.
ASCII_PAT = re.compile(rb"[\x20-\x7e]{5,}")
UTF16_PAT = re.compile(rb"(?:[\x20-\x7e]\x00){5,}")
INSTR = re.compile(r"\b(you are|you must|you should|do not|always|never|"
                   r"assistant|user|instruction|respond|answer|when the|"
                   r"if the|make sure|please|tool|prompt)\b", re.I)

# Catalog names that are gateway protocol / plumbing, not device
# commands (REPORT.md §5: "beside gateway plumbing").
GATEWAY_NAMES = {"agent.status", "bug_report.create",
                 "client.invoke", "client.register_capabilities"}
# Standalone catalog entries that are truncations of files.* names in
# an embedded 8-char field (command-catalog.txt's own note), not real
# commands.
TRUNCATED_ARTIFACTS = {"files.de", "files.re", "files.up", "files.wr"}
# Device commands attested in spec prose but not as standalone
# catalog strings (command-catalog.txt's header note).
PROSE_ONLY_COMMANDS = {"screen.snap", "files.delete"}

COMMAND_RE = re.compile(r"[a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+$")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def strings_of(data):
    out = [m.group().decode("ascii") for m in ASCII_PAT.finditer(data)]
    out += [m.group().decode("utf-16-le")
            for m in UTF16_PAT.finditer(data)]
    return out


def prompt_like(strs):
    hits = []
    for s in strs:
        if len(s) < 80 or s.count(" ") < 7:
            continue
        if INSTR.search(s):
            hits.append(s)
    # Deterministic: length descending, then the string itself —
    # a bare length key would leave ties in set-iteration order,
    # which is hash-randomized per process and breaks idempotence.
    return sorted(set(hits), key=lambda s: (-len(s), s))


def parse_spec_descriptions(text):
    """Split the curated spec file into (short, long) fragment lists.

    The file's own header states the sets: one-line complete specs,
    then long spec / guidance fragments (>=200 chars). Both sets are
    sorted in the source; the split is verified against the counts
    in the header by the caller, not assumed.
    """
    rest = text.split("## One-line complete specs", 1)[1]
    short_part, long_part = rest.split(
        "## Long spec / guidance fragments (>=200 chars)", 1)

    def entries(part):
        return [e.strip() for e in part.strip().split("\n\n") if e.strip()]

    return entries(short_part), entries(long_part)


def parse_command_catalog(text):
    """Return (device_commands, gateway_names) from the catalog file.

    Standalone names are attested verbatim; the files.* family is
    attested by substring census (its section lists full names).
    Truncated 8-char artifacts and gateway/plumbing names are not
    device commands.
    """
    names = set()
    for line in text.splitlines():
        line = line.strip()
        if COMMAND_RE.fullmatch(line):
            names.add(line)
    if "## files.* family" in text:
        fam = text.split("## files.* family", 1)[1]
        for line in fam.splitlines():
            m = re.match(r"(files\.[a-z0-9_.]+)", line.strip())
            if m:
                names.add(m.group(1))
    names -= TRUNCATED_ARTIFACTS
    names |= PROSE_ONLY_COMMANDS
    gateway = sorted(n for n in names
                     if n.startswith(("chat.", "node.", "client."))
                     or n in GATEWAY_NAMES)
    device = sorted(n for n in names if n not in gateway)
    return device, gateway


def assign_fragments(commands, short, long):
    """Map each command to the fragments that name it.

    A fragment may name several commands (it is filed under each);
    a fragment naming none stays unattributed — it is guidance prose,
    counted in the manifest, and kept in spec-descriptions.txt.
    """
    per_command = {}
    for cmd in commands:
        per_command[cmd] = {
            "long": [f for f in long if cmd in f],
            "short": [f for f in short if cmd in f],
        }
    return per_command


def command_status(entry):
    if entry["long"]:
        return "described_long"
    if entry["short"]:
        return "fragmentary_only"
    return "name_only"


def strip_hash_header(text):
    """Drop a curated file's leading #-comment header (and the blank
    line after it); the repo file gets a fresh provenance header."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and lines[i].startswith("#"):
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    return "\n".join(lines[i:]).strip()


def header(title, version, dmg_sha, extra=()):
    lines = [f"# {title}",
             f"# Source artifact: Muse macOS app (Endo) {version}, "
             f"banked DMG app.dmg",
             f"# DMG sha256: {dmg_sha}",
             "# Produced by scripts/extract_mac_strings.py from the "
             "mac-inspect analysis artifacts (see mac-app/README.md).",
             "# Static extraction only: bytes read, nothing executed."]
    lines += [f"# {e}" for e in extra]
    return "\n".join(lines) + "\n\n"


def dump_app(version, app_dir, analysis_dir, dmg_sha, manifest):
    out = OUT_ROOT
    out.mkdir(parents=True, exist_ok=True)
    bundle_id = manifest.get("bundle_id")
    build = manifest.get("build")

    # ---- strings/ (re-derived from the app copy's binaries) ----
    sdir = out / "strings"
    sdir.mkdir(exist_ok=True)
    census = {}
    per_binary_prompt = {}
    main_prompt = []
    for label in sorted(BINARIES):
        data = (app_dir / BINARIES[label]).read_bytes()
        strs = strings_of(data)
        uniq = sorted(set(strs))
        (sdir / f"{label}.strings.txt").write_text("\n".join(uniq))
        pl = prompt_like(uniq)
        if pl:
            per_binary_prompt[label] = pl
        if label == MAIN_BINARY:
            main_prompt = pl
        census[label] = {
            "path_in_bundle": BINARIES[label],
            "size": len(data),
            "sha256": sha256(data),
            "string_count_total": len(strs),
            "string_count_unique": len(uniq),
            "prompt_like_count": len(pl),
        }
    (sdir / "census.json").write_text(
        json.dumps(census, indent=1, sort_keys=True) + "\n")
    with open(sdir / "prompt-like.txt", "w") as fh:
        for label in sorted(per_binary_prompt):
            hits = per_binary_prompt[label]
            fh.write(f"===== {label} ({len(hits)}) =====\n")
            fh.write("\n---\n".join(hits))
            fh.write("\n")

    # ---- prompt-strings.txt (main binary's prompt-like subset) ----
    (out / "prompt-strings.txt").write_text("\n\n".join(main_prompt))

    # ---- tool-prompts/ ----
    spec_text = (analysis_dir / "spec-descriptions.txt").read_text()
    short, long = parse_spec_descriptions(spec_text)
    catalog_text = (analysis_dir / "command-catalog.txt").read_text()
    device, gateway = parse_command_catalog(catalog_text)
    per_command = assign_fragments(device, short, long)
    attributed = set()
    for frags in per_command.values():
        attributed.update(frags["long"])
        attributed.update(frags["short"])

    tdir = out / "tool-prompts"
    tdir.mkdir(exist_ok=True)
    spec_head = header(
        f"mac-app {version} — shipped node-command spec descriptions",
        version, dmg_sha,
        extra=("The Mac specs are stored as fragment strings split at "
               "format placeholders; both recovered sets are kept "
               "verbatim: one-line complete specs (short) and long "
               "spec / guidance fragments (>=200 chars).",
               f"Long fragments: {len(long)}; short fragments: "
               f"{len(short)}."))
    body = ("## One-line complete specs\n\n" + "\n\n".join(short) +
            "\n\n## Long spec / guidance fragments (>=200 chars)\n\n" +
            "\n\n".join(long) + "\n")
    (tdir / "spec-descriptions.txt").write_text(spec_head + body)
    (tdir / "long-fragments.txt").write_text(
        header(f"mac-app {version} — long spec / guidance fragments",
               version, dmg_sha,
               extra=(f"Fragments: {len(long)}.",)) +
        "\n\n".join(long) + "\n")
    (tdir / "short-fragments.txt").write_text(
        header(f"mac-app {version} — short / fragmentary specs",
               version, dmg_sha,
               extra=("The fragmentary class: one-line complete specs "
                      "and short fragments, kept and labelled rather "
                      "than dropped — the analogue of the VM "
                      "extraction's bare-prompt / skipped class.",
                      f"Fragments: {len(short)}.",)) +
        "\n\n".join(short) + "\n")

    tools_manifest = {
        "app": bundle_id,
        "version": version,
        "build": build,
        "dmg_sha256": dmg_sha,
        "source": "command-catalog.txt + spec-descriptions.txt "
                  "(mac-inspect analysis of Contents/MacOS/Muse)",
        "fragment_counts": {
            "long": len(long),
            "short": len(short),
            "attributed_long": len([f for f in long if f in attributed]),
            "attributed_short": len([f for f in short if f in attributed]),
            "unattributed": len(short) + len(long) - len(attributed),
        },
        "gateway_or_plumbing_names": gateway,
        "truncated_catalog_artifacts": sorted(TRUNCATED_ARTIFACTS),
        "commands": {},
    }
    for cmd in device:
        entry = per_command[cmd]
        status = command_status(entry)
        tools_manifest["commands"][cmd] = {
            "file": f"{cmd}.txt",
            "status": status,
            "long_fragments": len(entry["long"]),
            "short_fragments": len(entry["short"]),
        }
        note = ""
        if status == "name_only":
            note = ("# status: name_only — attested in the command "
                    "catalog but named by no recovered spec fragment; "
                    "kept as its own file so the skipped class is "
                    "visible, mirroring the VM tools-manifest.\n")
        (tdir / f"{cmd}.txt").write_text(
            header(f"mac-app {version} — tool prompt fragments: {cmd}",
                   version, dmg_sha,
                   extra=(f"status: {status}; long fragments: "
                          f"{len(entry['long'])}; short fragments: "
                          f"{len(entry['short'])}.",)) +
            note +
            "\n\n".join(entry["long"] + entry["short"]) +
            ("\n" if entry["long"] or entry["short"] else ""))
    (tdir / "tools-manifest.json").write_text(
        json.dumps(tools_manifest, indent=1, sort_keys=True) + "\n")

    # ---- curated verbatim categories ----
    (out / "command-catalog.txt").write_text(
        header(f"mac-app {version} — command catalog", version, dmg_sha) +
        strip_hash_header(catalog_text) + "\n")
    urls_text = (analysis_dir / "urls.txt").read_text()
    (out / "urls.txt").write_text(
        header(f"mac-app {version} — URLs", version, dmg_sha) +
        strip_hash_header(urls_text) + "\n")
    ent_text = (analysis_dir / "entitlements.txt").read_text()
    (out / "entitlements.txt").write_text(
        header(f"mac-app {version} — entitlements", version, dmg_sha) +
        ent_text.strip() + "\n")
    plist_text = (analysis_dir / "info-plist-summary.txt").read_text()
    (out / "manifest-summary.txt").write_text(
        header(f"mac-app {version} — bundle / Info.plist summary",
               version, dmg_sha,
               extra=(f"bundle_id: {bundle_id}; build: {build}; "
                      f"team_id: {manifest.get('team_id')}; "
                      f"minimum_macos: {manifest.get('minimum_macos')}.",)) +
        plist_text.strip() + "\n")
    kw_text = (analysis_dir / "keyword-hits.txt").read_text()
    (out / "keyword-hits.txt").write_text(
        header(f"mac-app {version} — keyword hits (topical greps)",
               version, dmg_sha) + kw_text.strip() + "\n")

    # ---- objc-census/ ----
    odir = out / "objc-census"
    odir.mkdir(exist_ok=True)
    name_files = {"classes.txt": "classes.arm64.txt",
                  "protocols.txt": "protocols.arm64.txt",
                  "selectors.txt": "selectors.arm64.txt",
                  "swift-names.txt": "swift-reflstr.arm64.txt"}
    for dest_name, src_name in name_files.items():
        names = sorted(set(
            (analysis_dir / "objc-names" / src_name)
            .read_text().splitlines()))
        (odir / dest_name).write_text("\n".join(names))
    objc_main = json.loads((analysis_dir / "objc-main.json").read_text())
    summary = {"file": "Contents/MacOS/Muse",
               "evidence": objc_main.get("evidence"),
               "slices": [{k: v for k, v in s.items()
                           if k in ("arch", "method", "cryptid",
                                    "counts")}
                          for s in objc_main.get("slices", [])]}
    (odir / "summary.json").write_text(
        json.dumps(summary, indent=1, sort_keys=True) + "\n")

    files = {}
    for f in sorted(out.rglob("*")):
        # README.md is hand-maintained, not generated — not a dump file.
        if f.is_file() and f.name != "README.md":
            files[str(f.relative_to(OUT_ROOT))] = sha256(f.read_bytes())
    return files, census, tools_manifest


def input_fingerprint(version, app_dir, analysis_dir):
    """Hash the curated analysis inputs, so a re-analysis (not just a
    new DMG) also re-triggers the dump."""
    h = hashlib.sha256()
    for name in ("spec-descriptions.txt", "command-catalog.txt",
                 "urls.txt", "entitlements.txt",
                 "info-plist-summary.txt", "keyword-hits.txt",
                 "objc-main.json"):
        h.update((analysis_dir / name).read_bytes())
    for name in ("classes.arm64.txt", "protocols.arm64.txt",
                 "selectors.arm64.txt", "swift-reflstr.arm64.txt"):
        h.update((analysis_dir / "objc-names" / name).read_bytes())
    for label in sorted(BINARIES):
        h.update((app_dir / BINARIES[label]).read_bytes())
    return h.hexdigest()


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    force = "--force" in argv
    versions_dir = ARCHIVE / "versions"
    if not versions_dir.is_dir():
        print("mac strings: no Mac app archive; skipping")
        return 0
    # Flat tree: only the newest banked version is dumped, and the map
    # records that one version as metadata.
    candidate = None
    for vdir in sorted(versions_dir.iterdir()):
        dmg = vdir / "app.dmg"
        manifest_path = vdir / "manifest.json"
        if dmg.exists() and manifest_path.exists():
            candidate = vdir
    if candidate is None:
        print("mac strings: no banked Mac app version; skipping")
        return 0
    version = candidate.name
    manifest = json.loads((candidate / "manifest.json").read_text())
    dmg = candidate / "app.dmg"
    dmg_data_len = dmg.stat().st_size
    dmg_sha = sha256(dmg.read_bytes())
    if manifest.get("sha256") and manifest["sha256"] != dmg_sha:
        print(f"mac strings: DMG sha256 mismatch for {version} "
              f"(manifest {manifest['sha256'][:12]}… != "
              f"actual {dmg_sha[:12]}…); skipping", file=sys.stderr)
        return 0
    analysis_dir = ANALYSIS_ROOT / version
    app_dir = analysis_dir / "work" / "Muse.app"
    if not app_dir.is_dir():
        print(f"mac strings: no extracted app copy at {app_dir}; "
              f"skipping {version}")
        return 0
    fingerprint = input_fingerprint(version, app_dir, analysis_dir)
    mmap = {}
    if MAP_PATH.exists():
        mmap = json.loads(MAP_PATH.read_text())
    if (not force and mmap.get("version") == version
            and mmap.get("dmg_sha256") == dmg_sha
            and mmap.get("input_fingerprint") == fingerprint):
        print(f"mac strings: {version} already dumped "
              f"(map matches DMG sha256 + input fingerprint)")
        return 0
    print(f"mac strings: dumping {version} "
          f"({dmg_data_len} bytes, sha256 {dmg_sha[:12]}…)")
    files, census, tools_manifest = dump_app(
        version, app_dir, analysis_dir, dmg_sha, manifest)
    web = app_dir / WEB_CLIENT
    mmap = {
        "version": version,
        "build": manifest.get("build"),
        "bundle_id": manifest.get("bundle_id"),
        "team_id": manifest.get("team_id"),
        "dmg_sha256": dmg_sha,
        "dmg_size": dmg_data_len,
        "input_fingerprint": fingerprint,
        "binaries": {k: {"size": v["size"], "sha256": v["sha256"],
                         "string_count_unique":
                             v["string_count_unique"],
                         "prompt_like_count": v["prompt_like_count"]}
                     for k, v in census.items()},
        "device_commands": len(tools_manifest["commands"]),
        "web_client_excluded": {
            "path_in_bundle": WEB_CLIENT,
            "size": web.stat().st_size if web.exists() else None,
            "sha256": sha256(web.read_bytes()) if web.exists() else None,
            "reason": "embedded web chat UI; node implementation "
                      "is native — see mac-app/README.md",
        },
        "files": files,
    }
    MAP_PATH.write_text(json.dumps(mmap, indent=1, sort_keys=True) + "\n")
    print(f"mac strings: mac-app-map.json updated "
          f"(version {version}, {len(files)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
