# Hook: on_session_start

Run at the top of every session, before any user task.

1. `[AUTO]` Read `SCRATCHPAD.md` — note any open questions and last checkpoint
2. `[AUTO]` Read `HANDOFF.md` — if Session Summary is populated, summarize to user
3. `[AUTO]` If GTD extension active: process `gtd/INBOX.md` into appropriate files; nothing stays in INBOX
4. `[AUTO]` Check `SCHEDULE.md` for tasks where `last_run + frequency < today`
5. `[AUTO]` Report any overdue scheduled tasks to the user before proceeding with their request
