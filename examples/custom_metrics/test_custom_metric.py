# here any import works as long as it is installed
# e.g. import numpy as np


def test_metric(**kwargs) -> float:
    return float(__helper_function(kwargs["frequency"]))


def another_test_metric(**kwargs) -> float:
    return 1


def __helper_function(a):
    # all functions starting with '__' won't be accessible as metrics
    return a + 1000
