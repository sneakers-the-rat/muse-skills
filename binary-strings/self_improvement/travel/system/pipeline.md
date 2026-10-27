## The System

A run, one execution from `window` through `gate`, updates one user-editable
file: `~/memory/travel/PROFILE.md`.

1. `window` checks whether new user-visible conversation exists.
2. `evidence_branch` skips directly to `gate` only when that check
   successfully finds no new rows. Probe failures run the workflow.
3. `travel_context` loads a bounded copy of the current profile (the durable
   file as it existed at the start of the run), plus its content hash and
   section counts.
4. `profile` is the writer turn. It stages the candidate profile (the
   complete replacement after this run) and submits the complete entry list.
5. `verify_profile` checks file structure, the fixed headings, booking and
   identity details that match known patterns (long numbers, emails, phone
   numbers, amounts, dates, listed terms), and that staged bullets and
   submitted entries agree. It then asks the judge for two checks:
   - `evidence_grounded`: new and changed entries satisfy the Ground Rules.
   - `preservation`: valid current entries were not silently lost.
6. A failed check may trigger one writer repair using the exact reasons.
7. `apply_profile` stamps file-level frontmatter and promotes the verified
   candidate only if the durable file has not changed since it was read.
8. `gate` records the result.

The writer and judge are separate model turns with separate tools. They
communicate through step outputs, the staged file, and verification reasons.
Deterministic code owns branching, structural checks, frontmatter, and
promotion.
