The active client currently declares these parameter-free navigation commands:

{ui_control_commands}

Call `ui_control` exactly once with `action` set to `navigate` and the declared target matching the view the user asked to open. Do not include `params` or `mode`. If no declared target matches, end without a tool call.
