# Affirm instructions

## Page setup

- **Cookies.** Answer the cookie banner with “Reject all” or “Accept all”;
  “Manage cookies” opens the detailed settings.
- **Promotions.** Close the “Add the free Chrome extension” panel before
  reading the page behind it.

## Paying a loan

1. Open the loan under “Current loans” and choose “Make a payment”.
2. Pick the amount the task names, such as “Overdue payment” or “Overdue &
   upcoming payment”, then check “Payment date” and “Payment method”.
3. The final button states the amount (“Pay …”). Pressing it is the payment
   itself.

- Affirm's own account pages are not a merchant's checkout.
- Move between account pages with on-page links. Loading an account URL
  directly can end the session.
- “Turn on AutoPay” and “Set up AutoPay” create a standing authorization.
  Leave them alone unless the task asks for AutoPay.

## Financing offers

- At a merchant checkout, “Continue” can advance to verification or to
  financing terms. Read the resulting page before choosing a plan.
- Keep the amount due today, payment schedule, interest and total repayment
  separate. A financing offer is not a completed payment, and it never
  replaces the payment method the task asked for.

## Signing in

- Sign-in starts with “Mobile number” and “Continue”; Affirm then texts a
  verification code. “New number? Update your account.” is for a changed phone
  number, not another account.
- “Log in with passkey” needs the user's device. Prefer the texted code; treat
  the passkey as a step for the user only when the site offers no other method,
  and never open account recovery to get around it.

### Verification codes

- The code field submits on its own once the last digit is in. Observe the page
  with `browser.observe` after entering the code rather than pressing “Continue”
  again.
- Use “Didn't get a code?” only when no code arrived.

## Bot detection

- Affirm's sign-in sometimes fails for automated browsers with an error page:
  “This page isn't loading right now” and “We can't reach this page”, with a
  “Go back” button. It is not a puzzle and says nothing about the account.
- Treat it as a bot challenge. Do not reload the sign-in page in a loop.
