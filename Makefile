setup: ## Dependencies
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

test: ## Run tests and
	pip install pytest
	pytest
	pip install pytest-cov
	pytest --cov=school_report