 (in hatch-agent).
#
# Fields:
#   id      monotonically increasing, starts at 1
#   notify  what live sessions are told when they reach this version:
#             "none"      no-op; no live delivery, watermark still advances
#             "notice"    passive developer message before the user's next turn
#             "act"       inject a developer message and let the agent act now
#             "recompact" force compaction so the change lands in working memory
#   hash    optional sha256 of the prompt source set for prompt-adjacent audit
#           entries. Runtime delivery is keyed by id/watermark, not by hash.
#           Omit for re-announcements / deploy notices that don't need a source
#           snapshot.
#   kind    "system-update" (default) for deploy / re-announcement notices; use
#           "prompt-update" for prompt/guidance corrections, or "incident-fix".
#           Renders a [{kind}] sentinel; mixed pending kinds render [update].
#   note    short human summary of what changed (for the audit log)
#   message (optional) developer-authored text delivered to the agent when
#           notify != "none"; omit to fall back to an auto change-pointer

[[version]]
id = 1
hash = "3eecec096646a77f40a54e5ff4100c39790995bf8ed523d4c86321ce8e8a10ed"
notify = "none"
note = "Baseline snapshot of the system-prompt sources at feature introduction."

[[version]]
id = 2
hash = "2fabf41acfa157f6bd4df6102c47a915884cd9520ae0804e2b8a6a5082fe95ce"
notify = "notice"
note = "Spaces -> web artifacts rename: refreshed the artifact wording in the system prompt, shipping alongside the create_web_artifact / modify_web_artifact / artifact_action tool renames in the same deploy."
message = "What used to be called Spaces are now web artifacts, built and updated with `create_web_artifact`, `modify_web_artifact`, and `artifact_action`. Use these names and this terminology going forward."

[[version]]
id = 3
hash = "0a75f3a3543a69c574921484a4be10e6a85958532ba8faca73424aacf6bc9ec1"
notify = "notice"
note = "Removed the Credits and Subscription account-status block from the system prompt."
message = "The system prompt no longer includes account-status context for subscription tier, plan pricing, credit quota, or reset timing. Do not rely on prompt-provided account-status details."

[[version]]
id = 4
hash = "365a32b71ba164a9078b8511dadb54e3a3ed8eb182de6464f361d0f454e3c0b3"
notify = "none"
note = "Removed explicit CAPTCHA solve/handoff guidance from the BrowserTask system prompt."

[[version]]
id = 5
notify = "notice"
note = "Re-announce id=2 (Spaces -> web artifacts) and id=3 (account-status removed). At dev-notice feature introduction every existing VM's fresh watermark seeded to the then-latest id, marking the launch-window notices already-seen, so id=2 reached no VMs and id=3 only some. This hash-less re-announcement reaches every session at watermark <= 4 exactly once; the message re-states both updates because a VM already past id=3 receives only this entry. Kind defaults to system-update."
message = "Two recent platform updates, in case earlier context missed them: (1) What used to be called Spaces are now web artifacts — build and update them with `create_web_artifact`, `modify_web_artifact`, and `artifact_action`, and use that terminology going forward. (2) The system prompt no longer includes account-status context (subscription tier, plan pricing, credit quota, or reset timing) — do not rely on prompt-provided account-status details."

[[version]]
id = 6
hash = "a1eb982e6b201c2e5abc51b041ae151e274a5f5d19523dbb39bdd76cd60e517f"
kind = "prompt-update"
notify = "notice"
note = "BrowserTask prompt now names visual browser automation as a fallback for freeform cursor movement."
message = "BrowserTask agents now have `default.visual_automation`, a by-sight fallback for click, drag, or hover gestures when `default.automation` has no element to target."

[[version]]
id = 7
kind = "system-update"
notify = "notice"
note = "Announce the Ideas shared-surface rename to live sessions."
message = "The shared Ideas community surface is now called Discovery Pool; older context may use a prior name for the same feature, so use the current name and do not repeat the prior one. This is a terminology note only: it does not change your current task, tool, or output schema, so continue the active work and make your required terminal tool call, such as submit_step_output, exactly as you otherwise would."

[[version]]
id = 8
kind = "system-update"
notify = "none"
note = "Audit correction: preserve id=4 as the historical CAPTCHA-guidance removal record; the current BrowserTask prompt again includes explicit bot-challenge/CAPTCHA handoff guidance."

[[version]]
id = 9
kind = "prompt-update"
hash = "96e541b68cfee73dc14a17f56e0f0d69c989a1247d843a2e24ae404e51b7dc3f"
notify = "none"
note = "Added the Ideas builder subagent system prompt, final handoff contract, and concise artifact guidance."

[[version]]
id = 10
kind = "system-update"
notify = "notice"
note = "Ideas subsystem hard-cut of the legacy `space` vocabulary. The item `kind` formerly emitted as `space` is now `artifact` (add_item schema + 