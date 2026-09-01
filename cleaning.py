# Reorganized purely for READ ORDER (top-to-bottom = call order).
# No logic changed from what you wrote and tested — just reordered.

import re, argparse
from pathlib import Path
import csv


def is_date(value: str) -> bool:
    return re.match(r"\d{2}-\d{2}-\d{4}$|\d{4}-\d{2}-\d{2}$|\d{2}/\d{2}/\d{4}$|\d{4}/\d{2}/\d{2}$|\d{2}-\d{2}-\d{2}$|\d{2}/\d{2}/\d{2}$", value) is not None


def is_amount(value: str) -> bool:
    return re.match(r"(\d+,)*\d+(\.\d+)?$", value) is not None


def detect_columns(column_values: list[str]) -> str:
    type_count_dict = {"date": 0, "amount": 0, "description": 0}
    for value in column_values:
        if is_date(value):
            type_count_dict["date"] += 1
        elif is_amount(value):
            type_count_dict["amount"] += 1
        else:
            type_count_dict["description"] += 1
    return max(type_count_dict, key=type_count_dict.get)


def get_column_type(columns: list[list[str]]) -> dict:
    column_type = {}
    for i in range(len(columns)):
        column_type[i] = detect_columns(columns[i])
    return column_type


def read_input(filepath):
    filepath = Path(filepath)
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        total_columns = len(header)
        columns = [[] for _ in range(total_columns)]
        for row in reader:
            for i in range(0, len(row)):
                columns[i].append(row[i])
    return columns


def read_mapping(mapping_filepath: str) -> dict:
    mapping_filepath = Path(mapping_filepath)
    with open(mapping_filepath, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        merchant_category = {}
        for row in reader:
            merchant_category[row[0]] = row[1]
    return merchant_category


def categorize_txn(description: str, merchant_dict: dict) -> str:
    for merchant, category in merchant_dict.items():
        search_result = re.search(r"\b" + merchant + r"\b", description, re.IGNORECASE)
        if search_result is not None:
            return category
    return "Other"


def normalize_merchant(raw_string: str) -> tuple[str, str, str]:
    raw_string = raw_string.lower()
    merchant = re.search(r"[a-z]+", raw_string)
    if merchant is not None:
        status = "ok"
        reason = ""
        return merchant.group(), status, reason
    else:
        status = "fail"
        reason = "Invalid merchant name"
        return "", status, reason


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("raw_string")
    # args = parser.parse_args()
    # print(normalize_merchant(args.raw_string))

    cols = read_input("dummy_expenses.csv")
    merchant_dict = read_mapping("merchant_mapping.csv")
    column_types = get_column_type(cols)

    category = []
    for column_idx, column_type in column_types.items():
        if column_type == "description":
            for row_val in cols[column_idx]:
                category.append(categorize_txn(row_val, merchant_dict))
    cols.append(category)

    print(cols)


if __name__ == '__main__':
    main()