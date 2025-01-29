number_of_lines = int(input())
brackets_list = []
is_opening_bracket = False
is_closing_bracket = False
counter_balanced = 0
counter_unbalanced = 0
bracket = ""
is_unbalanced = False
is_balanced = False

for index in range(number_of_lines):
    string = input()
    if string == "(":
        brackets_list.append(string)
        if brackets_list.index(string) == - 1:
            is_unbalanced = True
            counter_unbalanced += 1
            break
        if is_opening_bracket:
            is_unbalanced = True
            counter_unbalanced += 1
            break
        else:
            is_opening_bracket = True
        counter_unbalanced += 1
        if is_closing_bracket:
            is_opening_bracket = False
            is_closing_bracket = False
            counter_balanced += 1
            counter_unbalanced -= 2
    if string == ")":
        brackets_list.append(string)
        if brackets_list.index(string) == 0:
            counter_unbalanced += 1
            is_unbalanced = True
            break
        if is_closing_bracket:
            is_unbalanced = True
            counter_unbalanced += 1
            break
        else:
            is_closing_bracket = True
        counter_unbalanced += 1
        if is_opening_bracket:
            is_opening_bracket = False
            is_closing_bracket = False
            counter_balanced += 1
            counter_unbalanced -= 2

if is_balanced or counter_balanced > counter_unbalanced and is_opening_bracket == is_closing_bracket:
    print("BALANCED")
elif is_unbalanced or counter_balanced <= counter_unbalanced and is_opening_bracket != is_closing_bracket:
    print("UNBALANCED")