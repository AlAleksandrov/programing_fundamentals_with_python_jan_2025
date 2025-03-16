import re

string = input()
pattern = r"\s(([a-z0-9]+[-._]*[a-z0-9]+)@([a-z\-]+)(\.[a-z]+)+)\b"
matches = re.findall(pattern, string)

for match in matches:
    print("".join(match[0]))