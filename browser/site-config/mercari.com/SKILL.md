# Mercari instructions

## Signing in

- Sign-in on jp.mercari.com, login.jp.mercari.com and mercari-shops.com cannot
  be completed in this browser, and the user taking control of this browser
  does not help either. The user can finish it only on their own phone or
  computer.
- Searching and reading listings work without signing in. Buying, making an
  offer, liking, commenting, messaging a seller, listing an item and the
  account's own pages need a signed-in account.
- When a step needs sign-in, such as a “ログイン” button, a redirect to
  login.jp.mercari.com or a passkey prompt, stop at that step. Do not start
  sign-in, try a saved password or a one-time code, or create an account.
- Report it with `browser.report` as a user_control need: to continue, the user
  can do this step only in their own browser on their phone or computer,
  because control of this browser cannot complete it. Do not give a passkey or
  any other sign-in method as the reason, because the user's account may not
  use one.
- Give the exact HTTPS address of the listing or shop page that led to sign-in,
  never a login.jp.mercari.com address. Add the choices already made, such as
  the item, variant, quantity and price, and what is left to do.
- Say that signing in on the user's own browser does not sign this browser in,
  so this task cannot carry out that step after the user signs in.
- When the page already shows the user's account signed in, continue normally.
