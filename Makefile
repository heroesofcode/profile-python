setup: ## Dependencies
	poetry update
	poetry install
	poetry config virtualenvs.in-project true

test: ## Run tests
	python -m pip install --upgrade pip
	pip install pytest-cov
	poetry run pytest --cov=profile_python tests/

setup_deploy: ## Dependencies deploy
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

deploy: ## Deploy package
	python setup.py sdist bdist_wheel
	twine upload dist/*
