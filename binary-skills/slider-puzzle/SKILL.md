# Slider puzzle

A slider asks you to drag a puzzle piece or image along a track until it fits a gap. Pages say things like "Slide right to complete the puzzle", "Drag the puzzle piece into place" or "Please slide to verify".

- When the widget offers an audio challenge behind a headphones or Audio button, use it with the audio challenge guide before you drag.
- Find three things in the screenshot: the handle on the track, the moving piece and the gap it must fill.
- The handle and the piece move by the same distance. Drag the handle as far as the gap sits from the piece, not to the end of the track.
- Press the handle with `mouse_down`, described in `look` with the widget's reference in `within`, and move it with `mouse_move` to the point on the track that distance away.
- Read the view after each move: it shows the piece against the gap. Nudge the handle with `mouse_move` by `dx` until the piece fills the gap, then let go with `mouse_up`. The release submits the answer on most sliders, so let go only once the piece lines up.
- When the browser cannot keep the button down, with `pointer_hold_unsupported`, make the whole distance one `drag` from the handle to that point, in `from_look` and `to_look` with the widget's reference in `from_within` and `to_within`. A test drag or a second, corrective drag counts as a new attempt.
- A rejected slide loads a new image. Measure the new gap afresh; the old distance no longer applies.
- A track with no gap, such as "Slide to verify", needs the handle dragged to the end in one motion.
- When the handle is back at the start after a drag and the widget shows no message and no new puzzle, the widget did not take the drag. Reload the page with `bot_challenge.recover`, wait for the slider to load, and drag once more.
- When a fresh slider also ignores the drag, or the handle reaches the end and the slider resets twice in a row, request `replace_environment` with `bot_challenge.recover`. When the moved tab's slider ignores or resets the drag the same way, report it with `browser.report`.
- When the slide passes and the page then restricts access for your network, the network is rejected. Request `replace_environment` with `bot_challenge.recover`.
