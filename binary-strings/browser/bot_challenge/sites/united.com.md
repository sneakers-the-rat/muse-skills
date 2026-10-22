## Bot detection

- United rarely shows a CAPTCHA, but its protection often acts silently: a
  submitted form resets to empty, or sign-in fails with “Something went wrong”.
- Treat a visible challenge or a silent reset as a bot challenge. Resubmitting
  the same form does not get past it; report it only after the bot-check agent
  could not.
