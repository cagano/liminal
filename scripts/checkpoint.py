"""
checkpoint.py — Git checkpoint utility for Merovingian Agent
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
            break  # Reached the next section without finding the table
        elif in_checkpoints and re.match(r"^\|\s*-+\s*\|\s*-+\s*\|", line):
            # Found the Markdown table divider (e.g., |---|---|)
            insert_idx = i + 1
            break

    if insert_idx != -1:
        lines.insert(insert_idx, new_row)
    else:
        # Fallback: table missing or malformed — append a new one
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
