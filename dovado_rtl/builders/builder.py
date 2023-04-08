from abc import ABC, abstractmethod
from dovado_rtl.explorers.utilities.design_points import (
    DesignPoint,
    EvaluatedDesignPoint,
)
from pathlib import Path
from dovado_rtl.fill import fill
from typing import Union
from dovado_rtl.explorers.utilities.tasks import EndExploration
from nacolla.stateful_callable import StatefulCallable


class Builder(StatefulCallable, ABC):
    _placeholder = "____"

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def build(
        self, design_point: DesignPoint
    ) -> Union[EvaluatedDesignPoint, EndExploration]:
        ...

    def _fill(
        self,
        replacements: list[str],
        package: str,
        resource: str,
        out_path: Path,
    ) -> None:
        fill(replacements, package, resource, out_path, self._placeholder)
