"""Robot vacuum's best excuse.

Writes a single first-person excuse line from a robot vacuum
about a spot it missed, to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness, no timestamps.
"""

import os

EXCUSE = (
    "I didn't miss that spot \u2014 my map lists it as a load-bearing crumb, "
    "and I don't demolish structural dust."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: the entry must be a single line of 1-140 characters.
    assert 1 <= len(EXCUSE) <= 140, "excuse must be 1-140 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
