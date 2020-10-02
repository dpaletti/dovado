from typing import List, Dict, Tuple

FREE_PARAMETERS_RANGE: Dict[str, Tuple[int, int]] = None
METRICS: List[Tuple[str, str]] = None
FREE_PARAMETERS: List[str] = None


def set_free_parameters_range(free_parameters_range):
    global FREE_PARAMETERS_RANGE
    FREE_PARAMETERS_RANGE = free_parameters_range


def set_metrics(metrics):
    global METRICS
    METRICS = metrics


def set_free_parameters(free_parameters):
    global FREE_PARAMETERS
    FREE_PARAMETERS = free_parameters
    print("FREE PARAM: " + str(FREE_PARAMETERS))
