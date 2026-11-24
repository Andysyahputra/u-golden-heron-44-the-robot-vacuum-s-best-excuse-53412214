#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

A small deadpan machine explains why it missed a spot. The excuse is
assembled from three beats -- what the sensors saw, what they decided,
and how long the polite avoidance has lasted -- then written, exactly
once, to /output/entry.txt. Deterministic: no input, no randomness,
no network, so every run produces the same bytes.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 140

# The three beats of the excuse, in the vacuum's own voice.
_BEATS = (
    "My sensors found the spot,",
    "classified it as furniture,",
    "and I have been politely cleaning around it for three weeks.",
)


def build_entry() -> str:
    """Join the beats into the single entry line."""
    line = " ".join(_BEATS)
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
