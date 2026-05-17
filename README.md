# URLshortner

Production-style FastAPI scaffold for a URL shortener service.

## Stack
- Python 3.11+
- FastAPI
- PostgreSQL
- Redis
- uv (dependency management)
- Ruff + Pytest

## Project Structure
`src/`
- `api/` API routes
- `core/` settings/configuration
- `db/` database setup
- `models/` ORM models
- `schemas/` request/response schemas
- `services/` business logic

## Local Setup
1. Install uv:
   ```bash
   pip install uv
   ```
2. Create virtual environment and sync dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```
3. Run API:
   ```bash
   uv run uvicorn src.main:app --reload
   ```
4. Open health endpoint:
   - http://127.0.0.1:8000/health

## Tooling
- Lint:
  ```bash
  uv run ruff check .
  ```
- Format:
  ```bash
  uv run ruff format .
  ```
- Tests:
  ```bash
  uv run pytest
  ```

## Docker Compose
Run app + postgres + redis:
```bash
docker compose up --build
```
