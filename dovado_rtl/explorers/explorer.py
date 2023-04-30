from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
from nacolla.stateful_callable import StatefulCallable
from dovado_rtl.explorers.utilities.tasks import ParsedProject
from dovado_rtl.explorers.utilities.design_points import (
    DesignPoint,
    EvaluatedDesignPoint,
    EndExploration,
)
import csv
import datetime


class Explorer(StatefulCallable, ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def explore(self, task: ParsedProject) -> DesignPoint:
        ...

    @abstractmethod
    def update(
        self, evaluated_design_point: Union[EvaluatedDesignPoint, EndExploration]
    ) -> Union[DesignPoint, EndExploration]:
        ...

    @staticmethod
    def _get_file_name(work_dir: str, base_file_name: str) -> str:
        current_file = base_file_name + ".csv"
        if not Path(work_dir, current_file).exists():
            return current_file

        return (
            base_file_name
            + "_"
            + str(datetime.datetime.now()).replace(" ", "_")
            + ".csv"
        )

    @staticmethod
    def _add_row_to_output(row: list[str], file: Path) -> None:
        opened_file = file.open("a", newline="")
        csv_writer = csv.writer(opened_file)
        csv_writer.writerow(row)
        opened_file.flush()
