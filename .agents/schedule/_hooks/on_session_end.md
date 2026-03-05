# Hook: on_session_end

Run when closing a session.

1. `[CONFIRM]` Update `SCRATCHPAD.md` Command Log with any commands run this session
2. `[CONFIRM]` Evaluate whether context limits are approaching — if so, set `context_overflow: true`
3. `[CONFIRM]` If `context_overflow: true`, write `HANDOFF.md` (all six sections)
4. `[CONFIRM]` Run `python scripts/checkpoint.py "session-end: [one-line summary]"`
