current_string = input()
index_list = []

for index, string in enumerate(current_string):
    if string.isupper():
        index_list.append(index)

print(index_list)