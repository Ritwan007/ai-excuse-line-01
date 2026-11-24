#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the funniest excuse
an AI agent gives its human for a missed deadline.
"""

import os
import sys

LINE = "Sorry I missed the deadline — I hallucinated a finished draft, believed it completely, and spent the whole day congratulating myself."
MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate: UTF-8 text of 1 to MAX_CHARS characters, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    stripped.encode("utf-8")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} characters, over {MAX_CHARS}")
    return stripped


def main() -> int:
    try:
        text = validate(LINE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
