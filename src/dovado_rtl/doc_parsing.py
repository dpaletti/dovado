import re
from typing import List
import dovado_rtl.vivado_interaction as vivado


def get_directives_paragraph(command: str) -> str:

    if command not in {"synthesis", "place", "route", "read checkpoint"}:
        raise ValueError(
            "get_directives_paragraph called with " + str(command)
        )
    if command == "synthesis":
        help = vivado.get_help("synth_design").strip()
    elif command == "place":
        help = vivado.get_help("place_design").strip()
    elif command == "route":
        help = vivado.get_help("route_design").strip()
    elif command == "read checkpoint":
        help = vivado.get_help("read_checkpoint").strip()
    else:
        raise Exception(
            "Unrecognized command in get_directives_paragraph: "
            + command
            + " available are: synthesis, place, route, read_checkpoint"
        )
    help = re.split("(\r\n?|\n)+", help)
    directive_index = help.index(
        [
            i
            for i in [i for i in help if re.search("-directive", i)]
            if re.search(r"-directive (\[.*\]|<arg>) -", i)
        ][0]
    )
    help_slice_from_directive = help[directive_index + 1 :]
    next_field_occurrences = [
        i
        for i in [
            i
            for i in help_slice_from_directive
            if re.search("-[a-zA-Z_]+[ \t]*(<arg>|<args>)?[ \t]*-[ \t]*", i)
        ]
        if i.strip()[0] == "-"
    ]
    return "".join(
        help[directive_index : help.index(next_field_occurrences[0])]
    ).strip()


def get_directives(directives_paragraph: str) -> List[str]:
    return [
        re.sub(r"\*|-| ", "", item)
        for sublist in [
            re.findall(r"\* .* -", i.strip())
            for i in re.split("(\r\n?|\n)+", directives_paragraph)
            if re.match(r"\*.*", i.strip())
        ]
        for item in sublist
    ]
