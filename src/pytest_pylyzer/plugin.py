from pytest import Parser, Config

def pytest_addoption(parser: Parser):
    group = parser.getgroup("pylyzer")
    group.addoption(
        "--pylyzer",
        action="store_true",
        help="Run pylyzer.",
    )


def pytest_configure(config: Config):
    """Register the additional marker."""
    config.addinivalue_line(
        "markers", "pylyzer: run pylyzer"
    )
