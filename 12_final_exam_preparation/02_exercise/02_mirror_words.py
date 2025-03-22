import re

string = input()

pattern = r"(@|#)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})"
matches = list(re.findall(pattern, string))

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

result = []
for match in matches:
    if match[1] == match[2][::-1]:
        result.append(f"{match[1]} <=> {match[2]}")

if result:
    print("The mirror words are:")
    print(', '.join(result))
else:
    print("No mirror words!")