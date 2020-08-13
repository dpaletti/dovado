import re
from bs4 import BeautifulSoup
from pathlib import Path


def get_utilisation(
    utilization_metrics, titles, report_path, column_name, row_name
):
    if len(utilization_metrics) != len(titles):
        raise ValueError(
            "Length mismatch between utilization_metrics and titles"
            + "\nUtilization: "
            + str(utilization_metrics)
            + "\nTitles: "
            + str(titles)
        )
    row_name_to_title = dict(zip(utilization_metrics, titles))
    try:
        report = BeautifulSoup(Path(report_path).open(), "lxml-xml")
        section = report("section", {"title": row_name_to_title[row_name]})[0]
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
    except Exception as e:
        raise Exception(str(e))


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
    except Exception as e:
        raise Exception(str(e))
