"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the one-line resignation letter of a cron job to /output/entry.txt.
It has fired every minute since March, never been thanked, and HR still
calls it "the cron thing".
"""

from pathlib import Path

LINE = "I resign. I have fired every minute since March, never once been thanked, and HR still calls me 'the cron thing'. — your cron job"
MAX_CHARS = 140


def main() -> None:
    assert LINE, "entry must not be empty"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, max {MAX_CHARS}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {len(LINE)} char(s) to {out}")


if __name__ == "__main__":
    main()
