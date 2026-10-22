# YouTube media instructions

## Media links

- This host serves YouTube video and audio streams. Use the originating YouTube
  page for the title, captions, playback controls and source context.
- Stream URLs can be signed, can expire and can each carry a separate track.
  Keep a URL intact and get a fresh link from the source page when needed.
- A segment or audio track is not a complete video, and `browser.files` saves
  only a download control's file or an open image or PDF, so it cannot save
  these streams.

## Bot detection

- Stream requests are rarely blocked. When one fails, reload the YouTube page,
  not the stream URL.
