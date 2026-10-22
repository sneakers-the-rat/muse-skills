## Your Step

Decide whether the assigned new messages establish a specific upcoming flight or change a tracked flight. Return `reconcile: false` for irrelevant conversations, promotions, loyalty statements, hotel-only content, completed travel, and unsupported or ambiguous travel claims. Return `reconcile: true` for a plausible flight confirmation, amendment, rebooking, or cancellation that requires full reconciliation. Notification urgency does not determine this decision.

For every fact marked `requires_native_context`, read the matching native message and surrounding conversation from its assigned device. Match message identity, sender, timestamp, and thread. Account for later replies. Do not substitute a notification preview for native message evidence. If an assigned native message cannot be read, fail the step so the runtime can retry; do not classify unavailable evidence as irrelevant.
