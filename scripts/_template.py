"""
_template.py — Reference script for The Liminal tools
============================================================
Demonstrates project standards for all scripts in this layer:
  - argparse CLI interface
  - Structured YAML error output to stderr
  - Results to stdout
  - Exit codes: 0 = success, 1 = expected error, 2 = unexpected error

Usage:
    python scripts/_template.py --input <path> [--output <path>] [--verbose]
"""

import argparse
import logging
import sys
from pathlib import Path

import yaml  # pip install pyyaml


log = logging.getLogger(__name__)


def process(input_path: Path, output_path: Path | None, verbose: bool) -> dict:
    """
    Core logic placeholder. Replace with domain-specific processing.
    Returns a result dict that will be serialized to stdout as YAML.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")

    # --- your logic here ---
    result = {
        "status": "ok",
        "input": str(input_path),
        "rows_processed": 0,
    }

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(yaml.dump(result, allow_unicode=True), encoding="utf-8")
        if verbose:
            log.info("Output written to %s", output_path)

    return result


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--input", required=True, type=Path, help="Input file path")
    parser.add_argument("--output", type=Path, default=None, help="Output file path (optional)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def main() -> None:
    args = cli()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s %(message)s",
        stream=sys.stderr,
    )

    try:
        result = process(args.input, args.output, args.verbose)
        print(yaml.dump(result, allow_unicode=True), end="")
        sys.exit(0)

    except (FileNotFoundError, ValueError) as e:
        # Expected errors — caller can handle these
        error = {"status": "error", "type": type(e).__name__, "message": str(e)}
        print(yaml.dump(error, allow_unicode=True), end="", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        # Unexpected errors — signal something is wrong with the script itself
        error = {"status": "error", "type": "UnexpectedError", "message": str(e)}
        print(yaml.dump(error, allow_unicode=True), end="", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
