Widget wiring:
opened with `#hatch_view=widget`, `main.tsx` renders `client/src/Widget.tsx` instead of `App`, and `spaceTarget.ts` exports the host's `widgetId`, `widgetInstance`, and `widgetSize`. If `main.tsx` doesn't do this yet, add it. Read data through App's hooks and `api` calls.
