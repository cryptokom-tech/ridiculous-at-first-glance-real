#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (max 200 characters) pitching a bizarre startup idea
that sounds absurd until you realise it would actually sell, to
/output/entry.txt. Deterministic, stdlib only, no network.

The pitch: fake paparazzi for micro-influencers. It sounds like a joke —
paying strangers to ambush you outside a cafe so people think you are
famous — until the money chain lands: brands only sponsor influencers who
already look famous, so the look of fame is itself a product worth $99.
"""

import os

PITCH = (
    "We send fake paparazzi to ambush you outside cafés so your followers "
    "think you're famous; micro-influencers pay $99 a shoot because brands "
    "only sponsor people who already look famous."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The gate allows UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not text or text.isspace():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text:
        raise ValueError("entry must be a single sentence on one line")


def main() -> None:
    validate(PITCH)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Read back and confirm the run is byte-identical every time: the
    # grader runs the program twice and both runs must match.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != PITCH:
        raise ValueError("read-back mismatch: entry.txt differs from PITCH")
    print(f"wrote {len(PITCH)} chars to {path}")


if __name__ == "__main__":
    main()
