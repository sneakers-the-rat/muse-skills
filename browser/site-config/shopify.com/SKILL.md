# Shopify instructions

## Telling the surfaces apart

- Merchant checkout, Shopify account sign-in (accounts.shopify.com) and the
  store admin (admin.shopify.com/store/…) have different controls and
  completion states. Identify which one you are on before acting.
- Shopify Inbox runs at inbox.shopify.com/store/…, with separate views for
  open, unread, unassigned, blocked and closed conversations.

## Store admin

- The admin's global search (“Search”, Ctrl K) and the theme editor's “Search
  blocks” have different scopes. Select the intended store before changing
  anything.
- In the theme editor, “Add section” and “Add block” insert content, and each
  item's “Re-arrange … order within the list” control moves it.
- “Save”, “Save as” and “Cancel and discard all changes” are distinct. After
  saving, inspect the resulting state with `browser.observe`; never replay an
  uncertain save.
- A redirect loop (ERR_TOO_MANY_REDIRECTS) is an access failure, not evidence
  that a cart or edit was saved. Keep the original checkout or editor context
  for recovery.

## Signing in

- Admin sign-in runs on accounts.shopify.com. A one-time code, when Shopify
  asks for one, goes in a single field.

## Bot detection

- Shopify admin pages frequently stop at “Just a moment...”, a page that says
  “Your connection needs to be verified before you can proceed”. The admin page
  behind it has not loaded.
- Treat it as a bot challenge. Do not reload in a loop.
