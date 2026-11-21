#!/usr/bin/env python3
"""Dump the important strings of every banked Muse Android APK into
this repo under android-strings/<version>/:

  dex-strings.txt        every string from every dex (sorted, unique)
  prompt-strings.txt     the instruction-bearing subset: strings of
                         >=240 chars that read as agent instructions
                         (the tool/data-source descriptions and rules
                         the client ships for the model)
  spec-descriptions.txt  the NodeCommandSpec tool descriptions
                         (recovered from the dex strings: the
                         'Reports the device…' / imperative forms are
                         re-derived by the android-inspect analysis;
                         here we keep the raw long-string superset in
                         prompt-strings.txt and the spec openers below)
  resources-strings.txt  every string pool in resources.arsc
  manifest-summary.txt   decoded manifest: package, permissions,
                         components
  native-strings/        printable strings of each native .so
  ../android-map.json    provenance: apk sha256, signer cert sha256,
                         size, per-file sha256, dump time

Source of truth for APKs: ~/workspace/your_files/android-app-archive
(per-version, signer-gated). The dump is idempotent: a version whose
apk sha256 already matches android-map.json is skipped, so hourly
runs only write when a new version is banked. No banked APK -> exit 0
with a note; this script must never fail the snapshot on its own.

Implementation lives in the android-inspect toolkit
(~/workspace/android-inspect); this script is the hook entry point,
in the same shim style as extract_binary_files.py.
"""
import hashlib
import json
import pathlib
import re
import sys
import zipfile

HOME = pathlib.Path.home()
sys.path.insert(0, str(HOME / "workspace" / "android-inspect"))
sys.path.insert(0, str(HOME / "workspace" / "your_files" /
                       "android-app-archive" / "tools"))

REPO = pathlib.Path(__file__).resolve().parent.parent
ARCHIVE = HOME / "workspace" / "your_files" / "android-app-archive"
OUT_ROOT = REPO / "android-strings"
MAP_PATH = REPO / "android-map.json"

INST = re.compile(r"\b(NEVER|never|always|Always|must|Do not|Use this|use this)\b")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def dump_version(apk_path, version):
    import axml_dump
    import dex_census
    import arsc_strings

    out = OUT_ROOT / version
    out.mkdir(parents=True, exist_ok=True)
    z = zipfile.ZipFile(apk_path)

    # dex strings
    all_strings = set()
    tmp = pathlib.Path("/tmp/_android_dump_dex")
    tmp.mkdir(exist_ok=True)
    for n in sorted(z.namelist()):
        if n.startswith("classes") and n.endswith(".dex"):
            p = tmp / n
            p.write_bytes(z.read(n))
            all_strings.update(dex_census.parse(str(p))["strings"])
    dex_sorted = sorted(all_strings)
    (out / "dex-strings.txt").write_text("\n".join(dex_sorted))

    long_strings = [s for s in dex_sorted if len(s) >= 240]
    prompt = [s for s in long_strings if INST.search(s)]
    (out / "prompt-strings.txt").write_text("\n\n".join(prompt))
    specs = [s for s in long_strings
             if s.startswith(("Reports the device", "Report the device"))]
    (out / "spec-descriptions.txt").write_text("\n\n".join(specs))

    # resources
    res = sorted(set(arsc_strings.pools(z.read("resources.arsc"))))
    (out / "resources-strings.txt").write_text("\n".join(res))

    # manifest summary (reuse apk_extract's walker logic inline)
    manifest = axml_dump.decode(z.read("AndroidManifest.xml"))

    def walk(el, kind, acc):
        if el["name"] == kind:
            acc.append(el)
        for c in el.get("children", []):
            walk(c, kind, acc)

    lines = [f"package: {manifest['attrs'].get('package')}",
             f"version: {version}", ""]
    perms = []
    walk(manifest, "uses-permission", perms)
    walk(manifest, "uses-permission-sdk-23", perms)
    lines.append(f"== permissions ({len(perms)}) ==")
    for p in perms:
        lines.append("  " + str(p["attrs"].get("android:name")))
    for kind in ("activity", "activity-alias", "service", "receiver",
                 "provider"):
        comps = []
        walk(manifest, kind, comps)
        lines.append(f"\n== {kind} ({len(comps)}) ==")
        for c in comps:
            a = c["attrs"]
            lines.append(
                f"  {a.get('android:name')} exported={a.get('android:exported')}"
                f" permission={a.get('android:permission')}")
    (out / "manifest-summary.txt").write_text("\n".join(lines))

    # native library strings (the toolkit's standalone tool)
    import subprocess
    subprocess.run(
        [sys.executable,
         str(HOME / "workspace" / "android-inspect" / "so_strings.py"),
         str(apk_path), str(out / "native-strings")],
        check=True, capture_output=True, text=True)

    files = {}
    for f in sorted(out.rglob("*")):
        if f.is_file():
            files[str(f.relative_to(OUT_ROOT))] = sha256(f.read_bytes())
    return files


def main():
    import bank_apk
    from apk_signer import signer_fingerprints

    versions_dir = ARCHIVE / "versions"
    if not versions_dir.is_dir():
        print("android strings: no APK archive; skipping")
        return 0
    amap = {}
    if MAP_PATH.exists():
        amap = json.loads(MAP_PATH.read_text())
    changed = False
    for vdir in sorted(versions_dir.iterdir()):
        apk = vdir / "app.apk"
        if not apk.exists():
            continue
        data = apk.read_bytes()
        digest = sha256(data)
        entry = amap.get(vdir.name)
        if entry and entry.get("apk_sha256") == digest:
            continue
        print(f"android strings: dumping {vdir.name} "
              f"({len(data)} bytes, sha256 {digest[:12]}…)")
        files = dump_version(apk, vdir.name)
        amap[vdir.name] = {
            "apk_sha256": digest,
            "apk_size": len(data),
            "signer_cert_sha256": sorted(signer_fingerprints(apk)),
            "files": files,
        }
        changed = True
    if changed:
        MAP_PATH.write_text(json.dumps(amap, indent=1, sort_keys=True))
        print(f"android strings: android-map.json updated "
              f"({len(amap)} versions)")
    else:
        print("android strings: all banked versions already dumped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
