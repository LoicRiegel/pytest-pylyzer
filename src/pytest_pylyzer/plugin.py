from pathlib import Path

import pytest
from .run import run_pylyzer
from .exceptions import PylyzerError


class PylyzerItem(pytest.Item):
    name = "pylyzer"

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(name=name, *args, **kwargs)
        self.add_marker("pylyzer")

    def runtest(self):
        self.handler(path=self.fspath)

    def reportinfo(self):
        return (self.fspath, None, "")

    def handler(self, path):
        return run_pylyzer(path)


class PylyzerFile(pytest.File):
    def collect(self) -> tuple[PylyzerItem]:
        return (PylyzerItem.from_parent(self, name="pylyzer"),)


def pytest_addoption(parser: pytest.Parser):
    group = parser.getgroup("pylyzer")
    group.addoption(
        "--pylyzer",
        action="store_true",
        help="Run pylyzer.",
    )


def pytest_configure(config: pytest.Config):
    """Register the additional marker."""
    config.addinivalue_line("markers", "pylyzer: run pylyzer")


def pytest_collect_file(
    file_path: Path, parent: pytest.Collector
) -> PylyzerFile | None:
    """Return the PylyzerFile collector or None if not applicable."""
    config = parent.config
    if not config.option.pylyzer:
        return
    if file_path.suffix != ".py":
        return None
    return PylyzerFile.from_parent(parent, path=file_path, name="pylyzer")


def pytest_exception_interact(
    node: pytest.Item | pytest.Collector,
    call: pytest.CallInfo,
    report: pytest.CollectReport | pytest.TestReport,
) -> None:
    if call.excinfo is not None and isinstance(call.excinfo.value, PylyzerError):
        report.longrepr = str(call.excinfo.value)
