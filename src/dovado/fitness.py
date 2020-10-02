import math
import typing
import yaml
from pathlib import Path
from functools import lru_cache
from heapq import nlargest
import dovado.point_evaluation as pe
import dovado.estimation as es
import numpy as np
from typing import Tuple, List
import dovado.global_user_selections as gus

CONFIG = yaml.safe_load(Path("config.yaml").open())


@lru_cache
def fitness(design_point: Tuple[int], metric: str):
    # design_point is a Tuple because lists are unhashable
    # while caching is allowed only with hashable parameters
    print(
        "Distance: "
        + str(_nth_nearest_distance(design_point, es.examples, CONFIG["N"]))
    )
    if (
        _nth_nearest_distance(design_point, es.examples, CONFIG["N"]) == 0
    ) or (
        _nth_nearest_distance(design_point, es.examples, CONFIG["N"])
        > CONFIG["THRESHOLD"]
    ):
        full_design_value = pe.evaluate(design_point)
        design_value = pe.get_metric(full_design_value, "metric_1")
        if (
            _nth_nearest_distance(design_point, es.examples, CONFIG["N"])
            > CONFIG["THRESHOLD"]
        ):
            es.add_example(
                es.Example(
                    dict(zip(gus.FREE_PARAMETERS, design_point)),
                    full_design_value,
                )
            )
    else:
        design_value = es.estimate(design_point, metric)
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
        distances.append(
            _distance(design_point, list(example.design_point.values()))
        )
    try:
        return nlargest(n, distances)[n]
    except Exception:
        return nlargest(n, distances)[-1]
