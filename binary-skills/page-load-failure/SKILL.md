# Page load failure

The browser shows its own error page instead of the site, or the tab's navigation never finishes. Error pages say things like "This site can't be reached", "The connection was reset", "took too long to respond", "This site can't provide a secure connection" or "This page isn't working", often with a code such as ERR_CONNECTION_CLOSED, ERR_HTTP2_PROTOCOL_ERROR or HTTP ERROR 502.

- Report the browser's own page saying the site is blocked, such as "Your organization doesn't allow you to view this site" with ERR_BLOCKED_BY_ADMINISTRATOR or "This page has been blocked" with ERR_BLOCKED_BY_CLIENT, blocked at once in `browser.report` with reason `site_unreachable`, quoting the page. It comes from this browser's own policy, and no reload or move changes it.
- HTTP ERROR 403 on the browser's own error page is the site refusing this browser, not a failed load. That makes it a block page, with its own guide.
- For any other error page, assess it as `environment_error`, and copy the page's words and its error code into `evidence`.
- Reload the page with `bot_challenge.recover`. A reload often fixes a page that failed to load.
- When the same error comes back after the reload, report it blocked in `browser.report` with the error code, with reason `site_error` for an HTTP error from the site and `site_unreachable` otherwise.
- Read the tab again with `browser.observe` when every read says `browser_navigation_pending`, and assess the view once one comes back. The browser is holding a navigation to a sensitive site until the user allows it, and the tab has no view to assess or act on until then.
- While the reads stay pending, report blocked in `browser.report` with reason `site_unreachable`, saying the navigation to the site waits for the user to allow it, which is not a bot check. A move or a new tab to the same site meets the same hold.
