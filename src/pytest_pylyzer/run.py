from subprocess import Popen

from .exceptions import PylyzerCheckFailed


def run_pylyzer(path):
    command = ["pylyzer", path]
    with Popen(command) as child:
        pass

    if child.returncode == 1:
        raise PylyzerCheckFailed(path)
