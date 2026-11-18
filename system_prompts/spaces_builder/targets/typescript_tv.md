TV wiring:
the host opens the app with `#hatch_target=tv`. `client/src/spaceTarget.ts` sets `data-hatch-target="tv"` on `<html>`; make sure `main.tsx` imports `./spaceTarget`. Leave phone and desktop untouched—put every TV change behind a `tv:` variant (`@custom-variant tv (&:where([data-hatch-target="tv"], [data-hatch-target="tv"] *));`).
