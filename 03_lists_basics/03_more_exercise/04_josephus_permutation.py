def josephus_permutation(people_list: list, number: int) -> list:
    if number == 0:
        return []

    result = []
    index = 0
    temp_list = people_list.copy()

    while temp_list:
        if len(temp_list) == 1:
            result.append(temp_list.pop(0))
            break

        index = (index + number - 1) % len(temp_list)
        result.append(temp_list.pop(index))

    return result


people_in_the_circle = input().split()
executions_number = int(input())
people_by_order_of_executions = josephus_permutation(people_in_the_circle, executions_number)

print("[", end="")
print(",".join(map(str, people_by_order_of_executions)), end="]")