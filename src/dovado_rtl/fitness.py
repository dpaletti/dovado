import math
from pathlib import Path
from functools import lru_cache
from heapq import nlargest
import dovado_rtl.point_evaluation as pe
import dovado_rtl.estimation as es
from dovado_rtl.config import get_config
import numpy as np
from typing import Tuple, List


threshold: int = 0

estimate_working = True


@lru_cache
def fitness(design_point: Tuple[int], metric: Tuple[str, str]):
    # design_point is a Tuple because lists are unhashable
    # while caching is allowed only with hashable parameters
    global estimate_working
    print(
        "Nth nearest distance: "
        + str(
            _nth_nearest_distance(design_point, es.examples, get_config("N"))
        )
    )
    if (
        (
            _nth_nearest_distance(design_point, es.examples, get_config("N"))
            == 0
        )
        or (
            _nth_nearest_distance(design_point, es.examples, get_config("N"))
            > threshold
        )
        or (not estimate_working)
    ):
        print("Fitness calling Vivado directly")
        full_design_value = pe.evaluate(design_point)
        design_value = pe.get_metric(full_design_value, metric)
        if (
            _nth_nearest_distance(design_point, es.examples, get_config("N"))
            > threshold
        ) and estimate_working:

            if any(
                np.isinf(v) for v in full_design_value.utilisation.values()
            ) or np.isinf(full_design_value.negative_max_frequency):
                es.add_example(
                    es.Example(design_point, full_design_value, True)
                )
            else:
                es.add_example(
                    es.Example(design_point, full_design_value, False)
                )
            set_threshold(es.examples)
    else:
        print("Fitness estimating")
        design_value = es.estimate(design_point, metric)
        if not design_value:
            print("Disabling estimator")
            estimate_working = False
            full_design_value = pe.evaluate(design_point)
            design_value = pe.get_metric(full_design_value, metric)

    print("design_point: " + str(design_point))
    print("metric: " + str(metric))
    print("Design Value: " + str(design_value))
    return design_value


def _distance(design_point_1: List[int], design_point_2: List[int]) -> float:
    if len(design_point_1) != len(design_point_2):
        raise ValueError("Mismatching design points: different dimensionality")
    return math.sqrt(
        np.sum(
            np.power(
                np.subtract(
                    np.array(design_point_1), np.array(design_point_2)
                ),
                np.array([2] * len(design_point_1)),
            )
        )
        / len(design_point_1)
    )


def _nth_nearest_distance(
    design_point: List[int], examples: List[es.Example], n: int,
) -> float:
    distances = []
    for example in examples:
        distances.append(_distance(design_point, example.design_point))

    try:
        return nlargest(n, distances)[n - 1]
    except Exception:
        return nlargest(n, distances)[-2]


def _mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def set_threshold(examples):
    global threshold
    distances = []
    for example in examples:
        distances.append(
            _nth_nearest_distance(
                example.design_point, examples, get_config("N")
            )
        )
    print("Distances for threshold: " + str(distances))
    threshold = int(round(_mean(distances)))
    print("Set Threshold: " + str(threshold))
