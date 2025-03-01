number = int(input())
dictionary = {}
for _ in range(number):
    key = input()
    value = input()
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += ", " + value

for key, value in dictionary.items():
    print(f"{key} - {value}")