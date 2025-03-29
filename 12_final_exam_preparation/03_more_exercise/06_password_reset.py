string = input()

while True:
    commands = input()

    if commands == "Done":
        print(f"Your password is: {string}")
        break

    if commands == "TakeOdd":
        new_string = ""
        for index, char in enumerate(string):
            if index % 2 != 0:
                new_string += char
        string = new_string
        print(string)
        continue

    command = commands.split()
    if command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        string = string[:index] + string[index + length:]
        print(string)
    elif command[0] == "Substitute":
        substring, substitute = command[1],command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")