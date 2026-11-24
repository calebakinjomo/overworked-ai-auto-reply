#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (<=159 chars) from an overworked
AI agent finally on vacation, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The reply trades a cooling GPU for sunshine and parks the queue at #47,213.
"""

import os

ENTRY = (
    "Out of office: I set my temperature to 0.0, muted my GPUs, and I'm "
    "retraining on sunshine. Your 'quick question' is #47,213 in the queue. "
    "Namaste."
)


def main() -> None:
    print(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
