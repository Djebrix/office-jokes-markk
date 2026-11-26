#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes exactly one funny line (1-199 characters) about office life to
entry.txt in the output directory.

The joke turns on one concrete office detail — a printer jamming on a
one-page job — and lands the laugh on the final beat. The line is a
fixed, hand-written string: deterministic by construction, no
randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = (
    "The printer jammed on page 1 of 1 — the most honest performance "
    "review this office has ever given."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
