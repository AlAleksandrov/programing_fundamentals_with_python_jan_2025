strings = input().split(', ')
numbers = []
counter = 0
for string in strings:
    if int(string) == 0:
        counter += 1
    else:
        numbers.append(int(string))

if counter > 0:
    for digit in range(counter):
        numbers.append(0)

print(numbers)