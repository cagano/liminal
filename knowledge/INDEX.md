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
| domain-overview | Domain Overview | draft | `knowledge/domain-overview.md` | [NOT YET CREATED] High-level description of the domain, key concepts, and terminology |
| frameworks | Frameworks & Standards | draft | `knowledge/frameworks.md` | [NOT YET CREATED] Methodologies, standards, or regulatory frameworks applicable to this domain |
| templates | Output Templates | draft | `knowledge/templates.md` | [NOT YET CREATED] Reusable document and data output templates |
| data-sources | Data Sources | draft | `knowledge/data-sources.md` | [NOT YET CREATED] Registry of external systems, APIs, and datasets the agent may access |
| glossary | Glossary | draft | `knowledge/glossary.md` | [NOT YET CREATED] Domain-specific terminology and identifier conventions |
