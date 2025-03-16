import re

string = input()
word = input()
pattern = fr"\b{word}\b"
matches = re.findall(pattern, string, re.IGNORECASE)

print(len(matches))