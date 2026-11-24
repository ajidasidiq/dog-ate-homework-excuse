#!/usr/bin/env python3
"""Writes the dog's excuse, one line, to /output/entry.txt.

The dog was caught eating the homework. Its defence: it was not
eating, it was marking. The homework failed, so it filed the evidence
in its stomach, where no teacher can ever check the marking.
"""

import os

LINE = "I didn't eat your homework, I marked it. It failed, so I filed it in my stomach."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
