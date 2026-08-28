import re

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


print(normalize_merchant("SWIGGY*ORDER8827"))
print(normalize_merchant("AMAZON PAY"))
print(normalize_merchant("1234567890"))

