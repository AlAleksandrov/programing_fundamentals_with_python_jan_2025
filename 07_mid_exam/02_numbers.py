sequence_of_numbers = list(map(int, input().split()))
command = input().split()

while command[0] != 'Finish':
    if command[0] == 'Add':
        value = int(command[1])
        sequence_of_numbers.append(value)
    elif command[0] == 'Remove':
        value = int(command[1])
        if value in sequence_of_numbers:
            sequence_of_numbers.pop(sequence_of_numbers.index(value))
    elif command[0] == 'Replace':
        value = int(command[1])
        replacement = int(command[2])
        if value in sequence_of_numbers:
            index = sequence_of_numbers.index(value)
            sequence_of_numbers[index] =  replacement
    elif command[0] == 'Collapse':
        value = int(command[1])
        sequence_of_numbers = [num for num in sequence_of_numbers if num >= value]

    command = input().split()


print(" ".join(map(str, sequence_of_numbers)))