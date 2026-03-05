# SCRATCHPAD.md

Operational state and tool development notes. Check before running any command. Update after.

---

## Tool Development Log

What works, what doesn't, and what to remember when building new scripts for this system.
Patterns, pitfalls, and hard-won lessons from programming tools in the scripts/ layer.

| Date | Tool / Script | Insight | Category |
|------|--------------|---------|----------|
| 2026-03-05 | checkpoint.py | Line-by-line table parsing is robust; regex substitution on full content is brittle against LLM-generated formatting variations | pattern |
| 2026-03-05 | checkpoint.py | Always include a fallback (auto-recovery table) when parsing structured Markdown — the file may be hand-edited or malformed | defensive |
| 2026-03-05 | _template.py | YAML error output to stderr + clean YAML to stdout keeps scripts composable in pipelines | pattern |

Categories: `pattern` (reusable approach), `pitfall` (avoid this), `defensive` (guard against this), `convention` (team/project standard)

---

## Command Log

| Timestamp | Command | Result | Notes |
|-----------|---------|--------|-------|
| — | — | — | — |

---

## Checkpoints

| Hash | Message | Date |
|------|---------|------|
| `aab7caa` | fix: audit findings — CLAUDE.md framing, requirements.txt, SCHEDULE format, GTD/schedule rules in AGENT.md, working directories | 2026-03-05 |
| `a31cb17` | scaffold: merovingian agent framework — all phases complete | 2026-03-05 |
| — | scaffold init | — |

---

## Context Overflow

```yaml
context_overflow: false
```

If `true`, write `HANDOFF.md` before ending the session.

---

## Open Questions

- (none)
