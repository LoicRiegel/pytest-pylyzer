

def test_help_message(pytester):
    result = pytester.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        "pylyzer:",
        "*--pylyzer*Run pylyzer.",
    ])


def test_markers(pytester):
    result = pytester.runpytest(
        '--markers',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        "@pytest.mark.pylyzer: run pylyzer"
    ])