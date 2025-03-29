cities = {}

while True:
    commands = input()

    if commands == "Sail":
        break

    city, population, gold = commands.split("||")
    if city not in cities:
        cities[city] = {"Population": int(population), "Gold": int(gold)}
    else:
        cities[city]["Population"] += int(population)
        cities[city]["Gold"] += int(gold)

while True:
    events = input()

    if events == "End":
        break

    events = events.split("=>")
    event_type = events[0]

    if event_type == "Plunder":
        town, people, stealing_gold = events[1], events[2], events[3]
        cities[town]["Gold"] -= int(stealing_gold)
        cities[town]["Population"] -= int(people)
        print(f"{town} plundered! {stealing_gold} gold stolen, {people} citizens killed.")

        if cities[town]["Population"] <= 0 or cities[town]["Gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    elif event_type == "Prosper":
        town, gold_amount = events[1], events[2]
        if int(gold_amount) < 0:
            print("Gold added cannot be a negative number!")
            continue

        cities[town]["Gold"] += int(gold_amount)
        print(f"{gold_amount} gold added to the city treasury. {town} now has {cities[town]['Gold']} gold.")


if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, details in cities.items():
        print(f"{city} -> Population: {details['Population']} citizens, Gold: {details['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")