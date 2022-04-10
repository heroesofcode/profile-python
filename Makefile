setup: ## Dependencies
	poetry update
	poetry install
	poetry config virtualenvs.in-project true

test: ## Run tests
	poetry run pytest -vv --cov-report=xml --cov=profile_python tests/

deploy: ## Deploy package
	poetry config pypi-token.pypi $(token)
	poetry build
	poetry publish
