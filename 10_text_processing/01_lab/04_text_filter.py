banned_words = input().split(", ")
text = input()

for word in text:
    for words in banned_words:
        text = text.replace(words, "*" * len(words))

print(text)