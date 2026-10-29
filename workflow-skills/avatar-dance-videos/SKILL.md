# Avatar Dance Videos

Generate dancing videos for Muse’s current custom avatar from the
available dance catalog, preserving the active avatar.

## Default Jolly

- Use avatar.edit’s dance-video generation operation to retrieve
  Jolly’s existing dances.

- Request the exact number the user specifies. When no number is
  specified, request all available dances.

- Show Jolly’s returned videos immediately in your reply. Describe
  them as existing dances; do not promise new generation or a
  later background gallery.

## Prepare custom-avatar generation

- Generate the exact number of videos the user specifies. When no
  number is specified, generate all available dance slots.

- Completed, pending, and previously failed slots are excluded from
  new batches.

- The runtime checks eligibility and availability. A request exceeding
  availability is rejected without starting generation.

## Generate custom-avatar videos

- Use avatar.edit’s dance-video generation operation.

- For an accepted gallery offer, preserve the confirmed number and
  the identity of the avatar shown. If the avatar has changed, show
  the current gallery and obtain fresh confirmation.

- Generation returns its status directly, without an avatar preview
  to activate.

## Report custom-avatar progress and completion

- Explain how many videos completed, remain pending, failed, or
  did not start.

- Accepted pending jobs continue in the background. The runtime
  publishes completed videos as a chat gallery.

- Each call requests a new batch. Do not repeat the generation call
  to check progress.

## Available connectors

- Uses native avatar tools; no account connector is required.
