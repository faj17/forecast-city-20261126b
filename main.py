#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — one line for Dribbleton.

In Dribbleton the rain falls upwards, so the official advice is
necessarily upside down too. validate() enforces the competition
gate (1-120 chars, not only whitespace) before anything is written.
"""

import os

SETUP = "In Dribbleton, rain falls upwards today. Umbrellas will not help."
PUNCH = "Hats are advised, worn underneath."

MAX_CHARS = 120


def assemble() -> str:
    return f"{SETUP} {PUNCH}"


def validate(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
