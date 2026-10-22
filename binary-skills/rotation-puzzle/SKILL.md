# Rotation puzzle

A picture must be turned until it stands upright or matches a reference, with a slider, arrow buttons or a drag. Pages say things like "Drag the slider to make the image upright" or "Use the arrows to rotate the animal to face the direction of the hand".

- When the widget offers an audio challenge behind a headphones or Audio button, use it with the audio challenge guide before you turn the picture.
- Work out the goal from the instruction: upright as a person would see the object, or turned to match the reference, including the direction it faces.
- Estimate how far the picture is turned and which way before you move anything.
- With arrow buttons, click the arrow that turns it the right way, and check the picture in each view before the next click.
- With a slider or a drag, press it with `mouse_down` and move it with `mouse_move` in proportion to the turn the picture needs. Read the picture in each view and nudge it with a small `mouse_move` by `dx` or `dy` until it matches the goal, then let go with `mouse_up`. The release usually submits the answer; when it does not, compare the picture with the goal and correct it.
- When the browser cannot keep the button down, with `pointer_hold_unsupported`, make the move one `drag`. A test drag counts as an attempt.
- Submit only once it matches, with the widget's own button when it has one.
- Complete every round the counter shows.
