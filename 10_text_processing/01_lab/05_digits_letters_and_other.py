string = input()
all_digits = ""
all_letters = ""
all_other_characters = ""

for char in string:
    if char.isdigit():
        all_digits += char
    elif char.isalpha():
        all_letters += char
    else:
        all_other_characters += char

print(all_digits)
print(all_letters)
print(all_other_characters)