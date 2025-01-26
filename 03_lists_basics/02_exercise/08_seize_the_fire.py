fires_with_their_cells = input().split("#")
amount_of_water = int(input())
type_of_fire = []
print("Cells:")
effort = 0.00
total_fire = 0

for i in range(len(fires_with_their_cells)):
    type_of_fire = fires_with_their_cells[i].split(" = ")
    if type_of_fire[0] == "High" and 81 <= int(type_of_fire[1]) <= 125:
        if amount_of_water - int(type_of_fire[1]) >= 0:
            amount_of_water -= int(type_of_fire[1])
        else:
            continue
        effort += 0.25 * int(type_of_fire[1])
        total_fire += int(type_of_fire[1])
        print(f" - {type_of_fire[1]}")
    elif type_of_fire[0] == "Medium" and 51 <= int(type_of_fire[1]) <= 80:
        if amount_of_water - int(type_of_fire[1]) >= 0:
            amount_of_water -= int(type_of_fire[1])
        else:
            continue
        effort += 0.25 * int(type_of_fire[1])
        total_fire += int(type_of_fire[1])
        print(f" - {type_of_fire[1]}")
    elif type_of_fire[0] == "Low" and 1 <= int(type_of_fire[1]) <= 50:
        if amount_of_water - int(type_of_fire[1]) >= 0:
            amount_of_water -= int(type_of_fire[1])
        else:
            continue
        effort += 0.25 * int(type_of_fire[1])
        total_fire += int(type_of_fire[1])
        print(f" - {type_of_fire[1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")