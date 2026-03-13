.PHONY: all mypy lint format format-check test

all: sync mypy lint format-check test

sync:
	uv sync --group dev

mypy:
	uv run mypy --strict .

lint:
	uv run ruff check .

format:
	uv run ruff check --fix .
	uv run ruff format .

format-check:
	uv run ruff format --check .

test:
	uv run pytest
