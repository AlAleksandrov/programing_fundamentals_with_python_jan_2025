chest = input().split("|")
initial_treasure_chest = chest.copy()
command = input()
items = []
steal_ = []
summarize = 0

while command != "Yohoho!":
    command_one = command.split(" ")[0]
    items = command.split(" ")[1:]

    if command_one == "Loot":
        for item in items:
            if item not in initial_treasure_chest:
                initial_treasure_chest.insert(0, item)

    elif command_one == "Drop":
        if 0 <= int(items[0]) < len(initial_treasure_chest):
            initial_treasure_chest.append(initial_treasure_chest.pop(int(items[0])))

    elif command_one == "Steal":
        count = int(items[0])
        if count >= len(initial_treasure_chest):
            steal_ = initial_treasure_chest[:]
            initial_treasure_chest.clear()
        else:
            steal_ = initial_treasure_chest[-count:]
            initial_treasure_chest = initial_treasure_chest[:-count]
        print(", ".join(steal_))

    command = input()

if len(initial_treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    summarize = sum(len(item) for item in initial_treasure_chest)
    print(f"Average treasure gain: {summarize/len(initial_treasure_chest):.2f} pirate credits.")