# here any import works
# e.g. import numpy as np
import numpy as np


def test_metric(**kwargs) -> float:
    # only one metric per file is admitted
    # if you want another custom metric create a new file
    print(kwargs)
    return float(0)


def __helper_function(a):
    # Care the underscores '__' are mandatory for helper functions
    # This function won't show as a metric is here only for helping purposes
    return a + 1000
