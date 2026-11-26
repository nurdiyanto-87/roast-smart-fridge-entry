"""Roast the Smart Fridge: one-line entry.

Writes a single roast line (<=160 chars, one line) to /output/entry.txt.
Pure Python standard library only.
"""

import os

ROAST = (
    "My smart fridge beeps if I leave the door open ten seconds, like it's "
    "timing how long I stand here staring inside hoping dinner will "
    "magically appear."
)


def validate(line: str) -> None:
    """Gate the entry the way the scorer does: one line, 1-160 chars."""
    if not (1 <= len(line) <= 160):
        raise ValueError(f"roast is {len(line)} chars, must be 1-160")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")


def main() -> None:
    validate(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
