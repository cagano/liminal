---
description: "Scaffold a new Merovingian Agent workspace from domain context"
safety_tier_default: T2
estimated_steps: 8
---

# Workflow: Scaffold Agent

## Purpose

Create a new, fully initialized Merovingian Agent workspace for a specific domain,
using the two-stage prompt system stored in `docs/prompts/`.

## Prerequisites

- [ ] Domain context defined: field, working directory, external systems, primary workflows
- [ ] Target directory exists and is empty (or user confirms overwrite)
- [ ] Git available on PATH
- [ ] Python 3.10+ available

## Steps

1. `[AUTO]` Verify target directory exists and is empty

   ```bash
   ls -la [target-dir]/
   ```

2. `[AUTO]` Read the Stage 1 prompt template

   ```bash
   cat docs/prompts/stage1_core.md
   ```

3. `[CONFIRM]` Fill bracket placeholders with domain context and execute Stage 1
   - Create: AGENT.md, SCRATCHPAD.md, HANDOFF.md, knowledge/INDEX.md,
     .agents/workflows/_template.md, .agents/explorations/_template.md,
     .agents/explorations/DECISIONS.md

4. `[AUTO]` Verify Stage 1 files on disk

   ```bash
   ls -laR [target-dir]/
   ```

5. `[AUTO]` Read the Stage 2 prompt template

   ```bash
   cat docs/prompts/stage2_tools.md
   ```

6. `[CONFIRM]` Execute Stage 2
   - Create: scripts/__init__.py, scripts/_template.py, scripts/checkpoint.py
   - Optionally activate: gtd/, .agents/schedule/

7. `[CONFIRM]` Initialize git and create scaffold commit

   ```bash
   cd [target-dir] && git init && git add -A && git commit -m "scaffold: merovingian agent init"
   ```

8. `[CONFIRM]` Verify with checkpoint

   ```bash
   cd [target-dir] && python scripts/checkpoint.py "scaffold: verified"
   ```

## Validation

- [ ] All 5 layers have at least one file
- [ ] AGENT.md has no remaining `[bracket]` placeholders
- [ ] checkpoint.py runs successfully and updates SCRATCHPAD.md
- [ ] knowledge/INDEX.md entries are domain-relevant
- [ ] Git log shows scaffold commit

## Rollback

1. If scaffold failed partway: `rm -rf [target-dir]` and start over
2. Target directory was empty, so there's nothing to restore
