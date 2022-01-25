isort:
	isort backoff-stubs/__init__.pyi setup.py

build:
	rm -rf dist
	python -m build
	rm -rf *.egg-info

upload:
	twine upload dist/*
