def is_palindrome(given_number: int) -> bool:
    current_result = False
    list_given_number = []
    for digit in str(given_number):
        list_given_number.append(int(digit))
    for index in range(len(list_given_number)):
        if list_given_number[index] != list_given_number[len(list_given_number) - index - 1]:
            current_result = False
            break
        else:
            current_result = True
            if len(list_given_number) - 2 == 1:
                break
    return current_result


list_of_positive_integers = input().split(", ")
for number in list_of_positive_integers:
    result = is_palindrome(int(number))
    print(result)