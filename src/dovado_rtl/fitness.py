import math
from functools import lru_cache
from heapq import nlargest
from dovado_rtl.simple_types import Metric, Example
from dovado_rtl.estimation import Estimator
from dovado_rtl.point_evaluation import DesignPointEvaluator
from dovado_rtl.config import Configuration
import numpy as np
from typing import Tuple, List

from dovado_rtl.abstract_classes import AbstractFitnessEvaluator


class FitnessEvaluator(AbstractFitnessEvaluator):
    def __init__(
        self,
        estimator: Estimator,
        evaluator: DesignPointEvaluator,
        config: Configuration,
    ):
        self.threshold: int = 0
        self.estimate_working: bool = True
        self.estimator: Estimator = estimator
        self.evaluator: DesignPointEvaluator = evaluator
        self.config: Configuration = config
        self.__set_threshold(self.estimator.get_examples())

    @lru_cache()
    def fitness(self, design_point: Tuple[int, ...], metric: Metric):
        # design_point is a Tuple because lists are unhashable
        # and caching is allowed only with hashable parameters

        sample_distance = self.__nth_nearest_distance(
            list(design_point),
            self.estimator.get_examples(),
            int(self.config.get_config("N")),
        )
        print("Nth nearest distance: " + str(sample_distance))
        if (
            (sample_distance == 0)
            or (sample_distance > self.threshold)
            or (not self.estimate_working)
        ):
            print("Fitness calling Vivado directly")
            full_design_value = self.evaluator.evaluate(design_point)
            design_value = full_design_value.value[metric]
            if self.estimate_working:
                self.estimator.add_example(
                    Example(list(design_point), full_design_value)
                )
                self.__set_threshold(self.estimator.get_examples())
        else:
            print("Fitness estimating")
            design_value = self.estimator.estimate(list(design_point), metric)
            if not design_value:
                print("Disabling estimator")
                self.estimate_working = False
                full_design_value = self.evaluator.evaluate(design_point)
                design_value = full_design_value.value[metric]
        print("design_point: " + str(design_point))
        print("metric: " + str(metric))
        print("Design Value: " + str(design_value))
        return design_value

    @staticmethod
    def __distance(
        design_point_1: List[int], design_point_2: List[int]
    ) -> float:
        if len(design_point_1) != len(design_point_2):
            raise ValueError(
                "Mismatching design points: different dimensionality"
            )
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

    def __nth_nearest_distance(
        self, design_point: List[int], examples: List[Example], n: int,
    ) -> float:
        distances = []
        for example in examples:
            distances.append(
                self.__distance(design_point, example.design_point)
            )

        largest_list = nlargest(n, distances)
        if len(largest_list) > n - 1:
            return largest_list[n - 1]
        else:
            return largest_list[-2]

    @staticmethod
    def __mean(numbers: List[float]) -> float:
        return float(sum(numbers)) / max(len(numbers), 1)

    def __set_threshold(self, examples: List[Example]) -> None:
        distances = []
        for example in examples:
            distances.append(
                self.__nth_nearest_distance(
                    example.design_point,
                    examples,
                    int(self.config.get_config("N")),
                )
            )
        print("Distances for threshold: " + str(distances))
        self.threshold = int(round(self.__mean(distances)))
        print("Set Threshold: " + str(self.threshold))
