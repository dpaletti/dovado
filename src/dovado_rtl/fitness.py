from dovado_rtl.point_evaluation import DesignPointEvaluator
from typing import List, Union, Dict, Optional

from dovado_rtl.abstract_classes import AbstractFitnessEvaluator
from movado import approximate


class FitnessEvaluator(AbstractFitnessEvaluator):
    def __init__(
        self,
        evaluator: DesignPointEvaluator,
        disable: bool = False,
        controller: str = "Distance",
        estimator: str = "HoeffdingAdaptiveTree",
        **kwargs
    ):

        self.__evaluator: DesignPointEvaluator = evaluator
        if not disable:
            print("Approximating Design Space Exploration with Movado!")
        else:
            print("Exact Design Space Exploration")
        self.fitness = approximate(
            disabled=disable,
            outputs=len(self.__evaluator.get_metrics()),
            estimator=estimator,
            controller=controller,
            controller_debug=True,
            **kwargs
        )(self.fitness)

    def fitness(self, design_point: List[int]) -> List[float]:
        return list(
            self.__evaluator.evaluate(tuple(design_point)).value.values()
        )
