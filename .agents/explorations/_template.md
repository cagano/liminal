---
seed: "[The initial idea, question, or problem as stated by the user]"
status: open          # open | crystallizing | archived
started: 2026-03-05
last_touched: 2026-03-05
crystallized_to: []   # list of knowledge/ or workflows/ files this produced
---

# Exploration: [Slug]

## Seed

> [The original idea or problem, quoted verbatim from the user.]

---

## Problem Frames

Before solving anything, map what this problem might actually be.
List at least three distinct interpretations.

| # | Frame | Core tension | Who feels it most |
|---|-------|-------------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Selected frame:** (none yet — or note which one the user gravitated toward and why)

---

## Assumptions

Surface what's being taken for granted. Challenge each one.

| # | Assumption | Challenge | Status |
|---|-----------|-----------|--------|
| 1 | | | `[UNTESTED]` |
| 2 | | | `[UNTESTED]` |

Status values: `[UNTESTED]`, `[CONFIRMED]`, `[REJECTED]`, `[REFRAMED]`

---

## Transformations

Apply deliberate lenses to mutate the idea. Not all will be useful — that's the point.

### Inversion
_What if we did the opposite?_

### Analogy Transfer
_What existing solution in another domain does something structurally similar?_

### Constraint Shift
_What if the user had zero expertise? What if they had 30 seconds? What if there were no budget?_

### Adjacent Possible
_What exists nearby that doesn't exist yet? What's the gap between two known things?_

---

## Directions

Distinct conceptual paths forward. Each should be mutually exclusive enough
that choosing one forecloses or deprioritizes the others.

### Direction A: [Name]

**Mental model:** (marketplace / garden / pipeline / etc.)
**Enables:** (what this path makes possible)
**Forecloses:** (what you give up)
**Confidence:** `[SPECULATIVE]`

### Direction B: [Name]

**Mental model:**
**Enables:**
**Forecloses:**
**Confidence:** `[SPECULATIVE]`

### Direction C: [Name]

**Mental model:**
**Enables:**
**Forecloses:**
**Confidence:** `[SPECULATIVE]`

---

## Stress Test

Red-team the strongest direction before committing.

**If the core assumption is wrong:** (what happens?)

**If this succeeds wildly:** (what second-order problems emerge?)

**Three most likely disappointments:**
1.
2.
3.

---

## Forks & Decisions

Record every deliberate choice point. These are the "why" behind the design.

| # | Fork | Chosen | Deferred | Reasoning |
|---|------|--------|----------|-----------|
| 1 | | | | |

---

## Crystallization

When a direction is solid enough to act on, extract it into the execution layers.

- [ ] Problem frame → `knowledge/[slug]-problem.md`
- [ ] Chosen direction → `knowledge/[slug]-concept.md`
- [ ] First workflow → `.agents/workflows/[slug].md`
- [ ] Assumptions that need validation → task in `gtd/NEXT.md`

Once all extractions are done, set `status: archived` in frontmatter.
