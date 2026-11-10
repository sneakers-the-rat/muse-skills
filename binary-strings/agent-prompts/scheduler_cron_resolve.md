# Onboarding tour handoff

Every tour run hands its prepared copy to the main agent, which translates and delivers it. `muse.nothing_to_report` is unavailable for this run. Call `muse.notify_main_agent` with the complete prepared copy in `message`. If the copy is missing, call `muse.notify_main_agent` with `outcome: failed` and say why in `message`. Choose `outcome` as the contract above describes.
