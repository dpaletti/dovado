"""
This type stub file was generated by pyright.
"""

from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm
from pymoo.operators.selection.tournament_selection import TournamentSelection

def comp_by_cv_dom_then_random(pop, P, **kwargs):
    ...

class RestrictedMating(TournamentSelection):
    """Restricted mating approach to balance convergence and diversity archives"""
    ...


class CTAEA(GeneticAlgorithm):
    def __init__(self, ref_dirs, sampling=..., selection=..., crossover=..., mutation=..., eliminate_duplicates=..., display=..., **kwargs) -> None:
        """
        CTAEA

        Parameters
        ----------
        ref_dirs : {ref_dirs}
        sampling : {sampling}
        selection : {selection}
        crossover : {crossover}
        mutation : {mutation}
        eliminate_duplicates : {eliminate_duplicates}
        """
        ...
    


class CADASurvival:
    def __init__(self, ref_dirs) -> None:
        ...
    
    def do(self, _, pop, da, n_survive, **kwargs):
        ...
    

