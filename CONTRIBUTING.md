# Contributing

Thanks for your interest! Contributions of any size are welcome.

> 🇧🇷 Contribuições em português também são bem-vindas.

## How to contribute

1. Open an [issue](../../issues/new/choose) describing the bug or idea before large changes.
2. Fork the repository and create a branch: `git checkout -b feat/short-description`.
3. Set up the environment:
   ```bash
   uv sync
   ```
4. Make your changes and check them locally:
   ```bash
   uv run ruff check .
   uv run ruff format .
   uv run pytest
   ```
5. Commit using [Conventional Commits](https://www.conventionalcommits.org/), e.g. `feat: add data loader` or `fix: handle empty input`.
6. Open a pull request and fill in the template.

## Guidelines

- Keep pull requests small and focused on one change.
- Add or update tests for any behavior change.
- Never commit data files, trained models, or secrets (`.env`, API keys).

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
