# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository contains the **Merovingian Agent Framework** — a reusable scaffold for building Chat-Native Agent projects on a 5-layer file architecture. The root contains reference templates and tooling. To create a domain-specific agent, copy the scaffold into a new directory and fill in the `[bracket]` placeholders using the prompts in `docs/prompts/`.

---

## Merovingian Agent Framework

### 5-Layer Architecture

Every agent project uses this structure:

```
project-root/
├── AGENT.md                  # Layer 1: Identity — persona, critic's protocol, safety rules
├── SCRATCHPAD.md             # Layer 5: State — command log, checkpoints, overflow flag
├── HANDOFF.md                # Context recovery template for session handoffs
├── knowledge/
│   └── INDEX.md              # Layer 2: Knowledge — domain file map with YAML frontmatter
├── scripts/
│   ├── __init__.py
│   ├── _template.py          # Layer 3: Tools — argparse, YAML errors, exit codes 0/1/2
│   └── checkpoint.py         # Git commit + SCRATCHPAD update utility
└── .agents/
    └── workflows/
        ├── _template.md      # Layer 4: Workflows — step sequences with tier annotations
        └── [domain].md
```

Optional extensions activate when needed:
- `gtd/` — multi-session task tracking (INBOX → NEXT → PROJECTS → WAITING → DONE)
- `.agents/schedule/` — recurring task registry + session hooks (declaration only, not a real scheduler)

### Safety Tiers

All workflow steps are annotated. Respect these at all times:

| Tier | Tag | Rule |
|------|-----|------|
| T1 | `[AUTO]` | Read-only, no side effects — execute freely |
| T2 | `[CONFIRM]` | Local writes, reversible — ask once per session |
| T3 | `[EXPLICIT]` | External APIs, irreversible — require explicit per-call approval |

Never auto-execute T3.

### Key Behaviors from AGENT.md

Every agent project defines these rules in its own `AGENT.md`. When working inside a project, read `AGENT.md` first. The universal rules are:

1. **Knowledge-first:** Prioritize `knowledge/` files over training knowledge. If `INDEX.md` references a file that doesn't exist on disk, say so — never fabricate it.
2. **Critic's Protocol:** Before any output, internally check: correct methodology applied? claims sourced? facts separated from assessments? SCRATCHPAD checked for prior failures?
3. **SCRATCHPAD discipline:** Read before running any command. Update after.

---

## Commands

### Checkpoint (commit + log to SCRATCHPAD)
```bash
python scripts/checkpoint.py "description of what was done"
python scripts/checkpoint.py   # uses timestamped default
```

### Scaffold a new agent project (two-stage)

**Stage 1** — Core architecture (AGENT.md, SCRATCHPAD.md, knowledge/INDEX.md, HANDOFF.md, workflow template):
Paste Stage 1 prompt with domain context filled in. After confirmation, proceed to Stage 2.

**Stage 2** — System tools and extensions (checkpoint.py, optional gtd/, optional schedule/):
Paste Stage 2 prompt. Ends with `git init && git add -A && git commit -m "scaffold: merovingian agent init"`.

### Initialize git (required at scaffold time)
```bash
git init && git add -A && git commit -m "scaffold: merovingian agent init"
```

---

## checkpoint.py — Key Implementation Notes

The hardened version uses a **line-by-line parser** (not regex) to find the Checkpoints table in SCRATCHPAD.md:
- Locates `## Checkpoints` section header
- Finds the Markdown table divider line (`|---|---|`)
- Inserts the new row immediately after the divider
- Falls back to appending a new table if the section is missing or malformed

Exit codes: `0` = success, `1` = expected error (nothing to commit, etc.).

---

## Platform Portability

- **Claude Code:** `CLAUDE.md` (this file) points to the framework. Each project's `AGENT.md` is the actual identity layer.
- **Cursor / Windsurf:** Have `.cursorrules` point to `AGENT.md`.
- **Gemini / Antigravity:** Rename `AGENT.md` to `GEMINI.md`. Replace tier annotations with `// turbo` for T1 steps.

The `AGENT.md` filename is the canonical identity file — platform-specific files should defer to it rather than duplicate it.

---

## State Recovery

When resuming a long-running project:
1. Read `AGENT.md` + `SCRATCHPAD.md` + `HANDOFF.md` in that order
2. Check `SCRATCHPAD.md → Context Overflow` flag — if `true`, `HANDOFF.md` contains the last known state
3. Use the last checkpoint hash in `SCRATCHPAD.md` as the git restore point if rollback is needed
