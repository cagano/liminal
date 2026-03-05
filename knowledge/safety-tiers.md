---
doc_id: safety-tiers
title: Safety Tier System
status: approved
domain: core
related:
  - architecture
  - platform-portability
last_updated: 2026-03-05
---

# Safety Tier System

## Tiers

| Tier | Tag | Criteria | Agent Behavior |
|------|-----|----------|----------------|
| T1 | `[AUTO]` | Read-only, no side effects, no network | Execute freely without asking |
| T2 | `[CONFIRM]` | Local writes, reversible operations | Ask once per session or per batch |
| T3 | `[EXPLICIT]` | External APIs, irreversible actions, sensitive data | Require explicit per-invocation approval |

## Classification Rules

**T1 if all of these are true:**
- Operation reads but does not modify state
- No network calls
- No sensitive data accessed
- Idempotent — running it twice changes nothing

**T2 if any of these are true (and none of the T3 triggers):**
- Creates or modifies local files
- Makes git commits
- Runs local computations that produce output files
- Modifies SCRATCHPAD.md or other state files

**T3 if any of these are true:**
- Calls an external API
- Sends data outside the local environment (email, webhook, upload)
- Performs an irreversible operation (data deletion, production deployment)
- Accesses credentials, tokens, or personal data
- Exports data to a format that leaves the project boundary

## Workflow Annotation

Every step in a workflow file must be annotated with its tier:

```markdown
1. `[AUTO]` Read the input file
2. `[CONFIRM]` Write the processed output
3. `[EXPLICIT]` Push results to external API
```

If a step's tier is ambiguous, classify it at the higher tier.

## Platform Mapping

- **Claude Code:** T1 maps to auto-allowed tools. T2 maps to tools that prompt once. T3 maps to tools that always prompt.
- **Cursor / Windsurf:** T1 maps to `// turbo` annotation. T2/T3 require manual approval.
- **Gemini / Antigravity:** T1 maps to `// turbo`. No native T2/T3 distinction — all non-turbo steps prompt.
