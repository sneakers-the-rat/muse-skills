# Pinterest media instructions

## What this host serves

- This host serves Pin images and videos, under paths such as `/474x/…`,
  `/originals/…` and `/videos/…`. Use the originating Pin on pinterest.com for
  its description, board, source website and controls.
- Download an image from the observed media URL as given; `browser.files`
  cannot save Pin videos. Do not rewrite a path to get a larger image; open the
  Pin to find an original or larger one.

## Bot detection

- Checks appear occasionally. If a media URL is refused, return to the Pin page
  instead of retrying the file.
