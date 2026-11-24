#!/usr/bin/env python3
"""The 3 AM Commit Message -- make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

MESSAGE = "fix: deleted production at 3 AM, then asked myself to review the change \u2014 I approved it"


def main() -> None:
    # Self-check the competition gate before writing: 1-200 chars,
    # a single line, and not only white space.
    if not 1 <= len(MESSAGE) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(MESSAGE))
    if "\n" in MESSAGE or not MESSAGE.strip():
        raise SystemExit("entry must be one non-blank line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
