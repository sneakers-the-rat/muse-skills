"""Shared core for hatch_extract: the binary reader, the manifest
(binary-map.json) plumbing, and the curation Registrar.

The Binary reader is mmap-backed: mechanisms receive a bytes-like
view and slice it; the binary is never loaded whole into RAM.
Its SHA-256 is computed by streaming.

The manifest helpers and Registrar are ported verbatim from
scripts/binary_string_methods.py in the 2026-10-31 package
restructure (that module is now a shim over this one).
"""
import hashlib
import json
import mmap
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
DEFAULT_BIN = pathlib.Path("/opt/hatch/bin/hatch")


class Binary:
    """An mmap view of one binary plus its streamed SHA-256."""

    def __init__(self, path=DEFAULT_BIN):
        self.path = pathlib.Path(path)
        self._f = open(self.path, "rb")
        self.data = mmap.mmap(self._f.fileno(), 0,
                              access=mmap.ACCESS_READ)
        self.size = len(self.data)

    def sha256(self):
        h = hashlib.sha256()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()

    def close(self):
        self.data.close()
        self._f.close()


# ---- manifest plumbing -------------------------------------------------
# binary-map.json holds one bin record whose "contents" mix the file
# extractor's generic entries ({"source", "target", "offset"}) with
# topical curations' entries ({"match", "target", "offset", "topic"}).

def load_manifest(repo):
    p = repo / "binary-map.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def save_manifest(repo, manifest):
    (repo / "binary-map.json").write_text(
        json.dumps(manifest, indent=2) + "\n")


def check_binary(binrec, sha):
    """A curation refuses to run against a binary the manifest does
    not describe (run extract first)."""
    return binrec["sha256"] == sha


def own_entries(binrec, topic):
    """This topic's registered entries. Legacy entries without a
    topic field belong to the first curation (bot_challenge) — the
    default in the bot_challenge curation's TOPIC handling."""
    return [c for c in binrec["contents"]
            if "match" in c and c.get("topic", topic) == topic]


def already_done(binrec, repo, topic):
    """Skip rule: this topic's entries are registered and every
    target is present on disk."""
    entries = own_entries(binrec, topic)
    return bool(entries) and all(
        (repo / c["target"]).exists() for c in entries)


class Registrar:
    """Collects a curation's outputs: writes files under the repo and
    records their manifest entries under the curation's topic."""

    def __init__(self, repo, topic):
        self.repo = repo
        self.topic = topic
        self.entries = []
        self.produced = set()

    def write(self, target, blob):
        p = self.repo / target
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(blob, str):
            blob = blob.encode()
        p.write_bytes(blob)

    def register(self, match, target, offset):
        self.entries.append({"match": match, "target": target,
                             "offset": offset, "topic": self.topic})
        self.produced.add(target)

    def write_and_register(self, match, target, offset, blob):
        self.write(target, blob)
        self.register(match, target, offset)


def prune_owned(repo, candidates, produced):
    """Delete candidate files (the curation's own owned paths) that
    this run did not produce, and remove directories they emptied.
    Candidates must be scoped by the curation to what it owns —
    other extractions' files are never passed in."""
    for f in candidates:
        rel = f.relative_to(repo).as_posix()
        if f.is_file() and rel not in produced:
            f.unlink()
    # second pass: empty directories among the candidates' parents
    dirs = sorted({f.parent for f in candidates},
                  key=lambda d: len(d.parts), reverse=True)
    for d in dirs:
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()


def finish_manifest(manifest, binrec, topic, entries):
    """Replace this topic's entries in the manifest with the new
    ones, keeping the file extractor's entries and every other
    topic's entries. Contents stay sorted by target."""
    keep = [c for c in binrec["contents"]
            if "source" in c
            or ("match" in c and c.get("topic", topic) != topic)]
    binrec["contents"] = sorted(keep + entries,
                                key=lambda c: c["target"])
    return manifest
