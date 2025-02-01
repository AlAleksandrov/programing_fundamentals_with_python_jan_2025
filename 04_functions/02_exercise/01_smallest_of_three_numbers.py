def the_smallest_number(numbers: list) -> int:
    result = min(numbers)
    return result


number_one = int(input())
number_two = int(input())
number_tree = int(input())
number = the_smallest_number([number_one, number_two, number_tree])
print(number)