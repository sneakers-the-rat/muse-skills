# Soft block

The page loads but withholds what a person would see, often right after a check. It shows up as a blank page, a results list that is suddenly empty, a page stripped of prices or details, a spinner that never stops, buttons that do nothing or a redirect that keeps looping.

- Rule out ordinary causes first: wait for slow content with a `wait` action, scroll, and close any banner that covers the page.
- Compare the page with what a person would expect, such as results for a common search or a price on a product page. A check that keeps coming back after it cleared belongs here too.
- Content the view says was withheld for protection is still on the page. That is not a soft block.
- Assess it as `bot_wall` when the page offers nothing a person could use, and say in `evidence` what is missing.
- Reload the page with `bot_challenge.recover` once. When the page still lacks what it should show after a wait and a reload, this browser or its network is rejected. Request `replace_environment` with `bot_challenge.recover`.
- When the moved tab still lacks it, report what the page withholds in `browser.report`. The caller can reach the content by another route on the site.
