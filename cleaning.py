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
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_string")
    args = parser.parse_args()
    print(normalize_merchant(args.raw_string))


if __name__ == '__main__':
    main()

