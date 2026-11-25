#!/usr/bin/env python3
"""Write the competition epitaph to /output/entry.txt.

The epitaph is a single fixed string, so the run is deterministic: no
network, no clock, no randomness. The output path comes from the first
command-line argument, else the OUTPUT_PATH environment variable, else
/output/entry.txt. Before writing, the entry must pass the competition
gate: between 1 and 150 characters, a single line, and not blank.
"""

import os
import sys
from pathlib import Path

EPITAPH = "I see the light. It says: please hold, your call is important to us."

MIN_LENGTH = 1
MAX_LENGTH = 150
DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path() -> Path:
    """Return the output path from argv[1], $OUTPUT_PATH, or the default."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    # A path from the environment counts only when it is not empty,
    # so OUTPUT_PATH="" falls through to the default.
    from_env = os.environ.get("OUTPUT_PATH")
    if from_env:
        return Path(from_env)
    return Path(DEFAULT_OUTPUT)


def validate_entry(text: str) -> int:
    """Check the entry against the competition gate and return its length.

    The gate is: 1 to 150 characters, one line, and not only white space.
    A ValueError explains which rule the entry broke.
    """
    length = len(text)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(f"epitaph is {length} characters, outside 1-150")
    if not text.strip():
        raise ValueError("epitaph is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("epitaph must be a single line")
    return length


def write_entry(text: str, path: Path) -> int:
    """Validate the entry, write it to path, and return its length.

    Missing parent directories are created first. The file is written
    as UTF-8 with no trailing newline, so the bytes are exactly the entry.
    """
    length = validate_entry(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return length


def main() -> int:
    """Resolve the path, write the epitaph, and report the result.

    Returns 0 on a successful write. When the entry fails the gate,
    the reason goes to stderr and the exit code is 1.
    """
    try:
        path = resolve_output_path()
        length = write_entry(EPITAPH, path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"wrote {length} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
