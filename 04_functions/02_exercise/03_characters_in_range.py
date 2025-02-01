def single_string_with_all_the_characters_in_between_them(first: str, second: str) -> list:
    list_string = []
    for number_char in range(ord(first) + 1, ord(second)):
        list_string.append(chr(number_char))
    return list_string


first_character = input()
second_character = input()
single_string = single_string_with_all_the_characters_in_between_them(first_character, second_character)
print(" ".join(single_string))