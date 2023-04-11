from pathlib import Path
from dovado_rtl.explorers.utilities.spaces import ContinuousSpace, DiscreteSpace, Space
from dovado_rtl.explorers.utilities.tasks import (
    ParsedProject,
    ManualExplorationProject,
    AutomaticExplorationProject,
)
from dovado_rtl.input import Input
from dovado_rtl.parsers.utilities.parsed import Parsed
from dovado_rtl.parsers.utilities.parser import Parser
from dovado_rtl.explorers.utilities.design_points import DesignPoint
from typing import Union


def parse(
    input_project: Union[Input, DesignPoint],
    parser: type[Parser],
) -> Union[ParsedProject, DesignPoint]:
    task_file = input_project.task_file
    project_root = input_project.project_root

    target_source = parser().parse(Path(project_root, input_project.target_file))

    if isinstance(input_project, DesignPoint):
        # if the parser is needed in the middle of the flow
        return DesignPoint(**(dict(input_project) | {"target_source": target_source}))

    if task_file.suffix == ".csv":
        discrete_space = DiscreteSpace(task_file, project_root)
        parameter_sources = _parse_sources(project_root, discrete_space, parser)
        return ManualExplorationProject(
            **(
                dict(input_project)
                | {
                    "space": discrete_space,
                    "parameter_sources": parameter_sources,
                    "target_source": target_source,
                }
            )
        )

    elif task_file.suffix == ".toml":
        continuous_space = ContinuousSpace(task_file)
        parameter_sources = _parse_sources(project_root, continuous_space, parser)
        return AutomaticExplorationProject(
            **(
                dict(input_project)
                | {
                    "space": continuous_space,
                    "parameter_sources": parameter_sources,
                    "target_source": target_source,
                }
            )
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
