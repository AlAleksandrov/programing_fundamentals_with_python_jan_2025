string = input()

while True:
    commands = input()
    if commands == "End":
        break

    command = commands.split()

    if command[0] == "Translate":
        char, replacement = command[1], command[2]
        string = string.replace(char, replacement)
        print(string)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif command[0] == "Start":
        substring = command[1]
        if string.startswith(substring):
            print("True")
        else:
            print("False")

    elif command[0] == "Lowercase":
        string = string.lower()
        print(string)

    elif command[0] == "FindIndex":
        char = command[1]
        print(string.rindex(char))

    elif command[0] == "Remove":
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)