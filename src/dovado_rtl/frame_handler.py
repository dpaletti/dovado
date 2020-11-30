import re
from typing import List, Optional
from pathlib import Path
from dovado_rtl.antlr.HdlRepresentation import Parameter


class FrameHandler:
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
            out: str = re.sub(
                self.placeholder,
                lambda m, r=iter(self.get_replacements()): next(r),
                Path(self.frame_path).open("r").read(),
            )
            Path(self.out_path).write_text(out)
            self.replacements = None
            return True
        except Exception:
            return False

    def set_parameters(self, parameters: List[Parameter]) -> None:
        "Optional override"
        pass
