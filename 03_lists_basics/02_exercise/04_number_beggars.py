string_of_integers = input().split(", ")
count_of_beggars = int(input())
sum_of_every_beggar = []
start_index = 0

for counter in range(count_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(string_of_integers), count_of_beggars):
        current_beggar_sum += int(string_of_integers[index])

    start_index += 1
    sum_of_every_beggar.append(current_beggar_sum)

print(sum_of_every_beggar)