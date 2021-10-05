setup: ## Dependencies
	python -m pip install --upgrade pip
	pip install setuptools wheel twine
	pip install pytest
	pip install pytest-cov

test: ## Run tests
	pytest
	pytest --cov=profile_python tests/

setup_deploy: ## Dependencies deploy
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

deploy: ## Deploy package
	python setup.py sdist bdist_wheel
	twine upload dist/*
