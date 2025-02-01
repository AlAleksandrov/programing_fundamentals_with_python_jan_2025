def sum_numbers(one: int, two: int) -> int:
    return one + two


def subtract(result_sum: int, three: int) -> int:
    return result_sum - three


def add_and_subtract(one: int, two: int, three: int) -> int:
    returned_result = sum_numbers(one, two)
    total_result = subtract(returned_result, three)
    return total_result


number_one = int(input())
number_two = int(input())
number_three = int(input())
final_result = add_and_subtract(number_one, number_two, number_three)
print(final_result)