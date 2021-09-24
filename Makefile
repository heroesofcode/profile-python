setup: ## Dependencies
	python -m pip install --upgrade pip
	pip install setuptools wheel twine
	pip install pytest
	pip install pytest-cov

tests: ## Run tests and
	pytest
	pytest --cov=profile_python tests/