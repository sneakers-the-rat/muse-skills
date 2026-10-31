"""The extraction pipeline: one pass over the binary walking the
mechanism registry in authority order, writing every artifact it
produces into the archive tree and registering every one of them
in binary-map.json — the one manifest. By construction there is
no other bookkeeping: a mechanism's output that is not in the
manifest is not written.

Ported from scripts/extract_binary_files.py main() in the
2026-10-31 package restructure; mechanisms 7-13 and the byte
accounting are new. Provenance is one-way: binary-map.json is a
record of where files came from, never a lookup table — its one
functional use is the hash check below.
"""
import hashlib
import json
import subprocess
import sys
import traceback
from collections import Counter
from datetime import datetime, timezone

from . import accounting
from .core import DEFAULT_BIN, REPO, Binary
from .elftools import _text_ok, elf_maps, lea_census
from .mechanisms import agent_definitions as m_agent
from .mechanisms import bare_prompts as m_bare
from .mechanisms import code_literals as m_code
from .mechanisms import heuristic as m_heur
from .mechanisms import length_prefixed as m_lenp
from .mechanisms import nul_strings as m_nul
from .mechanisms import panic_locations as m_panic
from .mechanisms import prose_regions as m_prose
from .mechanisms import register_descriptors as m_reg
from .mechanisms import slices as m_slices
from .mechanisms import static_refs as m_static
from .mechanisms import struct_descriptors as m_struct
from .mechanisms import tables as m_tables
from .paths import target_for

MANAGED_ROOTS = ["system_prompts", "binary-skills", "binary-etc",
                 "binary-strings/agent-definitions",
                 "binary-strings/agent-prompts",
                 "binary-strings/prose-regions",
                 "binary-strings/referred",
                 "binary-strings/artifacts",
                 "binary-strings/browser/instructions",
                 "binary-strings/browser/site-config",
                 "binary-strings/browser/workflows",
                 "binary-strings/self_improvement"]


