def division_factorials(first:int,second:int) -> str:
    factorial_first = 1
    factorial_second = 1
    for digit_first in range(2, first + 1):
        factorial_first *= digit_first
    for digit_second in range(2, second + 1):
        factorial_second *= digit_second
    result = factorial_first / factorial_second
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
current_result = division_factorials(first_number, second_number)
print(current_result)