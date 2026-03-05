# Knowledge Index

Maps domain concepts to files. All knowledge files use the YAML frontmatter schema below.
The agent treats this index as the authoritative list — if a file is listed here but missing on disk, say so. Never fabricate its contents.

---

## Frontmatter Schema

Every knowledge file must begin with:

```yaml
---
doc_id: unique-slug
title: Human-Readable Title
status: draft           # draft | review | approved
domain: sub-domain-tag
related:
  - other-doc-id
last_updated: 2026-03-05
---
```

Only `approved` files may be cited as authoritative sources. `draft` and `review` files should be labeled `[DRAFT]` when referenced.

---

## Index

| doc_id | Title | Status | File | Description |
|--------|-------|--------|------|-------------|
| architecture | 5-Layer Architecture | approved | `knowledge/architecture.md` | The core Identity/Knowledge/Tools/Workflows/State decomposition, cross-cutting concerns, and how layers interact |
| safety-tiers | Safety Tier System | approved | `knowledge/safety-tiers.md` | T1/T2/T3 auto-execution model, criteria for each tier, platform mapping (Claude Code permissions, Cursor turbo, etc.) |
| exploration-patterns | Exploration Patterns | approved | `knowledge/exploration-patterns.md` | Divergent ideation techniques: problem framing, transformation lenses, assumption excavation, stress testing, crystallization |
| tool-conventions | Tool Development Conventions | approved | `knowledge/tool-conventions.md` | Script standards: argparse CLI, YAML errors to stderr, exit codes 0/1/2, line-by-line Markdown parsing, composability |
| platform-portability | Platform Portability Guide | draft | `knowledge/platform-portability.md` | [NOT YET CREATED] How to adapt the framework for Claude Code, Cursor, Windsurf, Gemini/Antigravity |
| glossary | Glossary | draft | `knowledge/glossary.md` | [NOT YET CREATED] Domain-specific terms: crystallization, confidence tiers, safety tiers, checkpoint, exploration, etc. |
| stack-selection | Stack Selection Criteria | approved | `knowledge/stack-selection.md` | Filter for stack-eligible ideas: cost gate, dimension count, stack fit, permanence. Includes current stack map and Pareto ingestion rule. |
