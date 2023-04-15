from importlib.machinery import ModuleSpec
from typing import Any, Callable, ClassVar, Literal, Optional, Union
from nacolla import ImmutableModel
from pydantic import DirectoryPath, FilePath
from pathlib import Path
import importlib.util
import toml
from dovado_rtl.builders.vivado.directives import (
    SYNTHESIS_DIRECTIVE,
    PLACE_DIRECTIVE,
    ROUTE_DIRECTIVE,
)

OPTION_DICTIONARY = dict[str, Optional[Union[str, int, bool, float]]]

_default_genetic_options: OPTION_DICTIONARY = {"pop_size": 10, "n_offsprings": None}
_default_genetic_sampling: OPTION_DICTIONARY = {"method": "int_random"}
_default_genetic_crossover: OPTION_DICTIONARY = {
    "method": "int_sbx",
    "prob": 0.9,
    "eta": 15,
}
_default_genetic_mutation: OPTION_DICTIONARY = {"method": "int_pm", "eta": 20}
_default_genetic_termination: OPTION_DICTIONARY = {"method": None}
_default_genetic_algorithm: str = "NSGA2"
_default_approximation_options: OPTION_DICTIONARY = {
    "stochastic": False,
    "estimator": "HoeffdingAdaptiveTree",
    "controller": "Mab",
}
_default_approximation: bool = False


class Input(ImmutableModel):
    flow: str  # which flow to use to explore the input project
    project_root: DirectoryPath  # all paths in the exploration file are appended to this path
    target_file: Path  # the full path for the target file is computed by appending this to the project root.
    task_file: FilePath  # the full path to the task file
    board: str  # board for synthesis/implementation
    clock_port: str  # clock port in the target module
    implementation: bool = (
        False  # whether to calculate metrics after synthesi or implementation
    )
    incremental: bool = False  # whether to use incremental synthesis/implementation
    synthesis_directive: SYNTHESIS_DIRECTIVE = "RuntimeOptimized"
    place_directive: PLACE_DIRECTIVE = "RuntimeOptimized"
    route_directive: ROUTE_DIRECTIVE = "RuntimeOptimized"
    target_clock: float = 1000  # target clock in Mhz
    target_module: Optional[
        str
    ] = None  # if the target file contains only one module may be left unspecified

    in_place: bool = False  # Whether to work on a copy of the target project

    custom_metrics_folder: Optional[DirectoryPath] = None
    default_metrics: list[str] = []
    custom_metrics: dict[str, Callable[..., float]] = {}

    verbose: bool = False  # for now it controls whether the Vivado builder should print every vivado output

    algorithm: str = _default_genetic_algorithm  # options for now are (case insensitive): NSGA2, AGEMOEA, MOEAD, RVEA, RNSGA2, CTAEA, NSGA3, RNSGA3, UNSGA3
    approximate: bool = _default_approximation

    options: OPTION_DICTIONARY = _default_genetic_options
    sampling: OPTION_DICTIONARY = _default_genetic_sampling
    crossover: OPTION_DICTIONARY = _default_genetic_crossover
    mutation: OPTION_DICTIONARY = _default_genetic_mutation
    termination: OPTION_DICTIONARY = _default_genetic_termination
    approximation_options: OPTION_DICTIONARY = _default_approximation_options

    default_metrics_folder: ClassVar[str] = "custom_metrics"
    work_directory: ClassVar[str] = "dovado_work"

    extra: Optional[dict] = None

    @staticmethod
    def make_from_file(input_file: Path) -> "Input":
        input_dict = toml.load(input_file)
        metrics = input_dict.get("metrics")
        genetic_settings = Input._make_genetic_settings(input_dict)
        if metrics is not None:
            custom_metrics_folder = Input._get_metrics_folder(
                input_dict.get("custom_metrics_folder")
            )

            (default_metrics, custom_metrics) = Input._retrieve_metrics(
                input_dict["metrics"], custom_metrics_folder
            )

            input_dict.pop("custom_metrics_folder", None)
            input_dict.pop("metrics", None)
            input_dict.pop("genetic", None)
            if genetic_settings:
                return Input(
                    **input_dict,
                    **genetic_settings,
                    custom_metrics=custom_metrics,
                    default_metrics=default_metrics,
                    custom_metrics_folder=Path(custom_metrics_folder),
                )
        return Input(**input_dict, **genetic_settings)

    @staticmethod
    def _make_genetic_settings(input_dict: dict[str, Any]) -> dict[str, Any]:
        genetic = input_dict.get("genetic")
        if genetic is not None:
            algorithm = genetic.get("algorithm")
            approximate = genetic.get("approximate")
            options = genetic.get("options")
            termination = genetic.get("termination")
            sampling = genetic.get("sampling")
            crossover = genetic.get("crossover")
            mutation = genetic.get("mutation")
            movado = genetic.get("movado")
            return {
                "algorithm": algorithm
                if algorithm is not None
                else _default_genetic_algorithm,
                "approximate": approximate
                if approximate is not None
                else _default_approximation,
                "options": (_default_genetic_options | options)
                if options is not None
                else _default_genetic_options,
                "termination": (_default_genetic_termination | termination)
                if termination is not None
                else _default_genetic_termination,
                "sampling": (_default_genetic_sampling | sampling)
                if sampling is not None
                else _default_genetic_sampling,
                "crossover": (_default_genetic_crossover | crossover)
                if crossover
                else _default_genetic_crossover,
                "mutation": (_default_genetic_mutation | mutation)
                if mutation is not None
                else _default_genetic_mutation,
                "approximation_options": (_default_approximation_options | movado)
                if movado is not None
                else _default_approximation_options,
            }
        return {
            "algorithm": _default_genetic_algorithm,
            "approximate": _default_approximation,
            "options": _default_genetic_options,
            "termination": _default_genetic_termination,
            "sampling": _default_genetic_sampling,
            "crossover": _default_genetic_crossover,
            "mutation": _default_genetic_mutation,
            "approximation_options": _default_approximation_options,
        }

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
        metrics_folder: Optional[Path],
    ) -> tuple[list[str], dict[str, Callable[..., float]]]:

        if not isinstance(metrics, dict):
            raise ValueError("Invalid format for metrics " + str(metrics))
        if not set(metrics.keys()).intersection({"default", "custom"}):
            raise ValueError("Allowed keys for metrics are 'default' and 'custom'")

        if "default" in metrics.keys():
            default_metrics = metrics["default"]
        else:
            default_metrics = []

        custom_metrics = {}
        if "custom" in metrics.keys():
            if metrics_folder is None:
                raise ValueError("Could not find custom metrics folder")
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
    def _get_metrics_folder(custom_metrics_folder: Optional[str]) -> Optional[Path]:

        custom_metrics_path = (
            Path(custom_metrics_folder)
            if custom_metrics_folder is not None
            else Path(Input.default_metrics_folder)
        )
        if custom_metrics_path.is_dir():
            return custom_metrics_path
        return None
