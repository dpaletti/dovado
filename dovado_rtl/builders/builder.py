from abc import ABC, abstractmethod
from dovado_rtl.explorers.utilities.design_points import (
    DesignPoint,
    EvaluatedDesignPoint,
)
from pathlib import Path
from dovado_rtl.fill import fill


class Builder(ABC):
    _placeholder = "____"

    @abstractmethod
    def build(self, design_point: DesignPoint) -> EvaluatedDesignPoint:
        ...

    def _fill(
        self,
        replacements: list[str],
        package: str,
        resource: str,
        out_path: Path,
    ) -> None:
        fill(replacements, package, resource, out_path, self._placeholder)
