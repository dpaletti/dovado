from statsmodels.nonparametric.kernel_regression import KernelReg
from typing import Dict, Tuple, List
from dovado_rtl.point_evaluation import evaluate, DesignValue, get_metric
from random import randint, shuffle
from dataclasses import dataclass
import dovado_rtl.global_user_selections as gus
import numpy as np


@dataclass
class Example:
    design_point: List[int]
    design_value: DesignValue


examples: List[Example] = []
examples_updated = True


def add_example(example: Example):
    global examples
    global examples_updated
    examples.append(example)
    shuffle(examples)
    examples_updated = True
    print("EXAMPLES: " + str(examples))


def generate_dataset(
    size: int,
    parameters_range: Dict[str, Tuple[int, int]],
    free_parameters: List[str],
):
    for i in range(0, size):
        design_point = []
        for k in free_parameters:
            design_point.append(
                randint(parameters_range[k][0], parameters_range[k][1])
            )
        design_value = evaluate(tuple(design_point))
        add_example(Example(design_point, design_value))


def get_dependent_variable(
    examples: List[Example], metric: Tuple[str, str]
) -> np.ndarray:
    dependent_variable = []
    for example in examples:
        dependent_variable.append(get_metric(example.design_value, metric))
    return np.array(dependent_variable)


def get_independent_variables(
    examples: List[Example], free_parameters: List[str]
) -> np.ndarray:
    independent_variables = []
    for parameter in free_parameters:
        parameter_accumulator = []
        for example in examples:
            parameter_accumulator.append(example.design_point[parameter])
        independent_variables.append(parameter_accumulator)
    return np.array(independent_variables)


estimator = None


def estimate(design_point: List[float], metric: Tuple[str, str]):
    global estimator
    global examples_updated
    if examples_updated:
        independent_variables = get_independent_variables(
            examples, gus.FREE_PARAMETERS
        )
        estimator = KernelReg(
            get_dependent_variable(examples, metric),
            independent_variables,
            "c" * len(independent_variables),
        )
        examples_updated = False
    estimate, _ = estimator.fit(np.array(design_point))
    return estimate[0]
