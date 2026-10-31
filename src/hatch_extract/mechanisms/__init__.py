"""The mechanism registry: every extraction mechanism in the
package, in number order. The pipeline walks this registry for
its report; each mechanism lives in its own module.

Mechanisms 1-6 recover embedded FILES (path-bearing material).
Mechanism 7 segments the fused pools no reference delimits.
Mechanism 8 carves attributed bare prompts from code-referenced
extents. Mechanisms 9-13 are the string-reference census: every
way this Rust binary refers to a string, enumerated completely —
their spans feed the byte accounting that says what is left.
"""

REGISTRY = [
    {"number": 1, "name": "tables", "module": "tables",
     "blurb": "(path, data) fat-pointer tables in the relocation data"},
    {"number": 2, "name": "slices", "module": "slices",
     "blurb": "content slices: a slice target's length is authoritative"},
    {"number": 3, "name": "struct descriptors", "module": "struct_descriptors",
     "blurb": "constructor descriptors, struct-store variant"},
    {"number": 4, "name": "register descriptors",
     "module": "register_descriptors",
     "blurb": "constructor descriptors, register variant + general/matcher recovery"},
    {"number": 5, "name": "heuristic", "module": "heuristic",
     "blurb": "heuristic string-splitting of unseparated bundle text"},
    {"number": 6, "name": "agent definitions", "module": "agent_definitions",
     "blurb": "the sub-agent registry: anchored TOML documents"},
    {"number": 7, "name": "prose regions", "module": "prose_regions",
     "blurb": "prose-region segmentation of the fused constant pools"},
    {"number": 8, "name": "bare prompts", "module": "bare_prompts",
     "blurb": "bare-string prompt carving + needle attribution"},
    {"number": 9, "name": "static fat-pointers", "module": "static_refs",
     "blurb": "reference form (b): (ptr, len) pairs stored in data sections"},
    {"number": 10, "name": "code literals", "module": "code_literals",
     "blurb": "reference form (c): lea + immediate-length literals in code"},
    {"number": 11, "name": "panic locations", "module": "panic_locations",
     "blurb": "reference form (d): panic Location {file, line, col} records"},
    {"number": 12, "name": "NUL-terminated strings", "module": "nul_strings",
     "blurb": "reference form (e): terminator-delimited C strings"},
    {"number": 13, "name": "length-prefixed strings",
     "module": "length_prefixed",
     "blurb": "reference form (f): u32/u64 length immediately before the bytes"},
]
