#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one office joke to /output/entry.txt.
"""

import os

ENTRY = "The printer jammed on page 214 of a 215-page report, and the only copy of the fix instructions is on page 215."

# The twist lands in the final words: the fix is on the one page the
# jammed printer cannot reach. Two concrete numbers, one office object,
# one turn — no second beat, no explanation of the joke.

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
