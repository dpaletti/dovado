from importlib.machinery import ModuleSpec
from typing import Callable, ClassVar, Literal, Optional, Union
from nacolla import ImmutableModel
from pydantic import DirectoryPath, FilePath
from pathlib import Path
import importlib.util
import toml


class Input(ImmutableModel):
    project_root: DirectoryPath  # all paths in the exploration file are appended to this path
    target_file: Path  # the full path for the target file is computed by appending this to the project root.
    task_file: FilePath  # the full path to the task file
    board: str  # board for synthesis/implementation
    clock_port: str  # clock port in the target module
    implementation: bool = (
        False  # whether to calculate metrics after synthesi or implementation
    )
    incremental: bool = False  # whether to use incremental synthesis/implementation
    synthesis_directives: list[str] = [
        "RuntimeOptimized"
    ]  # a list of synthesis directives
    implementation_directives: list[str] = [
        "RuntimeOptimized"
    ]  # a list of implementation directives
    target_clock: int = 1000  # target clock in Mhz
    target_module: Optional[
        str
    ] = None  # if the target file contains only one module may be left unspecified

    custom_metrics_folder: Optional[DirectoryPath] = None
    default_metrics: list[str] = []
    custom_metrics: dict[str, Callable[..., float]] = {}

    default_metrics_folder: ClassVar[str] = "custom_metrics"
    work_directory: ClassVar[str] = "dovado_work"

    @staticmethod
    def make_from_file(input_file: Path) -> "Input":
        input_dict = toml.load(input_file)
        metrics = input_dict.get("metrics")
        if metrics is not None:
            custom_metrics_folder = Input._get_metrics_folder(
                input_dict.get("custom_metrics_folder")
            )

            (
                default_metrics,
                custom_metrics,
            ) = Input._retrieve_metrics(input_dict["metrics"], custom_metrics_folder)

            del input_dict["custom_metrics_folder"]
            del input_dict["metrics"]
            return Input(
                **input_dict,
                custom_metrics=custom_metrics,
                default_metrics=default_metrics,
                custom_metrics_folder=Path(custom_metrics_folder)
            )
        return Input(**input_dict)

    @staticmethod
    def get_available_custom_metrics(
        custom_metrics_folder: Path,
    ) -> dict[str, ModuleSpec]:
        function_to_module = {}
        for file in custom_metrics_folder.glob("**/*.py"):
            spec = importlib.util.spec_from_file_location(file.stem, file)
            if spec is None or spec.loader is None:
                raise ValueError("Could not load " + str(file))

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            function_to_module.update(
                {
                    public_function: module
                    for public_function in module.__dir__()
                    if not (public_function[0] == "_" or public_function[1] == "__")
                }
            )
        return function_to_module

    @staticmethod
    def _retrieve_metrics(
        metrics: dict[Union[Literal["default"], Literal["custom"]], list[str]],
        metrics_folder: Path,
    ) -> tuple[list[str], dict[str, Callable[..., float]]]:

        if not isinstance(metrics, dict):
            raise ValueError("Invalid format for metrics " + str(metrics))
        if set(metrics.keys()) != set(("default", "custom")):
            raise ValueError("Allowed keys for metrics are 'default' and 'custom'")

        if "default" in metrics.keys():
            default_metrics = metrics["default"]
        else:
            default_metrics = []

        custom_metrics = {}
        if "custom" in metrics.keys():
            function_to_module = Input.get_available_custom_metrics(metrics_folder)
            for custom_metric in metrics["custom"]:
                module = function_to_module.get(custom_metric)
                if not module:
                    raise ValueError(
                        "Could not find "
                        + str(custom_metric)
                        + " in "
                        + str(metrics_folder)
                    )
                custom_metrics[custom_metric] = getattr(module, custom_metric)

        return default_metrics, custom_metrics

    @staticmethod
    def _get_metrics_folder(custom_metrics_folder: Optional[str]) -> Path:

        custom_metrics_path = (
            Path(custom_metrics_folder)
            if custom_metrics_folder is not None
            else Path(Input.default_metrics_folder)
        )
        if custom_metrics_path.is_dir():
            return custom_metrics_path
        raise ValueError(
            "Cannot find custom_metrics folder " + str(custom_metrics_folder)
        )
