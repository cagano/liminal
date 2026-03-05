# Initialization Prompts

These prompts scaffold a new Liminal agent workspace. Use them in order.

## Usage

1. Fill in all `[bracket]` placeholders in `stage1_core.md`
2. Paste the filled prompt into Claude Code (or your agent of choice)
3. Wait for the agent to confirm all files are created
4. Fill in `stage2_tools.md` if any optional extensions differ
5. Paste Stage 2 and let the agent finalize

## Two-Stage Rationale

Stage 1 creates the architecture files (text-heavy, many sections).
Stage 2 creates the Python scripts (code-heavy, requires exact output).
Splitting prevents output token limits from truncating the script code.
