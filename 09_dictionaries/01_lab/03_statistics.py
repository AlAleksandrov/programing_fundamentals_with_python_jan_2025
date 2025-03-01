count_all_products = 0
sum_all_quantities = 0
bakery = {}

while True:
    command = input().split(": ")

    if command[0] == "statistics":
        print("Products in stock:")
        for product, quantity in bakery.items():
            print(f"- {product}: {quantity}")
        print(f"Total Products: {count_all_products}")
        print(f"Total Quantity: {sum_all_quantities}")
        break

    product = command[0]
    quantity = int(command[1])
    sum_all_quantities += quantity

    if product not in bakery:
        bakery[product] = quantity
        count_all_products += 1
    else:
        quantity += int(bakery[product])
        bakery[product] = quantity