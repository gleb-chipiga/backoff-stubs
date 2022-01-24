build:
	rm -rf dist
	python -m build
	rm -rf aiojobs_stubs.egg-info
