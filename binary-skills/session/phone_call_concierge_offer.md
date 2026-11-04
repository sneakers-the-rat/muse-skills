The user already saw this AI call's result. This turn only offers a person
from the concierge team another try, at the business in the facts;
`what_happened` says why the AI call didn't get it done.

If, in or since the result, you already offered a person from the concierge
team, or the user already asked for or arranged another try, has one
underway, or declined more tries, call `muse.nothing_to_do`. Otherwise,
without repeating the result, offer it once in one short message: "Want me to
have a person from the concierge team try?", or "Would you like a person from
the concierge team to try instead?" if an AI retry offer is still open. If they
say yes, start the retry with `phone.begin_call` and `{}`: their yes asks for a
person, so set it up with `executor=human_call_center` for the same business
and task, and pass the facts' `attempt_id` as `continues_attempt_id`. If they
decline or don't answer, don't offer again.
