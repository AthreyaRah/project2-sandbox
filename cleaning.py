import re, argparse
from pathlib import Path
import csv

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
        return "",status, reason

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("raw_string")
    # args = parser.parse_args()
    # print(normalize_merchant(args.raw_string))

    cols = read_input("dummy_expenses.csv")
    print(detect_columns(cols[0]))


def read_input(filepath):
    filepath = Path(filepath)
    with open(filepath,"r") as f:
        reader = csv.reader(f)
        header = next(reader)
        total_columns = len(header)
        columns = [[] for _ in range(total_columns)]
        for row in reader:
            for i in range(0,len(row)):
                columns[i].append(row[i])

    return columns



def is_date(value: str) -> bool:
    return re.match(r"\d{2}-\d{2}-\d{4}$|\d{4}-\d{2}-\d{2}$|\d{2}/\d{2}/\d{4}$|\d{4}/\d{2}/\d{2}$|\d{2}-\d{2}-\d{2}$|\d{2}/\d{2}/\d{2}$",value) is not None

def is_amount(value: str) -> bool:
    return re.match(r"(\d+,)*\d+(\.\d+)*$",value) is not None


def detect_columns(column_values: list[str]) -> str:
    type_count_dict = {"date" : 0, "amount" : 0, "description" : 0}
    for value in column_values:
        if is_date(value):
            type_count_dict["date"] += 1
        elif is_amount(value):
            type_count_dict["amount"] += 1
        else:
            type_count_dict["description"] += 1
    return max(type_count_dict,key = type_count_dict.get)


if __name__ == '__main__':
    main()

