import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from bs4 import BeautifulSoup
from bs4.element import PageElement, ResultSet
import numpy as np


def _represents_float(s: Any):
    try:
        float(s)
        return True
    except ValueError:
        return False


def _get_percentage_util(columns: ResultSet, row: PageElement) -> str:
    column_number = 0
    column: PageElement
    for column in columns:
        if str(column.get("contents")) == "Util%":
            column_number: int = int(columns.index(column))
            break
    siebling = row
    if column_number > 0:
        for _ in range(0, column_number - 1):
            siebling: Any = siebling.findNext("tablecell")
    return siebling.findNext("tablecell").get("contents")


def get_available_indices(report_path: str) -> Dict[str, List[str]]:
    report: BeautifulSoup = BeautifulSoup(
        Path(report_path).open(), "lxml-xml",
    )
    indices = {}
    sections_partial: ResultSet = report.find_all("section")
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


def get_utilisation(report_path: str, section_name: str, row_name: str):
    report: BeautifulSoup = BeautifulSoup(
        Path(report_path).open(), "lxml-xml",
    )
    section: PageElement = report.find("section", {"title": section_name})
    columns: ResultSet = section.find_all("tableheader")
    row: PageElement = section.find(
        "tablecell",
        {"contents": re.compile("[ \t\r\n]*" + row_name + r"(\*)?[ \t\r\n]*")},
    )
    try:
        return float(_get_percentage_util(columns, row))
    except Exception:
        return 0


def get_wns(report_path: str) -> float:
    try:
        first_line = Path(report_path).open().readline()
        try:
            return float(
                re.findall(r"([-+]?(\d*\.\d*|inf))", first_line)[0][0]
            )
        except Exception:
            return float(np.inf)

    except FileNotFoundError as f:
        raise FileNotFoundError(
            "Wrong path: "
            + report_path
            + "\n"
            + "FileNotFoundError: "
            + str(f)
        )
