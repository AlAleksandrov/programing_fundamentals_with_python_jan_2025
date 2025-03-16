import re

command = input()
furnitures = []
total_cost = 0.00

while command != "Purchase":
    pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)"
    bought_furniture = re.findall(pattern, command)
    if bought_furniture:
        furniture_name = bought_furniture[0][0]
        price = bought_furniture[0][1]
        quantity = bought_furniture[0][2]
        furnitures.append(furniture_name)
        total_cost += float(price) * int(quantity)

    command = input()
print("Bought furniture:")
for furniture in furnitures:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")