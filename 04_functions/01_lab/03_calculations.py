def calculator(function, number_one, number_two):
    if function == "multiply":
        return number_one * number_two
    elif function == "divide":
        if number_two != 0:
            return int(number_one / number_two)
        else:
            return "None"
    elif function == "add":
        return number_one + number_two
    elif function =="subtract":
        return number_one - number_two

operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(operator, first_number, second_number))