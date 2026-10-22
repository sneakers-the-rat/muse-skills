# OpenAI instructions

## Finding the right place

- Tell the public site (openai.com), account sign-in (auth.openai.com) and a
  product workspace apart, and choose the requested workspace and product.
- API billing and ChatGPT subscriptions are separate purchases with different
  confirmation states.

## Signing in

- “Email address” and “Continue” lead to “Enter your password” or a
  verification step. Read the new page instead of reusing the previous field;
  “Edit email” goes back.
- Google, Apple, Microsoft and “Continue with phone” are separate methods. An
  account picker (`/choose-an-account`) can appear before the password.

## Bot detection

- Checks are frequent, on sign-in and on openai.com pages such as Careers. The
  page is titled “Just a moment...” and shows “Performing security
  verification” with a Cloudflare “Verify you are human” checkbox, or
  “Verifying...” while the check runs.
- Treat it as a bot challenge. The form behind it is unusable until it clears;
  do not reload while it is verifying.
