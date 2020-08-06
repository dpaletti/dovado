import re
from pathlib import Path


def fill_frame(tcl_frame_path, replacements, placeholder, out_path):
    try:
        tcl_out = re.sub(placeholder,
                         lambda m, r=iter(replacements): next(r),
                         Path(tcl_frame_path).open("r").read())
        Path(out_path).write_text(tcl_out)

    except IOError as e:
        print("Failed while opening or writing file:\n"
              + out_path
              + "\nIOError:\n" + str(e))
        exit(1)
