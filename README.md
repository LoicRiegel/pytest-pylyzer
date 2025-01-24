# pytest-pylyzer

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
The plugin will run one `pylyzer` check test per file and fail if `pylyzer` detects any errors in that file.

## Contributing

Contributions are very welcome. 

Use ``tox`` to make sure that the tests pass against all supported python versions and that the code is linted and formatted.

## License

Distributed under the terms of the [MIT](./LICENSE) license. This is free and open source software.
