class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length1 = float(input("Enter length of first rectangle: "))
breadth1 = float(input("Enter breadth of first rectangle: "))

length2 = float(input("Enter length of second rectangle: "))
breadth2 = float(input("Enter breadth of second rectangle: "))

rectangle1 = Rectangle(length1, breadth1)
rectangle2 = Rectangle(length2, breadth2)


area1 = rectangle1.area()
area2 = rectangle2.area()

if area1 > area2:
    print("Area of first rectangle is greater.")
elif area2 > area1:
    print("Area of second rectangle is greater.")
else:
    print("Both rectangles have the same area.")

print(f"\nArea of first rectangle: {area1}")
print(f"Perimeter of first rectangle: {rectangle1.perimeter()}")

print(f"\nArea of second rectangle: {area2}")
print(f"Perimeter of second rectangle: {rectangle2.perimeter()}")
