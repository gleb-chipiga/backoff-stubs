flake8:
	flake8 --exclude .tox,.env .

mypy:
	mypy --strict .

isort:
	isort -s .env -s .tox .

build:
	if [ -d dist ]; then rm -rf dist; fi
	python -m build
	rm -rf *.egg-info

upload:
	twine upload dist/*
	rm -rf dist
