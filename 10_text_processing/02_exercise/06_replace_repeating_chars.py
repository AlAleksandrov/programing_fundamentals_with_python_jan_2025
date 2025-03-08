string = input()
new_string = ""
char = ""

for ch in string:
    if char != ch:
        new_string += ch
        char = ch

print(new_string)