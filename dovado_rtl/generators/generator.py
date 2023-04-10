from dovado_rtl.explorers.utilities.design_points import DesignPoint
from nacolla.stateful_callable import StatefulCallable
from abc import abstractmethod


class Generator(StatefulCallable):
    @abstractmethod
    def generate(self, design_point: DesignPoint) -> DesignPoint:
        ...
