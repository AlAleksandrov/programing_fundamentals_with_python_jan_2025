secret_message = input().split()
ascii_value = 0
decipher_message = []
for string in secret_message:
    ascii_value_string = ""
    for char in string:
        if char.isdigit():
            ascii_value_string = ascii_value_string + char
    ascii_value = int(ascii_value_string)
    if len(string) - len(ascii_value_string) == 1:
        string = chr(ascii_value) + string[len(string) - 1:len(string):]
    else:
        string = chr(ascii_value) + string[len(string) - 1:len(string):] + string[len(ascii_value_string) + 1:len(string) - 1:] + string[len(ascii_value_string):len(ascii_value_string) + 1:]
    decipher_message.append(string)
print(" ".join(decipher_message))
