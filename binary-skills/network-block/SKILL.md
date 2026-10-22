# Network block

The page blames your network address, or unusual or automated traffic from your network. Pages say things like "Our systems have detected unusual traffic from your computer network", "Your IP address has been blocked" or "Access from your network is restricted".

- Assess it as `ip_blocked` and quote the page's words in `evidence`.
- When the page also offers a checkbox or a puzzle, solve it first with that challenge's guide. That is often enough.
- No answer, wait or reload changes the network. When the page offers nothing to solve, or solving it does not let you through, request `replace_environment` with `bot_challenge.recover`.
- After the move, assess the page again. When the new network is blocked the same way, report it in `browser.report`; a tab moves only once.
