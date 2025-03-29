def main(current_number:int):
    cars = {}
    for _ in range(current_number):
        some_cars, current_mileage, fuel_available = input().split("|")
        cars[some_cars] = {"Mileage": int(current_mileage), "Fuel": int(fuel_available)}
    while True:
        commands = input()
        if commands == "Stop":
            return cars
        commands = commands.split(" : ")
        action = commands[0]
        if action == "Drive":
            automobile, distance, fuel = commands[1], commands[2], commands[3]
            if cars[automobile]["Fuel"] < int(fuel):
                print("Not enough fuel to make that ride")
            else:
                cars[automobile]["Mileage"] += int(distance)
                cars[automobile]["Fuel"] -= int(fuel)
                print(f"{automobile} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[automobile]["Mileage"] >= 100000:
                print(f"Time to sell the {automobile}!")
                del cars[automobile]
        elif action == "Refuel":
            automobile, fuel = commands[1], commands[2]
            cars[automobile]["Fuel"] += int(fuel)
            if cars[automobile]["Fuel"] > 75:
                added_fuel = int(fuel) - (cars[automobile]["Fuel"] - 75)
                cars[automobile]["Fuel"] = 75
                print(f"{automobile} refueled with {added_fuel} liters")
            else:
                print(f"{automobile} refueled with {fuel} liters")
        elif action == "Revert":
            automobile, distance = commands[1], commands[2]
            cars[automobile]["Mileage"] -= int(distance)
            if cars[automobile]["Mileage"] < 10000:
                cars[automobile]["Mileage"] = 10000
            else:
                print(f"{automobile} mileage decreased by {distance} kilometers")


number = int(input())
result = main(number)
for car, details in result.items():
    print(f"{car} -> Mileage: {details['Mileage']} kms, Fuel in the tank: {details['Fuel']} lt.")