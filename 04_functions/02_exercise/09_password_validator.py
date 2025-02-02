def is_valid_password(password:str) ->str:
    is_valid_long = False
    is_valid_consist = False
    is_valid_digits = False
    result = ""
    if 6 <= len(password) <= 10:
        is_valid_long = True
    else:
        result = f"Password must be between 6 and 10 characters\n"
    counter_letters = 0
    counter_digits = 0
    for string in password:
        if 65 <= ord(string) <= 90 or 97 <= ord(string) <= 122:
            counter_letters += 1
        if 48 <= ord(string) <= 57:
            counter_digits += 1
        if counter_digits >= 2:
            is_valid_digits = True
        if counter_letters + counter_digits == len(password):
            is_valid_consist = True
    if not is_valid_consist:
        result += f"Password must consist only of letters and digits\n"
    if not is_valid_digits:
        result += "Password must have at least 2 digits"
    if is_valid_long and is_valid_consist and is_valid_digits:
        result = "Password is valid"

    return result


current_password = input()
current_result = is_valid_password(current_password)
print(current_result)