the_sequence_of_targets = list(map(int,input().split()))
command = input()

while command != "End":
    commands = command.split()
    manipulator = commands[0]
    index, item = int(commands[1]), int(commands[2])

    if manipulator == "Shoot":
        if 0 <= index <= len(the_sequence_of_targets) - 1:
            the_sequence_of_targets[index] -= item
            if the_sequence_of_targets[index] <= 0:
                the_sequence_of_targets.pop(index)

    elif manipulator == "Add":
        if 0 <= index <= len(the_sequence_of_targets) - 1:
            the_sequence_of_targets.insert(index, item)
        else:
            print("Invalid placement!")

    elif manipulator == "Strike":
        if index - item >= 0 and index + item < len(the_sequence_of_targets):
            del the_sequence_of_targets[index - item:index + item + 1]
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, the_sequence_of_targets)))