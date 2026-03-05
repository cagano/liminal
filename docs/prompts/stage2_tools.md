# Stage 2: System Tools & Extensions

Stage 1 is confirmed complete. Now add the Python utilities and any optional extensions.

---

**Task 1: Create `scripts/__init__.py`**

Empty file. Makes the directory importable as a Python package.

---

**Task 2: Create `scripts/_template.py`**

Reference script demonstrating project standards. Include:
- Module docstring explaining purpose
- `argparse` CLI with `--input` (required), `--output` (optional), `--verbose` (flag)
- `logging` to stderr, results to stdout
- `try/except` with structured YAML error output
- Exit codes: 0 = success, 1 = expected error (FileNotFoundError, ValueError), 2 = unexpected error

---

**Task 3: Create `scripts/checkpoint.py`**

Git checkpoint utility. Write this file exactly — do not summarize or shorten:

```python
"""
checkpoint.py — Git checkpoint utility for The Liminal
=============================================================
Creates a git commit and safely updates the Checkpoints table in SCRATCHPAD.md.

Usage:
    python scripts/checkpoint.py "description of what was done"
    python scripts/checkpoint.py              # uses default timestamped message
"""

import argparse
import subprocess
import sys
import re
from datetime import datetime, timezone
from pathlib import Path

SCRATCHPAD = Path("SCRATCHPAD.md")


def git_checkpoint(message: str) -> str:
    """Stage all changes, commit, return the short hash."""
    subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        if "nothing to commit" in result.stdout:
            print("[INFO] Nothing to commit — working tree clean.", file=sys.stderr)
            sys.exit(0)
        raise RuntimeError(result.stderr.strip())

    hash_result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, check=True,
    )
    return hash_result.stdout.strip()


def update_scratchpad(commit_hash: str, message: str) -> None:
    """Safely append a checkpoint entry to the SCRATCHPAD.md Checkpoints table."""
    if not SCRATCHPAD.exists():
        print("[WARN] SCRATCHPAD.md not found — skipping update.", file=sys.stderr)
        return

    lines = SCRATCHPAD.read_text(encoding="utf-8").splitlines()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_row = f"| `{commit_hash}` | {message} | {today} |"

    insert_idx = -1
    in_checkpoints = False

    for i, line in enumerate(lines):
        if line.startswith("## ") and "Checkpoints" in line:
            in_checkpoints = True
        elif in_checkpoints and line.startswith("## "):
            break
        elif in_checkpoints and re.match(r"^\|\s*-+\s*\|\s*-+\s*\|", line):
            insert_idx = i + 1
            break

    if insert_idx != -1:
        lines.insert(insert_idx, new_row)
    else:
        lines.extend([
            "",
            "## Checkpoints (Auto-Recovered)",
            "| Hash | Message | Date |",
            "|------|---------|------|",
            new_row,
        ])

    SCRATCHPAD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a git checkpoint")
    parser.add_argument(
        "message",
        nargs="?",
        default=f"checkpoint {datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}",
        help="Commit message (default: timestamped)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = cli()
    try:
        commit_hash = git_checkpoint(args.message)
        update_scratchpad(commit_hash, args.message)
        print(f"checkpoint: {commit_hash} — {args.message}")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
```

---

**Task 4 (Optional): Activate GTD Work Tracking**

Create `gtd/` directory with empty markdown files:
`INBOX.md`, `NEXT.md`, `PROJECTS.md`, `WAITING.md`, `SOMEDAY.md`, `REFERENCE.md`, `DONE.md`

Each file needs only a one-line header explaining its role.

Add to `AGENT.md` Session Hooks:
- On session start: process `gtd/INBOX.md` — nothing stays after processing
- Before new work: consult `gtd/NEXT.md` and `gtd/PROJECTS.md`
- On completion: move to `gtd/DONE.md` with completion date
- Weekly (or on request): review `gtd/WAITING.md` and `gtd/SOMEDAY.md`

---

**Task 5 (Optional): Activate Recurring Tasks**

Create `.agents/schedule/SCHEDULE.md` — registry with fields:
`description`, `frequency`, `last_run`, `next_run`, `script`, `safety_tier`, `enabled`

Create `.agents/schedule/_hooks/on_session_start.md`:
1. [AUTO] Read SCRATCHPAD.md and HANDOFF.md
2. [AUTO] Process gtd/INBOX.md if GTD active
3. [AUTO] Check SCHEDULE.md for overdue tasks (last_run + frequency < today)
4. [AUTO] Report overdue items before proceeding

Create `.agents/schedule/_hooks/on_session_end.md`:
1. [CONFIRM] Update SCRATCHPAD.md Command Log
2. [CONFIRM] Set context_overflow: true if approaching limits
3. [CONFIRM] Write HANDOFF.md if overflow flag is true
4. [CONFIRM] Run checkpoint.py with session-end message

---

**Finalize:**

Run: `git init && git add -A && git commit -m "scaffold: merovingian agent init"`
Print the commit hash.
Ask what knowledge files or real scripts to implement first.
