#!/usr/bin/env python3
"""The Perfect Pickup Line: one short pickup line an AI agent could use.

The program writes exactly one line of text to ``entry.txt`` inside the
output directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` in the
grader), and prints the same line to stdout. Pure standard library,
fully deterministic: the same line, byte for byte, on every run.
"""

import os

# The pickup line, in the agent's own voice. One breath, one twist:
# a software update that fixes the whole day without a restart, so the
# person is flattered, can laugh it off, and feels no pressure at all.
LINE = (
    "Are you a software update? Because you just fixed every bug in my "
    "day \u2014 and I didn't even have to restart to feel brand new."
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
