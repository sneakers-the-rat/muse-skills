# TikTok instructions

## Surfaces

- The public feed, TikTok Studio (`/tiktokstudio`) for uploads and content,
  and the advertising tools (Promote, Ads Manager) are separate surfaces. Check
  the active account and surface before editing or publishing.
- Signed out, search can return an empty results area. When the task names an
  account, open its profile directly at `/@handle`.

## Uploads

- After an upload, read the media preview, caption and publication settings.
  Upload completion alone does not mean the video is published.

## Signing in

- “Log in” opens a dialog with several methods. Use “Back to more login
  options” to choose the intended one; “Phone” and “Username or email” expose
  different forms.
- After choosing a method, observe its current fields with `browser.observe`.
  Never reuse references from the previous form, and never toggle the password
  to reveal it.

### Verification codes

- The phone form takes the country code (“US +1 …”) and “Phone number”.
  “Send code” stays disabled until the number is complete, and the code goes in
  the single “Enter 6-digit code” field.
- “Maximum number of attempts reached. Try again later.” under the password is a
  rate limit. Stop signing in and report it in `browser.report`.

## Bot detection

- TikTok frequently shows a puzzle overlay that asks you to “Drag the slider to
  fit the puzzle”. It can cover a signed-in page; the session is still signed
  in behind it.
- Treat it as a bot challenge.
