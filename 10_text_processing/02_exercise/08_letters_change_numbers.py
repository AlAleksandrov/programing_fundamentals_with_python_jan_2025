strings = input().split()
total_sum = 0
number = 0

for string in strings:
    front_letter = string[0]
    back_letter = string[-1]
    number = int(string[1:len(string) - 1])
    if front_letter.isupper():
        divide = ord(front_letter) - 64
        total_sum += number / divide
    elif front_letter.islower():
        multiply = ord(front_letter) - 96
        total_sum += number * multiply
    if back_letter.isupper():
        subtract = ord(back_letter) - 64
        total_sum -= subtract
    elif back_letter.islower():
        add = ord(back_letter) - 96
        total_sum += add

print(f"{total_sum:.2f}")