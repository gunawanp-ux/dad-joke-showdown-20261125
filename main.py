"""Dad Joke Showdown entry.

Writes a single original dad joke to /output/entry.txt, where the
competition's gate scorer reads it (1-200 UTF-8 characters).
"""

from pathlib import Path

JOKE = "I told my son the gravy was the best storyteller at the table. It always thickens the plot."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: 1 to 200 characters.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError(f"joke is {len(JOKE)} characters, outside the 1-200 gate")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
