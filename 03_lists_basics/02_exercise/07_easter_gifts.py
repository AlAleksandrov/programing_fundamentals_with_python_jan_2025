gifts = input().split()
all_command = input()

while all_command !="No Money":
    command = all_command.split()
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"
    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":
        if gifts:
            gifts[-1] = command[1]
    all_command = input()

i = 0
for element in gifts:
    i += 1
    if element != "None":
        if len(gifts) != i:
            print(element, end = " ")
        else:
            print(element)