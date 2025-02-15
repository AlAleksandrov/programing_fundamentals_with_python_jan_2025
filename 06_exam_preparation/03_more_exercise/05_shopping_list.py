initial_list = input().split("!")
commands = input()

while True:
    if commands == "Go Shopping!":
        break
    else:
        commands = commands.split()
    if commands[0] == "Urgent":
        item = commands[1]
        if item not in initial_list:
            initial_list.insert(0, item)

    elif commands[0] == "Unnecessary":
        item = commands[1]
        if item in initial_list:
            initial_list.remove(item)
    elif commands[0] == "Correct":
        item_old = commands[1]
        item_new = commands[2]
        if item_old in initial_list:
            initial_list[initial_list.index(item_old)] = item_new
    elif commands[0] == "Rearrange":
        item = commands[1]
        if item in initial_list:
            initial_list.append(initial_list.pop(initial_list.index(item)))

    commands = input()


print(", ".join(initial_list))