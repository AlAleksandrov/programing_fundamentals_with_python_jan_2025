string = input().split(", ")
index_even_numbers = []

for index, num in enumerate(string):
    if int(num) % 2 == 0:
        index_even_numbers.append(index)

print(index_even_numbers)