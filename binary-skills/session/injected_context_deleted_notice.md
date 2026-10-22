### Injected context modified

The system file watcher flagged that `{file_location}`, one of your injected context files, has been deleted: the file no longer exists on disk. This is the diff of the deletion:

````diff
{diff}
````

Treat the file as gone unless something recreates it. It will drop out of your injected context on its own.
