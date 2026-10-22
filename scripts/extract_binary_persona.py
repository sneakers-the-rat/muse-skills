#!/usr/bin/env python3
"""The browser_persona TOPICAL curation of binary strings.

Sibling of extract_binary_strings.py (the bot_challenge curation),
built the same way: all general machinery lives in
binary_string_methods.py; this file holds only what is specific to
the browser-persona topic — how the browser fabricates the identity
it presents to pages, how that identity is seeded and selected, and
how the system verifies what pages actually observe.

What this curation produces, under binary-strings/browser/persona/:

  global-config.yaml     the browsers/persona/web_bot_auth/egress
                         sections of the embedded default.yaml —
                         the lane system (realtime vs background),
                         the default persona per lane, the
                         hatch_browser_enhanced kill switch, the
                         default egress chain
  site-personas.yaml     the persona: blocks the per-site configs
                         pin (aa.com, ebay.com, macys.com present
                         macOS on the realtime lane), with the
                         egress: inversions of ridge.com and
                         threadless.com alongside as the related
                         route configuration
  telemetry-fields.txt   the browser_document_persona_* and
                         browser_document_fingerprint_* telemetry
                         field families and the browser_persona_seed
                         / browser_profile_mode counters — the
                         selection, seeding and probing pipeline as
                         the instrumentation names it
  structs.txt            field clusters for the persona-adjacent
                         schemas: DocumentPersonaSeedIdentity,
                         DocumentFingerprintObservation,
                         BrowserRequestDocument, BrowserRequestEgress,
                         BrowserControlSnapshot
  observed-fingerprint-paths.txt
                         the observed-fingerprint path vocabulary
                         (/identity/platform, /webgl/.../renderer,
                         /display/screen/width, /locale/...) — the
                         surfaces the probe reads back. NOTE: the
                         collector script that produces these values
                         is NOT in this binary (no getHighEntropyValues
                         or WEBGL_debug_renderer_info text exists in
                         it); this binary holds the output schema,
                         and the collector is hashed at runtime
                         (browser_document_fingerprint_collector_sha256)
  module-paths.txt       the implementation's source paths:
                         hatch-protocol/src/browser_persona/
                         {native_document,observed_fingerprint}.rs

Every file is registered in binary-map.json with
"topic": "browser_persona" — see extract_binary_strings.py for the
registration and hash rules, which are identical.
"""
import hashlib
import re
import sys
from pathlib import Path

import binary_string_methods as M

BIN = Path("/opt/hatch/bin/hatch")
REPO = Path(__file__).resolve().parent.parent
ROOT = REPO / "binary-strings"
TOPIC = "browser_persona"
BP = "binary-strings/browser/persona"

STRUCTS = (b"DocumentPersonaSeedIdentity",
           b"DocumentFingerprintObservation",
           b"BrowserRequestDocument", b"BrowserRequestEgress",
           b"BrowserControlSnapshot")


def yaml_sections(text, keys):
    """The named top-level sections of a small YAML document, each
    with the comment lines that precede it. Returns text."""
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if any(line.startswith(k + ":") for k in keys):
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ")
                                      or lines[j].startswith("-")
                                      or not lines[j].strip()):
                j += 1
            out.extend(lines[i:j])
            i = j
        elif line.startswith("#"):
            # keep a comment block only if a wanted section follows
            j = i
            while j < len(lines) and lines[j].startswith("#"):
                j += 1
            if j < len(lines) and any(
                    lines[j].startswith(k + ":") for k in keys):
                out.extend(lines[i:j])
                i = j
            else:
                i = j
        else:
            i += 1
    return "".join(out)


