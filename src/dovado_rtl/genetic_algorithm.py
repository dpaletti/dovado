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
import dovado_rtl.global_user_selections as gus
from dovado_rtl.fitness import fitness
import pickle


class MyProblem(Problem):
    def __init__(self):
        super().__init__(
            n_var=len(gus.FREE_PARAMETERS_RANGE),
            n_obj=len(gus.METRICS),
            n_constr=0,
            xl=[
                gus.FREE_PARAMETERS_RANGE[parameter][0]
                for parameter in gus.FREE_PARAMETERS
            ],
            xu=[
                gus.FREE_PARAMETERS_RANGE[parameter][1]
                for parameter in gus.FREE_PARAMETERS
            ],
            type_var=np.int,
            elementwise_evaluation=True,
        )

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = np.column_stack(
            [
                fitness(tuple(x), metric)
                for metric in (gus.METRICS + ["max_frequency"])
            ]
        )


def optimize(execution_time: str) -> np.ndarray:
    problem = MyProblem()

    algorithm = NSGA2(
        pop_size=10 * len(gus.FREE_PARAMETERS),
        n_offsprings=10 * len(gus.FREE_PARAMETERS),
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
    return res.F[-1]
