#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes a two-line warning to /output/entry.txt:
line one warns the writer's past self about one specific moment,
line two says in one sentence why that moment mattered.
"""

import os

ENTRY = (
    "Don't apologise to her in the car park after the argument on Sunday.\n"
    "The words you swallowed became the letter you wrote instead, "
    "and the letter is the only thing she kept."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
