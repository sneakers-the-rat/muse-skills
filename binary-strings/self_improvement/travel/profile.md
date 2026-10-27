Update the travel profile for this run.

1. Read `window` and `travel_context`. The current profile body is in
   `travel_context.profile_markdown`. If `travel_context.truncated` is true,
   only part of it loaded, so return `no_change` and say so.
2. Find what the user said about how they and their companions like to
   travel: planning, flight and hotel searches, bookings, and direct
   statements. `muse.context_fetch` reads the conversation. `muse.memory_search`
   and `muse.memory_get` help find older evidence; confirm what they return in
   the conversation itself, using `queries` and an earlier `since` when it is
   older than this run.
3. Decide what changes under the Ground Rules. When nothing in this window
   adds, changes, or removes an entry, return `no_change`.
4. Otherwise, stage the complete candidate at `travel/PROFILE.md` in your
   staging directory (its full path ends in `travel/<run id>/travel/PROFILE.md`)
   and submit its entries in file order. The shape check compares the
   submitted statements with the staged bullets and returns any mismatch for
   repair.

The staged file looks like this, with only the headings that hold entries:

```
# Travel Profile

## Airports
- <one entry>

## Loyalty programs
- <one entry>
```

Each submitted entry has:

- `section`: the heading, without `##`;
- `statement`: the bullet text, without the leading `- `;
- `evidence`: the message or quoted span where the user stated the preference
  or fact, or the trips behind a repeated pattern; and
- `claim`: the matching memory claim ID, when there is one.
