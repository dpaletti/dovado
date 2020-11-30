"""
This type stub file was generated by pyright.
"""

from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm
from pymoo.model.survival import Survival

def binary_tournament(pop, P, algorithm, **kwargs):
    ...

class NSGA2(GeneticAlgorithm):
    def __init__(self, pop_size=..., sampling=..., selection=..., crossover=..., mutation=..., eliminate_duplicates=..., n_offsprings=..., display=..., **kwargs) -> None:
        """

        Parameters
        ----------
        pop_size : {pop_size}
        sampling : {sampling}
        selection : {selection}
        crossover : {crossover}
        mutation : {mutation}
        eliminate_duplicates : {eliminate_duplicates}
        n_offsprings : {n_offsprings}

        """
        ...
    


class RankAndCrowdingSurvival(Survival):
    def __init__(self) -> None:
        ...
    


def calc_crowding_distance(F, filter_out_duplicates=...):
    ...
