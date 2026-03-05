---
seed: "explore the idea of this framework itself"
status: open
started: 2026-03-05
last_touched: 2026-03-05
crystallized_to:
  - knowledge/stack-selection.md
---

# Exploration: liminal-framework

## Seed

> "The first idea we'll explore is the idea of this framework itself."

---

## Problem Frames

| # | Frame | Core tension | Who feels it most |
|---|-------|-------------|-------------------|
| 1 | **The Discipline Problem** | AI agents are powerful but undisciplined — sessions drift, claims fabricate, context evaporates. The framework is cognitive scaffolding that makes AI-assisted work reliable and epistemically honest. | Developers/researchers running long, multi-session agent projects |
| 2 | **The Knowledge Decay Problem** | Every AI session starts fresh. Humans can't hold all context either. The framework is a solution to persistent amnesia — a structured memory layer that neither side maintains naturally. | Solo knowledge workers doing deep, ongoing work with AI |
| 3 | **The Trust Problem** | You can't trust what an AI tells you unless you know where it got it. The framework is fundamentally a provenance system — confidence tiers, knowledge-first directives, traceable claims. | Anyone burned by an AI confidently stating something wrong |
| 4 | **The Handoff Problem** | AI-assisted work is currently non-transferable and non-auditable. DECISIONS.md + explorations create a permanent record of *why*, not just *what*. The framework makes AI work legible to a future self or collaborator. | Teams; solo workers handing off to future-self across sessions |

**Selected frame:** None yet — all four are live. Frames 2 and 4 feel most generative; Frame 3 is the sharpest commercial hook.

---

## Assumptions

| # | Assumption | Challenge | Status |
|---|-----------|-----------|--------|
| 1 | Markdown files are the right persistence layer | A database, vector store, or structured format might serve memory better. Markdown is human-readable but not machine-queryable at scale. | `[UNTESTED]` |
| 2 | A single AGENT.md is sufficient to define agent identity across platforms | Different platforms impose different constraints; a single file may not map cleanly to all runtimes. | `[UNTESTED]` |
| 3 | Users will maintain the discipline (SCRATCHPAD updates, checkpoints, tier annotations) | The framework's value depends on consistent use. Friction kills adoption. No enforcement mechanism exists. | `[UNTESTED]` |
| 4 | The 5-layer separation maps cleanly onto real work | In practice, identity/knowledge/tools/workflows may blur or collapse. The abstraction may not hold under pressure. | `[UNTESTED]` |
| 5 | The framework's primary consumer is a single agent + single user | Multi-agent, multi-user, or automated pipeline scenarios are not addressed and may expose structural gaps. | `[UNTESTED]` |
| 6 | Session-scoped memory is the main problem to solve | The real bottleneck might be something else: quality of knowledge files, quality of prompts, or the gap between agent capability and task complexity. | `[UNTESTED]` |

---

## Transformations

### Inversion
_What if we did the opposite?_

Instead of disciplining the **agent**, discipline the **user**. A framework that prompts the human to be more structured — to write clearer seeds, flag their own assumptions, state what they actually want before the agent responds. The agent becomes a mirror, not a worker. The discipline layer sits upstream of the session, not inside it.

### Analogy Transfer
_What existing solution in another domain does something structurally similar?_

- **Scientific lab notebook** — methodology documented, results separated from interpretation, all claims traceable to experiment. The framework is this, applied to AI-assisted cognitive work.
- **ADR (Architecture Decision Records)** — DECISIONS.md is exactly an ADR log. The framework wraps ADRs around the entire AI collaboration, not just code.
- **Operating procedures in aviation / medicine** — checklists for high-stakes, repeatable actions. Safety tiers + workflow annotations are this. The parallel suggests the framework may have untapped value in high-stakes domains.

### Constraint Shift
_What if the user had zero expertise? What if they had 30 seconds? What if there were no budget?_

