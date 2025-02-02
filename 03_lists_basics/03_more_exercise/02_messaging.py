sequence_of_numbers = input().split()
current_string = input()
string = []
for i, character in enumerate(current_string):
    string.append(character)
result = ""

for number in sequence_of_numbers:
    numbers_sum = 0
    for digit in number:
        numbers_sum += int(digit)
    if numbers_sum >= len(string):
        for index, char in enumerate(string):
            if index == numbers_sum - len(string):
                result += char
                string.remove(char)
                break
    else:
        for index, char in enumerate(string):
            if index == numbers_sum:
                result += char
                string.remove(char)
                break

print(result)