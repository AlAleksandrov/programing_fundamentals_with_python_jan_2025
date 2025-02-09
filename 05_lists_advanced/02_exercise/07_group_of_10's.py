sequence_of_numbers = input().split(", ")
group = 0

while sequence_of_numbers:
    group += 10
    list_of_numbers = []
    for number in sequence_of_numbers:
        if int(number) <= group:
            list_of_numbers.append(int(number))

    print(f"Group of {group}'s: {list_of_numbers}")
    sequence_of_numbers = [num for num in sequence_of_numbers if int(num) > group]