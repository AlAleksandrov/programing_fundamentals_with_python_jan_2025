class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * ((self.diameter / 2) ** 2)

current_diameter = int(input())
circle = Circle(current_diameter)
current_angle = int(input())

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(current_angle):.2f}")