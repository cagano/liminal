# SCHEDULE

Recurring task registry. This is a *declaration layer* — actual triggering requires a real mechanism
(system cron, CI schedule, task runner, or session-start hook). The agent reads this to know what
to do when triggered; it does not self-trigger.

Format per entry:
```yaml
## [task-slug]
description: (what this task does)
frequency: daily | weekly | monthly | on-session-start | manual
last_run: YYYY-MM-DD or "never"
next_run: YYYY-MM-DD or "on next trigger"
script: path/to/script.py or "agent"
safety_tier: T1 | T2 | T3
enabled: true | false
```

---

## session-start-check
description: Read SCRATCHPAD, process INBOX, check for overdue scheduled tasks
frequency: on-session-start
last_run: never
next_run: on next trigger
script: agent
safety_tier: T1
enabled: true
