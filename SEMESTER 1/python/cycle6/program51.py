from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, num_sides):
        self.num_sides = num_sides

    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
        self.length = 0
        self.breadth = 0

    def get_dimensions(self):
        self.length = float(input("Enter length of the rectangle: "))
        self.breadth = float(input("Enter breadth of the rectangle: "))

    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        self.base = 0
        self.height = 0

    def get_dimensions(self):
        self.base = float(input("Enter base length of the triangle: "))
        self.height = float(input("Enter height of the triangle: "))

    def calculate_area(self):
        return 0.5 * self.base * self.height

rectangle = Rectangle()
triangle = Triangle()

rectangle.get_dimensions()
triangle.get_dimensions()
area_rectangle = rectangle.calculate_area()
area_triangle = triangle.calculate_area()

print(f"Area of the rectangle: {area_rectangle}")
print(f"Area of the triangle: {area_triangle}")
