# Press and hold

A button asks you to press and hold it until it fills. Pages say things like "Press & Hold to confirm you are a human" or "Press and hold the button".

- Hold the middle of the button with one `hold` action, described in `look` with the widget's reference in `within`. Do not click it.
- Set `duration_ms` to about 10000, and longer when the widget's fill or stated duration needs more. A hold that stops short fails, and the browser refuses a hold longer than 15000 ms.
- When the button needs longer than that, or a hold keeps falling short, press it with `mouse_down` instead, observe until it fills, and let go with `mouse_up`. The browser lets go by itself after two minutes.
- When the browser cannot keep the button down, with `pointer_hold_unsupported`, hold it once for 15000 ms if you have not yet, since a `drag` cannot hold it. When that falls short too, or the button needs longer, report in `browser.report` that this browser cannot hold the button that long.
- Read the next view. A check mark or the next page means it passed; the same button means it did not, because an accepted press is not an accepted verification.
- When the button says the challenge is completed and asks you to wait, wait for its dialog to disappear with a `wait` on the dialog's reference.
- When the hold completed but the page keeps an empty challenge box or does not move on, reload the page with `bot_challenge.recover`.
- When the button resets, the hold was too short, lost focus or was not accepted. Hold again for longer.
- When it resets after a long hold twice in a row, this browser or its network is rejected. Request `replace_environment` with `bot_challenge.recover`. When the moved tab resets the same way, report it with `browser.report`.
- A passed hold can lead to a second check or a puzzle. Assess it again with `bot_challenge.assess`.
