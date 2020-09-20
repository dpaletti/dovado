from hdlConvertorAst.language import Language
from hdlConvertor import HdlConvertor
from hdlConvertorAst.hdlAst import (
    HdlModuleDef,
    HdlModuleDec,
    HdlImport,
    HdlAll,
    HdlValueInt,
    HdlCompInst,
    HdlOp,
    HdlValueId,
)
from hdlConvertor._hdlConvertor import ParseException
from hdlConvertorAst.to.vhdl.vhdl2008 import ToVhdl2008
from hdlConvertorAst.to.verilog.verilog2005 import ToVerilog2005


parsed_src_path = None
parsed = None


def parse(src_path):
    global parsed_src_path
    global parsed
    parsed_src_path = src_path
    src_path_string = str(src_path)
    if src_path.suffix == ".vhd":
        try:
            parsed = HdlConvertor().parse(
                src_path_string,
                Language.VHDL,
                [],
                hierarchyOnly=False,
                debug=True,
            )
        except ParseException:
            raise ValueError("Could not parse " + src_path_string + " as VHDL")
    elif src_path.suffix == ".v":
        try:
            parsed = HdlConvertor().parse(
                src_path_string,
                Language.VERILOG,
                [],
                hierarchyOnly=False,
                debug=True,
            )
        except ParseException:
            raise ValueError(
                "Could not parse "
                + str(src_path)
                + " as Verilog, .v files must be Verilog,"
                + " SystemVerilog files must be .sv"
            )
    elif src_path.suffix == ".sv":
        try:
            parsed = HdlConvertor().parse(
                src_path_string,
                Language.SYSTEM_VERILOG,
                [],
                hierarchyOnly=False,
                debug=True,
            )
        except ParseException:
            raise ValueError(
                "Could not parse "
                + str(src_path)
                + " as SystemVerilog, .sv files must be SystemVerilog,"
                + " Verilog files must be .v"
            )


def _is_parsed(src_path):
    if not parsed or parsed_src_path != src_path:
        return False
    return True


def get_modules(src_path):
    if not _is_parsed(src_path):
        parse(src_path)
    modules = []
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec):
            modules.append(o.name)
        if isinstance(o, HdlModuleDef):
            if o.dec:
                modules.append(o.dec.name)
    return modules


def get_parameters(src_path, module):
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec) and o.name == module:
            return o.params
        if isinstance(o, HdlModuleDef) and o.dec and o.dec.name == module:
            return o.dec.params


def write_to_file(out_path):
    with open(out_path, "w") as f:
        if out_path.suffix == ".vhd":
            # explicit conversion of all instantiations to direct instantiations
            # mandatory for Vivado compatibility
            for o in parsed.objs:
                if isinstance(o, HdlModuleDef):
                    for def_obj in o.objs:
                        if isinstance(def_obj, HdlCompInst) and isinstance(
                            def_obj.module_name, HdlOp
                        ):
                            def_obj.module_name.ops[0] = HdlValueId(
                                "entity work"
                            )

            ToVhdl2008(f).visit_HdlContext(parsed)
        else:
            ToVerilog2005(f).visit_HdlContext(parsed)
    global parsed_src_path
    parsed_src_path = out_path


def set_parameter(src_path, module, parameter, value):
    # value must be base 10
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec) and o.name == module:
            for param in o.params:
                if param.name == parameter.name:
                    param.value = HdlValueInt(
                        value, None, None
                    )  # here we force base 10

        if isinstance(o, HdlModuleDef) and o.dec and o.dec.name == module:
            for param in o.dec.params:
                if param.name == parameter.name:
                    param.value = HdlValueInt(value, None, None)

    write_to_file(src_path)


def map_parameter(src_path, module, parameter, value):
    print(parameter)
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDef):
            for module_definition in o.objs:
                if (
                    isinstance(module_definition, HdlCompInst)
                    and module_definition.param_map
                ):
                    for param in module_definition.param_map:
                        if str(param.ops[0]) == str(parameter.name):
                            param.ops[1] = HdlValueInt(value, None, None)
                            write_to_file(src_path)
                            return
        if isinstance(o, HdlModuleDec):
            for module_definition in o.objs:
                if (
                    isinstance(module_definition, HdlCompInst)
                    and module_definition.param_map
                ):
                    for param in module_definition.param_map:
                        if str(param.ops[0]) == str(parameter.name):
                            param.ops[1] = HdlValueInt(value, None, None)
                            write_to_file(src_path)
                            return


def get_ports(src_path, module):
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec) and o.name == module:
            return o.ports
        if isinstance(o, HdlModuleDef) and o.dec and o.dec.name == module:
            return o.dec.ports


def get_port_id(port):
    return str(port.name)


def get_port_from_id(port, ports):
    for i in ports:
        if i.name == port:
            return i
    return None


def get_port_direction(port):
    direction = str(port.direction)
    return direction[direction.find(".") + 1 :]


def get_port_type(port):
    try:
        return str(port.type.ops[0])
    except AttributeError:
        return str(port.type)


def get_imports(src_path):
    if not _is_parsed(src_path):
        parse(src_path)
    libraries = []
    use_clauses = []
    for o in parsed.objs:
        if isinstance(o, HdlImport):
            if o.path[0].val not in libraries and o.path[0].val != "work":
                libraries.append(o.path[0].val)
            use_clause = o.path[0].val + "." + o.path[1].val
            if HdlAll in o.path:
                use_clause += ".all"
            if use_clause not in use_clauses:
                use_clauses.append(use_clause)
    return libraries, use_clauses
