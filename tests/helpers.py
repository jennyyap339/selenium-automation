import csv
import json
import os
import openpyxl


def get_data_path(filename):
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        filename
    )

def read_csv_data():
    test_data = []
    with open(get_data_path("login_data.csv"), newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("skip", "False") == "True": # CSV needs string comparison
                continue # skip this row
            test_data.append((
                row["username"],
                row["password"],
                row["expected"],
                row["should_pass"] == "True"
            ))
    return test_data

def read_json_data():
    test_data = []
    with open(get_data_path("login_data.json"), newline='') as jsonfile:
        rows = json.load(jsonfile)
        for row in rows:
            if row.get("skip", False):
                continue # skip this row
            test_data.append((
                row["username"],
                row["password"],
                row["expected"],
                row["should_pass"]
            ))
    return test_data

def read_excel_data():
    test_data = []
    # Load the workbook
    workbook = openpyxl.load_workbook(get_data_path("login_data.xlsx"))
    sheet = workbook.active # Gets the currently active sheet — the first sheet by default
    # Read rows — skip the header row (row 1)
    for row in sheet.iter_rows(min_row=2, values_only=True): # start from row 2, return just the values not cell objects
        username, password, expected, should_pass, skip = row   # instead of row["username"] like CSV/JSON
                                                                # Excel uses position, not column names
        # Skip if marked True
        if skip: # Excel stores real booleans
            continue
        test_data.append((username, password, expected, should_pass))
    return test_data