array_with_integers = list(map(int, input().split()))
commands = input().split()

while commands[0] != 'end':
    if commands[0] == 'swap':
        index_one, index_two = int(commands[1]), int(commands[2])
        array_with_integers[index_one], array_with_integers[index_two] = array_with_integers[index_two], array_with_integers[index_one]
    elif commands[0] == 'multiply':
        index_one, index_two = int(commands[1]), int(commands[2])
        array_with_integers[index_one] *= array_with_integers[index_two]
    elif commands[0] == 'decrease':
        array_with_integers = [num - 1 for num in array_with_integers]

    commands = input().split()
print(", ".join(map(str, array_with_integers)))