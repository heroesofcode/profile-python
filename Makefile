setup: ## Dependencies
	poetry update
	poetry install
	poetry config virtualenvs.in-project true

test: ## Run tests and
	poetry run pytest -vv --cov-report=xml --cov=profile_python tests/