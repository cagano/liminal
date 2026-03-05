---
doc_id: architecture
title: 5-Layer Architecture
status: approved
domain: core
related:
  - safety-tiers
  - tool-conventions
last_updated: 2026-03-05
---

# 5-Layer Architecture

The Liminal framework decomposes a Chat-Native Agent into five layers, each backed by files
on disk that the agent reads and writes during conversation.

## Layers

### Layer 1: Identity (`AGENT.md`)
Defines who the agent is: name, tone, core directives, protocols (Critic's and Explorer's),
safety tiers, and session hooks. This is the first file read on every session start.

### Layer 2: Knowledge (`knowledge/INDEX.md` + files)
The agent's source of truth. Prioritized over training knowledge. All files use YAML frontmatter
with status tracking (draft/review/approved). Only approved files are authoritative.

### Layer 3: Tools (`scripts/`)
CLI-first Python utilities. Each script follows a standard pattern: argparse interface,
YAML-structured errors to stderr, clean output to stdout, exit codes 0/1/2.
Scripts are composable — output from one can pipe into another.

### Layer 4: Workflows (`.agents/workflows/`)
Repeatable step sequences. Each step is annotated with a safety tier ([AUTO], [CONFIRM], [EXPLICIT]).
Every workflow has prerequisites, validation criteria, and rollback instructions.

### Layer 5: State (`SCRATCHPAD.md` + `HANDOFF.md`)
Operational memory. SCRATCHPAD tracks tool development lessons, command history, checkpoints,
and context overflow status. HANDOFF enables session continuity when context limits are reached.

## Cross-Cutting Concerns

Three concerns span all layers:

1. **Safety Boundaries** — The T1/T2/T3 tier system governs what actions require confirmation.
2. **Versioning & Rollback** — Git checkpoints after significant operations. SCRATCHPAD records
   commit hashes. Rollback via `git checkout [hash]`.
3. **Context Overflow** — When conversation grows long, the agent writes HANDOFF.md before
   session end. New sessions read it to resume.

## Extensions

Extensions are optional layers that activate when their directories exist:

- **Explorations** (`.agents/explorations/`) — Divergent ideation layer. Pre-workflow concept
  development with the Explorer's Protocol. Produces exploration files that crystallize into
  knowledge and workflows.
- **GTD** (`gtd/`) — Multi-session task tracking. INBOX for capture, NEXT for actions,
  PROJECTS for multi-step outcomes, WAITING for blockers, DONE for completion log.
- **Schedule** (`.agents/schedule/`) — Declaration layer for recurring tasks. Not a real
  scheduler — requires external triggering. Session hooks check for overdue items.

## Key Principle: Explore Then Execute

The architecture supports two modes of work:
- **Divergent** (Explorer's Protocol) — Generate possibilities, surface assumptions, map
  the problem space. Produces exploration files.
- **Convergent** (Critic's Protocol) — Execute with discipline, trace claims to sources,
  validate methodology. Produces knowledge files, scripts, and workflows.

Crystallization is the bridge: an exploration's chosen direction becomes a knowledge file
and/or workflow in the execution layer.
