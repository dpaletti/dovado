from bs4 import BeautifulSoup
from pathlib import Path
import re


def get_utilisation(report_path, title, column_name, row_name):
    try:
        report = BeautifulSoup(Path(report_path).open(), "lxml-xml")
        section = report('section', {"title": title})[0]
        rows = section('tablerow')
        header = rows[0]
        column = header("tableheader").index(
            header("tableheader", {"contents": column_name})[0])
        row = section('tablecell', {"contents":
                                    re.compile(" *" + row_name)})[0].parent()
        return float(row[column]["contents"])
    except FileNotFoundError as f:
        print("Wrong path: " + report_path + "\n"
              + "FileNotFoundError: " + str(f))
        return
    except IndexError as e:
        print("Calling parameters that could have caused this:\n"
              + title + "\n" + column_name + "\n" + row_name + "\n"
              + "IndexError message: " + str(e))


def get_wns_whs(report_path):
    try:
        first_line = Path(report_path).open().readline()
        return float(re.findall(r'\d.\d+', first_line)[0])
    except FileNotFoundError as f:
        print("Wrong path: " + report_path + "\n"
              + "FileNotFoundError: " + str(f))
        return
