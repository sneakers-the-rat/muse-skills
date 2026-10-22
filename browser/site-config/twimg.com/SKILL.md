# X media instructions

## Media files

- This host serves the images and videos of X posts (`/media/…`), not the posts
  or account controls. Read a post and its context on the originating X page.
- Keep the observed media URL and its format parameters. Images download from
  it; `browser.files` cannot save videos. If an image fails, open the source
  post for a current link before downloading again.

## Bot detection

- Bot checks are rare on this host. When a media request fails, return to the
  source post rather than retrying the same URL.
