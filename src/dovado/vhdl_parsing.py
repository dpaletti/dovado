import re

port_modes = ["in", "out", "buffer", "inout"]


def list_files(src_dir):
    try:
        return [str(pth) for pth in src_dir.rglob("*.vhd") if pth.is_file]
    except Exception:
        return []


def list_modules(src):
    return [
        re.sub(r"[ \t]*is", "", re.sub(r"entity[ \t]*", "", i))
        for i in re.findall(r"entity[ \t]*.*[ \t]*is", strip_comments(src),)
    ]


def strip_comments(src):
    return re.sub(r"--.*\n", "\n", src)


def get_entity(src, entity):
    no_comments = strip_comments(src)
    entity_search = re.search("entity[ \t]+" + entity, no_comments)
    if not entity_search:
        return None
    entity_start = entity_search.start()
    entity_end = re.search(
        "end[ \t]*(entity)?[ \t]*" + entity, no_comments
    ).end()
    return no_comments[entity_start : entity_end + 1]


def is_entity(src):
    entities = re.findall(r"\bentity\b", src)
    entities_end = re.findall(r"\bend[ \t]*entity\b", src)
    if len(entities) != 1 if not entities_end else len(entities) != 2:
        return False
    return True


def strip_parameters(entity):
    if not is_entity(entity):
        raise ValueError("Values can be stripped only from single entities")
    open_par_search = re.search(r"generic[ \t]*\(", entity)
    if not open_par_search:
        return entity, None
    entity_skip = entity[open_par_search.end() :]
    parameters = entity[open_par_search.start() : entity.find(")") + 1]
    return (
        entity.replace(parameters, ""),
        [i.strip() for i in entity_skip[: entity_skip.find(")")].split(";")],
    )


def list_declarations(entity):
    if not is_entity(entity):
        raise ValueError(
            "Declaration section is not defined for multiple entities"
        )
    no_param, _ = strip_parameters(entity)
    declaration_search = re.search(r"port[ \t]*\(.*\);", no_param, re.DOTALL)
    declarations = re.sub(
        r"port[ \t]*\(",
        "",
        no_param[declaration_search.start() : declaration_search.end() - 2],
    ).split(";")
    return [
        " ".join(
            i.strip()
            .replace("\n", "")
            .replace("\r", "")
            .replace("\t", " ")
            .split()
        )
        for i in declarations
    ]


def declaration_exists(declarations, identifier):
    for i in declarations:
        for j in [j.strip() for j in i.split(",")]:
            if (
                re.match(r"[ \t]*" + identifier + "[  \t]*:", j)
                or j == identifier
            ):
                return "".join(i)
    return None


def get_direction(declaration):
    direction = declaration[declaration.find(":") + 1 :].strip().split()[0]
    if direction not in port_modes:
        raise ValueError(
            "Error while parsing, expected as a direction for declaration "
            + str(port_modes)
            + " found "
            + direction
            + " instead"
        )
    return direction


def get_type(declaration):
    # types cannot be checked because they depend on input libraries
    type = declaration[declaration.find(":") + 1 :].strip().split()[1]
    return type[: type.find("(")] if type.find("(") != -1 else type


def sub_declaration_identifier(declaration, identifier):
    ids_bound = declaration.find(":")
    if ids_bound == -1:
        raise ValueError("Malformed declaration: " + declaration)
    return identifier + declaration[ids_bound:]
