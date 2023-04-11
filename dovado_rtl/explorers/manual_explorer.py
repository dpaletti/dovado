from collections import deque
from pathlib import Path
from typing import Optional, Union

from dovado_rtl.explorers.explorer import (
    DesignPoint,
    EndExploration,
    EvaluatedDesignPoint,
    Explorer,
)
from dovado_rtl.explorers.utilities.spaces import SOURCE_PATH
from dovado_rtl.explorers.utilities.tasks import ManualExplorationProject
from dovado_rtl.parsers.utilities.parsed import MODULE_NAME_STR, PARAMETER_NAME_STR


class ManualExplorer(Explorer):
    _output_file_name = "exploration"
    _homonymous_files_limit = 100

    def __init__(self) -> None:
        super().__init__()
        self._evaluated_points = 0
        self._output_file: Optional[Path] = None
        self._task: Optional[ManualExplorationProject] = None
        self._metrics: list[str] = []
        self._points_under_evaluation: deque[DesignPoint] = deque()
        self._buffered_evaluated_points: list[EvaluatedDesignPoint] = []

    def explore(self, task: ManualExplorationProject) -> DesignPoint:
        self._task = task
        self._metrics = task.default_metrics + list(task.custom_metrics.keys())

        Path(task.work_directory).mkdir(exist_ok=True)
        self._output_file = Path(
            task.work_directory,
            self._get_file_name(
                self._task.work_directory, ManualExplorer._output_file_name
            ),
        )
        self._output_file.touch(exist_ok=False)

        Explorer._add_row_to_output(self._metrics, self._output_file)

        current_points = self._set_point(self._evaluated_points, task)
        if current_points is None:
            raise ValueError("Found at least one parameter with no values to explore")

        design_point = DesignPoint(
            **(dict(self._task.get_parsed_project()) | {"points": current_points})
        )
        self._points_under_evaluation.append(design_point)
        return design_point

    def update(
        self, evaluated_design_point: Union[EvaluatedDesignPoint, EndExploration]
    ) -> Union[DesignPoint, EndExploration]:
        if isinstance(evaluated_design_point, EndExploration):
            return EndExploration()

        if self._task is None:
            raise ValueError("Found None task in manual explorer")
        if self._output_file is None:
            raise ValueError("Found None output_file")

        if self._points_under_evaluation[0].points == evaluated_design_point.points:
            Explorer._add_row_to_output(
                [
                    str(evaluated_design_point.design_value[metric])
                    for metric in self._metrics
                ],
                self._output_file,
            )
            self._points_under_evaluation.pop()
            self._add_buffered_points_to_output()

        else:
            self._buffered_evaluated_points.append(evaluated_design_point)

        current_points = self._set_point(self._evaluated_points, self._task)
        if current_points is None:
            return EndExploration()

        design_point = DesignPoint(
            **(dict(self._task.get_parsed_project()) | {"points": current_points})
        )
        self._points_under_evaluation.append(design_point)
        return design_point

    def _add_buffered_points_to_output(self) -> None:
        if self._output_file is None:
            raise ValueError("Found None output file")
        for point_under_evaluation in self._points_under_evaluation:
            used_buffered_point = False
            for buffered_evaluated_point in self._buffered_evaluated_points:
                if point_under_evaluation.points == buffered_evaluated_point.points:
                    Explorer._add_row_to_output(
                        [
                            str(buffered_evaluated_point.design_value[metric])
                            for metric in self._metrics
                        ],
                        self._output_file,
                    )
                    self._points_under_evaluation.pop()
                    self._buffered_evaluated_points.remove(buffered_evaluated_point)
                    used_buffered_point = True
                    break
            if not used_buffered_point:
                break

    def _set_point(
        self, iterations: int, task: ManualExplorationProject
    ) -> Optional[
        dict[SOURCE_PATH, dict[MODULE_NAME_STR, dict[PARAMETER_NAME_STR, str]]]
    ]:
        current_points = {}
        for source_path, modules_to_parameters_dict in task.space.points.items():
            parsed = task.parameter_sources[source_path]
            current_points[source_path] = {}
            module_to_parameter_to_value = {}

            for module_name, parameters_to_values in modules_to_parameters_dict.items():
                module_to_parameter_to_value[module_name] = {}

                for parameter, values in parameters_to_values.items():
                    if len(values) == iterations:
                        return None

                    module_to_parameter_to_value[module_name][parameter] = values[
                        iterations
                    ]

                current_points[source_path].update(module_to_parameter_to_value)

            Path(task.project_root, source_path).open("w").write(
                parsed.replace(module_to_parameter_to_value)
            )

        self._evaluated_points += 1
        return current_points
