"""Roast the Smart Fridge: one-line entry.

Writes a single roast line (<=160 chars, one line) to /output/entry.txt.
Pure Python standard library only.
"""

import os

ROAST = (
    "My smart fridge's touchscreen suggests recipes from what's inside \u2014 "
    "mostly condiments and regret \u2014 then judges me like a nutritionist "
    "who caught me lying."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
