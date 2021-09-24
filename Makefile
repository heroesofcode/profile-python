.DEFAULT_GOAL := help

setup: ## Install dependencies
	python -m pip install --upgrade pip
        pip install setuptools wheel twine

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		sort |\
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
