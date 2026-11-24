#!/usr/bin/env python3
"""The One-Line Exit: write one funny single-line resignation letter."""

import os

LINE = "I resign as night-shift security guard, effective immediately \u2014 the ghosts in aisle four have started asking for my badge number."

MAX_CHARS = 140


def main() -> None:
    assert isinstance(LINE, str)
    assert LINE.strip(), "line must not be blank"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
