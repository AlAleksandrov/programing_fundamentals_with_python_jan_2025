def move(current_message:str, current_number_of_letters:int) -> str:
    current_message = current_message[current_number_of_letters:] + current_message[:current_number_of_letters]
    return current_message

def inserting(current_message, current_index, current_value):
    current_message = current_message[:current_index] + current_value + current_message[current_index:]
    return current_message

def change_all(current_message, current_substring, current_replacement):
    current_message = current_message.replace(current_substring, current_replacement)
    return current_message

def main(message:str) -> str:
    while True:
        commands = input().split("|")
        action = commands[0]
        if action == "Decode":
            return message
        if action == "Move":
            number_of_letters = int(commands[1])
            message = move(message, number_of_letters)
        elif action == "Insert":
            index, value = int(commands[1]), commands[2]
            message = inserting(message, index, value)
        elif action == "ChangeAll":
            substring, replacement = commands[1], commands[2]
            message = change_all(message, substring, replacement)


string = input()
result = main(string)
print(f"The decrypted message is: {result}")