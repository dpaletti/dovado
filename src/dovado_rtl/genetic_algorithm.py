from typing import List, Tuple
from collections import OrderedDict
from pymoo.model.problem import Problem
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import (
    get_sampling,
    get_crossover,
    get_mutation,
    get_termination,
)
from pymoo.optimize import minimize


import numpy as np
from dovado_rtl.simple_types import Metric
from dovado_rtl.fitness import FitnessEvaluator
import pickle


class MyProblem(Problem):
    def __init__(
        self,
        fitness_evaluator: FitnessEvaluator,
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        metrics: List[Metric],
    ):
        self.evaluator: FitnessEvaluator = fitness_evaluator
        self.metrics: List[Metric] = metrics
        super().__init__(
            n_var=len(free_parameters_range.keys()),
            n_obj=len(free_parameters_range.keys()),
            n_constr=0,
            xl=[
                free_parameters_range[parameter][0]
                for parameter in free_parameters_range.keys()
            ],
            xu=[
                free_parameters_range[parameter][1]
                for parameter in free_parameters_range.keys()
            ],
            type_var=np.int,
            elementwise_evaluation=True,
        )

    def _evaluate(self, x: List[int], out, *args, **kwargs):
        out["F"] = np.column_stack(
            [
                self.evaluator.fitness(tuple(x), metric)
                for metric in self.metrics
            ]
        )


def optimize(
    evaluator: FitnessEvaluator,
    free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
    metrics: List[Metric],
    execution_time: str,
) -> List[float]:
    problem = MyProblem(evaluator, free_parameters_range, metrics)

    algorithm = NSGA2(
        pop_size=10 * len(free_parameters_range.keys()),
        n_offsprings=10 * len(free_parameters_range.keys()),
        sampling=get_sampling("int_random"),
        crossover=get_crossover("int_sbx", prob=0.9, eta=15),
        mutation=get_mutation("int_pm", eta=20),
        eliminate_duplicates=True,
    )

    termination = get_termination("time", execution_time)
    res = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        save_history=True,
        verbose=True,
    )
    with open("objs.pkl", "wb") as f:
        pickle.dump([res, algorithm], f)
    # with open('objs.pkl', 'rb') as f:
    #     obj0, obj1, obj2 = pickle.load(f)
    return res.F[-1].tolist()
