from dataclasses import dataclass
from typing import Literal, Union

PORT_DIRECTION = Union[Literal["input"], Literal["output"], Literal["inout"]]
PORT_DIMENSION = Union[Literal["scalar"], Literal["vectorial"]]


@dataclass
class Port:
    name: str
    direction: PORT_DIRECTION
    dimension: PORT_DIMENSION
    has_default: bool
