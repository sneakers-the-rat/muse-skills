### Injected context modified

The system file watcher flagged a change to `{file_location}`, one of your injected context files: the file on disk no longer matches the copy you have. This is the diff of the change:

````diff
{diff}
````

This change came from outside this conversation, such as<!-- personal-muse-only:start --> the user editing the file in the app,<!-- personal-muse-only:end --> another chat, a scheduled task, or a background worker of yours, unless one of your own tool calls made it. Use it; your injected copy may still show the old content.
