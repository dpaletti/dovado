from dataclasses import dataclass
from pathlib import Path

from dovado_rtl.parsers.parameter import Parameter


@dataclass
class SourceFile:
    parameters: list[Parameter]
