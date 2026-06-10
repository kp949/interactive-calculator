# Calculator Project

This project is a basic Python command-line calculator with automated tests.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling
- Simple REPL command-line interface
- Pytest automated tests
- GitHub Actions continuous integration
- 100% test coverage
- Parameterized pytest tests

## Set up the project

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the calculator

```powershell
python calculator.py
```

## Run tests

```powershell
pytest
```

## GitHub Actions

The workflow in `.github/workflows/tests.yml` runs the pytest test suite automatically on each push and pull request.

- Installs project dependencies
- Runs the pytest test suite
- Checks for 100% test coverage
- Fails the build if coverage drops below 100%

The workflow runs automatically on each push and pull request.
