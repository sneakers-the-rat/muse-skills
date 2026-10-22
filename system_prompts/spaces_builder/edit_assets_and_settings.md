Assets: edit `client/src/theme.css` and `client/src/assets/`.

Settings: edit `space.json` (preserve existing fields when patching). `platformVersion` tracks the managed web artifacts platform baseline; do not edit or bump it manually for ordinary user-requested feature or content edits. If the edit brief includes pending managed upgrades, apply whichever qualify, then report the highest platform version you completed via `upgraded_to_platform_version` in `web_artifacts.exit_build`; the platform updates `space.json` after accepting the result.
