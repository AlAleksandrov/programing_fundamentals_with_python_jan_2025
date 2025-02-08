string = input().split(', ')

sorted_string = sorted(string, key=lambda x: (-len(x), x))

print(sorted_string)