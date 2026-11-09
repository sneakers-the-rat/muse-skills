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
hatch_extract shim package like every other extractor script):
each unit text starts at a line exactly "[Unit]" and runs to the
next text; a unit's file name comes from its Description= base
plus its body section's suffix, or — for a socket with a prose
Description — from the stem of its own Service= line. Texts that
name nothing recoverable (prose-described slices, helper services,
guest units) are skipped and counted in the run summary, never
filed under a made-up name.

This script maintains its own bin entry in binary-map.json
(path, sha256, timestamp, size, counts) with one contents entry
per unit file (source = the spawnd path, target, offset, len, end,
sha256), so re-slicing the binary at [offset:end] reproduces each
file. The tree under binary-strings/spawnd/systemd/ exactly
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
    units = spawnd_units.segment_units(data)
    skipped = spawnd_units.unrecovered_texts(data)

    manifest_path = repo / "binary-map.json"
    manifest = json.loads(manifest_path.read_text())
    bins = manifest.setdefault("bins", [])
    existing = next((b for b in bins if b.get("path") == BIN_KEY), None)

    # unchanged binary and unchanged tree: nothing to do
    if existing and existing.get("sha256") == digest:
        on_disk = {p.name for p in (repo / TARGET_DIR).glob("*")
                   if p.is_file()}
        if on_disk == {u.name for u in units}:
            return {"units": len(units), "skipped": len(skipped),
                    "changed": False}

    # write the tree: exactly the current units, nothing else
    out_dir = repo / TARGET_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for u in units:
        wanted.add(u.name)
        target = out_dir / u.name
        blob = data[u.offset:u.end]
        if not target.exists() or target.read_bytes() != blob:
            target.write_bytes(blob)
    for p in sorted(out_dir.iterdir()):
        if p.is_file() and p.name not in wanted:
            p.unlink()

    # (re)build this binary's manifest entry
    counts = {}
    for u in units:
        kind = u.name.rsplit(".", 1)[-1]
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
            }
            for u in units
        ],
    }
    if existing is None:
        bins.append(entry)
    else:
        bins[bins.index(existing)] = entry
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return {"units": len(units), "skipped": len(skipped),
            "changed": True}


def main() -> None:
    summary = extract(REPO, SPAWND)
    state = "updated" if summary["changed"] else "unchanged"
    print(f"spawnd systemd units: {summary['units']} extracted, "
          f"{summary['skipped']} embedded texts unnamed and skipped "
          f"({state})")


if __name__ == "__main__":
    main()
