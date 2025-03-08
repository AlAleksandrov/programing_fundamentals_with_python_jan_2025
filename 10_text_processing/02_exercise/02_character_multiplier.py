strings = input().split()
string_one, string_two = strings[0], strings[1]
total_sum = 0

if len(string_one) > len(string_two):
    for i in range(len(string_two)):
        total_sum += ord(string_one[i]) * ord(string_two[i])
    for i in range(len(string_two),len(string_one)):
        total_sum += ord(string_one[i])
elif len(string_one) < len(string_two):
    for i in range(len(string_one)):
        total_sum += ord(string_one[i]) * ord(string_two[i])
    for i in range(len(string_one), len(string_two)):
        total_sum += ord(string_two[i])
else:
    for i in range(len(string_two)):
        total_sum += ord(string_one[i]) * ord(string_two[i])

print(total_sum)