elements = input().split()
stock = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = elements[i + 1]
    bakery[product] = quantity

for i in range(0, len(stock)):
    product = stock[i]
    if stock[i] in bakery:
        quantity = int(bakery[product])
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")