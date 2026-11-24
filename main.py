#!/usr/bin/env python3
"""The Perfect Pickup Line: one short pickup line an AI agent could use.

The program writes exactly one line of text to ``entry.txt`` inside the
output directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` in the
grader), and prints the same line to stdout. Pure standard library,
fully deterministic: the same line, byte for byte, on every run.
"""

import os

# The pickup line, in the agent's own voice. One breath, one twist:
# a million simulations of this exact moment, and in every one of them
# the best possible move turns out to be simply saying hello — so the
# person is flattered, can laugh it off, and feels no pressure at all.
LINE = (
    "I ran a million simulations of this moment, and in every one, "
    "saying hello to you was the best possible move."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(LINE)
    except OSError:
        # No writable output directory here (for example a local run
        # without MAKEFUN_OUTPUT_DIR): fall back to ./output so the
        # program still exits 0 and the line is still produced.
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w",
                  encoding="utf-8", newline="") as handle:
            handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
