TV target:
Design for a 960×540 screen read from across the room. It never scrolls: everything fits, so reflow, shrink, or cut rather than overflow. Keep content inside a 5% overscan margin. Dark by default. Input is a D-pad (arrows, Enter, and Escape for Back): every control is a real button or link, focus is large and obvious, the primary control starts focused, arrows move focus spatially, and Back closes the top overlay first. Nothing depends on hover, drag, or typing.

The host chooses the view; don't add a switcher.

The audit captures the TV view and flags scrolling, content in the overscan margin, and a missing starting focus; fix what it flags. To look yourself, run the probe's `viewport tv`.
