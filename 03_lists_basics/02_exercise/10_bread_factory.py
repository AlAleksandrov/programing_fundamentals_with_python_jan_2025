working_day_events = input().split("|")
current_energy = 100
current_coins = 100
is_closed = False
for event in working_day_events:
    command = event.split("-")
    event_ingredient, value = command[0], int(command[1])
    if event_ingredient == "rest":
        initial_energy = current_energy
        current_energy += value
        if current_energy > 100:
            current_energy = 100
        gained_energy = current_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_ingredient == "order":
        if current_energy >= 30:
            current_coins += value
            current_energy -= 30
            print(f"You earned {value} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if current_coins >= value:
            current_coins -= value
            print(f"You bought {event_ingredient}.")
        else:
            is_closed = True
            break
if is_closed:
    print(f"Closed! Cannot afford {event_ingredient}.")
else:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")