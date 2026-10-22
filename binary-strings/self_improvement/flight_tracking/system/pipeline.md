## Pipeline

The runtime resolves one retained message group. A read-only step checks flight relevance and reads native message context when required. The runtime validates those receipts before the reconciliation step can mutate Tracking. Reconciliation updates the canonical trip and its goal-owned jobs. The runtime verifies the reported activities and acknowledges the subscription. Processing ends there. Proactivity independently reads the original context events.
