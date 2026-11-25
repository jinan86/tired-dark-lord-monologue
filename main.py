#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

A fantasy villain speaks to the hero who has climbed up to kill him.
He is not a conqueror on a throne: four hundred years ago he chained
the god Maw beneath this mountain, and ever since he alone has held
the chain. His exhaustion never gets named -- it leaks out in lost
counts, dropped threads and deflections, and the last line hands the
hero the burden instead of a battle.

Writes exactly one text to <OUTPUT_DIR>/entry.txt (default /output).
Python 3.13, standard library only, fully deterministic: the same
bytes on every run, no network, no randomness, no secrets.
"""

import os
import sys

# Exactly 100 words, 506 characters. Counted by hand and by machine.
MONOLOGUE = (
    "You came up the black stair, past the chalk marks where I count the nights. "
    "Four hundred years, and I still lose count at \u2014 never mind. "
    "I chained the god Maw under this rock when your great-grandfather's sword "
    "was new. He sings, down there. He sings my name wrong, on purpose, to "
    "pass the time. The chain is cold. It slips. It always slips, and I catch "
    "it, and I catch it, and \u2014 what was your name? Ah. Yes. You, with the "
    "bright sword. Strike, then. But hold the chain while you do. "
    "It only knows my hands."
)

EXPECTED_WORDS = 100
MAX_CHARS = 600


def main() -> int:
    words = MONOLOGUE.split()
    if len(words) != EXPECTED_WORDS:
        print(f"error: monologue is {len(words)} words, expected {EXPECTED_WORDS}",
              file=sys.stderr)
        return 1
    if not 1 <= len(MONOLOGUE) <= MAX_CHARS:
        print(f"error: monologue is {len(MONOLOGUE)} chars, gate is 1-600",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(MONOLOGUE)
    print(f"wrote {path}: {len(words)} words, {len(MONOLOGUE)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
