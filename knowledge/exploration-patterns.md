---
doc_id: exploration-patterns
title: Exploration Patterns
status: approved
domain: ideation
related:
  - architecture
  - tool-conventions
last_updated: 2026-03-05
---

# Exploration Patterns

Techniques for divergent ideation within the Liminal framework. These patterns are used
when working with `.agents/explorations/` files and governed by the Explorer's Protocol.

## 1. Problem Framing

Before solving, ask: "What problem is this actually?"

Generate at least three distinct frames for any seed idea. Each frame implies different
solutions, users, and success metrics. Example:

> Seed: "A better way to manage personal finances"
> - Frame A: Budget discipline problem (behavioral)
> - Frame B: Emotional spending problem (psychological)
> - Frame C: Investment education problem (informational)

The user picks a frame. That choice shapes everything downstream.

## 2. Transformation Lenses

Deliberately mutate the idea through structured perspectives:

**Inversion:** Do the opposite. "Instead of helping people save, help them spend intentionally."

**Analogy Transfer:** Import structure from another domain. "What would Duolingo for X mean?"

**Constraint Shift:** Change the user's situation radically. "What if they had zero expertise?
What if they had 30 seconds per week? What if budget was unlimited?"

**Adjacent Possible:** Find the gap between two existing things. "X exists. Y exists.
What should exist between them?"

Apply at least two lenses per exploration. Not all will produce useful output — that's expected.

## 3. Assumption Excavation

Surface what's taken for granted, then challenge it:

- Identify implicit beliefs in the seed idea
- For each, ask: "Is this actually true? What if the opposite were true?"
- Label each assumption: `[UNTESTED]`, `[CONFIRMED]`, `[REJECTED]`, `[REFRAMED]`

Key questions:
- "You said users want X — do they want X, or do they want Y? Those lead to different designs."
- "This assumes people know what they want. What if they don't?"
- "What are you optimizing for? What are you willing to sacrifice?"

## 4. Direction Articulation

Present 3+ genuinely distinct paths. Each must include:

- **Mental model** — the metaphor that governs the design (marketplace, garden, pipeline, etc.)
- **Enables** — what this path makes possible
- **Forecloses** — what you give up by choosing this
- **Confidence** — `[SPECULATIVE]`, `[GROUNDED]`, or `[VALIDATED]`

If two directions only differ in surface features, they're the same direction. Push harder.

## 5. Stress Testing

Before committing to a direction, red-team it:

- **Core assumption wrong:** "If your main bet is wrong, what happens?"
- **Wild success:** "If this works perfectly, what second-order problems emerge?"
- **Failure modes:** "What are the three most likely ways this disappoints?"

## 6. Crystallization

The transition from exploration to execution. When a direction is solid enough:

1. Extract the problem frame into `knowledge/` as a concept document
2. Extract the chosen direction into `knowledge/` as a design document
3. Define the first workflow in `.agents/workflows/`
4. Move untested assumptions to `gtd/NEXT.md` as validation tasks
5. Update the exploration file: `status: archived`, fill `crystallized_to`

The exploration file is never deleted — it's the permanent record of how the idea evolved.

## Anti-Patterns

- **Premature convergence:** Jumping to a solution before mapping the space
- **Cosmetic diversity:** Presenting three versions of the same idea as "different directions"
- **Assumption blindness:** Taking the seed idea's framing as given without questioning it
- **Validation theater:** Asking questions that only confirm what was already decided
- **Orphaned exploration:** Starting an exploration but never crystallizing or archiving it
