# Verification checkbox

One checkbox or button verifies the visitor, sometimes followed by a puzzle. It reads like "Verify you are human", "I'm not a robot" or "I am human".

- Click the checkbox once by its reference, then wait with one `wait` action for success, a puzzle or an error. Clicking again during "Verifying…" restarts the check.
- A puzzle that opens after the click has its own guide. Assess it again with `bot_challenge.assess` and read that guide with `bot_challenge.guide`.
- Success shows a check mark or "Success!", and many pages then move on by themselves. Wait for that before reporting.
- A verified checkbox can expire after about two minutes. Return promptly once verified, and click again when the widget says verification expired.
- A widget that shows "Verifying…" and then a fresh checkbox, or a failure message such as "Verification failed", did not accept the attempt. Try again with the same click after a short wait, or reload the page with `bot_challenge.recover` when the failed widget offers nothing to click. A hover, a key press or a hold in place of the click does not change the result.
- When it resets or fails twice in a row, request `replace_environment` with `bot_challenge.recover`. When the moved tab resets the same way, report it with `browser.report`.
- An invalid sitekey or unauthorized domain message is the site's own fault, and no answer or network fixes it. Report it.
