# Waiting room

The site admits visitors from a queue in order. Pages say things like "You are now in line", "Your estimated wait time is 5 minutes" or "Thank you for your patience. You will be redirected shortly".

- Assess it as `managed`, with any estimated wait in `retry_after`.
- Never reload, go back or open the site in another tab. Leaving or refreshing can lose your place in the queue.
- When the estimated wait is a few minutes or less, wait for the page to move on with `wait` actions, and assess the page it reaches.
- When the wait is longer, report it in `browser.report` with the position and the estimated wait the page shows. Leave the tab where it is, so the caller keeps the place.
