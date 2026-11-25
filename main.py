import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
ENTRY_TEXT = "Thank you for all the opportunities. I've taken them, including this one."


def main() -> None:
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