- **Zero expertise:** The framework as written requires the user to understand the 5-layer model, know when to use Explorer's vs Critic's Protocol, and maintain discipline across sessions. A zero-expertise user can't operate it. This is a gap.
- **30 seconds:** The session-start hooks alone take several reads. If the framework must boot in 30 seconds, the entire AGENT.md + SCRATCHPAD read becomes a bottleneck. Suggests a compressed "fast context" format.
- **No persistent storage:** If files don't persist (ephemeral environments), what remains? The protocols and tiers — the mental model — survive even without files. The framework's deepest value may be the *thinking*, not the *files*.

### Adjacent Possible
_What's the gap between two known things?_

The gap between "AI assistant you chat with occasionally" and "AI partner embedded in a long-running project with institutional memory" is large and mostly unoccupied. The framework is attempting to occupy that gap. The adjacent possible is a **protocol standard** — a specification that any agent on any platform can implement, enabling genuine handoffs between agents, between sessions, and between teams. The framework is currently a scaffold; the adjacent possible is an interoperability standard.

---

## Directions

### Direction A: The Discipline Layer (Methodology)

**Mental model:** Scientific lab notebook / operating procedure
**Enables:** Rigorous, recoverable, epistemically honest AI-assisted work for a single practitioner. The framework as a practice — refined, documented, used.
**Forecloses:** Scale, automation, multi-user. Requires an expert user who understands and maintains the discipline.
**Confidence:** `[GROUNDED]`

### Direction B: The Product (Distributable Tool)

**Mental model:** Project scaffolding tool (create-react-app, cookiecutter)
**Enables:** Broad adoption. A CLI that generates scaffold, validates structure, checks tier annotations, flags missing files. The framework as a package anyone can install and use without understanding the internals.
**Forecloses:** Deep customization, practitioner-level nuance. Risk of cargo-culting — users follow the form without the intent.
**Confidence:** `[SPECULATIVE]`

### Direction C: The Protocol Standard (Interoperability)

**Mental model:** HTTP for agents — a shared specification enabling any compliant agent to hand off to any other
**Enables:** Multi-agent workflows, cross-platform continuity, team-scale AI collaboration, ecosystem effects.
**Forecloses:** Simplicity. A standard requires governance, versioning, compatibility negotiation. The maintenance burden is high and the adoption path is long.
**Confidence:** `[SPECULATIVE]`

---

## Stress Test

_(Applied to Direction A — the most grounded and currently active path.)_

**If the core assumption is wrong** (that Markdown + discipline = reliable AI-assisted work):
The framework becomes bureaucratic overhead. Sessions slow down because of hook rituals. Knowledge files accumulate but aren't actually consulted. The agent ignores them and hallucinates anyway. Result: ceremony without substance.

**If this succeeds wildly** (Direction A becomes the standard practice for serious AI-assisted work):
The bottleneck shifts from "how do I structure my sessions" to "how do I scale across projects, collaborators, and agents." The single-practitioner model breaks. The framework needs a migration path to Direction C without a full rewrite.

**Three most likely disappointments:**
1. Discipline collapse — the SCRATCHPAD and checkpoint hygiene erodes after a few sessions because the friction is real and the benefit is deferred.
2. Knowledge file rot — files get created but not updated, becoming stale faster than they get revised, eroding the knowledge-first principle.
3. Platform fragility — the framework works well in Claude Code but degrades in other environments where AGENT.md isn't read consistently or safety tiers aren't enforced.

---

## Forks & Decisions

| # | Fork | Chosen | Deferred | Reasoning |
|---|------|--------|----------|-----------|
| 1 | Where to start: refine the existing scaffold vs. explore what the framework *is* | Explore what the framework is (this file) | Refinement | Can't refine well without knowing which direction to refine toward |

---

## Crystallization

When a direction is solid enough to act on, extract it into the execution layers.

- [ ] Problem frame → `knowledge/liminal-framework-problem.md`
- [ ] Chosen direction → `knowledge/liminal-framework-concept.md`
- [ ] First workflow → `.agents/workflows/liminal-framework.md`
- [ ] Assumptions that need validation → task in `gtd/NEXT.md`

Once all extractions are done, set `status: archived` in frontmatter.
