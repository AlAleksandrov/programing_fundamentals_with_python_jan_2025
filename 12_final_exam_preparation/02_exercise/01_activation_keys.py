def contains(activation_key_:str, substring_list:str) ->str:
    if substring_list not in activation_key_:
        return "Substring not found!"
    return f"{activation_key_} contains {substring_list}"

def flip(activation_key_:str, upper_lower_:str, start_index_:int, end_index_:int) ->str:
    middle = ""
    if upper_lower_ == "Upper":
        middle = activation_key_[start_index_:end_index_].upper()
    elif upper_lower_ == "Lower":
        middle = activation_key_[start_index_:end_index_].lower()
    activation_key_ = activation_key_[:start_index_] + middle + activation_key_[end_index_:]
    return activation_key_

def slicer(activation_key_, start_index_, end_index_):
    before_string = activation_key_[:start_index_]
    after_string = activation_key_[end_index_:]
    activation_key_ = before_string + after_string
    return activation_key_

def main(activation_key:str, command_line:str) -> str:
    while True:
        command_line = command_line.split(">>>")
        if command_line[0] == "Generate":
            return f"Your activation key is: {activation_key}"
        if command_line[0] == "Contains":
            substring = command_line[1]
            current_result = contains(activation_key, substring)
            print(current_result)
        elif command_line[0] == "Flip":
            upper_lower, start_index, end_index = command_line[1], int(command_line[2]), int(command_line[3])
            activation_key = flip(activation_key, upper_lower, start_index, end_index)
            print(activation_key)
        elif command_line[0] == "Slice":
            start_index, end_index = int(command_line[1]), int(command_line[2])
            activation_key = slicer(activation_key, start_index, end_index)
            print(activation_key)

        command_line = input()


raw_activation_key = input()
command = input()
result = main(raw_activation_key, command)
print(result)