def _new_mechanism_pass(data, secs, v2o, _slices, lea_sites,
                        found, put, d_agents, sha):
    """Mechanisms 7-13: prose regions, the string-reference
    census, bare prompts, and the byte accounting. Kept apart
    from the core pass so run_extract can guard it: a failure
    here must never kill the core extraction the archive
    backup depends on. Returns the pieces the write phase
    needs."""
    # ---- mechanism 7: prose regions over .rodata ----------------------
    ro = secs[".rodata"]
    r0, r1 = ro[4], ro[4] + ro[5]
    regions = m_prose.prose_regions(data, r0, r1)
    for reg in regions:
        off = reg["offset"]
        put(f"prose-regions/region-{off:08x}.txt", off, reg["body"],
            "prose-region",
            extra={"features": reg["features"],
                   "prompt_score": reg["prompt_score"]})

    # ---- mechanisms 9-13: the string-reference census ------------------
    static_spans = m_static.static_refs(_slices, v2o)
    extents = m_code.literal_extents(data, v2o, lea_sites)
    file_starts = {off for off, _b, _v in found.values()}
    starts_all = m_code.boundary_starts(
        extents, file_starts | {s["offset"] for s in static_spans})
    code_spans = []       # {offset, len, refs, form, tier}
    weak_code = []        # candidates below the boundary bar
    for start, lens in extents.items():
        for length, sup in lens.items():
            rec = {"offset": start, "len": length, "refs": sup,
                   "form": "code-referenced literal (lea+imm)"}
            if m_code.end_is_boundary(start + length, starts_all,
                                      len(data)):
                rec["tier"] = "strong"
                code_spans.append(rec)
            else:
                rec["tier"] = "weak"
                weak_code.append(rec)
    panic_spans = m_panic.panic_locations(data, _slices, v2o)
    string_sections = [(ro[4], ro[5])] + [
        (v[4], v[5]) for name, v in secs.items()
        if name.startswith(".rodata.") and v[5] > 0]
    nul_spans = m_nul.nul_strings(data, string_sections)
    lenp_spans = m_lenp.length_prefixed(data, string_sections)

    # ---- mechanism 8: bare prompts -------------------------------------
    covered_spans = [(off, off + len(body))
                     for off, body, _v in found.values()
                     if _v != "prose-region"]
    carved, dup_prompts, bare_problems = m_bare.bare_prompts(
        data, d_agents, extents, covered_spans, starts_all)
    for p in bare_problems:
        print(f"  SKIP {p}", file=sys.stderr)
    for aid, c in carved.items():
        put(f"agent-prompts/{aid}.md", c["offset"], c["body"],
            "bare-prompt",
            extra={"note": f"carved by mechanism 8 "
                           f"({c['rule']}); code-reference support "
                           f"{c['support']}"})

    # ---- referred-span index + byte accounting --------------------------
    span_forms = {}

    def add_span(off, length, form, refs):
        key = (off, length)
        rec = span_forms.setdefault(
            key, {"offset": off, "len": length, "refs": 0, "forms": []})
        rec["refs"] += refs
        if form not in rec["forms"]:
            rec["forms"].append(form)

    for s in static_spans:
        add_span(s["offset"], s["len"], s["form"], s["refs"])
    for s in code_spans:
        add_span(s["offset"], s["len"], s["form"], s["refs"])
    for s in panic_spans:
        add_span(s["offset"], s["len"], s["form"], s["refs"])
    for s in nul_spans:
        add_span(s["offset"], s["len"], s["form"], s["refs"])
    for s in lenp_spans:
        add_span(s["offset"], s["len"], s["form"], s["refs"])
    referred = sorted(span_forms.values(), key=lambda r: r["offset"])
    weak_kept = [w for w in weak_code if w["refs"] >= 2]
    weak_dropped = [w for w in weak_code if w["refs"] < 2]

    span_sets = {
        "extracted files (mechanisms 1-6)": [
            (off, off + len(body)) for off, body, via in found.values()
            if via not in ("prose-region", "bare-prompt")],
        "bare prompts (mechanism 8)": [
            (off, off + len(body)) for off, body, via in found.values()
            if via == "bare-prompt"],
        "static fat-pointers (mechanism 9)": [
            (s["offset"], s["offset"] + s["len"]) for s in static_spans],
        "code literals, boundary-validated (mechanism 10)": [
            (s["offset"], s["offset"] + s["len"]) for s in code_spans],
        "panic Location strings (mechanism 11)": [
            (s["offset"], s["offset"] + s["len"]) for s in panic_spans],
        "NUL-terminated strings (mechanism 12)": [
            (s["offset"], s["offset"] + s["len"]) for s in nul_spans],
        "length-prefixed strings (mechanism 13)": [
            (s["offset"], s["offset"] + s["len"]) for s in lenp_spans],
        "prose regions (mechanism 7, segmentation)": [
            (r["offset"], r["end"]) for r in regions],
    }
    acct_sections = [(name, v[4], v[5]) for name, v in secs.items()
                     if v[5] > 0 and v[1] != 8 and name and v[2] & 0x2]
    acct = accounting.build_accounting(data, acct_sections, span_sets)
    acct["weak_code_candidates"] = {
        "kept_in_index_refs_ge_2": len(weak_kept),
        "dropped_refs_1": len(weak_dropped),
        "dropped_bytes": sum(w["len"] for w in weak_dropped),
        "note": "code-literal candidates whose end is not "
                "boundary-validated; refs>=2 are in the index, "
                "refs==1 are counted here, not in coverage",
    }
    acct["binary_sha256"] = sha
    return {"regions": regions, "carved": carved,
            "dup_prompts": dup_prompts, "referred": referred,
            "weak_kept": weak_kept, "weak_dropped": weak_dropped,
            "acct": acct}


