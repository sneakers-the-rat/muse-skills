"""Mechanism 5 — heuristic string-splitting (the supplement):
bundle text stored as <path><content><path><content>... with no
separators; markers are censused, clustered, sliced to the next
marker and validated.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re
import subprocess
from collections import Counter

from ..paths import (CLUSTER_GAP, KNOWN_ROOTS, MAX_FILE, MIN_CLUSTER_FILES,
                     PATHCH, SLUGS, clean_path, split_token, target_for)


def census(data, bin_path):
    raw = subprocess.run(
        ["grep", "-a", "-b", "-o", "-E",
         r"[A-Za-z0-9_.\-]+(/[A-Za-z0-9_.\-]+)*\.(md|yaml|yml|json|toml)",
         str(bin_path)], capture_output=True).stdout.decode(errors="replace")
    marks = []  # (offset, path, content_start, is_last_in_token)
    for line in raw.splitlines():
        off, _, tok = line.partition(":")
        off = int(off)
        if len(tok) > 200 or ".." in tok:
            continue
        if off > 0 and data[off - 1] in PATHCH:
            continue
        for local, sub, is_last in split_token(tok):
            marks.append((off + local, sub, off + len(tok) if is_last
                          else off + local + len(sub), is_last))
    marks.sort()
    return marks



def rodata_range(bin_path):
    out = subprocess.run(["readelf", "-S", "-W", str(bin_path)],
                         capture_output=True).stdout.decode(errors="replace")
    for line in out.splitlines():
        parts = line.split()
        # [Nr] Name Type Address Offset Size ...
        if len(parts) >= 6 and parts[1] == ".rodata":
            try:
                off = int(parts[4], 16)
                size = int(parts[5], 16)
                return off, off + size
            except ValueError:
                pass
    return 0, bin_path.stat().st_size


def find_heuristic(data, bin_path):
    """The heuristic pass from the monolith's main(): census the
    path markers, cluster them into bundles, and slice each
    candidate file's content to the next marker. Returns
    (found_h, problems, marks, bundle) where found_h maps
    source -> (content offset, body)."""
    marks = census(data, bin_path)
    r0, r1 = rodata_range(bin_path)
    rod = [m for m in marks if r0 <= m[0] < r1]
    slash_offsets = sorted(m[0] for m in rod if "/" in m[1])

    # bundle clusters: dense runs of slash-path markers
    clusters = []
    for m in rod:
        if "/" not in m[1]:
            continue
        if clusters and m[0] - clusters[-1][-1][0] <= CLUSTER_GAP:
            clusters[-1].append(m)
        else:
            clusters.append([m])
    bundle = []
    for cl in clusters:
        plausible = {clean_path(p) for _, p, _, _ in cl}
        plausible = {p for p in plausible
                     if p is not None and target_for(p) is not None}
        # A cluster is a bundle if it is dense overall, or if it is a
        # small single-root table (e.g. the activity_monitor fragments):
        # >= 4 plausible files, >= 3 of them under one root, tight span.
        roots = Counter(p.split("/")[0] for p in plausible)
        dense = len(plausible) >= MIN_CLUSTER_FILES
        small_table = (len(plausible) >= 4 and roots and
                       max(roots.values()) >= 3 and
                       cl[-1][0] - cl[0][0] <= 0x100000)
        if dense or small_table:
            bundle.extend(cl)

    # candidates: cleaned source -> [occurrences]
    cands = {}
    for off, raw, cstart, is_last in bundle:
        src = clean_path(raw)
        if src is None or target_for(src) is None:
            continue
        cands.setdefault(src, []).append((off, cstart, is_last))

    def boundary_after(anchor):
        after = [o for o in slash_offsets if o > anchor]
        return after[0] if after else len(data)

    found_h = {}   # source -> (content offset, body)
    problems = []
    for src in sorted(cands):
        done = False
        for off, cstart, is_last in cands[src]:
            end = cstart if not is_last else boundary_after(off)
            body = data[cstart:end]
            if validate(body, is_last) is not None:
                continue
            found_h[src] = (cstart, body)
            done = True
            break
        if not done:
            problems.append(src)

    # Special case: arithmetic-and-counting has no SKILL.md marker; its
    # guide starts at its '# Arithmetic and counting' heading, inside the
    # guide cluster (the cluster holding the other guide slugs).
    src = "arithmetic-and-counting/SKILL.md"
    if src not in found_h:
        guide = [m for m in bundle if clean_path(m[1]) in
                 {f"{s}/SKILL.md" for s in SLUGS}]
        if guide:
            lo = min(m[0] for m in guide) - CLUSTER_GAP
            hi = max(m[0] for m in guide) + CLUSTER_GAP
            h = data.find(b"# Arithmetic and counting", lo, hi)
            if h != -1:
                body = data[h:boundary_after(h)]
                if validate(body, True) is None:
                    found_h[src] = (h, body)
    return found_h, problems, marks, bundle, cands



def validate(body, is_last):
    """Return None if the slice looks like a stored file, else a reason."""
    if len(body) == 0:
        return None if not is_last else "empty slice"
    if len(body) > MAX_FILE:
        return f"size {len(body)} rejected"
    if b"\x00" in body:
        return "NUL bytes in slice"
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return "slice is not UTF-8"
    if text.startswith('"') or text.startswith("` -"):
        return "list/index fragment, not a file"
    if text[0].islower() and not re.match(r"^[a-z_]+:", text):
        return "starts mid-sentence (a mention, not a file start)"
    return None

