from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Union

import toml
from dovado_rtl.explorers.utilities.range import Range

from dovado_rtl.parsers.utilities.parsed import (
    MODULE_NAME_STR,
    PARAMETER_NAME_STR,
    VALUE_STR,
)
import toml
import csv

SOURCE_PATH = Path


@dataclass
class Space(ABC):
    @abstractmethod
    def get_sources(self) -> list[SOURCE_PATH]:
        ...


@dataclass
class ContinuousSpace(Space):
    ranges: dict[SOURCE_PATH, dict[MODULE_NAME_STR, dict[PARAMETER_NAME_STR, Range]]]

    def __init__(self, toml_file: Path) -> None:
        try:
            toml_dict = toml.load(toml_file)
        except Exception as e:
            raise ValueError(
                "TOML file '" + str(toml_file) + " could not be loaded.\n" + str(e)
            )
        self.ranges = {}
        for source, module_parameter_dict in toml_dict.items():
            source_path = Path(source)
            self.ranges[source_path] = {}
            for module_name, parameter_range_dict in module_parameter_dict.items():
                self.ranges[source_path][module_name] = {}
                for parameter_name, range in parameter_range_dict.items():
                    self.ranges[source_path][module_name][parameter_name] = Range(range)

    def get_sources(self) -> list[SOURCE_PATH]:
        return list(self.ranges.keys())

    def get_structure(
        self,
    ) -> dict[SOURCE_PATH, dict[MODULE_NAME_STR, list[PARAMETER_NAME_STR]]]:
        out = {}
        for source, module_to_parameter in self.ranges.items():
            out[source] = {}
            for module, parameter_to_range in module_to_parameter.items():
                out[source][module] = []
                for parameter, _ in parameter_to_range.items():
                    out[source][module].append(parameter)
        return out

    def get_range(
        self,
        source_path: SOURCE_PATH,
        module_name: MODULE_NAME_STR,
        parameter_name: PARAMETER_NAME_STR,
    ) -> Range:
        return self.ranges[source_path][module_name][parameter_name]

    def get_ranges(self) -> list[tuple[PARAMETER_NAME_STR, Range]]:
        out = []
        for _, module_to_parameter in self.ranges.items():
            for _, parameter_to_range in module_to_parameter.items():
                for parameter, range in parameter_to_range.items():
                    out.append((parameter, range))
        return out

    def number_of_parameters(self) -> int:
        return len(self.get_ranges())

    def get_parameters(self) -> list[PARAMETER_NAME_STR]:
        return [parameter_range[0] for parameter_range in self.get_ranges()]

    def steps(self) -> list[Union[int, Literal["powers_of_two"]]]:
        return [range.step for _, range in self.get_ranges()]


@dataclass
class DiscreteSpace(Space):
    points: dict[
        SOURCE_PATH, dict[MODULE_NAME_STR, dict[PARAMETER_NAME_STR, list[VALUE_STR]]]
    ]

    def __init__(self, csv_file: Path, project_root: Path) -> None:
        try:
            csv_dict = self._strip_white_spaces(csv.DictReader(open(csv_file)))
        except Exception as e:
            raise ValueError(
                "CSV file '" + str(csv_file) + " could not be loaded.\n" + str(e)
            )
        fully_specified_parameters = list(csv_dict[0].keys())
        self.points = {}
        for fully_specified_parameter in fully_specified_parameters:
            source_path = self._find_source_path(
                fully_specified_parameter, project_root
            )
            if source_path not in self.points.keys():
                self.points[source_path] = {}

            module_name = self._find_module(fully_specified_parameter, project_root)
            if module_name not in self.points[source_path].keys():
                self.points[source_path][module_name] = {}

            parameter_name = self._find_parameter(fully_specified_parameter)
            self.points[source_path][module_name][parameter_name] = self._get_column(
                csv_dict, fully_specified_parameter
            )

    def get_sources(self) -> list[SOURCE_PATH]:
        return list(self.points.keys())

    def get_points(
        self,
        source_path: SOURCE_PATH,
        module_name: MODULE_NAME_STR,
        parameter_name: PARAMETER_NAME_STR,
    ) -> list[VALUE_STR]:
        return self.points[source_path][module_name][parameter_name]

    @staticmethod
    def _strip_white_spaces(csv_dict: csv.DictReader) -> list[Any]:
        return [{k.strip(): v.strip() for k, v in row.items()} for row in csv_dict]

    @staticmethod
    def _get_column(
        csv_dict: list[dict[str, Any]], fully_specified_parameter: str
    ) -> list[VALUE_STR]:
        return [row[fully_specified_parameter] for row in csv_dict]

    @staticmethod
    def _find_parameter(fully_specified_parameter: str) -> PARAMETER_NAME_STR:
        return fully_specified_parameter.split("/")[-1]

    @staticmethod
    def _find_module(
        fully_specified_parameter: str, project_root: Path
    ) -> MODULE_NAME_STR:
        source_path = DiscreteSpace._find_source_path(
            fully_specified_parameter, project_root
        )
        module_parameter_path = fully_specified_parameter.replace(str(source_path), "")

        # Module names such as module1/module2 mean that module2 is a submodule of module1
        # TODO: support this in the AntlrParsed
        return "/".join(module_parameter_path.split("/")[1:-1])

    @staticmethod
    def _find_source_path(fully_specified_parameter: str, project_root: Path) -> Path:
        accumulated_path = []
        for directory in fully_specified_parameter.split("/"):
            current_path = Path(project_root, *accumulated_path, directory)
            if current_path.is_file():
                return Path(*accumulated_path, directory)
            accumulated_path.append(directory)
        raise ValueError(
            "Could not find the source path for parameter "
            + str(fully_specified_parameter)
        )
