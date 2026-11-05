POETRY ?= poetry

.PHONY: format
format: ## Format code with ruff
	$(POETRY) run ruff format
	$(POETRY) run ruff check

.PHONY: lint
lint: ## Run linting checks (ruff, flake8, mypy)
	$(POETRY) run ruff check --exit-non-zero-on-fix
	$(POETRY) run ruff format --check --diff
	$(POETRY) run flake8 .

.PHONY: type-check
type-check: ## Run type checking (mypy)
	$(POETRY) run mypy src/sanya

.PHONY: unit
unit: ## Run unit tests with pytest
	$(POETRY) run pytest

.PHONY: sort
sort:
	$(POETRY) run python3 src/sanya/data/sort.py

.PHONY: test
test: lint type-check unit ## Run all checks (lint, unit, package)