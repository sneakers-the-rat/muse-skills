# Image grid

A grid of tiles asks you to pick every tile that matches a rule, often over several rounds. Pages say things like "Select all images with traffic lights", "Select all squares with motorcycles. If there are none, click skip" or "Please click each image containing a bird".

- When the widget offers an accessible text or audio challenge behind a headphones or accessibility button, prefer it, and follow the audio challenge guide for audio.
- Read the instruction in every round. It can name a category, a relation to an example picture or the tiles that do not match, and it changes between rounds.
- Judge each tile from the current screenshot, and follow the instruction's rule for an object that crosses tile borders.
- Name every matching tile by its row and column in one click, such as "the top-left and bottom-middle tiles", with the widget's reference in `within`.
- When a click on a tile's reference comes back `page_busy` or `page_unresponsive`, observe the grid with `browser.observe` to see which tiles it took, then pick that grid's tiles by `look`.
- When a picked tile fades and a new one appears, wait for it and judge the new tile too, until no match is left.
- On a grid that keeps its tiles, check which tiles show as selected before you press Verify.
- Rounds can run on a timer, and a slow round expires or closes the widget. When one expires before you submit, make the next round's picks and press Confirm or Verify by its reference in the same call.
- Next brings another round. Skip only when the widget allows it and nothing matches.
- A Verify button you cannot see yet does not stop you from making the current selection.
- "Please try again" or "Please select all matching images" means a tile was missed or picked wrongly. The next round is new, so judge it afresh.
- When a round is too hard to read, the widget's reload control gives a new one.
- When the widget offers to verify on a phone or with a QR code, look for another option in the widget first.
