materials = {"shards":0,"fragments":0,"motes":0}
legendary_item = ""
obtained_legendary_item = False

while not obtained_legendary_item:
    action = input().split()
    for i in range(0, len(action),2):
        quantity = int(action[i])
        material = action[i + 1].lower()

        if material in materials:
            materials[material] += quantity
        else:
            materials[material] = quantity

        if materials["shards"] >= 250:
            legendary_item = "Shadowmourne"
            obtained_legendary_item = True
            materials[material] -= 250

        elif materials["fragments"] >= 250:
            legendary_item = "Valanyr"
            obtained_legendary_item = True
            materials[material] -= 250

        elif materials["motes"] >= 250:
            legendary_item = "Dragonwrath"
            obtained_legendary_item = True
            materials[material] -= 250

        if obtained_legendary_item:
            print(f"{legendary_item} obtained!")
            break


for material, quantity in materials.items():
    print(f"{material}: {quantity}")