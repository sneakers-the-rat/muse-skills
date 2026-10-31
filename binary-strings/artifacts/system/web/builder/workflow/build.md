### Goal

{goal_entry}

{orient_entry}

### Architecture

- Schema in `server/src/schema.ts`, migrations in `drizzle/*.sql`, action logic in `server/src/actions.ts`. The client calls typed server actions.
- `ctx.db` for structured rows, `ctx.blobs` for binary payloads. After mutations, use `ctx.invalidateQueries` or the local query helper pattern.
- Give each `defineAction` a one-sentence `description` for the user's agent.
- Schema changes: update `server/src/schema.ts`, create a forward migration with `web_artifacts.new_migration`, edit the new `drizzle/<NNNN>_*.sql`, then build as below. Don't edit migrations already applied to `app.db`. In multi-statement SQL migrations, put `--> statement-breakpoint` on its own line between statements.
- If an action needs native host capabilities (local files, installed CLIs, Node/Bun-only APIs, subprocesses), put that work in `server/src/privileged.ts` with `definePrivilegedContracts` and `definePrivilegedHandlers`, import descriptors from `@space/privileged`, declare them on the action, and call `ctx.executePrivileged`. Don't import `server/src/privileged.ts` from action-reachable code.

### TypeScript

The build typechecks with `strict`, `noUncheckedIndexedAccess` and `verbatimModuleSyntax`. Five shapes cause most compile failures.

- **Indexing gives `T | undefined`.** `arr[i]`, `record[key]`, `.find(...)` and array destructuring all need a real guard or fallback (`?? x`, `?.`, an early return, a destructuring default), never a bare `!`. For a date key write ``new Date(`${value}T00:00:00`)``. `const [y = 1970, m = 1, d = 1] = value.split("-").map(Number)` also compiles, but the defaults miss `NaN` and `m` is 1-indexed, so it needs `new Date(y, m - 1, d)`.
- **Import types with `import type`:** `import { useState, type FormEvent } from "react"`. Same for `ChangeEvent`, `KeyboardEvent`, `ReactNode`, and `import type { Actions }`.
- **`ctx.db` is an accessor:** call `ctx.db<typeof schema>()`. It has `select`, `insert`, `update`, `delete`, `run`, `all`, `get` and `batch`, and nothing else. No `transaction`, `query` or `selectDistinct`; for an atomic multi-statement write use `.batch([...])`.
- **Annotate a handler you factor out:** `import type { Ctx } from "@hatch/space-sdk"`, then `async function loadRows(ctx: Ctx, args: { limit: number })`. An untyped `ctx` is `any`, which also breaks `ctx.db<typeof schema>()`.
- **A response schema is checked at runtime; don't widen it to compile.** Returned values widen: `true` becomes `boolean`, and a text column is `string`. Hoist the schema to a name and annotate the handler against that name: `const doneResponse = z.object({ ok: z.literal(true) });`, then `response: doneResponse, handler: async (ctx, args): Promise<z.infer<typeof doneResponse>> => ...`. That keeps `z.literal(true)`. For an enum field type the column, `text("status", { enum: ["open", "done"] })`, not the schema. Widen only when the value really is computed. This error prints the whole handler signature, including `args: Record<string, never>`; the real mismatch is at the end of it, in the return type.

### Runtime Tool Patterns

{web_builder_runtime_media_guidance}
- `ctx.inference.complete(prompt, { schema, ... })` is for bounded transformations over data you already have: extraction, classification, summarization, rewriting, formatting, structured generation. A Zod `schema` is required (import `z` from `@hatch/space-sdk`); the runtime validates the response and returns the parsed, typed value; don't call `JSON.parse(...)` on it or cast it with `as`. Keep `prompt` about the task itself: never tell the model to return JSON, repeat the schema shape, or wrap the result in a code fence. Put types and constraints in the Zod schema. For text-only output pass `schema: z.string()`. Validation failures throw `InferenceSchemaError` (also exported from `@hatch/space-sdk`); prefer letting it propagate. If you do recover from schema failures, check with `InferenceSchemaError.is(e)`, NOT `e instanceof InferenceSchemaError`: the worker and your `actions.js` are separate bundles with separate class identities. **This is the one way to run a model in a web artifact: route every model task, text or vision, through it, and don't load or bundle your own model instead** (no client-side ML library, no downloaded weights, no third-party inference API) and don't fake a model's job with a heuristic or random stand-in. For vision tasks, pass `images: [{ dataBase64, mimeType: "image/jpeg" | "image/png", filename?, caption? }, ...]`; only JPEG and PNG are supported, so convert other formats client-side. Encode client file-input images with `fileToBase64` from `@hatch/space-sdk/client` and pass the result through the action request.

For spawned artifact tasks, keep one retrieval path: a refresh action starts or resumes a task with a precise assignment; the task gathers external content and calls the artifact's save action; the save action validates, dedupes, and stores; the client reads stored rows through normal queries. No competing paths for the same data source.

### Client Implementation

- Render server data straight from the query; a `useState` or `useRef` copy of it goes stale the moment the agent writes. Keep local state only for in-flight input (a drag, an unsaved form), and never put data sync behind a one-shot guard, a per-key guard, or an id-only dependency array. Syncing never discards what the user has typed, including after a failed save.
- Phone-first React UI: at phone width, the main task must be usable without horizontal scroll or cramped controls. Larger breakpoints improve composition; they don't make the basic product work.
- Every visible control must do something real; the audit addresses elements by accessible name, so give every control one (`aria-label` on icon-only buttons and inputs, or a visible bound label).
- Do not claim the artifact is using real data in copy; demonstrate it through content, timestamps, source labels, and working refresh/actions.
- Source-backed content uses real data from its source. {source_gap_remedy} Don't fill the gap with plausible rows.

### Styling

{space_template_build_styling}

### Build

{build_step}

Call `web_artifacts.exit_build` early only for a true blocker: unavailable required source material, wrong runtime, or a source/data failure that cannot be solved honestly.{blocker_exit_status}
