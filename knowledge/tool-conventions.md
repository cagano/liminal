---
doc_id: tool-conventions
title: Tool Development Conventions
status: approved
domain: tooling
related:
  - architecture
  - safety-tiers
last_updated: 2026-03-05
---

# Tool Development Conventions

Standards for all Python scripts in the `scripts/` layer.

## CLI Interface

Every script uses `argparse`. No positional-only arguments without clear semantics.
Include a module-level docstring that `argparse` can reference.

```python
def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()
```

## Output Contract

- **stdout:** Clean, machine-readable output (YAML preferred). This is the script's "return value."
- **stderr:** Human-readable logs and structured error output.
- Scripts are composable: `script_a.py | script_b.py` should work when both follow this contract.

## Error Handling

```python
try:
    result = do_work()
    print(yaml.dump(result), end="")
    sys.exit(0)
except (FileNotFoundError, ValueError) as e:
    # Expected errors — the caller can handle these
    error = {"status": "error", "type": type(e).__name__, "message": str(e)}
    print(yaml.dump(error), end="", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    # Unexpected errors — something is wrong with the script
    error = {"status": "error", "type": "UnexpectedError", "message": str(e)}
    print(yaml.dump(error), end="", file=sys.stderr)
    sys.exit(2)
```

## Exit Codes

| Code | Meaning | Example |
|------|---------|---------|
| 0 | Success | Script completed, output is valid |
| 1 | Expected error | File not found, invalid input, nothing to commit |
| 2 | Unexpected error | Bug in the script, unhandled exception |

## Markdown Parsing

When scripts read or modify Markdown files (e.g., SCRATCHPAD.md):

- **Use line-by-line parsing**, not regex on the full content string
- Scan for section headers (`## `) to locate the target section
- Find structural markers (table dividers `|---|---|`) within the section
- Always include a fallback path if the expected structure is missing or malformed
- LLMs generate Markdown with inconsistent spacing — design parsers to tolerate this

## Dependencies

All Python dependencies go in `requirements.txt` at project root. Scripts that import
third-party packages must list the install command in a comment on the import line:

```python
import yaml  # pip install pyyaml
```

## Naming

- `_template.py` — Reference script, not meant to be run directly
- `checkpoint.py` — Git checkpoint + SCRATCHPAD update
- Domain scripts: verb-noun pattern (e.g., `parse_input.py`, `generate_report.py`)
