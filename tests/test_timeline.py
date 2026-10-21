from pathlib import Path

import pytest

from journey.github import releases_to_entries, repos_to_entries
from journey.timeline import END, START, Entry, load_entries, render, replace_block


def test_entry_rejects_unknown_kind() -> None:
    with pytest.raises(ValueError, match="unknown kind"):
        Entry(date="2026-10", kind="party", title="x")


def test_entry_rejects_bad_date() -> None:
    with pytest.raises(ValueError, match="YYYY-MM"):
        Entry(date="2026-13", kind="course", title="x")


def test_entry_rejects_empty_title() -> None:
    with pytest.raises(ValueError, match="title"):
        Entry(date="", kind="course", title="  ")


def test_render_groups_by_year_newest_first() -> None:
    md = render(
        [
            Entry("2025-03", "course", "Old course"),
            Entry("2026-10", "project", "New project", link="https://x.y", notes="Nice"),
            Entry("", "milestone", "Member of LIA"),
        ]
    )
    assert md.index("### Ongoing") < md.index("### 2026") < md.index("### 2025")
    assert "- **Oct 2026** · 🚀 [New project](https://x.y) — Nice" in md
    assert "- 🏁 Member of LIA" in md
    assert md.splitlines()[0] == "🏁 1 milestone · 🎓 1 course · 🚀 1 project"


def test_render_removes_duplicates_and_handles_empty() -> None:
    e = Entry("2026-01", "reading", "Paper")
    assert render([e, e]).count("Paper") == 1
    assert render([]) == "_No entries yet._"


def test_replace_block_is_idempotent() -> None:
    readme = f"intro\n{START}\nold\n{END}\nend\n"
    once = replace_block(readme, "new")
    assert once == f"intro\n{START}\nnew\n{END}\nend\n"
    assert replace_block(once, "new") == once


def test_replace_block_requires_markers() -> None:
    with pytest.raises(ValueError, match="markers"):
        replace_block("no markers here", "x")


def test_load_entries(tmp_path: Path) -> None:
    f = tmp_path / "journey.toml"
    f.write_text(
        '[github]\nexclude = ["skip-me"]\n\n'
        '[[entry]]\ndate = "2026-10"\nkind = "course"\ntitle = "ML basics"\n',
        encoding="utf-8",
    )
    entries, exclude = load_entries(f)
    assert entries == [Entry("2026-10", "course", "ML basics")]
    assert exclude == {"skip-me"}


def test_repos_to_entries_filters_and_maps() -> None:
    base = {"fork": False, "archived": False, "private": False, "description": None}
    repos = [
        {**base, "name": "good", "created_at": "2026-10-21T00:00:00Z", "html_url": "u1"},
        {**base, "name": "skip-me", "created_at": "2026-10-21T00:00:00Z", "html_url": "u2"},
        {**base, "name": "forked", "fork": True, "created_at": "2026-01-01", "html_url": "u3"},
    ]
    assert repos_to_entries(repos, {"skip-me"}) == [
        Entry("2026-10", "project", "Started good", link="u1")
    ]


def test_releases_to_entries_skips_drafts() -> None:
    releases = [
        {
            "draft": False,
            "published_at": "2026-11-02T00:00:00Z",
            "tag_name": "v0.2.0",
            "html_url": "r1",
        },
        {"draft": True, "published_at": None, "tag_name": "v0.3.0", "html_url": "r2"},
    ]
    assert releases_to_entries("tpl", releases) == [
        Entry("2026-11", "project", "Released tpl v0.2.0", link="r1")
    ]
