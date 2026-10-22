# Snapchat instructions

## Snapchat for Web

- Chats, stories and the friends feed live in Snapchat for Web at `/web/`.
  Public profile pages can show “Log in” while the web app is signed in, so
  check sign-in state in `/web/`.
- A “Camera blocked” notice in the main area asks for camera and microphone
  access. It does not stop you from reading chats.
- Select the intended conversation before composing. A “Delivered” label on an
  earlier message does not verify a new send.

## Public posts

- In a public upload, check the video preview and “Add a description and
  #topics”. “Save to a Public Profile” changes where the Snap appears.
- “Continue posting” returns to a pending post; it is not evidence of
  publication. Check the resulting post state.

## Signing in

- Sign-in starts with “Username or email address” (some layouts: “Username or
  Email”) and “Log in”; the password follows on the next page, so observe it
  with `browser.observe` before filling. “Use phone number instead” switches to
  a phone form.
- “Sign in with a passkey” and “Continue with Google”, which opens a new tab,
  are separate methods. Observe the new form with `browser.observe` after
  choosing one.

## Bot detection

- Snapchat occasionally shows a verification page. Treat it as a bot challenge.
