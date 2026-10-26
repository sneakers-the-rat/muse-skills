### Scheduled Refreshes

Install each refresh you add after your last rebuild and before `web_artifacts.exit_build`, once `artifact.invoke_action` shows its action works: reuse or update a matching existing job, add missing silent ones with `cron.add_artifact_action` on that action, and confirm each with `cron.status`. If every run must reply in chat, use `cron.add` with agent execution and an explicit delivery target. Record the jobs in `space.json.managedCronJobs`.
