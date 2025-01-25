factor = int(input())
count_number = int(input())
numbers = []

for multiplier in range(1, count_number + 1):
    numbers.append(multiplier * factor)

print(numbers)