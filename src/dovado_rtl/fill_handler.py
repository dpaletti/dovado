from typing import Optional, List
from pathlib import Path
from importlib_resources import files
from dovado_rtl.antlr.hdl_representation import Parameter
import re


class FillHandler:
    def __init__(
        self, placeholder: str, frame_path: str, out_path: str,
    ):
        self.placeholder = placeholder
        self.replacements: Optional[List[str]] = None
        self.out_path: str = out_path
        self.frame_path: str = frame_path

    def get_replacements(self) -> List[str]:
        if self.replacements:
            return self.replacements
        else:
            raise Exception(
                "Trying to fill frame in FrameHandler without setting replacements"
            )

    def fill(self) -> bool:
        try:
            frame_path_parts = Path(self.frame_path).parts
            out: str = re.sub(
                self.placeholder,
                lambda m, r=iter(self.get_replacements()): next(r),
                files(frame_path_parts[0])
                .joinpath("".join(frame_path_parts[1:]))
                .read_text(),
            )
            Path(self.out_path).write_text(out)
            self.replacements = None
            return True
        except Exception as e:
            raise Exception(
                "Exception during frame filling at fill handling: " + str(e)
            )

    def set_parameters(self, parameters: List[Parameter]) -> None:
        "Optional override"
        pass
