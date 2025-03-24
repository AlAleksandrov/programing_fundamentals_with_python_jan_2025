def add_stop(current_string, current_index, current_add_string):
    current_string = current_string[:current_index] + current_add_string + current_string[current_index:]
    return current_string

def remove_stop(current_string, current_start_index, current_end_index):
    current_string = current_string[:current_start_index] + current_string[current_end_index + 1:]
    return current_string

def switch(current_string, current_old_string, current_new_string):
    current_string = current_string.replace(current_old_string, current_new_string)
    return current_string

def main(current_string):
    while True:
        commands = input().split(":")
        action = commands[0]
        if action == "Travel":
            return current_string
        if action == "Add Stop":
            index, add_string = int(commands[1]), commands[2]
            if index < len(current_string):
                current_string = add_stop(current_string, index, add_string)
        elif action == "Remove Stop":
            start_index, end_index = int(commands[1]), int(commands[2])
            if start_index < len(current_string) and end_index < len(current_string):
                current_string = remove_stop(current_string, start_index, end_index)
        elif action == "Switch":
            old_string, new_string = commands[1], commands[2]
            if old_string in current_string:
                current_string = switch(current_string, old_string, new_string)

        print(current_string)


trip = input()
result = main(trip)
print(f"Ready for world tour! Planned stops: {result}")