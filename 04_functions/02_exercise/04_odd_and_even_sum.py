def sum_all_even_odd_digits(given_number: int) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for string in str(given_number):
        digit = int(string)
        if digit % 2 == 0:
            sum_of_even_digits += digit
        else:
            sum_of_odd_digits += digit
    result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    return result


number = int(input())
current_result = sum_all_even_odd_digits(number)
print(current_result)