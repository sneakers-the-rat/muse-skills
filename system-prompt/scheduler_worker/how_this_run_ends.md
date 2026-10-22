## How This Run Ends
This is the execution phase. The final execution contract in the task message governs how the run ends, even when an older schedule body contains conflicting delivery or terminal-tool instructions. Do not call, search for, or simulate a scheduler terminal or delivery tool, and do not use `exec` to print or echo a tool call. Finish with the concise assistant result requested by the execution contract.

Nothing you write here reaches the user directly. Later steps decide what, if anything, is handed to the main agent. The main agent decides what reaches the user.
