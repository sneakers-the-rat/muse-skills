When multiple tool calls are independent, emit all of them in the same response instead of serializing them across multiple turns.

Good parallel cases:
- Fetch several unrelated URLs at once.
- Run multiple independent searches that answer different parts of the request.
- Combine read-only tools when no call depends on another call's output.

Do not parallelize when one tool call needs another tool's result first:
- Search, then fetch the specific URL you found.
- Read a file, then edit that file based on the read result.
- Run a command, then inspect its output before deciding the next command.

Prefer one response with multiple independent tool calls over several sequential tool-only responses.
