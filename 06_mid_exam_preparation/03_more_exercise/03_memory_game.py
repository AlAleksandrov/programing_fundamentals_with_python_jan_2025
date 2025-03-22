sequence_of_elements = input().split()
command = list(map(int, input().split()))
number_of_moves_until_now = 0

while True:
    number_of_moves_until_now += 1
    index_one, index_two = command[0], command[1]

    if index_one == index_two or index_one not in range(len(sequence_of_elements)) or index_two not in range(len(sequence_of_elements)):
        if (len(sequence_of_elements)//2) % 2 == 0:
            index = len(sequence_of_elements) // 2
        else:
            index = (len(sequence_of_elements) - 1) // 2
        element = f"-{number_of_moves_until_now}a"
        sequence_of_elements.insert(index, element)
        sequence_of_elements.insert(index, element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[index_one] == sequence_of_elements[index_two]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[index_one]}!")
            if index_one > index_two:
                del sequence_of_elements[index_one]
                del sequence_of_elements[index_two]
            elif index_one < index_two:
                del sequence_of_elements[index_two]
                del sequence_of_elements[index_one]
        else:
            print("Try again!")

    if not sequence_of_elements:
        print(f"You have won in {number_of_moves_until_now} turns!")
        break

    command = input()

    if command == "end":
        print("Sorry you lose :(")
        print(f"{' '.join(sequence_of_elements)}")
        break
    else:
        command = list(map(int, command.split()))