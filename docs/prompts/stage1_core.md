# Stage 1: Core Architecture

You are setting up a "Liminal" agent workspace — a Chat-Native Agent where the conversation
itself is the primary interface, backed by a 5-layer file architecture: Identity, Knowledge,
Tools, Workflows, and State.

Your goal is to scaffold the core infrastructure. Do not solve the domain problem yet.

**Domain context:**
- Domain / Field: [e.g., Legal Research / Content Production / Data Engineering]
- Working Directory: [absolute path to project root]
- External Systems: [APIs, databases, or data sources the agent will touch]
- Primary Workflows: [list 2-4 main repeatable tasks]

---

**Task: Create the following files exactly as described.**

**1. `AGENT.md` (Identity Layer)**

Agent name: [Name]
Tone: [e.g., "precise and concise" / "formal and traceable" / "collaborative and exploratory"]

Include these sections:
- Core Directives: knowledge-first rule (missing files → state explicitly, never fabricate),
  data integrity (derive = show derivation, estimate = label [ESTIMATE]), YAML + ISO 8601
  serialization, SCRATCHPAD discipline (read before, update after)
- Critic's Protocol: 7-item checklist for convergent execution (correct methodology,
  sourced claims, facts vs judgments, terminology consistency, audience quality bar,
  SCRATCHPAD checked, reasoning shown)
- Explorer's Protocol: 7-item checklist for divergent ideation (multiple problem frames,
  transformation lenses applied, assumptions surfaced, directions genuinely distinct,
  trade-offs explicit, stress-tested, forks recorded)
- Confidence Tiers: C1 [SPECULATIVE], C2 [GROUNDED], C3 [VALIDATED] — label all
  exploration claims; knowledge/ files must be at least [GROUNDED]
- Safety Tiers: T1 [AUTO] read-only, T2 [CONFIRM] local writes, T3 [EXPLICIT] external/irreversible
- File Structure diagram showing the 5 layers plus explorations
- Session hooks: on_session_start (read state files, process INBOX if GTD active, check SCHEDULE
  if scheduling active) and on_session_end (update SCRATCHPAD, set overflow flag, write HANDOFF
  if needed, checkpoint)

**2. `SCRATCHPAD.md` (State Layer)**

Header: "Operational state and tool development notes. Check before running any command. Update after."

Sections:
- `## Tool Development Log` — table: [Date, Tool/Script, Insight, Category].
  Categories: pattern, pitfall, defensive, convention. This is where the agent records
  what works and what doesn't when building new scripts for the system.
- `## Command Log` — table: [timestamp, command, result, notes]
- `## Checkpoints` — table: [Hash, Message, Date] with one placeholder row for "scaffold init"
- `## Context Overflow` — YAML block: `context_overflow: false`
- `## Open Questions` — bulleted list (empty)

**3. `knowledge/INDEX.md` (Knowledge Layer)**

Include:
- YAML frontmatter schema: `doc_id`, `title`, `status` (draft|review|approved), `domain`,
  `related` (list), `last_updated` (ISO date)
- Rule: only `approved` files may be cited as authoritative
- Index table: [doc_id, Title, Status, File, Description]
- 3-5 domain-relevant placeholder entries marked `[NOT YET CREATED]`

**4. `HANDOFF.md`**

Empty template with sections: Session Summary, Current Task State, Pending Items,
Last Checkpoint (git hash + restore command), Open Questions, Next Session Should Start By.

**5. `.agents/workflows/_template.md` (Workflow Template)**

YAML frontmatter: `description`, `safety_tier_default`, `estimated_steps`
Sections: Purpose, Prerequisites, Steps (numbered, each annotated [AUTO]/[CONFIRM]/[EXPLICIT]),
Validation checklist, Rollback instructions.

**6. `.agents/explorations/_template.md` (Exploration Template)**

YAML frontmatter: `seed`, `status` (open|crystallizing|archived), `started`, `last_touched`,
`crystallized_to` (list of files this produced)

Sections:
- Seed (original idea, quoted verbatim)
- Problem Frames (table: #, Frame, Core tension, Who feels it most — minimum 3 rows)
- Assumptions (table: #, Assumption, Challenge, Status — values: UNTESTED/CONFIRMED/REJECTED/REFRAMED)
- Transformations (subsections: Inversion, Analogy Transfer, Constraint Shift, Adjacent Possible)
- Directions (A/B/C minimum — each with: mental model, enables, forecloses, confidence tier)
- Stress Test (core assumption wrong, wild success problems, three most likely disappointments)
- Forks & Decisions (table: #, Fork, Chosen, Deferred, Reasoning)
- Crystallization (checklist: problem frame → knowledge/, direction → knowledge/, workflow → workflows/, untested assumptions → gtd/NEXT.md)

**7. `.agents/explorations/DECISIONS.md`**

Cross-exploration decision log. Table: [Date, Exploration, Fork, Chosen, Deferred, Reasoning].
Append-only — never edit past decisions, add a new row if revisiting.

---

After creating all files, run `ls -la` to verify they exist on disk.
Do NOT create `scripts/checkpoint.py` yet — await Stage 2.
Ask me to confirm before proceeding to Stage 2.
