### Goal

Use existing state or minimal, clearly identified test fixtures when needed, open the audit session with `web_artifacts.audit`, drive what you changed through the probe CLI, fix what `assessment.fix_before_attesting` names, and rebuild and re-audit once after the fix pass.

### Pre-Audit Seeding

- Use `artifact.list_actions` with the artifact slug to list actions; add an action name to inspect its request schema. Invoke the refresh/import/populate action a real user would rely on with `artifact.invoke_action`, using concrete inputs from the plan or sampled user data.
- Do not seed fake core content. {population_gap_exit}
- The test environment is isolated after the first `web_artifacts.build`: `artifact.invoke_action` and `web_artifacts.audit` use the builder's copy of `app.db`, not production data. Seed through actions, not by editing `app.db`; seeded test data is discarded after submit.
- If users should see fetched/generated data on first open, declare `post_submit_action` on the audit call and the submit call, make sure it is callable, and document it in the submit result. The action must fetch real data in production using the same logic as refresh. Don't use migrations or builder-side test writes as production seed data.

### Audit And Drive

Call `web_artifacts.audit` after the latest successful build and read its `assessment`: `scope`, `fix_before_attesting`, `advisory`, `next`. The response's `guidance` has the probe mechanics. For a creation, drive each kind of control or flow once and read the two fold screenshots once. For an edit, drive what the edit changed and look at every view, state, or output the request names; one you have not seen is not verified, and an unrelated click verifies nothing. Prove effects, not presence: `--fill` a unique marker, or read a count before and after, and read the frame after an act that should have changed something. Sandbox rows may mix copied user records with fixtures; judge test outcomes against test inputs, and never claim production values or persistence from sandbox evidence. A successful sandbox action does not verify a pending `post_submit_action`. The content and security reviews in the response judge content, provenance, and data movement; do not repeat them.

Report `status` and `verification_status` as the Completion section of your system prompt says.
