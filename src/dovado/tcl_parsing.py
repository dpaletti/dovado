import re
from pathlib import Path


def fill_frame(tcl_frame_path, replacements, placeholder, out_path):
    # TODO make this work both with verilog and vhdl at the same time
    # Care that there may be nested folder, this must be handled
    # Both synthesis and implementation may be taken into account
    # check that here and in main is correct
    try:
        tcl_out = re.sub(
            placeholder,
            lambda m, r=iter(replacements): next(r),
            Path(tcl_frame_path).open("r").read(),
        )
        Path(out_path).write_text(tcl_out)

    except IOError as e:
        raise IOError(
            "Failed while opening or writing file:\n"
            + out_path
            + "\nIOError:\n"
            + str(e)
        )
