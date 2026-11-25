#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.
Deterministic, no network, no secrets.
"""

import os

ENTRY = (
    "One star. He named me Fern, repotted me into a mug with no drainage "
    "holes, and now tells guests I'm 'low-maintenance' while I sit here "
    "drowning in three inches of standing water."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 279, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
