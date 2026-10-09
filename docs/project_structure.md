# Project Structure

```text
.
├── .github/              # CI workflow and pull request template
├── docs/                 # Technical and process documentation
├── src/
│   └── password_generator.py
├── tests/
│   └── test_password_generator.py
├── main.py               # Command-line interface
├── pyproject.toml        # Ruff and pytest configuration
└── requirements.txt
```

## Purpose

- `src/`: main source code.
- `tests/`: automated tests with `pytest`.
- `docs/`: technical and process documentation, including the prompt log.
- `main.py`: command-line entry point built on `argparse`.
