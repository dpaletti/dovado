#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
from dovado_rtl.explorers.spaces import ContinuousSpace, DiscreteSpace, SOURCE_PATH
from dovado_rtl.input import Input
from dovado_rtl.parsing_utilities.parsed import (
    MODULE_NAME_STR,
    PARAMETER_NAME_STR,
    VALUE_STR,
    Parsed,
)


class ParsedProject(Input):
    target_sources: dict[SOURCE_PATH, Parsed]

    def replace(
        self,
        source_path: SOURCE_PATH,
        module_parameter_to_value: dict[
            MODULE_NAME_STR, dict[PARAMETER_NAME_STR, VALUE_STR]
        ],
    ):
        self.target_sources[source_path].replace(module_parameter_to_value)

    def get_parsed_project(self) -> "ParsedProject":
        # This method is meaningful only when called by a children
        parsed_project_attributes = ParsedProject.__fields__

        return ParsedProject(
            **{
                key: value
                for key, value in dict(self).items()
                if key in parsed_project_attributes
            }
        )


class Probe(Input):
    ...


class AutomaticExplorationProject(ParsedProject):
    space: ContinuousSpace


class ManualExplorationProject(ParsedProject):
    space: DiscreteSpace
