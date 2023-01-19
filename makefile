venv:
	python3.11 -m venv venv
	venv/bin/python -m pip install --upgrade pip

requirements: venv
	venv/bin/python -m pip install --upgrade -r requirements.txt

test-requirements: venv
	venv/bin/python -m pip install --upgrade -r tests/__pypackages__/requirements.txt

test:
	python3.11 tests/demo.py

build: venv
	rm -fr dist
	find . -depth -name '*.egg-info' -exec rm -fr {} \;
	venv/bin/python -m build

pypi-test: build
	venv/bin/python -m twine upload --repository testpypi dist/*

pypi: build
	venv/bin/python -m twine upload dist/*
