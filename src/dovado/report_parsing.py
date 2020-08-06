import re
from bs4 import BeautifulSoup
from pathlib import Path


def get_directives_paragraph(help, next_parameter):
    # next_parameter for synth_design is -rtl
    help = help.strip()
    help = re.split("(\r\n?|\n)+", help)
    directive_index = help.index(
        [
            i
            for i in [i for i in help if re.search("-directive", i)]
            if re.search("-directive <arg> -", i)
        ][0]
    )
    help_slice_from_directive = help[directive_index + 1 :]
    next_field_occurrences = [
        i for i in help_slice_from_directive if re.search(next_parameter, i)
    ]
    eventual_note = "".join(
        help[directive_index : help.index(next_field_occurrences[0])]
    ).strip()
    note_match = re.search("Note:", eventual_note)
    return eventual_note[: note_match.start()] if note_match else eventual_note


def get_directives(directives_paragraph):
    # TODO test with place and route
    return [
        re.sub(r"\*|-| ", "", item)
        for sublist in [
            re.findall(r"\* .* -", i.strip())
            for i in re.split("(\r\n?|\n)+", directives_paragraph)
            if re.match(r"\*.*", i.strip())
        ]
        for item in sublist
    ]


def get_utilisation(
    utilization_metrics, titles, report_path, column_name, row_name
):
    if len(utilization_metrics) != len(titles):
        raise ValueError(
            "Length mismatch between utilization_metrics and titles"
            + +"\nUtilization: "
            + str(utilization_metrics)
            + +"\nTitles: "
            + str(titles)
        )
    column_name_to_title = dict(zip(utilization_metrics, titles))
    try:
        report = BeautifulSoup(Path(report_path).open(), "lxml-xml")
        section = report(
            "section", {"title": column_name_to_title[column_name]}
        )[0]
        rows = section("tablerow")
        header = rows[0]
        column = header("tableheader").index(
            header("tableheader", {"contents": column_name})[0]
        )
        row = section("tablecell", {"contents": re.compile(" *" + row_name)})[
            0
        ].parent()
        return float(row[column]["contents"])
    except FileNotFoundError as f:
        raise FileNotFoundError(
            "Wrong path: "
            + report_path
            + "\n"
            + "FileNotFoundError: "
            + str(f)
        )
    except IndexError as e:
        raise IndexError(
            "Failed parsing utilization report"
            + "Calling parameters that could have caused this"
            + "\n"
            + column_name
            + "\n"
            + row_name
            + "\n"
            + "IndexError message: "
            + str(e)
        )


def get_wns(report_path):
    try:
        first_line = Path(report_path).open().readline()
        return float(re.findall(r"\d.\d+", first_line)[0])
    except FileNotFoundError as f:
        raise FileNotFoundError(
            "Wrong path: "
            + report_path
            + "\n"
            + "FileNotFoundError: "
            + str(f)
        )
