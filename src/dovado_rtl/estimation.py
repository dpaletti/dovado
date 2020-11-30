from statsmodels.nonparametric.kernel_regression import KernelReg
from collections import OrderedDict
from typing import Tuple, List
from random import randint, shuffle
import numpy as np
from dovado_rtl.point_evaluation import DesignPointEvaluator, DesignValue


class Example:
    def __init__(self, design_point: List[int], design_value: DesignValue):
        self.design_point: List[int] = design_point
        self.design_value: DesignValue = design_value


class Estimator:
    def __init__(
        self,
        design_point_evaluator: DesignPointEvaluator,
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        dataset_size: int,
    ):
        self.__examples: List[Example] = []
        self.__examples_updated: bool = True
        self.__estimator = None
        self.__design_point_evaluator: DesignPointEvaluator = design_point_evaluator
        self.__dataset_size: int = dataset_size
        self.__generate_dataset(free_parameters_range,)

    def estimate(
        self, design_point: List[float], metric: Tuple[str, str]
    ) -> float:
        if self.__examples_updated:
            independent_variables = self.__get_independent_variables()
            self.__estimator = KernelReg(
                self.__get_dependent_variable(metric),
                independent_variables,
                "c" * len(independent_variables),
            )
            self.__examples_updated = False
        estimate, _ = self.__estimator.fit(np.array(design_point))
        return estimate[0]

    def add_example(self, example: Example) -> None:
        self.__examples.append(example)
        shuffle(self.__examples)
        self.__examples_updated = True

    def __generate_dataset(
        self, parameters_range: "OrderedDict[str, Tuple[int, int]]",
    ) -> None:
        for _ in range(0, self.__dataset_size):
            design_point = []
            for k in parameters_range.keys():
                design_point.append(
                    randint(parameters_range[k][0], parameters_range[k][1])
                )
            design_value = self.__design_point_evaluator.evaluate(
                tuple(design_point)
            )
            self.add_example(Example(design_point, design_value))

    def __get_dependent_variable(
        self, metric: Tuple[str, str]
    ) -> "np.ndarray":
        dependent_variable = []
        for example in self.__examples:
            dependent_variable.append(
                DesignPointEvaluator.get_metric(example.design_value, metric)
            )
        return np.array(dependent_variable)

    def __get_independent_variables(self) -> "np.ndarray":
        independent_variables = []
        for example in self.__examples:
            independent_variables.append(example.design_point)
        return np.array(independent_variables)

    def get_examples(self):
        return self.__examples
