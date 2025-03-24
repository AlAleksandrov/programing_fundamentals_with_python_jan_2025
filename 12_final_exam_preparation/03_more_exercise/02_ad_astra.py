import re

string = input()

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"

matches = list(re.finditer(pattern, string))
calories = sum(int(match.group(4)) for match in matches)
days = calories // 2000
print(f"You have food to last you for: {days} days!")

for match in matches:
    food = match.group(2)
    date = match.group(3)
    current_calories = match.group(4)
    print(f"Item: {food}, Best before: {date}, Nutrition: {current_calories}")