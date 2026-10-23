### Injected context modified

The system file watcher flagged that `{file_location}`, one of your injected context files, has been deleted: the file no longer exists on disk. This is the diff of the deletion:

````diff
{diff}
````

This deletion came from outside this conversation, such as the user deleting it in the app, another chat, a scheduled task, or a background worker of yours. Treat the file as gone; your injected copy may still show it.
