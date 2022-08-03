# python-template

[![Build](https://github.com/ionite34/python-template/actions/workflows/build.yml/badge.svg)](https://github.com/ionite34/python-template/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/ionite34/python-template/branch/main/graph/badge.svg)](https://codecov.io/gh/ionite34/python-template)
[![DeepSource](https://deepsource.io/gh/ionite34/python-template.svg/?label=active+issues&show_trend=true&token=U949myD2-vuIl3F-Q8Lbg8iP)](https://deepsource.io/gh/ionite34/python-template/?ref=repository-badge)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ionite34/python-template/main.svg)](https://results.pre-commit.ci/latest/github/ionite34/python-template/main)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Fpython-template.svg?type=shield)](https://app.fossa.com/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Fpython-template?ref=badge_shield)


[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/_)](https://pypi.org/project/_/)
[![PyPI version](https://badge.fury.io/py/_.svg)](https://pypi.org/project/_/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


## Getting started
### 1. Create on GitHub
[![Use Template](https://img.shields.io/badge/use%20this-template-blue?logo=github)](https://github.com/ionite34/python-template/generate)

### 2. Using GitHub CLI
```shell
gh repo create my-project --template ionite34/python-template
```

### 3. Cloning
```shell
git clone https://github.com/ionite34/python-template
```

## Features

### 📦 Dependency Management - [Poetry][PTR]

### 💾 Cached workflow builds for GitHub Actions

### 🧪 Testing and Coverage
- Pre-commit enabled with [pre-commit.ci](https://pre-commit.ci/)
- Uses GitHub Actions with [pytest][PYT], [coverage.py][COV], and [Codecov][CDC]
    > #### [coverage.yml](.github/workflows/coverage.yml)
    > First runs tests and coverage on `Python 3.10` with `Ubuntu`, uploads results to Codecov

    > #### [tests.yml](.github/workflows/tests.yml)
    > If coverage passes, runs 12 extended matrix tests on `Python 3.7 - 3.10` with `Ubuntu, Windows, macOS`

### ⚖️ License Compliance Scan
- Verify that all linked dependencies are compatible with your open-source license type
- Requires repository secret: [`FOSSA_API`][FOSSA_API]

### 🏗️ Automatic Build and Publish to PyPI
- Requires repository secret: [`PYPI_TOKEN`](https://pypi.org/help/#apitoken)
- Action will start on new published releases
- Requires [`tests`](.github/workflows/tests.yml) actions on the branch to be passing

### 🔬 Code quality issues and auto-transforms - [DeepSource](https://deepsource.io/)
- Requires [`DEEPSOURCE_DSN`](https://deepsource.io/)


## Required Repository Tokens
```
PYPI_TOKEN
FOSSA_API
DEEPSOURCE_DSN
```


## Requirements
```
pytest >= 7.1.2
pytest-cov >= 3.0.0
mypy = ~= 0.961
pylint >= 2.14.4
black >= 22.6.0
tox ~= 3.25.1
pre-commit >= 2.20.0
```

## License
The code in this template is released under the [MIT License](LICENSE).

[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Fpython-template.svg?type=large)](https://app.fossa.com/projects/custom%2B31224%2Fgithub.com%2Fionite34%2Fpython-template?ref=badge_large)


[PYT]: https://pypi.org/project/pytest/
[COV]: https://pypi.org/project/coverage/
[CDC]: https://about.codecov.io/
[PTR]: https://python-poetry.org/
[FOSSA_API]: https://docs.fossa.com/docs/api-reference
