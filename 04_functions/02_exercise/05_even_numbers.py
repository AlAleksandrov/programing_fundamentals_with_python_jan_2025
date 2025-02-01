def only_the_even_numbers(number:int) -> bool:
    return number % 2 == 0


numbers = input().split()
numbers_as_digit = []
for number in numbers:
    numbers_as_digit.append(int(number))
result = list(filter(only_the_even_numbers, numbers_as_digit))
print(result)