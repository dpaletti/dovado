from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Parameter:
    name: str
    value: str
