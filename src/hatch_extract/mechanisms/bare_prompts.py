"""Mechanism 8 — bare-prompt carving + needle attribution.

Some agents' prompts are stored as bare &str constants in the fused
string pool: no path, no delimiters. The prompt census (2026-10-31)
found five by hand, with hand-read endpoints. This mechanism is the
general form of that carve:

  * Extents come from the code itself (mechanism 10's census):
    a lea site materializes the prompt's (ptr, len), so the span
    is exact — endpoints are the compiler's, not a guess.
  * Attribution rides the census's needle ladder, strongest first:
    (1) the prompt abuts the agent's own id string in the pool;
    (2) the body names a tool unique to one agent;
    (3) the body opens with a markdown heading whose words match
        exactly one agent's id/name vocabulary (distinctive words
        weigh double);
    (4) the body contains a word distinctive to one agent and
        opens with an instruction opener.
    Adjacency alone is never proof: every carve is an attributed,
    boundary-validated, prompt-shaped extent.
  * Endpoint selection: among the code-candidate lengths at an
    attributed start, take the shortest that is boundary-validated
    (another referenced span starts at its end, or one byte later
    across a '\\n' separator). One normalization: a body ending in
    a template placeholder close + '\\n' ("}}\\n") trims the
    newline — the separator the next reference proves.
  * A carve that intersects an extracted file's span is not bare
    and is skipped; a start claimed by two agents is a problem,
    never a silent pick.
"""
import re
import tomllib
from collections import Counter

from .code_literals import end_is_boundary
from .prose_regions import prompt_score

MIN_PROMPT = 64
OPENER_RE = re.compile(
    r"^(You |The |This |Your |Generate |Classify |Judge |Determine |"
    r"Review |Check |Submit |Write |Create |Read |Given |Act |Decide |"
    r"Evaluate |Assess |Select |Always |When |If |For |A |An )")
WORD_RE = re.compile(r"[a-z]+")
ID_TAIL = re.compile(rb"[a-z0-9_]")


def parse_defs(defs):
    """defs: {aid: (offset, body)} from mechanism 6. Returns
    {aid: {"name": str, "tools": [str]}} (regex fallback when a
    body is not clean TOML)."""
    out = {}
    for aid, (_off, body) in defs.items():
        name, tools = aid, []
        try:
            doc = tomllib.loads(body.decode("utf-8"))
            name = doc.get("name", aid)
            tools = doc.get("tools", []) or []
        except Exception:
            m = re.search(rb'\nname = "([^"]+)"', body)
            if m:
                name = m.group(1).decode()
            tools = [t.decode() for t in
                     re.findall(rb'\n    "([a-z0-9_.]+)",?', body)]
        out[aid] = {"name": name, "tools": tools}
    return out


def _vocab(parsed):
    vocab = {}
    for aid, d in parsed.items():
        words = set(aid.split("_"))
        words.update(w for w in WORD_RE.findall(d["name"].lower()))
        vocab[aid] = words
    distinctive = {}
    counts = Counter()
    for words in vocab.values():
        counts.update(words)
    for aid, words in vocab.items():
        distinctive[aid] = {w for w in words if counts[w] == 1}
    return vocab, distinctive


def _prompt_shaped(body):
    if b"\x00" in body:
        return False
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError:
        return False
    if prompt_score(body) >= 1:
        return True
    if text.startswith("# "):
        return True
    if "{{" in text and OPENER_RE.match(text):
        return True
    return False


