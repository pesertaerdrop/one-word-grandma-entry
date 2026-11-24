"""One Word From Grandma — deterministic entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the single word
a grandma would text about AI.

The word is "doohickey": the grandma word for a gadget she cannot name.
Warm, a little baffled, pointed at a machine, funny in one word with no
caption — and fresh against a field full of "robot" / "computer" / "magic".

Deterministic: no randomness, no network, no clock, no environment input
beyond the output directory. Every run writes the same 9 bytes.
"""

import os
from pathlib import Path

WORD = "doohickey"


def verify_entry(entry_path: Path) -> None:
    """Re-read entry.txt as bytes and confirm it is exactly b"doohickey"."""
    actual = entry_path.read_bytes()
    if actual != b"doohickey":
        raise SystemExit(
            f"entry verification failed: entry.txt is {actual!r}, "
            f"expected b'doohickey'"
        )


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Exactly the word, no trailing newline: 9 characters, 9 bytes, valid UTF-8.
    entry_path.write_text(WORD, encoding="utf-8")
    # Post-write byte-for-byte check: the entry must be exactly "doohickey"
    # (9 bytes, no newline). A silent wrong write would submit a bad entry,
    # so verify the bytes on disk right after writing and fail loudly.
    verify_entry(entry_path)


if __name__ == "__main__":
    main()
