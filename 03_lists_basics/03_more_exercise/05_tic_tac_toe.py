numbers = []
result = ""
for x in range(3):
    row = input().split(" ")
    for y in range(3):
        numbers.append(int(row[y]))

winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

for combination in winning_combinations:
    if numbers[combination[0]] == numbers[combination[1]] == numbers[combination[2]] != 0:
        if numbers[combination[0]] == 1:
            result = "First player won"
            break
        elif numbers[combination[0]] == 2:
            result = "Second player won"
            break

if result:
    print(result)
else:
    print("Draw!")