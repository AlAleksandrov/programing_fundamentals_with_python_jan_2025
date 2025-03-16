import re

text = input()

while text:
    pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"
    match = re.search(pattern, text)
    if match:
        print("".join(match.group(1)))

    text = input()