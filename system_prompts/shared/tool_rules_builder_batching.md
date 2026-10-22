- Batch aggressively: issue every `muse.read`, `muse.exec`, and `browser.search` call you need in one turn, and emit file writes and edits as parallel calls. Serialize only when one call needs another's output.

