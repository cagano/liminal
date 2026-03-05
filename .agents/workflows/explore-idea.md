---
description: "Run a structured divergent exploration on a new idea or problem"
safety_tier_default: T1
estimated_steps: 9
---

# Workflow: Explore Idea

## Purpose

Take a seed idea from the user and develop it through structured divergent exploration,
producing an exploration file that can later crystallize into knowledge and workflows.

## Prerequisites

- [ ] User has articulated a seed idea or problem
- [ ] `.agents/explorations/_template.md` exists
- [ ] `knowledge/exploration-patterns.md` exists and is `approved`

## Steps

1. `[AUTO]` Read the exploration template and patterns knowledge file

   ```bash
   cat .agents/explorations/_template.md
   cat knowledge/exploration-patterns.md
   ```

2. `[CONFIRM]` Create a new exploration file from template

   Copy `_template.md` to `.agents/explorations/[slug].md`.
   Fill in: seed (quoted verbatim from user), started date, status: open.

3. `[AUTO]` Problem Framing — generate at least three distinct frames

   Present frames to user in the exploration file's Problem Frames table.
   Ask: "Which resonates most, or is it something else entirely?"

4. `[AUTO]` Assumption Excavation — surface 3-5 buried assumptions

   Challenge each assumption with a reframing question.
   Label all as `[UNTESTED]`.

5. `[AUTO]` Apply at least two transformation lenses

   Fill in the Transformations section. Not all lenses will produce useful results.

6. `[AUTO]` Articulate 3+ genuinely distinct directions

   Each direction must have: mental model, enables, forecloses, confidence tier.
   Present trade-offs explicitly.

7. `[AUTO]` Stress test the strongest direction

   Fill in: core assumption wrong, wild success problems, three likely disappointments.

8. `[CONFIRM]` Record forks and decisions

   Update the exploration file's Forks table.
   Append to `.agents/explorations/DECISIONS.md`.

9. `[CONFIRM]` Evaluate readiness for crystallization

   Run Explorer's Protocol (all 7 items).
   If ready: update status to `crystallizing` and begin extraction to knowledge/workflows.
   If not ready: note what's missing in the exploration file and leave status as `open`.

## Validation

- [ ] Explorer's Protocol passed (all 7 items)
- [ ] At least 3 problem frames articulated
- [ ] At least 3 assumptions surfaced and labeled
- [ ] At least 2 transformation lenses applied
- [ ] At least 3 directions with trade-offs
- [ ] Stress test completed on strongest direction
- [ ] All forks recorded in DECISIONS.md

## Rollback

Explorations are low-risk — they produce only Markdown files.
1. If an exploration should be discarded: set `status: archived` with a note explaining why
2. Never delete exploration files — they're the audit trail of ideation
