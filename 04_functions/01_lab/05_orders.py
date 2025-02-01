def order(product, quantity):
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    result = 0.00
    if product == "coffee":
        result = quantity * coffee
    elif product == "coke":
        result = quantity * coke
    elif product == "water":
        result = quantity * water
    elif product == "snacks":
        result = quantity * snacks
    return f"{result:.2f}"

current_product = input()
current_quantity = int(input())
total_price = order(current_product, current_quantity)
print(total_price)