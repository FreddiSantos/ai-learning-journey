"""Timeline model and Markdown rendering. Pure functions, no network access."""

from __future__ import annotations

import re
import tomllib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

START = "<!-- TIMELINE:START -->"
END = "<!-- TIMELINE:END -->"

KINDS = {
    "milestone": "🏁",
    "course": "🎓",
    "project": "🚀",
    "reading": "📚",
    "learning": "💡",
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DATE_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")


@dataclass(frozen=True)
class Entry:
    date: str  # "YYYY-MM" or "" for ongoing
    kind: str
    title: str
    link: str = ""
    notes: str = ""

    def __post_init__(self) -> None:
        if self.kind not in KINDS:
            raise ValueError(f"unknown kind {self.kind!r}; use one of {sorted(KINDS)}")
        if self.date and not DATE_RE.match(self.date):
            raise ValueError(f"date must be 'YYYY-MM' or empty, got {self.date!r}")
        if not self.title.strip():
            raise ValueError("title must not be empty")


def load_entries(path: Path) -> tuple[list[Entry], set[str]]:
    """Read journey.toml. Returns the manual entries and the repo names to exclude."""
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    entries = [Entry(**raw) for raw in data.get("entry", [])]
    exclude = set(data.get("github", {}).get("exclude", []))
    return entries, exclude


def _format_month(date: str) -> str:
    year, month = date.split("-")
    return f"{MONTHS[int(month) - 1]} {year}"


def _format_entry(entry: Entry, with_date: bool) -> str:
    title = f"[{entry.title}]({entry.link})" if entry.link else entry.title
    prefix = f"**{_format_month(entry.date)}** · " if with_date else ""
    line = f"- {prefix}{KINDS[entry.kind]} {title}"
    return f"{line} — {entry.notes}" if entry.notes else line


def render(entries: list[Entry]) -> str:
    """Render entries as Markdown: summary, ongoing items, then dated items by year."""
    unique = list(dict.fromkeys(entries))  # remove exact duplicates, keep order
    counts = Counter(e.kind for e in unique)
    summary = " · ".join(
        f"{KINDS[k]} {counts[k]} {k}{'s' if counts[k] != 1 else ''}" for k in KINDS if counts[k]
    )
    lines = [summary or "_No entries yet._", ""]

    ongoing = [e for e in unique if not e.date]
    if ongoing:
        lines += ["### Ongoing", ""]
        lines += [_format_entry(e, with_date=False) for e in ongoing]
        lines.append("")

    dated = sorted((e for e in unique if e.date), key=lambda e: (e.date, e.title), reverse=True)
    year = None
    for entry in dated:
        entry_year = entry.date[:4]
        if entry_year != year:
            if year is not None:
                lines.append("")
            lines += [f"### {entry_year}", ""]
            year = entry_year
        lines.append(_format_entry(entry, with_date=True))

    return "\n".join(lines).rstrip()


def replace_block(readme: str, block: str) -> str:
    """Replace the text between the timeline markers. Raises if the markers are missing."""
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        raise ValueError(f"markers {START} / {END} not found")
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", readme)
