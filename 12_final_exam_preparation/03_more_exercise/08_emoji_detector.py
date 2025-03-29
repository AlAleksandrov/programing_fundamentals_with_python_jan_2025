import re
emoji_dict = {}
cool_threshold = 1
text = input()
pattern_digits = r"(\d)"
matches_digits = list(re.findall(pattern_digits, text))

for match in matches_digits:
    cool_threshold *= int(match)

print(f"Cool threshold: {cool_threshold}")
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = list(re.finditer(pattern, text))
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    coolness = 0
    for char in match[2]:
        coolness += ord(char)
    emoji_dict[match[2]] = coolness
    if coolness >= cool_threshold:
        print(f"{match[0]}")
