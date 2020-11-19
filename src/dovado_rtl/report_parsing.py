import re
from pathlib import Path
from bs4 import BeautifulSoup
import numpy as np


def _represents_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def _get_percentage_util(columns, row):
    column_number = 0
    for column in columns:
        if column.get("contents") == "Util%":
            column_number = columns.index(column)
            break
    siebling = row
    if column_number > 0:
        for i in range(0, column_number - 1):
            siebling = siebling.findNext("tablecell")
    return siebling.findNext("tablecell").get("contents")


def get_available_indices(report_path):
    report = BeautifulSoup(Path(report_path).open(), "lxml-xml")
    indices = {}
    sections_partial = report.find_all("section")
    sections = []
    sections.extend(sections_partial)
    for section in sections:

        for nested_section in section.find_all("section"):
            nested_section.decompose()

        columns = []
        rows = []

        for column in (
            section.find("tablerow").find_all("tableheader")
            if section.find("tablerow")
            else []
        ):
            columns.append(column.get("contents").strip())
        if "Util%" in columns:
            for row in section.find_all("tablerow"):
                if row.find("tablecell") and _represents_float(
                    _get_percentage_util(section.find_all("tableheader"), row)
                ):
                    rows.append(row.find("tablecell").get("contents").strip())
            indices[section.get("title")] = rows

    return indices


def get_utilisation(report_path, section_name, row_name):
    report = BeautifulSoup(Path(report_path).open(), "lxml-xml")
    section = report.find("section", {"title": section_name})
    columns = section.find_all("tableheader")
    row = section.find(
        "tablecell",
        {"contents": re.compile("[ \t\r\n]*" + row_name + r"(\*)?[ \t\r\n]*")},
    )
    return float(_get_percentage_util(columns, row))


def get_wns(report_path) -> float:
    try:
        first_line = Path(report_path).open().readline()
        try:
            return float(
                re.findall(r"([-+]?(\d*\.\d*|inf))", first_line)[0][0]
            )
        except Exception:
            return np.inf

    except FileNotFoundError as f:
        raise FileNotFoundError(
            "Wrong path: "
            + report_path
            + "\n"
            + "FileNotFoundError: "
            + str(f)
        )
