dwarfs = []
color_count = {}
dwarf_index = {}

while True:
    command = input()
    if command == "Once upon a time":
        break
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    key = (name, color)
    if key not in dwarf_index:
        dwarf_index[key] = len(dwarfs)
        dwarfs.append([name, color, physics])
        color_count[color] = color_count.get(color, 0) + 1
    else:
        idx = dwarf_index[key]
        if physics > dwarfs[idx][2]:
            dwarfs[idx][2] = physics

dwarfs.sort(key=lambda x: (-x[2], -color_count[x[1]], dwarf_index[(x[0], x[1])]))
for name, color, physics in dwarfs:
    print(f"({color}) {name} <-> {physics}")