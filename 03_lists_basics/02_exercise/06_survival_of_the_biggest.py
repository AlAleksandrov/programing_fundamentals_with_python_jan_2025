import sys
list_of_integers = input().split()
count_of_removed_numbers = int(input())
numbers = 0

for number in range(count_of_removed_numbers):
    smallest_one_number = sys.maxsize
    for index in range(len(list_of_integers)):
        if int(list_of_integers[index]) < smallest_one_number:
            smallest_one_number = int(list_of_integers[index])
    list_of_integers.remove(str(smallest_one_number))

for index1, number1  in enumerate(list_of_integers):
    numbers = int(number1)
    if index1 + 1 == len(list_of_integers):
        print(numbers)
    else:
        print(numbers, end =", ")