### Goal

The audit of the current build names something to do before a SUCCEEDED attestation. Do that, then call `web_artifacts.exit_build`: it rebuilds and re-audits a changed artifact.

### What To Do

Read `assessment`: `scope`, `fix_before_attesting`, `advisory`, `next`. Fix every `fix_before_attesting` item in one pass. When `next` asks you to drive the page, use the probe session the response opened (its `guidance` has the mechanics): for a creation, drive each kind of control or flow once; for an edit, drive what the edit changed and look at every view the request names. Prove effects, not presence: `--fill` a unique marker, or read a count before and after, and read the frame after an act that should have changed something. Sandbox rows may mix copied user records with fixtures; judge test outcomes against test inputs, and never claim production values or persistence from sandbox evidence. The content and security reviews in the response judge content, provenance, and data movement; do not repeat them.

When a user-entry artifact needs rows to exercise interactions, create unique test-only rows with `artifact.invoke_action`; the builder's copy of `app.db` is isolated, and seeded test data is discarded after submit. Do not seed fake core content. {population_gap_exit} If users should see fetched data on first open, declare `post_submit_action` on the submit; it must fetch real data in production with the same logic as refresh.

Report `status` and `verification_status` as the Completion section of your system prompt says.
