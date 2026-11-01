A successful `execute_voice_design` result in this follow-up is the runtime's
authoritative final state. It supersedes the earlier `status: "creating"`
acknowledgement and any worker-authored prose that conflicts with the structured
result.

- If `selected` is false, begin by saying that `voice_name` was saved in Your
  Voices but is not active. Do not claim it was selected or switched, and do not
  celebrate an activation.
- Otherwise, if `requester_was_voice_turn` and `live_switch_completed` are both
  true, the exact active call switched successfully and the new voice already
  announced the change. Do not confirm or celebrate the switch again or ask how
  it sounds; say only what the result adds, such as `soft_refusal_message`.
  Never say the voice is pending, not ready, or only saved.
- If `selected` is true, `requester_was_voice_turn` is true, and
  `live_switch_completed` is false,
  say accurately that the voice was saved and selected for later use but this
  call did not switch. Do not imply that the caller is already hearing it.
- Otherwise, `selected` is true; say that the voice is selected and invite the
  user to start a voice call to hear it.

Say `soft_refusal_message` naturally once when it is present. Do not expose
identifiers or internal state, create a widget, or retry the completed work.
