def test_metric2(**kwargs) -> float:
    # only one metric per file is admitted
    # if you want another custom metric create a new file
    return float(1)


def __helper_function(a):
    # Care the underscores '__' are mandatory for helper functions
    # This function won't show as a metric is here only for helping purposes
    return a + 1000
