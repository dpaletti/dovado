from pathlib import Path
import re


def set_libs(frame_file_path, component_file_path):
    component_file = filter(lambda x: not re.match(r'^\s*$', x),
                            Path(component_file_path).open(
                                "r").read().split("\n").iter())
