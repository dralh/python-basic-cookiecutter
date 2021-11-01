# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

{{ cookiecutter.project_name }} requires [Python](https://www.python.org/downloads/) v3.8 to run.
If you want to run the project in an isolated mode install [Virutalenv](https://pypi.org/project/virtualenv/).

Install the dependencies.

For development environments...
```sh
virtualenv venv
source ./venv/bin/activate
pip install -e ".[dev]"
```

## DevTools

{{ cookiecutter.project_name }} uses some tools to keep code readable.

| Tool | Version | Command | Repository |
| ------ | ------ | ------ | ------ |
| Black | 21.10b0 | black . | https://github.com/psf/black |
| Isort | 5.9.3 | isort . | https://github.com/PyCQA/isort |
| Pre-commit | 2.15.0 | pre-commit run | https://github.com/pre-commit/pre-commit |

#### Building for source

For development release:

```sh
python setup.py build_dev
```

For production release:

```sh
python setup.py build_prod
```
