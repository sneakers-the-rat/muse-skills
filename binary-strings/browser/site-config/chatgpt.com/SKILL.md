# ChatGPT instructions

## Conversations

- Check the active conversation before typing. “Search chats” searches
  conversation history; it is not the message composer.
- Wait for the response to finish before treating it as complete. A stopped or
  failed response may be partial.
- Keep the current conversation open when a login prompt appears. After signing
  in or clearing a check, inspect the page with `browser.observe` before sending
  the request again.

## Plans and checkout

- Subscription checkout is a payment flow. Choosing a payment tab such as
  PayPal, Google Pay or Apple Pay, or returning to the chat, does not prove an
  upgrade was charged.

## Signing in

- “Log in” and “Sign up for free” open a sign-in page offering “Continue with
  Google”, “Continue with Apple”, “Continue with phone”, or an “Email address”
  with “Continue”.
- A provider sign-in such as Apple returns through auth.openai.com, where the
  security check can also appear.

## Bot detection

- ChatGPT often shows Cloudflare's “Just a moment...” page, with a “Verify you
  are human” checkbox or a “Verifying...” widget that names Cloudflare. It can
  appear on the homepage, inside a conversation and during sign-in.
- Treat it as a bot challenge. A checkbox that comes back unchecked after
  verifying means that attempt did not count, not that the check cannot be
  passed.
