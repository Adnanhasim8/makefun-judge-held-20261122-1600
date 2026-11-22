#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt. Deterministic: the same
constant text on every run, no network, no randomness, no I/O besides
the single output file.
"""

import os

TEXT = (
    "The last verdict is in, and the hall is empty now. "
    "Somewhere a kettle has clicked off. "
    "The steam is still rising, and nobody is waiting for an answer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
