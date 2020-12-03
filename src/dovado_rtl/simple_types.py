from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)  # this makes Metric hashable
class Metric:
    utilisation: Optional[Tuple[str, str]]
    is_frequency: bool


@dataclass
class IsIncremental:
    synthesis: bool
    implementation: bool


@dataclass
class DesignValue:
    value: Dict[Metric, float]


@dataclass
class Example:
    design_point: List[int]
    design_value: DesignValue
