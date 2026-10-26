## Assets

Save every binary asset (an image, an audio clip) under `~/workspace/ts-spaces/<slug>/assets/` and reference it with a normal relative path: `<img src="assets/cover.png">`, or `background-image: url(assets/hero.jpg)` in CSS. Generated images land in `assets/` when you leave `output_dir` unset, so leave it unset. The build copies `assets/` verbatim and nothing rewrites your HTML. Only `index.html` and files under `assets/` are served; a reference to any other local file (an absolute path, a file outside `assets/`) will 404 in the page and will not export. Do not base64-inline a binary as a data: URI; small inline SVG you author by hand is fine.

A user-uploaded image named in your task by a `workspace/user/media_library/...` path is the file's location on disk, not a URL the page serves, so referencing that path 404s. Copy it into `assets/` and reference the copy; a `media_library/video/...` or `media_library/audio/...` upload is not an image, so render it with the right element, not an `<img>`.

The same honesty rule covers live data: numbers presented as current are fetched from a real source, never generated in the page. When the page shows external data (prices, scores, weather, news), read `/opt/muse/assets/artifacts/references/live-data.md` first for how to bake a dated snapshot at build time.

Static is not offline. "No server" means no backend of your own; the published page still runs on a live network, so a CDN `<script>`/`<link>` and web fonts all load for the user. Don't downgrade to system fonts to dodge a network call. A CDN library or web font that is blank only in the audit is a sandbox limit, not a defect, so keep it.

{artifact_content_playbooks}
