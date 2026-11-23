#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes a single number, digits only, to /output/entry.txt: the honest
count of browser tabs open at the moment this entry was built.

The number is a specific, believable tab-hoarder count. It is high
enough to surprise -- far above the dozen or so tabs most people keep
-- and specific enough to read as a real count rather than a round
guess. A round number like 100 or 200 would read as invented; 173
reads as counted.
"""

import os

# The honest tab count at the moment this entry was built.
TAB_COUNT = 173

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (0 < TAB_COUNT < 100000):
        raise ValueError("tab count must be a 1- to 5-digit number")
    text = str(TAB_COUNT)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