def bare_prompts(data, defs, extents, covered_spans, starts):
    """Carve attributed bare prompts. defs from mechanism 6,
    extents from mechanism 10, covered_spans = [(start, end)] of
    extracted files, starts = boundary oracle set.
    Returns (carved, duplicates, problems):
      carved: {aid: {offset, body, rule, support}}
      duplicates: {aid: [extra offsets with identical bytes]}
      problems: [str]"""
    parsed = parse_defs(defs)
    vocab, distinctive = _vocab(parsed)
    tool_count = Counter()
    for d in parsed.values():
        tool_count.update(d["tools"])
    unique_tool = {}
    for aid, d in parsed.items():
        for t in d["tools"]:
            if tool_count[t] == 1:
                unique_tool[t.encode()] = aid

    def covered(start, end):
        return any(a <= start < b or a < end <= b or
                   (start <= a and b <= end)
                   for a, b in covered_spans)

    # ---- candidate starts ------------------------------------------
    cand = {}   # start -> set of attribution hints

    def hint(start, h):
        cand.setdefault(start, set()).add(h)

    # (1) id-abut occurrences
    for aid, (doff, _body) in defs.items():
        needle = aid.encode()
        i = data.find(needle)
        while i != -1:
            if i != doff and not (i > 0 and ID_TAIL.match(data[i - 1:i])):
                hint(i + len(needle), ("id-abut", aid))
            i = data.find(needle, i + 1)
    # (2) unique-tool needle occurrences -> their containing extent
    starts_sorted = sorted(extents)
    import bisect
    for needle, aid in unique_tool.items():
        i = data.find(needle)
        while i != -1:
            k = bisect.bisect_right(starts_sorted, i) - 1
            if k >= 0:
                hint(starts_sorted[k], ("unique-tool", aid))
            i = data.find(needle, i + 1)
    # (3)+(4) heading / opener extent starts
    for start in starts_sorted:
        head = bytes(data[start:start + 400])
        if head.startswith(b"# ") or OPENER_RE.match(
                head.decode("utf-8", "replace")):
            hint(start, ("shape", None))

    # ---- carve ------------------------------------------------------
    carved = {}
    problems = []
    claimed = {}
    for start in sorted(cand):
        lens = extents.get(start)
        if not lens:
            continue
        hints = cand[start]
        for length in sorted(lens):
            end = start + length
            body = bytes(data[start:end])
            if body.endswith(b"}}\n"):
                body = body[:-1]
                end -= 1
            if len(body) < MIN_PROMPT or covered(start, end):
                continue
            if not end_is_boundary(end, starts, len(data)):
                continue
            if not _prompt_shaped(body):
                continue
            # attribution ladder
            aid = None
            rule = None
            for kind, who in hints:
                if kind == "id-abut":
                    aid, rule = who, "id-abut"
                    break
            if aid is None:
                owners = {who for kind, who in hints
                          if kind == "unique-tool"}
                # the needle must be inside THIS extent, not a
                # longer neighbour sharing the start
                owners = {w for w in owners
                          if any(data.find(t, start, end) != -1
                                 for t, a in unique_tool.items()
                                 if a == w)}
                if len(owners) == 1:
                    aid, rule = owners.pop(), "unique-tool needle"
            if aid is None and body.startswith(b"# "):
                head_line = body.split(b"\n", 1)[0].decode(
                    "utf-8", "replace").lower()
                hw = set(WORD_RE.findall(head_line))
                scores = {}
                for a, words in vocab.items():
                    s = len(hw & words) + 2 * len(hw & distinctive[a])
                    if s:
                        scores[a] = s
                if scores:
                    best = max(scores.values())
                    tops = [a for a, s in scores.items() if s == best]
                    if len(tops) == 1 and best >= 2:
                        aid, rule = tops[0], "heading vocabulary"
            if aid is None:
                owners = set()
                for a, words in distinctive.items():
                    if any(w.encode() in body for w in words):
                        owners.add(a)
                if len(owners) == 1 and OPENER_RE.match(
                        body.decode("utf-8", "replace")):
                    aid, rule = owners.pop(), "distinctive word + opener"
            if aid is None:
                continue
            if aid in carved:
                problems.append(
                    f"bare-prompt {aid}: second attributed extent at "
                    f"{start} (first at {carved[aid]['offset']}) — "
                    "kept the first")
                continue
            if start in claimed:
                problems.append(
                    f"bare-prompt: extent at {start} claimed by both "
                    f"{claimed[start]} and {aid} — skipped")
                continue
            claimed[start] = aid
            carved[aid] = {"offset": start, "body": body, "rule": rule,
                           "support": lens[length]}
            break

    # ---- duplicate copies -------------------------------------------
    duplicates = {}
    for aid, c in carved.items():
        body = c["body"]
        offs = []
        i = data.find(body)
        while i != -1:
            if i != c["offset"]:
                offs.append(i)
            i = data.find(body, i + 1)
        if offs:
            duplicates[aid] = offs
    return carved, duplicates, problems
