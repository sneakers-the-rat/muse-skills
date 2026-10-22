# Block page

The site refuses the request and offers nothing to interact with, often with a reference number. Pages say things like "Access denied", "Request blocked", "Sorry, you have been blocked", "You don't have permission to access this page" or "This is taking longer than usual. Please refresh the page to try again".

- Look over the whole page first, and scroll if it continues. A checkbox, a puzzle or a button that starts a check anywhere on it makes it a challenge with its own guide.
- Assess it as `bot_wall`, and copy the page's words and its reference number into `evidence`.
- Wait a little, then reload the page with `bot_challenge.recover`. A block page often clears on the next request.
- Treat the page's own Refresh or Try again button as that reload, not as a challenge. A page that comes back the same, often with a new reference number, is still this block page.
- When the page still offers nothing to interact with after a wait and a reload, the network or this browser is rejected. Request `replace_environment` with `bot_challenge.recover`.
- When the moved tab meets the same block, report it in `browser.report` with every reference number you saw. The caller can still reach the site another way, such as from its home page.
- The word blocked in the address or a security service's logo does not establish the cause. Go by what the page says.
- An error on a form submission, such as "temporary system issue", is the site's own answer and not a block page, even when it repeats. So is an error that names a field or a rule.
