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


class Probe(Input):
    ...


class AutomaticExplorationProject(ParsedProject):
    space: ContinuousSpace

    def get_parsed_project(self) -> ParsedProject:
        return super()


class ManualExplorationProject(ParsedProject):
    space: DiscreteSpace

    def get_parsed_project(self) -> ParsedProject:
        return super()
