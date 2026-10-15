import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2    

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter radius: "))

c2 = Circle(radius)

print("Area of circle:", round(c2.calculate_area() ))
print("Circumference of circle:", round(c2.calculate_circumference(), 2))