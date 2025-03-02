products = {}
items = input()

while items != "buy":
    name, price, quantity = items.split()
    if name not in products:
        products[name] = [float(price), float(quantity)]
    else:
        products[name][0] = float(price)
        products[name][1] += float(quantity)

    items = input()


for name, price_quantity in products.items():
    total_price = products[name][0] * products[name][1]
    print(f"{name} -> {total_price:.2f}")