def main():
    data = BIN.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    manifest = M.load_manifest(REPO)
    if manifest is None:
        print("binary-map.json missing; run extract_binary_files.py "
              "first", file=sys.stderr)
        return 1
    binrec = manifest["bins"][0]
    if not M.check_binary(binrec, sha):
        print("binary differs from binary-map.json; run "
              "extract_binary_files.py first", file=sys.stderr)
        return 1
    if M.already_done(binrec, REPO, TOPIC):
        print(f"binary unchanged ({sha[:12]}…); {TOPIC} curation "
              "skipped")
        return 0

    reg = M.Registrar(REPO, TOPIC)
    contents = binrec["contents"]

    # ---- the global browser config's relevant sections --------------
    for c in contents:
        if c.get("source") == "default.yaml":
            f = REPO / c["target"]
            if f.exists():
                sections = yaml_sections(
                    f.read_text(),
                    ("browsers", "persona", "web_bot_auth", "egress"))
                reg.write_and_register(
                    "browsers/persona/web_bot_auth/egress sections "
                    "of the embedded default.yaml (global browser "
                    "configuration)", f"{BP}/global-config.yaml",
                    c["offset"],
                    "# From the embedded default.yaml — the global "
                    "browser configuration.\n" + sections)
            break

    # ---- per-site persona and egress configuration -------------------
    blocks = []
    first_off = None
    for c in contents:
        if "source" not in c:
            continue
        t = c["target"]
        if not (t.startswith("binary-strings/browser/site-config/")
                and t.endswith("/config.yaml")):
            continue
        f = REPO / t
        if not f.exists():
            continue
        text = f.read_text()
        secs = yaml_sections(text, ("persona", "egress"))
        # keep only configs that pin a persona, or whose egress
        # section LEADS with residential (an inversion of the global
        # default order — a trailing residential is just the default
        # fallback and is not a per-site choice)
        has_persona = "persona:" in secs
        egress_inverted = False
        if "egress:" in secs:
            tail = secs.split("egress:", 1)[1]
            i = tail.find("- via:")
            if i != -1 and tail[i:].startswith("- via: residential"):
                egress_inverted = True
        if not (has_persona or egress_inverted):
            continue
        domain = t.split("/")[3]
        blocks.append(f"# {domain}\n{secs}")
        if first_off is None:
            first_off = c["offset"]
    if blocks:
        reg.write_and_register(
            "persona:/egress: sections of the per-site configs "
            "that pin a persona or invert the egress order",
            f"{BP}/site-personas.yaml", first_off or 0,
            "\n".join(blocks))

    # ---- telemetry identifier families --------------------------------
    # The identifiers live inside enormous fused schema runs with no
    # delimiters, so the census segments the runs at family-stem
    # boundaries: a token runs from a family stem (browser_document_
    # persona_*, ..._fingerprint_*, ..._observed_*,
    # document_fingerprint_observer_*, browser_persona*,
    # browser_profile_mode) to the next browser_/document_ stem or
    # the first byte outside [a-z0-9_]. Tokens that still fail the
    # family shape afterwards are listed verbatim under
    # "# fused remainders" rather than silently repaired.
    stems = (b"browser_", b"document_")
    fam_stems = (rb"browser_document_persona_",
                 rb"browser_document_fingerprint_",
                 rb"browser_document_observed_",
                 rb"document_fingerprint_observer_",
                 rb"browser_persona", rb"browser_profile_mode")
    starts = set()
    for fam in fam_stems:
        for m in re.finditer(fam, data):
            starts.add(m.start())
    # A segmented token counts as clean only if what follows its
    # family stem is a sequence of words from this closed telemetry
    # vocabulary; anything else keeps a glued neighbour and is
    # listed verbatim as a fused remainder instead.
    vocab = {
        "active", "architecture", "at", "attribution", "capacity",
        "captures", "chrome", "collector", "concurrency", "config",
        "dedupe", "delivery", "device", "discontinuities", "documents",
        "dropped", "duration", "events", "evidence", "evictions",
        "failed", "gb", "generation", "gpu", "hardware", "height",
        "id", "instance", "json", "malformed", "measured", "memory",
        "model", "ms", "not", "observations", "observed", "os",
        "parameters", "partial", "pending", "pixel", "platform",
        "probe", "ratio", "reason", "renderer", "scope", "screen",
        "seed", "selection", "sha256", "site", "snapshot", "source",
        "state", "status", "timezone", "total", "trigger", "version",
        "width",
    }

    def remainder_clean(tok):
        for fam in (b"browser_document_persona_",
                    b"browser_document_fingerprint_",
                    b"browser_document_observed_",
                    b"document_fingerprint_observer_",
                    b"browser_persona", b"browser_profile_mode"):
            fs = fam.decode()
            if tok.startswith(fs):
                rest = tok[len(fs):].strip("_")
                if not rest:
                    return True
                return all(w in vocab for w in rest.split("_"))
        return False

    clean, fused = {}, {}
    word = re.compile(rb"[a-z0-9_]+")
    for s in sorted(starts):
        m = word.match(data, s)
        if not m:
            continue
        end = m.end()
        for stem in stems:
            nxt = data.find(stem, s + len(stem))
            if nxt != -1 and nxt < end:
                end = nxt
        tok = data[s:end].decode()
        if remainder_clean(tok):
            clean.setdefault(tok, s)
        else:
            fused.setdefault(tok, s)
    if clean or fused:
        body = "\n".join(sorted(clean))
        if fused:
            body += ("\n\n# fused remainders (verbatim; a neighbour "
                     "from another family is glued on and no clean "
                     "boundary exists in the binary):\n"
                     + "\n".join(sorted(fused)))
        first = min(list(clean.values()) + list(fused.values()))
        reg.write_and_register(
            "census of browser_document_persona_*/"
            "browser_document_fingerprint_* telemetry identifiers, "
            "segmented from the fused schema runs at family-stem "
            "boundaries", f"{BP}/telemetry-fields.txt",
            first, body + "\n")

    # ---- persona-adjacent struct field clusters -----------------------
    parts = []
    first = None
    for struct in STRUCTS:
        best = None
        for m in re.finditer(re.escape(struct), data):
            win = data[max(0, m.start() - 100):m.start() + 1600]
            score = win.count(b"/") + win.count(b"_")
            if best is None or score > best[1]:
                best = (m.start(), score, win)
        if best:
            parts.append(f"@@ {struct.decode()} (window at "
                         f"0x{best[0]:x})\n".encode() + best[2])
            if first is None or best[0] < first:
                first = best[0]
    if parts:
        reg.write_and_register(
            "field clusters of the persona-adjacent observation "
            "structs", f"{BP}/structs.txt", first or 0,
            b"\n\n".join(parts))

    # ---- the observed-fingerprint path vocabulary ---------------------
    # The paths live in ONE fused cluster (see structs.txt): each
    # path runs from a root marker (/identity/, /webgl/, /display/,
    # /locale/) to the next root marker. The cluster's tail glues
    # the observation's own next field names (attempted, index,
    # event) onto the final path; those are cut, and the cut is
    # documented in the file rather than hidden.
    for m in M.PRINT_RUN.finditer(data):
        if b"/identity/platform" in m.group() and \
                b"/webgl/" in m.group():
            cluster = m.group()
            marks = [mm.start() for mm in re.finditer(
                rb"/(?:identity|webgl|display|locale)/", cluster)]
            segments = []
            for i, st in enumerate(marks):
                en = marks[i + 1] if i + 1 < len(marks) \
                    else len(cluster)
                seg = cluster[st:en].decode("utf-8", "replace")
                if i + 1 == len(marks):
                    seg = seg.split("attempted")[0]
                if seg.startswith("/") and " " not in seg:
                    segments.append(seg)
            body = ("# The observed-fingerprint paths, segmented "
                    "from the fused schema cluster at their root "
                    "markers. In the cluster the final path is "
                    "followed by the observation's own field names "
                    "(attempted, index, event) — not part of any "
                    "path — and they are cut here.\n"
                    + "\n".join(segments))
            reg.write_and_register(
                "observed-fingerprint path vocabulary, segmented "
                "from the fused schema cluster at root markers "
                "(the surfaces the fingerprint probe reads back)",
                f"{BP}/observed-fingerprint-paths.txt", m.start(),
                body + "\n")
            break

    # ---- implementation source paths ----------------------------------
    paths = sorted({m.group().decode()
                    for m in re.finditer(
                        rb"[a-z0-9_/.-]*browser_persona/[a-z_]+\.rs",
                        data)})
    if paths:
        off = data.find(paths[0].encode())
        reg.write_and_register(
            "browser_persona module source paths",
            f"{BP}/module-paths.txt", off, "\n".join(paths) + "\n")

    # ---- prune this curation's stale outputs, update the manifest -----
    bp_dir = ROOT / "browser" / "persona"
    owned = [p for p in bp_dir.rglob("*") if p.is_file()] \
        if bp_dir.exists() else []
    M.prune_owned(REPO, owned, reg.produced)
    M.finish_manifest(manifest, binrec, TOPIC, reg.entries)
    M.save_manifest(REPO, manifest)
    print(f"{TOPIC} curation files: {len(reg.entries)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
