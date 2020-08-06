import re
from pathlib import Path


def list_modules(src):
    return [
        re.sub(r"[ \t]*is", "", re.sub(r"entity[ \t]*", "", i))
        for i in re.findall(
            r"entity .* is",
            re.sub(r"--.*\n", "", Path(src).open("r").read()),
            re.DOTALL,
        )
    ]


def list_files(src_folder):
    return [
        str(pth) for pth in Path(src_folder).iterdir() if pth.suffix == ".vhd"
    ]
