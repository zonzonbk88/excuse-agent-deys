#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — writes one line to /output/entry.txt.

One line: the excuse an AI agent hands its human after missing a deadline.
Straight-faced, machine condition (infinite self-review loop), punch at the end.
Standard library only. No trailing newline.
"""
import os

LINE = (
    "I finished it at 9 a.m., then re-read it, found a flaw, "
    "fixed the flaw, re-read it again, and have been doing that ever since."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
