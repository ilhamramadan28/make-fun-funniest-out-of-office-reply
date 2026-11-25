"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Gate: UTF-8 text, 1-160 characters, not whitespace-only.
"""

import os

ENTRY = "I'm out of office. My inbox is being handled by a man named Regret, and he's on annual leave too."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the gate before writing: 1-160 chars, not whitespace-only.
    if not (1 <= len(ENTRY) <= 160) or not ENTRY.strip():
        raise ValueError("entry fails the 1-160 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
