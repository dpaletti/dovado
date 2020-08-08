import re
from pathlib import Path


def list_modules(src):
    return [
        i[0 : i.find("(")] if i.find("(") != -1 else i
        for i in [
            re.sub(r"module", "", i).strip()
            for i in re.findall(
                r"module[ \t]*[^{\s, :}]+[ \t]*",
                re.sub(
                    r"//.*\n",
                    "",
                    re.sub(r"/\*.*\*/", "", Path(src).open("r").read()),
                ),
            )
        ]
    ]


def list_files(src_folder):
    return [
        str(pth) for pth in Path(src_folder).iterdir() if pth.suffix == ".v"
    ]
