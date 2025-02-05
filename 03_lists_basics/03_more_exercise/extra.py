def josephus_permutation(people_list: list, number:int) -> list:
    execution_list = []
    counter = - number
    while len(people_list) > 0:
        if number == 0:
            return []
        if len(people_list) == 1:
            for j in range(len(people_list)):
                execution_list.append(people_list[j])
                people_list.pop(j)
        elif len(people_list) == 2:
            if number % 2 == 0:
                for j in range(len(people_list)):
                    execution_list.append(people_list[j + 1])
                    people_list.pop(j + 1)
                    break
            else:
                for j in range(len(people_list)):
                    execution_list.append(people_list[j])
                    people_list.pop(j)
                    break
        else:
            if len(people_list) < number:
                for index in range(len(people_list)):
                    counter += 1
                    if counter == 0:
                        execution_list.append(people_list[index])
                        people_list.remove(people_list[index])
                        counter = - number - index
                        break
            else:
                for index in range(number - 1, len(people_list)):
                    if index == number - 1:
                        people = people_list.pop(index)
                        execution_list.append(int(people))
                        for i in range(index, len(people_list)):
                            if i >= number - 1:
                                people_list.insert(i - (number - 1), people_list[i])
                                people_list.pop(i + 1)
                            if i == len(people_list) - 1:
                                break
                        break
    return execution_list


count = 0
people_in_the_circle = input().split()
executions_number = int(input())
people_by_order_of_executions = josephus_permutation(people_in_the_circle, executions_number)

print("[", end="")
for people_for_execution in people_by_order_of_executions:
    count += 1
    if len(people_by_order_of_executions) != count:
        print(f"{people_for_execution}", end=",")
    else:
        print(f"{people_for_execution}]")