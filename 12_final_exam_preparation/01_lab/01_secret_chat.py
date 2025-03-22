def insert_space(message_:str, index_:int):
    message_ = message_[:index_] + " " + message_[index_:]
    return message_

def reverse(message_:str, substring_:str):
    if substring_ in message_:
        message_ = message_.replace(substring_,"",1) + substring_[::-1]
        return message_
    else:
        return "error"

def change_all(message_:str, substring_:str, replacement_:str):
    message_ = message_.replace(substring_, replacement_)
    return message_

def main(message_:str, command_:str):
    while True:
        action = command_.split(':|:')
        if action[0] == "Reveal":
            return message_
        if action[0] == "InsertSpace":
            index = int(action[1])
            message_ = insert_space(message_, index)
        elif action[0] == "Reverse":
            substring = action[1]
            message_probe = reverse(message_, substring)
            if message_probe != "error":
                message_ = message_probe
            else:
                print("error")
                command_ = input()
                continue
        elif action[0] == "ChangeAll":
            substring, replacement = action[1], action[2]
            message_ = change_all(message_, substring, replacement)

        print(message_)
        command_ = input()


message = input()
command = input()
result = main(message, command)
print(f"You have a new text message: {result}")