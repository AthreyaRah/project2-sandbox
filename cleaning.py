import re, argparse

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

    print(is_date("26-08-31"))
    print(is_amount("0.09"))

    print(detect_columns(["31-08-2026", "01-01-25", "15/06/2024", "31-08-2026"]))
    print(detect_columns(["1,234.50", "0", "USD 300", "45.00"]))


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

