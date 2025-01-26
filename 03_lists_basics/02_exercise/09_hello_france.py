collection_of_items = input().split("|")
budget = float(input())
sell_prices =[]
max_value_clothes = 50.00
max_value_shoes = 35.00
max_value_accessories = 20.50
sell_price_clothes = 0.00
sell_price_shoes = 0.00
sell_price_accessories = 0.00
total_sell_price_clothes = 0.00
total_sell_price_shoes = 0.00
total_sell_price_accessories = 0.00
profit = 0.00
profit_clothes = 0.00
profit_shoes = 0.00
profit_accessories = 0.00

for i in range(len(collection_of_items)):
    type_price = collection_of_items[i].split("->")
    if type_price[0] == "Clothes" and float(type_price[1]) <= max_value_clothes:
        if budget - float(type_price[1]) >= 0:
            budget -= float(type_price[1])
        else:
            continue
        sell_price_clothes = 1.40 * float(type_price[1])
        total_sell_price_clothes += sell_price_clothes
        profit_clothes += 0.40 * float(type_price[1])
        sell_prices.append(sell_price_clothes)
    elif type_price[0] == "Shoes" and float(type_price[1]) <= max_value_shoes:
        if budget - float(type_price[1]) >= 0:
            budget -= float(type_price[1])
        else:
            continue
        sell_price_shoes = 1.40 * float(type_price[1])
        total_sell_price_shoes += sell_price_shoes
        profit_shoes += 0.40 * float(type_price[1])
        sell_prices.append(sell_price_shoes)
    elif type_price[0] == "Accessories" and float(type_price[1]) <= max_value_accessories:
        if budget - float(type_price[1]) >= 0:
            budget -= float(type_price[1])
        else:
            continue
        sell_price_accessories = 1.40 * float(type_price[1])
        total_sell_price_accessories += sell_price_accessories
        profit_accessories += 0.40 * float(type_price[1])
        sell_prices.append(sell_price_accessories)

for j, string in enumerate(sell_prices):
    if (j + 1) != len(sell_prices):
        print(f"{string:.2f}", end = " ")
    else:
        print(f"{string:.2f}")

profit = profit_clothes + profit_shoes + profit_accessories

print(f"Profit: {profit:.2f}")

if (budget + total_sell_price_clothes + total_sell_price_shoes + total_sell_price_accessories) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")