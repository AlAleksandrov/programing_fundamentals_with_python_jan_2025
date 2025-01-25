my_list = input().split()
count_of_shuffles = int(input())
shuffled_list = my_list.copy()

for counter in range(count_of_shuffles):
    number = len(shuffled_list) // 2
    for index in range(len(shuffled_list) - 3):
        if index % 2 == 0:
            moved_card = shuffled_list.pop(number)
            shuffled_list.insert(index + 1, moved_card)
            number += 1

print(shuffled_list)