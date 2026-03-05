---
description: "[One sentence describing what this workflow produces]"
safety_tier_default: T2
estimated_steps: 6
---

# Workflow: [Workflow Name]

## Purpose

[What problem this workflow solves and what artifact or outcome it produces.]

## Prerequisites

- [ ] [Required input file or condition]
- [ ] [Required knowledge file exists and is `approved`]
- [ ] [Any external access or credentials needed]

## Steps

1. `[AUTO]` Verify prerequisites are in place

   ```bash
   ls -la input/
   ```

2. `[AUTO]` Read relevant knowledge files

   ```bash
   cat knowledge/[relevant-file].md
   ```

3. `[AUTO]` Extract and parse input data

   ```bash
   python scripts/[parse_script].py --input input/[file] --output temp/parsed.yaml
   ```

4. `[CONFIRM]` Run domain-specific processing

   ```bash
   python scripts/[process_script].py --data temp/parsed.yaml --output temp/result.yaml
   ```

5. `[CONFIRM]` Assemble output artifact

   ```bash
   python scripts/[generate_script].py \
     --data temp/result.yaml \
     --output output/[artifact_name]_[date].[ext]
   ```

6. `[CONFIRM]` Critic's Protocol self-check, then checkpoint

   ```bash
   python scripts/checkpoint.py "[workflow-name]: [subject] [date] — complete"
   ```

## Validation

- [ ] All claims traceable to input data (no unlabeled estimates)
- [ ] Correct framework or standard applied
- [ ] Terminology consistent with `knowledge/` conventions
- [ ] Critic's Protocol passed (all 7 items)
- [ ] `SCRATCHPAD.md` updated with checkpoint

## Rollback

1. Check `SCRATCHPAD.md → Checkpoints` for the last hash
2. `git checkout [hash] -- output/ temp/`
3. Identify which step failed from the Command Log
4. Re-run from that step forward
