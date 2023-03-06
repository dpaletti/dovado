from dataclasses import asdict
from pathlib import Path
from typing import TypeVar, Union
from dovado_rtl.explorers.spaces import ContinuousSpace, DiscreteSpace, Space
from dovado_rtl.explorers.tasks import (
    AutomaticExplorationProject,
    ManualExplorationProject,
)
from dovado_rtl.input import Input
from dovado_rtl.parsing_utilities.parsed import Parsed
from dovado_rtl.parsing_utilities.parser import Parser


def parse(
    input_project: Input,
    parser: type[Parser],
) -> Union[AutomaticExplorationProject, ManualExplorationProject]:
    task_file = input_project.task_file
    project_root = input_project.project_root

    if task_file.suffix == ".csv":
        discrete_space = DiscreteSpace(task_file, project_root)
        target_sources = _parse_sources(project_root, discrete_space, parser)
        return ManualExplorationProject(
            **dict(input_project), space=discrete_space, target_sources=target_sources
        )

    elif task_file.suffix == ".toml":
        continuous_space = ContinuousSpace(task_file)
        target_sources = _parse_sources(project_root, continuous_space, parser)
        return AutomaticExplorationProject(
            **dict(input_project), space=continuous_space, target_sources=target_sources
        )
    else:
        raise ValueError(
            "The task file must be either a csv file for manual exploration or a toml file for automatic exploration"
        )


def _parse_sources(
    project_root: Path, space: Space, parser: type[Parser]
) -> dict[Path, Parsed]:
    source_to_parsed = {}
    for source in space.get_sources():
        source_to_parsed[source] = parser().parse(Path(project_root, source))
    return source_to_parsed
