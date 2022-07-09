PACKAGE=src
PACKAGE_PATH=./$(PACKAGE)
TESTS=tests
ALLOWED = ./$(PACKAGE) ./tests

POETRY=poetry
PYTEST=$(POETRY) run pytest
MYPY=$(POETRY) run mypy --ignore-missing-imports
BLACK=$(POETRY) run black  --line-length=110
ISORT=$(POETRY) run isort

FLAKE8=$(POETRY) run flake8 --max-line-length=110
PYLINT=$(POETRY) run pylint  --errors-only


install:
	$(POETRY) install

update:
	$(POETRY) update

test: install
	$(MYPY) $(ALLOWED)
	$(PYTEST) -vv

lint:
	$(ISORT) $(ALLOWED)
	$(BLACK) $(ALLOWED)
	$(FLAKE8) $(ALLOWED)
	$(PYLINT) $(ALLOWED)

ready_for_commit: lint test
