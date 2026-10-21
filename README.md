<!--
TEMPLATE — checklist ao criar um projeto novo (apague este comentário no fim):
1. Substitua todos os trechos entre <> neste README e no CITATION.cff.
2. Renomeie src/project_name e ajuste "name" e "module-name" no pyproject.toml e "source" em [tool.coverage.run].
3. Rode `uv lock` para atualizar o uv.lock.
4. Adicione topics ao repositório (ex.: machine-learning, python, civil-engineering).
-->


# <Project name>

[![CI](https://github.com/FreddiSantos/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/FreddiSantos/<repo>/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

<One sentence: what this project does and for whom.>

> 🇧🇷 <Resumo de uma linha em português.>

## Problem

<What problem does this solve? Why does it matter? Include context from civil engineering or AI if relevant.>

## Solution

<How the project approaches the problem. Add an architecture diagram or a screenshot/GIF if possible.>

## Getting started

Requirements: [uv](https://docs.astral.sh/uv/) (it installs the right Python version automatically).

```bash
git clone https://github.com/FreddiSantos/<repo>.git
cd <repo>
uv sync
uv run pytest
```

<How to run the main script or notebook, e.g. `uv run python -m project_name`.>

If the project uses API keys, copy `.env.example` to `.env` and fill it in. The `.env` file is never committed.

### Project structure

```text
├── data/            # raw data (not versioned, see data/README.md)
├── notebooks/       # exploration notebooks
├── src/project_name # source code
├── tests/           # automated tests
└── pyproject.toml   # dependencies and tool settings
```

### Data

<Where the data comes from, its license, and how to download it. Raw data is not versioned — see [data/README.md](data/README.md).>

### Reproducibility

- Dependencies are pinned in `uv.lock`.
- Random seed: `SEED` in `.env` (default `42`), applied in <where it is set>.
- Hardware used for the reported results: <CPU/GPU, RAM>.

## Stack

<Python · pandas · PyTorch · ...>

## Results

<Metrics, charts or sample outputs. Compare with a baseline when possible.>

## Roadmap

- [ ] <Next step>
- [ ] <Next step>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). This project follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Citation

If this project helps your work, please cite it using the **Cite this repository** button (generated from [CITATION.cff](CITATION.cff)).

## License

[MIT](LICENSE) © Pedro Freddi
