"""Fetch public repositories and releases from the GitHub REST API (stdlib only)."""

from __future__ import annotations

import json
import urllib.request

from journey.timeline import Entry

API = "https://api.github.com"


def _get(url: str, token: str | None) -> list[dict]:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def repos_to_entries(repos: list[dict], exclude: set[str]) -> list[Entry]:
    """One 'project' entry per public, non-fork, non-archived repository."""
    entries = []
    for repo in repos:
        if repo["fork"] or repo["archived"] or repo["private"] or repo["name"] in exclude:
            continue
        entries.append(
            Entry(
                date=repo["created_at"][:7],
                kind="project",
                title=f"Started {repo['name']}",
                link=repo["html_url"],
                notes=repo.get("description") or "",
            )
        )
    return entries


def releases_to_entries(repo_name: str, releases: list[dict]) -> list[Entry]:
    """One 'project' entry per published (non-draft) release."""
    return [
        Entry(
            date=rel["published_at"][:7],
            kind="project",
            title=f"Released {repo_name} {rel['tag_name']}",
            link=rel["html_url"],
        )
        for rel in releases
        if not rel["draft"] and rel.get("published_at")
    ]


def fetch_entries(login: str, exclude: set[str], token: str | None) -> list[Entry]:
    repos = _get(f"{API}/users/{login}/repos?per_page=100&type=owner", token)
    entries = repos_to_entries(repos, exclude)
    for repo in repos:
        if repo["name"] in exclude or repo["fork"] or repo["private"]:
            continue
        releases = _get(f"{API}/repos/{login}/{repo['name']}/releases?per_page=100", token)
        entries += releases_to_entries(repo["name"], releases)
    return entries
