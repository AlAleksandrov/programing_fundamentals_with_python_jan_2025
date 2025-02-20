number_of_cities = int(input())
total_profit = 0

for i in range(1, number_of_cities + 1):
    city_name = input()
    earned_money =  float(input())
    spending_money = float(input())
    if i % 5 == 0:
        earned_money *= 0.9
    elif i % 3 == 0:
        spending_money *= 1.5

    profit = earned_money - spending_money
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
    total_profit += profit

print(f"Burger Bus total profit: {total_profit:.2f} leva.")