PYTHON = python3
VENV = venv
PIP = $(VENV)/bin/pip
PY = $(VENV)/bin/python

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install pygame flake8 mypy

run:
	$(PY) main.py

debug:
	$(PY) -m pdb main.py

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf $(VENV)
	find . -name "*.pyc" -delete

lint:
	$(PY) -m flake8 .
	$(PY) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PY) -m flake8 .
	$(PY) -m mypy . --strict