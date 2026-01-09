# Agent Configuration -eo_lib

## 🏗 Technical Stack
- **Language**: Python 3.8+
- **Build System**: Setuptools (see `setup.py`)
- **Main Dependencies**: Playwright
- **Test Framework**: Pytest
- **Linting Tools**: Black, Flake8, isort

## 📂 Project Structure Map
- `src/dgp_cnpq_lib/__init__.py`: Package initialization.
- `src/dgp_cnpq_lib/core.py`: Main Crawler logic.
- `src/dgp_cnpq_lib/extractors.py`: Parsing helper functions.
- `src/dgp_cnpq_lib/__main__.py`: CLI entry point.
- `tests/`: Test suite.
- `README.md`: Project documentation.
- `setup.py`: Package configuration.

## ⚙️ Environment Commands
- **Install**: `pip install .`
- **Run**: `python -m dgp_cnpq_lib <url>`
- **Lint**: `flake8 src tests`
- **Format**: `black src tests && isort src tests`
- **Pre-commit**: `lefthook run pre-commit`
- **Bump Version**: `python scripts/bump_version.py [major|minor|patch]`

## 📦 Distribution Standards
- Adhere to SemVer 2.0.0.
- Minimal external dependencies.
- Unified Domain/ORM models (DRY).

## 📝 Governance Templates
Use these patterns for all new issues:
- **Epic**: [.agent/templates/epic.md](.agent/templates/epic.md)
- **User Story**: [.agent/templates/user_story.md](.agent/templates/user_story.md)
- **Task**: [.agent/templates/task.md](.agent/templates/task.md)
