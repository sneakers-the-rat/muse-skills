# Path drawing

A path must be drawn through objects in order without crossing itself. Pages say things like "Connect the dots in order" or "Draw a line through the icons in the order shown".

- Work out the order from the instruction, such as numbers or a sequence of icons.
- Plan the whole route before you start, so no stretch crosses another or an obstacle.
- Draw the path as one stroke. Press the first object with `mouse_down`, move to each next object in order with a `mouse_move` each, and let go on the last one with `mouse_up`, describing each object in `look` with the widget's reference in `within`. Read the view between moves when you need to check the line.
- When the browser cannot keep the button down, with `pointer_hold_unsupported`, draw each stretch as a `drag` from one object to the next, describing both ends in `from_look` and `to_look` with the widget's reference in `from_within` and `to_within`.
- When the widget clears the line or says try again, start again from the first object, or load a new puzzle.
