import re
number = int(input())
numbers = []
command = ""
for _ in range(number):
    string = input()
    pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

    matches = re.findall(pattern, string)
    if matches:
        for match in matches:
            command, number_string = match
            [numbers.append(str(ord(char))) for char in number_string]
        print(f"{command}: {' '.join(numbers)}")
    else:
        print("The message is invalid")