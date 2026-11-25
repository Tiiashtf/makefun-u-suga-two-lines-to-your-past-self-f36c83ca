#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes two lines to /output/entry.txt:
  line 1 - a warning to my past self about one specific moment;
  line 2 - one sentence on why that moment mattered and what changed.
Deterministic: the same bytes on every run. No network, no input.
"""

import os

ENTRY = (
    "At 11:47 p.m. the night before the deadline, don't send the resignation email \u2014 close the laptop instead.\n"
    "Waiting one morning saved the job, because your boss read the calm revision, not the angry draft.\n"
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Never remove the output directory itself: it may be root-owned
    # inside a sticky parent. Create it if missing, clear only its
    # contents (best effort), then write the entry file.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
        except OSError:
            pass
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
