def func(string, word):
    if string == "int":
        return str(int(word) * 2)
    elif string == "real":
        return f"{float(word) * 1.5:.2f}"
    else:
        return f"${word}$"



data_type = input()
current_input = input()
result = func(data_type, current_input)
print(result)