# pytest-pylyzer

[![check](https://github.com/LoicRiegel/pytest-pylyzer/actions/workflows/check.yml/badge.svg)](https://github.com/LoicRiegel/pytest-pylyzer/actions/workflows/check.yml)
[![pypi latest version](https://img.shields.io/pypi/v/pytest-pylyzer.svg)](https://pypi.python.org/pypi/pytest-pylyzer)
[![pypi versions](https://img.shields.io/pypi/pyversions/pytest-pylyzer.svg)](https://pypi.python.org/pypi/pytest-pylyzer)

A [pytest](https://docs.pytest.org/en/stable/) plugin to run [pylyzer](https://github.com/mtshiba/pylyzer), a static code analyzer / language server for Python, written in Rust.

## Installation

```
pip install pytest-pylyzer
```

Or include `pytest-pylyzer` in your project's dev-dependencies.

## Usage

```
pytest --pylyzer
```

The plugin will run `pylyzer` against all python files and fail if any error is detected.

## Contributing

Contributions are very welcome.

Use ``tox`` to make sure that the tests pass against all supported python versions and that the code is linted and formatted.

## License

Distributed under the terms of the [MIT](./LICENSE) license. This is free and open source software.
