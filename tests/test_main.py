from pathlib import Path

import pytest

import journey.__main__ as cli
import journey.github as gh
from journey.timeline import END, START, Entry


@pytest.fixture
def workdir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "journey.toml").write_text(
        '[[entry]]\ndate = "2026-10"\nkind = "milestone"\ntitle = "Kickoff"\n', encoding="utf-8"
    )
    (tmp_path / "README.md").write_text(f"# J\n{START}\n{END}\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_main_offline_updates_then_is_idempotent(
    workdir: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert cli.main(["--offline"]) == 0
    assert "Kickoff" in (workdir / "README.md").read_text(encoding="utf-8")
    assert cli.main(["--offline"]) == 0
    assert "already up to date" in capsys.readouterr().out


def test_main_online_merges_github_entries(workdir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cli, "fetch_entries", lambda login, exclude, token: [Entry("2026-10", "project", "Repo")]
    )
    assert cli.main([]) == 0
    text = (workdir / "README.md").read_text(encoding="utf-8")
    assert "Kickoff" in text and "Repo" in text


def test_fetch_entries_uses_repos_and_releases(monkeypatch: pytest.MonkeyPatch) -> None:
    repo = {
        "name": "proj",
        "fork": False,
        "archived": False,
        "private": False,
        "description": "Desc",
        "created_at": "2026-10-01T00:00:00Z",
        "html_url": "u",
    }
    release = {
        "draft": False,
        "published_at": "2026-11-01T00:00:00Z",
        "tag_name": "v1",
        "html_url": "r",
    }
    calls: list[str] = []

    def fake_get(url: str, token: str | None) -> list[dict]:
        calls.append(url)
        return [release] if "/releases" in url else [repo, {**repo, "name": "skip"}]

    monkeypatch.setattr(gh, "_get", fake_get)
    entries = gh.fetch_entries("me", {"skip"}, token=None)
    assert [e.title for e in entries] == ["Started proj", "Released proj v1"]
    assert sum("/releases" in c for c in calls) == 1
