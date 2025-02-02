def is_perfect_number(positive_integer:int) -> str:
    sum_digits = 0
    for digit in range(1, positive_integer):
        if positive_integer % digit == 0:
            sum_digits += digit
    if positive_integer == sum_digits:
        result = "We have a perfect number!"
    else:
        result = "It's not so perfect."
    return result


number = int(input())
current_result = is_perfect_number(number)
print(current_result)