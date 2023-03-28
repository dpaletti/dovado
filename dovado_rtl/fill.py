from importlib.resources import files
import re
from pathlib import Path


def fill(
    replacements: list[str],
    package: str,
    resource: str,
    out_path: Path,
    placeholder: str,
) -> None:
    frame = files(package).joinpath(resource).read_text()
    filled_frame = re.sub(placeholder, lambda m, r=iter(replacements): next(r), frame)
    out_path.write_text(filled_frame)
