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
| `ab65bb4` | rename: Merovingian → The Liminal, Architect → Cartographer | 2026-03-05 |
| `78ee8d8` | init: system initialized — identity set, knowledge files created, workflows defined, GTD populated, schedule active | 2026-03-05 |
| `80bb04a` | feat: exploration layer — Explorer's Protocol, confidence tiers, exploration template, DECISIONS.md, SCRATCHPAD tool dev log | 2026-03-05 |
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

- Should the exploration layer have its own script tooling (e.g., a script that generates exploration files from a seed string)?
- How should confidence tiers interact with knowledge file status? Currently: knowledge must be [GROUNDED]+, but the mapping to draft/review/approved isn't formalized.
