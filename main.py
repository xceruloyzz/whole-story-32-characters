"""Tell a Whole Story in 32 Characters.

Running this program writes one Wi-Fi network name to entry.txt in
the output folder. The name is checked first (single line,
non-empty, at most 32 characters per the kit gate), then written
straight to the final file with no temporary files in the output
folder.
"""

import os

ENTRY = "The Neighbors Heard Everything"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not ENTRY.strip():
        raise ValueError("entry must not be empty")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > 32:
        raise ValueError("entry is over 32 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
