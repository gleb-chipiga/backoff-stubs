activate := "source .env/bin/activate"

flake8:
    #!/usr/bin/env bash
    {{activate}}
    flake8 --exclude .tox,.env .

mypy:
    #!/usr/bin/env bash
    {{activate}}
    mypy --strict .

isort:
    #!/usr/bin/env bash
    {{activate}}
    isort --line-length 79 --skip .env --skip .mypy_cache --skip .hypothesis \
        --skip .tox .

black: isort
    #!/usr/bin/env bash
    {{activate}}
    black --line-length 79 --extend-exclude="\.env/|\.tox/" .

build:
    #!/usr/bin/env bash
    {{activate}}
    if [ -d dist ]; then rm -rf dist; fi
    python -m build
    rm -rf *.egg-info

upload:
    #!/usr/bin/env bash
    {{activate}}
    twine upload dist/*
    rm -rf dist