def run_extract(repo=REPO, bin_path=DEFAULT_BIN):
    b = Binary(bin_path)
    data = b.data
    sha = b.sha256()
    # Skip rule: if the binary is the one the manifest records and
    # every recorded target is on disk, the embedded strings cannot
    # have changed. The new-mechanism keys are required, so a
    # manifest written by the pre-package extractor never skips.
    manifest_path = repo / "binary-map.json"
    if manifest_path.exists():
        try:
            old = json.loads(manifest_path.read_text())
            oldbin = old["bins"][0]
            if oldbin["sha256"] == sha and \
                    oldbin.get("agent_definitions") is not None and \
                    oldbin.get("prose_regions") is not None and \
                    oldbin.get("agent_prompts") is not None and \
                    oldbin.get("referred_spans") is not None and all(
                    (repo / c["target"]).exists()
                    for c in oldbin["contents"]):
                print(f"binary unchanged ({sha[:12]}…); extraction skipped")
                return 0
        except (ValueError, KeyError, IndexError, TypeError):
            pass  # a malformed manifest is just re-created below

    # ---- mechanism 5 (computed first): heuristic splitting ---------
    found_h, problems, marks, bundle, cands = m_heur.find_heuristic(
        data, bin_path)

    # ---- deterministic phases ---------------------------------------
    _loads, secs, v2o, o2v = elf_maps(data)
    _slices, by_target, pairs = m_tables.build_slices(data, secs, v2o)
    lea_sites = lea_census(data, secs, v2o)
    d_struct = m_struct.struct_descriptors(data, secs, v2o, lea_sites)
    starts = {cs for cs, _b in found_h.values()}
    starts |= {cfo for cfo, _ln in d_struct.values()}
    starts |= {v2o(tv) for tv, _ln in pairs.values()}
    starts.discard(None)
    d_reg = m_reg.register_descriptors(data, secs, v2o, lea_sites,
                                       set(pairs) | set(d_struct), starts)

    if not bundle and not pairs:
        print("ERROR: no bundle clusters or tables found — binary "
              "layout changed; refusing to write an empty extraction",
              file=sys.stderr)
        return 1

    # ---- merge by authority: table > slice > struct > register > heur.
    RANK = {"table": 7, "agent-def": 7, "bare-prompt": 7, "slice": 6,
            "descriptor-struct": 5, "descriptor-register": 4,
            "matcher": 3, "descriptor-general": 2, "heuristic": 1,
            "prose-region": 1}
    found = {}   # source -> (offset, body, via)
    rank = {}
    extras = {}  # source -> extra manifest fields

    def put(s, off, body, via, extra=None):
        if RANK[via] > rank.get(s, 0):
            found[s] = (off, body, via)
            rank[s] = RANK[via]
            if extra:
                extras[s] = extra

    for s, (cs, body) in found_h.items():
        put(s, cs, body, "heuristic")
    m_slices.confirm_slices(found, put, by_target, data, o2v)
    for s, (cfo, ln) in d_struct.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-struct")
    for s, (cfo, ln) in d_reg.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-register")
    for s, (tv, ln) in pairs.items():
        if target_for(s) is not None:
            tfo = v2o(tv)
            if tfo is not None:
                put(s, tfo, data[tfo:tfo + ln], "table")
    # general floating-arrangement reader for what is still heuristic
    starts_g = set(starts)
    for _off, _raw, _cs, _il in marks:
        starts_g.add(_off)
        starts_g.add(_cs)
    for _cfo, _ln in d_struct.values():
        starts_g.add(_cfo)
        starts_g.add(_cfo + _ln)
    for _cfo, _ln in d_reg.values():
        starts_g.add(_cfo)
    todo_h = {s: cs for s, (cs, _b) in found_h.items()
              if rank.get(s, 0) < RANK["descriptor-general"]}
    d_gen = m_reg.general_descriptors(data, secs, v2o, o2v, lea_sites,
                                      todo_h, starts_g)
    for s, (cfo, ln) in d_gen.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "descriptor-general")
    # jump-table matcher arms, for anything still below that rank
    wanted_m = {s for s in set(cands) | set(found_h)
                if rank.get(s, 0) < RANK["matcher"]}
    d_match = m_reg.matcher_descriptors(data, secs, v2o, wanted_m)
    for s, (cfo, ln) in d_match.items():
        if target_for(s) is not None:
            put(s, cfo, data[cfo:cfo + ln], "matcher")
    # ---- mechanism 6: agent definitions ------------------------------
    d_agents, agent_problems = m_agent.agent_definitions(data)
    for aid, (cfo, body) in d_agents.items():
        put(f"agent-definitions/{aid}.toml", cfo, body, "agent-def")
    for p in agent_problems:
        print(f"  SKIP {p}", file=sys.stderr)
    problems = [p for p in problems if p not in found]

    # ---- mechanisms 7-13 (guarded: a failure here must never
    # kill the core extraction — the archive backup depends on it.
    # On failure the new-mechanism puts are rolled back, the
    # manifest lacks the new keys, and the next run retries.)
    r0 = secs[".rodata"][4]
    regions, carved, dup_prompts = [], {}, {}
    referred, weak_kept, weak_dropped, acct = [], [], [], None
    try:
        newres = _new_mechanism_pass(data, secs, v2o, _slices,
                                     lea_sites, found, put,
                                     d_agents, sha)
        regions = newres["regions"]
        carved = newres["carved"]
        dup_prompts = newres["dup_prompts"]
        referred = newres["referred"]
        weak_kept = newres["weak_kept"]
        weak_dropped = newres["weak_dropped"]
        acct = newres["acct"]
    except Exception:
        traceback.print_exc()
        print("ERROR: mechanisms 7-13 failed — continuing with "
              "the core extraction only; the manifest will lack "
              "the new keys and the next run retries them",
              file=sys.stderr)
        for s in [s for s, (_o, _b, v) in list(found.items())
                  if v in ("prose-region", "bare-prompt")]:
            del found[s]
            rank.pop(s, None)
            extras.pop(s, None)

    # ---- write ---------------------------------------------------------
    contents = []
    n_new = n_changed = 0
    for s in sorted(found):
        off, body, _via = found[s]
        target = target_for(s)
        dest = repo / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            if dest.read_bytes() != body:
                n_changed += 1
                dest.write_bytes(body)
        else:
            n_new += 1
            dest.write_bytes(body)
        entry = {"source": s, "target": target, "offset": off,
                 "len": len(body), "end": off + len(body),
                 "sha256": hashlib.sha256(body).hexdigest()}
        entry.update(extras.get(s, {}))
        contents.append(entry)
    # duplicate bare-prompt copies: same target, second offset
    for aid, offs in sorted(dup_prompts.items()):
        c = carved[aid]
        for off in offs:
            contents.append({
                "source": f"agent-prompts/{aid}.md",
                "target": f"binary-strings/agent-prompts/{aid}.md",
                "offset": off, "len": len(c["body"]),
                "end": off + len(c["body"]),
                "sha256": hashlib.sha256(c["body"]).hexdigest(),
                "note": "second embedded copy; bytes identical to "
                        "the primary carve"})
    if acct is not None:
        # the referred index + accounting are artifacts too: registered
        index_lines = ["offset,len,refs,forms"]
        for r in referred:
            index_lines.append(f"{r['offset']},{r['len']},{r['refs']},"
                               f"{'+'.join(r['forms'])}")
        for w in weak_kept:
            index_lines.append(f"{w['offset']},{w['len']},{w['refs']},"
                               "code-referenced literal (lea+imm) [weak]")
        index_blob = ("\n".join(index_lines) + "\n").encode()
        acct_blob = (json.dumps(acct, indent=1) + "\n").encode()
        for target, blob, match, moff in (
                ("binary-strings/referred/INDEX.csv", index_blob,
                 "referred string spans (mechanisms 9-13): offset,len,"
                 "refs,forms", referred[0]["offset"] if referred else 0),
                ("binary-strings/referred/ACCOUNTING.json", acct_blob,
                 "byte accounting of every section by span kind", r0)):
            dest = repo / target
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists() or dest.read_bytes() != blob:
                dest.write_bytes(blob)
            contents.append({"match": match, "target": target,
                             "offset": moff, "topic": "referred"})
    contents.sort(key=lambda c: c["target"])

    # ---- prune stale outputs (monolith rules) --------------------------
    keep = {c["target"] for c in contents}
    tracked = set(subprocess.run(
        ["git", "-C", str(repo), "ls-files"], capture_output=True,
        text=True).stdout.split())
    pruned = preserved = 0
    for root in MANAGED_ROOTS:
        base = repo / root
        if not base.is_dir():
            continue
        for f in sorted(base.rglob("*"), reverse=True):
            rel = f.relative_to(repo).as_posix()
            if f.is_file() and rel not in keep:
                if rel in tracked:
                    f.unlink()
                    pruned += 1
                else:
                    preserved += 1
            elif f.is_dir() and not any(f.iterdir()):
                f.rmdir()
    if pruned:
        print(f"pruned {pruned} stale extracted files")
    if preserved:
        print(f"preserved {preserved} untracked (unclassified) files")

    # ---- manifest -------------------------------------------------------
    rodata_acct = next((a for a in acct["sections"]
                        if a["section"] == ".rodata"), None) \
        if acct is not None else None
    manifest = {"bins": [{
        "path": str(bin_path),
        "sha256": sha,
        "timestamp": datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"),
        "size": len(data),
        "agent_definitions": sum(
            1 for c in contents
            if c["target"].startswith("binary-strings/agent-definitions/")),
        "prose_regions": sum(
            1 for c in contents
            if c["target"].startswith("binary-strings/prose-regions/")),
        "agent_prompts": sum(
            1 for c in contents
            if c["target"].startswith("binary-strings/agent-prompts/")),
        "referred_spans": (len(referred) + len(weak_kept)) if acct is not None else None,
        "accounting": {
            "file": "binary-strings/referred/ACCOUNTING.json",
            "rodata_covered_bytes":
                rodata_acct["covered_bytes"] if rodata_acct else None,
            "rodata_size": rodata_acct["size"] if rodata_acct else None,
            "rodata_residual_bytes":
                rodata_acct["residual_bytes"] if rodata_acct else None,
        },
        "contents": contents,
    }]}
    (repo / "binary-map.json").write_text(
        json.dumps(manifest, indent=2) + "\n")
    vias = Counter(v for _o, _b, v in found.values())
    print(f"binary {sha[:12]}… size {len(data)}")
    print(f"extracted {len(contents)} files; skipped {len(problems)}")
    print(f"by mechanism: {dict(vias)}")
    print(f"new on disk: {n_new}; changed on disk: {n_changed}")
    print(f"heuristic-only residue: {vias.get('heuristic', 0)}")
    print(f"prose regions: {len(regions)} "
          f"({sum(r['end'] - r['offset'] for r in regions)} bytes)")
    print(f"bare prompts carved: {len(carved)} "
          f"({', '.join(sorted(carved))})")
    print(f"referred spans: {len(referred)} strong + "
          f"{len(weak_kept)} weak kept; "
          f"{len(weak_dropped)} weak dropped")
    if rodata_acct:
        print(f".rodata accounting: {rodata_acct['covered_bytes']} of "
              f"{rodata_acct['size']} bytes covered "
              f"({rodata_acct['covered_fraction']:.1%}); residual "
              f"{rodata_acct['residual_bytes']} bytes in "
              f"{rodata_acct['residual_classes']}")
    file_spans = sorted((off, off + len(body))
                        for off, body, via in found.values()
                        if via not in ("prose-region", "bare-prompt"))
    for p in problems:
        occ = []
        i = data.find(p.encode())
        while i != -1:
            occ.append(i)
            i = data.find(p.encode(), i + 1)
        mention = bool(occ) and all(
            any(a <= o < b for a, b in file_spans) for o in occ)
        print(f"  SKIP {'(mention) ' if mention else ''}{p}",
              file=sys.stderr)
    b.close()
    return 0
