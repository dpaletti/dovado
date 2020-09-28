import math
import typing
import yaml
import random
from pathlib import Path
from functools import lru_cache
from heapq import nlargest
from dataclasses import dataclass
import dovado.point_evaluation as pe
from dovado.estimation import estimate

CONFIG = yaml.safe_load(Path("config.yaml").open())

examples = []


@dataclass
class Example:
    design_point: dict
    design_value: dict


def _add_example(example: Example):
    examples.append(example)
    random.shuffle(examples)


@lru_cache
def fitness(design_point):
    if _nth_nearest_distance(design_point, examples, CONFIG["N"]) == 0:
        # the point has already been evaluated thus cached
        return pe.evaluate(design_point)

    if (
        _nth_nearest_distance(design_point, examples, CONFIG["N"])
        > CONFIG["THRESHOLD"]
    ):
        _add_example(design_point)
    return estimate(design_point)


def _distance(design_point_1, design_point_2) -> typing.Float:
    if design_point_1.keys() != design_point_2.keys():
        raise ValueError(
            "Mismatching design points: different indices considered"
        )
    squared_subtractions = []
    for k in design_point_1.keys():
        squared_subtractions.append(
            math.pow(design_point_1.get(k) - design_point_2.get(k), 2,)
        )
    return math.sqrt(
        math.fsum(squared_subtractions) / len(squared_subtractions)
    )


def _nth_nearest_distance(
    design_point, examples: typing.Set[pe.DesignValue], n: typing.Integer,
) -> typing.Float:
    distances = []
    for example in examples:
        distances.append(_distance(design_point, example))
    nlargest(n, distances)
