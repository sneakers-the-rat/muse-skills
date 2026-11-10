#!/usr/bin/env python3
"""Extract the systemd unit texts embedded in the spawnd binary
into binary-strings/spawnd/systemd/.

spawnd is the host provisioner; it embeds the host services'
systemd unit texts as strings and writes them out on the host.
Those texts (ExecStart lines, SocketMode, environment declarations
such as JARVIS_TELEMETRY_PROXY_ALLOWED_USERS, PeerAcl comments)
exist nowhere on disk in this cell — the binary is the only copy.

The segmentation and naming machinery lives in the shared library
(binary_inspect.extract.spawnd_units, reached here through the
hatch_extract shim package like every other extractor script).
Naming runs in the library's three-step pipeline:

  1. texts from the plain string scan (each starts at a line
     exactly "[Unit]" and runs to the next text);
  2. names by CODE ATTRIBUTION — each text is produced by a tiny
     getter function in the binary's code, and the binary's own
     (getter, name) registry pairs it with its file name (the
     registry is rotated by one record; see the library docstring).
     The manifest records these entries with tier "code-attributed"
     plus the getter and registry-record addresses as evidence;
  3. HEURISTIC FALLBACK for the texts attribution did not name —
     the in-text rules (Description= base + section suffix, or a
     socket's Service= stem) and elimination against the binary's
     own unit-name pool. The manifest records these with tier
     "heuristic"; a heuristic name is a match, not a name printed
     in the text, and the archive does not present it as one.

Where both tiers would name a text and disagree, attribution is
the record and the disagreement is printed in the run summary,
never silently resolved. Texts neither tier names (on the current
binary: a socket whose registry name is stored as a code thunk,
the guest CA-trust and Home Assistant guest units, and the fused
tail blocks) are skipped and counted, never filed under a made-up
name. Two attributed names carry a directory prefix — postgresql
drop-in files — and are filed under that subdirectory.

This script maintains its own bin entry in binary-map.json
(path, sha256, timestamp, size, counts) with one contents entry
per unit file (source = the spawnd path, target, offset, len, end,
sha256, tier), so re-slicing the binary at [offset:end] reproduces
each file. The tree under binary-strings/spawnd/systemd/ exactly
reflects the current binary after every run: new and changed
units are written, vanished units are removed. Re-running on an
unchanged binary changes no file and no manifest timestamp.

spawnd is read as bytes only — it is never executed.
"""

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from hatch_extract.core import REPO  # noqa: E402
from binary_inspect.elf import ElfFile  # noqa: E402
from binary_inspect.extract import spawnd_units  # noqa: E402

SPAWND = Path("/opt/hatch/bin/spawnd")
BIN_KEY = "/opt/hatch/bin/spawnd"
TARGET_DIR = "binary-strings/spawnd/systemd"


def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def extract(repo: Path, spawnd_path: Path) -> dict:
    """Run the extraction over *spawnd_path* into *repo*.

    Returns a summary dict. Files and the manifest are only touched
    when something actually changed (idempotent re-runs).
    """
    data = spawnd_path.read_bytes()
    digest = sha256_hex(data)
    elf = ElfFile.load(spawnd_path)
    units, report = spawnd_units.name_units(data, elf)
    n_code = report[spawnd_units.TIER_CODE]
    n_heur = report[spawnd_units.TIER_HEURISTIC]
    skipped = len(report["unfiled"])

    manifest_path = repo / "binary-map.json"
    manifest = json.loads(manifest_path.read_text())
    bins = manifest.setdefault("bins", [])
    existing = next((b for b in bins if b.get("path") == BIN_KEY), None)

    # unchanged binary and unchanged tree: nothing to do
    if existing and existing.get("sha256") == digest:
        out_dir = repo / TARGET_DIR
        on_disk = {str(p.relative_to(out_dir)) for p in out_dir.rglob("*")
                   if p.is_file()}
        recorded = {c["target"][len(TARGET_DIR) + 1:]
                    for c in existing.get("contents", [])}
        if on_disk == {u.name for u in units} == recorded:
            return {"units": len(units), "code": n_code,
                    "heuristic": n_heur, "skipped": skipped,
                    "disagreements": report["disagreements"],
                    "changed": False}

    # write the tree: exactly the current units, nothing else
    out_dir = repo / TARGET_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for u in units:
        wanted.add(u.name)
        target = out_dir / u.name
        target.parent.mkdir(parents=True, exist_ok=True)
        blob = data[u.offset:u.end]
        if not target.exists() or target.read_bytes() != blob:
            target.write_bytes(blob)
    for p in sorted(out_dir.rglob("*")):
        if p.is_file() and str(p.relative_to(out_dir)) not in wanted:
            p.unlink()
    for p in sorted(out_dir.rglob("*"), reverse=True):
        if p.is_dir() and not any(p.iterdir()):
            p.rmdir()

    # (re)build this binary's manifest entry
    counts = {}
    for u in units:
        base = u.name.rsplit("/", 1)[-1]
        kind = base.rsplit(".", 1)[-1] if "." in base else "other"
        counts[kind] = counts.get(kind, 0) + 1
    entry = {
        "path": BIN_KEY,
        "sha256": digest,
        "timestamp": datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"),
        "size": len(data),
        "counts": {"units": len(units), **dict(sorted(counts.items()))},
        "contents": [
            {
                "source": BIN_KEY,
                "target": f"{TARGET_DIR}/{u.name}",
                "offset": u.offset,
                "len": u.length,
                "end": u.end,
                "sha256": sha256_hex(data[u.offset:u.end]),
                "tier": u.tier,
                **({"getter_va": u.getter_va,
                    "record_slot": u.record_slot}
                   if u.tier == spawnd_units.TIER_CODE else {}),
            }
            for u in units
        ],
    }
    if existing is None:
        bins.append(entry)
    else:
        bins[bins.index(existing)] = entry
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return {"units": len(units), "code": n_code, "heuristic": n_heur,
            "skipped": skipped,
            "disagreements": report["disagreements"],
            "changed": True}


def main() -> None:
    summary = extract(REPO, SPAWND)
    state = "updated" if summary["changed"] else "unchanged"
    print(f"spawnd systemd units: {summary['units']} extracted "
          f"({summary['code']} by code attribution, "
          f"{summary['heuristic']} by heuristic fallback), "
          f"{summary['skipped']} embedded texts unfiled ({state})")
    for d in summary["disagreements"]:
        print(f"  disagreement at offset {d['offset']}: heuristic "
              f"{d['heuristic']} vs code-attributed "
              f"{d['attributed']} (attribution recorded)")


if __name__ == "__main__":
    main()
