from statsmodels.nonparametric.kernel_regression import KernelReg
from typing import Dict, Tuple, List
from dovado.point_evaluation import evaluate, DesignValue, get_metric
import dovado.global_user_selections as gus
from random import randint, shuffle
from dataclasses import dataclass
import dovado.global_user_selections as gus
import numpy as np


@dataclass
class Example:
    design_point: List[int]
    design_value: DesignValue
    is_infinite: bool = False


examples: List[Example] = []
held_back_examples: List[Example] = []
examples_updated = True


def _is_design_value_infinite(design_value):
    if any(np.isinf(v) for v in design_value.utilisation.values()) or np.isinf(
        design_value.negative_max_frequency
    ):
        return True
    return False


def _replace_infinite_values():
    global examples
    print("Replacing infinite values")
    for example in examples:
        if example.is_infinite:
            example.design_value.negative_max_frequency = _get_max(True, None)
            for metric in gus.METRICS:
                example.design_value.utilisation[metric] = _get_max(
                    False, metric
                )


def add_example(example: Example):
    global examples
    global examples_updated
    if not (
        any(np.isnan(v) for v in example.design_value.utilisation.values())
        or np.isnan(example.design_value.negative_max_frequency)
    ):
        examples.append(example)
        shuffle(examples)
        _replace_infinite_values()
        examples_updated = True
    else:
        print("Skipping NaN values")
    print("Last example added " + str(examples[-1]))


def _get_max(is_frequency, metric):
    if is_frequency:
        return max(
            example.design_value.negative_max_frequency
            for example in examples
            if example.design_value.negative_max_frequency != np.inf
        )
    return max(
        example.design_value.utilisation[metric]
        for example in examples
        if example.design_value.utilisation[metric] != np.inf
    )


def generate_dataset(
    size: int,
    parameters_range: Dict[str, Tuple[int, int]],
    free_parameters: List[str],
):
    global held_back_examples
    for i in range(0, size):
        design_point = []
        for k in free_parameters:
            design_point.append(
                randint(parameters_range[k][0], parameters_range[k][1])
            )
        design_value = evaluate(tuple(design_point))
        if _is_design_value_infinite(design_value):
            if len(examples) > 0:
                add_example(Example(design_point, design_value, True))
            else:
                print("Holding back invalid point until a valid one is found")
                held_back_examples.append(
                    Example(design_point, design_value, True)
                )

        else:
            add_example(Example(design_point, design_value, False))
            if len(held_back_examples) > 0:
                print("Adding held back points to the dataset")
                for held_back in held_back_examples:
                    add_example(held_back)
                held_back_examples = []
    if len(examples) == 0:
        raise Exception(
            "Values found while generating random dataset all produced"
            + " an error in Vivado, try re-running with a larger dataset size"
            + " or with more accurate bounds for parameters"
        )


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
            parameter_accumulator.append(
                dict(zip(gus.FREE_PARAMETERS, example.design_point))[parameter]
            )
        independent_variables.append(parameter_accumulator)
    return np.array(independent_variables)


estimator = None


def estimate(design_point: List[float], metric: Tuple[str, str]):
    global estimator
    global examples_updated
    if examples_updated:
        try:
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
        except Exception as e:
            print("Estimation algorithm failed due to: " + str(e))
            return None
