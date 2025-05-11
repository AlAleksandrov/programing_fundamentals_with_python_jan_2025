number = int(input())
type_colors = {}
type_names = {}

for num in range(number):
    command = input()
    type_color, name, damage, health, armor = command.split()

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    if type_color not in type_colors:
        type_colors[type_color] = [damage, health, armor, 1]
        type_names[type_color] = {name:[damage, health, armor]}
    else:
        if name not in type_names[type_color].keys():
            type_colors[type_color][0] += damage
            type_colors[type_color][1] += health
            type_colors[type_color][2] += armor
            type_colors[type_color][3] += 1
            type_names[type_color][name] = [damage, health, armor]
        else:
            type_colors[type_color][0] = type_colors[type_color][0] - type_names[type_color][name][0] + damage
            type_colors[type_color][1] = type_colors[type_color][1] - type_names[type_color][name][1] + health
            type_colors[type_color][2] = type_colors[type_color][2] - type_names[type_color][name][2] + armor
            type_names[type_color][name] = [damage, health, armor]


for color, attributes in type_colors.items():
    attributes[0] = float(attributes[0] / attributes[3])
    attributes[1] = float(attributes[1] / attributes[3])
    attributes[2] = float(attributes[2] / attributes[3])
    print(f"{color}::({attributes[0]:.2f}/{attributes[1]:.2f}/{attributes[2]:.2f})")
    sorted_type_names = sorted(type_names[color].items())
    for current_name, attributes in sorted_type_names:
        current_damage, current_health, current_armor = attributes[0], attributes[1], attributes[2]
        print(f"-{current_name} -> damage: {current_damage}, health: {current_health}, armor: {current_armor}")