sequence_of_numbers = input().split()
numbers_as_digit = []

for number in sequence_of_numbers:
    numbers_as_digit.append(int(number))

result_min = min(numbers_as_digit)
result_max = max(numbers_as_digit)
result_sum = sum(numbers_as_digit)
print(f"The minimum number is {result_min}")
print(f"The maximum number is {result_max}")
print(f"The sum number is: {result_sum}")