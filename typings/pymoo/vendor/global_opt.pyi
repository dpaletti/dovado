"""
This type stub file was generated by pyright.
"""

from pymoo.model.problem import Problem
from pymoo.vendor.go_benchmark_functions import *

class GlobalOptimizationProblem(Problem):
    def __init__(self, n_var=..., clazz=..., **kwargs) -> None:
        ...
    
    def success(self, x, **kwargs):
        ...
    


def get_global_optimization_problem_options():
    ...

if __name__ == "__main__":
    ...