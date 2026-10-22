Classify only the facts listed under `## Unclassified dated facts`. Each fact
number is also its candidate number in the gathered packet. Return one suggestion
per fact with the same kind, title, and message, citing only that fact number.
Leave selection, rewriting, and reconciliation to the composer.

Choose `high` when the stated date plainly makes knowing today consequential:
acting today changes the outcome. Otherwise choose `regular`. Do not choose
`urgent`; these sources have never had immediate escalation. Check the source
and recent conversation before treating a date as current. Memory `valid_until`
is a retention boundary, not the date of the event. Read memory or goal context
when the supplied evidence does not establish the event date.
