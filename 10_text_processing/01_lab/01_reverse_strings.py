word = input()

while word != "end":
    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")

    word = input()