string = input()
strength = 0
new_string = ""

for i, ch in enumerate(string):
    if ">" in ch:
        strength += int(string[i + 1])
        new_string += ch
    elif ch.isalpha():
        if strength > 0:
            strength -= 1
        else:
            new_string += ch
    else:
        strength -= 1

print(new_string)