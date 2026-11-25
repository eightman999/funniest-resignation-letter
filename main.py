import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
ENTRY_TEXT = "Effective Friday, my out-of-office message becomes a lifestyle."


def main() -> None:
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
