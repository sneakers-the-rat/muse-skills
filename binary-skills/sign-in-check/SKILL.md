# Sign-in check

The page asks you to sign in to prove you are human, or shows a limited view until you sign in. It reads like "Sign in to confirm you're not a bot", or like a notice that you are seeing a limited view, with links that open a sign-in prompt.

- Signing in is the caller's work, with the account its task names. Do not type into the sign-in form.
- When the page also offers a checkbox or a puzzle, solve that with its guide instead.
- Scroll a list in a limited view to load more, and assess it `clear` when what the caller needs is showing. The view comes from being signed out, so a reload or a move does not lift it.
- Otherwise report blocked in `browser.report` with reason `sign_in_required`, quoting the page's words. The caller signs in and carries on.
