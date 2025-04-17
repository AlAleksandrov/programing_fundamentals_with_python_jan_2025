import math
coordinates = []

def pythagoras(current_coordinates):
    for index, number in enumerate(current_coordinates):
        if number.isdigit():
            current_coordinates[index] = int(number)
        else:
            current_coordinates[index] = float(number)
    if current_coordinates[0] ** 2 + current_coordinates[1] ** 2 < current_coordinates[2] ** 2 + current_coordinates[3] ** 2:
        return f"({math.floor(current_coordinates[0])}, {math.floor(current_coordinates[1])})"
    return f"({math.floor(current_coordinates[2])}, {math.floor(current_coordinates[3])})"


for _ in range(4):
    coordinate = input()
    coordinates.append(coordinate)
result = pythagoras(coordinates)
print(result)