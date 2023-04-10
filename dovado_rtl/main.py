from pathlib import Path
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy
import sys
from nacolla.parsing import parse_implementation_map, IMPLEMENTATION_MAP
from nacolla.parsing.parse_flow import parse_flow
from nacolla.flow import Flow
from importlib.resources import files
import json

_DEFAULT_STEP_FILE_NAME = "default_steps.json"


def main() -> None:

    input_project = Input.make_from_file(_parse_config_path())

    if not input_project.in_place:
        input_project = project_copy(input_project)

    implementation_map = _make_implementation_map(Path(input_project.work_directory))
    flow = make_flow(implementation_map, input_project)

    for _ in flow:
        ...


def make_flow(
    implementation_map: IMPLEMENTATION_MAP,
    input_project: Input,
) -> Flow:

    flow_name = input_project.flow
    work_directory = Path(input_project.work_directory)

    default_flow_path = Path(
        str(files("dovado_rtl.nacolla.flows").joinpath(flow_name + ".toml"))
    )

    custom_flow_path = Path(work_directory, flow_name)

    if default_flow_path.is_file():
        flow_path = default_flow_path

    elif custom_flow_path.is_file():
        flow_path = custom_flow_path

    else:
        raise ValueError("Flow '" + flow_name + "' cannot be found")

    return parse_flow(flow_path, implementation_map, source=input_project)


def _make_implementation_map(work_directory: Path) -> IMPLEMENTATION_MAP:
    default_implementation_map_path: Path = Path(
        str(files("dovado_rtl.nacolla").joinpath("steps.json"))
    )
    steps = json.load(default_implementation_map_path.open())

    fixed_steps = steps.copy()
    for index, step in enumerate(steps["implementations"]):
        step_module = step["callable"]["module"]
        step_file = step_module.split("/")[-1]
        step_path = ".".join(step_module.split("/")[:-1])
        fixed_steps["implementations"][index]["callable"]["module"] = str(
            files("dovado_rtl." + step_path).joinpath(step_file)
        )

    default_steps = Path(work_directory, _DEFAULT_STEP_FILE_NAME)
    default_steps.touch()

    with default_steps.open("w") as f:
        json.dump(fixed_steps, f)

    implementation_map = parse_implementation_map(default_steps)

    user_steps_path = Path(work_directory, "steps.json")
    if user_steps_path.is_file():
        implementation_map |= parse_implementation_map(user_steps_path)

    return implementation_map


def _parse_config_path() -> Path:
    if len(sys.argv) == 1:
        raise ValueError("Missing the path to the configuration file")
    return Path(sys.argv[1])
