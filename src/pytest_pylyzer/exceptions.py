from pathlib import Path


class PylyzerError(Exception):
    """Pytest-pylyzer base error."""


class PylyzerCheckFailed(PylyzerError):
    """Error detected in file by Pylyzer."""

    def __init__(self, file: Path) -> None:
        super().__init__(f"Error(s) detected by Pylyzer in {file}")
        self.file = file
