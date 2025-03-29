import re
number = int(input())
for _ in range(number):
    string = input()
    pattern = r"@[#]+([A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+"
    matches = re.findall(pattern, string)
    if matches:
        digit = ""
        for match in matches:
            digit = "".join(re.findall(r"\d", match))
        if digit == "":
            digit = "00"
        print(f"Product group: {digit}")
    else:
        print("Invalid barcode")