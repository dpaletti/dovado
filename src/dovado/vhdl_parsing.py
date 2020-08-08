import re
from pathlib import Path


def list_modules(src):
    return [
        re.sub(r"[ \t]*is", "", re.sub(r"entity[ \t]*", "", i))
        for i in re.findall(
            r"entity[ \t]*.*[ \t]*is",
            re.sub(r"--.*\n", "", Path(src).read_text()),
        )
    ]


def list_files(src_folder):
    return [
        str(pth) for pth in Path(src_folder).iterdir() if pth.suffix == ".vhd"
    ]
