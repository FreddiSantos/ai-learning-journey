# 🧭 AI Learning Journey

[![CI](https://github.com/FreddiSantos/ai-learning-journey/actions/workflows/ci.yml/badge.svg)](https://github.com/FreddiSantos/ai-learning-journey/actions/workflows/ci.yml)
[![Update timeline](https://github.com/FreddiSantos/ai-learning-journey/actions/workflows/update-timeline.yml/badge.svg)](https://github.com/FreddiSantos/ai-learning-journey/actions/workflows/update-timeline.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A public log of how I'm learning Artificial Intelligence as a **Civil Engineering student at UFSCar**: courses, projects, readings and milestones.

> 🇧🇷 Registro público da minha jornada em IA como estudante de Engenharia Civil na UFSCar.

## 🗺️ Timeline

<!-- TIMELINE:START -->
🏁 3 milestones · 🚀 4 projects

### Ongoing

- 🏁 Member of LIA — Artificial Intelligence Lab at UFSCar
- 🏁 Member of PET Engenharia Civil at UFSCar

### 2026

- **Oct 2026** · 🚀 [Started python-project-template](https://github.com/FreddiSantos/python-project-template) — Template for Python and data science projects: CI, linting, tests and community files ready to go.
- **Oct 2026** · 🚀 [Started github-setup](https://github.com/FreddiSantos/github-setup) — Versioned configuration for my GitHub workflow: bootstrap, templates and automation.
- **Oct 2026** · 🚀 [Started ai-learning-journey](https://github.com/FreddiSantos/ai-learning-journey) — My public log of learning AI as a civil engineering student: courses, projects, readings and milestones.
- **Oct 2026** · 🏁 [Set up a professional GitHub workflow](https://github.com/FreddiSantos/github-setup) — CI, security scanning, Conventional Commits and automated releases in every project.
- **Oct 2026** · 🚀 [Released python-project-template v0.2.0](https://github.com/FreddiSantos/python-project-template/releases/tag/v0.2.0)
<!-- TIMELINE:END -->

## How this works

- Manual entries (courses, readings, milestones) live in [`journey.toml`](journey.toml).
- New public repositories and releases on my GitHub are added automatically.
- A [weekly GitHub Action](.github/workflows/update-timeline.yml) rebuilds the timeline above, and it also runs whenever `journey.toml` changes.

Run it locally:

```bash
uv sync
uv run python -m journey README.md            # with GitHub data
uv run python -m journey README.md --offline  # only journey.toml
```

## 💬 Suggestions

Know a good course, paper or project idea at the intersection of **AI and civil engineering**? Share it in [Discussions](https://github.com/FreddiSantos/ai-learning-journey/discussions).

## License

[MIT](LICENSE) © Pedro Freddi
