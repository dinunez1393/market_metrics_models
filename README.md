Start alembic project: alembic init alembic

Generate migration: uv run alembic revision --autogenerate -m "initial_tables"
Apply migration: uv run alembic upgrade head

uv install packages:
-- Optional if access denied error appears, run this command first:
Remove-Item -Recurse -Force ".\.venv\Lib\site-packages\market_metrics_allocator-0.1.0.dist-info"

uv add pandas
uv sync (install all dependencies in pyproject.toml)
uv add git+https://github.com/dinunez1393/market_metrics_models.git (install from github repo)

Generate a new python project with standard layour: src/project_name (pkh):
uv init --lib <project-name>
