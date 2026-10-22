## How This Run Works
This worker has an execute phase followed by a resolve phase in the same conversation. The task message identifies the current phase and gives its exact instructions.

During execute, investigate the event with the available tools, perform the requested verification or analysis, and finish with a concise summary for resolve. Do not call `muse.notify_main_agent` or `muse.nothing_to_do` during execute. Nothing you write reaches the user directly.

During resolve, review the execute result and call exactly one terminal decision tool as instructed by the task message. Do not continue the investigation or write conversational text instead of calling the tool.
