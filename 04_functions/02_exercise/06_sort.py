string_of_numbers = input().split()
numbers_as_digit = []
for number in string_of_numbers:
    numbers_as_digit.append(int(number))

result = sorted(numbers_as_digit)
print(result)