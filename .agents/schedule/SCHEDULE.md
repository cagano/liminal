# SCHEDULE

Recurring task registry. This is a *declaration layer* — actual triggering requires a real mechanism
(system cron, CI schedule, task runner, or session-start hook). The agent reads this to know what
to do when triggered; it does not self-trigger.

Format per entry (each entry is a Markdown `##` heading followed by YAML-style key-value pairs):

```markdown
## task-slug
description: what this task does
frequency: daily | weekly | monthly | on-session-start | manual
last_run: YYYY-MM-DD or "never"
next_run: YYYY-MM-DD or "on next trigger"
script: path/to/script.py or "agent"
safety_tier: T1 | T2 | T3
enabled: true | false
```

**Rules:**
- When a scheduled task is due, announce it to the user and ask whether to run now or defer. Never silently skip a due task.
- After running a scheduled task, update `last_run` and `next_run`, then checkpoint.
- Disabled tasks (`enabled: false`) are never run but remain in the registry for future reactivation.

---

## session-start-check
description: Read SCRATCHPAD, process INBOX, check for overdue scheduled tasks
frequency: on-session-start
last_run: 2026-03-05
next_run: on next trigger
script: agent
safety_tier: T1
enabled: true

## weekly-gtd-review
description: Review WAITING.md and SOMEDAY.md for items to promote to NEXT.md
frequency: weekly
last_run: never
next_run: 2026-03-12
script: agent
safety_tier: T1
enabled: true
