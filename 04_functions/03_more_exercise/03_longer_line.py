import math
coordinates = []
points = {}
count = 0

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_point_distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)
def pythagoras(current_coordinates):
    line1_length = calculate_distance(
        float(current_coordinates[1][0]), float(current_coordinates[1][1]),
        float(current_coordinates[2][0]), float(current_coordinates[2][1])
    )
    line2_length = calculate_distance(
        float(current_coordinates[3][0]), float(current_coordinates[3][1]),
        float(current_coordinates[4][0]), float(current_coordinates[4][1])
    )
    if line1_length < line2_length:
        if calculate_point_distance_from_center(float(current_coordinates[3][0]), float(current_coordinates[3][1])) <=\
                calculate_point_distance_from_center(float(current_coordinates[4][0]), float(current_coordinates[4][1])):
            return f"({math.floor(float(current_coordinates[3][0]))}, {math.floor(float(current_coordinates[3][1]))})({math.floor(float(current_coordinates[4][0]))}, {math.floor(float(current_coordinates[4][1]))})"
        else:
            return f"({math.floor(float(current_coordinates[4][0]))}, {math.floor(float(current_coordinates[4][1]))})({math.floor(float(current_coordinates[3][0]))}, {math.floor(float(current_coordinates[3][1]))})"
    else:
        if calculate_point_distance_from_center(float(current_coordinates[1][0]), float(current_coordinates[1][1])) <=\
            calculate_point_distance_from_center(float(current_coordinates[2][0]), float(current_coordinates[2][1])):
            return f"({math.floor(float(current_coordinates[1][0]))}, {math.floor(float(current_coordinates[1][1]))})({math.floor(float(current_coordinates[2][0]))}, {math.floor(float(current_coordinates[2][1]))})"
        else:
            return f"({math.floor(float(current_coordinates[2][0]))}, {math.floor(float(current_coordinates[2][1]))})({math.floor(float(current_coordinates[1][0]))}, {math.floor(float(current_coordinates[1][1]))})"


for counter in range(8):
    coordinate = float(input())
    coordinates.append(coordinate)
    if counter % 2 != 0:
        count += 1
        points[count] = coordinates
        coordinates = []
result = pythagoras(points)
print(result)