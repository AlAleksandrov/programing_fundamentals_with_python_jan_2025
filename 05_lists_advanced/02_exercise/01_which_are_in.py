strings = input().split(", ")
substrings = input().split(", ")

result = []
for string in strings:
    for substring in substrings:
        if string in substring:
            result.append(string)
            break
print(result)