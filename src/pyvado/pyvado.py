from itertools import chain, repeat
from pathvalidate import is_valid_filepath
from os import path
import re

# security measure against buffer overflows attack
MAXIMUM_TOP_MODULE_LENGTH = 100

RTL_FILE_PATH = next(filter(lambda x: (re.match(".*\\.vhd|.*\\.v", x)),
                            filter(lambda x: (path.exists(path.normpath(x))),
                                   filter(is_valid_filepath,
                                          map(input,
                                              chain(["Enter RTL file: "],
                                                    repeat("File not valid, "
                                                           "ensure it has the "
                                                           "correct extension "
                                                           "(.vhd or .v) "
                                                           "and that there "
                                                           "are no typo "
                                                           "in the path\n"
                                                           "try again: ")))))))
if(re.match(".*\\.vhd", RTL_FILE_PATH)):
    SRC_LANG = "VHDL"
else:
    SRC_LANG = "VERILOG"

TOP_MODULE = next(filter(lambda x: len(x) < MAXIMUM_TOP_MODULE_LENGTH,
                         map(input, chain(["Enter top module name: "],
                                          repeat("Invalid module name "
                                                 "(too long, " +
                                                 str(MAXIMUM_TOP_MODULE_LENGTH)
                                                 + " max)\n"
                                                 "try again: ")))))
