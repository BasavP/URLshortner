# uv Cheat Sheet

Quick reference for common `uv` commands in this project.

## Setup
```cmd
uv venv
```
Create a virtual environment in `.venv`.

```cmd
.venv\Scripts\activate
```
Activate the virtual environment in Windows `cmd`.

```cmd
uv sync
```
Install dependencies from `pyproject.toml` and sync the environment.

## Run
```cmd
uv run uvicorn src.main:app --reload
```
Start the FastAPI app locally with auto-reload.

```cmd
uv run pytest
```
Run the test suite.

```cmd
uv run ruff check .
```
Check linting and import issues.

```cmd
uv run ruff check . --fix
```
Auto-fix issues that Ruff can safely correct.

```cmd
uv run ruff format .
```
Format Python files.

## Add Dependencies
```cmd
uv add fastapi
```
Add a runtime dependency.

```cmd
uv add --dev pytest
```
Add a development dependency.

## Useful Extras
```cmd
uv --version
```
Confirm `uv` is installed and available on PATH.

```cmd
uv pip list
```
List installed packages in the active environment.

## Typical Workflow
```cmd
uv venv
.venv\Scripts\activate
uv sync
uv run pytest
uv run ruff check . --fix
uv run uvicorn src.main:app --reload
```
