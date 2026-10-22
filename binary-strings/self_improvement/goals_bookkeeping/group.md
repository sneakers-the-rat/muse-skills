# Task: group this run's candidates

Group the supplied candidate operations by the one tracking goal each
candidate describes.

Use an `existing` group when candidates belong to the same supplied
tracking goal, even when a chunk proposed `create`. Prefer an existing
goal identity over a new group. Use a `new` group only for a distinct
project that does not match any tracking goal; merge differently
worded candidates for that project into one group.

For an existing goal, use `group_id=goal:<goal_id>` and copy its exact
`goal_id`. For a new project, use a stable
`group_id=new:<short-project-key>`. Return every candidate operation
id in exactly one group.
