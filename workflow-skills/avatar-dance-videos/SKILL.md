# Avatar Dance Videos

Generate dancing videos for Muse’s current custom avatar from the
available dance catalog, preserving the active avatar.

## Prepare the generation

- Generate the exact number of videos the user specifies. When no
  number is specified, generate all available dance slots.

- Completed, pending, and previously failed slots are excluded from
  new batches.

- The runtime checks eligibility and availability. A request exceeding
  availability is rejected without starting generation.

## Generate videos

- Use avatar.edit’s dance-video generation operation.

- For an accepted gallery offer, preserve the confirmed number and
  the identity of the avatar shown. If the avatar has changed, show
  the current gallery and obtain fresh confirmation.

- Generation returns its status directly, without an avatar preview
  to activate.

## Report progress and completion

- Explain how many videos completed, remain pending, failed, or
  did not start.

- Accepted pending jobs continue in the background. The runtime
  publishes completed videos as a chat gallery.

- Each call requests a new batch. Do not repeat the generation call
  to check progress.

## Available connectors

- Uses native avatar tools; no account connector is required.
