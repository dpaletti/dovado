import re
from pathlib import Path

net_types = [
    "supply0",
    "supply1",
    "tri",
    "triand",
    "trior",
    "tri0",
    "tri",
    "wire",
    "wand",
    "wor",
]
directions = ["input", "output", "inout"]


def list_files(src_folder):
    try:
        return [str(pth) for pth in src_folder.rglob("*.v") if pth.is_file]
    except Exception:
        return []


def list_modules(src):
    try:
        return [
            i[0 : i.find("(")] if i.find("(") != -1 else i
            for i in [
                re.sub(r"module", "", i).strip()
                for i in re.findall(
                    r"module[ \t]*[^{\s, :}]+[ \t]*", strip_comments(src)
                )
            ]
        ]
    except Exception:
        return []


def strip_comments(src):
    return re.sub(
        r"//.*\n", "", re.sub(r"\/\*(\*(?!\/)|[^*])*\*\/", "", src, re.DOTALL)
    )


def get_module(src, module):
    no_comments = strip_comments(src)
    module_search = re.search("module[  \t]+" + module, no_comments)
    if not module_search:
        return None
    module_start = no_comments[module_search.start() :]
    return module_start[: module_start.find(";") + 1]


def is_module(src):
    modules = re.findall(r"\bmodule[#|\(]?\b", src)
    if modules != 1:
        return False
    return True


def strip_parameters(module):
    if not is_module(module):
        raise ValueError(
            "Parameters can be stripped only from single module, found multiple"
        )

    parameter_start = module.find("#(")
    parameter_end = module.find(")")
    if parameter_start == -1:
        return module, None
    parameters = module[parameter_start : parameter_end + 1]
    return module.replace(parameters, ""), parameters


def list_declarations(module):
    if not is_module(module):
        raise ValueError(
            "Declaration section is defined only for single Modules"
        )

    no_param = strip_parameters(module)[0]
    module_search = re.search("module[ \t]+" + module, no_param)
    module_decl_skip = no_param[module_search.end() :]
    declaration_section = module_decl_skip[
        module_decl_skip.find("(") : module_decl_skip.find(");") + 1
    ]
    return [
        re.sub("[  \t]+", " ", i.strip())
        for i in declaration_section.split("\n")
        if re.match("input |output |inout ", i.strip())
    ]


def is_valid_identifier(identifier):
    # Distinguishes between port_type or direction and actual name
    # Some more rules are needed for full identifier validation
    # in this context is not needed
    if (
        identifier in net_types
        or identifier in directions
        or identifier == "signed"
        or "[" in identifier
        or identifier == "reg"
    ):
        return False
    return True


def declaration_exists(declarations, identifier):
    if not is_valid_identifier(identifier):
        return None
    for i in declarations:
        for j in [j.strip() for j in i.split(",")]:
            if re.search(identifier, j):
                return "".join(i)
    return None


def get_direction(declaration):
    return declaration.split()[0]


def get_type(declaration):
    splitted = declaration.split()
    if splitted[1] in net_types:
        return splitted[1]
    return "wire"


def sub_declaration_identifier(declaration, identifier):
    splitted = declaration.split()
    for i in splitted:
        if is_valid_identifier(i):
            return (
                " ".join(splitted[: splitted.index(i)]) + " " + identifier,
            )
