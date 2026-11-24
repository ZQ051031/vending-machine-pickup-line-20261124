"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Entry: a pickup line a vending machine would use on a passing human.
Writes exactly one line to /output/entry.txt (no trailing newline).
Standard library only.
"""

import os

ENTRY = "Are you exact change? Because every time you walk by, my coin slot lights up and I can't make change for anyone else."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
