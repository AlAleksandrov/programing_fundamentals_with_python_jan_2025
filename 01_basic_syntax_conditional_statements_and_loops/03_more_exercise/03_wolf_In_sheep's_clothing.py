animals_string = input().split(", ")
is_wolf = False
index_wolf = 0
for index, animal in enumerate(animals_string):
    if animal == "wolf":
        is_wolf = True
        index_wolf = index - len(animals_string)
        if index_wolf == -1:
            print("Please go away and stop eating my sheep")
    else:
        if is_wolf:
            print(f"Oi! Sheep number {abs(index_wolf + 1)}! You are about to be eaten by a wolf!")
            break