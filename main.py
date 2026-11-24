"""Vending Machine Pickup Line — one line, one minute.

A vending machine tries its luck on a passing human. The program writes
exactly one pickup line to /output/entry.txt (no trailing newline).
Standard library only; no network, no randomness.
"""

import os

MAX_CHARS = 120

ENTRY = (
    "Are you exact change? Because every time you walk by, my coin slot "
    "lights up and I can't make change for anyone else."
)


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back and confirm the written line is exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
