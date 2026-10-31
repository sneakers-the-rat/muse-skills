"""Path policy for extracted files: which embedded paths are
bundle files, and where each lands in the archive tree.

# Ported verbatim from scripts/extract_binary_files.py in the
# 2026-10-31 package restructure; see hatch_extract.mechanisms.
"""
import re

PATHCH = set(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_./-")
EXTS = (".md", ".yaml", ".yml", ".json", ".toml")

KNOWN_ROOTS = {"blocks", "browser", "session", "self_improvement",
               "templates", "tools", "artifacts", "channels", "devices",
               "connections", "memory", "notes", "voice", "docs",
               "references", "assets", "chat-connections", "dreams",
               "orders", "selection", "shopping", "studying", "config",
               "src", "user", "update", "chat", "activity_monitor"}
SLUGS = {"arithmetic-and-counting", "audio-challenge", "automatic-check",
         "block-page", "game-puzzle", "icon-order", "image-click",
         "image-grid", "network-block", "page-load-failure", "path-drawing",
         "press-and-hold", "rotation-puzzle", "sign-in-check",
         "slider-puzzle", "soft-block", "start-gate", "text-captcha",
         "verification-checkbox", "waiting-room"}
DOMAIN = re.compile(r"^[a-z0-9\-]+(\.[a-z0-9\-]+)+$")
SKILL_ROOTS = {"session", "chat", "devices", "voice", "activity_monitor",
               "channels", "chat-connections", "shopping"}
SKIP_ROOTS = {"memory", "config", "notes", "orders", "user", "dreams",
              "selection", "update", "studying"}
MAX_FILE = 1_000_000
CLUSTER_GAP = 0x20000
MIN_CLUSTER_FILES = 20


def clean_path(raw):
    if "/" not in raw:
        return None  # bare filenames are mentions, not bundle files
    parts = raw.split("/")
    # a final component carrying two extensions is two fused names
    # ('a.mdvoice_chat_delegate.md'); the stored entry is the first name
    last = parts[-1]
    for ext in EXTS:
        i = last.find(ext)
        if i != -1 and any(e in last[i + len(ext):] for e in EXTS):
            parts[-1] = last[:i + len(ext)]
            raw = "/".join(parts)
            break
    if parts[0] in KNOWN_ROOTS or parts[0] in SLUGS:
        return raw
    if DOMAIN.match(parts[0]) and len(parts) == 2 and \
            parts[1] in ("SKILL.md", "config.yaml"):
        return raw
    # fused prefix ending in a known root as a suffix of the first
    # component ('are.session/x.md' -> 'session/x.md'): the root name is
    # the delimiter (the user's heuristic)
    for root in sorted(KNOWN_ROOTS, key=len, reverse=True):
        if parts[0].endswith(root) and len(parts[0]) > len(root):
            return "/".join([root] + parts[1:])
    for i in range(1, len(parts) - 1):
        if parts[i] in KNOWN_ROOTS:
            return "/".join(parts[i:])
    return None



def target_for(source):
    top, _, rest = source.partition("/")
    if top == "agent-definitions":
        return f"binary-strings/{source}"
    if top in ("agent-prompts", "prose-regions"):
        # mechanisms 8 and 7: synthetic sources for material that
        # carries no embedded path of its own
        return f"binary-strings/{source}"
    if top == "browser":
        return f"binary-strings/{source}"
    if top == "self_improvement":
        return f"binary-strings/{source}"
    if top == "blocks":
        return f"system_prompts/{rest}"
    if top == "templates":
        return f"binary-strings/artifacts/templates/{rest}"
    if top == "artifacts":
        return f"binary-strings/{source}"
    if top == "tools":
        return f"binary-strings/tools/{rest}"
    if top in SLUGS:
        return f"binary-skills/{source}"
    if DOMAIN.match(top) and source.count("/") == 1 and \
            rest in ("SKILL.md", "config.yaml"):
        return f"binary-strings/browser/site-config/{source}"
    if top in SKILL_ROOTS:
        return f"binary-skills/{source}"
    if top in SKIP_ROOTS:
        return None
    return f"binary-etc/{source}"



def split_token(tok):
    """Split a fused grep token into sub-paths. A split point is an
    extension end immediately followed by a plausible next path start
    (known root, guide slug, or domain component, each followed by '/').
    Returns [(local_start, subpath, is_last)]."""
    out = []
    pos = 0
    while pos < len(tok):
        # earliest extension end at or after pos
        end = None
        for ext in EXTS:
            i = tok.find(ext, pos)
            if i != -1 and (end is None or i + len(ext) < end[0]):
                end = (i + len(ext), ext)
        if end is None:
            out.append((pos, tok[pos:], True))
            break
        e = end[0]
        rest = tok[e:]
        nxt = None
        if rest:
            head = rest.split("/", 1)[0]
            if "/" in rest and (head in KNOWN_ROOTS or head in SLUGS
                                or DOMAIN.match(head)):
                nxt = e
        if nxt is None:
            out.append((pos, tok[pos:], True))
            break
        out.append((pos, tok[pos:e], False))
        pos = e
    return out

