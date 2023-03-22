from dataclasses import dataclass
from typing import Any, Literal, Union


@dataclass(frozen=True)
class Range:
    start: int
    end: int
    step: Union[int, Literal["powers_of_two"]]

    def __init__(self, raw_range: Union[list[int], dict[str, Any]]) -> None:
        if isinstance(raw_range, list):
            self._parse_range_list(raw_range)
            object.__setattr__(self, "step", 0)
        if isinstance(raw_range, dict):
            if "range" not in raw_range.keys():
                ValueError(
                    "When specifying a range as a dict please specify the 'range' key.\n"
                    + "Parsed dictionary is "
                    + str(raw_range)
                )
            self._parse_range_list(raw_range["range"])
            if "step" in raw_range.keys():
                step = raw_range["step"]
                if type(step) is int or step == "powers_of_two":
                    object.__setattr__(self, "step", raw_range["step"])
                else:
                    ValueError(
                        "A step may be specified either as an integer or as 'powers_of_two'."
                    )
            else:
                object.__setattr__(self, "step", 0)

    def _parse_range_list(self, range_list: list[int]) -> None:
        range_list_length = len(range_list)
        if range_list_length < 2 or range_list_length > 3:
            raise ValueError(
                "range list must contain two values (range start and end) and optionally a directive"
            )
        object.__setattr__(self, "start", range_list[0])
        object.__setattr__(self, "end", range_list[1])
