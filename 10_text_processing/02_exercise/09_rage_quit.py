string = input()
new_string = ""
new_chars = ""
number = ""

for i, ch in enumerate(string):
    if ch.isalpha():
        new_chars += ch.upper()
    elif ch.isdigit():
        number += ch
        if i + 1 < len(string):
            if string[i + 1].isdigit():
                continue
        new_string += new_chars * int(number)
        new_chars = ""
        number = ""
    else:
        new_chars += ch.upper()

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)