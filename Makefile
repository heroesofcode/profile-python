setup: ## Install dependencies
	poetry update
	poetry config virtualenvs.in-project true
	poetry install
