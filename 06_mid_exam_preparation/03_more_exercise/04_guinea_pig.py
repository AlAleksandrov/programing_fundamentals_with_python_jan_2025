quantity_of_food_per_month = 1000 * float(input())
quantity_of_hay_per_month = 1000 * float(input())
quantity_of_cover_per_month = 1000 * float(input())
weight_puppy = 1000 * float(input())
eats_food_per_day = 300
is_problem = False

for day in range(1, 31):
    quantity_of_food_per_month -= eats_food_per_day
    if day % 2 == 0:
        quantity_of_hay_per_month -= 0.05 * quantity_of_food_per_month
    if day % 3 == 0:
        quantity_of_cover_per_month -= 1/3 * weight_puppy
    if quantity_of_food_per_month <= 0 or quantity_of_hay_per_month <= 0 or quantity_of_cover_per_month <= 0:
        print("Merry must go to the pet store!")
        is_problem = True
        break
if not is_problem:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food_per_month/1000:.2f}, \
Hay: {quantity_of_hay_per_month/1000:.2f}, Cover: {quantity_of_cover_per_month/1000:.2f}.")