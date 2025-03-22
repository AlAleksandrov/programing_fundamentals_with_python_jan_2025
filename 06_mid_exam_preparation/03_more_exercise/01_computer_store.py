command = input()
total_price_without_taxes = 0.00
total_amount_of_taxes = 0.00
total_price_with_taxes = 0.00
price = 0.00

while True:
    tax_percentage = 0.20
    if command == "special":
        if total_price_without_taxes <= 0:
            print("Invalid order!")
            break
        tax_discount = 0.10
        total_price_with_taxes = total_price_without_taxes * (1 + tax_percentage)
        total_amount_of_taxes = total_price_without_taxes * (tax_percentage)
        total_price_with_taxes = total_price_with_taxes * (1 - tax_discount)
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_taxes:.2f}$")
        print(f"Taxes: {total_amount_of_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price_with_taxes:.2f}$")
        break
    elif command == "regular":
        if total_price_without_taxes <= 0:
            print("Invalid order!")
            break
        total_price_with_taxes = total_price_without_taxes * (1 + tax_percentage)
        total_amount_of_taxes = total_price_without_taxes * tax_percentage
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_taxes:.2f}$")
        print(f"Taxes: {total_amount_of_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price_with_taxes:.2f}$")
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += price

    command = input()