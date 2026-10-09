# Secure Password Generator

[![CI](https://github.com/guirodrigues0987/gerador-senhas-ia/actions/workflows/ci.yml/badge.svg)](https://github.com/guirodrigues0987/gerador-senhas-ia/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Python MVP that generates passwords with a focus on cryptographic security, command-line usability and process documentation, built as a lab project on AI-assisted development with generative AI.

## Setup

1. Create a virtual environment at the project root:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   ```bash
   # Linux / macOS
   source venv/bin/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```
3. Upgrade `pip` and install the dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

```bash
# Default length (16 characters)
python main.py

# 20 characters
python main.py --length 20

# Letters and numbers only
python main.py --no-symbols

# 24 characters, no numbers
python main.py --length 24 --no-numbers
```

| Flag | Description |
|---|---|
| `--length N` | Password length (default: 16) |
| `--no-letters` | Exclude ASCII letters |
| `--no-numbers` | Exclude digits |
| `--no-symbols` | Exclude punctuation symbols |

The generator guarantees at least one character from each enabled character set.

## Tech stack

- Python 3.11+
- Standard library only at runtime: `secrets`, `string`, `argparse`
- Tests: `pytest`
- Linting and formatting: [Ruff](https://docs.astral.sh/ruff/)
- Code assistant used during development: GPT-5.5 (see [`docs/prompt_log.md`](docs/prompt_log.md))

## Project structure

See [`docs/project_structure.md`](docs/project_structure.md).

## Tests

```bash
pytest
```

The unit tests cover:

- Password generation with the default length.
- Password generation with a custom length.
- Rejection of invalid lengths.
- Rejection when no character set is enabled.
- Rejection when the length is smaller than the number of enabled character sets.

## Limitations and next steps

Current limitations:

- No graphical interface.
- No history of generated passwords.
- No export to file or integration with password managers.
- No advanced complexity policy (e.g. minimum count per character type).
- No persisted user settings.

Possible next steps:

- Simple graphical interface.
- Optional local history.
- Password strength validation.
- Copy to clipboard.
- Generation presets.

## Releases

The current stable version is `v1.0.0`.

## Credits and license

Developed as an MVP for a generative AI lab. Released under the [MIT License](LICENSE).
