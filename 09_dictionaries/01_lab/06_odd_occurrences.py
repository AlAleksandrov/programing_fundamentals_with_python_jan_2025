words = input().lower().split()
lst = []
for word in words:
    if words.count(word) % 2 != 0:
        if word not in lst:
            lst.append(word)

print(" ".join(lst))