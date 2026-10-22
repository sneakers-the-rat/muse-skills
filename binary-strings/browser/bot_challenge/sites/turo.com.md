## Bot detection

Turo frequently blocks automated browsing, in two forms.

- **Verification page.** “Performing security verification” with a Cloudflare
  “Verify you are human” checkbox. It is interactive.
- **Block page.** “Sorry, you've been blocked” with a Cloudflare Ray ID. It is
  a bot wall with nothing to click.

Treat both as a bot challenge. Neither says anything
about a car's availability; do not reload in a loop.
