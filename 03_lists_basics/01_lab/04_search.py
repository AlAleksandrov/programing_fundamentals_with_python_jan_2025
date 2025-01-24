number = int(input())
word = input()
strings_list = []
filtered_list = []

for index in range(number):
    strings = input()
    strings_list.append(strings)
    if word in strings:
        filtered_list.append(strings)

print(strings_list)
print(filtered_list)