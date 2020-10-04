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
import io
import yaml
from pathlib import Path
from enum import Enum, auto
from dataclasses import dataclass


class RTL(Enum):
    VHDL = auto()
    VERILOG = auto()
    SYSTEM_VERILOG = auto()


class StopStep(Enum):
    SYNTHESIS = auto()
    IMPLEMENTATION = auto()


class ImplementationStep(Enum):
    PLACE = auto()
    ROUTE = auto()


@dataclass
class IsIncremental:
    synthesis: bool = True
    implementation: bool = True


CONFIG = yaml.safe_load(Path("config.yaml").open())

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
        except ParseException as e:
            raise ValueError(
                "Could not parse " + src_path_string + " as VHDL\n" + str(e)
            )
    elif src_path.suffix == ".v":
        try:
            parsed = HdlConvertor().parse(
                src_path_string,
                Language.VERILOG,
                [],
                hierarchyOnly=False,
                debug=True,
            )
        except ParseException as e:
            raise ValueError(
                "Could not parse "
                + str(src_path)
                + " as Verilog, .v files must be Verilog,"
                + " SystemVerilog files must be .sv\n"
                + str(e)
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


def is_to_box(src_path, stop_step):
    if stop_step is not StopStep.SYNTHESIS:
        return True
    if src_path.suffix == ".sv" or ".v":
        return True
    if not _is_parsed(src_path):
        parse(src_path)
    out_path = "vhdl/local_test_copy.vhd"
    write_to_file(out_path)
    try:
        parse(out_path)
        return False
    except Exception:
        return False


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


def get_parameter_range(parameter):
    # this method only works with VHDL parameters
    if isinstance(parameter.type, HdlOp):
        # case in which a range is specified
        if parameter.type.ops[1].fn.name != "TO":
            raise Exception(
                "Only 'to' is supported as an operation"
                + " for parameter range specification, input: "
                + str(parameter.type.ops[1].fn)
            )
        return tuple(parameter.type.ops[1].ops)
    try:
        return {
            "integer": (-CONFIG["INTEGER_HIGH"], CONFIG["INTEGER_HIGH"]),
            "natural": (0, CONFIG["INTEGER_HIGH"]),
            "positive": (1, CONFIG["INTEGER_HIGH"]),
            "signed": (-CONFIG["INTEGER_HIGH"], CONFIG["INTEGER_HIGH"]),
            "unsigned": (0, CONFIG["INTEGER_HIGH"]),
        }[str(parameter.type).lower()]
    except Exception as e:
        raise Exception(
            "Unsupported type: " + str(parameter.type).lower() + "\n" + str(e)
        )


added = False


def _add_dont_touch():
    global added
    if added:
        return
    for o in parsed.objs:
        if isinstance(o, HdlModuleDef):
            for def_o in o.objs:
                if isinstance(def_o, HdlCompInst):
                    def_o.module_name = HdlValueId(
                        '(* dont_touch  = "true" *) ' + str(def_o.module_name)
                    )
                    added = True
                    return


def write_to_file(out_path, no_touch=False):
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

            if not no_touch:
                ToVhdl2008(f).visit_HdlContext(parsed)
            else:
                stream = io.StringIO()
                ToVhdl2008(stream).visit_HdlContext(parsed)
                lines = [line for line in stream.getvalue().split("\n")]
                index = None
                for line in lines:
                    if line.lower() == "architecture box_arch of box is":
                        index = lines.index(line)
                if index:
                    lines.insert(index + 1, "attribute DONT_TOUCH : string;")
                    lines.insert(
                        index + 2,
                        'attribute DONT_TOUCH of BOXED : label is "TRUE";',
                    )
                f.write("\n".join(lines))
        else:
            if no_touch:
                _add_dont_touch()
            ToVerilog2005(f).visit_HdlContext(parsed)
    global parsed_src_path
    parsed_src_path = out_path


def get_parameter_on_name(src_path, module, parameter):
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec) and o.name == module:
            for param in o.params:
                if param.name == parameter:
                    return param

        if isinstance(o, HdlModuleDef) and o.dec and o.dec.name == module:
            for param in o.dec.params:
                if param.name == parameter:
                    return param


def set_parameter(src_path, module, parameter, value):
    # value must be base 10
    if not _is_parsed(src_path):
        parse(src_path)
    for o in parsed.objs:
        if isinstance(o, HdlModuleDec) and o.name == module:
            for param in o.params:
                if param.name == parameter.name:
                    param.value = HdlValueInt(value, None, None)

        if isinstance(o, HdlModuleDef) and o.dec and o.dec.name == module:
            for param in o.dec.params:
                if param.name == parameter.name:
                    param.value = HdlValueInt(value, None, None)

    write_to_file(src_path)


def map_parameter(src_path, module, parameter, value):
    print(
        "MAPPING PARAMETER: "
        + str(src_path)
        + "  "
        + str(module)
        + "  "
        + str(parameter)
        + "  "
        + str(value)
    )
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
                        if str(param.ops[0]) == parameter:
                            param.ops[1] = HdlValueInt(value, None, None)
                            write_to_file(src_path, no_touch=True)
                            return
        if isinstance(o, HdlModuleDec):
            for module_definition in o.objs:
                if (
                    isinstance(module_definition, HdlCompInst)
                    and module_definition.param_map
                ):
                    for param in module_definition.param_map:
                        if str(param.ops[0]) == parameter:
                            param.ops[1] = HdlValueInt(value, None, None)
                            write_to_file(src_path, no_touch=True)
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
