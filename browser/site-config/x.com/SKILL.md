# X instructions

## Page setup

- Close a covering dialog or cookie banner before using the page behind it.
  The banner offers to refuse non-essential cookies; prefer that option.

## Reading posts

- “Next media” advances through a post's media, not through search results.

## Posting

- The composer's “Add post” adds another post to a thread; it is not the final
  publish control. Check the thread, audience and attachments before posting.

## Signing in

- Sign-in can start with “Email or username”, then “Next” or “Continue”.
  “Continue with phone”, Google (which opens a new tab) and Apple are separate
  methods.
- The dialog replaces its fields between steps. Observe again with
  `browser.observe` after each step and after a stale or non-actionable field;
  never type into the old one.
- “We’ve temporarily limited your login. Please try again later.” under the
  username field is a rate limit. Stop signing in and report it in
  `browser.report`.

## Bot detection

- X occasionally shows a bot check. Treat any challenge page as a bot challenge.
- The login rate limit above is not a challenge to solve; the site asks you to
  try again later.
