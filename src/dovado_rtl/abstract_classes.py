import abc
from abc import abstractmethod
from typing import Tuple, List, Dict, Optional
from dovado_rtl.antlr.hdl_representation import (
    Entity,
    Parameter,
    TopLevel,
    Port,
)
from dovado_rtl.enums import RTL
from dovado_rtl.simple_types import DesignValue, Example, Metric
from dovado_rtl.fill_handler import FillHandler


class AbstractEstimator(abc.ABC):
    @abstractmethod
    def estimate(self, design_point: List[int], metric: Metric) -> float:
        pass

    @abstractmethod
    def add_example(self, example: Example) -> None:
        pass

    @abstractmethod
    def get_examples(self) -> List[Example]:
        pass


class AbstractDesignPointEvaluator(abc.ABC):
    @abstractmethod
    def evaluate(self, design_point: Tuple[int, ...]) -> DesignValue:
        pass

    @abstractmethod
    def get_max_frequency(self, wns: float) -> float:
        pass

    @abstractmethod
    def set_estimator(self, estimator: AbstractEstimator) -> None:
        pass

    @abstractmethod
    def get_metrics(self):
        pass

    @abstractmethod
    def set_metrics(self, metrics):
        pass


class AbstractFitnessEvaluator(abc.ABC):
    @abstractmethod
    def fitness(self, design_point: Tuple[int, ...]):
        pass


class AbstractSourceParser(abc.ABC):
    @abstractmethod
    def parse(self) -> Tuple[List[Entity], Optional[TopLevel]]:
        pass

    @abstractmethod
    def get_entity(self, entity: str) -> Entity:
        pass

    @abstractmethod
    def set_entity(self, entity: str) -> None:
        pass

    @abstractmethod
    def get_top_entity(self) -> Entity:
        pass

    @abstractmethod
    def get_path(self) -> str:
        pass

    @abstractmethod
    def get_folder(self) -> str:
        pass

    @abstractmethod
    def get_hdl(self) -> RTL:
        pass

    @abstractmethod
    def get_entities(self) -> List[Entity]:
        pass

    @abstractmethod
    def get_parameters(self) -> List[Parameter]:
        pass

    @abstractmethod
    def get_parameter(self, parameter: str) -> Parameter:
        pass

    @abstractmethod
    def get_top_level(self):
        pass

    @abstractmethod
    def get_parameter_value(self, parameter: str) -> Optional[int]:
        pass

    @abstractmethod
    def write_parameter_values(
        self, hdl_handler: FillHandler, values: Dict[str, int],
    ):
        pass

    @abstractmethod
    def get_ports(self) -> List[Port]:
        pass

    @abstractmethod
    def get_port(self, port: str) -> Port:
        pass

    @abstractmethod
    def check_port(self, port: str) -> Optional[Port]:
        pass

    @abstractmethod
    def get_port_direction(self, port: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_port_type(self, port: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_imports(self) -> Tuple[List[str], List[str]]:
        pass

