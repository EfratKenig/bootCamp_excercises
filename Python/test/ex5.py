import math


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


class Square(Rectangle):
    def __init__(self, edge):
        super().__init__(edge, edge)
        self.edge = edge


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round((self.radius ** 2) * math.pi, 3)

    def calculate_perimeter(self):
        return round(2 * self.radius * math.pi, 3)


class EquilateralTriangle:
    def __init__(self, edge):
        self.edge = edge

    def calculate_area(self):
        return round(self.edge * math.sqrt(3) / 2, 3)

    def calculate_perimeter(self):
        return 3 * self.edge
