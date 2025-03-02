characters = input()
my_dict = {}

for letter in characters:
    if letter != " ":
        if letter not in my_dict:
            my_dict[letter] = 0
        my_dict[letter] += 1

for char, occurrences in my_dict.items():
    print(f"{char} -> {occurrences}")