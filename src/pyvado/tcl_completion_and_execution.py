from itertools import chain, repeat
from pathvalidate import is_valid_filepath
from os import path
import subprocess
import re
from pathlib import Path


def request_file(file_type, regexp_extension, message_extension):
    return next(filter(lambda x: (re.match(regexp_extension, x)),
                       filter(lambda x: (path.exists(path.normpath(x))),
                              filter(is_valid_filepath,
                                     map(input,
                                         chain(["Enter " + file_type
                                                + " file: "],
                                               repeat(
                                                   "File not valid, ensure it "
                                                   "has the correct extension "
                                                   "(" + message_extension
                                                   + ") and that there are no "
                                                   "typo in the path.\n"
                                                   "Try again: "
                                               )))))))


def request_identifier(identifier_type, identifier_max_length):
    return next(filter(lambda x: len(x) < identifier_max_length,
                       map(input, chain(["Enter " + identifier_type
                                         + " identifier: "],
                                        repeat("Invalid module name "
                                               "(too long, " +
                                               str(identifier_max_length)
                                               + " max)\n"
                                               "Try again: ")))))


def get_src_lang(rtl_file):
    if(re.match(".*\\.vhd", rtl_file)):
        return "VHDL"
    else:
        return "VERILOG"


def write_tcl_evaluation_script(replacements, src_lang, vhdl_path,
                                verilog_path, placeholder, out_path):
    try:
        if(src_lang == "VHDL"):
            tcl_evaluate_point = Path(vhdl_path).read_text()
        else:
            tcl_evaluate_point = Path(verilog_path).read_text()

        tcl_out = re.sub(placeholder,
                         lambda m, r=iter(replacements): next(r),
                         tcl_evaluate_point)
        Path(out_path).write_text(tcl_out)

    except IOError as e:
        print("Failed while opening or writing file:\n"
              + out_path
              + "\nIOError:\n" + str(e))
        exit(1)


def evaluate_tcl_script(out_path):
    subprocess.run(" vivado -mode batch -source " + out_path,
                   shell=True)
