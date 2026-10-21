"""Update the README timeline.

Usage: uv run python -m journey [README.md] [--offline]
Env:   GITHUB_TOKEN (optional, raises the API rate limit), JOURNEY_LOGIN (default FreddiSantos).
Idempotent: running it twice in a row changes nothing.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from journey.github import fetch_entries
from journey.timeline import load_entries, render, replace_block


def main(argv: list[str]) -> int:
    offline = "--offline" in argv
    args = [a for a in argv if a != "--offline"]
    readme_path = Path(args[0] if args else "README.md")

    entries, exclude = load_entries(Path("journey.toml"))
    if not offline:
        login = os.environ.get("JOURNEY_LOGIN", "FreddiSantos")
        entries += fetch_entries(login, exclude, os.environ.get("GITHUB_TOKEN"))

    readme = readme_path.read_text(encoding="utf-8")
    updated = replace_block(readme, render(entries))
    if updated == readme:
        print("README already up to date.")
        return 0
    readme_path.write_text(updated, encoding="utf-8", newline="\n")
    print(f"README updated ({len(entries)} entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
