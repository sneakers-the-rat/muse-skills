"""Mechanism 7 — prose-region segmentation: segment a string
section into maximal runs of text bytes (the fused constant pools
that no (ptr, len) reference delimits), and record each region's
prose features and prompt-likeness score.

This is the segmentation layer, not ground truth: spans defined by
references (mechanisms 9-13) outrank regions, and the byte
accounting reports region coverage separately. The segmentation
rule, feature set and scoring markers are the prompt census's
(scan_prose.py / triage_prose.py), generalized from the census's
hardcoded section geometry to any (offset, size) span.
"""
import re

MIN_REGION = 160
TEXT_RUN = re.compile(rb"[^\x00-\x08\x0b\x0c\x0e-\x1f\x7f]{%d,}" % MIN_REGION)
PATH_TOKEN = re.compile(rb"[\w./\-]{3,}\.(?:md|toml|yaml|yml|json)")
LOWER = [bytes([c]) for c in range(97, 123)]

MARKERS = [
    (rb"You are ", 4), (rb"Your task", 4), (rb"You must", 3),
    (rb"You should", 2), (rb"Do not ", 2), (rb"\bYou\b", 0),
    (rb"## ", 2), (rb"### ", 2), (rb"When you", 2), (rb"Always ", 1),
    (rb"Never ", 1), (rb"system prompt", 3), (rb"sub-?agent", 2),
]
ANTI = [
    (rb"SELECT ", -3), (rb"INSERT INTO", -3), (rb"function ", -1),
    (rb"\\u00", -2), (rb"{\"", -1), (rb"charset", -2), (rb"tzdata", -3),
]


def features(blob: bytes):
    try:
        blob.decode("utf-8")
        decodable = True
    except UnicodeDecodeError:
        decodable = False
    n = max(len(blob), 1)
    return {
        "utf8_clean": decodable,
        "newlines": blob.count(b"\n"),
        "blank_lines": blob.count(b"\n\n"),
        "md_headings": blob.count(b"\n#") + (1 if blob.startswith(b"#") else 0),
        "md_bullets": blob.count(b"\n- ") + blob.count(b"\n* "),
        "spaces_ratio": round(blob.count(b" ") / n, 3),
        "lower_ratio": round(sum(blob.count(c) for c in LOWER) / n, 3),
        "question_marks": blob.count(b"?"),
        "path_tokens": [m.group(0).decode("utf-8", "replace")
                        for m in PATH_TOKEN.finditer(blob)][:20],
    }


def prompt_score(blob: bytes) -> int:
    s = 0
    for pat, w in MARKERS:
        s += w * len(re.findall(pat, blob))
    for pat, w in ANTI:
        s += w * len(re.findall(pat, blob))
    return s


def prose_regions(data, start, end):
    """All prose regions >= MIN_REGION in data[start:end].
    Returns [{offset, end, body, features, prompt_score}]."""
    region = bytes(data[start:end])
    out = []
    for m in TEXT_RUN.finditer(region):
        blob = m.group(0)
        out.append({
            "offset": start + m.start(),
            "end": start + m.end(),
            "body": blob,
            "features": features(blob),
            "prompt_score": prompt_score(blob),
        })
    return out
